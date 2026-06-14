#!/usr/bin/env python3
"""Report per-podcast star rating distribution vs template caps."""

from __future__ import annotations

import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))

from src.template_config import template_path_for_podcast  # noqa: E402
from src.validate import load_template_config, rating_distribution_stats, validate_rating_distribution  # noqa: E402

APPROVED = ROOT / "data" / "approved"
PODCASTS = ("Acquired", "Invest Like the Best", "Founders", "Business Breakdowns")


def main() -> int:
    violations: list[str] = []
    for podcast in PODCASTS:
        tmpl = load_template_config(template_path_for_podcast(podcast))
        stats = rating_distribution_stats(tmpl, APPROVED, podcast=podcast)
        five_headroom = stats["five_cap"] - stats["five_count"]
        four_headroom = stats["four_cap"] - stats["four_count"]
        print(
            f"{podcast}: n={stats['total']} | "
            f"5★ {stats['five_count']}/{stats['five_cap']} ({stats['five_pct']}%) headroom={five_headroom} | "
            f"4★ {stats['four_count']}/{stats['four_cap']} ({stats['four_pct']}%) headroom={four_headroom} | "
            f"cap={stats['cap_method']}"
        )
        if five_headroom < 0 or four_headroom < 0:
            violations.append(podcast)
        if five_headroom == 0 and stats["total"] >= 5:
            print(f"  note: 5★ at cap — new 5★ ratings will be auto-downgraded on publish")
        if four_headroom == 0 and stats["total"] >= 5:
            print(f"  note: 4★ at cap — new 4★ ratings will be auto-downgraded on publish")

    # spot-check a hypothetical new 5★ on Acquired
    tmpl = load_template_config(template_path_for_podcast("Acquired"))
    issues = validate_rating_distribution(5, tmpl, APPROVED, podcast="Acquired")
    if issues:
        print("\nIf a new Acquired episode were rated 5★ today:")
        for issue in issues:
            print(f"  {issue.severity}: {issue.message}")

    return 1 if violations else 0


if __name__ == "__main__":
    raise SystemExit(main())
