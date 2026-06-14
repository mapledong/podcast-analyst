#!/usr/bin/env python3
"""Pre-fetch YouTube transcripts for discovered ILTB episodes."""

from __future__ import annotations

import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))

from src.fetch_transcript import extract_video_id, fetch_transcript, save_transcript  # noqa: E402

DISCOVERED = ROOT / "data" / "discovered" / "iltb_episodes.json"
SKIP = {"ep475", "ep476", "ep477"}


def main() -> None:
    data = json.loads(DISCOVERED.read_text(encoding="utf-8"))
    ok, skip, fail = 0, 0, 0
    for ep in data["episodes"]:
        eid = ep.get("id")
        yt = ep.get("youtube_url", "")
        if not eid or eid in SKIP or not yt:
            skip += 1
            continue
        vid = extract_video_id(yt)
        tpath = ROOT / "data" / "transcripts" / f"{vid}.txt"
        if tpath.exists():
            skip += 1
            continue
        try:
            result = fetch_transcript(yt)
            save_transcript(result, ROOT / "data" / "transcripts")
            print(f"✓ {eid} ({result.line_count} lines)")
            ok += 1
        except Exception as exc:
            print(f"✗ {eid}: {exc}")
            fail += 1
    print(f"\nFetched: {ok} | skipped: {skip} | failed: {fail}")


if __name__ == "__main__":
    main()
