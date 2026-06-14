#!/usr/bin/env python3
"""Validate and publish all approved Acquired summaries."""

from __future__ import annotations

import argparse
import json
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))

from scripts.publish_approved_batch import publish  # noqa: E402
from src.template_config import template_path_for_podcast  # noqa: E402
from src.validate import load_template_config, validate_rating_distribution, validate_summary  # noqa: E402

APPROVED = ROOT / "data" / "approved"
TMPL = load_template_config(template_path_for_podcast("Acquired"))


def validate_all(*, prefix: str = "acq-") -> tuple[list[str], list[tuple[str, str]]]:
    ok: list[str] = []
    bad: list[tuple[str, str]] = []
    for path in sorted(APPROVED.glob(f"{prefix}*.json")):
        data = json.loads(path.read_text(encoding="utf-8"))
        report = validate_summary(data, TMPL)
        rating = data.get("episode_rating", {}).get("overall")
        try:
            rating_int = int(rating)
            if float(rating) == rating_int and 1 <= rating_int <= 5:
                for issue in validate_rating_distribution(
                    rating_int, TMPL, APPROVED, podcast="Acquired", episode_id=path.stem
                ):
                    report.add(issue.section, issue.message, issue.severity)
        except (TypeError, ValueError):
            pass
        if report.passed:
            ok.append(path.stem)
        else:
            msgs = "; ".join(i.message for i in report.issues if i.severity == "error")
            bad.append((path.stem, msgs))
    return ok, bad


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--publish", action="store_true")
    parser.add_argument("--prefix", default="acq-")
    args = parser.parse_args()
    ok, bad = validate_all(prefix=args.prefix)
    print(f"valid: {len(ok)}, invalid: {len(bad)}")
    for eid, msg in bad:
        print(f"  FAIL {eid}: {msg}")
    if args.publish and ok:
        n = publish(ok, sync_web=True)
        print(f"published: {n}")


if __name__ == "__main__":
    main()
