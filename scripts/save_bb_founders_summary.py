#!/usr/bin/env python3
"""Validate and publish a BB/Founders approved JSON from transcript metadata."""

from __future__ import annotations

import argparse
import json
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))

from src.template_config import template_path_for_podcast
from src.validate import load_template_config, validate_summary

APPLE_BB = "https://podcasts.apple.com/podcast/business-breakdowns/id1559120677"
SPOTIFY_BB = "https://open.spotify.com/show/4zQbeLbLgqKEyn7e2sKzez"
APPLE_FND = "https://podcasts.apple.com/podcast/founders/id1141877104"
SPOTIFY_FND = "https://open.spotify.com/show/3jWkZ6pYvYvYvYvYvYvYvYv"


def enrich_metadata(data: dict, ep: dict) -> None:
    meta = data.setdefault("metadata", {})
    meta.setdefault("episode_number", ep.get("episode_number"))
    meta.setdefault("title", ep.get("title"))
    meta.setdefault("guest", ep.get("guest"))
    meta.setdefault("guest_role", ep.get("guest_role"))
    meta.setdefault("date", ep.get("date"))
    meta.setdefault("duration_minutes", ep.get("duration_minutes"))
    youtube = ep.get("youtube_url", "")
    meta.setdefault("youtube_url", youtube)
    links = meta.setdefault("links", {})
    colossus = ep.get("colossus_url") or ""
    if colossus:
        links["colossus"] = colossus
    if youtube:
        links["youtube"] = youtube
    if data.get("podcast") == "Business Breakdowns":
        links.setdefault("apple_podcasts", APPLE_BB)
        links.setdefault("spotify", SPOTIFY_BB)
    else:
        links.setdefault("founders", "https://www.founderspodcast.com")
        links.setdefault("apple_podcasts", APPLE_FND)
        links.setdefault("spotify", SPOTIFY_FND)
    data.setdefault("extraction_meta", {})
    data["extraction_meta"].update(
        {
            "model": "manual-curated",
            "transcript_source": "whisper/base",
            "status": "approved",
            "template_version": "4.10",
        }
    )
    notes = data.get("review_notes", "")
    if "curated v4.10" not in notes:
        data["review_notes"] = (notes + " | curated v4.10").strip(" |")


def save_and_publish(data: dict, *, publish: bool) -> None:
    podcast = data["podcast"]
    tmpl = load_template_config(template_path_for_podcast(podcast))
    report = validate_summary(data, tmpl)
    if not report.passed:
        msgs = "; ".join(i.message for i in report.issues if i.severity == "error")
        raise SystemExit(f"Validation failed: {msgs}")
    path = ROOT / "data" / "approved" / f"{data['episode_id']}.json"
    path.write_text(json.dumps(data, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    print(f"✓ {data['episode_id']} ({report.total_words} words)")
    if publish:
        subprocess.run(
            [sys.executable, str(ROOT / "scripts/publish_approved_batch.py"), data["episode_id"]],
            cwd=str(ROOT),
            check=True,
        )


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("json_path", help="Path to draft approved JSON")
    parser.add_argument("--no-publish", action="store_true")
    args = parser.parse_args()
    data = json.loads(Path(args.json_path).read_text(encoding="utf-8"))
    save_and_publish(data, publish=not args.no_publish)


if __name__ == "__main__":
    main()
