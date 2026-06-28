#!/usr/bin/env python3
"""Run the weekly podcast-summary update via Cursor SDK.

This script is intended for GitHub Actions. It asks a Cursor agent to discover
new episodes for existing podcast series, create transcript-grounded summaries,
publish them, and leave the repository with committed-ready file changes.
"""

from __future__ import annotations

import os
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parent.parent


WEEKLY_UPDATE_PROMPT = """
You are updating the podcast-analyst repository for the weekly Saturday refresh.

Goal:
- For existing podcast series only, discover newly released episodes since the
  last approved summary.
- Create transcript-grounded summaries for new episodes only.
- Publish approved JSON to outputs and sync the web catalog.

Scope:
- Podcast series currently supported by the repo: Invest Like the Best, Acquired,
  Business Breakdowns, Founders.
- Do not backfill old episodes unless they are already in a curated backlog and
  have full transcripts.

Use existing repo tooling where it works:
- Discovery: scripts/discover_iltb.py, scripts/discover_acquired.py,
  scripts/discover_colossus_podcasts.py.
- Transcript fetch/transcribe: existing fetch/transcribe scripts.
- Publish: scripts/publish_approved_batch.py.
  Acquired EP numbers are auto-assigned by publish date (oldest=EP.1); never
  hand-pick episode_number — publish will correct it. After bulk Acquired adds,
  optionally run scripts/fix_acquired_catalog.py to recalibrate star ratings.
- Ticker normalization: scripts/normalize_summary_tickers.py --publish.
- Meta prose cleanup: scripts/fix_meta_prose_batch.py when relevant.
- Web sync: node web/scripts/sync-content.mjs.

Quality rules:
- Use only full transcripts or official show notes with enough detail.
- No invented facts, dates, numbers, tickers, or quotes.
- No meta prose like "in the transcript" or "the episode says".
- Conclusions must foreground the episode's core takeaway.
- Public company keywords and tickers should use canonical US ticker symbols.
- Investment ideas (top_investment_implications): prefer Long/Short on the episode
  thesis; max one Watch per episode; never Watch on tradable tickers or Private:*
  names — publish will hard-fail validation otherwise. Framework-only episodes
  still need directional Long/Short on cited examples when tickers are listed.

Finish by printing:
- New approved episode IDs.
- Skipped IDs and exact blocker.
- Commands run for validation/publish/sync.
"""


def main() -> int:
    api_key = os.environ.get("CURSOR_API_KEY")
    if not api_key:
        print("CURSOR_API_KEY is required for weekly Cursor-agent updates.", file=sys.stderr)
        return 2

    try:
        from cursor_sdk import Agent, AgentOptions, LocalAgentOptions
    except Exception as exc:  # pragma: no cover - dependency only present in CI
        print(f"cursor-sdk is not installed or failed to import: {exc}", file=sys.stderr)
        return 2

    model = os.environ.get("CURSOR_AGENT_MODEL", "auto")

    result = Agent.prompt(
        WEEKLY_UPDATE_PROMPT,
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
