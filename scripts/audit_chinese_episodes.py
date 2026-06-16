#!/usr/bin/env python3
"""Audit Chinese podcast episodes: transcript quality and quote grounding."""

from __future__ import annotations

import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))

from src.chinese_transcript import (  # noqa: E402
    CHINESE_EPISODE_IDS,
    assess_summary_quotes,
    assess_transcript,
    load_transcript_body,
    transcript_path,
)
from src.validate import load_template_config, validate_summary  # noqa: E402
from src.template_config import template_path_for_podcast  # noqa: E402

APPROVED_EN = ROOT / "data" / "approved"
APPROVED_ZH = ROOT / "data" / "approved" / "zh"


def _load_json(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def audit_episode(episode_id: str) -> dict:
    en_path = APPROVED_EN / f"{episode_id}.json"
    zh_path = APPROVED_ZH / f"{episode_id}.json"
    row: dict = {"episode_id": episode_id, "issues": [], "warnings": []}

    if not en_path.exists() or not zh_path.exists():
        row["issues"].append("missing approved zh/en JSON")
        return row

    en = _load_json(en_path)
    zh = _load_json(zh_path)
    duration = int(en.get("metadata", {}).get("duration_minutes", 60))

    tx = assess_transcript(episode_id, duration_minutes=duration)
    row["transcript"] = tx
    row["issues"].extend(tx["issues"])
    row["warnings"].extend(tx.get("warnings", []))

    template = load_template_config(template_path_for_podcast(en.get("podcast", "")))
    for locale, data in (("en", en), ("zh", zh)):
        report = validate_summary(data, template)
        for issue in report.issues:
            if issue.severity == "error":
                row["issues"].append(f"{locale} validate: {issue.message}")

    if tx["exists"]:
        body = load_transcript_body(transcript_path(episode_id))
        for locale, data in (("zh", zh), ("en", en)):
            quote_issues = assess_summary_quotes(data, body)
            for q in quote_issues:
                if locale == "zh":
                    row["issues"].append(q)
                else:
                    row["warnings"].append(q)

    row["ok"] = not row["issues"]
    return row


def main() -> None:
    rows = [audit_episode(eid) for eid in CHINESE_EPISODE_IDS]
    ok = sum(1 for r in rows if r["ok"])
    print(f"Chinese episode audit: {ok}/{len(rows)} passed\n")
    for row in rows:
        status = "PASS" if row["ok"] else "FAIL"
        tx = row.get("transcript", {})
        src = tx.get("source", "—")
        lines = tx.get("lines", 0)
        print(f"[{status}] {row['episode_id']}  transcript={src} lines={lines}")
        for issue in row["issues"]:
            print(f"  ERROR: {issue}")
        for warning in row["warnings"]:
            print(f"  warn: {warning}")

    failed = [r["episode_id"] for r in rows if not r["ok"]]
    if failed:
        print(f"\nFailed ({len(failed)}): {', '.join(failed)}")
        raise SystemExit(1)


if __name__ == "__main__":
    main()
