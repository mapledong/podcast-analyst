"""Expand existing summaries to meet template v4.9 / v5.3 word minimums."""

from __future__ import annotations

import json
import os
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

from openai import OpenAI

from src.duration import duration_tier, tier_limit
from src.extract import EXTRACTION_SCHEMA, _truncate_transcript
from src.extract_acquired import ACQUIRED_EXTRACTION_SCHEMA
from src.validate import validate_summary, word_count

ROOT = Path(__file__).resolve().parent.parent
PRESERVE_TOP_LEVEL = frozenset({"episode_id", "podcast", "host", "metadata", "episode_rating"})
EXPANDABLE_SECTIONS = (
    "conclusion",
    "background",
    "important_facts",
    "mental_model",
    "competitive_advantage",
    "key_insights",
    "top_investment_implications",
    "golden_quotes",
    "chronology",
    "keywords",
)


def _section_cfg(template: dict[str, Any], section_id: str) -> dict[str, Any]:
    return next((s for s in template["sections"] if s["id"] == section_id), {})


def build_expansion_brief(data: dict[str, Any], template: dict[str, Any]) -> str:
    report = validate_summary(data, template)
    duration = data.get("metadata", {}).get("duration_minutes", 60)
    tier = duration_tier(duration)
    gap = max(0, report.min_total_words - report.total_words)
    lines = [
        f"Duration: {duration} min ({tier})",
        f"Current counted words: {report.total_words}",
        f"Minimum required: {report.min_total_words}",
        f"Word gap to close: {gap}",
        "",
        "Section targets from template:",
    ]

    for section_id in (
        "important_facts",
        "mental_model",
        "key_insights",
        "conclusion",
        "background",
        "competitive_advantage",
    ):
        cfg = _section_cfg(template, section_id)
        if not cfg:
            continue
        parts: list[str] = []
        if cfg.get("min_words"):
            parts.append(f"min {cfg['min_words']} words")
        if cfg.get("max_words"):
            parts.append(f"max {cfg['max_words']} words")
        if cfg.get("item_count"):
            parts.append(f"exactly {cfg['item_count']} items")
        if parts:
            lines.append(f"- {section_id}: {', '.join(parts)}")

    lines.append("")
    lines.append("Validator warnings to fix:")
    for issue in report.issues:
        if issue.severity == "warning":
            lines.append(f"- [{issue.section}] {issue.message}")

    if gap > 0:
        lines.append("")
        lines.append(
            "Priority: deepen conclusion, important_facts, and mental_model first; "
            "then key_insights answers and competitive_advantage (Acquired only)."
        )
    return "\n".join(lines)


def _is_acquired(podcast: str | None) -> bool:
    return (podcast or "").strip() == "Acquired"


def _default_model(podcast: str | None) -> str:
    if _is_acquired(podcast):
        return os.environ.get("PODCAST_ANALYST_EXPAND_MODEL", "gpt-4.1")
    return os.environ.get("PODCAST_ANALYST_EXPAND_MODEL", "gpt-4.1-mini")


def resolve_transcript_path(data: dict[str, Any], transcripts_dir: Path | None = None) -> Path | None:
    transcripts = transcripts_dir or ROOT / "data" / "transcripts"
    episode_id = str(data.get("episode_id", ""))
    meta = data.get("metadata") or {}
    candidates: list[Path] = []

    if episode_id:
        candidates.append(transcripts / f"{episode_id}.txt")
        if episode_id.startswith("bb-"):
            candidates.append(transcripts / f"{episode_id.removeprefix('bb-')}.txt")
        if episode_id.startswith("fnd-"):
            parts = episode_id.split("-", 2)
            if len(parts) >= 3:
                candidates.append(transcripts / f"{parts[2]}.txt")

    links = meta.get("links") or {}
    colossus_url = links.get("colossus") or meta.get("colossus_url") or ""
    if "/episode/" in colossus_url:
        slug = colossus_url.rstrip("/").split("/")[-1]
        if data.get("podcast") == "Business Breakdowns":
            candidates.append(transcripts / f"bb-{slug}.txt")
        elif data.get("podcast") == "Founders":
            candidates.append(transcripts / f"fnd-{slug}.txt")

    acquired_url = links.get("acquired", "")
    if "/episodes/" in acquired_url:
        slug = acquired_url.rstrip("/").split("/")[-1]
        candidates.append(transcripts / f"acq-{slug}.txt")

    youtube = meta.get("youtube_url") or links.get("youtube", "")
    if youtube:
        try:
            from src.fetch_transcript import extract_video_id

            candidates.append(transcripts / f"{extract_video_id(youtube)}.txt")
        except ValueError:
            pass

    seen: set[str] = set()
    for path in candidates:
        key = str(path)
        if key in seen:
            continue
        seen.add(key)
        if path.exists() and path.stat().st_size > 1000:
            return path
    return None


def load_transcript_text(path: Path) -> str:
    text = path.read_text(encoding="utf-8")
    if text.startswith("# video_id:"):
        text = text.split("\n\n", 1)[-1]
    return text.strip()


def merge_expanded_summary(
    original: dict[str, Any],
    expanded: dict[str, Any],
    *,
    model: str,
) -> dict[str, Any]:
    merged: dict[str, Any] = {}
    for key in PRESERVE_TOP_LEVEL:
        if key in original:
            merged[key] = original[key]

    for key in EXPANDABLE_SECTIONS:
        if key in expanded:
            merged[key] = expanded[key]
        elif key in original:
            merged[key] = original[key]

    prior_notes = str(original.get("review_notes", "")).strip()
    merged["review_notes"] = f"{prior_notes} | expanded {model}".strip(" |")

    meta = dict(original.get("extraction_meta") or {})
    meta.update(
        {
            "expanded_by": model,
            "expanded_at": datetime.now(timezone.utc).isoformat(),
            "status": meta.get("status", "approved"),
        }
    )
    merged["extraction_meta"] = meta
    return merged


def expand_summary(
    data: dict[str, Any],
    transcript: str,
    template: dict[str, Any],
    *,
    model: str | None = None,
    prompts_dir: Path | None = None,
) -> dict[str, Any]:
    from src.env import load_dotenv

    load_dotenv()
    api_key = os.environ.get("OPENAI_API_KEY")
    if not api_key:
        raise RuntimeError("OPENAI_API_KEY not set")

    podcast = data.get("podcast", "")
    acquired = _is_acquired(podcast)
    prompts_dir = prompts_dir or ROOT / "prompts"
    prompt_name = "expansion_acquired.txt" if acquired else "expansion_iltb.txt"
    system_prompt = (prompts_dir / prompt_name).read_text(encoding="utf-8")
    model = model or _default_model(podcast)
    schema = ACQUIRED_EXTRACTION_SCHEMA if acquired else EXTRACTION_SCHEMA

    meta = data.get("metadata") or {}
    brief = build_expansion_brief(data, template)
    summary_json = json.dumps(
        {k: data[k] for k in EXPANDABLE_SECTIONS if k in data}
        | {"episode_rating": data.get("episode_rating", {})},
        indent=2,
        ensure_ascii=False,
    )

    user_prompt = (
        f"Podcast: {podcast}\n"
        f"Episode: {meta.get('episode_number')} — {meta.get('title')}\n"
        f"Guest/Subject: {meta.get('guest')} ({meta.get('guest_role', '')})\n"
        f"Duration: {meta.get('duration_minutes')} minutes\n\n"
        f"EXPANSION BRIEF:\n{brief}\n\n"
        f"CURRENT SUMMARY (expand these sections; do not shorten existing good content):\n"
        f"{summary_json}\n\n"
        f"TRANSCRIPT:\n{_truncate_transcript(transcript)}"
    )

    client = OpenAI(api_key=api_key)
    response = client.responses.create(
        model=model,
        input=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_prompt},
        ],
        text={
            "format": {
                "type": "json_schema",
                "name": "expanded_podcast_summary",
                "schema": schema,
                "strict": True,
            }
        },
    )

    expanded = json.loads(response.output_text)
    return merge_expanded_summary(data, expanded, model=model)


def section_word_counts(data: dict[str, Any], template: dict[str, Any]) -> dict[str, int]:
    counts: dict[str, int] = {}
    for section_id in ("conclusion", "background", "competitive_advantage"):
        counts[section_id] = word_count(str(data.get(section_id, "")))

    counts["important_facts"] = word_count(" ".join(data.get("important_facts", [])))
    mm = data.get("mental_model") or {}
    counts["mental_model"] = word_count(
        " ".join(str(mm.get(k, "")) for k in ("name", "components", "application"))
    )
    counts["key_insights"] = word_count(
        " ".join(
            " ".join(item.get(k, "") for k in ("view", "question", "answer"))
            for item in data.get("key_insights", [])
        )
    )
    report = validate_summary(data, template)
    counts["total"] = report.total_words
    counts["min_total"] = report.min_total_words
    return counts
