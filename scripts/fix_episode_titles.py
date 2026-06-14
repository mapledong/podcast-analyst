#!/usr/bin/env python3
"""Normalize episode title/guest metadata and re-render affected summaries."""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))

from src.display_titles import (  # noqa: E402
    _parse_episode_framing,
    normalize_episode_metadata,
    resolve_display_titles,
)
from src.render import render_summary, save_summary  # noqa: E402
from src.template_config import template_path_for_podcast  # noqa: E402
from src.validate import load_template_config  # noqa: E402

EPISODES_YAML = ROOT / "config" / "episodes.yaml"
APPROVED_DIR = ROOT / "data" / "approved"
OUTPUTS_DIR = ROOT / "outputs"
TEMPLATES_DIR = ROOT / "templates"

GENERIC_HEADLINE = re.compile(
    r"^(Interview|Special|Sessions|Short|Episode\s+\d+|Season\s+\d+(?:,\s*Episode\s+\d+)?|"
    r"Acquired(?:\s+Season\s+\d+\s+Episode\s+\d+)?)$",
    re.I,
)


def _needs_metadata_fix(title: str, guest: str) -> bool:
    subject, framing = _parse_episode_framing(title)
    if framing:
        return True
    if guest and guest.strip().lower() == title.strip().lower() and ":" in title:
        return True
    if GENERIC_HEADLINE.match(title.strip()):
        return True
    if guest and re.match(r"^Episode\s+\d+\s+", guest.strip(), re.I):
        return True
    return False


def _needs_display_fix(podcast: str, title: str, guest: str, guest_role: str) -> bool:
    headline, _, _, _ = resolve_display_titles(podcast, title, guest, guest_role)
    return bool(GENERIC_HEADLINE.match(headline.strip()))


def main() -> int:
    cfg = yaml.safe_load(EPISODES_YAML.read_text(encoding="utf-8"))
    changed_ids: list[str] = []

    for ep in cfg.get("episodes", []):
        podcast = ep.get("podcast", "")
        title = ep.get("title", "")
        guest = ep.get("guest", "")
        guest_role = ep.get("guest_role", "")

        if podcast != "Acquired":
            continue
        if not _needs_metadata_fix(title, guest) and not _needs_display_fix(
            podcast, title, guest, guest_role
        ):
            continue

        cleaned = normalize_episode_metadata(title, guest, guest_role)
        if (
            cleaned["title"] == title
            and cleaned["guest"] == guest
            and cleaned["guest_role"] == guest_role
        ):
            continue

        ep["title"] = cleaned["title"]
        ep["guest"] = cleaned["guest"]
        ep["guest_role"] = cleaned["guest_role"]
        changed_ids.append(ep["id"])
        print(f"yaml {ep['id']}: {title!r} -> {cleaned['title']!r}")

    if changed_ids:
        EPISODES_YAML.write_text(
            yaml.dump(cfg, sort_keys=False, allow_unicode=True),
            encoding="utf-8",
        )

    rerendered = 0
    for ep_id in changed_ids:
        path = APPROVED_DIR / f"{ep_id}.json"
        if not path.exists():
            continue
        data = json.loads(path.read_text(encoding="utf-8"))
        meta = data.setdefault("metadata", {})
        cleaned = normalize_episode_metadata(
            meta.get("title", ""),
            meta.get("guest", ""),
            meta.get("guest_role", ""),
        )
        meta["title"] = cleaned["title"]
        meta["guest"] = cleaned["guest"]
        meta["guest_role"] = cleaned["guest_role"]
        path.write_text(json.dumps(data, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")

        tmpl_path = template_path_for_podcast(data.get("podcast"))
        tmpl = load_template_config(tmpl_path)
        md = render_summary(data, TEMPLATES_DIR, tmpl)
        ep_num = int(meta.get("episode_number", 0))
        save_summary(md, OUTPUTS_DIR / f"EP{ep_num}_{ep_id}.md")
        rerendered += 1
        print(f"  rerendered {ep_id}")

    print(f"\nUpdated {len(changed_ids)} episodes in episodes.yaml; re-rendered {rerendered} summaries.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
