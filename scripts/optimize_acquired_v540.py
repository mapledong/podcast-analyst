#!/usr/bin/env python3
"""Deterministic Acquired summary cleanup (prose, dedupe, section trims). No LLM padding."""

from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))

from src.render import render_summary, save_summary  # noqa: E402
from src.template_config import template_path_for_podcast  # noqa: E402
from src.validate import load_template_config, validate_summary, word_count  # noqa: E402

APPROVED = ROOT / "data" / "approved"
OUTPUTS = ROOT / "outputs"
TEMPLATES = ROOT / "templates"
TMPL = load_template_config(template_path_for_podcast("Acquired"))

JUNK_PATTERNS = (
    re.compile(r'\s*Transcript line\s*:\s*"[^"]*"\s*', re.I),
    re.compile(r"\s*Transcript line\s*:\s*[^.!?]+[.!?]?", re.I),
    re.compile(r"\s*Transcript detail[^.]*\.", re.I),
    re.compile(r"\s*This maps to [^.]+\.", re.I),
    re.compile(r"\s*Related data point[^.]*\.", re.I),
    re.compile(r"\s*Hosts (?:note|stress)[^.]*\.", re.I),
)

AI_PHRASES = (
    re.compile(r"\bit['']s worth noting\b", re.I),
    re.compile(r"\bmoreover\b", re.I),
    re.compile(r"\bfurthermore\b", re.I),
    re.compile(r"\bdelve\b", re.I),
    re.compile(r"\bunderscores?\b", re.I),
    re.compile(r"\bat its core\b", re.I),
)

SECTION_LIMITS = {
    "background": 300,
    "conclusion": 180,
    "competitive_advantage": 580,
}


def clean_text(text: str) -> str:
    if not text:
        return ""
    out = str(text)
    for pat in JUNK_PATTERNS + AI_PHRASES:
        out = pat.sub(" ", out)
    return re.sub(r"\s+", " ", out).strip()


def _truncate_words(text: str, max_words: int) -> str:
    words = text.split()
    if len(words) <= max_words:
        return text.strip()
    return " ".join(words[:max_words]).rstrip(".,;:") + "."


def _norm_sentence(s: str) -> str:
    return re.sub(r"\s+", " ", s.strip().lower())


def _sentences(text: str) -> list[str]:
    return [p.strip() for p in re.split(r"(?<=[.!?])\s+", clean_text(text)) if p.strip()]


def dedupe_sentences(text: str, seen: set[str], *, min_words: int = 10) -> str:
    kept: list[str] = []
    for sent in _sentences(text):
        key = _norm_sentence(sent)
        if len(key.split()) >= min_words and key in seen:
            continue
        if len(key.split()) >= min_words:
            seen.add(key)
        kept.append(sent)
    return " ".join(kept)


def optimize_data(data: dict) -> tuple[dict, list[str]]:
    notes: list[str] = []
    seen: set[str] = set()

    for key in ("conclusion", "background", "competitive_advantage"):
        raw = str(data.get(key, ""))
        cleaned = clean_text(raw)
        if cleaned != raw:
            notes.append(f"cleaned {key}")
        max_w = SECTION_LIMITS.get(key)
        if max_w and word_count(cleaned) > max_w:
            cleaned = _truncate_words(cleaned, max_w)
            notes.append(f"trimmed {key}")
        data[key] = dedupe_sentences(cleaned, seen)

    facts = [clean_text(f) for f in data.get("important_facts", [])]
    facts = [dedupe_sentences(f, seen) for f in facts if f]
    if facts != data.get("important_facts"):
        notes.append("cleaned facts")
    data["important_facts"] = facts

    mm = dict(data.get("mental_model") or {})
    for part in ("name", "components", "application"):
        val = clean_text(str(mm.get(part, "")))
        val = dedupe_sentences(val, seen)
        if max_w := SECTION_LIMITS.get("mental_model"):
            pass
        if part != "name" and word_count(val) > 520:
            val = _truncate_words(val, 520)
            notes.append(f"trimmed mental_model.{part}")
        mm[part] = val
    data["mental_model"] = mm

    insights = []
    for item in data.get("key_insights", []):
        insights.append(
            {
                "view": clean_text(item.get("view", "")),
                "question": clean_text(item.get("question", "")),
                "answer": dedupe_sentences(clean_text(item.get("answer", "")), seen),
            }
        )
    if insights:
        data["key_insights"] = insights
        notes.append("cleaned insights")

    for clue in data.get("top_investment_implications", []):
        clue["thesis"] = clean_text(clue.get("thesis", ""))

    data["golden_quotes"] = [clean_text(q) for q in data.get("golden_quotes", []) if clean_text(q)]

    prior = str(data.get("review_notes", "")).strip()
    if notes and "optimized v5.4" not in prior:
        data["review_notes"] = f"{prior} | optimized v5.4".strip(" |")

    return data, notes


def main() -> int:
    parser = argparse.ArgumentParser(description="Deterministic Acquired summary cleanup.")
    parser.add_argument("ids", nargs="*", help="Episode IDs (default: all acq-*.json)")
    parser.add_argument("--publish", action="store_true", help="Re-render outputs markdown")
    args = parser.parse_args()

    paths = (
        [APPROVED / f"{eid}.json" for eid in args.ids]
        if args.ids
        else sorted(APPROVED.glob("acq-*.json"))
    )

    changed = 0
    for path in paths:
        if not path.exists():
            continue
        data = json.loads(path.read_text(encoding="utf-8"))
        before = validate_summary(data, TMPL)
        optimized, notes = optimize_data(data)
        after = validate_summary(optimized, TMPL)
        if notes:
            path.write_text(json.dumps(optimized, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
            changed += 1
            if args.publish:
                ep_num = optimized.get("metadata", {}).get("episode_number", path.stem)
                md = render_summary(optimized, TEMPLATES, template_cfg=TMPL)
                save_summary(md, OUTPUTS / f"EP{ep_num}_{path.stem}.md")
            print(
                f"{path.stem}: {before.total_words}→{after.total_words} words, "
                f"warnings {sum(1 for i in before.issues if i.severity=='warning')}→"
                f"{sum(1 for i in after.issues if i.severity=='warning')} ({', '.join(notes[:3])})"
            )

    print(f"\nOptimized {changed}/{len(paths)} episodes")
    if args.publish and changed:
        import subprocess

        subprocess.run(["node", str(ROOT / "web" / "scripts" / "sync-content.mjs")], cwd=str(ROOT / "web"), check=False)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
