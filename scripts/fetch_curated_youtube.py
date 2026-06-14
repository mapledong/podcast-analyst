#!/usr/bin/env python3
"""Fetch YouTube URLs and transcripts for curated BB/Founders episodes.

Priority workflow:
1. Resolve curated list; fetch missing youtube_url from Colossus pages.
2. For episodes with YouTube links, try YouTube transcript API first.
3. Skip non-YouTube episodes (no Whisper unless audio already cached elsewhere).
"""

from __future__ import annotations

import argparse
import json
import sys
import time
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))

from scripts.discover_colossus_podcasts import _fetch_youtube  # noqa: E402
from scripts.fetch_founders_youtube import (  # noqa: E402
    apply_matches,
    fetch_youtube_catalog,
    load_episodes,
    match_episodes,
    save_episodes,
    sync_approved_founders,
)
from scripts.resolve_curated_bb_founders import (  # noqa: E402
    DISCOVERED,
    _is_full_transcript,
    resolve_curated,
)
from src.expand import resolve_transcript_path  # noqa: E402
from src.fetch_transcript import extract_video_id, fetch_transcript, save_transcript  # noqa: E402


def _update_discovered_youtube(podcast: str, ep_num: int, youtube_url: str) -> None:
    path = DISCOVERED[podcast]
    data = json.loads(path.read_text(encoding="utf-8"))
    for ep in data["episodes"]:
        if int(ep.get("episode_number") or 0) == ep_num:
            ep["youtube_url"] = youtube_url
            break
    path.write_text(json.dumps(data, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")


def fetch_founders_youtube_urls() -> tuple[int, int]:
    """Match @founderspodcast1 videos to discovered episodes by title."""
    payload, episodes = load_episodes()
    catalog = fetch_youtube_catalog()
    matched = match_episodes(episodes, catalog)
    updated, _ = apply_matches(episodes, matched)
    save_episodes(payload)
    sync_approved_founders(episodes)
    return updated, len(matched)


def fetch_youtube_urls(*, delay: float = 0.5) -> tuple[int, int, int]:
    rows = resolve_curated()
    ok = skip = fail = 0

    fnd_updated, fnd_total = fetch_founders_youtube_urls()
    print(f"Founders YouTube: matched {fnd_total}, updated {fnd_updated} in discovered JSON")
    ok += fnd_updated

    for eps in rows.values():
        for ep in eps:
            if ep.get("podcast") == "Founders":
                continue
            if ep.get("youtube_url"):
                skip += 1
                continue
            url = ep.get("colossus_url") or ""
            if not url:
                skip += 1
                continue
            try:
                yt = _fetch_youtube(url)
                if yt:
                    _update_discovered_youtube(ep["podcast"], int(ep["episode_number"]), yt)
                    print(f"✓ {ep['id']} → {yt}")
                    ok += 1
                else:
                    print(f"– {ep['id']}: no YouTube on Colossus page")
                    skip += 1
            except Exception as exc:
                print(f"✗ {ep['id']}: {exc}")
                fail += 1
            time.sleep(delay)
    return ok, skip, fail


def fetch_youtube_transcripts(*, delay: float = 1.0) -> tuple[int, int, int]:
    rows = resolve_curated()
    ok = skip = fail = 0
    transcripts = ROOT / "data" / "transcripts"
    for eps in rows.values():
        for ep in eps:
            yt = ep.get("youtube_url") or ""
            if not yt:
                skip += 1
                continue
            stub = {"episode_id": ep["id"], "podcast": ep["podcast"], "metadata": ep}
            existing = resolve_transcript_path(stub)
            if _is_full_transcript(existing):
                skip += 1
                continue
            try:
                vid = extract_video_id(yt)
                vid_path = transcripts / f"{vid}.txt"
                if vid_path.exists() and _is_full_transcript(vid_path):
                    skip += 1
                    continue
                result = fetch_transcript(yt)
                save_transcript(result, transcripts)
                # Also write episode_id alias for resolve_transcript_path
                alias = transcripts / f"{ep['id']}.txt"
                header = (
                    f"# source: youtube/{result.source}\n"
                    f"# episode_id: {ep['id']}\n"
                    f"# video_id: {result.video_id}\n"
                    f"# lines: {result.line_count}\n\n"
                )
                alias.write_text(header + result.text + "\n", encoding="utf-8")
                print(f"✓ {ep['id']} ({result.line_count} lines)")
                ok += 1
            except Exception as exc:
                print(f"✗ {ep['id']}: {exc}")
                fail += 1
            time.sleep(delay)
    return ok, skip, fail


def main() -> None:
    parser = argparse.ArgumentParser(description="Curated BB/Founders YouTube URL + transcript fetch")
    parser.add_argument("--urls", action="store_true", help="Fetch YouTube URLs from Colossus pages")
    parser.add_argument("--transcripts", action="store_true", help="Fetch YouTube transcripts for linked episodes")
    parser.add_argument("--all", action="store_true", help="Run --urls then --transcripts")
    parser.add_argument("--delay", type=float, default=0.75)
    args = parser.parse_args()

    if not any((args.urls, args.transcripts, args.all)):
        parser.error("Specify --urls, --transcripts, or --all")

    if args.urls or args.all:
        ok, skip, fail = fetch_youtube_urls(delay=args.delay)
        print(f"\nURLs: fetched {ok}, skipped {skip}, failed {fail}")

    if args.transcripts or args.all:
        ok, skip, fail = fetch_youtube_transcripts(delay=args.delay)
        print(f"\nTranscripts: fetched {ok}, skipped {skip}, failed {fail}")


if __name__ == "__main__":
    main()
