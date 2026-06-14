#!/usr/bin/env python3
"""Nightly BB/Founders expansion via Cursor SDK.

Processes episodes from `resolve_curated_bb_founders.py --ready --limit N`
(transcript-first expanded pool; default target 80 per podcast). Intended for
GitHub Actions (~2am Beijing) or local launchd on Mac mini.
"""

from __future__ import annotations

import os
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DEFAULT_TARGET = 80


def _ready_ids(limit: int) -> list[str]:
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
    ids = [ln.strip() for ln in proc.stdout.splitlines() if ln.strip() and not ln.startswith("/")]
    return ids[:limit]


def _stats_json() -> str:
    proc = subprocess.run(
        [sys.executable, str(ROOT / "scripts/resolve_curated_bb_founders.py"), "--stats"],
        capture_output=True,
        text=True,
        cwd=str(ROOT),
    )
    return proc.stdout.strip()


def build_prompt(*, batch_size: int) -> str:
    ready = _ready_ids(batch_size)
    stats = _stats_json()
    target = int(os.environ.get("TARGET_PER_PODCAST", str(DEFAULT_TARGET)))
    ready_block = "\n".join(f"- {eid}" for eid in ready) if ready else "(none — check --stats)"
    return f"""
You are expanding the podcast-analyst BB/Founders library (overnight batch).

Long-term goal: **{target}+ high-quality approved summaries per podcast** (Business Breakdowns + Founders).

Transcript-first policy:
1. **Write summaries only from full transcripts** in `data/transcripts/` (do not invent facts).
2. Episodes in the ready queue already have transcripts — prioritize those.
3. If the queue is short, fetch YouTube captions before summarizing (`scripts/fetch_founders_youtube.py` / `scripts/fetch_curated_youtube.py`) — avoid Whisper unless no transcript exists.
4. Do NOT download mp3 or touch `data/audio_cache/`.

Current stats:
{stats}

Write approved summaries for up to {batch_size} episodes from this ready queue (Founders first, then BB; transcript-ready first):
{ready_block}

If the ready queue has fewer than {batch_size} transcript-ready episodes, summarize all transcript-ready IDs first, then fetch YouTube captions for the next highest-priority pool episodes (YouTube URL, no transcript yet) and summarize if captions succeed. Do not run Whisper in this nightly job.

If empty after caption fetch attempts, report blockers and exit.

Instructions: read `scripts/expand_bb_founders_agent_instructions.md` and follow template v4.10.

For each episode:
1. Read full transcript in `data/transcripts/`.
2. Write `data/approved/{{episode_id}}.json` (transcript-grounded only).
3. Run `python scripts/publish_approved_batch.py {{episode_id}}`.
4. Validate with `src/validate.py`; fix until pass.
5. Use US ticker symbols in keywords; no meta-phrasing; impactful conclusion.

After all episodes:
- Run `python scripts/normalize_summary_tickers.py --publish` if any new summaries.
- Run `node web/scripts/sync-content.mjs` from `web/`.
- Do NOT add, commit, or modify anything under `data/audio_cache/` or any `*.mp3` files.

Print: episodes written, final `--stats`, and any blockers.
"""


def main() -> int:
    api_key = os.environ.get("CURSOR_API_KEY")
    if not api_key:
        print("CURSOR_API_KEY is required.", file=sys.stderr)
        return 2

    batch_size = int(os.environ.get("NIGHTLY_BATCH_SIZE", "10"))

    try:
        from cursor_sdk import Agent, AgentOptions, LocalAgentOptions
    except Exception as exc:
        print(f"cursor-sdk import failed: {exc}", file=sys.stderr)
        return 2

    model = os.environ.get("CURSOR_AGENT_MODEL", "gpt-5.5-medium")
    prompt = build_prompt(batch_size=batch_size)

    result = Agent.prompt(
        prompt,
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
