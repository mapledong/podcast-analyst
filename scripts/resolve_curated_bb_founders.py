#!/usr/bin/env python3
"""Resolve curated + expanded BB/Founders episodes and report gaps.

Nightly pool: config/curated_bb_founders.yaml (30 each) plus
config/expand_bb_founders.yaml (fills to target_per_podcast, default 80).

Priority for ordering and auto-fill: full transcript > YouTube URL > needs transcribe.
"""

from __future__ import annotations

import argparse
import json
import os
import sys
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))

from src.company_tickers import load_company_tickers  # noqa: E402
from src.expand import resolve_transcript_path  # noqa: E402

CURATED = ROOT / "config" / "curated_bb_founders.yaml"
EXPAND = ROOT / "config" / "expand_bb_founders.yaml"
DISCOVERED = {
    "Business Breakdowns": ROOT / "data" / "discovered" / "business_breakdowns_episodes.json",
    "Founders": ROOT / "data" / "discovered" / "founders_episodes.json",
}
APPROVED = ROOT / "data" / "approved"
PODCAST_KEYS = [
    ("Business Breakdowns", "business_breakdowns"),
    ("Founders", "founders"),
]
DEFAULT_TARGET_PER_PODCAST = 80


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


def _transcript_source(path: Path | None) -> str:
    if path is None or not path.exists():
        return "none"
    head = path.read_text(encoding="utf-8", errors="replace")[:300].lower()
    if "# source: youtube/" in head or "# video_id:" in head:
        return "youtube"
    if "# source: whisper/" in head:
        return "whisper"
    return "file"


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


UNICORN_KEYWORDS = (
    "spacex",
    "stripe",
    "databricks",
    "openai",
    "anthropic",
    "airbnb",
    "uber",
    "palantir",
    "robinhood",
    "snowflake",
    "instacart",
    "doordash",
    "coinbase",
    "bytedance",
    "tiktok",
    "spacex",
    "blue origin",
    "figma",
    "canva",
    "discord",
    "revolut",
    "klarna",
    "shein",
    "spacex",
)


def _episode_subject_text(ep: dict) -> str:
    return " ".join(
        str(ep.get(k) or "")
        for k in ("title", "guest", "guest_role", "description")
    ).lower()


def _is_public_or_unicorn(ep: dict) -> bool:
    """Prioritize 上市公司 (public) and 一级市场独角兽 subjects."""
    text = _episode_subject_text(ep)
    aliases = load_company_tickers()["aliases"]
    if any(alias in text for alias in aliases):
        return True
    return any(kw in text for kw in UNICORN_KEYWORDS)


def _pool_priority_key(ep: dict) -> tuple[int, int, int, int]:
    """Transcript-first, public/unicorn subject, YouTube, then newer episodes."""
    return (
        0 if ep.get("has_transcript") else 1,
        0 if _is_public_or_unicorn(ep) else 1,
        0 if ep.get("has_youtube") else 1,
        -int(ep.get("episode_number") or 0),
    )


def _ready_priority_key(ep: dict) -> tuple[int, int, int, int]:
    """Nightly queue: transcript-ready > YouTube (fetch captions) > needs transcribe."""
    if ep.get("approved"):
        return (9, 9, 9, 0)
    if ep.get("has_transcript"):
        tier = 0
    elif ep.get("has_youtube"):
        tier = 1
    else:
        tier = 2
    podcast_rank = 0 if ep.get("podcast") == "Founders" else 1
    return (tier, podcast_rank, -int(ep.get("episode_number") or 0), 0)


def _load_curated_config() -> dict:
    return yaml.safe_load(CURATED.read_text(encoding="utf-8"))


def _load_expand_config() -> dict:
    if not EXPAND.exists():
        return {"target_per_podcast": DEFAULT_TARGET_PER_PODCAST, "business_breakdowns": [], "founders": []}
    return yaml.safe_load(EXPAND.read_text(encoding="utf-8"))


def _resolve_episode_row(podcast: str, ep: dict) -> dict:
    num = int(ep["episode_number"])
    eid = _approved_id_by_episode(podcast, num) or ep["id"]
    ep = {**ep, "id": eid, "podcast": podcast}
    approved = APPROVED / f"{eid}.json"
    stub = {"episode_id": eid, "podcast": podcast, "metadata": ep}
    tx = resolve_transcript_path(stub)
    full_tx = _is_full_transcript(tx)
    return {
        **ep,
        "approved": approved.exists(),
        "has_transcript": full_tx,
        "has_youtube": _has_youtube(ep),
        "transcript_source": _transcript_source(tx),
        "transcript_path": str(tx) if tx else "",
        "needs_transcribe": not full_tx and not _has_youtube(ep),
    }


def _auto_fill_extras(podcast: str, curated_nums: set[int], slots: int) -> list[dict]:
    if slots <= 0:
        return []
    by_num = _load_discovered(podcast)
    candidates: list[dict] = []
    for num, ep in by_num.items():
        if num in curated_nums:
            continue
        candidates.append(_resolve_episode_row(podcast, ep))
    candidates.sort(key=_pool_priority_key)
    return candidates[:slots]


def _target_per_podcast(expand_cfg: dict) -> int:
    env = os.environ.get("TARGET_PER_PODCAST", "").strip()
    if env.isdigit():
        return int(env)
    return int(expand_cfg.get("target_per_podcast", DEFAULT_TARGET_PER_PODCAST))


def resolve_curated() -> dict[str, list[dict]]:
    curated_cfg = _load_curated_config()
    expand_cfg = _load_expand_config()
    target = _target_per_podcast(expand_cfg)
    out: dict[str, list[dict]] = {}

    for podcast, key in PODCAST_KEYS:
        by_num = _load_discovered(podcast)
        curated_entries = curated_cfg[key]
        curated_nums = {int(e["episode_number"]) for e in curated_entries}
        expand_nums = {int(e["episode_number"]) for e in expand_cfg.get(key, [])}

        rows: list[dict] = []
        seen: set[int] = set()

        for entry in curated_entries:
            num = int(entry["episode_number"])
            ep = by_num.get(num)
            if not ep:
                raise SystemExit(f"Missing RSS episode {num} for {podcast}")
            rows.append(_resolve_episode_row(podcast, ep))
            seen.add(num)

        for num in sorted(expand_nums - curated_nums):
            if num in seen:
                continue
            ep = by_num.get(num)
            if not ep:
                continue
            rows.append(_resolve_episode_row(podcast, ep))
            seen.add(num)

        if len(rows) < target:
            auto = _auto_fill_extras(podcast, seen, target - len(rows))
            for ep in auto:
                num = int(ep["episode_number"])
                if num in seen:
                    continue
                rows.append(ep)
                seen.add(num)

        rows.sort(key=_pool_priority_key)
        out[podcast] = rows
    return out


def pool_stats(rows: dict[str, list[dict]] | None = None) -> dict[str, dict[str, int]]:
    rows = rows or resolve_curated()
    curated_cfg = _load_curated_config()
    expand_cfg = _load_expand_config()
    target = _target_per_podcast(expand_cfg)
    out: dict[str, dict[str, int]] = {}
    for podcast, eps in rows.items():
        key = next(k for p, k in PODCAST_KEYS if p == podcast)
        curated_nums = {int(e["episode_number"]) for e in curated_cfg[key]}
        not_approved = [e for e in eps if not e["approved"]]
        ready_tx = [e for e in not_approved if e["has_transcript"]]
        out[podcast] = {
            "target": target,
            "pool": len(eps),
            "curated_core": len(curated_nums),
            "full_transcript": sum(1 for e in eps if e["has_transcript"]),
            "youtube_no_transcript": sum(1 for e in eps if e["has_youtube"] and not e["has_transcript"]),
            "needs_transcribe": sum(1 for e in eps if e.get("needs_transcribe")),
            "approved": sum(1 for e in eps if e["approved"]),
            "ready_with_transcript": len(ready_tx),
            "ready_total": len(not_approved),
            "youtube_ready": sum(1 for e in ready_tx if e["has_youtube"]),
        }
    return out


def curated_stats(rows: dict[str, list[dict]] | None = None) -> dict[str, dict[str, int]]:
    """Backward-compatible stats keys plus expanded pool fields."""
    rows = rows or resolve_curated()
    base = pool_stats(rows)
    for podcast, eps in rows.items():
        base[podcast].update(
            {
                "curated": base[podcast]["pool"],
                "youtube": sum(1 for e in eps if e["has_youtube"]),
                "no_youtube": sum(1 for e in eps if not e["has_youtube"]),
                "no_transcript": sum(1 for e in eps if not e["has_transcript"]),
                "ready": base[podcast]["ready_with_transcript"],
            }
        )
    return base


def ready_queue(rows: dict[str, list[dict]], *, limit: int | None = None) -> list[dict]:
    pending = [ep for eps in rows.values() for ep in eps if not ep["approved"]]
    pending.sort(key=_ready_priority_key)
    if limit is not None and limit > 0:
        return pending[:limit]
    return pending


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--json", action="store_true")
    parser.add_argument("--missing-approved", action="store_true", help="Print episode IDs lacking approved JSON")
    parser.add_argument("--missing-transcript", action="store_true", help="Print episode IDs lacking transcript")
    parser.add_argument(
        "--ready",
        action="store_true",
        help="Print nightly candidates (transcript-ready first; use --limit for batch size)",
    )
    parser.add_argument("--stats", action="store_true", help="Print pool / transcript / approved counts")
    parser.add_argument("--ids-only", action="store_true", help="With gap flags: print IDs only (no table)")
    parser.add_argument(
        "--limit",
        type=int,
        default=0,
        help="Cap --ready output (default: all transcript-ready; with limit, fill from expanded pool)",
    )
    args = parser.parse_args()

    rows = resolve_curated()
    limit = args.limit or None
    if args.limit and not args.ready:
        limit = None

    if args.stats:
        print(json.dumps(pool_stats(rows), indent=2))
        return

    if args.missing_approved:
        for ep in (ep for eps in rows.values() for ep in eps if not ep["approved"]):
            print(ep["id"])
        return

    if args.ready:
        queue = ready_queue(rows, limit=limit)
        for ep in queue:
            if limit is None and not ep["has_transcript"]:
                continue
            print(ep["id"])
        return

    if args.missing_transcript:
        for ep in (ep for eps in rows.values() for ep in eps if not ep["has_transcript"]):
            print(ep["id"])
        return

    if args.json:
        print(json.dumps(rows, indent=2))
        return

    target = _target_per_podcast(_load_expand_config())
    for podcast, eps in rows.items():
        print(f"\n=== {podcast} ({len(eps)}/{target} pool) ===")
        for ep in eps:
            flags = []
            if ep.get("has_youtube"):
                flags.append("yt")
            if ep["approved"]:
                flags.append("approved")
            if ep["has_transcript"]:
                flags.append("tx")
            elif ep.get("needs_transcribe"):
                flags.append("whisper?")
            print(f"  {ep['episode_number']:3d} {ep['id'][:45]:45s} {' '.join(flags) or 'NEW'}")


if __name__ == "__main__":
    main()
