#!/usr/bin/env python3
"""Download YouTube audio and transcribe with faster-whisper (Chinese)."""

from __future__ import annotations

import argparse
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
AUDIO_DIR = ROOT / "data" / "audio_cache"
OUT_DIR = ROOT / "data" / "transcripts"


def _download_audio(url: str, dest: Path) -> None:
    dest.parent.mkdir(parents=True, exist_ok=True)
    if dest.exists() and dest.stat().st_size > 100_000:
        return
    cmd = [
        "yt-dlp",
        "-x",
        "--audio-format",
        "mp3",
        "--audio-quality",
        "5",
        "-o",
        str(dest.with_suffix(".%(ext)s")),
        url,
    ]
    subprocess.run(cmd, check=True)


def _transcribe(audio_path: Path, *, model: str = "small") -> str:
    from faster_whisper import WhisperModel

    whisper = WhisperModel(model, device="cpu", compute_type="int8")
    segments, _info = whisper.transcribe(
        str(audio_path),
        language="zh",
        vad_filter=True,
        beam_size=1,
    )
    return "\n".join(seg.text.strip() for seg in segments if seg.text.strip())


def transcribe(url: str, slug: str, *, model: str = "small", force: bool = False) -> Path:
    out = OUT_DIR / f"{slug}.txt"
    if out.exists() and not force:
        print(f"skip {slug}: transcript exists")
        return out

    audio = AUDIO_DIR / f"{slug}.mp3"
    print(f"downloading {slug} …")
    _download_audio(url, audio)
    print(f"transcribing {slug} ({audio.stat().st_size // 1024} KB) …")
    text = _transcribe(audio, model=model)
    lines = [ln for ln in text.splitlines() if ln.strip()]
    header = f"# source: whisper-{model}\n# slug: {slug}\n# lines: {len(lines)}\n\n"
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(header + text.strip() + "\n", encoding="utf-8")
    print(f"saved {out} ({len(lines)} lines)")
    return out


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("url")
    parser.add_argument("--slug", required=True)
    parser.add_argument("--model", default="small")
    parser.add_argument("--force", action="store_true")
    args = parser.parse_args()
    transcribe(args.url, args.slug, model=args.model, force=args.force)


if __name__ == "__main__":
    main()
