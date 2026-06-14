"""Shared helpers for acq batch 491-500 write script."""
from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DISCOVERED = json.loads((ROOT / "data" / "discovered" / "acquired_episodes.json").read_text())
META = {e["id"]: e for e in DISCOVERED["episodes"]}

APPLE = "https://podcasts.apple.com/podcast/acquired/id1050462261"
SPOTIFY = "https://open.spotify.com/show/2HI3KdjtJnr3E8B4W8Y0Yx"
HOST = "Ben Gilbert & David Rosenthal"
EXTRACTION = {
    "model": "manual-gpt-agent-v5.1-acquired",
    "transcript_source": "acquired.fm",
    "status": "approved",
    "template_version": "5.1-acquired",
}


def links(ep: dict) -> dict:
    out = {
        "acquired": ep["acquired_url"],
        "apple_podcasts": APPLE,
        "spotify": SPOTIFY,
    }
    yt = ep.get("youtube_url") or ""
    if yt:
        out["youtube"] = yt
    return out


def base(ep_id: str, **kwargs) -> dict:
    ep = META[ep_id]
    m = {
        "episode_number": ep["episode_number"],
        "title": ep["title"],
        "guest": ep["guest"],
        "guest_role": ep["guest_role"],
        "date": ep["date"],
        "duration_minutes": ep["duration_minutes"],
        "youtube_url": ep.get("youtube_url") or "",
        "links": links(ep),
    }
    return {
        "episode_id": ep_id,
        "podcast": "Acquired",
        "host": HOST,
        "metadata": m,
        "extraction_meta": EXTRACTION,
        "review_notes": "Manual GPT Acquired batch v5.1 — episodes 491-500",
        **kwargs,
    }
