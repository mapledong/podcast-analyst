#!/usr/bin/env python3
"""Discover ILTB episodes from Apple Podcasts RSS and match YouTube videos."""

from __future__ import annotations

import json
import re
import subprocess
import sys
import urllib.request
import xml.etree.ElementTree as ET
from datetime import datetime, timezone
from email.utils import parsedate_to_datetime
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
OUT = ROOT / "data" / "discovered" / "iltb_episodes.json"
sys.path.insert(0, str(ROOT))

from scripts.ytdlp_bin import ytdlp_bin  # noqa: E402
ITUNES_NS = "http://www.itunes.com/dtds/podcast-1.0.dtd"
APPLE_PODCAST_ID = 1154105909
DEFAULT_CUTOFF = datetime(2021, 6, 14, tzinfo=timezone.utc)
YOUTUBE_CHANNEL = "https://www.youtube.com/@ILTB_Podcast/videos"


def _itunes(tag: str) -> str:
    return f"{{{ITUNES_NS}}}{tag}"


def _normalize_name(name: str) -> str:
    return re.sub(r"[^a-z0-9]+", " ", name.lower()).strip()


def _parse_rss_title(title: str) -> tuple[str, str, int | None]:
    """Return (guest, episode_title, episode_number)."""
    ep_match = re.search(r"EP\.(\d+)\]", title, re.I)
    ep_num = int(ep_match.group(1)) if ep_match else None
    core = re.sub(r"\s*-\s*\[Invest Like the Best.*$", "", title, flags=re.I).strip()

    # "Guest on Topic" (single segment, no "Guest - Title" split)
    on_match = re.match(r"^([A-Z][^\s-]+(?:\s+[A-Z][^\s-]+)?)\s+on\s+(.+)$", core)
    if on_match and " - " not in core:
        return on_match.group(1).strip(), on_match.group(2).strip(), ep_num

    if " - " in core:
        guest, ep_title = [p.strip() for p in core.split(" - ", 1)]
        return guest, ep_title, ep_num

    return core, core, ep_num


def _fetch_feed_url() -> str:
    lookup = f"https://itunes.apple.com/lookup?id={APPLE_PODCAST_ID}&entity=podcast"
    with urllib.request.urlopen(lookup, timeout=30) as resp:
        data = json.loads(resp.read())
    feed = data["results"][0]["feedUrl"]
    return feed


def _parse_duration(itunes_duration: str | None) -> int | None:
    if not itunes_duration:
        return None
    if itunes_duration.isdigit():
        return max(1, int(itunes_duration) // 60)
    parts = itunes_duration.split(":")
    try:
        nums = [int(p) for p in parts]
    except ValueError:
        return None
    if len(nums) == 3:
        h, m, s = nums
        return max(1, round((h * 3600 + m * 60 + s) / 60))
    if len(nums) == 2:
        m, s = nums
        return max(1, round((m * 60 + s) / 60))
    return None


def _fetch_rss_episodes(feed_url: str, cutoff: datetime) -> list[dict]:
    with urllib.request.urlopen(feed_url, timeout=120) as resp:
        root = ET.fromstring(resp.read())

    episodes: list[dict] = []
    for item in root.findall(".//item"):
        title_el = item.find("title")
        if title_el is None or not title_el.text:
            continue
        title = title_el.text.strip()
        pub_el = item.find("pubDate")
        if pub_el is None or not pub_el.text:
            continue
        pub_dt = parsedate_to_datetime(pub_el.text)
        if pub_dt.tzinfo is None:
            pub_dt = pub_dt.replace(tzinfo=timezone.utc)
        if pub_dt < cutoff:
            continue

        guest, ep_title, ep_num = _parse_rss_title(title)
        enc = item.find("enclosure")
        audio_url = enc.get("url") if enc is not None else ""
        link = (item.find("link").text or "").strip() if item.find("link") is not None else ""
        duration = _parse_duration(item.find(_itunes("duration")).text if item.find(_itunes("duration")) is not None else None)

        episodes.append(
            {
                "id": f"ep{ep_num}" if ep_num else None,
                "episode_number": ep_num,
                "title": ep_title,
                "guest": guest,
                "guest_role": "",
                "date": pub_dt.strftime("%Y-%m-%d"),
                "duration_minutes": duration or 60,
                "audio_url": audio_url,
                "apple_url": link,
                "youtube_url": "",
                "rss_title": title,
            }
        )
    episodes.sort(key=lambda e: e["episode_number"] or 0, reverse=True)
    return episodes


def _fetch_youtube_catalog() -> list[dict]:
    cmd = [
        ytdlp_bin(),
        "--ignore-errors",
        "--print",
        "%(id)s\t%(title)s\t%(description)s",
        YOUTUBE_CHANNEL,
    ]
    result = subprocess.run(cmd, capture_output=True, text=True, timeout=600)
    if result.returncode not in (0, 1):
        raise RuntimeError(f"yt-dlp failed: {result.stderr}")

    catalog: list[dict] = []
    for line in result.stdout.splitlines():
        if not line.strip() or "\t" not in line:
            continue
        vid, title, desc = line.split("\t", 2)
        catalog.append({"id": vid.strip(), "title": title.strip(), "description": desc.strip()})
    return catalog


def _match_youtube(episodes: list[dict], yt_catalog: list[dict]) -> None:
    used_vids: set[str] = set()
    for ep in episodes:
        guest_norm = _normalize_name(ep["guest"])
        if not guest_norm:
            continue
        guest_tokens = guest_norm.split()
        best: tuple[int, dict] | None = None
        for vid in yt_catalog:
            if vid["id"] in used_vids:
                continue
            hay = _normalize_name(vid["title"] + " " + vid["description"][:800])
            score = 0
            if guest_norm in hay:
                score += 10
            elif all(t in hay for t in guest_tokens if len(t) > 2):
                score += 6
            elif guest_tokens and guest_tokens[0] in hay:
                score += 3
            ep_num = ep.get("episode_number")
            if ep_num and re.search(rf"\bEP\.?\s*{ep_num}\b", vid["description"], re.I):
                score += 20
            if score > 0 and (best is None or score > best[0]):
                best = (score, vid)
        if best and best[0] >= 6:
            vid = best[1]
            ep["youtube_url"] = f"https://www.youtube.com/watch?v={vid['id']}"
            ep["youtube_title"] = vid["title"]
            used_vids.add(vid["id"])


def discover(cutoff: datetime | None = None) -> dict:
    cutoff = cutoff or DEFAULT_CUTOFF
    feed_url = _fetch_feed_url()
    episodes = _fetch_rss_episodes(feed_url, cutoff)
    yt_catalog = _fetch_youtube_catalog()
    _match_youtube(episodes, yt_catalog)

    with_yt = sum(1 for e in episodes if e.get("youtube_url"))
    payload = {
        "discovered_at": datetime.now(timezone.utc).isoformat(),
        "feed_url": feed_url,
        "cutoff_date": cutoff.strftime("%Y-%m-%d"),
        "total": len(episodes),
        "with_youtube": with_yt,
        "episodes": episodes,
    }
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(json.dumps(payload, indent=2, ensure_ascii=False), encoding="utf-8")
    return payload


def main() -> None:
    payload = discover()
    print(f"Discovered {payload['total']} episodes since {payload['cutoff_date']}")
    print(f"YouTube matched: {payload['with_youtube']}")
    print(f"Saved → {OUT}")


if __name__ == "__main__":
    main()
