#!/usr/bin/env python3
"""Batch-expand approved summaries to meet v4.8 / v5.2 word minimums."""

from __future__ import annotations

import argparse
import json
import sys
import time
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))

from src.expand import (  # noqa: E402
    expand_summary,
    load_transcript_text,
    resolve_transcript_path,
    section_word_counts,
)
from src.template_config import template_path_for_podcast  # noqa: E402
from src.validate import expansion_warnings, load_template_config, needs_expansion, validate_summary, word_gap  # noqa: E402

APPROVED = ROOT / "data" / "approved"
STATE_PATH = ROOT / "data" / "expand_state.json"
RETRY_DELAY = 30


def _load_state() -> dict:
    if STATE_PATH.exists():
        return json.loads(STATE_PATH.read_text(encoding="utf-8"))
    return {"completed": [], "failed": [], "skipped": [], "started_at": None}


def _save_state(state: dict) -> None:
    STATE_PATH.parent.mkdir(parents=True, exist_ok=True)
    STATE_PATH.write_text(json.dumps(state, indent=2), encoding="utf-8")


def _iter_paths(ids: list[str] | None, podcast: str | None) -> list[Path]:
    if ids:
        paths = [APPROVED / f"{eid}.json" for eid in ids]
    else:
        paths = sorted(APPROVED.glob("*.json"))
    out: list[Path] = []
    for path in paths:
        if not path.exists():
            continue
        if podcast:
            data = json.loads(path.read_text(encoding="utf-8"))
            if data.get("podcast") != podcast:
                continue
        out.append(path)
    return out


def _already_ok(data: dict, template: dict, *, min_gap: int) -> bool:
    if needs_expansion(data, template):
        return False
    return word_gap(data, template) < min_gap


def _process_one(
    path: Path,
    *,
    model: str | None,
    require_transcript: bool,
    min_gap: int,
    dry_run: bool,
) -> str:
    data = json.loads(path.read_text(encoding="utf-8"))
    eid = path.stem
    podcast = data.get("podcast", "")
    template = load_template_config(template_path_for_podcast(podcast))

    if _already_ok(data, template, min_gap=min_gap):
        return "skipped"

    transcript_path = resolve_transcript_path(data)
    if not transcript_path:
        if require_transcript:
            raise RuntimeError("no transcript found")
        if dry_run:
            print(f"[dry-run] {eid}: would expand without transcript (not allowed)")
            return "skipped"

    before = section_word_counts(data, template)
    gap_before = word_gap(data, template)
    warnings_before = len(expansion_warnings(data, template))

    if dry_run:
        tx = transcript_path.name if transcript_path else "NONE"
        print(
            f"[dry-run] {eid}: {before['total']}/{before['min_total']} words "
            f"(gap {gap_before}, {warnings_before} warnings) transcript={tx}"
        )
        return "dry-run"

    if not transcript_path:
        raise RuntimeError("no transcript found")

    transcript = load_transcript_text(transcript_path)
    expanded = expand_summary(data, transcript, template, model=model)
    report = validate_summary(expanded, template)
    gap_after = max(0, report.min_total_words - report.total_words)

    path.write_text(json.dumps(expanded, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    print(
        f"✓ {eid}: {before['total']} → {report.total_words} words "
        f"(gap {gap_before} → {gap_after}, warnings {warnings_before} → "
        f"{len(expansion_warnings(expanded, template))})"
    )
    if gap_after > 0:
        print(f"  still below minimum by {gap_after} words — may need second pass")
    return "completed"


def main() -> None:
    parser = argparse.ArgumentParser(description="Expand approved summaries via LLM.")
    parser.add_argument("ids", nargs="*", help="Episode IDs (default: all needing expansion)")
    parser.add_argument("--podcast", help='Filter by podcast, e.g. "Invest Like the Best"')
    parser.add_argument("--limit", type=int, default=None)
    parser.add_argument("--model", default=None)
    parser.add_argument("--delay", type=float, default=2.0, help="Seconds between API calls")
    parser.add_argument("--min-gap", type=int, default=1, help="Skip if word gap below this")
    parser.add_argument("--dry-run", action="store_true", help="Report what would expand")
    parser.add_argument("--allow-no-transcript", action="store_true", help="Allow expand without transcript")
    parser.add_argument("--retry-failed", action="store_true", help="Retry IDs in failed list")
    args = parser.parse_args()

    state = _load_state()
    if not state.get("started_at"):
        state["started_at"] = datetime.now(timezone.utc).isoformat()

    paths = _iter_paths(args.ids or None, args.podcast)
    if args.retry_failed:
        failed_ids = {item["id"] if isinstance(item, dict) else item for item in state.get("failed", [])}
        paths = [p for p in paths if p.stem in failed_ids]

    queue: list[Path] = []
    for path in paths:
        eid = path.stem
        if eid in state.get("completed", []) and not args.ids and not args.retry_failed:
            continue
        data = json.loads(path.read_text(encoding="utf-8"))
        tmpl = load_template_config(template_path_for_podcast(data.get("podcast")))
        if not args.ids and _already_ok(data, tmpl, min_gap=args.min_gap):
            if eid not in state["skipped"]:
                state["skipped"].append(eid)
            continue
        queue.append(path)

    if args.limit:
        queue = queue[: args.limit]

    print(f"Queue: {len(queue)} episodes")
    if args.dry_run:
        print("DRY RUN — no files will be modified")

    counts = {"completed": 0, "skipped": 0, "failed": 0, "dry-run": 0}
    for i, path in enumerate(queue, 1):
        eid = path.stem
        print(f"[{i}/{len(queue)}] {eid}")
        attempt = 0
        while attempt < 3:
            attempt += 1
            try:
                status = _process_one(
                    path,
                    model=args.model,
                    require_transcript=not args.allow_no_transcript,
                    min_gap=args.min_gap,
                    dry_run=args.dry_run,
                )
                counts[status] = counts.get(status, 0) + 1
                if status == "completed" and eid not in state["completed"]:
                    state["completed"].append(eid)
                state["failed"] = [
                    item
                    for item in state.get("failed", [])
                    if (item["id"] if isinstance(item, dict) else item) != eid
                ]
                break
            except Exception as exc:
                err = str(exc)
                if "429" in err or "rate" in err.lower():
                    print(f"  rate limited, retry {attempt}/3 in {RETRY_DELAY}s")
                    time.sleep(RETRY_DELAY)
                    continue
                print(f"✗ {eid}: {exc}")
                state["failed"] = [
                    item
                    for item in state.get("failed", [])
                    if (item["id"] if isinstance(item, dict) else item) != eid
                ]
                state["failed"].append({"id": eid, "error": err})
                counts["failed"] += 1
                break
        _save_state(state)
        if not args.dry_run and i < len(queue):
            time.sleep(args.delay)

    print(
        f"\nDone: completed={counts.get('completed', 0)} "
        f"skipped={counts.get('skipped', 0)} failed={counts.get('failed', 0)} "
        f"dry-run={counts.get('dry-run', 0)}"
    )


if __name__ == "__main__":
    main()
