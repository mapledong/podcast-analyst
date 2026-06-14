"""LLM extraction for Acquired episodes (template v5.4-acquired)."""

from __future__ import annotations

import json
import os
from pathlib import Path
from typing import Any

from openai import OpenAI

from src.extract import _truncate_transcript

ACQUIRED_EXTRACTION_SCHEMA: dict[str, Any] = {
    "type": "object",
    "additionalProperties": False,
    "required": [
        "episode_rating",
        "conclusion",
        "background",
        "important_facts",
        "mental_model",
        "competitive_advantage",
        "key_insights",
        "top_investment_implications",
        "golden_quotes",
        "chronology",
        "keywords",
    ],
    "properties": {
        "episode_rating": {
            "type": "object",
            "additionalProperties": False,
            "required": ["overall"],
            "properties": {"overall": {"type": "integer", "minimum": 1, "maximum": 5}},
        },
        "conclusion": {"type": "string"},
        "background": {"type": "string"},
        "important_facts": {
            "type": "array",
            "items": {"type": "string"},
            "minItems": 5,
            "maxItems": 5,
        },
        "mental_model": {
            "type": "object",
            "additionalProperties": False,
            "required": ["name", "components", "application"],
            "properties": {
                "name": {"type": "string"},
                "components": {"type": "string"},
                "application": {"type": "string"},
            },
        },
        "competitive_advantage": {"type": "string"},
        "key_insights": {
            "type": "array",
            "minItems": 5,
            "maxItems": 5,
            "items": {
                "type": "object",
                "additionalProperties": False,
                "required": ["view", "question", "answer"],
                "properties": {
                    "view": {"type": "string"},
                    "question": {"type": "string"},
                    "answer": {"type": "string"},
                },
            },
        },
        "top_investment_implications": {
            "type": "array",
            "minItems": 1,
            "maxItems": 3,
            "items": {
                "type": "object",
                "additionalProperties": False,
                "required": ["ticker", "direction", "confidence", "thesis"],
                "properties": {
                    "ticker": {"type": "string"},
                    "direction": {"type": "string", "enum": ["Long", "Short", "Watch"]},
                    "confidence": {"type": "string", "enum": ["High", "Medium", "Low"]},
                    "thesis": {"type": "string"},
                },
            },
        },
        "golden_quotes": {
            "type": "array",
            "items": {"type": "string"},
            "minItems": 3,
            "maxItems": 3,
        },
        "chronology": {
            "type": "object",
            "additionalProperties": False,
            "required": ["subject", "events"],
            "properties": {
                "subject": {"type": "string"},
                "events": {
                    "type": "array",
                    "minItems": 10,
                    "maxItems": 20,
                    "items": {
                        "type": "object",
                        "additionalProperties": False,
                        "required": ["date", "event"],
                        "properties": {
                            "date": {"type": "string"},
                            "event": {"type": "string"},
                        },
                    },
                },
            },
        },
        "keywords": {
            "type": "array",
            "items": {"type": "string"},
            "minItems": 3,
            "maxItems": 4,
        },
    },
}


def extract_acquired_summary(
    transcript: str,
    episode_meta: dict[str, Any],
    *,
    model: str | None = None,
    prompts_dir: Path | None = None,
) -> dict[str, Any]:
    from src.env import load_dotenv

    load_dotenv()
    api_key = os.environ.get("OPENAI_API_KEY")
    if not api_key:
        raise RuntimeError("OPENAI_API_KEY not set")

    prompts_dir = prompts_dir or Path(__file__).resolve().parent.parent / "prompts"
    system_prompt = (prompts_dir / "extraction_acquired.txt").read_text(encoding="utf-8")
    model = model or os.environ.get("PODCAST_ANALYST_MODEL", "gpt-4.1")

    user_prompt = (
        f"Podcast: Acquired\n"
        f"Episode: {episode_meta.get('title')}\n"
        f"Guest/Subject: {episode_meta.get('guest')} ({episode_meta.get('guest_role', '')})\n"
        f"Duration: {episode_meta.get('duration_minutes')} minutes\n\n"
        f"TRANSCRIPT:\n{_truncate_transcript(transcript, max_chars=150_000)}"
    )

    client = OpenAI(api_key=api_key)
    response = client.responses.create(
        model=model,
        input=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_prompt},
        ],
        text={
            "format": {
                "type": "json_schema",
                "name": "acquired_summary",
                "schema": ACQUIRED_EXTRACTION_SCHEMA,
                "strict": True,
            }
        },
    )
    return json.loads(response.output_text)


def merge_acquired_metadata(
    extracted: dict[str, Any],
    episode: dict[str, Any],
    *,
    model: str,
) -> dict[str, Any]:
    links = {
        "acquired": episode.get("acquired_url", ""),
        "apple_podcasts": "https://podcasts.apple.com/podcast/acquired/id1050462261",
        "spotify": "https://open.spotify.com/show/2HI3KdjtJnr3E8B4W8Y0Yx",
    }
    yt = episode.get("youtube_url") or ""
    if yt:
        links["youtube"] = yt

    return {
        "episode_id": episode["id"],
        "podcast": "Acquired",
        "host": "Ben Gilbert & David Rosenthal",
        "metadata": {
            "episode_number": episode.get("episode_number", 0),
            "title": episode["title"],
            "guest": episode.get("guest", episode["title"]),
            "guest_role": episode.get("guest_role", "Acquired"),
            "date": episode.get("date", ""),
            "duration_minutes": episode.get("duration_minutes", 60),
            "youtube_url": yt,
            "links": links,
        },
        **extracted,
        "review_notes": "batch-auto v5.4-acquired",
        "extraction_meta": {
            "model": model,
            "transcript_source": "acquired.fm",
            "status": "approved",
            "template_version": "5.4-acquired",
        },
    }
