#!/usr/bin/env python3
"""Download m4a from xiaoyuzhou RSS URLs and transcribe with faster-whisper.

Audio stays in data/audio_cache/ (gitignored). Do not commit or push m4a/mp3 to GitHub.
"""

from __future__ import annotations

import json
import subprocess
import sys
import urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
AUDIO_DIR = ROOT / "data" / "audio_cache"
OUT_DIR = ROOT / "data" / "transcripts"
DEFAULT_URLS = ROOT / "config" / "chinese_episode_m4a_urls.json"


def download(url: str, dest: Path) -> None:
    dest.parent.mkdir(parents=True, exist_ok=True)
    if dest.exists() and dest.stat().st_size > 100_000:
        print(f"skip download {dest.name}")
        return
    print(f"downloading {dest.name} …")
    urllib.request.urlretrieve(url, dest)


def transcribe(audio: Path, slug: str, *, model: str = "small", force: bool = False) -> Path:
    out = OUT_DIR / f"{slug}.txt"
    if out.exists() and not force:
        print(f"skip transcribe {slug}")
        return out
    from faster_whisper import WhisperModel

    print(f"transcribing {slug} ({audio.stat().st_size // 1024} KB, model={model}) …")
    whisper = WhisperModel(model, device="cpu", compute_type="int8")
    segments, _ = whisper.transcribe(str(audio), language="zh", vad_filter=True, beam_size=1)
    text = "\n".join(seg.text.strip() for seg in segments if seg.text.strip())
    lines = [ln for ln in text.splitlines() if ln.strip()]
    header = f"# source: whisper-{model}\n# slug: {slug}\n# lines: {len(lines)}\n\n"
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(header + text.strip() + "\n", encoding="utf-8")
    print(f"saved {out} ({len(lines)} lines)")
    return out


def main() -> None:
    import argparse

    parser = argparse.ArgumentParser()
    parser.add_argument("model", nargs="?", default="small", help="Whisper model (default: small)")
    parser.add_argument("slugs", nargs="*", help="Episode slugs")
    parser.add_argument("--urls-file", default=str(DEFAULT_URLS))
    parser.add_argument("--force", action="store_true", help="Overwrite existing transcripts")
    args = parser.parse_args()

    episodes = json.loads(Path(args.urls_file).read_text(encoding="utf-8"))
    slugs = args.slugs or list(episodes.keys())
    for slug in slugs:
        info = episodes[slug]
        audio = AUDIO_DIR / f"{slug}.m4a"
        download(info["url"], audio)
        transcribe(audio, slug, model=args.model, force=args.force)


if __name__ == "__main__":
    main()
