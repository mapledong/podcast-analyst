#!/usr/bin/env python3
"""Validate a single Acquired approved JSON against v5.1 template."""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))

from src.template_config import template_path_for_podcast  # noqa: E402
from src.validate import load_template_config, validate_summary  # noqa: E402


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("episode_id", help="e.g. acq-amazon-com")
    args = parser.parse_args()
    path = ROOT / "data" / "approved" / f"{args.episode_id}.json"
    if not path.exists():
        raise SystemExit(f"Not found: {path}")
    data = json.loads(path.read_text(encoding="utf-8"))
    tmpl = load_template_config(template_path_for_podcast("Acquired"))
    report = validate_summary(data, tmpl)
    for issue in report.issues:
        print(f"[{issue.severity}] {issue.section}: {issue.message}")
    print(f"words={report.total_words} min={report.min_total_words} max={report.max_total_words} pass={report.passed}")
    raise SystemExit(0 if report.passed else 1)


if __name__ == "__main__":
    main()
