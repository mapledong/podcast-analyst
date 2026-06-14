#!/usr/bin/env python3
"""Transcribe Business Breakdowns / Founders episodes from Megaphone RSS audio.

Curated workflow prioritizes YouTube-linked episodes (fetch via fetch_curated_youtube.py).
By default --curated-missing / --curated-new skip non-YouTube episodes to avoid slow
Whisper runs; pass --include-non-youtube to transcribe RSS audio for all gaps.
"""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))

from scripts.transcribe_acquired_audio import _download_audio, _save, _transcribe  # noqa: E402
from scripts.resolve_curated_bb_founders import _has_youtube, resolve_curated  # noqa: E402

DISCOVERED = {
    "Business Breakdowns": ROOT / "data" / "discovered" / "business_breakdowns_episodes.json",
    "Founders": ROOT / "data" / "discovered" / "founders_episodes.json",
}
AUDIO_DIR = ROOT / "data" / "audio_cache"


def _disc_by_id() -> dict[str, dict]:
    out: dict[str, dict] = {}
    approved_by_podcast_num: dict[tuple[str, int], str] = {}
    for approved in (ROOT / "data" / "approved").glob("*.json"):
        try:
            data = json.loads(approved.read_text(encoding="utf-8"))
        except Exception:
            continue
        podcast = data.get("podcast")
        num = int((data.get("metadata") or {}).get("episode_number") or 0)
        if podcast and num:
            approved_by_podcast_num[(podcast, num)] = data["episode_id"]

    for path in DISCOVERED.values():
        if not path.exists():
            continue
        for ep in json.loads(path.read_text(encoding="utf-8"))["episodes"]:
            out[ep["id"]] = ep
            # alias: approved id by episode number
            num = ep.get("episode_number")
            podcast = ep.get("podcast")
            if num and podcast:
                aid = approved_by_podcast_num.get((podcast, int(num)))
                if aid:
                    out[aid] = ep
    return out


def _slug_from_id(episode_id: str) -> str:
    if episode_id.startswith("bb-"):
        return episode_id.removeprefix("bb-")
    if episode_id.startswith("fnd-"):
        # fnd-376-jensen-huang → keep full suffix after number
        parts = episode_id.split("-", 2)
        return parts[2] if len(parts) >= 3 else episode_id.removeprefix("fnd-")
    return episode_id


def transcribe_episode(episode_id: str, *, model: str = "base", force: bool = False, fast: bool = False) -> Path:
    from src.expand import resolve_transcript_path

    by_id = _disc_by_id()
    ep = by_id.get(episode_id)
    if not ep:
        raise FileNotFoundError(f"Unknown episode {episode_id}; run discover_colossus_podcasts.py")

    stub = {"episode_id": episode_id, "podcast": ep["podcast"], "metadata": ep}
    if not force:
        existing = resolve_transcript_path(stub)
        if existing and existing.read_text(encoding="utf-8", errors="replace")[:200].find("# source: whisper/") >= 0:
            print(f"skip {episode_id}: {existing.name}")
            return existing

    audio_url = ep.get("audio_url") or ""
    if not audio_url:
        raise RuntimeError(f"No audio_url for {episode_id}")

    audio_path = AUDIO_DIR / f"{episode_id}.mp3"
    print(f"downloading {episode_id} …")
    _download_audio(audio_url, audio_path)
    print(f"transcribing {episode_id} ({audio_path.stat().st_size // 1024} KB) …")
    text = _transcribe(audio_path, model=model, fast=fast)
    out = ROOT / "data" / "transcripts" / f"{episode_id}.txt"
    lines = [ln for ln in text.splitlines() if ln.strip()]
    header = f"# source: whisper/{model}\n# episode_id: {episode_id}\n# lines: {len(lines)}\n\n"
    out.write_text(header + text.strip() + "\n", encoding="utf-8")
    print(f"✓ {episode_id} → {out.name} ({len(lines)} lines)")
    return out


def _curated_ids(*, missing_transcript: bool, missing_approved: bool, youtube_only: bool) -> list[str]:
    rows = resolve_curated()
    ids: list[str] = []
    for eps in rows.values():
        for ep in eps:
            if missing_transcript and ep["has_transcript"]:
                continue
            if missing_approved and ep["approved"]:
                continue
            if youtube_only and not _has_youtube(ep):
                continue
            ids.append(ep["id"])
    return ids


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("episode_ids", nargs="*", help="Episode IDs; omit with --curated-missing")
    parser.add_argument("--curated-missing", action="store_true", help="Transcribe curated episodes missing transcripts")
    parser.add_argument("--curated-new", action="store_true", help="Transcribe curated episodes missing approved JSON")
    parser.add_argument(
        "--youtube-only",
        action="store_true",
        help="With --curated-*: only Whisper YouTube-linked episodes (default unless --include-non-youtube)",
    )
    parser.add_argument(
        "--include-non-youtube",
        action="store_true",
        help="With --curated-*: also Whisper non-YouTube episodes",
    )
    parser.add_argument("--fast", action="store_true", help="Faster whisper (tiny + no VAD)")
    parser.add_argument("--model", default="base")
    parser.add_argument("--force", action="store_true")
    args = parser.parse_args()

    youtube_only = not args.include_non_youtube
    if args.youtube_only and args.include_non_youtube:
        parser.error("--youtube-only and --include-non-youtube are mutually exclusive")
    ids = list(args.episode_ids)
    if args.curated_missing:
        ids = _curated_ids(missing_transcript=True, missing_approved=False, youtube_only=youtube_only)
    elif args.curated_new:
        ids = _curated_ids(missing_transcript=False, missing_approved=True, youtube_only=youtube_only)

    ok = fail = 0
    for eid in ids:
        try:
            transcribe_episode(eid, model=args.model, force=args.force, fast=args.fast)
            ok += 1
        except Exception as exc:
            print(f"✗ {eid}: {exc}", file=sys.stderr)
            fail += 1
    print(f"\nDone: {ok} ok, {fail} failed")
    raise SystemExit(1 if fail else 0)


if __name__ == "__main__":
    main()
