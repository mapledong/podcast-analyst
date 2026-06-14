#!/usr/bin/env python3
"""Download Megaphone audio for curated episodes missing cache files."""

from __future__ import annotations

import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))

from scripts.transcribe_acquired_audio import _download_audio  # noqa: E402
from scripts.resolve_curated_bb_founders import resolve_curated  # noqa: E402

AUDIO = ROOT / "data" / "audio_cache"


def main() -> None:
    rows = resolve_curated()
    ok = skip = fail = 0
    for ep in (e for eps in rows.values() for e in eps):
        eid = ep["id"]
        dest = AUDIO / f"{eid}.mp3"
        if dest.exists() and dest.stat().st_size > 100_000:
            skip += 1
            continue
        url = ep.get("audio_url") or ""
        if not url:
            print(f"✗ {eid}: no audio_url")
            fail += 1
            continue
        try:
            print(f"downloading {eid} …")
            _download_audio(url, dest)
            print(f"✓ {eid} ({dest.stat().st_size // 1024} KB)")
            ok += 1
        except Exception as exc:
            print(f"✗ {eid}: {exc}")
            fail += 1
    print(f"\nDone: {ok} downloaded, {skip} cached, {fail} failed")


if __name__ == "__main__":
    main()
