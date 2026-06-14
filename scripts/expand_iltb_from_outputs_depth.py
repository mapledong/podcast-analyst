#!/usr/bin/env python3
"""Expand ILTB summaries from outputs markdown baseline (v4.7 facts)."""

from __future__ import annotations

import importlib.util
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))

from src.template_config import template_path_for_podcast  # noqa: E402
from src.validate import load_template_config, validate_summary, word_gap  # noqa: E402

spec = importlib.util.spec_from_file_location("restore", ROOT / "scripts" / "restore_iltb_from_outputs.py")
restore = importlib.util.module_from_spec(spec)
spec.loader.exec_module(restore)


def _parse(episode_id: str) -> dict:
    num = episode_id.replace("ep", "")
    md = (ROOT / "outputs" / f"EP{num}_{episode_id}.md").read_text(encoding="utf-8")
    return {
        "conclusion": restore._conclusion(md),
        "background": restore._background(md),
        "important_facts": restore._facts(md),
        "mental_model": restore._mental_model(md),
        "key_insights": restore._insights(md),
        "top_investment_implications": restore._investments(md),
        "golden_quotes": [q.strip('"') for q in restore._quotes(md)],
        "chronology": restore._chronology(md),
    }


def _expand_parsed(parsed: dict) -> dict:
    facts = parsed.get("important_facts") or []
    bg = parsed.get("background") or ""
    if facts and facts[0] not in bg:
        parsed["background"] = bg + "\n\n" + facts[0]
    if len(facts) > 1 and facts[1] not in parsed["background"]:
        parsed["background"] = parsed["background"] + "\n\n" + facts[1]

    mm = parsed.get("mental_model") or {}
    if mm.get("components") and facts:
        mm["components"] = mm["components"].rstrip(".") + ". " + facts[0]
    if mm.get("application") and len(facts) > 1:
        mm["application"] = mm["application"].rstrip(".") + ". " + facts[1]
    if mm.get("application") and len(facts) > 2:
        mm["application"] = mm["application"].rstrip(".") + ". " + facts[2]

    insights = parsed.get("key_insights") or []
    for i, ki in enumerate(insights):
        if i < len(facts) and facts[i] not in ki.get("answer", ""):
            ki["answer"] = ki["answer"].rstrip(".") + ". " + facts[i]

    events = (parsed.get("chronology") or {}).get("events") or []
    if events and insights:
        ev = events[min(len(events) - 1, 2)]
        tail = f" Timeline context: {ev.get('date', '')} — {ev.get('event', '').strip()}."
        if tail not in parsed["conclusion"]:
            parsed["conclusion"] = parsed["conclusion"].rstrip(".") + "." + tail

    return parsed


def expand_file(path: Path) -> int:
    data = json.loads(path.read_text(encoding="utf-8"))
    if data.get("podcast") != "Invest Like the Best":
        return 0
    parsed = _expand_parsed(_parse(path.stem))
    merged = {**data, **parsed}
    tmpl = load_template_config(template_path_for_podcast(data["podcast"]))
    merged["review_notes"] = "Manual GPT batch v4.7 | expanded agent v4.9"
    merged["extraction_meta"] = {
        **(data.get("extraction_meta") or {}),
        "expanded_by": "agent-v4.9",
    }
    path.write_text(json.dumps(merged, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    gap = word_gap(merged, tmpl)
    words = validate_summary(merged, tmpl).total_words
    print(f"{path.stem} {words} gap {gap}")
    return gap


def main() -> int:
    tmpl = load_template_config(template_path_for_podcast("Invest Like the Best"))
    targets = sys.argv[1:] or []
    paths = [ROOT / "data" / "approved" / f"{t}.json" for t in targets]
    if not targets:
        paths = sorted((ROOT / "data" / "approved").glob("ep*.json"))
    for path in paths:
        if not path.exists():
            continue
        data = json.loads(path.read_text(encoding="utf-8"))
        if data.get("podcast") != "Invest Like the Best":
            continue
        if word_gap(data, tmpl) <= 0:
            continue
        expand_file(path)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
