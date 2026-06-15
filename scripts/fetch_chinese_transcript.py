#!/usr/bin/env python3
"""Fetch YouTube transcripts (Chinese or English) and save to data/transcripts/."""

from __future__ import annotations

import argparse
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))

from src.fetch_transcript import extract_video_id, save_transcript, TranscriptResult  # noqa: E402
from youtube_transcript_api import YouTubeTranscriptApi  # noqa: E402
from youtube_transcript_api._errors import NoTranscriptFound, TranscriptsDisabled, VideoUnavailable  # noqa: E402


def fetch_chinese_transcript(url: str, languages: list[str] | None = None) -> TranscriptResult:
    langs = languages or ["zh-Hans", "zh", "zh-CN", "en", "en-US"]
    video_id = extract_video_id(url)
    api = YouTubeTranscriptApi()

    try:
        transcript_list = api.list(video_id)
    except (TranscriptsDisabled, VideoUnavailable) as exc:
        raise RuntimeError(f"Transcript unavailable for {video_id}: {exc}") from exc

    transcript = None
    used_lang = langs[0]
    source = "manual"

    for lang in langs:
        try:
            transcript = transcript_list.find_transcript([lang])
            used_lang = lang
            source = "manual" if not transcript.is_generated else "auto"
            break
        except NoTranscriptFound:
            continue

    if transcript is None:
        try:
            transcript = transcript_list.find_generated_transcript(langs)
            used_lang = transcript.language_code
            source = "auto"
        except NoTranscriptFound as exc:
            raise RuntimeError(f"No transcript for video {video_id}") from exc

    fetched = transcript.fetch()
    lines = [snippet.text.strip() for snippet in fetched if snippet.text.strip()]
    text = "\n".join(lines)

    return TranscriptResult(
        video_id=video_id,
        text=text,
        language=used_lang,
        source=source,
        line_count=len(lines),
    )


def main() -> None:
    parser = argparse.ArgumentParser(description="Fetch YouTube transcript for Chinese podcasts")
    parser.add_argument("url", help="YouTube video URL")
    parser.add_argument("--slug", required=True, help="Output filename slug (without .txt)")
    parser.add_argument("--out-dir", default=str(ROOT / "data" / "transcripts"))
    args = parser.parse_args()

    result = fetch_chinese_transcript(args.url)
    out_dir = Path(args.out_dir)
    out_dir.mkdir(parents=True, exist_ok=True)
    path = out_dir / f"{args.slug}.txt"
    header = (
        f"# video_id: {result.video_id}\n"
        f"# language: {result.language}\n"
        f"# source: {result.source}\n"
        f"# lines: {result.line_count}\n\n"
    )
    path.write_text(header + result.text, encoding="utf-8")
    print(f"Saved {path} ({result.line_count} lines, {result.language}, {result.source})")


if __name__ == "__main__":
    main()
