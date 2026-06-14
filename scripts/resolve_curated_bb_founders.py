#!/usr/bin/env python3
"""Resolve curated BB/Founders episodes and report gaps (transcript / approved JSON).

Priority: episodes with YouTube links are processed first; non-YouTube episodes
without a full transcript are skipped for Whisper (see transcribe_colossus_audio.py).
"""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))

from src.expand import resolve_transcript_path  # noqa: E402

CURATED = ROOT / "config" / "curated_bb_founders.yaml"
DISCOVERED = {
    "Business Breakdowns": ROOT / "data" / "discovered" / "business_breakdowns_episodes.json",
    "Founders": ROOT / "data" / "discovered" / "founders_episodes.json",
}
APPROVED = ROOT / "data" / "approved"


def _approved_id_by_episode(podcast: str, ep_num: int) -> str | None:
    for path in APPROVED.glob("*.json"):
        try:
            data = json.loads(path.read_text(encoding="utf-8"))
        except Exception:
            continue
        if data.get("podcast") != podcast:
            continue
        if int((data.get("metadata") or {}).get("episode_number") or 0) == ep_num:
            return data["episode_id"]
    return None


def _load_discovered(podcast: str) -> dict[int, dict]:
    path = DISCOVERED[podcast]
    data = json.loads(path.read_text(encoding="utf-8"))
    return {int(ep["episode_number"]): ep for ep in data["episodes"] if ep.get("episode_number")}


MIN_FULL_TRANSCRIPT_CHARS = 10_000


def _transcript_body_chars(path: Path) -> int:
    try:
        text = path.read_text(encoding="utf-8", errors="replace")
    except OSError:
        return 0
    if text.startswith("#"):
        parts = text.split("\n\n", 1)
        body = parts[1] if len(parts) > 1 else ""
    else:
        body = text
    return len(body.strip())


def _is_full_transcript(path: Path | None) -> bool:
    if path is None or not path.exists():
        return False
    head = path.read_text(encoding="utf-8", errors="replace")[:200]
    if "# source: whisper/" in head or "# source: youtube/" in head:
        return True
    if "# video_id:" in head:
        return True
    return _transcript_body_chars(path) >= MIN_FULL_TRANSCRIPT_CHARS


def _has_youtube(ep: dict) -> bool:
    return bool((ep.get("youtube_url") or "").strip())


def _priority_key(ep: dict) -> tuple[int, int, int]:
    """YouTube-linked + ready-to-summarize episodes sort first."""
    return (
        0 if _has_youtube(ep) else 1,
        0 if ep.get("has_transcript") and not ep.get("approved") else 1,
        int(ep.get("episode_number") or 0),
    )


def curated_stats(rows: dict[str, list[dict]] | None = None) -> dict[str, dict[str, int]]:
    rows = rows or resolve_curated()
    out: dict[str, dict[str, int]] = {}
    for podcast, eps in rows.items():
        out[podcast] = {
            "curated": len(eps),
            "youtube": sum(1 for e in eps if _has_youtube(e)),
            "no_youtube": sum(1 for e in eps if not _has_youtube(e)),
            "full_transcript": sum(1 for e in eps if e["has_transcript"]),
            "no_transcript": sum(1 for e in eps if not e["has_transcript"]),
            "approved": sum(1 for e in eps if e["approved"]),
            "ready": sum(1 for e in eps if e["has_transcript"] and not e["approved"]),
            "youtube_ready": sum(
                1 for e in eps if _has_youtube(e) and e["has_transcript"] and not e["approved"]
            ),
        }
    return out


def resolve_curated() -> dict[str, list[dict]]:
    cfg = yaml.safe_load(CURATED.read_text(encoding="utf-8"))
    out: dict[str, list[dict]] = {}
    for podcast, key in [("Business Breakdowns", "business_breakdowns"), ("Founders", "founders")]:
        by_num = _load_discovered(podcast)
        rows: list[dict] = []
        for entry in cfg[key]:
            num = int(entry["episode_number"])
            ep = by_num.get(num)
            if not ep:
                raise SystemExit(f"Missing RSS episode {num} for {podcast}")
            eid = _approved_id_by_episode(podcast, num) or ep["id"]
            ep = {**ep, "id": eid}
            approved = APPROVED / f"{eid}.json"
            stub = {"episode_id": eid, "podcast": podcast, "metadata": ep}
            tx = resolve_transcript_path(stub)
            full_tx = _is_full_transcript(tx)
            rows.append(
                {
                    **ep,
                    "approved": approved.exists(),
                    "has_transcript": full_tx,
                    "has_youtube": _has_youtube(ep),
                    "transcript_path": str(tx) if tx else "",
                }
            )
        rows.sort(key=_priority_key)
        out[podcast] = rows
    return out


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--json", action="store_true")
    parser.add_argument("--missing-approved", action="store_true", help="Print episode IDs lacking approved JSON")
    parser.add_argument("--missing-transcript", action="store_true", help="Print episode IDs lacking transcript")
    parser.add_argument("--ready", action="store_true", help="Print IDs with full transcript but no approved JSON")
    parser.add_argument("--stats", action="store_true", help="Print YouTube / transcript / approved counts")
    parser.add_argument("--ids-only", action="store_true", help="With gap flags: print IDs only (no table)")
    args = parser.parse_args()

    rows = resolve_curated()

    if args.stats:
        print(json.dumps(curated_stats(rows), indent=2))
        return

    if args.missing_approved:
        for ep in (ep for eps in rows.values() for ep in eps if not ep["approved"]):
            print(ep["id"])
        return

    if args.ready:
        for ep in (ep for eps in rows.values() for ep in eps if ep["has_transcript"] and not ep["approved"]):
            print(ep["id"])
        return

    if args.missing_transcript:
        for ep in (ep for eps in rows.values() for ep in eps if not ep["has_transcript"]):
            print(ep["id"])
        return

    if args.json:
        print(json.dumps(rows, indent=2))
        return

    for podcast, eps in rows.items():
        print(f"\n=== {podcast} ({len(eps)} curated) ===")
        for ep in eps:
            flags = []
            if ep.get("has_youtube"):
                flags.append("yt")
            if ep["approved"]:
                flags.append("approved")
            if ep["has_transcript"]:
                flags.append("tx")
            print(f"  {ep['episode_number']:3d} {ep['id'][:45]:45s} {' '.join(flags) or 'NEW'}")


if __name__ == "__main__":
    main()
