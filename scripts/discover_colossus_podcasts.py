#!/usr/bin/env python3
"""Discover Business Breakdowns and Founders episodes from Megaphone RSS."""

from __future__ import annotations

import argparse
import json
import re
import urllib.request
import xml.etree.ElementTree as ET
from email.utils import parsedate_to_datetime
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
OUT_BB = ROOT / "data" / "discovered" / "business_breakdowns_episodes.json"
OUT_FND = ROOT / "data" / "discovered" / "founders_episodes.json"
ITUNES = "http://www.itunes.com/dtds/podcast-1.0.dtd"
FEEDS = {
    "Business Breakdowns": "https://feeds.megaphone.fm/breakdowns",
    "Founders": "https://feeds.megaphone.fm/DSLLC6297708582",
}
UA = "Mozilla/5.0 (podcast-analyst/1.0)"


def _it(tag: str) -> str:
    return f"{{{ITUNES}}}{tag}"


def _parse_duration(raw: str | None) -> int:
    if not raw:
        return 60
    raw = raw.strip()
    if raw.isdigit():
        return max(1, int(raw) // 60)
    parts = raw.split(":")
    try:
        nums = [int(p) for p in parts]
    except ValueError:
        return 60
    if len(nums) == 3:
        h, m, s = nums
        return max(1, round((h * 3600 + m * 60 + s) / 60))
    if len(nums) == 2:
        m, s = nums
        return max(1, round((m * 60 + s) / 60))
    return 60


def _slug(text: str, max_len: int = 55) -> str:
    s = re.sub(r"[^a-z0-9]+", "-", text.lower()).strip("-")
    s = re.sub(r"-+", "-", s)
    return s[:max_len].strip("-")


def _episode_id(podcast: str, ep_num: int, title: str) -> str:
    prefix = "bb" if podcast == "Business Breakdowns" else "fnd"
    slug = _slug(title)
    if prefix == "fnd":
        return f"{prefix}-{ep_num}-{slug}" if ep_num else f"{prefix}-{slug}"
    return f"{prefix}-{slug}"


def _parse_bb_title(rss_title: str) -> tuple[int, str]:
    m = re.search(r"EP\.?\s*(\d+)", rss_title, re.I)
    ep_num = int(m.group(1)) if m else 0
    core = re.sub(r"\s*-\s*\[Business Breakdowns.*$", "", rss_title, flags=re.I).strip()
    core = re.sub(r"\s*-\s*\[Web3 Breakdowns.*$", "", core, flags=re.I).strip()
    return ep_num, core


def _parse_fnd_title(rss_title: str) -> tuple[int, str]:
    m = re.match(r"#?(\d+)\s*:?\s+(.*)$", rss_title.strip())
    if m:
        return int(m.group(1)), m.group(2).strip()
    return 0, rss_title.strip()


def _guest_from_bb_title(title: str) -> tuple[str, str]:
    if ":" in title:
        guest, rest = title.split(":", 1)
        return guest.strip(), rest.strip()
    return title.strip(), "Public company breakdown"


def _fetch_youtube(colossus_url: str) -> str:
    if not colossus_url:
        return ""
    try:
        req = urllib.request.Request(colossus_url, headers={"User-Agent": UA})
        with urllib.request.urlopen(req, timeout=60) as resp:
            page = resp.read().decode("utf-8", errors="replace")
        m = re.search(
            r"(?:youtube\.com/(?:watch\?v=|embed/)|youtu\.be/)([A-Za-z0-9_-]{11})",
            page,
        )
        return f"https://www.youtube.com/watch?v={m.group(1)}" if m else ""
    except Exception:
        return ""


def discover_podcast(name: str, *, fetch_youtube: bool = False) -> list[dict]:
    feed_url = FEEDS[name]
    with urllib.request.urlopen(feed_url, timeout=120) as resp:
        root = ET.fromstring(resp.read())

    episodes: list[dict] = []
    for item in root.findall(".//item"):
        rss_title = (item.findtext("title") or "").strip()
        if not rss_title or any(x in rss_title.lower() for x in ("trailer", "welcome to")):
            continue

        if name == "Business Breakdowns":
            ep_num, title = _parse_bb_title(rss_title)
            guest, guest_role = _guest_from_bb_title(title)
        else:
            ep_num, title = _parse_fnd_title(rss_title)
            guest = title.split(":")[0].strip() if ":" in title else title
            guest_role = f"Biography · Episode {ep_num}" if ep_num else "Biography"

        link = (item.findtext("link") or "").strip()
        pub_el = item.find("pubDate")
        date = ""
        if pub_el is not None and pub_el.text:
            try:
                dt = parsedate_to_datetime(pub_el.text)
                date = dt.strftime("%Y-%m-%d")
            except Exception:
                pass

        enc = item.find("enclosure")
        audio_url = enc.get("url") if enc is not None else ""
        duration = _parse_duration(item.findtext(_it("duration")))

        colossus_url = link if "colossus.com" in link or "joincolossus.com" in link else ""
        yt = _fetch_youtube(colossus_url) if fetch_youtube and colossus_url else ""

        eid = _episode_id(name, ep_num, title)
        episodes.append(
            {
                "id": eid,
                "episode_number": ep_num,
                "title": title,
                "guest": guest,
                "guest_role": guest_role,
                "date": date,
                "duration_minutes": duration,
                "colossus_url": colossus_url,
                "audio_url": audio_url,
                "youtube_url": yt,
                "rss_title": rss_title,
                "podcast": name,
            }
        )

    if name == "Business Breakdowns":
        episodes.sort(key=lambda e: e["episode_number"], reverse=True)
    else:
        episodes.sort(key=lambda e: e["episode_number"], reverse=True)
    return episodes


def _merge_existing_youtube(episodes: list[dict], path: Path) -> None:
    if not path.exists():
        return
    try:
        old = {int(e["episode_number"]): e for e in json.loads(path.read_text(encoding="utf-8")).get("episodes", [])}
    except Exception:
        return
    for ep in episodes:
        num = int(ep.get("episode_number") or 0)
        prev = old.get(num)
        if prev and prev.get("youtube_url") and not ep.get("youtube_url"):
            ep["youtube_url"] = prev["youtube_url"]
            if prev.get("youtube_title"):
                ep["youtube_title"] = prev["youtube_title"]


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--youtube", action="store_true", help="Fetch YouTube URLs from Colossus pages (slow)")
    parser.add_argument(
        "--founders-youtube",
        action="store_true",
        help="After RSS refresh, match Founders episodes to @founderspodcast1",
    )
    args = parser.parse_args()

    bb = discover_podcast("Business Breakdowns", fetch_youtube=args.youtube)
    fnd = discover_podcast("Founders", fetch_youtube=False)
    _merge_existing_youtube(fnd, OUT_FND)

    OUT_BB.parent.mkdir(parents=True, exist_ok=True)
    OUT_BB.write_text(json.dumps({"podcast": "Business Breakdowns", "episodes": bb}, indent=2), encoding="utf-8")
    OUT_FND.write_text(json.dumps({"podcast": "Founders", "episodes": fnd}, indent=2), encoding="utf-8")
    print(f"Business Breakdowns: {len(bb)} → {OUT_BB}")
    print(f"Founders: {len(fnd)} → {OUT_FND}")

    if args.founders_youtube or args.youtube:
        from scripts.fetch_founders_youtube import (  # noqa: WPS433
            apply_matches,
            fetch_youtube_catalog,
            load_episodes,
            match_episodes,
            save_episodes,
            sync_approved_founders,
        )

        payload, episodes = load_episodes()
        matched = match_episodes(episodes, fetch_youtube_catalog())
        updated, _ = apply_matches(episodes, matched)
        save_episodes(payload)
        sync_approved_founders(episodes)
        print(f"Founders YouTube: matched {len(matched)}, updated {updated}")


if __name__ == "__main__":
    main()
