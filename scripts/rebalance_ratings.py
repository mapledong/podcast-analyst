#!/usr/bin/env python3
"""Fix rating distribution violations and optionally create headroom below caps."""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))

from src.render import render_summary, save_summary  # noqa: E402
from src.template_config import template_path_for_podcast  # noqa: E402
from src.validate import load_template_config, rating_distribution_stats  # noqa: E402

APPROVED = ROOT / "data" / "approved"
OUTPUTS = ROOT / "outputs"
TEMPLATES = ROOT / "templates"


def _episodes_for_podcast(podcast: str) -> list[tuple[Path, dict]]:
    rows: list[tuple[Path, dict]] = []
    key = podcast.strip().lower()
    for path in sorted(APPROVED.glob("*.json")):
        if path.stem == "batch_state":
            continue
        data = json.loads(path.read_text(encoding="utf-8"))
        if str(data.get("podcast", "")).strip().lower() != key:
            continue
        rows.append((path, data))
    return rows


def _candidates(rows: list[tuple[Path, dict]], star: int) -> list[tuple[Path, dict]]:
    hits = [(p, d) for p, d in rows if int(d.get("episode_rating", {}).get("overall", 0)) == star]
    hits.sort(key=lambda item: int(item[1].get("metadata", {}).get("episode_number", 0)), reverse=True)
    return hits


def rebalance_podcast(
    podcast: str,
    *,
    headroom: int,
    apply: bool,
) -> int:
    tmpl = load_template_config(template_path_for_podcast(podcast))
    rows = _episodes_for_podcast(podcast)
    stats = rating_distribution_stats(tmpl, APPROVED, podcast=podcast)
    five_target = max(0, stats["five_cap"] - headroom)
    four_target = max(0, stats["four_cap"] - headroom)
    need_five = max(0, stats["five_count"] - five_target)
    need_four = max(0, stats["four_count"] - four_target)

    if need_five == 0 and need_four == 0:
        print(
            f"{podcast}: already within headroom "
            f"(5★ {stats['five_count']}/{stats['five_cap']}, 4★ {stats['four_count']}/{stats['four_cap']})"
        )
        return 0

    changes: list[tuple[Path, dict, int, int]] = []
    used: set[str] = set()

    for path, data in _candidates(rows, 5)[:need_five]:
        old = int(data["episode_rating"]["overall"])
        changes.append((path, data, old, 3))
        used.add(path.stem)

    four_count = 0
    for path, data in _candidates(rows, 4):
        if four_count >= need_four:
            break
        if path.stem in used:
            continue
        old = int(data["episode_rating"]["overall"])
        changes.append((path, data, old, 3))
        used.add(path.stem)
        four_count += 1

    changed = 0
    for path, data, old, new_rating in changes:
        print(f"{'apply' if apply else 'dry-run'} {path.stem}: {old}★ -> {new_rating}★")
        if apply:
            data["episode_rating"] = {"overall": new_rating}
            path.write_text(json.dumps(data, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
            ep_num = data.get("metadata", {}).get("episode_number", path.stem)
            md = render_summary(data, TEMPLATES, template_cfg=tmpl)
            save_summary(md, OUTPUTS / f"EP{ep_num}_{path.stem}.md")
        changed += 1

    stats = rating_distribution_stats(tmpl, APPROVED, podcast=podcast)
    print(
        f"{podcast} after: 5★ {stats['five_count']}/{stats['five_cap']} ({stats['five_pct']}%) | "
        f"4★ {stats['four_count']}/{stats['four_cap']} ({stats['four_pct']}%)"
    )
    return changed


def main() -> int:
    parser = argparse.ArgumentParser(description="Rebalance episode ratings to respect per-podcast caps.")
    parser.add_argument("--podcast", default="Acquired", help="Podcast name (default: Acquired)")
    parser.add_argument(
        "--headroom",
        type=int,
        default=3,
        help="Keep this many slots below the cap for 5★ and 4★ (default: 3)",
    )
    parser.add_argument("--apply", action="store_true", help="Write changes to approved JSON and re-render")
    parser.add_argument("--all-podcasts", action="store_true", help="Rebalance all main podcasts")
    args = parser.parse_args()

    podcasts = (
        ["Acquired", "Invest Like the Best", "Founders", "Business Breakdowns"]
        if args.all_podcasts
        else [args.podcast]
    )
    total = 0
    for podcast in podcasts:
        total += rebalance_podcast(podcast, headroom=args.headroom, apply=args.apply)

    if args.apply and total:
        import subprocess

        subprocess.run(["node", str(ROOT / "web" / "scripts" / "sync-content.mjs")], cwd=str(ROOT / "web"), check=False)

    print(f"\n{'Applied' if args.apply else 'Dry-run complete:'} {total} rating changes")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
