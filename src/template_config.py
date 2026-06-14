"""Resolve summary template config by podcast name."""

from __future__ import annotations

from pathlib import Path

PODCAST_TEMPLATE_FILES: dict[str, str] = {
    "Acquired": "template-acquired.yaml",
}

DEFAULT_TEMPLATE_FILE = "template.yaml"


def template_path_for_podcast(podcast: str | None, config_dir: Path | None = None) -> Path:
    root = config_dir or Path(__file__).resolve().parent.parent / "config"
    filename = PODCAST_TEMPLATE_FILES.get(podcast or "", DEFAULT_TEMPLATE_FILE)
    return root / filename
