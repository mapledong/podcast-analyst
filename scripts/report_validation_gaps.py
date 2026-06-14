#!/usr/bin/env python3
"""Report word-count and policy gaps across approved summaries."""

from __future__ import annotations

import argparse
import json
import sys
from collections import defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))

from src.duration import duration_tier  # noqa: E402
from src.expand import resolve_transcript_path  # noqa: E402
from src.template_config import template_path_for_podcast  # noqa: E402
from src.validate import expansion_warnings, load_template_config, validate_summary, word_gap  # noqa: E402

APPROVED = ROOT / "data" / "approved"

TIER_LABELS = {
    "under_90_min": "<90 min → ~5 min read",
    "90_to_180_min": "90–179 min → 5–8 min read",
    "over_180_min": "180+ min → 8–10 min read",
}


def _needs_total_expansion(data: dict, template: dict) -> bool:
    return word_gap(data, template) > 0


def _needs_any_expansion(data: dict, template: dict) -> bool:
    return bool(expansion_warnings(data, template))


def _iter_paths(ids: list[str] | None, podcast: str | None) -> list[Path]:
    if ids:
        paths = [APPROVED / f"{eid}.json" for eid in ids]
    else:
        paths = sorted(APPROVED.glob("*.json"))
    out: list[Path] = []
    for path in paths:
        if not path.exists():
            continue
        if podcast:
            data = json.loads(path.read_text(encoding="utf-8"))
            if data.get("podcast") != podcast:
                continue
        out.append(path)
    return out


def main() -> None:
    parser = argparse.ArgumentParser(description="Report validation gaps for batch expansion.")
    parser.add_argument("ids", nargs="*", help="Episode IDs (default: all approved)")
    parser.add_argument("--podcast", help='Filter by podcast name, e.g. "Acquired"')
    parser.add_argument("--json", action="store_true", help="Emit machine-readable JSON")
    parser.add_argument("--needs-expansion", action="store_true", help="Only episodes with warnings")
    parser.add_argument(
        "--total-only",
        action="store_true",
        help="Only episodes below total word minimum (ignore section/policy warnings)",
    )
    args = parser.parse_args()

    paths = _iter_paths(args.ids or None, args.podcast)
    rows: list[dict] = []
    by_podcast_total: dict[str, int] = defaultdict(int)
    by_podcast_any: dict[str, int] = defaultdict(int)
    by_tier_total: dict[str, int] = defaultdict(int)
    by_tier_any: dict[str, int] = defaultdict(int)
    no_transcript = 0
    ok_total = 0
    ok_any = 0

    for path in paths:
        data = json.loads(path.read_text(encoding="utf-8"))
        podcast = data.get("podcast", "Unknown")
        tmpl = load_template_config(template_path_for_podcast(podcast))
        report = validate_summary(data, tmpl)
        warnings = expansion_warnings(data, tmpl)
        gap = word_gap(data, tmpl)
        tier = duration_tier(data.get("metadata", {}).get("duration_minutes", 60))
        has_transcript = resolve_transcript_path(data) is not None
        needs_total = _needs_total_expansion(data, tmpl)
        needs_any = _needs_any_expansion(data, tmpl)

        if needs_total:
            by_podcast_total[podcast] += 1
            by_tier_total[tier] += 1
        else:
            ok_total += 1

        if needs_any:
            by_podcast_any[podcast] += 1
            by_tier_any[tier] += 1
        else:
            ok_any += 1

        if args.total_only and not needs_total:
            continue
        if args.needs_expansion and not needs_any:
            continue

        row = {
            "id": path.stem,
            "podcast": podcast,
            "tier": tier,
            "duration": data.get("metadata", {}).get("duration_minutes", 60),
            "words": report.total_words,
            "min_words": report.min_total_words,
            "gap": gap,
            "warnings": len(warnings),
            "needs_total": needs_total,
            "needs_any": needs_any,
            "has_transcript": has_transcript,
            "issues": [f"{i.section}: {i.message}" for i in warnings],
        }
        rows.append(row)
        if not has_transcript:
            no_transcript += 1

    summary = {
        "total": len(paths),
        "ok_total_words": ok_total,
        "need_total_expansion": len(paths) - ok_total,
        "ok_no_warnings": ok_any,
        "need_any_expansion": len(paths) - ok_any,
        "missing_transcript": no_transcript,
        "total_word_gap": sum(r["gap"] for r in rows if r["needs_total"]),
        "by_podcast_total": dict(by_podcast_total),
        "by_podcast_any": dict(by_podcast_any),
        "by_tier_total": dict(by_tier_total),
        "by_tier_any": dict(by_tier_any),
    }

    if args.json:
        print(json.dumps({"episodes": rows, "summary": summary}, indent=2))
        return

    print(f"Scanned {len(paths)} episodes\n")
    print("=== Read-length tiers (episode duration → target read) ===")
    for key, label in TIER_LABELS.items():
        n = by_tier_total.get(key, 0)
        total_in_tier = sum(1 for r in rows if r["tier"] == key) if rows else 0
        print(f"  {label}: {n} need total expansion")
    print()
    print(f"Below total word minimum: {summary['need_total_expansion']} (rewrite/expand)")
    print(f"Already meet total minimum: {summary['ok_total_words']}")
    print(f"Any validator warning (incl. sections/policy): {summary['need_any_expansion']}")
    print(f"Missing transcript: {no_transcript}")
    print()
    print("By podcast (below total minimum):")
    for podcast, count in sorted(by_podcast_total.items(), key=lambda x: -x[1]):
        print(f"  {podcast}: {count}")
    print()
    print(f"{'ID':<40} {'DUR':>4} {'WORDS':>6} {'MIN':>6} {'GAP':>5} {'TX':>3} TOT ANY")
    print("-" * 78)
    show = rows if rows else []
    for row in sorted(show, key=lambda r: (-r["gap"], r["id"])):
        tx = "Y" if row["has_transcript"] else "N"
        tot = "!" if row["needs_total"] else " "
        any_ = "!" if row["needs_any"] else " "
        print(
            f"{tot}{row['id']:<39} {row['duration']:>4} {row['words']:>6} {row['min_words']:>6} "
            f"{row['gap']:>5} {tx:>3} {tot:>3} {any_:>3}"
        )


def _summary(rows: list[dict]) -> dict:
    needs = [r for r in rows if r["needs_total"]]
    return {
        "total": len(rows),
        "needs_expansion": len(needs),
        "missing_transcript": sum(1 for r in rows if not r["has_transcript"]),
        "total_word_gap": sum(r["gap"] for r in needs),
    }


if __name__ == "__main__":
    main()
