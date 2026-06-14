#!/usr/bin/env python3
"""Batch-fetch Colossus page transcripts for curated BB/Founders episodes."""

from __future__ import annotations

import argparse
import sys
import time
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))

from scripts.fetch_colossus_transcript import fetch_transcript, save  # noqa: E402
from scripts.resolve_curated_bb_founders import resolve_curated  # noqa: E402


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--delay", type=float, default=1.0)
    args = parser.parse_args()

    rows = resolve_curated()
    ok = skip = fail = 0
    for eps in rows.values():
        for ep in eps:
            if ep["has_transcript"]:
                skip += 1
                continue
            url = ep.get("colossus_url") or ""
            if not url:
                skip += 1
                continue
            eid = ep["id"]
            out = ROOT / "data" / "transcripts" / f"{eid}.txt"
            if out.exists() and out.stat().st_size > 1500:
                skip += 1
                continue
            prefix = "bb" if ep["podcast"] == "Business Breakdowns" else "fnd"
            slug = url.rstrip("/").split("/")[-1]
            try:
                text, n = fetch_transcript(url)
                save(slug, text, n, prefix=prefix)
                out.write_text(
                    f"# source: joincolossus.com\n# episode_id: {eid}\n# lines: {n}\n\n{text}\n",
                    encoding="utf-8",
                )
                print(f"✓ {eid} ({len(text)} chars)")
                ok += 1
            except Exception as exc:
                print(f"✗ {eid}: {exc}")
                fail += 1
            time.sleep(args.delay)
    print(f"\nFetched {ok}, skipped {skip}, failed {fail}")


if __name__ == "__main__":
    main()
