#!/usr/bin/env python3
"""Pick transcript-grounded golden quotes and patch refine body modules."""

from __future__ import annotations

import ast
import json
import re
import sys
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))
_SCRIPTS = Path(__file__).resolve().parent
if str(_SCRIPTS) not in sys.path:
    sys.path.insert(0, str(_SCRIPTS))

from src.chinese_transcript import (  # noqa: E402
    CHINESE_EPISODE_IDS,
    assess_summary_quotes,
    load_transcript_body,
    quote_supported_in_transcript,
    transcript_path,
)

BODY_FILES = [
    ROOT / "scripts" / "refine_chinese_pilot_bodies.py",
    ROOT / "scripts" / "refine_chinese_pilot_rest.py",
    ROOT / "scripts" / "refine_new_episodes_bodies.py",
    ROOT / "scripts" / "refine_batch3_episodes_bodies.py",
    ROOT / "scripts" / "refine_batch4_episodes_bodies.py",
]

SKIP_LINE_PATTERNS = (
    re.compile(r"^大家好"),
    re.compile(r"^哈[喽啰]"),
    re.compile(r"^欢迎"),
    re.compile(r"^我是小"),
    re.compile(r"^今天我们"),
)


def _cjk_ratio(line: str) -> float:
    if not line:
        return 0.0
    cjk = sum(1 for c in line if "\u4e00" <= c <= "\u9fff")
    return cjk / len(line)


def _is_garbled(line: str) -> bool:
    if len(set(line)) < max(8, len(line) // 6):
        return True
    if re.search(r"(.)\1{5,}", line):
        return True
    if line.count("我碰到") >= 3:
        return True
    return False


def _candidate_lines(transcript: str) -> list[str]:
    lines: list[str] = []
    for raw in transcript.splitlines():
        line = raw.strip()
        if len(line) < 15 or len(line) > 100:
            continue
        if any(p.search(line) for p in SKIP_LINE_PATTERNS):
            continue
        if line.count("?") > 2:
            continue
        if _cjk_ratio(line) < 0.55 and not re.search(r"[A-Za-z]{8,}", line):
            continue
        if _is_garbled(line):
            continue
        lines.append(line)
    seen: set[str] = set()
    ranked: list[str] = []
    for line in sorted(lines, key=lambda s: (_cjk_ratio(s), len(s)), reverse=True):
        key = re.sub(r"\s+", "", line)[:24]
        if key in seen:
            continue
        seen.add(key)
        ranked.append(line)
    return ranked


def _best_quotes(transcript: str, count: int = 3) -> list[str]:
    candidates = _candidate_lines(transcript)
    chosen: list[str] = []
    for line in candidates:
        if len(chosen) >= count:
            break
        if all(quote_supported_in_transcript(line, c, min_ratio=0.35) is False for c in chosen):
            chosen.append(line)
    while len(chosen) < count and candidates:
        for line in candidates:
            if line not in chosen:
                chosen.append(line)
                break
        else:
            break
    return chosen[:count]


def _load_refined() -> dict[str, dict[str, dict[str, Any]]]:
    from refine_chinese_pilot_bodies import REFINED  # noqa: WPS433

    return REFINED


def _replace_golden_quotes_in_file(path: Path, episode_id: str, locale: str, quotes: list[str]) -> bool:
    text = path.read_text(encoding="utf-8")
    marker = f'"{episode_id}"'
    if marker not in text:
        return False

    # Locate episode block and golden_quotes list for locale.
    ep_idx = text.find(marker)
    if ep_idx < 0:
        return False
    locale_marker = f'"{locale}"'
    loc_idx = text.find(locale_marker, ep_idx)
    if loc_idx < 0:
        return False
    gq_idx = text.find('"golden_quotes"', loc_idx)
    if gq_idx < 0:
        return False
    start = text.find("[", gq_idx)
    if start < 0:
        return False
    depth = 0
    end = start
    for i in range(start, len(text)):
        ch = text[i]
        if ch == "[":
            depth += 1
        elif ch == "]":
            depth -= 1
            if depth == 0:
                end = i + 1
                break
    if end <= start:
        return False

    new_list = "[" + ", ".join(json.dumps(q, ensure_ascii=False) for q in quotes) + "]"
    updated = text[:start] + new_list + text[end:]
    if updated == text:
        return False
    path.write_text(updated, encoding="utf-8")
    return True


def main() -> None:
    import argparse

    parser = argparse.ArgumentParser()
    parser.add_argument("ids", nargs="*", help="Episode IDs (default: all needing zh quote fixes)")
    parser.add_argument("--dry-run", action="store_true")
    parser.add_argument("--force", action="store_true", help="Replace quotes even if current ones pass")
    args = parser.parse_args()

    refined = _load_refined()
    targets = args.ids or list(CHINESE_EPISODE_IDS)
    patched = 0
    for eid in targets:
        tx_path = transcript_path(eid)
        if not tx_path.exists():
            print(f"skip {eid}: no transcript")
            continue
        body = load_transcript_body(tx_path)
        zh = refined.get(eid, {}).get("zh", {})
        current = zh.get("golden_quotes") or []
        issues = assess_summary_quotes({"podcast": "张小珺商业访谈录", "golden_quotes": current}, body)
        if not issues and current and not args.force:
            print(f"ok {eid}: zh quotes already grounded")
            continue
        quotes = _best_quotes(body, 3)
        if len(quotes) < 3:
            print(f"warn {eid}: only found {len(quotes)} quote candidates")
            continue
        print(f"patch {eid} zh quotes:")
        for q in quotes:
            print(f"  - {q[:80]}{'…' if len(q) > 80 else ''}")
        if args.dry_run:
            continue
        for path in BODY_FILES:
            if _replace_golden_quotes_in_file(path, eid, "zh", quotes):
                patched += 1
                print(f"  updated {path.name}")
                break
        else:
            print(f"  ERROR: could not locate {eid} in body files")

    print(f"\nPatched {patched} episode(s)")


if __name__ == "__main__":
    main()
