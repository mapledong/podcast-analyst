"""LLM-based structured extraction from podcast transcripts."""

from __future__ import annotations

import json
import os
from pathlib import Path
from typing import Any

from openai import OpenAI

EXTRACTION_SCHEMA: dict[str, Any] = {
    "type": "object",
    "additionalProperties": False,
    "required": [
        "episode_rating",
        "conclusion",
        "background",
        "important_facts",
        "mental_model",
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
            "properties": {
                "overall": {"type": "integer", "minimum": 1, "maximum": 5},
            },
        },
        "conclusion": {"type": "string"},
        "background": {"type": "string"},
        "important_facts": {
            "type": "array",
            "items": {"type": "string"},
            "minItems": 3,
            "maxItems": 3,
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
        "key_insights": {
            "type": "array",
            "minItems": 3,
            "maxItems": 3,
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
                    "minItems": 5,
                    "maxItems": 10,
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
            "maxItems": 5,
        },
    },
}


def _truncate_transcript(text: str, max_chars: int = 120_000) -> str:
    if len(text) <= max_chars:
        return text
    head = int(max_chars * 0.7)
    tail = max_chars - head
    return text[:head] + "\n\n[... transcript truncated ...]\n\n" + text[-tail:]


def extract_summary(
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
        raise RuntimeError(
            "OPENAI_API_KEY not set. Set it or pass a pre-built JSON via --from-json for human review."
        )

    prompts_dir = prompts_dir or Path(__file__).resolve().parent.parent / "prompts"
    system_prompt = (prompts_dir / "extraction_system.txt").read_text(encoding="utf-8")
    model = model or os.environ.get("PODCAST_ANALYST_MODEL", "gpt-4.1-mini")

    user_prompt = (
        f"Podcast: {episode_meta.get('podcast', 'Unknown')}\n"
        f"Episode: {episode_meta.get('episode_number')} — {episode_meta.get('title')}\n"
        f"Guest: {episode_meta.get('guest')} ({episode_meta.get('guest_role', '')})\n"
        f"Duration: {episode_meta.get('duration_minutes')} minutes\n\n"
        f"TRANSCRIPT:\n{_truncate_transcript(transcript)}"
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
                "name": "podcast_summary",
                "schema": EXTRACTION_SCHEMA,
                "strict": True,
            }
        },
    )

    raw = response.output_text
    extracted = json.loads(raw)
    return extracted


def merge_with_metadata(
    extracted: dict[str, Any],
    episode_cfg: dict[str, Any],
    podcast_cfg: dict[str, Any],
    *,
    transcript_source: str,
    model: str,
) -> dict[str, Any]:
    return {
        "episode_id": episode_cfg["id"],
        "podcast": podcast_cfg.get("podcast", ""),
        "host": podcast_cfg.get("host", ""),
        "metadata": {
            "episode_number": episode_cfg["episode_number"],
            "title": episode_cfg["title"],
            "guest": episode_cfg["guest"],
            "guest_role": episode_cfg.get("guest_role", ""),
            "date": episode_cfg["date"],
            "duration_minutes": episode_cfg["duration_minutes"],
            "youtube_url": episode_cfg.get("youtube_url", ""),
        },
        **extracted,
        "review_notes": "",
        "extraction_meta": {
            "model": model,
            "transcript_source": transcript_source,
            "status": "draft",
        },
    }
