#!/usr/bin/env python3
"""Normalize company names to canonical tickers in approved summary JSON."""

from __future__ import annotations

import argparse
import json
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))

from src.company_tickers import (  # noqa: E402
    normalize_investment_ticker,
    normalize_keywords,
)

APPROVED_DIR = ROOT / "data" / "approved"


def normalize_summary(data: dict) -> tuple[dict, list[str]]:
    changes: list[str] = []
    out = dict(data)

    keywords, kw_changes = normalize_keywords(data.get("keywords") or [])
    if kw_changes:
        out["keywords"] = keywords
        for old, new in kw_changes:
            changes.append(f"keywords: {old!r} → {new!r}")

    clues = data.get("top_investment_implications") or []
    new_clues: list[dict] = []
    clues_changed = False
    for row in clues:
        row_out = dict(row)
        new_ticker, changed = normalize_investment_ticker(str(row.get("ticker", "")))
        if changed:
            row_out["ticker"] = new_ticker
            clues_changed = True
            changes.append(f"ticker: {row.get('ticker')!r} → {new_ticker!r}")
        new_clues.append(row_out)
    if clues_changed:
        out["top_investment_implications"] = new_clues

    return out, changes


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("episode_ids", nargs="*", help="Specific episode IDs (default: all approved)")
    parser.add_argument("--dry-run", action="store_true", help="Report changes without writing")
    parser.add_argument("--publish", action="store_true", help="Publish changed episodes after normalize")
    parser.add_argument("--sync-web", action="store_true", help="Sync web catalog after publish")
    args = parser.parse_args()

    if args.episode_ids:
        paths = [APPROVED_DIR / f"{eid}.json" for eid in args.episode_ids]
    else:
        paths = sorted(APPROVED_DIR.glob("*.json"), key=lambda p: p.stem)

    changed_ids: list[str] = []
    total_changes = 0

    for path in paths:
        if not path.exists() or path.stem == "batch_state":
            continue
        data = json.loads(path.read_text(encoding="utf-8"))
        normalized, changes = normalize_summary(data)
        if not changes:
            continue

        total_changes += len(changes)
        changed_ids.append(path.stem)
        print(f"{path.stem}:")
        for change in changes:
            print(f"  {change}")

        if not args.dry_run:
            path.write_text(json.dumps(normalized, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")

    print(f"\n{len(changed_ids)} summaries with {total_changes} changes")
    if args.dry_run or not changed_ids:
        return 0

    if args.publish:
        cmd = [sys.executable, str(ROOT / "scripts/publish_approved_batch.py"), *changed_ids]
        subprocess.run(cmd, check=True)

    if args.sync_web:
        subprocess.run(["node", str(ROOT / "web/scripts/sync-content.mjs")], cwd=str(ROOT / "web"), check=True)

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
