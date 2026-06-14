#!/usr/bin/env python3
"""Fetch Business Breakdowns transcript text from joincolossus.com episode pages."""

from __future__ import annotations

import argparse
import html
import re
import urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
OUT_DIR = ROOT / "data" / "transcripts"

UA = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36"


def _slug_from_url(url: str) -> str:
    return url.rstrip("/").split("/")[-1]


def fetch_transcript(url: str) -> tuple[str, int]:
    req = urllib.request.Request(url, headers={"User-Agent": UA})
    with urllib.request.urlopen(req, timeout=120) as resp:
        page = resp.read().decode("utf-8", errors="replace")

    page = re.sub(r"<script[^>]*>.*?</script>", " ", page, flags=re.S | re.I)
    page = re.sub(r"<style[^>]*>.*?</style>", " ", page, flags=re.S | re.I)
    plain = html.unescape(re.sub(r"<[^>]+>", " ", page))
    plain = re.sub(r"\s+", " ", plain).strip()

    start_markers = (
        "Matt This is Matt",
        "Transcript Contents Introduction",
        "Introduction Matt",
    )
    start = -1
    for marker in start_markers:
        idx = plain.find(marker)
        if idx >= 0:
            start = idx
            break
    if start < 0:
        raise RuntimeError(f"No transcript marker found on {url}")

    # Trim at common footer markers
    end_markers = (
        "Please enjoy this Breakdown",
        "For the full show notes",
        "colossus.com/",
        "Episode is brought to you",
    )
    chunk = plain[start:]
    for em in end_markers:
        eidx = chunk.find(em)
        if eidx > 5000:
            chunk = chunk[:eidx]
            break

    # Split into pseudo-lines on speaker changes
    chunk = re.sub(r"\b(Matt|Zack|Guest|Alan|Daniel)\b(?=\s)", r"\n\1", chunk)
    lines = [ln.strip() for ln in chunk.split("\n") if ln.strip()]
    text = "\n".join(lines)
    if len(text) < 1500:
        raise RuntimeError(f"Transcript too short ({len(text)} chars) for {url}")
    return text, len(lines)


def save(slug: str, text: str, line_count: int, *, prefix: str = "bb") -> Path:
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    path = OUT_DIR / f"{prefix}-{slug}.txt"
    header = f"# source: joincolossus.com\n# slug: {slug}\n# lines: {line_count}\n\n"
    path.write_text(header + text, encoding="utf-8")
    return path


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("url", help="joincolossus.com episode URL")
    parser.add_argument("--prefix", default="bb")
    args = parser.parse_args()
    slug = _slug_from_url(args.url)
    text, n = fetch_transcript(args.url)
    path = save(slug, text, n, prefix=args.prefix)
    print(f"Saved {path} ({n} lines, {len(text)} chars)")


if __name__ == "__main__":
    main()
