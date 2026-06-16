#!/usr/bin/env python3
"""Refine bilingual approved JSON for Chinese podcast pilot episodes.

Loads metadata from existing approved files, applies transcript-verified body content,
and writes data/approved/{id}.json and data/approved/zh/{id}.json.
"""

from __future__ import annotations

import json
import sys
from copy import deepcopy
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parent.parent
_SCRIPTS = Path(__file__).resolve().parent
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))
if str(_SCRIPTS) not in sys.path:
    sys.path.insert(0, str(_SCRIPTS))

from refine_chinese_pilot_bodies import REFINED as _REFINED_RAW  # noqa: E402
from refine_expansions import apply_expansions  # noqa: E402
from polish_bilingual_bodies import polish_refined  # noqa: E402

REFINED = polish_refined(_REFINED_RAW)

ZH_DIR = ROOT / "data" / "approved" / "zh"
EN_DIR = ROOT / "data" / "approved"

EPISODE_IDS = [
    "zj-ep136",
    "zj-ep137",
    "zj-ep138",
    "zj-ep139",
    "tzs-ep178",
    "tzs-ep181",
    "tzs-ep182",
    "tzs-ep183",
    "zj-ep140",
    "zj-ep141",
    "zj-ep142",
    "zj-ep143",
    "zj-ep144",
    "zj-ep145",
    "tzs-ep179",
    "tzs-ep180",
    "tzs-ep184",
    "tzs-ep185",
    "tzs-ep186",
    "tzs-ep187",
    "zj-ep121",
    "zj-ep120",
    "zj-ep109",
    "zj-ep104",
    "zj-ep83",
    "tzs-ep176",
    "tzs-ep170",
    "tzs-ep167",
    "tzs-ep158",
    "tzs-ep126",
]


def _load_meta(episode_id: str, locale: str) -> dict[str, Any]:
    path = (ZH_DIR if locale == "zh" else EN_DIR) / f"{episode_id}.json"
    data = json.loads(path.read_text(encoding="utf-8"))
    return {
        "episode_id": data["episode_id"],
        "podcast": data["podcast"],
        "host": data["host"],
        "metadata": deepcopy(data["metadata"]),
        "episode_rating": deepcopy(data["episode_rating"]),
    }


if __name__ == "__main__":
    ZH_DIR.mkdir(parents=True, exist_ok=True)
    for eid in EPISODE_IDS:
        if eid not in REFINED:
            raise SystemExit(f"missing refined content for {eid}")
        for locale, out_dir in (("zh", ZH_DIR), ("en", EN_DIR)):
            meta = _load_meta(eid, locale)
            body = apply_expansions(REFINED[eid][locale], eid, locale)
            merged = {**meta, **body}
            path = out_dir / f"{eid}.json"
            path.write_text(
                json.dumps(merged, ensure_ascii=False, indent=2) + "\n",
                encoding="utf-8",
            )
        print(f"wrote {eid}")

    import subprocess

    subprocess.run([sys.executable, str(_SCRIPTS / "apply_chinese_podcast_ratings.py")], check=True)
