#!/usr/bin/env python3
"""Orchestrate curated BB/Founders library build: discover → YouTube → transcribe → report."""

from __future__ import annotations

import argparse
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
PY = sys.executable


def main() -> None:
    parser = argparse.ArgumentParser(description="BB/Founders curated library pipeline")
    parser.add_argument("--discover", action="store_true", help="Refresh RSS episode list")
    parser.add_argument("--youtube", action="store_true", help="Fetch YouTube URLs + transcripts for curated")
    parser.add_argument("--transcribe", action="store_true", help="Whisper from cache (YouTube-linked only by default)")
    parser.add_argument("--report", action="store_true")
    parser.add_argument("--sync", action="store_true")
    parser.add_argument(
        "--include-non-youtube",
        action="store_true",
        help="With --transcribe: also Whisper non-YouTube curated episodes",
    )
    args = parser.parse_args()

    if args.discover:
        subprocess.run([PY, str(ROOT / "scripts/discover_colossus_podcasts.py"), "--founders-youtube"], check=True, cwd=str(ROOT))

    if args.youtube:
        subprocess.run(
            [PY, str(ROOT / "scripts/fetch_founders_youtube.py"), "--curated-only"],
            check=False,
            cwd=str(ROOT),
        )
        subprocess.run(
            [PY, str(ROOT / "scripts/fetch_founders_youtube.py"), "--transcripts"],
            check=False,
            cwd=str(ROOT),
        )
        subprocess.run(
            [PY, str(ROOT / "scripts/fetch_curated_youtube.py"), "--transcripts"],
            check=False,
            cwd=str(ROOT),
        )

    if args.transcribe:
        whisper_args = [
            PY,
            str(ROOT / "scripts/transcribe_colossus_audio.py"),
            "--curated-new",
            "--model",
            "tiny",
            "--fast",
        ]
        cache_args = [PY, str(ROOT / "scripts/transcribe_from_cache.py"), "--curated"]
        if args.include_non_youtube:
            whisper_args.append("--include-non-youtube")
            cache_args.append("--include-non-youtube")
        subprocess.run(whisper_args, check=False, cwd=str(ROOT))
        subprocess.run(cache_args, check=False, cwd=str(ROOT))

    if args.report or not any((args.discover, args.youtube, args.transcribe, args.sync)):
        subprocess.run([PY, str(ROOT / "scripts/resolve_curated_bb_founders.py"), "--stats"], cwd=str(ROOT))
        subprocess.run([PY, str(ROOT / "scripts/resolve_curated_bb_founders.py")], cwd=str(ROOT))

    if args.sync:
        subprocess.run(["node", str(ROOT / "web/scripts/sync-content.mjs")], cwd=str(ROOT / "web"), check=True)


if __name__ == "__main__":
    main()
