#!/usr/bin/env python3
"""Fetch Acquired episode transcripts from acquired.fm show notes."""

from __future__ import annotations

import argparse
import html
import re
import sys
import urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))

OUT_DIR = ROOT / "data" / "transcripts"


def _strip_html(text: str) -> str:
    return html.unescape(re.sub(r"<[^>]+>", "", text)).strip()


def _extract_transcript_lines(page: str) -> list[str]:
    """Parse Ben/David dialogue from acquired.fm (legacy and Webflow formats)."""
    lines: list[str] = []
    seen: set[str] = set()

    # Webflow: <p><strong>Ben: </strong>text</p>
    for speaker, body in re.findall(
        r"<p[^>]*>\s*<strong>\s*(Ben|David)\s*:\s*</strong>\s*(.*?)\s*</p>",
        page,
        re.S | re.I,
    ):
        line = f"{speaker}: {_strip_html(body)}"
        if line and line not in seen:
            seen.add(line)
            lines.append(line)

    if len(lines) >= 20:
        return lines

    # Legacy: <p>Ben: text</p>
    legacy: list[str] = []
    seen_legacy: set[str] = set()
    for p in re.findall(r"<p[^>]*>((?:Ben|David):.*?)</p>", page, re.S):
        line = _strip_html(p)
        if line and line not in seen_legacy:
            seen_legacy.add(line)
            legacy.append(line)

    return legacy if len(legacy) > len(lines) else lines


def fetch_transcript(slug: str) -> tuple[str, int]:
    url = f"https://www.acquired.fm/episodes/{slug}"
    with urllib.request.urlopen(url, timeout=120) as resp:
        page = resp.read().decode("utf-8", errors="replace")
    lines = _extract_transcript_lines(page)
    if not lines:
        raise RuntimeError(f"No transcript paragraphs found for {slug}")
    return "\n".join(lines), len(lines)


def save(slug: str, text: str, line_count: int) -> Path:
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    path = OUT_DIR / f"acq-{slug}.txt"
    header = f"# source: acquired.fm\n# slug: {slug}\n# lines: {line_count}\n\n"
    path.write_text(header + text, encoding="utf-8")
    return path


def main() -> None:
    parser = argparse.ArgumentParser(description="Fetch Acquired transcript by episode slug")
    parser.add_argument("slug", help="Episode slug, e.g. vanguard")
    args = parser.parse_args()
    text, n = fetch_transcript(args.slug)
    path = save(args.slug, text, n)
    print(f"Saved {path} ({n} lines, {len(text)} chars)")


if __name__ == "__main__":
    main()
