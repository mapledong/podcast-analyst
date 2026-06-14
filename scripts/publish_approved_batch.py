#!/usr/bin/env python3
"""Publish approved JSON summaries without running LLM extraction."""

from __future__ import annotations

import argparse
import json
import subprocess
import sys
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))

from src.render import render_summary, save_summary  # noqa: E402
from src.template_config import template_path_for_podcast  # noqa: E402
from src.validate import load_template_config, validate_rating_distribution, validate_summary  # noqa: E402

APPROVED_DIR = ROOT / "data" / "approved"
EPISODES_YAML = ROOT / "config" / "episodes.yaml"
OUTPUTS_DIR = ROOT / "outputs"


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
    }
    if data.get("podcast"):
        entry["podcast"] = data["podcast"]
    return entry


def _upsert_episode_config(entries: list[dict]) -> None:
    cfg = _load_yaml(EPISODES_YAML)
    existing = {ep["id"]: ep for ep in cfg.get("episodes", [])}
    for entry in entries:
        existing[entry["id"]] = entry
    cfg["episodes"] = sorted(existing.values(), key=lambda ep: int(ep["episode_number"]), reverse=True)
    _save_yaml(EPISODES_YAML, cfg)


def _approved_paths(ids: list[str] | None) -> list[Path]:
    if ids:
        return [APPROVED_DIR / f"{eid}.json" for eid in ids]
    paths = sorted(APPROVED_DIR.glob("*.json"), key=lambda p: p.stem)
    return [p for p in paths if p.stem not in ("batch_state",)]


def publish(ids: list[str] | None, *, sync_web: bool) -> int:
    paths = _approved_paths(ids)
    entries: list[dict] = []
    published = 0

    for path in paths:
        if not path.exists():
            print(f"missing: {path}", file=sys.stderr)
            continue
        data = json.loads(path.read_text(encoding="utf-8"))
        tmpl = load_template_config(template_path_for_podcast(data.get("podcast")))
        report = validate_summary(data, tmpl)
        rating = data.get("episode_rating", {}).get("overall")
        try:
            rating_int = int(rating)
            if float(rating) == rating_int and 1 <= rating_int <= 5:
                for issue in validate_rating_distribution(
                    rating_int,
                    tmpl,
                    APPROVED_DIR,
                    podcast=data.get("podcast"),
                    episode_id=path.stem,
                ):
                    report.add(issue.section, issue.message, issue.severity)
        except (TypeError, ValueError):
            pass
        if not report.passed:
            errors = "; ".join(issue.message for issue in report.issues if issue.severity == "error")
            print(f"validation failed for {path.stem}: {errors}", file=sys.stderr)
            continue

        entries.append(_episode_entry(data))
        episode_number = data.get("metadata", {}).get("episode_number", path.stem)
        markdown = render_summary(data, ROOT / "templates", template_cfg=tmpl)
        output = OUTPUTS_DIR / f"EP{episode_number}_{path.stem}.md"
        save_summary(markdown, output)
        print(f"published {path.stem} -> {output.relative_to(ROOT)}")
        published += 1

    if entries:
        _upsert_episode_config(entries)

    if sync_web and published:
        subprocess.run(["node", str(ROOT / "web" / "scripts" / "sync-content.mjs")], cwd=str(ROOT / "web"), check=True)

    return published


def main() -> None:
    parser = argparse.ArgumentParser(description="Publish approved summaries to outputs and web catalog.")
    parser.add_argument("ids", nargs="*", help="Episode IDs to publish; defaults to all approved JSON files")
    parser.add_argument("--no-sync", action="store_true", help="Skip web catalog sync")
    args = parser.parse_args()
    count = publish(args.ids or None, sync_web=not args.no_sync)
    print(f"published_count: {count}")


if __name__ == "__main__":
    main()
