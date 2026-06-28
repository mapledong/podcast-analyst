#!/usr/bin/env python3
"""Renumber Acquired episodes by date (oldest=1) and recalibrate star ratings."""

from __future__ import annotations

import json
import math
import re
import subprocess
import sys
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parent.parent
APPROVED = ROOT / "data" / "approved"
OUTPUTS = ROOT / "outputs"
EPISODES_YAML = ROOT / "config" / "episodes.yaml"

FIVE_MAX_PCT = 0.20
FOUR_MAX_PCT = 0.30


def _is_acquired(path: Path) -> bool:
    return path.name.startswith("acq") and path.suffix == ".json"


def _rank_key(stem: str, duration: int) -> tuple:
    """Lower sort key = higher priority for 5★."""
    slug = stem.removeprefix("acq-")
    penalty = 0
    if re.search(r"holiday-special|sessions|interview|short-|acq-sessions", slug):
        penalty += 40
    if re.search(r"ceo-|munger|jensen-huang|mark-zuckerberg|jamie-dimon|ballmer|stratechery", slug):
        penalty += 25
    if "live-from-chase" in slug or "10-years-of-acquired" in slug:
        penalty += 20
    if "benchmark-part-ii|benchmarks-mitch" in slug:
        penalty += 15
    # Prefer long deep dives
    return (penalty, -duration, slug)


def _load_episodes() -> list[tuple[Path, dict]]:
    rows: list[tuple[Path, dict]] = []
    for path in sorted(APPROVED.glob("acq*.json")):
        rows.append((path, json.loads(path.read_text(encoding="utf-8"))))
    return rows


def renumber_by_date(rows: list[tuple[Path, dict]] | None = None) -> list[tuple[Path, dict, int]]:
    """Return (path, data, episode_number) sorted oldest→newest for assignment."""
    from src.acquired_catalog import renumber_all

    if rows is None:
        return renumber_all(APPROVED)
    # Legacy: accept pre-loaded rows (tests / callers)
    dated = []
    for path, data in rows:
        date = data.get("metadata", {}).get("date", "1970-01-01")
        dated.append((date, path, data))
    dated.sort(key=lambda x: (x[0], x[1].stem))
    return [(path, data, i) for i, (_, path, data) in enumerate(dated, start=1)]


def assign_ratings(rows: list[tuple[Path, dict, int]]) -> dict[str, int]:
    n = len(rows)
    five_cap = max(1, math.floor(n * FIVE_MAX_PCT))
    four_cap = max(1, math.floor(n * FOUR_MAX_PCT))
    three_count = n - five_cap - four_cap
    if three_count < 0:
        four_cap = n - five_cap
        three_count = 0

    ranked = sorted(
        rows,
        key=lambda r: _rank_key(r[0].stem, int(r[1].get("metadata", {}).get("duration_minutes", 60))),
    )
    ratings: dict[str, int] = {}
    for path, _, _ in ranked[:five_cap]:
        ratings[path.stem] = 5
    for path, _, _ in ranked[five_cap : five_cap + four_cap]:
        ratings[path.stem] = 4
    for path, _, _ in ranked[five_cap + four_cap :]:
        ratings[path.stem] = 3
    return ratings


def _episode_yaml_entry(data: dict) -> dict:
    meta = data.get("metadata", {})
    links = meta.get("links", {})
    entry = {
        "id": data["episode_id"],
        "episode_number": int(meta["episode_number"]),
        "title": meta.get("title", ""),
        "guest": meta.get("guest", ""),
        "guest_role": meta.get("guest_role", ""),
        "date": meta.get("date", ""),
        "duration_minutes": meta.get("duration_minutes", 60),
        "youtube_url": meta.get("youtube_url") or links.get("youtube", ""),
        "podcast": "Acquired",
    }
    return entry


def _upsert_episodes_yaml(entries: list[dict]) -> None:
    cfg = yaml.safe_load(EPISODES_YAML.read_text(encoding="utf-8"))
    existing = {ep["id"]: ep for ep in cfg.get("episodes", []) if not str(ep.get("id", "")).startswith("acq")}
    for entry in entries:
        existing[entry["id"]] = entry
    cfg["episodes"] = sorted(existing.values(), key=lambda e: int(e["episode_number"]), reverse=True)
    EPISODES_YAML.write_text(yaml.dump(cfg, sort_keys=False, allow_unicode=True), encoding="utf-8")


def _cleanup_stale_outputs() -> None:
    for path in OUTPUTS.glob("EP*_acq-*.md"):
        path.unlink(missing_ok=True)


def main() -> None:
    numbered = renumber_by_date()
    ratings = assign_ratings(numbered)

    yaml_entries: list[dict] = []
    for path, data, ep_num in numbered:
        data["metadata"]["episode_number"] = ep_num
        data.setdefault("episode_rating", {})["overall"] = ratings[path.stem]
        path.write_text(json.dumps(data, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
        yaml_entries.append(_episode_yaml_entry(data))

    _upsert_episodes_yaml(yaml_entries)
    _cleanup_stale_outputs()

    subprocess.run(
        [sys.executable, str(ROOT / "scripts" / "publish_approved_batch.py")],
        cwd=str(ROOT),
        check=True,
    )
    subprocess.run(["node", str(ROOT / "web/scripts/sync-content.mjs")], cwd=str(ROOT / "web"), check=True)

    from collections import Counter

    c = Counter(ratings.values())
    print(f"Renumbered {len(numbered)} Acquired episodes (EP.1 oldest → EP.{len(numbered)} newest)")
    print(f"Ratings: 5★={c[5]} ({c[5]/len(numbered):.0%}), 4★={c[4]} ({c[4]/len(numbered):.0%}), 3★={c[3]} ({c[3]/len(numbered):.0%})")
    print(f"Caps: 5★≤{math.floor(len(numbered)*FIVE_MAX_PCT)}, 4★≤{math.floor(len(numbered)*FOUR_MAX_PCT)}")


if __name__ == "__main__":
    main()
