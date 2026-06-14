#!/usr/bin/env python3
"""Batch process ILTB episodes: fetch → extract → approve → publish with resume."""

from __future__ import annotations

import json
import math
import os
import sys
import time
from datetime import datetime, timezone
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))

from src.extract import extract_summary, merge_with_metadata  # noqa: E402
from src.fetch_transcript import extract_video_id, fetch_transcript, save_transcript  # noqa: E402
from src.render import render_summary, save_summary  # noqa: E402
from src.validate import choose_rating, load_template_config, validate_rating_distribution, validate_summary  # noqa: E402

DISCOVERED = ROOT / "data" / "discovered" / "iltb_episodes.json"
STATE_PATH = ROOT / "data" / "batch_state.json"
EPISODES_YAML = ROOT / "config" / "episodes.yaml"
APPROVED_DIR = ROOT / "data" / "approved"
SKIP_IDS = {"ep475", "ep476", "ep477"}
DEFAULT_RATING = 3
RETRY_DELAY = 30


def _load_state() -> dict:
    if STATE_PATH.exists():
        return json.loads(STATE_PATH.read_text(encoding="utf-8"))
    return {"completed": [], "failed": [], "skipped": [], "started_at": None}


def _save_state(state: dict) -> None:
    STATE_PATH.parent.mkdir(parents=True, exist_ok=True)
    STATE_PATH.write_text(json.dumps(state, indent=2), encoding="utf-8")


def _load_discovered() -> list[dict]:
    data = json.loads(DISCOVERED.read_text(encoding="utf-8"))
    return data["episodes"]


def _podcast_cfg() -> dict:
    return yaml.safe_load(EPISODES_YAML.read_text(encoding="utf-8"))


def _ensure_episode_yaml(ep: dict) -> None:
    cfg = _podcast_cfg()
    existing = {e["id"] for e in cfg.get("episodes", [])}
    if ep["id"] in existing:
        return
    entry = {
        "id": ep["id"],
        "episode_number": ep["episode_number"],
        "title": ep["title"],
        "guest": ep["guest"],
        "guest_role": ep.get("guest_role", ""),
        "date": ep["date"],
        "duration_minutes": ep.get("duration_minutes", 60),
        "youtube_url": ep.get("youtube_url", ""),
    }
    cfg.setdefault("episodes", []).append(entry)
    cfg["episodes"].sort(key=lambda e: e["episode_number"], reverse=True)
    EPISODES_YAML.write_text(yaml.dump(cfg, sort_keys=False, allow_unicode=True), encoding="utf-8")


def _choose_rating(extracted_rating: int, tmpl: dict, podcast: str) -> int:
    """Pick a rating that respects per-podcast distribution caps; default bulk rating is 3★."""
    return choose_rating(
        extracted_rating,
        tmpl,
        APPROVED_DIR,
        podcast=podcast,
    )


def _process_episode(ep: dict, tmpl: dict, model: str, podcast_cfg: dict) -> str:
    """Returns status: completed | skipped | failed"""
    eid = ep["id"]
    if not eid:
        return "skipped"
    if eid in SKIP_IDS:
        return "skipped"
    if APPROVED_DIR.joinpath(f"{eid}.json").exists():
        out_md = ROOT / "outputs" / f"EP{ep['episode_number']}_{eid}.md"
        if out_md.exists():
            return "skipped"

    yt = ep.get("youtube_url", "")
    if not yt:
        return "skipped"

    vid = extract_video_id(yt)
    tpath = ROOT / "data" / "transcripts" / f"{vid}.txt"
    if not tpath.exists():
        try:
            result = fetch_transcript(yt)
            save_transcript(result, ROOT / "data" / "transcripts")
        except Exception as exc:
            raise RuntimeError(f"transcript fetch failed: {exc}") from exc

    text = tpath.read_text(encoding="utf-8")
    if text.startswith("# video_id:"):
        text = text.split("\n\n", 1)[-1]

    episode_meta = {
        "podcast": podcast_cfg.get("podcast", "Invest Like the Best"),
        "episode_number": ep["episode_number"],
        "title": ep["title"],
        "guest": ep["guest"],
        "guest_role": ep.get("guest_role", ""),
        "duration_minutes": ep.get("duration_minutes", 60),
    }

    extracted = extract_summary(text, episode_meta, model=model)
    rating = int(extracted.get("episode_rating", {}).get("overall", DEFAULT_RATING))
    rating = _choose_rating(rating, tmpl, podcast_cfg.get("podcast", "Invest Like the Best"))
    extracted["episode_rating"] = {"overall": rating}

    merged = merge_with_metadata(
        extracted,
        {
            "id": eid,
            "episode_number": ep["episode_number"],
            "title": ep["title"],
            "guest": ep["guest"],
            "guest_role": ep.get("guest_role", ""),
            "date": ep["date"],
            "duration_minutes": ep.get("duration_minutes", 60),
            "youtube_url": yt,
        },
        podcast_cfg,
        transcript_source="youtube",
        model=model,
    )
    merged["review_notes"] = "batch-auto v4.7"
    merged["extraction_meta"]["status"] = "approved"

    report = validate_summary(merged, tmpl)
    for issue in validate_rating_distribution(
        rating, tmpl, APPROVED_DIR, podcast=podcast_cfg.get("podcast", "Invest Like the Best")
    ):
        report.add(issue.section, issue.message, issue.severity)
    if not report.passed:
        msgs = "; ".join(i.message for i in report.issues if i.severity == "error")
        raise RuntimeError(f"validation failed: {msgs}")

    approved_path = APPROVED_DIR / f"{eid}.json"
    approved_path.parent.mkdir(parents=True, exist_ok=True)
    approved_path.write_text(json.dumps(merged, indent=2, ensure_ascii=False), encoding="utf-8")

    _ensure_episode_yaml(ep)
    md = render_summary(merged, ROOT / "templates", template_cfg=tmpl)
    out = ROOT / "outputs" / f"EP{ep['episode_number']}_{eid}.md"
    save_summary(md, out)
    return "completed"


def _sync_web() -> None:
    import subprocess

    sync_script = ROOT / "web" / "scripts" / "sync-content.mjs"
    subprocess.run(["node", str(sync_script)], cwd=str(ROOT / "web"), check=False)


def run_batch(*, limit: int | None = None, newest_first: bool = True) -> dict:
    from src.env import load_dotenv

    load_dotenv()
    if not DISCOVERED.exists():
        raise SystemExit(f"Run discover first: python scripts/discover_iltb.py → {DISCOVERED}")

    episodes = _load_discovered()
    processable = [
        e
        for e in episodes
        if e.get("id")
        and e["id"] not in SKIP_IDS
        and e.get("youtube_url")
        and not (APPROVED_DIR / f"{e['id']}.json").exists()
    ]
    if newest_first:
        processable.sort(key=lambda e: e["episode_number"] or 0, reverse=True)
    else:
        processable.sort(key=lambda e: e["episode_number"] or 0)

    if limit:
        processable = processable[:limit]

    state = _load_state()
    if not state.get("started_at"):
        state["started_at"] = datetime.now(timezone.utc).isoformat()

    tmpl = load_template_config(ROOT / "config" / "template.yaml")
    podcast_cfg = _podcast_cfg()
    model = os.environ.get("PODCAST_ANALYST_MODEL", "gpt-4.1-mini")

    for ep in processable:
        eid = ep["id"]
        print(f"\n=== {eid} EP.{ep['episode_number']} — {ep['guest']} ===")
        attempts = 0
        while attempts < 3:
            attempts += 1
            try:
                status = _process_episode(ep, tmpl, model, podcast_cfg)
                if status == "completed":
                    state["completed"].append(eid)
                    print(f"✓ published {eid}")
                elif status == "skipped":
                    if eid not in state["skipped"]:
                        state["skipped"].append(eid)
                    print(f"⊘ skipped {eid}")
                break
            except Exception as exc:
                err = str(exc)
                if "rate limit" in err.lower() or "429" in err:
                    wait = RETRY_DELAY * attempts
                    print(f"Rate limit, waiting {wait}s …")
                    time.sleep(wait)
                    continue
                print(f"✗ failed {eid}: {exc}")
                if eid not in state["failed"]:
                    state["failed"].append({"id": eid, "error": err})
                break
        _save_state(state)
        _sync_web()

    state["last_run"] = datetime.now(timezone.utc).isoformat()
    _save_state(state)

    discovered = json.loads(DISCOVERED.read_text(encoding="utf-8"))
    return {
        "discovered": discovered["total"],
        "with_youtube": discovered["with_youtube"],
        "processed_this_run": len(processable),
        "completed_total": len(state["completed"]),
        "failed_total": len(state["failed"]),
        "skipped_total": len(state["skipped"]),
    }


def main() -> None:
    import argparse

    parser = argparse.ArgumentParser(description="Batch ILTB pipeline")
    parser.add_argument("--limit", type=int, default=None, help="Max episodes this run")
    parser.add_argument("--oldest-first", action="store_true")
    args = parser.parse_args()
    stats = run_batch(limit=args.limit, newest_first=not args.oldest_first)
    print("\n--- Batch stats ---")
    for k, v in stats.items():
        print(f"{k}: {v}")


if __name__ == "__main__":
    main()
