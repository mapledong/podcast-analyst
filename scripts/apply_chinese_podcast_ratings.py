#!/usr/bin/env python3
"""Apply template-compliant star ratings to Chinese podcast approved JSON."""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))

from src.validate import load_template_config, rating_distribution_stats  # noqa: E402

CONFIG = ROOT / "config" / "chinese_episode_ratings.yaml"
EN_DIR = ROOT / "data" / "approved"
ZH_DIR = ROOT / "data" / "approved" / "zh"
TEMPLATE = ROOT / "config" / "template.yaml"


def _episode_ids_for_podcast(podcast_name: str) -> list[str]:
    key = podcast_name.strip().lower()
    ids: list[tuple[int, str]] = []
    for path in sorted(EN_DIR.glob("*.json")):
        if path.stem == "batch_state":
            continue
        data = json.loads(path.read_text(encoding="utf-8"))
        if str(data.get("podcast", "")).strip().lower() != key:
            continue
        ep_num = int(data.get("metadata", {}).get("episode_number", 0))
        ids.append((ep_num, path.stem))
    ids.sort()
    return [eid for _, eid in ids]


def _assign_ratings(
    episode_ids: list[str],
    five_star: list[str],
    four_star: list[str],
) -> dict[str, int]:
    tmpl = load_template_config(TEMPLATE)
    n = len(episode_ids)
    stats = rating_distribution_stats(tmpl, EN_DIR, podcast=None)
    # recompute caps for this subset size
    from src.validate import _rating_cap

    cfg = tmpl.get("rating_distribution") or {}
    five_cap = _rating_cap(n, float(cfg.get("five_star_max_pct", 0.20)), str(cfg.get("cap_method", "floor")))
    four_cap = _rating_cap(n, float(cfg.get("four_star_max_pct", 0.30)), str(cfg.get("cap_method", "floor")))

    present = set(episode_ids)
    assigned: dict[str, int] = {eid: 3 for eid in episode_ids}

    five_assigned: set[str] = set()
    five_used = 0
    for eid in five_star:
        if eid not in present or five_used >= five_cap:
            continue
        assigned[eid] = 5
        five_assigned.add(eid)
        five_used += 1

    four_candidates: list[str] = []
    seen: set[str] = set()
    for eid in four_star:
        if eid in present and eid not in seen:
            four_candidates.append(eid)
            seen.add(eid)
    for eid in five_star:
        if eid in present and eid not in five_assigned and eid not in seen:
            four_candidates.append(eid)
            seen.add(eid)

    four_used = 0
    for eid in four_candidates:
        if four_used >= four_cap:
            break
        if assigned.get(eid) == 5:
            continue
        assigned[eid] = 4
        four_used += 1

    return assigned


def apply_ratings(*, dry_run: bool = False) -> int:
    cfg = yaml.safe_load(CONFIG.read_text(encoding="utf-8")) or {}
    tmpl = load_template_config(TEMPLATE)
    changed = 0

    for _pod_id, block in cfg.items():
        if not isinstance(block, dict):
            continue
        podcast = str(block.get("podcast", "")).strip()
        if not podcast:
            continue
        episode_ids = _episode_ids_for_podcast(podcast)
        if not episode_ids:
            continue

        ratings = _assign_ratings(
            episode_ids,
            list(block.get("five_star") or []),
            list(block.get("four_star") or []),
        )

        stats = rating_distribution_stats(tmpl, EN_DIR, podcast=podcast)
        print(f"\n{podcast} ({len(episode_ids)} eps, caps 5★≤{stats['five_cap']} 4★≤{stats['four_cap']}):")
        for eid in episode_ids:
            new = ratings[eid]
            for locale, ddir in (("en", EN_DIR), ("zh", ZH_DIR)):
                path = ddir / f"{eid}.json"
                if not path.exists():
                    continue
                data = json.loads(path.read_text(encoding="utf-8"))
                old = int(data.get("episode_rating", {}).get("overall", 3))
                if old == new:
                    print(f"  {eid} [{locale}]: {new}★ (unchanged)")
                    continue
                print(f"  {eid} [{locale}]: {old}★ → {new}★")
                if not dry_run:
                    data["episode_rating"] = {"overall": new}
                    path.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
                    changed += 1

        stats = rating_distribution_stats(tmpl, EN_DIR, podcast=podcast)
        print(
            f"  distribution: 5★ {stats['five_count']}/{stats['five_cap']} | "
            f"4★ {stats['four_count']}/{stats['four_cap']} | "
            f"3★ {stats['total'] - stats['five_count'] - stats['four_count']}"
        )

    return changed


def main() -> int:
    parser = argparse.ArgumentParser(description="Apply Chinese podcast star ratings from config.")
    parser.add_argument("--dry-run", action="store_true")
    args = parser.parse_args()
    n = apply_ratings(dry_run=args.dry_run)
    if args.dry_run:
        print(f"\nDry-run: would change {n} files")
    else:
        print(f"\nApplied {n} rating updates")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
