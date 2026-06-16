"""Transcript requirements for Chinese podcast summaries.

Accuracy policy: summaries must be grounded in a primary source text on disk.
Preferred source order:
  1. YouTube captions (manual or auto) — no audio transcription needed
  2. Whisper on audio (m4a/YouTube) — only when captions are unavailable

The hard gate checks source presence, minimum length, and (for zh) quote grounding.
Whisper model tier is advisory (audit warning), not a publish blocker.
"""

from __future__ import annotations

import re
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parent.parent
TRANSCRIPTS_DIR = ROOT / "data" / "transcripts"

CHINESE_EPISODE_IDS: tuple[str, ...] = (
    "zj-ep136",
    "zj-ep137",
    "zj-ep138",
    "zj-ep139",
    "zj-ep140",
    "zj-ep141",
    "zj-ep142",
    "zj-ep143",
    "zj-ep144",
    "zj-ep145",
    "zj-ep121",
    "zj-ep120",
    "zj-ep109",
    "zj-ep104",
    "zj-ep83",
    "tzs-ep178",
    "tzs-ep181",
    "tzs-ep182",
    "tzs-ep183",
    "tzs-ep179",
    "tzs-ep180",
    "tzs-ep184",
    "tzs-ep185",
    "tzs-ep186",
    "tzs-ep187",
    "tzs-ep176",
    "tzs-ep170",
    "tzs-ep167",
    "tzs-ep158",
    "tzs-ep126",
)

CHINESE_PODCAST_NAMES = frozenset(
    {
        "Zhang Xiaojun Podcast",
        "张小珺商业访谈录",
        "Practical Investments",
        "投资实战派",
    }
)

# ~12 lines/min is a conservative floor for Chinese interview audio.
LINES_PER_MINUTE_MIN = 12
ABSOLUTE_MIN_LINES = 400


def is_chinese_episode_id(episode_id: str) -> bool:
    return episode_id in CHINESE_EPISODE_IDS or episode_id.startswith(("zj-ep", "tzs-ep"))


def is_chinese_podcast_data(data: dict[str, Any]) -> bool:
    podcast = str(data.get("podcast", ""))
    episode_id = str(data.get("episode_id", ""))
    return podcast in CHINESE_PODCAST_NAMES or is_chinese_episode_id(episode_id)


def transcript_path(episode_id: str) -> Path:
    return TRANSCRIPTS_DIR / f"{episode_id}.txt"


def _parse_header(path: Path) -> dict[str, str]:
    meta: dict[str, str] = {}
    for line in path.read_text(encoding="utf-8", errors="replace").splitlines()[:12]:
        if not line.startswith("#"):
            break
        if ":" in line:
            key, _, value = line[2:].partition(":")
            meta[key.strip()] = value.strip()
    return meta


def load_transcript_body(path: Path) -> str:
    text = path.read_text(encoding="utf-8", errors="replace")
    if text.startswith("#"):
        parts = text.split("\n\n", 1)
        return parts[1] if len(parts) > 1 else ""
    return text


def transcript_line_count(path: Path) -> int:
    body = load_transcript_body(path)
    return len([ln for ln in body.splitlines() if ln.strip()])


def transcript_source(path: Path) -> str:
    head = path.read_text(encoding="utf-8", errors="replace")[:300]
    if "# source: whisper-tiny" in head or "# source: whisper/tiny" in head:
        return "whisper-tiny"
    if "# source: whisper-small" in head or "# source: whisper/small" in head:
        return "whisper-small"
    if "# source: whisper-base" in head or "# source: whisper/base" in head:
        return "whisper-base"
    if "# video_id:" in head:
        caption_source = "manual"
        lang = "unknown"
        for line in head.splitlines():
            if line.startswith("# language:"):
                lang = line.split(":", 1)[1].strip()
            if line.startswith("# source:"):
                caption_source = line.split(":", 1)[1].strip()
        return f"youtube-{lang}-{caption_source}"
    meta = _parse_header(path)
    return meta.get("source", "unknown")


def is_youtube_transcript(source: str) -> bool:
    return source.startswith("youtube-")


def source_quality_warnings(source: str) -> list[str]:
    """Advisory notes — do not block publish."""
    warnings: list[str] = []
    if source == "whisper-tiny":
        warnings.append(
            "whisper-tiny source is error-prone; prefer YouTube captions when available"
        )
    elif source.startswith("youtube-") and source.endswith("-auto"):
        warnings.append("YouTube auto-captions may have errors; spot-check key facts")
    return warnings


def min_lines_for_duration(duration_minutes: int) -> int:
    return max(ABSOLUTE_MIN_LINES, int(duration_minutes) * LINES_PER_MINUTE_MIN)


def _normalize_for_match(text: str) -> str:
    lowered = text.lower()
    return re.sub(r"[\s\W_]+", "", lowered)


def quote_supported_in_transcript(quote: str, transcript: str, *, min_ratio: float = 0.55) -> bool:
    quote = quote.strip()
    if not quote or quote in {"占位", "placeholder"}:
        return False
    normalized_quote = _normalize_for_match(quote)
    if len(normalized_quote) < 6:
        return True
    normalized_transcript = _normalize_for_match(transcript)
    if normalized_quote in normalized_transcript:
        return True
    idx = 0
    matched = 0
    for ch in normalized_quote:
        found = normalized_transcript.find(ch, idx)
        if found >= 0:
            matched += 1
            idx = found + 1
    return (matched / len(normalized_quote)) >= min_ratio


def assess_transcript(episode_id: str, *, duration_minutes: int | None = None) -> dict[str, Any]:
    path = transcript_path(episode_id)
    result: dict[str, Any] = {
        "episode_id": episode_id,
        "path": str(path),
        "exists": path.exists(),
        "source": None,
        "lines": 0,
        "min_lines": min_lines_for_duration(duration_minutes or 60),
        "adequate_lines": False,
        "is_youtube": False,
        "ok": False,
        "issues": [],
        "warnings": [],
    }
    if not path.exists():
        result["issues"].append("missing transcript — fetch YouTube captions or transcribe audio")
        return result

    result["source"] = transcript_source(path)
    result["lines"] = transcript_line_count(path)
    result["adequate_lines"] = result["lines"] >= result["min_lines"]
    result["is_youtube"] = is_youtube_transcript(result["source"])
    result["warnings"].extend(source_quality_warnings(result["source"]))

    if not result["adequate_lines"]:
        result["issues"].append(
            f"transcript too short: {result['lines']} lines < {result['min_lines']} required"
        )

    result["ok"] = not result["issues"]
    return result


def assess_summary_quotes(data: dict[str, Any], transcript: str) -> list[str]:
    issues: list[str] = []
    locale = "zh" if data.get("podcast") in {"张小珺商业访谈录", "投资实战派"} else "en"
    quotes = data.get("golden_quotes") or []
    for i, quote in enumerate(quotes, start=1):
        if not quote_supported_in_transcript(str(quote), transcript):
            issues.append(f"{locale} golden_quote[{i}] not supported by transcript")
    return issues


def require_transcript_gate(
    episode_id: str,
    *,
    duration_minutes: int,
    data: dict[str, Any] | None = None,
    check_quotes: bool = True,
) -> None:
    assessment = assess_transcript(episode_id, duration_minutes=duration_minutes)
    if not assessment["ok"]:
        raise RuntimeError(
            f"{episode_id}: accuracy gate failed — {'; '.join(assessment['issues'])}"
        )

    if check_quotes and data is not None:
        podcast = str(data.get("podcast", ""))
        if podcast not in {"张小珺商业访谈录", "投资实战派"}:
            return
        path = transcript_path(episode_id)
        body = load_transcript_body(path)
        quote_issues = assess_summary_quotes(data, body)
        if quote_issues:
            raise RuntimeError(
                f"{episode_id}: quote verification failed — {'; '.join(quote_issues)}"
            )
