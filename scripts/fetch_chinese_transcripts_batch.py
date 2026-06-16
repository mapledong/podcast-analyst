#!/usr/bin/env python3
"""Try YouTube captions for all Chinese episodes (preferred accuracy source)."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))

from src.chinese_transcript import CHINESE_EPISODE_IDS, assess_transcript, is_youtube_transcript  # noqa: E402

APPROVED = ROOT / "data" / "approved"
FETCH = ROOT / "scripts" / "fetch_chinese_transcript.py"


def _youtube_url(episode_id: str) -> str:
    data = json.loads((APPROVED / f"{episode_id}.json").read_text(encoding="utf-8"))
    meta = data.get("metadata") or {}
    links = meta.get("links") or {}
    return str(meta.get("youtube_url") or links.get("youtube") or "").strip()


def main() -> None:
    import argparse

    parser = argparse.ArgumentParser(description="Fetch YouTube captions for Chinese episodes")
    parser.add_argument("ids", nargs="*", help="Episode IDs (default: all 30)")
    parser.add_argument("--force", action="store_true", help="Fetch even if YouTube transcript exists")
    args = parser.parse_args()

    ids = args.ids or list(CHINESE_EPISODE_IDS)
    ok = skipped = failed = 0

    for eid in ids:
        duration = int(
            json.loads((APPROVED / f"{eid}.json").read_text(encoding="utf-8"))
            .get("metadata", {})
            .get("duration_minutes", 60)
        )
        tx = assess_transcript(eid, duration_minutes=duration)
        if tx["is_youtube"] and not args.force:
            print(f"skip {eid}: already has YouTube transcript ({tx['source']})")
            skipped += 1
            continue

        url = _youtube_url(eid)
        if not url:
            print(f"skip {eid}: no youtube_url")
            skipped += 1
            continue

        print(f"fetch {eid} …")
        proc = subprocess.run(
            [sys.executable, str(FETCH), url, "--slug", eid],
            capture_output=True,
            text=True,
        )
        if proc.returncode != 0:
            print(f"FAIL {eid}: captions unavailable")
            failed += 1
            continue

        tx = assess_transcript(eid, duration_minutes=duration)
        print(f"OK {eid}: {tx['source']} ({tx['lines']} lines)")
        ok += 1

    print(f"\nDone: {ok} fetched, {skipped} skipped, {failed} unavailable")


if __name__ == "__main__":
    main()
