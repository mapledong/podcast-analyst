#!/usr/bin/env python3
"""Sequential transcription from audio cache with file lock (one Whisper at a time).

Curated --curated mode skips non-YouTube episodes unless --include-non-youtube.
Prefer fetch_curated_youtube.py for YouTube-linked episodes before Whisper.
"""

from __future__ import annotations

import argparse
import fcntl
import sys
import time
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))

from scripts.transcribe_acquired_audio import _transcribe  # noqa: E402
from scripts.resolve_curated_bb_founders import _has_youtube, resolve_curated  # noqa: E402

LOCK = ROOT / "data" / ".whisper.lock"
AUDIO = ROOT / "data" / "audio_cache"
TRANSCRIPTS = ROOT / "data" / "transcripts"


def _transcribe_cached(episode_id: str, *, model: str, fast: bool) -> Path:
    mp3 = AUDIO / f"{episode_id}.mp3"
    if not mp3.exists():
        raise FileNotFoundError(f"No cached audio: {mp3.name}")
    print(f"transcribing {episode_id} from cache ({mp3.stat().st_size // 1024} KB) …")
    text = _transcribe(mp3, model=model, fast=fast)
    out = TRANSCRIPTS / f"{episode_id}.txt"
    lines = [ln for ln in text.splitlines() if ln.strip()]
    header = f"# source: whisper/{model}\n# episode_id: {episode_id}\n# lines: {len(lines)}\n\n"
    out.write_text(header + text.strip() + "\n", encoding="utf-8")
    print(f"✓ {episode_id} → {out.name} ({len(lines)} lines)")
    return out


def _needs_full_transcript(episode_id: str) -> bool:
    rows = resolve_curated()
    for eps in rows.values():
        for ep in eps:
            if ep["id"] == episode_id:
                return not ep["has_transcript"]
    return True


def _missing_curated(*, youtube_only: bool) -> list[str]:
    rows = resolve_curated()
    ids: list[str] = []
    for eps in rows.values():
        for ep in eps:
            if ep["has_transcript"]:
                continue
            if youtube_only and not _has_youtube(ep):
                continue
            ids.append(ep["id"])
    return ids


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("episode_ids", nargs="*", help="Optional episode IDs")
    parser.add_argument("--curated", action="store_true", help="Curated episodes missing full transcript")
    parser.add_argument(
        "--include-non-youtube",
        action="store_true",
        help="With --curated: also process non-YouTube episodes with cached audio",
    )
    parser.add_argument("--model", default="tiny")
    parser.add_argument("--fast", action="store_true", default=True)
    args = parser.parse_args()

    youtube_only = not args.include_non_youtube
    ids = list(args.episode_ids) or (_missing_curated(youtube_only=youtube_only) if args.curated else [])
    if not ids:
        print("Nothing to transcribe")
        return

    LOCK.parent.mkdir(parents=True, exist_ok=True)
    with LOCK.open("w") as lockf:
        try:
            fcntl.flock(lockf, fcntl.LOCK_EX | fcntl.LOCK_NB)
        except BlockingIOError:
            print(f"Another transcription holds {LOCK}; exit and retry later.", file=sys.stderr)
            raise SystemExit(2)

        ok = fail = 0
        for eid in ids:
            mp3 = AUDIO / f"{eid}.mp3"
            if not mp3.exists():
                print(f"skip {eid}: no cached audio ({mp3.name})", file=sys.stderr)
                fail += 1
                continue
            try:
                _transcribe_cached(eid, model=args.model, fast=args.fast)
                ok += 1
            except Exception as exc:
                print(f"✗ {eid}: {exc}", file=sys.stderr)
                fail += 1
        print(f"\nDone: {ok} ok, {fail} failed")
        raise SystemExit(1 if fail else 0)


if __name__ == "__main__":
    main()
