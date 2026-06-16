#!/usr/bin/env python3
"""Re-transcribe Chinese episodes: YouTube captions first, else Whisper on audio."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))

from src.chinese_transcript import (  # noqa: E402
    CHINESE_EPISODE_IDS,
    assess_transcript,
    transcript_path,
)

APPROVED = ROOT / "data" / "approved"
SCRIPTS = ROOT / "scripts"


def _youtube_url(episode_id: str) -> str:
    data = json.loads((APPROVED / f"{episode_id}.json").read_text(encoding="utf-8"))
    meta = data.get("metadata") or {}
    links = meta.get("links") or {}
    return str(meta.get("youtube_url") or links.get("youtube") or "").strip()


def _retranscribe_one(episode_id: str, *, force: bool = True) -> str:
    url = _youtube_url(episode_id)
    if url:
        fetch = subprocess.run(
            [
                sys.executable,
                str(SCRIPTS / "fetch_chinese_transcript.py"),
                url,
                "--slug",
                episode_id,
            ],
            capture_output=True,
            text=True,
        )
        if fetch.returncode == 0:
            return "youtube"

    m4a_config = ROOT / "config" / "chinese_episode_m4a_urls.json"
    episodes = json.loads(m4a_config.read_text(encoding="utf-8"))
    if episode_id not in episodes:
        raise RuntimeError(f"{episode_id}: no m4a URL in {m4a_config.name} and YouTube fetch failed")

    whisper = subprocess.run(
        [
            sys.executable,
            str(SCRIPTS / "transcribe_m4a_batch.py"),
            "small",
            episode_id,
            "--force",
        ],
        capture_output=True,
        text=True,
    )
    if whisper.returncode == 0:
        return "whisper-small-m4a"

    raise RuntimeError(
        f"{episode_id}: youtube fetch, youtube whisper, and m4a whisper failed\n"
        f"fetch: {fetch.stderr or fetch.stdout}\n"
        f"whisper: {whisper.stderr or whisper.stdout}"
    )


def main() -> None:
    import argparse

    parser = argparse.ArgumentParser()
    parser.add_argument("ids", nargs="*", help="Episode IDs (default: all failing gate)")
    parser.add_argument("--all", action="store_true", help="Process all 30 Chinese episodes")
    args = parser.parse_args()

    if args.all:
        ids = list(CHINESE_EPISODE_IDS)
    elif args.ids:
        ids = args.ids
    else:
        ids = []
        for eid in CHINESE_EPISODE_IDS:
            data = json.loads((APPROVED / f"{eid}.json").read_text(encoding="utf-8"))
            duration = int(data.get("metadata", {}).get("duration_minutes", 60))
            if not assess_transcript(eid, duration_minutes=duration)["ok"]:
                ids.append(eid)

    print(f"Re-transcribing {len(ids)} episode(s)…")
    for eid in ids:
        print(f"\n=== {eid} ===")
        try:
            source = _retranscribe_one(eid)
            tx = assess_transcript(
                eid,
                duration_minutes=int(
                    json.loads((APPROVED / f"{eid}.json").read_text(encoding="utf-8"))
                    .get("metadata", {})
                    .get("duration_minutes", 60)
                ),
            )
            print(f"done {eid} via {source}: {tx['lines']} lines, ok={tx['ok']}")
            if tx["issues"]:
                for issue in tx["issues"]:
                    print(f"  still: {issue}")
        except Exception as exc:
            print(f"FAIL {eid}: {exc}")


if __name__ == "__main__":
    main()
