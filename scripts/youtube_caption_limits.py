"""Shared conservative rate limits for YouTube caption / transcript fetches.

Defaults favor **small batches, many runs** to avoid 429 / IP blocks.
Override via env for local testing only:

  YOUTUBE_CAPTION_BATCH_SIZE=2
  YOUTUBE_CAPTION_DELAY=90
"""

from __future__ import annotations

import os
import random
import sys
import time

DEFAULT_BATCH_SIZE = int(os.environ.get("YOUTUBE_CAPTION_BATCH_SIZE", "2"))
DEFAULT_TRANSCRIPT_DELAY = float(os.environ.get("YOUTUBE_CAPTION_DELAY", "90"))
MAX_TRANSCRIPT_RETRIES = 3
TRANSCRIPT_BACKOFF_DELAYS = (90, 180, 360)
# Extra random pause on top of delay (seconds)
JITTER_RANGE = (8.0, 30.0)


def sleep_between_episodes(delay: float, *, reason: str = "between episodes") -> None:
    jitter = random.uniform(*JITTER_RANGE)
    total = delay + jitter
    print(f"  sleeping {total:.0f}s ({reason}, base {delay:.0f}s + jitter {jitter:.0f}s) …")
    time.sleep(total)


def sleep_logged(seconds: float, *, reason: str) -> None:
    print(f"  sleeping {seconds:.0f}s ({reason}) …")
    time.sleep(seconds)


def reject_bulk_unless_forced(*, bulk_flag: bool, flag_name: str) -> None:
    """Abort bulk queue processing unless explicitly opted in."""
    if not bulk_flag:
        return
    if os.environ.get("YOUTUBE_CAPTION_BULK_OK") == "1":
        print(
            f"WARNING: {flag_name} enabled with YOUTUBE_CAPTION_BULK_OK=1 — "
            "high risk of YouTube rate limits / IP blocks.",
            file=sys.stderr,
        )
        return
    print(
        f"Refusing {flag_name}: bulk caption fetch risks YouTube 429 / IP blocks.\n"
        "Use the scheduled workflow (2 episodes × several times daily) or rerun with\n"
        "default batch limits. For a one-off bulk run only: YOUTUBE_CAPTION_BULK_OK=1",
        file=sys.stderr,
    )
    raise SystemExit(2)


def _is_transient_youtube_error(exc: Exception) -> bool:
    msg = str(exc).lower()
    name = type(exc).__qualname__.lower()
    markers = (
        "429",
        "too many requests",
        "ipblocked",
        "ip blocked",
        "ipblock",
        "rate limit",
        "connection reset",
        "timed out",
        "timeout",
        "temporary failure",
        "503",
        "502",
        "service unavailable",
    )
    return any(marker in msg or marker in name for marker in markers)


def with_transcript_backoff(fn, *, episode_id: str):
    last_err: Exception | None = None
    for attempt in range(MAX_TRANSCRIPT_RETRIES + 1):
        if attempt:
            wait = TRANSCRIPT_BACKOFF_DELAYS[min(attempt - 1, len(TRANSCRIPT_BACKOFF_DELAYS) - 1)]
            print(f"  retry {attempt}/{MAX_TRANSCRIPT_RETRIES} for {episode_id}, sleeping {wait}s …")
            time.sleep(wait)
        try:
            return fn()
        except Exception as exc:
            last_err = exc
            if not _is_transient_youtube_error(exc) or attempt >= MAX_TRANSCRIPT_RETRIES:
                raise
    raise last_err or RuntimeError(f"transcript fetch failed for {episode_id}")
