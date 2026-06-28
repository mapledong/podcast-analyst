"""Acquired catalog EP numbers: ordinal by publish date (oldest=EP.1, newest=EP.N)."""

from __future__ import annotations

import json
from pathlib import Path


def _acquired_rows(approved_dir: Path) -> list[tuple[str, str, dict]]:
    rows: list[tuple[str, str, dict]] = []
    for path in sorted(approved_dir.glob("acq*.json")):
        data = json.loads(path.read_text(encoding="utf-8"))
        date = data.get("metadata", {}).get("date", "1970-01-01")
        rows.append((date, path.stem, data))
    rows.sort(key=lambda x: (x[0], x[1]))
    return rows


def episode_number_by_date(episode_id: str, approved_dir: Path) -> int:
    """Return catalog EP number for an Acquired episode_id (1 = oldest)."""
    for i, (_, stem, _) in enumerate(_acquired_rows(approved_dir), start=1):
        if stem == episode_id:
            return i
    raise KeyError(f"Acquired episode not found: {episode_id}")


def renumber_all(approved_dir: Path) -> list[tuple[Path, dict, int]]:
    """Return (path, data, episode_number) for every Acquired approved JSON."""
    rows = _acquired_rows(approved_dir)
    out: list[tuple[Path, dict, int]] = []
    for i, (_, stem, data) in enumerate(rows, start=1):
        path = approved_dir / f"{stem}.json"
        out.append((path, data, i))
    return out
