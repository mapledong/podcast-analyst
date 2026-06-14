"""Resolve yt-dlp binary for local venv or CI (pip install yt-dlp)."""

from __future__ import annotations

import os
import shutil
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent


def ytdlp_bin() -> str:
    if env := (os.environ.get("YT_DLP") or "").strip():
        return env
    local = ROOT / ".venv" / "bin" / "yt-dlp"
    if local.is_file():
        return str(local)
    found = shutil.which("yt-dlp")
    if found:
        return found
    raise RuntimeError("yt-dlp not found — run: pip install yt-dlp")
