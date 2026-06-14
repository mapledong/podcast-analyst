#!/usr/bin/env python3
"""One-shot transcript-grounded expansion for 10 Acquired episodes (v5.4)."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))

from scripts._expand_acq_batch_user_10_bodies import BODIES  # noqa: E402
from src.validate import load_template_config, validate_summary, word_gap  # noqa: E402
from src.template_config import template_path_for_podcast  # noqa: E402

APPROVED = ROOT / "data" / "approved"
TMPL = load_template_config(template_path_for_podcast("Acquired"))

EPISODE_IDS = list(BODIES.keys())


def apply_expansion(eid: str) -> tuple[int, int, list[str]]:
    path = APPROVED / f"{eid}.json"
    data = json.loads(path.read_text(encoding="utf-8"))
    before = validate_summary(data, TMPL).total_words

    patch = BODIES[eid]
    for key, val in patch.items():
        data[key] = val

    notes = str(data.get("review_notes", "")).strip()
    if "optimized v5.4" not in notes:
        data["review_notes"] = f"{notes} | optimized v5.4".strip(" |")

    path.write_text(json.dumps(data, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")

    after_report = validate_summary(data, TMPL)
    after = after_report.total_words
    warnings = [w.message for w in after_report.issues if w.severity == "warning"]
    return before, after, warnings


def main() -> None:
    results = []
    for eid in EPISODE_IDS:
        before, after, warnings = apply_expansion(eid)
        d = json.loads((APPROVED / f"{eid}.json").read_text())
        gap = word_gap(d, TMPL)
        results.append((eid, before, after, gap, warnings))

        if gap == 0:
            subprocess.run(
                [sys.executable, str(ROOT / "scripts" / "publish_approved_batch.py"), eid],
                check=True,
                cwd=ROOT,
            )

    print("\n=== EXPANSION RESULTS ===")
    for eid, before, after, gap, warnings in results:
        status = "OK" if gap == 0 else f"GAP {gap}"
        print(f"{eid}: {before} -> {after} [{status}]")
        for w in warnings[:5]:
            print(f"  - {w}")


if __name__ == "__main__":
    main()
