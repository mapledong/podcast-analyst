"""Render structured summary JSON to markdown."""

from __future__ import annotations

import re
from pathlib import Path
from typing import Any

from jinja2 import Environment, FileSystemLoader, select_autoescape

from src.display_titles import display_fields_from_summary


def direction_label(direction: str) -> str:
    icons = {"Long": "🟢", "Short": "🔴", "Watch": "🟡"}
    return f"{icons.get(direction, '⚪')} {direction.upper()}"


def confidence_bar(confidence: str) -> str:
    bars = {"High": "●●●", "Medium": "●●○", "Low": "●○○"}
    return f"{bars.get(confidence, '○○○')} {confidence}"


def star_rating(score: float) -> str:
    n = max(1, min(5, int(float(score) + 0.5)))
    display = "★" * n + "☆" * (5 - n)
    return f"**{display}** · {n}/5"


def format_date(date_str: str) -> str:
    """2026-06-09 → Jun 9, 2026"""
    from datetime import datetime

    try:
        return datetime.strptime(date_str[:10], "%Y-%m-%d").strftime("%b %-d, %Y")
    except ValueError:
        return date_str


def md_safe(text: str) -> str:
    """Replace ~ before numbers/$ so markdown renderers don't strike/subscript spans."""
    if not text:
        return text
    return re.sub(r"~(\$|\d)", r"≈\1", str(text))


def fix_approx_tildes(markdown: str) -> str:
    """Post-process rendered markdown for the same ~ pairing issue."""
    return md_safe(markdown)


def _body_text(data: dict[str, Any]) -> str:
    mm = data.get("mental_model", {})
    parts: list[str] = [
        data.get("conclusion", ""),
        data.get("background", ""),
        " ".join(data.get("important_facts", [])),
        mm.get("name", ""),
        mm.get("components", ""),
        mm.get("application", ""),
        data.get("competitive_advantage", ""),
    ]
    for item in data.get("key_insights", []):
        parts.extend([item.get("view", ""), item.get("question", ""), item.get("answer", "")])
    for clue in data.get("top_investment_implications", []):
        parts.append(clue.get("thesis", ""))
    parts.append(" ".join(data.get("golden_quotes", [])))
    return " ".join(p for p in parts if p)


def estimate_reading_time(data: dict[str, Any], wpm: int = 200) -> int:
    return max(1, round(len(_body_text(data).split()) / wpm))


def render_summary(
    data: dict[str, Any],
    templates_dir: Path,
    template_cfg: dict[str, Any] | None = None,
) -> str:
    env = Environment(
        loader=FileSystemLoader(str(templates_dir)),
        autoescape=select_autoescape(default=False),
        trim_blocks=True,
        lstrip_blocks=True,
    )
    env.filters["direction_label"] = direction_label
    env.filters["confidence_bar"] = confidence_bar
    env.filters["star_rating"] = star_rating
    env.filters["format_date"] = format_date
    env.filters["md_safe"] = md_safe

    ctx = {
        **data,
        **display_fields_from_summary(data),
        "reading_time_min": estimate_reading_time(data),
    }
    rendered = env.get_template("summary.md.j2").render(**ctx)
    return fix_approx_tildes(rendered)


def save_summary(markdown: str, output_path: Path) -> Path:
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(markdown, encoding="utf-8")
    return output_path
