"""Shared helpers for early-season Acquired v5.1 batch writes."""
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


def word_count(text: str) -> int:
    return len(text.split())


def links(ep: dict) -> dict:
    out = {
        "youtube": ep.get("youtube_url") or "",
        "acquired": ep["acquired_url"],
        "apple_podcasts": APPLE,
        "spotify": SPOTIFY,
    }
    return out


def base(ep_id: str, **kwargs) -> dict:
    ep = META[ep_id]
    return {
        "episode_id": ep_id,
        "podcast": "Acquired",
        "host": HOST,
        "metadata": {
            "episode_number": ep["episode_number"],
            "title": ep["title"],
            "guest": ep["guest"],
            "guest_role": ep["guest_role"],
            "date": ep["date"],
            "duration_minutes": ep["duration_minutes"],
            "youtube_url": ep.get("youtube_url") or "",
            "links": links(ep),
        },
        "extraction_meta": EXTRACTION,
        "review_notes": "Manual GPT Acquired batch v5.1 — early season backlog (episodes 10–17)",
        **kwargs,
    }


def counted_words(data: dict) -> int:
    from src.validate import word_count as wc

    total = 0
    total += wc(data.get("conclusion", ""))
    total += wc(data.get("background", ""))
    total += wc(data.get("competitive_advantage", ""))
    total += wc(" ".join(data.get("golden_quotes", [])))
    total += wc(" ".join(data.get("important_facts", [])))
    mm = data.get("mental_model", {})
    total += wc(" ".join(str(mm.get(k, "")) for k in ("name", "components", "application")))
    for item in data.get("key_insights", []):
        total += wc(" ".join(item.get(k, "") for k in ("view", "question", "answer")))
    for row in data.get("top_investment_implications", []):
        total += wc(row.get("thesis", ""))
    return total
