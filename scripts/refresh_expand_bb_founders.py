#!/usr/bin/env python3
"""Refresh config/expand_bb_founders.yaml extras from discovered episode lists.

Keeps curated_bb_founders.yaml unchanged. Fills up to target_per_podcast (default 80)
with transcript-first, then YouTube-linked, then other discovered episodes.
"""

from __future__ import annotations

import argparse
import sys
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))

from scripts.resolve_curated_bb_founders import (  # noqa: E402
    _auto_fill_extras,
    _load_curated_config,
    _load_expand_config,
    EXPAND,
)

PODCAST_KEYS = [
    ("Business Breakdowns", "business_breakdowns"),
    ("Founders", "founders"),
]


def main() -> None:
    parser = argparse.ArgumentParser(description="Write expand_bb_founders.yaml extras from discovered RSS")
    parser.add_argument("--target", type=int, help="Override target_per_podcast (default: from yaml or 80)")
    parser.add_argument("--dry-run", action="store_true", help="Print yaml without writing")
    args = parser.parse_args()

    curated = _load_curated_config()
    expand = _load_expand_config()
    target = args.target or int(expand.get("target_per_podcast", 80))

    out: dict = {
        "target_per_podcast": target,
        "business_breakdowns": [],
        "founders": [],
    }
    for podcast, key in PODCAST_KEYS:
        curated_nums = {int(e["episode_number"]) for e in curated[key]}
        extras = _auto_fill_extras(podcast, curated_nums, target - len(curated_nums))
        out[key] = [{"episode_number": int(e["episode_number"])} for e in extras]

    header = (
        "# Expanded nightly pool beyond config/curated_bb_founders.yaml (30 curated each).\n"
        "# Long-term goal: 80+ approved summaries per podcast.\n"
        "# Refresh: python scripts/refresh_expand_bb_founders.py\n"
        "# Priority when selecting extras: full transcript > public company/unicorn subject > YouTube URL > other.\n\n"
    )
    body = yaml.dump(
        out,
        default_flow_style=False,
        sort_keys=False,
        allow_unicode=True,
    )
    text = header + body

    if args.dry_run:
        print(text)
        return

    EXPAND.write_text(text, encoding="utf-8")
    print(f"Wrote {EXPAND} (target_per_podcast={target})")
    for podcast, key in PODCAST_KEYS:
        print(f"  {podcast}: {len(curated[key])} curated + {len(out[key])} expand = {len(curated[key]) + len(out[key])}")


if __name__ == "__main__":
    main()
