#!/usr/bin/env python3
"""Discover Acquired episodes: RSS metadata + sitemap slug resolution."""

from __future__ import annotations

import argparse
import json
import re
import urllib.request
import xml.etree.ElementTree as ET
from datetime import datetime, timezone
from email.utils import parsedate_to_datetime
from html import unescape
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
OUT = ROOT / "data" / "discovered" / "acquired_episodes.json"
FEED_URL = "https://feeds.transistor.fm/acquired"
SITEMAP_URL = "https://www.acquired.fm/sitemap.xml"
ITUNES_NS = "http://www.itunes.com/dtds/podcast-1.0.dtd"
# Hand-summarized under acq-sp26-* ids; skip duplicate discovery entries
SKIP_SLUGS = {"vanguard", "ferrari", "formula-1"}
# Not full episodes
SKIP_SLUG_PATTERNS = (r"^trailer", r"^acq2-")


def _itunes(tag: str) -> str:
    return f"{{{ITUNES_NS}}}{tag}"


def _parse_duration(raw: str | None) -> int:
    if not raw:
        return 120
    raw = raw.strip()
    if raw.isdigit():
        return max(1, int(raw) // 60)
    parts = raw.split(":")
    try:
        nums = [int(p) for p in parts]
    except ValueError:
        return 120
    if len(nums) == 3:
        h, m, s = nums
        return max(1, round((h * 3600 + m * 60 + s) / 60))
    if len(nums) == 2:
        m, s = nums
        return max(1, round((m * 60 + s) / 60))
    return 120


def _slug_from_link(link: str) -> str:
    slug = link.rstrip("/").split("/")[-1]
    if slug in ("acquired.fm", "episodes", ""):
        return ""
    return slug


def _norm_title(title: str) -> str:
    t = re.sub(r"\s*\|\s*Acquired\s*$", "", title, flags=re.I)
    t = re.sub(r"^(Episode|Ep\.?)\s*\d+[:\.\s-]+", "", t, flags=re.I)
    t = re.sub(r"^Acquired Episode \d+[:\.\s-]+", "", t, flags=re.I)
    t = re.sub(r"^Acquired Special Episode[:\.\s-]+", "", t, flags=re.I)
    return re.sub(r"[^a-z0-9]+", " ", t.lower()).strip()


def _slug_norm(slug: str) -> str:
    return re.sub(r"[^a-z0-9]+", " ", slug.replace("-", " ")).strip()


def _fetch_sitemap_slugs() -> list[str]:
    with urllib.request.urlopen(SITEMAP_URL, timeout=120) as resp:
        html = resp.read().decode("utf-8", errors="replace")
    slugs = re.findall(r"/episodes/([^<\"]+)", html)
    seen: set[str] = set()
    out: list[str] = []
    for slug in slugs:
        slug = slug.strip().rstrip("/")
        if not slug or slug in seen:
            continue
        if any(re.search(p, slug) for p in SKIP_SLUG_PATTERNS):
            continue
        seen.add(slug)
        out.append(slug)
    return out


def _fetch_page_meta(slug: str) -> dict:
    url = f"https://www.acquired.fm/episodes/{slug}"
    try:
        with urllib.request.urlopen(url, timeout=60) as resp:
            page = resp.read().decode("utf-8", errors="replace")
    except Exception:
        return {}
    meta: dict[str, str] = {}
    for prop, key in (
        (r'<meta property="og:title" content="([^"]+)"', "og_title"),
        (r'<meta name="twitter:title" content="([^"]+)"', "twitter_title"),
    ):
        m = re.search(prop, page)
        if m:
            meta[key] = unescape(m.group(1))
    yt = re.search(r"https://www\.youtube\.com/watch\?v=[A-Za-z0-9_-]+", page)
    if yt:
        meta["youtube_url"] = yt.group(0)
    return meta


def _guest_role(season: str, episode: str) -> str:
    if season and episode:
        return f"Season {season} · Episode {episode}"
    if season:
        return f"Season {season}"
    return "Acquired"


def _parse_rss() -> tuple[list[dict], dict[str, dict], dict[str, dict]]:
    """Return (all_items, by_slug, by_norm_title)."""
    with urllib.request.urlopen(FEED_URL, timeout=120) as resp:
        root = ET.fromstring(resp.read())

    items: list[dict] = []
    by_slug: dict[str, dict] = {}
    by_title: dict[str, dict] = {}

    for item in root.findall("channel/item"):
        etype = item.findtext(_itunes("episodeType")) or "full"
        if etype == "trailer":
            continue
        link = (item.findtext("link") or "").strip()
        slug = _slug_from_link(link)
        duration = _parse_duration(item.findtext(_itunes("duration")))
        pub = item.findtext("pubDate")
        date = parsedate_to_datetime(pub).strftime("%Y-%m-%d") if pub else ""
        title_short = (item.findtext("title") or "").strip()
        season = (item.findtext(_itunes("season")) or "").strip()
        epnum = (item.findtext(_itunes("episode")) or "").strip()
        row = {
            "slug": slug,
            "title_short": title_short,
            "guest": title_short,
            "date": date,
            "duration_minutes": duration,
            "season": season,
            "episode": epnum,
            "acquired_url": link if slug else "",
            "norm_title": _norm_title(title_short),
        }
        items.append(row)
        if slug:
            by_slug[slug] = row
        nt = row["norm_title"]
        if nt and nt not in by_title:
            by_title[nt] = row
    return items, by_slug, by_title


def _match_rss_row(slug: str, by_slug: dict[str, dict], by_title: dict[str, dict]) -> dict | None:
    if slug in by_slug:
        return by_slug[slug]
    sn = _slug_norm(slug)
    if sn in by_title:
        return by_title[sn]
    # Partial match: slug words contained in title norm
    slug_words = set(sn.split())
    if slug_words:
        best: dict | None = None
        best_score = 0
        for nt, row in by_title.items():
            title_words = set(nt.split())
            score = len(slug_words & title_words)
            if score > best_score and score >= max(1, len(slug_words) - 1):
                best_score = score
                best = row
        if best:
            return best
    return None


def discover(
    *,
    limit: int | None = 50,
    min_minutes: int = 30,
    fetch_meta: bool = False,
    all_episodes: bool = False,
) -> dict:
    sitemap_slugs = _fetch_sitemap_slugs()
    _, by_slug, by_title = _parse_rss()

    episodes: list[dict] = []
    unmatched: list[str] = []

    for slug in sitemap_slugs:
        if slug in SKIP_SLUGS:
            continue
        rss = _match_rss_row(slug, by_slug, by_title)
        meta = _fetch_page_meta(slug) if fetch_meta else {}
        page_title = meta.get("og_title") or meta.get("twitter_title") or ""
        page_title = re.sub(r"\s*\|\s*Acquired\s*$", "", page_title, flags=re.I).strip()

        if rss:
            title = page_title or rss["title_short"]
            title = re.sub(r"\s*\|\s*Acquired\s*$", "", title, flags=re.I).strip()
            date = rss["date"]
            duration = rss["duration_minutes"]
            season = rss["season"]
            epnum = rss["episode"]
            acquired_url = rss["acquired_url"] or f"https://www.acquired.fm/episodes/{slug}"
        else:
            unmatched.append(slug)
            title = page_title or slug.replace("-", " ").title()
            date = ""
            duration = 120
            season = ""
            epnum = ""
            acquired_url = f"https://www.acquired.fm/episodes/{slug}"

        if duration < min_minutes:
            continue

        episodes.append(
            {
                "id": f"acq-{slug}",
                "slug": slug,
                "episode_number": 0,
                "title": title,
                "guest": title,
                "guest_role": _guest_role(season, epnum),
                "date": date,
                "duration_minutes": duration,
                "youtube_url": meta.get("youtube_url", ""),
                "acquired_url": acquired_url,
                "season": season,
                "season_episode": epnum,
            }
        )

    # Newest first (by date, then slug)
    episodes.sort(key=lambda e: (e["date"] or "1970-01-01", e["slug"]), reverse=True)

    if not all_episodes and limit is not None:
        episodes = episodes[:limit]

    return {
        "discovered_at": datetime.now(timezone.utc).isoformat(),
        "feed_url": FEED_URL,
        "sitemap_url": SITEMAP_URL,
        "limit": limit,
        "all_episodes": all_episodes,
        "total_sitemap": len(sitemap_slugs),
        "total_matched": len(episodes),
        "unmatched_slugs": unmatched[:20],
        "episodes": episodes,
    }


def main() -> None:
    parser = argparse.ArgumentParser(description="Discover Acquired episodes")
    parser.add_argument("--limit", type=int, default=50, help="Max episodes (ignored with --all)")
    parser.add_argument("--all", action="store_true", help="Include all sitemap episodes")
    parser.add_argument("--min-minutes", type=int, default=30)
    parser.add_argument("--fetch-meta", action="store_true", help="Fetch og:title and YouTube from pages")
    args = parser.parse_args()
    data = discover(
        limit=None if args.all else args.limit,
        min_minutes=args.min_minutes,
        fetch_meta=args.fetch_meta,
        all_episodes=args.all,
    )
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(json.dumps(data, indent=2, ensure_ascii=False), encoding="utf-8")
    print(f"Wrote {len(data['episodes'])} episodes → {OUT} (sitemap {data['total_sitemap']})")
    if data.get("unmatched_slugs"):
        print(f"Unmatched RSS (sample): {data['unmatched_slugs'][:5]}")
    for ep in data["episodes"][:5]:
        print(f"  {ep['id']} · {ep['date']} · {ep['duration_minutes']}m · {ep['title'][:60]}")


if __name__ == "__main__":
    main()
