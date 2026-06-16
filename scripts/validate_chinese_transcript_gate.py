#!/usr/bin/env python3
"""Hard gate: all Chinese episodes must have adequate transcripts before publish."""

from __future__ import annotations

import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))

from src.chinese_transcript import CHINESE_EPISODE_IDS, require_transcript_gate  # noqa: E402

APPROVED_EN = ROOT / "data" / "approved"
APPROVED_ZH = ROOT / "data" / "approved" / "zh"


def main() -> None:
    import argparse

    parser = argparse.ArgumentParser()
    parser.add_argument("ids", nargs="*", help="Episode IDs (default: all 30 Chinese)")
    parser.add_argument("--no-quotes", action="store_true", help="Skip golden-quote verification")
    args = parser.parse_args()

    ids = args.ids or list(CHINESE_EPISODE_IDS)
    failed: list[str] = []
    for eid in ids:
        en_path = APPROVED_EN / f"{eid}.json"
        zh_path = APPROVED_ZH / f"{eid}.json"
        if not en_path.exists() or not zh_path.exists():
            print(f"FAIL {eid}: missing approved JSON")
            failed.append(eid)
            continue
        en = json.loads(en_path.read_text(encoding="utf-8"))
        zh = json.loads(zh_path.read_text(encoding="utf-8"))
        duration = int(en.get("metadata", {}).get("duration_minutes", 60))
        try:
            require_transcript_gate(
                eid,
                duration_minutes=duration,
                data=zh,
                check_quotes=not args.no_quotes,
            )
            require_transcript_gate(
                eid,
                duration_minutes=duration,
                data=en,
                check_quotes=False,
            )
            print(f"OK {eid}")
        except RuntimeError as exc:
            print(f"FAIL {eid}: {exc}")
            failed.append(eid)

    if failed:
        print(f"\nGate failed for {len(failed)} episode(s)")
        raise SystemExit(1)
    print(f"\nAll {len(ids)} episode(s) passed transcript gate")


if __name__ == "__main__":
    main()
