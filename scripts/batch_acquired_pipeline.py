#!/usr/bin/env python3
"""Orchestrate Acquired batch: discover → fetch transcripts → (optional LLM extract) → publish."""

from __future__ import annotations

import argparse
import json
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DISCOVERED = ROOT / "data" / "discovered" / "acquired_episodes.json"
PY = sys.executable


def main() -> None:
    parser = argparse.ArgumentParser(description="Acquired batch pipeline")
    parser.add_argument("--limit", type=int, default=50)
    parser.add_argument("--all", action="store_true", help="Discover all sitemap episodes")
    parser.add_argument("--discover", action="store_true")
    parser.add_argument("--fetch", action="store_true")
    parser.add_argument("--publish", action="store_true")
    parser.add_argument("--fetch-meta", action="store_true")
    args = parser.parse_args()

    if args.discover:
        cmd = [PY, str(ROOT / "scripts" / "discover_acquired.py")]
        if args.all:
            cmd.append("--all")
        else:
            cmd.extend(["--limit", str(args.limit)])
        if args.fetch_meta:
            cmd.append("--fetch-meta")
        subprocess.run(cmd, check=True, cwd=str(ROOT))

    if args.fetch:
        subprocess.run(
            [PY, str(ROOT / "scripts" / "fetch_acquired_transcripts_batch.py"), "--limit", str(args.limit)],
            check=True,
            cwd=str(ROOT),
        )

    if args.publish:
        subprocess.run(
            [PY, str(ROOT / "scripts" / "validate_acquired_batch.py"), "--publish"],
            check=True,
            cwd=str(ROOT),
        )

    if DISCOVERED.exists():
        data = json.loads(DISCOVERED.read_text(encoding="utf-8"))
        approved = list((ROOT / "data" / "approved").glob("acq-*.json"))
        print(f"discovered={len(data['episodes'])} approved_acq={len(approved)}")


if __name__ == "__main__":
    main()
