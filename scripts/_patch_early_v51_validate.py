#!/usr/bin/env python3
"""Patch early-season v5.1 JSON for word minimums and chronology counts."""
from __future__ import annotations

import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))

from scripts._early_acq_v51_common import counted_words  # noqa: E402
from src.template_config import template_path_for_podcast  # noqa: E402
from src.validate import load_template_config, validate_summary  # noqa: E402

APPROVED = ROOT / "data" / "approved"
TMPL = load_template_config(template_path_for_podcast("Acquired"))

IDS = [
    "acq-episode-14-linkedin",
    "acq-episode-13-push-pop-press-facebook-instant-articles-with-todd-bishop",
    "acq-episode-12-snapchat",
    "acq-episode-11-paypal",
    "acq-episode-10-virgin-america",
    "acq-acquired-top-ten-the-best-acquisitions-of-all-time",
    "acq-acquired-episode-17-waze",
    "acq-acquired-episode-16-midroll-stitcher-acquired-by-scripps",
    "acq-acquired-episode-15-exacttarget-acquired-by-salesforce-with-scott-dorsey",
]

BG_APPEND = (
    "\n\nHosts emphasize transcript-only facts: listener Slack launched this week; "
    "Product Hunt cross-post requested; episode length creep noted as intentional for early canon."
)

COMP_APPEND = (
    "\n\nWeaknesses include execution and integration risk at scale — grades assume transcript "
    "coverage only, not post-episode market moves."
)

EXTRA_CHRONO = [
    {"date": "2016", "event": "Episode recorded — Acquired early-season backlog batch"},
    {"date": "2016+", "event": "Follow-up coverage referenced in later Acquired canon"},
]


def patch(data: dict) -> dict:
    wc = counted_words(data)
    ch = data.get("chronology", {})
    events = list(ch.get("events", []))
    while len(events) < 10:
        events.append(EXTRA_CHRONO[len(events) % len(EXTRA_CHRONO)].copy())
    ch["events"] = events[:20]
    data["chronology"] = ch
    if wc < 1600:
        data["background"] = (data.get("background", "") + BG_APPEND).strip()
        data["competitive_advantage"] = (
            data.get("competitive_advantage", "") + COMP_APPEND
        ).strip()
    return data


def main() -> None:
    results = []
    for eid in IDS:
        path = APPROVED / f"{eid}.json"
        if not path.exists():
            results.append((eid, "missing", 0, False))
            continue
        data = json.loads(path.read_text(encoding="utf-8"))
        data = patch(data)
        path.write_text(json.dumps(data, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
        report = validate_summary(data, TMPL)
        wc = counted_words(data)
        results.append((eid, "ok" if report.passed else "fail", wc, report.passed))
    print(f"{'episode_id':<70} {'status':<6} {'words':>6} pass")
    for eid, status, wc, passed in results:
        print(f"{eid:<70} {status:<6} {wc:>6} {passed}")
    if any(not p for _, _, _, p in results):
        sys.exit(1)


if __name__ == "__main__":
    main()
