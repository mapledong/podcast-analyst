"""Fetch YouTube transcripts for podcast episodes."""

from __future__ import annotations

import re
from dataclasses import dataclass
from pathlib import Path

from youtube_transcript_api import YouTubeTranscriptApi
from youtube_transcript_api._errors import (
    NoTranscriptFound,
    TranscriptsDisabled,
    VideoUnavailable,
)


@dataclass
class TranscriptResult:
    video_id: str
    text: str
    language: str
    source: str
    line_count: int


def extract_video_id(url: str) -> str:
    patterns = [
        r"(?:v=|/v/|youtu\.be/|/embed/)([a-zA-Z0-9_-]{11})",
        r"^([a-zA-Z0-9_-]{11})$",
    ]
    for pattern in patterns:
        match = re.search(pattern, url)
        if match:
            return match.group(1)
    raise ValueError(f"Could not parse YouTube video ID from: {url}")


def fetch_transcript(url: str, languages: list[str] | None = None) -> TranscriptResult:
    langs = languages or ["en", "en-US", "en-GB"]
    video_id = extract_video_id(url)
    api = YouTubeTranscriptApi()

    try:
        transcript_list = api.list(video_id)
    except (TranscriptsDisabled, VideoUnavailable) as exc:
        raise RuntimeError(f"Transcript unavailable for {video_id}: {exc}") from exc

    transcript = None
    used_lang = "en"
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
            raise RuntimeError(f"No English transcript for video {video_id}") from exc

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


def save_transcript(result: TranscriptResult, output_dir: Path) -> Path:
    output_dir.mkdir(parents=True, exist_ok=True)
    path = output_dir / f"{result.video_id}.txt"
    header = (
        f"# video_id: {result.video_id}\n"
        f"# language: {result.language}\n"
        f"# source: {result.source}\n"
        f"# lines: {result.line_count}\n\n"
    )
    path.write_text(header + result.text, encoding="utf-8")
    return path
