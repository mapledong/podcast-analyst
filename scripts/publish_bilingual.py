#!/usr/bin/env python3
"""Publish bilingual (zh + en) approved summaries."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))

from src.render import render_summary, save_summary  # noqa: E402
from src.template_config import template_path_for_podcast  # noqa: E402

APPROVED_ZH = ROOT / "data" / "approved" / "zh"
APPROVED_EN = ROOT / "data" / "approved"
OUTPUTS_ZH = ROOT / "outputs" / "zh"
OUTPUTS_EN = ROOT / "outputs"
WEB_SUMMARIES = ROOT / "web" / "src" / "data" / "summaries"
WEB_SUMMARIES_ZH = WEB_SUMMARIES / "zh"
EPISODES_YAML = ROOT / "config" / "episodes.yaml"
TEMPLATES = ROOT / "templates"


def _load_yaml(path: Path) -> dict:
    return yaml.safe_load(path.read_text(encoding="utf-8"))


def _save_yaml(path: Path, data: dict) -> None:
    path.write_text(yaml.dump(data, sort_keys=False, allow_unicode=True), encoding="utf-8")


def _episode_entry(data: dict) -> dict:
    meta = data.get("metadata", {})
    links = meta.get("links", {})
    entry = {
        "id": data["episode_id"],
        "episode_number": int(meta["episode_number"]),
        "title": meta.get("title", ""),
        "guest": meta.get("guest", ""),
        "guest_role": meta.get("guest_role", ""),
        "date": meta.get("date", ""),
        "duration_minutes": meta.get("duration_minutes", 60),
        "youtube_url": meta.get("youtube_url") or links.get("youtube", ""),
        "podcast": data.get("podcast", ""),
        "xiaoyuzhou_url": links.get("xiaoyuzhou", ""),
    }
    return entry


def publish_pair(episode_id: str, *, sync_web: bool = True) -> None:
    zh_path = APPROVED_ZH / f"{episode_id}.json"
    en_path = APPROVED_EN / f"{episode_id}.json"
    if not zh_path.exists() or not en_path.exists():
        raise FileNotFoundError(f"Missing zh/en approved JSON for {episode_id}")

    zh_data = json.loads(zh_path.read_text(encoding="utf-8"))
    en_data = json.loads(en_path.read_text(encoding="utf-8"))
    ep_num = zh_data["metadata"]["episode_number"]

    zh_md = render_summary(zh_data, TEMPLATES, locale="zh")
    en_md = render_summary(en_data, TEMPLATES, locale="en")

    save_summary(zh_md, OUTPUTS_ZH / f"EP{ep_num}_{episode_id}.md")
    save_summary(en_md, OUTPUTS_EN / f"EP{ep_num}_{episode_id}.md")

    WEB_SUMMARIES_ZH.mkdir(parents=True, exist_ok=True)
    (WEB_SUMMARIES_ZH / f"{episode_id}.md").write_text(zh_md, encoding="utf-8")
    (WEB_SUMMARIES / f"{episode_id}.md").write_text(en_md, encoding="utf-8")

    cfg = _load_yaml(EPISODES_YAML)
    existing = {ep["id"]: ep for ep in cfg.get("episodes", [])}
    existing[episode_id] = _episode_entry(en_data)
    cfg["episodes"] = sorted(existing.values(), key=lambda ep: int(ep["episode_number"]), reverse=True)
    _save_yaml(EPISODES_YAML, cfg)

    print(f"published {episode_id} (zh + en)")

    if sync_web:
        subprocess.run(
            ["node", str(ROOT / "web" / "scripts" / "sync-content.mjs")],
            cwd=str(ROOT / "web"),
            check=True,
        )


def main() -> None:
    import argparse

    parser = argparse.ArgumentParser()
    parser.add_argument("ids", nargs="+", help="Episode IDs with zh+en approved JSON")
    parser.add_argument("--no-sync", action="store_true")
    args = parser.parse_args()
    for eid in args.ids:
        publish_pair(eid, sync_web=not args.no_sync)


if __name__ == "__main__":
    main()
