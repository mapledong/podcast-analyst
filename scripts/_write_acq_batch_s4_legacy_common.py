"""Shared helpers for S4 legacy Acquired batch write scripts."""
from __future__ import annotations

APPLE = "https://podcasts.apple.com/podcast/acquired/id1050462261"
SPOTIFY = "https://open.spotify.com/show/2HI3KdjtJnr3E8B4W8Y0Yx"
HOST = "Ben Gilbert & David Rosenthal"
EXTRACTION = {
    "model": "manual-gpt-agent-v5.1-acquired",
    "transcript_source": "acquired.fm",
    "status": "approved",
    "template_version": "5.1-acquired",
}


def meta(
    ep_id: str,
    title: str,
    guest: str,
    guest_role: str,
    date: str,
    duration_minutes: int,
    acquired_url: str,
) -> dict:
    return {
        "episode_number": 0,
        "title": title,
        "guest": guest,
        "guest_role": guest_role,
        "date": date,
        "duration_minutes": duration_minutes,
        "youtube_url": "",
        "links": {
            "youtube": "",
            "acquired": acquired_url,
            "apple_podcasts": APPLE,
            "spotify": SPOTIFY,
        },
    }


def shell(ep_id: str, metadata: dict, **body) -> dict:
    return {
        "episode_id": ep_id,
        "podcast": "Acquired",
        "host": HOST,
        "metadata": metadata,
        "extraction_meta": EXTRACTION,
        "review_notes": "Manual GPT Acquired batch — v5.1-acquired; legacy season batch",
        **body,
    }
