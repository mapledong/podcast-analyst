#!/usr/bin/env python3
"""One-off: write 10 Business Breakdowns approved summaries for batch 10."""
from __future__ import annotations

import json
import importlib.util
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
APPROVED = ROOT / "data" / "approved"

COMMON_LINKS = {
    "apple_podcasts": "https://podcasts.apple.com/podcast/business-breakdowns/id1559120677",
    "spotify": "https://open.spotify.com/show/4zQbeLbLgqKEyn7e2sKzez",
}

META = {
    "bb-kaspi-kz-the-kazakh-super-app": {
        "episode_number": 204,
        "title": "Kaspi.kz: The Kazakh Super-App",
        "guest": "Kaspi.kz",
        "date": "2025-01-22",
        "duration_minutes": 55,
        "youtube_url": "https://www.youtube.com/watch?v=wDtXE7lowH8",
        "colossus_url": "https://joincolossus.com/episode/kaspi-kz-the-kazakh-super-app/",
        "guest_role": "Public · KSPI",
        "rating": 3,
    },
    "bb-apollo-connoisseurs-of-complexity": {
        "episode_number": 208,
        "title": "Apollo: Connoisseurs of Complexity",
        "guest": "Apollo",
        "date": "2025-03-14",
        "duration_minutes": 73,
        "youtube_url": "https://www.youtube.com/watch?v=Q5xa7XveU5g",
        "colossus_url": "https://joincolossus.com/episode/apollo-connoisseurs-of-complexity/",
        "guest_role": "Public · APO",
        "rating": 3,
    },
    "bb-essilorluxottica-sight-to-behold": {
        "episode_number": 210,
        "title": "EssilorLuxottica: Sight To Behold",
        "guest": "EssilorLuxottica",
        "date": "2025-03-26",
        "duration_minutes": 44,
        "youtube_url": "https://www.youtube.com/watch?v=8ODea4SXwF4",
        "colossus_url": "https://joincolossus.com/episode/essilorluxottica-sight-to-behold/",
        "guest_role": "Public · ESLOY",
        "rating": 3,
    },
    "bb-goosehead-insuring-coverage": {
        "episode_number": 212,
        "title": "Goosehead: Insuring Coverage",
        "guest": "Goosehead",
        "date": "2025-04-09",
        "duration_minutes": 69,
        "youtube_url": "https://www.youtube.com/watch?v=dL9XOw6Sk04",
        "colossus_url": "https://joincolossus.com/episode/goosehead-insuring-coverage/",
        "guest_role": "Public · GSHD",
        "rating": 3,
    },
    "bb-chemed-empire-of-care": {
        "episode_number": 215,
        "title": "Chemed: Empire of Care",
        "guest": "Chemed",
        "date": "2025-05-01",
        "duration_minutes": 45,
        "youtube_url": "https://www.youtube.com/watch?v=rnq6k3eswHQ",
        "colossus_url": "https://joincolossus.com/episode/chemed-empire-of-care/",
        "guest_role": "Public · CHE",
        "rating": 3,
    },
    "bb-interactive-brokers-margin-masters": {
        "episode_number": 216,
        "title": "Interactive Brokers: Margin Masters",
        "guest": "Interactive Brokers",
        "date": "2025-05-09",
        "duration_minutes": 45,
        "youtube_url": "https://www.youtube.com/watch?v=xNHPgKQCiBI",
        "colossus_url": "https://joincolossus.com/episode/ibkr-margin-masters/",
        "guest_role": "Public · IBKR",
        "rating": 3,
    },
    "bb-moncler-the-apr-s-playbook": {
        "episode_number": 218,
        "title": "Moncler: The Après Playbook",
        "guest": "Moncler",
        "date": "2025-05-30",
        "duration_minutes": 59,
        "youtube_url": "https://www.youtube.com/watch?v=7falKgxDbOc",
        "colossus_url": "https://joincolossus.com/episode/moncler-the-apres-playbook/",
        "guest_role": "Private · Moncler",
        "rating": 3,
    },
    "bb-eqt-returns-at-scale": {
        "episode_number": 220,
        "title": "EQT: Returns at Scale",
        "guest": "EQT",
        "date": "2025-06-18",
        "duration_minutes": 78,
        "youtube_url": "https://www.youtube.com/watch?v=Rpd0bWv3BP4",
        "colossus_url": "https://joincolossus.com/episode/eqt-returns-at-scale/",
        "guest_role": "Private · EQT (Stockholm-listed PE firm)",
        "rating": 3,
    },
    "bb-agilent-back-to-the-lab": {
        "episode_number": 223,
        "title": "Agilent: Back To The Lab",
        "guest": "Agilent",
        "date": "2025-07-16",
        "duration_minutes": 41,
        "youtube_url": "https://www.youtube.com/watch?v=m8p5hGQljOQ",
        "colossus_url": "https://joincolossus.com/episode/agilent-back-to-the-lab/",
        "guest_role": "Public · A",
        "rating": 3,
    },
    "bb-compass-real-estate-revolution": {
        "episode_number": 226,
        "title": "Compass: Real Estate Revolution",
        "guest": "Compass",
        "date": "2025-08-13",
        "duration_minutes": 62,
        "youtube_url": "https://www.youtube.com/watch?v=T7zvk9VzxM4",
        "colossus_url": "https://joincolossus.com/episode/compass-real-estate-revolution/",
        "guest_role": "Public · COMP",
        "rating": 3,
    },
}


def base(ep_id: str, body: dict) -> dict:
    m = META[ep_id]
    links = {
        **COMMON_LINKS,
        "acquired": m["colossus_url"],
        "youtube": m["youtube_url"],
    }
    return {
        "episode_id": ep_id,
        "podcast": "Business Breakdowns",
        "host": "Matt Reustle & Zack Fuss",
        "metadata": {
            "episode_number": m["episode_number"],
            "title": m["title"],
            "guest": m["guest"],
            "guest_role": m["guest_role"],
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
    "_write_bb_batch10_content",
    Path(__file__).resolve().parent / "_write_bb_batch10_content.py",
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
