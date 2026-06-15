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
DEFAULT_SDK_TIMEOUT_S = 3600.0


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


def build_queue(*, batch_size: int) -> list[str]:
    new_ids = _new_ready_ids(batch_size)
    remaining = max(0, batch_size - len(new_ids))
    backlog_ids = _bb_founders_ready(remaining) if remaining else []
    seen: set[str] = set()
    queue: list[str] = []
    for eid in new_ids + backlog_ids:
        if eid not in seen:
            seen.add(eid)
            queue.append(eid)
    return queue[:batch_size]


def build_episode_prompt(episode_id: str, *, index: int, total: int) -> str:
    return f"""
You are running the **nightly content update** for podcast-analyst (episode {index}/{total}).

Write and publish **one** episode summary: `{episode_id}`

## Steps
1. Read the full transcript in `data/transcripts/` (fetch YouTube captions only if missing — max 2 attempts).
2. Write `data/approved/{episode_id}.json` using the correct template:
   - ILTB / Acquired: `config/template.yaml` or `config/template-acquired.yaml`
   - BB / Founders: `scripts/expand_bb_founders_agent_instructions.md` v4.10
3. Run `python scripts/publish_approved_batch.py {episode_id}`
4. Validate with `src/validate.py`; fix until pass.
5. US ticker symbols for public companies; analyst prose only (no meta-phrasing).

## Prose rules
- Complete sentences only — no incomplete transcript fragments or dangling quotes.
- Do not use "He states:", "He also gives a concrete magnitude:", or similar template filler.
- Weave numbers naturally into the analysis.

## Do NOT
- Download mp3 or touch `data/audio_cache/`
- Run Whisper unless explicitly required
- Bulk-fetch YouTube captions

Print: status for {episode_id}, validation outcome, blockers if any.
"""


def _run_episode_agent(
    client,
    prompt: str,
    *,
    api_key: str,
    model: str,
) -> tuple[str, str]:
    from cursor_sdk import LocalAgentOptions

    with client.agents.create(
        model=model,
        api_key=api_key,
        local=LocalAgentOptions(cwd=str(ROOT)),
    ) as agent:
        result = agent.send(prompt).wait()
    return result.status, (result.result or "")


def main() -> int:
    api_key = os.environ.get("CURSOR_API_KEY")
    if not api_key:
        print("CURSOR_API_KEY is required.", file=sys.stderr)
        return 2

    batch_size = int(os.environ.get("NIGHTLY_BATCH_SIZE", str(DEFAULT_BATCH)))
    model = os.environ.get("CURSOR_AGENT_MODEL", "auto")
    timeout_s = float(os.environ.get("CURSOR_SDK_TIMEOUT", str(DEFAULT_SDK_TIMEOUT_S)))

    try:
        from cursor_sdk import CursorClient  # noqa: F401 — verify import
    except Exception as exc:
        print(f"cursor-sdk import failed: {exc}", file=sys.stderr)
        return 2

    stats = json.dumps(_new_episode_stats(), indent=2)
    queue = build_queue(batch_size=batch_size)
    print(f"Pending stats:\n{stats}")
    print(f"Tonight's queue ({len(queue)} max): {queue}")

    if not queue:
        print("Queue empty — nothing to summarize.")
        return 0

    failed: list[str] = []
    with CursorClient.launch_bridge(workspace=str(ROOT)) as client:
        client = client.with_options(timeout=timeout_s, max_retries=2)
        for index, episode_id in enumerate(queue, start=1):
            print(f"\n=== Episode {index}/{len(queue)}: {episode_id} ===", flush=True)
            prompt = build_episode_prompt(episode_id, index=index, total=len(queue))
            try:
                status, text = _run_episode_agent(
                    client,
                    prompt,
                    api_key=api_key,
                    model=model,
                )
                print(f"Cursor agent status: {status}")
                if text:
                    print(text)
                if status != "completed":
                    failed.append(episode_id)
            except Exception as exc:
                print(f"Agent error for {episode_id}: {exc}", file=sys.stderr)
                failed.append(episode_id)

    print(f"\nFinished: {len(queue) - len(failed)}/{len(queue)} succeeded")
    if failed:
        print(f"Failed: {', '.join(failed)}", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
