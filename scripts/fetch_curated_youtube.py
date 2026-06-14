#!/usr/bin/env python3
"""Fetch YouTube URLs and transcripts for curated BB/Founders episodes.

Priority workflow:
1. Resolve curated list; fetch missing youtube_url from Colossus pages.
2. For episodes with YouTube links, try YouTube transcript API first.
3. Skip non-YouTube episodes (no Whisper unless audio already cached elsewhere).

Transcript fetching (--transcripts) defaults to 3 episodes per run, 60s between
requests, and exponential backoff on 429/IP blocks. Use --full-queue for no
batch limit, or override with --batch-size / --delay.
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
    DEFAULT_BATCH_SIZE,
    DEFAULT_TRANSCRIPT_DELAY,
    _sleep_logged,
    _with_transcript_backoff,
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


def fetch_youtube_transcripts(
    *,
    delay: float = DEFAULT_TRANSCRIPT_DELAY,
    batch_size: int = DEFAULT_BATCH_SIZE,
    process_all: bool = False,
) -> tuple[int, int, int]:
    rows = resolve_curated()
    ok = skip = fail = 0
    transcripts = ROOT / "data" / "transcripts"
    queue: list[dict] = []

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
            except ValueError:
                skip += 1
                continue
            vid_path = transcripts / f"{vid}.txt"
            if vid_path.exists() and _is_full_transcript(vid_path):
                skip += 1
                continue
            queue.append(ep)

    queue.sort(key=lambda e: (bool(e.get("approved")), e["id"]))
    to_process = queue if process_all else queue[:batch_size]
    batch_total = len(to_process)

    if not to_process:
        return ok, skip, fail

    print(
        f"Transcript queue: {len(queue)} pending"
        + ("" if process_all else f", processing batch of {batch_total}")
    )

    for idx, ep in enumerate(to_process, start=1):
        yt = ep.get("youtube_url") or ""
        print(f"batch {idx}/{batch_total}: {ep['id']} …")
        try:

            def _do_fetch():
                return fetch_transcript(yt)

            result = _with_transcript_backoff(_do_fetch, episode_id=ep["id"])
            save_transcript(result, transcripts)
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
        if idx < batch_total:
            _sleep_logged(delay, reason="between episodes")

    if not process_all and len(queue) > batch_total:
        remaining = len(queue) - batch_total
        print(f"  {remaining} episode(s) remain in queue; rerun or pass --full-queue")

    return ok, skip, fail


def main() -> None:
    parser = argparse.ArgumentParser(description="Curated BB/Founders YouTube URL + transcript fetch")
    parser.add_argument("--urls", action="store_true", help="Fetch YouTube URLs from Colossus pages")
    parser.add_argument("--transcripts", action="store_true", help="Fetch YouTube transcripts for linked episodes")
    parser.add_argument("--all", action="store_true", help="Run --urls then --transcripts")
    parser.add_argument(
        "--full-queue",
        action="store_true",
        help="With --transcripts: process the full pending queue (no batch limit)",
    )
    parser.add_argument(
        "--batch-size",
        type=int,
        default=DEFAULT_BATCH_SIZE,
        help=f"Max episodes per --transcripts run (default: {DEFAULT_BATCH_SIZE})",
    )
    parser.add_argument(
        "--delay",
        type=float,
        default=0.75,
        help="Seconds between Colossus URL fetches (default: 0.75)",
    )
    parser.add_argument(
        "--transcript-delay",
        type=float,
        default=DEFAULT_TRANSCRIPT_DELAY,
        help=f"Seconds between transcript fetches (default: {DEFAULT_TRANSCRIPT_DELAY:.0f})",
    )
    args = parser.parse_args()

    if not any((args.urls, args.transcripts, args.all)):
        parser.error("Specify --urls, --transcripts, or --all")

    if args.urls or args.all:
        ok, skip, fail = fetch_youtube_urls(delay=args.delay)
        print(f"\nURLs: fetched {ok}, skipped {skip}, failed {fail}")

    if args.transcripts or args.all:
        ok, skip, fail = fetch_youtube_transcripts(
            delay=args.transcript_delay,
            batch_size=args.batch_size,
            process_all=args.full_queue,
        )
        print(f"\nTranscripts: fetched {ok}, skipped {skip}, failed {fail}")


if __name__ == "__main__":
    main()
