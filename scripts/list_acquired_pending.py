#!/usr/bin/env python3
"""List Acquired episodes missing approved summaries."""

from __future__ import annotations

import argparse
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DISCOVERED = ROOT / "data" / "discovered" / "acquired_episodes.json"
APPROVED = ROOT / "data" / "approved"
TRANSCRIPTS = ROOT / "data" / "transcripts"
# sp26 hand ids map to these slugs — treat as done
DONE_SLUGS = {"vanguard", "ferrari", "formula-1"}


def _is_done(ep: dict) -> bool:
    eid = ep["id"]
    slug = ep["slug"]
    if slug in DONE_SLUGS:
        return True
    if (APPROVED / f"{eid}.json").exists():
        return True
    # Legacy sp26 ids
    for legacy in ("acq-sp26-01", "acq-sp26-02", "acq-sp26-03"):
        legacy_path = APPROVED / f"{legacy}.json"
        if not legacy_path.exists():
            continue
        data = json.loads(legacy_path.read_text(encoding="utf-8"))
        links = data.get("metadata", {}).get("links", {})
        acq_url = links.get("acquired", "")
        if slug and slug in acq_url:
            return True
    return False


def pending(*, require_transcript: bool = False) -> list[dict]:
    data = json.loads(DISCOVERED.read_text(encoding="utf-8"))
    out: list[dict] = []
    for ep in data["episodes"]:
        if _is_done(ep):
            continue
        tpath = TRANSCRIPTS / f"acq-{ep['slug']}.txt"
        if require_transcript and not (tpath.exists() and tpath.stat().st_size > 5000):
            continue
        out.append({**ep, "has_transcript": tpath.exists() and tpath.stat().st_size > 5000})
    return out


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--require-transcript", action="store_true")
    parser.add_argument("--offset", type=int, default=0)
    parser.add_argument("--limit", type=int, default=None)
    parser.add_argument("--json", action="store_true")
    args = parser.parse_args()
    rows = pending(require_transcript=args.require_transcript)
    if args.offset:
        rows = rows[args.offset :]
    if args.limit:
        rows = rows[: args.limit]
    if args.json:
        print(json.dumps(rows, indent=2, ensure_ascii=False))
    else:
        print(f"pending: {len(rows)}")
        for ep in rows:
            tx = "✓" if ep.get("has_transcript") else "·"
            print(f"  [{tx}] {ep['id']} · {ep.get('date','?')} · {ep['duration_minutes']}m · {ep['title'][:55]}")
    return None


if __name__ == "__main__":
    main()
