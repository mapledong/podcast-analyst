#!/usr/bin/env python3
"""Match Founders YouTube channel videos to discovered episodes by title.

Transcript fetching (--transcripts) is rate-limited by default to avoid YouTube 429 /
IP blocks: **2 episodes per run**, **90s** between requests (+ random jitter), and
exponential backoff (90s → 180s → 360s, max 3 retries) on transient failures.
Prefer many small runs (see `.github/workflows/youtube-captions.yml`) over bulk fetch.
Use --all only with YOUTUBE_CAPTION_BULK_OK=1, or override with --batch-size / --delay.
"""

from __future__ import annotations

import argparse
import json
import re
import subprocess
import sys
import tempfile
import time
import unicodedata
from difflib import SequenceMatcher
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))

from scripts.resolve_curated_bb_founders import resolve_curated  # noqa: E402
from scripts.youtube_caption_limits import (  # noqa: E402
    DEFAULT_BATCH_SIZE,
    DEFAULT_TRANSCRIPT_DELAY,
    reject_bulk_unless_forced,
    sleep_between_episodes,
    with_transcript_backoff,
)
from scripts.ytdlp_bin import ytdlp_bin  # noqa: E402
from src.expand import resolve_transcript_path  # noqa: E402
from src.fetch_transcript import extract_video_id, fetch_transcript  # noqa: E402

DISCOVERED = ROOT / "data" / "discovered" / "founders_episodes.json"
APPROVED = ROOT / "data" / "approved"
YOUTUBE_CHANNEL = "https://www.youtube.com/@founderspodcast1/videos"

# High-confidence overrides when RSS/YouTube titles diverge but mapping is known.
MANUAL_BY_EPISODE: dict[int, str] = {
    376: "Sywq2Ua4GXw",  # How Jensen Works → Jensen Huang: Founder of Nvidia
    420: "JjV1uikElgs",  # Steve Jobs in Exile
    286: "t47NBQqlzbk",  # 400 Pages of Warren Buffett and Charlie Munger…
    2: "Hc3u0bUu8eg",  # The Biography of Walt Disney
    3: "KMnV7mX0EQM",  # The Biography of Thomas Edison
    190: "KzXxxbuTAAg",  # Henry Ford's Autobiography
    233: "GmmuNVv4ehE",  # Peter Thiel's Ideas (PayPal mafia episode)
}

MIN_MATCH_SCORE = 70

STOP = frozenset(
    {
        "the",
        "a",
        "an",
        "of",
        "and",
        "in",
        "on",
        "to",
        "for",
        "how",
        "who",
        "is",
        "his",
        "her",
        "from",
        "with",
        "by",
        "at",
        "it",
        "that",
        "this",
        "their",
        "our",
        "your",
        "all",
        "works",
        "worked",
        "thinks",
    }
)


def _normalize(text: str) -> str:
    text = unicodedata.normalize("NFKD", text).encode("ascii", "ignore").decode()
    text = text.lower()
    text = re.sub(r"[^a-z0-9\s]", " ", text)
    return re.sub(r"\s+", " ", text).strip()


def _tokens(text: str) -> set[str]:
    return {t for t in _normalize(text).split() if t not in STOP and len(t) > 2}


def _episode_number_in_title(ep_num: int, title: str) -> bool:
    """Match explicit episode markers in YouTube titles (#421, EP 421), not bare digits."""
    patterns = (
        rf"^#\s*{ep_num}\b",
        rf"^#\s*{ep_num}\s*:",
        rf"\bep(?:isode)?\.?\s*#?\s*{ep_num}\b",
        rf"\(#{ep_num}\)",
    )
    return any(re.search(p, title.strip(), re.I) for p in patterns)


def _rss_core(ep: dict) -> str:
    return re.sub(r"^#?\d+\s*:?\s*", "", ep.get("rss_title", "")).strip()


def _score_match(ep: dict, video: dict) -> tuple[int, str]:
    ep_num = int(ep.get("episode_number") or 0)
    ytitle = video["title"]
    if ep_num in MANUAL_BY_EPISODE and MANUAL_BY_EPISODE[ep_num] == video["id"]:
        return 100, "manual"

    if ep_num and _episode_number_in_title(ep_num, ytitle):
        return 100, "ep_in_title"

    candidates = [ep.get("title", ""), _rss_core(ep)]
    guest = (ep.get("guest") or "").strip()
    title = (ep.get("title") or "").strip()
    if guest and guest != title and _tokens(guest) and _tokens(guest).issubset(_tokens(title)):
        candidates.append(guest)

    best = 0
    ny = _normalize(ytitle)
    for cand in candidates:
        if not cand:
            continue
        nc = _normalize(cand)
        if nc == ny:
            return 95, "exact"
        if nc in ny or ny in nc:
            best = max(best, 88)
        best = max(best, int(SequenceMatcher(None, nc, ny).ratio() * 100))
        t1, t2 = _tokens(cand), _tokens(ytitle)
        if t1 and t2:
            overlap = len(t1 & t2)
            if overlap >= 2:
                coverage = overlap / len(t1)
                best = max(best, int(55 + coverage * 40))
    return best, "title"


def fetch_youtube_catalog(*, timeout: int = 600) -> list[dict]:
    cmd = [
        ytdlp_bin(),
        "--ignore-errors",
        "--flat-playlist",
        "--print",
        "%(id)s\t%(title)s",
        YOUTUBE_CHANNEL,
    ]
    result = subprocess.run(cmd, capture_output=True, text=True, timeout=timeout)
    if result.returncode not in (0, 1):
        raise RuntimeError(f"yt-dlp failed: {result.stderr.strip() or result.stdout.strip()}")

    catalog: list[dict] = []
    for line in result.stdout.splitlines():
        if not line.strip() or "\t" not in line:
            continue
        vid, title = line.split("\t", 1)
        catalog.append({"id": vid.strip(), "title": title.strip()})
    return catalog


def match_episodes(episodes: list[dict], catalog: list[dict]) -> dict[int, dict]:
    """Return episode_number → {id, title, url, score, reason} using one-to-one greedy assignment."""
    by_id = {v["id"]: v for v in catalog}
    used_eps: set[int] = set()
    used_vids: set[str] = set()
    matched: dict[int, dict] = {}

    for ep_num, vid in sorted(MANUAL_BY_EPISODE.items()):
        video = by_id.get(vid)
        if not video:
            continue
        matched[ep_num] = {
            "id": vid,
            "title": video["title"],
            "url": f"https://www.youtube.com/watch?v={vid}",
            "score": 100,
            "reason": "manual",
        }
        used_eps.add(ep_num)
        used_vids.add(vid)

    pairs: list[tuple[int, int, str, str, str]] = []
    for ep in episodes:
        ep_num = int(ep.get("episode_number") or 0)
        if not ep_num or ep_num in used_eps:
            continue
        for video in catalog:
            if video["id"] in used_vids:
                continue
            score, reason = _score_match(ep, video)
            if score >= MIN_MATCH_SCORE:
                pairs.append((score, ep_num, video["id"], video["title"], reason))

    pairs.sort(key=lambda row: row[0], reverse=True)
    for score, ep_num, vid, ytitle, reason in pairs:
        if ep_num in used_eps or vid in used_vids:
            continue
        matched[ep_num] = {
            "id": vid,
            "title": ytitle,
            "url": f"https://www.youtube.com/watch?v={vid}",
            "score": score,
            "reason": reason,
        }
        used_eps.add(ep_num)
        used_vids.add(vid)
    return matched


def apply_matches(episodes: list[dict], matched: dict[int, dict]) -> tuple[int, int]:
    updated = cleared = 0
    for ep in episodes:
        ep_num = int(ep.get("episode_number") or 0)
        hit = matched.get(ep_num)
        new_url = hit["url"] if hit else ""
        old_url = (ep.get("youtube_url") or "").strip()
        if new_url != old_url:
            ep["youtube_url"] = new_url
            if hit:
                ep["youtube_title"] = hit["title"]
            else:
                ep.pop("youtube_title", None)
            if new_url:
                updated += 1
            else:
                cleared += 1
    return updated, cleared


def sync_approved_founders(episodes: list[dict]) -> int:
    by_num = {int(ep["episode_number"]): ep for ep in episodes if ep.get("episode_number")}
    changed = 0
    for path in sorted(APPROVED.glob("fnd-*.json")):
        data = json.loads(path.read_text(encoding="utf-8"))
        if data.get("podcast") != "Founders":
            continue
        meta = data.setdefault("metadata", {})
        ep_num = int(meta.get("episode_number") or 0)
        ep = by_num.get(ep_num)
        if not ep:
            continue
        youtube = (ep.get("youtube_url") or "").strip()
        links = meta.setdefault("links", {})
        old_meta = (meta.get("youtube_url") or "").strip()
        old_link = (links.get("youtube") or "").strip()
        if old_meta == youtube and old_link == youtube:
            continue
        meta["youtube_url"] = youtube
        if youtube:
            links["youtube"] = youtube
        else:
            links.pop("youtube", None)
        path.write_text(json.dumps(data, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
        changed += 1
        print(f"  synced {path.name} → {youtube or '(cleared)'}")
    return changed


def load_episodes() -> tuple[dict, list[dict]]:
    payload = json.loads(DISCOVERED.read_text(encoding="utf-8"))
    return payload, payload["episodes"]


def save_episodes(payload: dict) -> None:
    DISCOVERED.write_text(json.dumps(payload, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")


def curated_episode_numbers() -> list[int]:
    import yaml

    cfg = yaml.safe_load((ROOT / "config" / "curated_bb_founders.yaml").read_text(encoding="utf-8"))
    return [int(e["episode_number"]) for e in cfg.get("founders", [])]


def _ytdlp() -> str:
    return ytdlp_bin()


def _is_youtube_transcript(path: Path | None) -> bool:
    if path is None or not path.exists():
        return False
    head = path.read_text(encoding="utf-8", errors="replace")[:200]
    return "# source: youtube/" in head


def _vtt_to_text(vtt: str) -> str:
    lines: list[str] = []
    seen: set[str] = set()
    for raw in vtt.splitlines():
        line = raw.strip()
        if not line or line.startswith("WEBVTT") or line.startswith("NOTE") or "-->" in line:
            continue
        if re.match(r"^\d+$", line):
            continue
        if line.startswith("Kind:") or line.startswith("Language:"):
            continue
        cleaned = re.sub(r"<[^>]+>", "", line).strip()
        if cleaned and cleaned not in seen:
            seen.add(cleaned)
            lines.append(cleaned)
    return "\n".join(lines)


def _json3_to_text(raw: str) -> str:
    data = json.loads(raw)
    lines: list[str] = []
    seen: set[str] = set()
    for event in data.get("events") or []:
        for seg in event.get("segs") or []:
            t = (seg.get("utf8") or "").strip()
            if t and t not in seen:
                seen.add(t)
                lines.append(t)
    return "\n".join(lines)


def _ytdlp_subtitle_url(url: str) -> str | None:
    cmd = [
        _ytdlp(),
        "--extractor-args",
        "youtube:player_client=android",
        "--dump-json",
        "--skip-download",
        url,
    ]
    result = subprocess.run(cmd, capture_output=True, text=True, timeout=180)
    if result.returncode != 0:
        return None
    try:
        info = json.loads(result.stdout)
    except json.JSONDecodeError:
        return None
    for key in ("subtitles", "automatic_captions"):
        for lang in ("en", "en-US", "en-GB"):
            tracks = (info.get(key) or {}).get(lang) or []
            for track in tracks:
                if track.get("url"):
                    return track["url"]
    return None


def _fetch_subtitle_url(url: str) -> tuple[str, int]:
    import urllib.request

    sub_url = _ytdlp_subtitle_url(url)
    if not sub_url:
        raise RuntimeError("no subtitle URL in yt-dlp metadata")
    sep = "&" if "?" in sub_url else "?"
    headers = {
        "User-Agent": (
            "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) "
            "AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
        ),
        "Accept-Language": "en-US,en;q=0.9",
    }
    for fmt in ("json3", "vtt"):
        req = urllib.request.Request(f"{sub_url}{sep}fmt={fmt}", headers=headers)
        with urllib.request.urlopen(req, timeout=60) as resp:
            body = resp.read().decode("utf-8", errors="replace")
        text = _json3_to_text(body) if fmt == "json3" else _vtt_to_text(body)
        line_count = len([ln for ln in text.splitlines() if ln.strip()])
        if line_count >= 50:
            return text, line_count
    raise RuntimeError("subtitle payload too short")


def _fetch_ytdlp_auto_sub(url: str) -> tuple[str, int]:
    """Download auto-generated English subtitles via yt-dlp metadata or auto-sub file."""
    try:
        return _fetch_subtitle_url(url)
    except Exception as exc:
        if _is_transient_youtube_error(exc):
            raise
    with tempfile.TemporaryDirectory() as tmp:
        out_tpl = str(Path(tmp) / "%(id)s")
        cmd = [
            _ytdlp(),
            "--extractor-args",
            "youtube:player_client=android",
            "--write-auto-sub",
            "--sub-langs",
            "en,en-US,en-GB",
            "--skip-download",
            "--sub-format",
            "vtt/best",
            "-o",
            out_tpl,
            url,
        ]
        result = subprocess.run(cmd, capture_output=True, text=True, timeout=180)
        if result.returncode != 0:
            err = result.stderr.strip() or result.stdout.strip() or "yt-dlp failed"
            raise RuntimeError(err)
        vtt_files = sorted(Path(tmp).glob("*.vtt"))
        if not vtt_files:
            raise RuntimeError("no VTT subtitles from yt-dlp")
        text = _vtt_to_text(vtt_files[0].read_text(encoding="utf-8", errors="replace"))
        line_count = len([ln for ln in text.splitlines() if ln.strip()])
        if line_count < 50:
            raise RuntimeError(f"subtitle too short ({line_count} lines)")
        return text, line_count


def _save_episode_transcript(ep: dict, *, video_id: str, text: str, source: str, line_count: int) -> None:
    transcripts = ROOT / "data" / "transcripts"
    transcripts.mkdir(parents=True, exist_ok=True)
    header = (
        f"# source: youtube/{source}\n"
        f"# episode_id: {ep['id']}\n"
        f"# video_id: {video_id}\n"
        f"# lines: {line_count}\n\n"
    )
    (transcripts / f"{ep['id']}.txt").write_text(header + text + "\n", encoding="utf-8")
    (transcripts / f"{video_id}.txt").write_text(
        f"# source: youtube/{source}\n"
        f"# video_id: {video_id}\n"
        f"# lines: {line_count}\n\n"
        + text
        + "\n",
        encoding="utf-8",
    )


def _fetch_episode_transcript(ep: dict, yt: str) -> tuple[str, str, int]:
    """Fetch transcript text for one episode; raises on failure."""

    def _do_fetch() -> tuple[str, str, int]:
        try:
            text, line_count = _fetch_ytdlp_auto_sub(yt)
            return text, "ytdlp-auto", line_count
        except Exception as ytdlp_exc:
            result = fetch_transcript(yt)
            return result.text, result.source, result.line_count

    text, source, line_count = with_transcript_backoff(_do_fetch, episode_id=ep["id"])
    return text, source, line_count


def fetch_founders_transcripts(
    *,
    delay: float = DEFAULT_TRANSCRIPT_DELAY,
    batch_size: int = DEFAULT_BATCH_SIZE,
    process_all: bool = False,
    unapproved_only: bool = True,
    episode_ids: set[str] | None = None,
) -> tuple[int, int, int]:
    """Fetch YouTube transcripts for curated Founders episodes via yt-dlp auto-subs."""
    rows = resolve_curated()["Founders"]
    ok = skip = fail = 0
    queue: list[dict] = []

    for ep in rows:
        if episode_ids is not None and ep["id"] not in episode_ids:
            continue
        if unapproved_only and ep.get("approved"):
            skip += 1
            continue
        yt = (ep.get("youtube_url") or "").strip()
        if not yt:
            skip += 1
            continue
        stub = {"episode_id": ep["id"], "podcast": "Founders", "metadata": ep}
        existing = resolve_transcript_path(stub)
        if _is_youtube_transcript(existing):
            skip += 1
            continue
        try:
            vid = extract_video_id(yt)
        except ValueError:
            skip += 1
            continue
        vid_path = ROOT / "data" / "transcripts" / f"{vid}.txt"
        if _is_youtube_transcript(vid_path):
            skip += 1
            continue
        queue.append(ep)

    queue.sort(key=lambda e: (bool(e.get("approved")), e["id"]))
    to_process = queue if process_all else queue[:batch_size]
    batch_total = len(to_process)

    if not to_process:
        return ok, skip, fail

    print(
        f"Transcript queue: {len(queue)} pending"
        + ("" if process_all else f", processing batch of {batch_total}")
    )

    for idx, ep in enumerate(to_process, start=1):
        yt = (ep.get("youtube_url") or "").strip()
        print(f"batch {idx}/{batch_total}: {ep['id']} …")
        try:
            text, source, line_count = _fetch_episode_transcript(ep, yt)
            vid = extract_video_id(yt)
            _save_episode_transcript(
                ep, video_id=vid, text=text, source=source, line_count=line_count
            )
            print(f"✓ {ep['id']} {source} ({line_count} lines)")
            ok += 1
        except Exception as exc:
            print(f"✗ {ep['id']}: {exc}")
            fail += 1
        if idx < batch_total:
            sleep_between_episodes(delay)

    if not process_all and len(queue) > batch_total:
        remaining = len(queue) - batch_total
        print(f"  {remaining} episode(s) remain in queue; rerun or pass --all")

    return ok, skip, fail


def main() -> None:
    parser = argparse.ArgumentParser(description="Match Founders YouTube videos to discovered episodes")
    parser.add_argument("--dry-run", action="store_true", help="Print matches without writing files")
    parser.add_argument(
        "--no-sync-approved",
        action="store_true",
        help="Skip updating data/approved/fnd-*.json youtube links",
    )
    parser.add_argument("--curated-only", action="store_true", help="Only match/report curated 30 episodes")
    parser.add_argument("--stats", action="store_true", help="Print match summary")
    parser.add_argument(
        "--transcripts",
        action="store_true",
        help="Fetch YouTube transcripts for unapproved curated Founders with youtube_url",
    )
    parser.add_argument(
        "--all",
        action="store_true",
        help="With --transcripts: process the full pending queue (requires YOUTUBE_CAPTION_BULK_OK=1)",
    )
    parser.add_argument(
        "--batch-size",
        type=int,
        default=DEFAULT_BATCH_SIZE,
        help=f"Max episodes per --transcripts run (default: {DEFAULT_BATCH_SIZE})",
    )
    parser.add_argument(
        "--delay",
        type=float,
        default=DEFAULT_TRANSCRIPT_DELAY,
        help=f"Seconds between transcript fetches (default: {DEFAULT_TRANSCRIPT_DELAY:.0f})",
    )
    parser.add_argument(
        "ids",
        nargs="*",
        help="Optional episode IDs to fetch (default: full pending queue)",
    )
    args = parser.parse_args()

    if args.transcripts:
        reject_bulk_unless_forced(bulk_flag=args.all, flag_name="--all")
        id_filter = set(args.ids) if args.ids else None
        ok, skip, fail = fetch_founders_transcripts(
            delay=args.delay,
            batch_size=args.batch_size,
            process_all=args.all,
            episode_ids=id_filter,
        )
        print(f"\nTranscripts: fetched {ok}, skipped {skip}, failed {fail}")
        return

    payload, episodes = load_episodes()
    catalog = fetch_youtube_catalog()
    matched = match_episodes(episodes, catalog)

    report_eps = episodes
    if args.curated_only:
        curated = set(curated_episode_numbers())
        report_eps = [ep for ep in episodes if int(ep.get("episode_number") or 0) in curated]

    if args.stats or args.dry_run:
        with_yt = sum(1 for ep in report_eps if int(ep.get("episode_number") or 0) in matched)
        print(f"YouTube catalog: {len(catalog)} videos")
        print(f"Matched episodes: {len(matched)} total ({with_yt}/{len(report_eps)} curated)")
        for ep in sorted(report_eps, key=lambda e: int(e.get("episode_number") or 0), reverse=True):
            ep_num = int(ep.get("episode_number") or 0)
            hit = matched.get(ep_num)
            if hit:
                print(f"  #{ep_num:3d} [{hit['score']:2d}] {ep['title'][:40]:40s} → {hit['title'][:50]}")
            elif args.curated_only:
                print(f"  #{ep_num:3d} --  {ep['title'][:40]}")

    if args.dry_run:
        return

    updated, cleared = apply_matches(episodes, matched)
    save_episodes(payload)
    print(f"Updated {DISCOVERED.name}: {updated} new/changed, {cleared} cleared")

    if not args.no_sync_approved:
        n = sync_approved_founders(episodes)
        print(f"Synced {n} approved Founders JSON files")


if __name__ == "__main__":
    main()
