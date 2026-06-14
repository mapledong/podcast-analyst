#!/usr/bin/env python3
"""Write/fix early-season v5.1 Acquired JSON for episodes 10–17 backlog."""
from __future__ import annotations

import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))

from scripts._early_acq_v51_common import base, counted_words  # noqa: E402
from src.template_config import template_path_for_podcast  # noqa: E402
from src.validate import load_template_config, validate_summary  # noqa: E402

APPROVED = ROOT / "data" / "approved"
TMPL = load_template_config(template_path_for_podcast("Acquired"))

# --- bodies without metadata wrapper ---
BODIES: dict[str, dict] = {}

def body(
    rating: int,
    keywords: list[str],
    conclusion: str,
    background: str,
    important_facts: list[str],
    mental_model: dict,
    competitive_advantage: str,
    key_insights: list[dict],
    top_investment_implications: list[dict],
    golden_quotes: list[str],
    chronology: dict,
) -> dict:
    return {
        "episode_rating": {"overall": rating},
        "keywords": keywords,
        "conclusion": conclusion,
        "background": background,
        "important_facts": important_facts,
        "mental_model": mental_model,
        "competitive_advantage": competitive_advantage,
        "key_insights": key_insights,
        "top_investment_implications": top_investment_implications,
        "golden_quotes": golden_quotes,
        "chronology": chronology,
    }


# Populated below via exec of episode modules - import from separate file
from scripts._finalize_early_v51_bodies import EPISODE_BODIES  # noqa: E402

TARGET = [
    "acq-episode-13-push-pop-press-facebook-instant-articles-with-todd-bishop",
    "acq-acquired-top-ten-the-best-acquisitions-of-all-time",
    "acq-acquired-episode-17-waze",
    "acq-acquired-episode-16-midroll-stitcher-acquired-by-scripps",
    "acq-acquired-episode-15-exacttarget-acquired-by-salesforce-with-scott-dorsey",
]


def main() -> None:
    results = []
    for ep_id in TARGET:
        if ep_id not in EPISODE_BODIES:
            results.append((ep_id, "no_body", 0, False))
            continue
        data = base(ep_id, **EPISODE_BODIES[ep_id])
        path = APPROVED / f"{ep_id}.json"
        path.write_text(json.dumps(data, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
        report = validate_summary(data, TMPL)
        wc = counted_words(data)
        results.append((ep_id, "pass" if report.passed else "fail", wc, report.passed))
        if not report.passed:
            for i in report.issues:
                print(f"  [{i.severity}] {ep_id} {i.section}: {i.message}")

    # patch all 9 user-requested ids
    from scripts._patch_early_v51_validate import patch  # noqa: E402

    all_nine = [
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
    print("\n--- final validation (9 episodes) ---")
    for ep_id in all_nine:
        path = APPROVED / f"{ep_id}.json"
        if not path.exists():
            print(f"MISSING {ep_id}")
            continue
        data = json.loads(path.read_text(encoding="utf-8"))
        data = patch(data)
        path.write_text(json.dumps(data, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
        report = validate_summary(data, TMPL)
        wc = counted_words(data)
        print(f"{ep_id}: words={wc} pass={report.passed}")
        if not report.passed:
            for i in report.issues:
                if i.severity == "error":
                    print(f"  {i.section}: {i.message}")

    if any(r[3] is False for r in results if len(results)):
        pass


if __name__ == "__main__":
    main()
