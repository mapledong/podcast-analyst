#!/usr/bin/env python3
"""Nightly discover → summarize → publish for new podcast episodes.

Runs at 01:00 Beijing via .github/workflows/nightly-content-update.yml.
Prioritizes newly released episodes (past 7 days) with transcripts, then BB/Founders expand pool.
"""

from __future__ import annotations

import json
import os
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DEFAULT_BATCH = 8


def _run(cmd: list[str]) -> str:
    proc = subprocess.run(cmd, cwd=str(ROOT), capture_output=True, text=True)
    if proc.returncode != 0:
        print(proc.stderr or proc.stdout, file=sys.stderr)
    return proc.stdout


def _new_episode_stats() -> dict:
    raw = _run([sys.executable, str(ROOT / "scripts/report_new_episodes.py"), "--stats"])
    try:
        return json.loads(raw)
    except json.JSONDecodeError:
        return {}


def _new_ready_ids(limit: int) -> list[str]:
    proc = subprocess.run(
        [
            sys.executable,
            str(ROOT / "scripts/report_new_episodes.py"),
            "--ready",
            "--limit",
            str(limit),
            "--ids-only",
        ],
        capture_output=True,
        text=True,
        cwd=str(ROOT),
    )
    return [ln.strip() for ln in proc.stdout.splitlines() if ln.strip()]


def _bb_founders_ready(limit: int) -> list[str]:
    proc = subprocess.run(
        [
            sys.executable,
            str(ROOT / "scripts/resolve_curated_bb_founders.py"),
            "--ready",
            "--limit",
            str(limit),
        ],
        capture_output=True,
        text=True,
        cwd=str(ROOT),
    )
    return [ln.strip() for ln in proc.stdout.splitlines() if ln.strip()]


def build_prompt(*, batch_size: int) -> str:
    stats = json.dumps(_new_episode_stats(), indent=2)
    new_ids = _new_ready_ids(batch_size)
    remaining = max(0, batch_size - len(new_ids))
    backlog_ids = _bb_founders_ready(remaining) if remaining else []
    # Dedupe while preserving order
    seen: set[str] = set()
    queue: list[str] = []
    for eid in new_ids + backlog_ids:
        if eid not in seen:
            seen.add(eid)
            queue.append(eid)
    queue = queue[:batch_size]

    queue_block = "\n".join(f"- {eid}" for eid in queue) if queue else "(none — report blockers)"

    return f"""
You are running the **nightly content update** for podcast-analyst (01:00 Beijing).

Goal: keep the public library current so the **Friday noon weekly digest** includes all episodes from the past 7 days.

Discovery and YouTube caption fetch already ran in CI. Your job is to **write and publish summaries only**.

## Priority (process in order, max {batch_size} episodes tonight)
1. **New releases** (published in last 7 days) with full transcript — highest priority
2. **BB/Founders expand pool** transcript-ready backlog (if batch slots remain)

Pending stats:
{stats}

Tonight's queue ({len(queue)} max):
{queue_block}

If the queue is empty, print stats and exit successfully.

## Per episode
1. Read full transcript in `data/transcripts/` (or fetch YouTube captions ONLY if missing — max 2 attempts, do not bulk fetch).
2. Write `data/approved/{{episode_id}}.json` using the correct template:
   - ILTB / Acquired: `config/template.yaml` or `config/template-acquired.yaml`
   - BB / Founders: `scripts/expand_bb_founders_agent_instructions.md` v4.10
3. Run `python scripts/publish_approved_batch.py {{episode_id}}`
4. Validate with `src/validate.py`; fix until pass.
5. US ticker symbols for public companies; no meta-phrasing.

## Do NOT
- Download mp3 or touch `data/audio_cache/`
- Run Whisper unless explicitly required (avoid in nightly)
- Bulk-fetch YouTube captions

## After all episodes
- `python scripts/normalize_summary_tickers.py --publish`
- `node web/scripts/sync-content.mjs` from `web/`

Print: episodes written, skipped IDs + blockers, final `report_new_episodes.py --stats`.
"""


def main() -> int:
    api_key = os.environ.get("CURSOR_API_KEY")
    if not api_key:
        print("CURSOR_API_KEY is required.", file=sys.stderr)
        return 2

    batch_size = int(os.environ.get("NIGHTLY_BATCH_SIZE", str(DEFAULT_BATCH)))

    try:
        from cursor_sdk import Agent, AgentOptions, LocalAgentOptions
    except Exception as exc:
        print(f"cursor-sdk import failed: {exc}", file=sys.stderr)
        return 2

    model = os.environ.get("CURSOR_AGENT_MODEL", "gpt-5.5-medium")
    result = Agent.prompt(
        build_prompt(batch_size=batch_size),
        AgentOptions(
            api_key=api_key,
            model=model,
            local=LocalAgentOptions(cwd=str(ROOT)),
        ),
    )
    print(f"Cursor agent status: {result.status}")
    print(result.result or "")
    return 0 if result.status == "completed" else 1


if __name__ == "__main__":
    raise SystemExit(main())
