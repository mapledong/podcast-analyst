#!/usr/bin/env python3
"""One-off: write 10 Founders approved summaries for expand pool (batch 11)."""
from __future__ import annotations

import json
import importlib.util
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
APPROVED = ROOT / "data" / "approved"

COMMON_LINKS = {
    "apple_podcasts": "https://podcasts.apple.com/podcast/founders/id1141877104",
    "spotify": "https://open.spotify.com/show/7txiovdzPARhjm18NwMUYj",
}

META = {
    "fnd-415-how-elon-thinks": {
        "episode_number": 415,
        "title": "How Elon Thinks",
        "guest": "Elon Musk",
        "date": "2026-03-24",
        "duration_minutes": 51,
        "youtube_url": "https://www.youtube.com/watch?v=nqiuSshC9GA",
        "slug": "415-how-elon-thinks",
        "rating": 5,
    },
    "fnd-417-arnold-schwarzenegger": {
        "episode_number": 417,
        "title": "Arnold Schwarzenegger",
        "guest": "Arnold Schwarzenegger",
        "date": "2026-04-19",
        "duration_minutes": 43,
        "youtube_url": "https://www.youtube.com/watch?v=-dh-QNlX12k",
        "slug": "417-arnold-schwarzenegger",
        "rating": 3,
    },
    "fnd-413-how-to-run-down-a-dream": {
        "episode_number": 413,
        "title": "How To Run Down A Dream",
        "guest": "Sam Hinkie",
        "date": "2026-03-03",
        "duration_minutes": 31,
        "youtube_url": "https://www.youtube.com/watch?v=eSZ4Xep1sJU",
        "slug": "413-how-to-run-down-a-dream",
        "rating": 3,
    },
    "fnd-412-how-roger-federer-works": {
        "episode_number": 412,
        "title": "How Roger Federer Works",
        "guest": "Roger Federer",
        "date": "2026-02-19",
        "duration_minutes": 48,
        "youtube_url": "https://www.youtube.com/watch?v=g2-duG1-Jxc",
        "slug": "412-how-roger-federer-works",
        "rating": 3,
    },
    "fnd-411-tortured-into-greatness-the-life-of-andre-agassi": {
        "episode_number": 411,
        "title": "Tortured Into Greatness: The Life of Andre Agassi",
        "guest": "Andre Agassi",
        "date": "2026-02-04",
        "duration_minutes": 61,
        "youtube_url": "https://www.youtube.com/watch?v=d_Bv59Rxo6w",
        "slug": "411-tortured-into-greatness-the-life-of-andre-agassi",
        "rating": 3,
    },
    "fnd-410-excellent-advice-for-living": {
        "episode_number": 410,
        "title": "Excellent Advice for Living",
        "guest": "Kevin Kelly",
        "date": "2026-01-25",
        "duration_minutes": 37,
        "youtube_url": "https://www.youtube.com/watch?v=RUKafK3xCfY",
        "slug": "410-excellent-advice-for-living",
        "rating": 3,
    },
    "fnd-409-the-creative-genius-of-rick-rubin": {
        "episode_number": 409,
        "title": "The Creative Genius of Rick Rubin",
        "guest": "Rick Rubin",
        "date": "2026-01-08",
        "duration_minutes": 43,
        "youtube_url": "https://www.youtube.com/watch?v=wYi4emYR89I",
        "slug": "409-the-creative-genius-of-rick-rubin",
        "rating": 3,
    },
    "fnd-407-bruce-springsteen-repairs-the-hole-in-himself": {
        "episode_number": 407,
        "title": "Bruce Springsteen Repairs the Hole in Himself",
        "guest": "Bruce Springsteen",
        "date": "2025-12-14",
        "duration_minutes": 72,
        "youtube_url": "https://www.youtube.com/watch?v=YRctPFgRb8U",
        "slug": "407-bruce-springsteen-repairs-the-hole-in-himself",
        "rating": 3,
    },
    "fnd-406-christian-von-koenigsegg": {
        "episode_number": 406,
        "title": "Christian von Koenigsegg",
        "guest": "Christian von Koenigsegg",
        "date": "2025-12-03",
        "duration_minutes": 45,
        "youtube_url": "https://www.youtube.com/watch?v=03IcWhHFNMM",
        "slug": "406-christian-von-koenigsegg",
        "rating": 3,
    },
    "fnd-397-jiro-ono-simplicity-is-the-ultimate-advantage": {
        "episode_number": 397,
        "title": "Jiro Ono: Simplicity Is The Ultimate Advantage",
        "guest": "Jiro Ono",
        "date": "2025-08-04",
        "duration_minutes": 41,
        "youtube_url": "https://www.youtube.com/watch?v=x2Rj0sgjDSw",
        "slug": "397-jiro-ono-simplicity-is-the-ultimate-advantage",
        "rating": 3,
    },
}


def base(ep_id: str, body: dict) -> dict:
    m = META[ep_id]
    links = {
        **COMMON_LINKS,
        "founders": f"https://www.founderspodcast.com/episodes/{m['slug']}",
        "youtube": m["youtube_url"],
    }
    return {
        "episode_id": ep_id,
        "podcast": "Founders",
        "host": "David Senra",
        "metadata": {
            "episode_number": m["episode_number"],
            "title": m["title"],
            "guest": m["guest"],
            "guest_role": f"Biography · Episode {m['episode_number']}",
            "date": m["date"],
            "duration_minutes": m["duration_minutes"],
            "youtube_url": m["youtube_url"],
            "links": links,
        },
        "episode_rating": {"overall": m["rating"]},
        "review_notes": "| curated v4.10",
        "extraction_meta": {
            "model": "manual-curated-v4.10",
            "transcript_source": "youtube/ytdlp-auto",
            "status": "approved",
            "template_version": "4.10",
            "rebalanced_v410": True,
        },
        **body,
    }


_spec = importlib.util.spec_from_file_location(
    "_write_founders_batch11_content",
    Path(__file__).resolve().parent / "_write_founders_batch11_content.py",
)
_content = importlib.util.module_from_spec(_spec)
assert _spec.loader is not None
_spec.loader.exec_module(_content)
EPISODES = _content.EPISODES


def main() -> None:
    for ep_id, body in EPISODES.items():
        path = APPROVED / f"{ep_id}.json"
        data = base(ep_id, body)
        path.write_text(json.dumps(data, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
        print(f"wrote {path.name}")


if __name__ == "__main__":
    main()
