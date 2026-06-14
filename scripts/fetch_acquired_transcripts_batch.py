#!/usr/bin/env python3
"""Batch-fetch Acquired transcripts from acquired.fm show notes."""

from __future__ import annotations

import argparse
import json
import sys
import time
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))

from scripts.fetch_acquired_transcript import fetch_transcript, save  # noqa: E402

DISCOVERED = ROOT / "data" / "discovered" / "acquired_episodes.json"
STATE = ROOT / "data" / "acquired_batch_state.json"


def _load_state() -> dict:
    if STATE.exists():
        return json.loads(STATE.read_text(encoding="utf-8"))
    return {"fetched": [], "failed": []}


def _save_state(state: dict) -> None:
    STATE.parent.mkdir(parents=True, exist_ok=True)
    STATE.write_text(json.dumps(state, indent=2), encoding="utf-8")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--limit", type=int, default=None, help="Max episodes this run")
    parser.add_argument("--delay", type=float, default=1.5, help="Seconds between requests")
    parser.add_argument("--slug", action="append", default=[], help="Fetch specific slug(s) only")
    args = parser.parse_args()

    if args.slug:
        slugs = args.slug
    else:
        if not DISCOVERED.exists():
            raise SystemExit(f"Run discover first: python scripts/discover_acquired.py → {DISCOVERED}")
        data = json.loads(DISCOVERED.read_text(encoding="utf-8"))
        slugs = [ep["slug"] for ep in data["episodes"]]
        if args.limit:
            slugs = slugs[: args.limit]

    state = _load_state()
    ok = fail = skip = 0

    for slug in slugs:
        out = ROOT / "data" / "transcripts" / f"acq-{slug}.txt"
        if out.exists() and out.stat().st_size > 5000:
            skip += 1
            continue
        try:
            text, n = fetch_transcript(slug)
            path = save(slug, text, n)
            print(f"✓ {slug} → {path.name} ({n} lines)")
            if slug not in state["fetched"]:
                state["fetched"].append(slug)
            ok += 1
        except Exception as exc:
            print(f"✗ {slug}: {exc}")
            state["failed"].append({"slug": slug, "error": str(exc)})
            fail += 1
        _save_state(state)
        time.sleep(args.delay)

    print(f"\nFetched {ok}, skipped {skip}, failed {fail}")


if __name__ == "__main__":
    main()
