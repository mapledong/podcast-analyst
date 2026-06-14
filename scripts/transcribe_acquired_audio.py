#!/usr/bin/env python3
"""Transcribe Acquired episodes from RSS audio when no show-notes transcript exists."""

from __future__ import annotations

import argparse
import json
import re
import sys
import urllib.request
import xml.etree.ElementTree as ET
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))

from src.expand import resolve_transcript_path  # noqa: E402

FEED_URL = "https://feeds.transistor.fm/acquired"
OUT_DIR = ROOT / "data" / "transcripts"
AUDIO_DIR = ROOT / "data" / "audio_cache"


def _norm_title(title: str) -> str:
    t = re.sub(r"\s*\|\s*Acquired\s*$", "", title, flags=re.I)
    t = re.sub(r"^(Episode|Ep\.?)\s*\d+[:\.\s-]+", "", t, flags=re.I)
    t = re.sub(r"^Acquired Episode \d+[:\.\s-]+", "", t, flags=re.I)
    t = re.sub(r"^Season \d+, Episode \d+:\s*", "", t, flags=re.I)
    return re.sub(r"[^a-z0-9]+", " ", t.lower()).strip()


def _rss_audio_by_norm_title() -> dict[str, str]:
    with urllib.request.urlopen(FEED_URL, timeout=120) as resp:
        root = ET.fromstring(resp.read())
    channel = root.find("channel")
    out: dict[str, str] = {}
    for item in channel.findall("item"):
        title = (item.findtext("title") or "").strip()
        enc = item.find("enclosure")
        if enc is None:
            continue
        url = enc.get("url") or ""
        if not url:
            continue
        out[_norm_title(title)] = url
    return out


def _token_overlap(a: str, b: str) -> float:
    ta = set(a.split())
    tb = set(b.split())
    if not ta or not tb:
        return 0.0
    return len(ta & tb) / len(ta | tb)


def _find_rss_audio(rss: dict[str, str], norm: str) -> str | None:
    if norm in rss:
        return rss[norm]
    partial = [(k, u) for k, u in rss.items() if norm in k or k in norm]
    if len(partial) == 1:
        return partial[0][1]
    scored = sorted((( _token_overlap(norm, k), k, u) for k, u in rss.items()), reverse=True)
    if scored and scored[0][0] >= 0.5:
        return scored[0][2]
    return None


def _episode_norm_title(data: dict) -> str:
    meta = data.get("metadata") or {}
    title = meta.get("title") or meta.get("guest") or ""
    return _norm_title(title)


def _slug_from_data(data: dict) -> str:
    links = (data.get("metadata") or {}).get("links") or {}
    acquired_url = links.get("acquired", "")
    if "/episodes/" in acquired_url:
        return acquired_url.rstrip("/").split("/")[-1]
    return data["episode_id"].removeprefix("acq-")


def _download_audio(url: str, dest: Path) -> None:
    dest.parent.mkdir(parents=True, exist_ok=True)
    if dest.exists() and dest.stat().st_size > 100_000:
        return
    req = urllib.request.Request(
        url,
        headers={
            "User-Agent": (
                "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) "
                "AppleWebKit/537.36 (KHTML, like Gecko) "
                "Chrome/126.0.0.0 Safari/537.36"
            ),
            "Accept": "*/*",
            "Accept-Language": "en-US,en;q=0.9",
            "Referer": "https://www.podtrac.com/",
        },
    )
    with urllib.request.urlopen(req, timeout=600) as resp:
        dest.write_bytes(resp.read())


def _transcribe(audio_path: Path, *, model: str, fast: bool = False) -> str:
    from faster_whisper import WhisperModel

    whisper = WhisperModel(model, device="cpu", compute_type="int8")
    kwargs: dict = {"language": "en"}
    if fast:
        kwargs.update({"vad_filter": False, "beam_size": 1})
    else:
        kwargs["vad_filter"] = True
    segments, _info = whisper.transcribe(str(audio_path), **kwargs)
    return "\n".join(seg.text.strip() for seg in segments if seg.text.strip())


def _save(slug: str, text: str, source: str) -> Path:
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    lines = [ln for ln in text.splitlines() if ln.strip()]
    path = OUT_DIR / f"acq-{slug}.txt"
    header = f"# source: {source}\n# slug: {slug}\n# lines: {len(lines)}\n\n"
    path.write_text(header + text.strip() + "\n", encoding="utf-8")
    return path


def transcribe_episode(
    episode_id: str,
    *,
    model: str = "base",
    force: bool = False,
) -> Path | None:
    approved = ROOT / "data" / "approved" / f"{episode_id}.json"
    if not approved.exists():
        raise FileNotFoundError(approved)
    data = json.loads(approved.read_text(encoding="utf-8"))
    if not force and resolve_transcript_path(data):
        print(f"skip {episode_id}: transcript exists")
        return None

    slug = _slug_from_data(data)
    rss = _rss_audio_by_norm_title()
    norm = _episode_norm_title(data)
    audio_url = _find_rss_audio(rss, norm)
    if not audio_url:
        raise RuntimeError(f"No RSS audio match for {episode_id!r} ({norm!r})")

    audio_path = AUDIO_DIR / f"{episode_id}.mp3"
    print(f"downloading {episode_id} …")
    _download_audio(audio_url, audio_path)
    print(f"transcribing {episode_id} ({audio_path.stat().st_size // 1024} KB) …")
    text = _transcribe(audio_path, model=model)
    path = _save(slug, text, f"whisper/{model}")
    print(f"✓ {episode_id} → {path.name} ({len(text.splitlines())} lines)")
    return path


def main() -> None:
    parser = argparse.ArgumentParser(description="Transcribe Acquired episodes from RSS audio")
    parser.add_argument("episode_ids", nargs="+", help="e.g. acq-meituan")
    parser.add_argument("--model", default="base", help="faster-whisper model (default: base)")
    parser.add_argument("--force", action="store_true", help="Re-transcribe even if file exists")
    args = parser.parse_args()

    ok = fail = 0
    for eid in args.episode_ids:
        try:
            transcribe_episode(eid, model=args.model, force=args.force)
            ok += 1
        except Exception as exc:
            print(f"✗ {eid}: {exc}", file=sys.stderr)
            fail += 1
    print(f"\nDone: {ok} ok, {fail} failed")
    raise SystemExit(1 if fail else 0)


if __name__ == "__main__":
    main()
