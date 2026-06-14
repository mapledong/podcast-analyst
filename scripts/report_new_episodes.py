#!/usr/bin/env python3
"""Report discovered episodes missing approved summaries (all podcast series)."""

from __future__ import annotations

import argparse
import json
import sys
from datetime import date, timedelta
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))

from src.expand import resolve_transcript_path  # noqa: E402

APPROVED = ROOT / "data" / "approved"
DISCOVERED_DIR = ROOT / "data" / "discovered"

PODCAST_FEEDS: list[tuple[str, str]] = [
    ("Invest Like the Best", "iltb_episodes.json"),
    ("Acquired", "acquired_episodes.json"),
    ("Business Breakdowns", "business_breakdowns_episodes.json"),
    ("Founders", "founders_episodes.json"),
]

MIN_TRANSCRIPT_CHARS = 10_000


def _parse_date(raw: str) -> date | None:
    if not raw:
        return None
    try:
        return date.fromisoformat(str(raw)[:10])
    except ValueError:
        return None


def _has_approved(ep_id: str) -> bool:
    return (APPROVED / f"{ep_id}.json").exists()


def _transcript_ok(ep_id: str, podcast: str, ep: dict) -> bool:
    stub = {"episode_id": ep_id, "podcast": podcast, "metadata": ep}
    path = resolve_transcript_path(stub)
    if path is None or not path.exists():
        return False
    try:
        body = path.read_text(encoding="utf-8", errors="replace")
    except OSError:
        return False
    if "# source: youtube/" in body[:200] or "# source: whisper/" in body[:200]:
        return True
    if len(body.strip()) >= MIN_TRANSCRIPT_CHARS:
        return True
    return False


def collect_pending(*, recent_days: int = 7) -> list[dict[str, Any]]:
    today = date.today()
    recent_cutoff = today - timedelta(days=recent_days)
    rows: list[dict[str, Any]] = []

    for podcast, filename in PODCAST_FEEDS:
        path = DISCOVERED_DIR / filename
        if not path.exists():
            continue
        data = json.loads(path.read_text(encoding="utf-8"))
        for ep in data.get("episodes") or []:
            eid = ep.get("id") or ""
            if not eid or _has_approved(eid):
                continue
            ep_date = _parse_date(ep.get("date") or "")
            has_tx = _transcript_ok(eid, podcast, ep)
            is_recent = ep_date is not None and ep_date >= recent_cutoff
            rows.append(
                {
                    "id": eid,
                    "podcast": podcast,
                    "title": ep.get("title") or "",
                    "guest": ep.get("guest") or "",
                    "guest_role": ep.get("guest_role") or "",
                    "date": ep_date.isoformat() if ep_date else "",
                    "has_transcript": has_tx,
                    "is_recent_release": is_recent,
                    "youtube_url": ep.get("youtube_url") or "",
                }
            )

    def sort_key(row: dict[str, Any]) -> tuple[int, int, str]:
        # Recent + transcript first, then recent, then transcript, then date desc
        return (
            0 if row["is_recent_release"] and row["has_transcript"] else 1,
            0 if row["is_recent_release"] else 1,
            0 if row["has_transcript"] else 1,
            row.get("date") or "",
        )

    rows.sort(key=sort_key, reverse=True)
    return rows


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--recent-days", type=int, default=7)
    parser.add_argument("--ready", action="store_true", help="Only episodes with full transcript")
    parser.add_argument("--recent", action="store_true", help="Only episodes published in recent-days")
    parser.add_argument("--limit", type=int, default=0)
    parser.add_argument("--json", action="store_true")
    parser.add_argument("--ids-only", action="store_true")
    parser.add_argument("--stats", action="store_true")
    args = parser.parse_args()

    rows = collect_pending(recent_days=args.recent_days)
    if args.ready:
        rows = [r for r in rows if r["has_transcript"]]
    if args.recent:
        rows = [r for r in rows if r["is_recent_release"]]
    if args.limit > 0:
        rows = rows[: args.limit]

    if args.stats:
        all_rows = collect_pending(recent_days=args.recent_days)
        print(
            json.dumps(
                {
                    "pending_total": len(all_rows),
                    "pending_recent": sum(1 for r in all_rows if r["is_recent_release"]),
                    "pending_ready": sum(1 for r in all_rows if r["has_transcript"]),
                    "pending_recent_ready": sum(
                        1 for r in all_rows if r["is_recent_release"] and r["has_transcript"]
                    ),
                },
                indent=2,
            )
        )
        return 0

    if args.ids_only:
        for row in rows:
            print(row["id"])
        return 0

    if args.json:
        print(json.dumps(rows, indent=2, ensure_ascii=False))
        return 0

    print(f"pending: {len(rows)}")
    for row in rows:
        flags = []
        if row["is_recent_release"]:
            flags.append("new")
        if row["has_transcript"]:
            flags.append("tx")
        print(
            f"  [{' '.join(flags) or '-'}] {row['id']} · {row.get('date') or '?'} · "
            f"{row['podcast'][:12]:12s} · {row['title'][:50]}"
        )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
