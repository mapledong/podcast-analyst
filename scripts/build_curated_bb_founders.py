#!/usr/bin/env python3
"""Build curated approved JSON for BB/Founders episode IDs."""

from __future__ import annotations

import argparse
import json
import sys
import time
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))

from src.extract import extract_summary, merge_with_metadata
from src.expand import load_transcript_text, resolve_transcript_path
from src.template_config import template_path_for_podcast
from src.validate import choose_rating, load_template_config, validate_rating_distribution, validate_summary

APPROVED = ROOT / "data" / "approved"
DISCOVERED_PATHS = (
    ROOT / "data" / "discovered" / "business_breakdowns_episodes.json",
    ROOT / "data" / "discovered" / "founders_episodes.json",
)


def _discovered_by_id() -> dict[str, dict]:
    out: dict[str, dict] = {}
    for path in DISCOVERED_PATHS:
        if not path.exists():
            continue
        payload = json.loads(path.read_text(encoding="utf-8"))
        for ep in payload.get("episodes", []):
            out[ep["id"]] = ep
    return out


def _clean_text_fields(data: dict) -> dict:
    # Enforce no "meta prose" references to transcript framing.
    banned = (
        "in the transcript",
        "the transcript says",
        "the transcript shows",
        "this transcript",
        "according to the transcript",
        "in this episode",
    )

    def clean(value):
        if isinstance(value, str):
            out = value
            for phrase in banned:
                out = out.replace(f" {phrase}", "")
                out = out.replace(phrase.capitalize(), phrase.capitalize().replace("the ", ""))
            return out.replace("  ", " ").strip()
        if isinstance(value, list):
            return [clean(v) for v in value]
        if isinstance(value, dict):
            return {k: clean(v) for k, v in value.items()}
        return value

    return clean(data)


def _metadata_for(ep: dict) -> dict:
    podcast = ep.get("podcast", "")
    episode_number = int(ep.get("episode_number") or 0)
    guest = ep.get("guest", "")
    guest_role = ep.get("guest_role", "")
    if podcast == "Founders":
        guest_role = f"Biography · Episode {episode_number}"
    return {
        "id": ep["id"],
        "episode_number": episode_number,
        "title": ep.get("title", ""),
        "guest": guest,
        "guest_role": guest_role,
        "date": ep.get("date", ""),
        "duration_minutes": int(ep.get("duration_minutes") or 60),
        "youtube_url": ep.get("youtube_url", ""),
    }


def _inject_links(data: dict, ep: dict) -> None:
    meta = data.setdefault("metadata", {})
    links = meta.setdefault("links", {})
    colossus = ep.get("colossus_url", "")
    audio = ep.get("audio_url", "")
    youtube = ep.get("youtube_url", "")
    if colossus:
        links["colossus"] = colossus
    if audio:
        links["audio"] = audio
    if youtube:
        links["youtube"] = youtube
    if ep.get("podcast") == "Business Breakdowns":
        links.setdefault("apple_podcasts", "https://podcasts.apple.com/podcast/business-breakdowns/id1559120677")
        links.setdefault("spotify", "https://open.spotify.com/show/4zQbeLbLgqKEyn7e2sKzez")
    elif ep.get("podcast") == "Founders":
        links.setdefault("founders", "https://www.founderspodcast.com")
        links.setdefault("apple_podcasts", "https://podcasts.apple.com/podcast/founders/id1141877104")


def build_one(eid: str, ep: dict, *, model: str) -> tuple[bool, str]:
    path = APPROVED / f"{eid}.json"
    if path.exists():
        return False, "already approved"

    stub = {"episode_id": eid, "podcast": ep.get("podcast"), "metadata": ep}
    tx_path = resolve_transcript_path(stub)
    if not tx_path:
        return False, "missing transcript"
    transcript = load_transcript_text(tx_path)

    podcast = ep.get("podcast", "")
    template = load_template_config(template_path_for_podcast(podcast))
    extracted = extract_summary(
        transcript,
        {
            "podcast": podcast,
            "episode_number": ep.get("episode_number"),
            "title": ep.get("title"),
            "guest": ep.get("guest"),
            "guest_role": ep.get("guest_role", ""),
            "duration_minutes": ep.get("duration_minutes", 60),
        },
        model=model,
    )

    merged = merge_with_metadata(
        extracted,
        _metadata_for(ep),
        {"podcast": podcast, "host": "Matt Reustle & Zack Fuss" if podcast == "Business Breakdowns" else "David Senra"},
        transcript_source="whisper/base",
        model=model,
    )
    merged["episode_id"] = eid
    merged["extraction_meta"]["status"] = "approved"
    merged["extraction_meta"]["template_version"] = "4.10"
    notes = str(merged.get("review_notes", "")).strip()
    merged["review_notes"] = f"{notes} | curated v4.10".strip(" |")
    _inject_links(merged, ep)
    merged = _clean_text_fields(merged)

    candidate = int(merged.get("episode_rating", {}).get("overall", 3))
    merged["episode_rating"] = {
        "overall": choose_rating(
            candidate,
            template,
            APPROVED,
            podcast=podcast,
            episode_id=eid,
            default_rating=3,
        )
    }

    report = validate_summary(merged, template)
    for issue in validate_rating_distribution(
        int(merged["episode_rating"]["overall"]),
        template,
        APPROVED,
        podcast=podcast,
        episode_id=eid,
    ):
        report.add(issue.section, issue.message, issue.severity)
    if not report.passed:
        errs = "; ".join(i.message for i in report.issues if i.severity == "error")
        return False, f"validation failed: {errs}"

    path.write_text(json.dumps(merged, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    return True, f"ok ({report.total_words} words)"


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("ids", nargs="+")
    parser.add_argument("--model", default="gpt-5.3-codex")
    parser.add_argument("--delay", type=float, default=1.0)
    args = parser.parse_args()

    by_id = _discovered_by_id()
    ok = 0
    fail = 0
    for i, eid in enumerate(args.ids, 1):
        ep = by_id.get(eid)
        if not ep:
            print(f"[{i}/{len(args.ids)}] {eid} ✗ missing in discovered")
            fail += 1
            continue
        success, msg = build_one(eid, ep, model=args.model)
        print(f"[{i}/{len(args.ids)}] {eid} {'✓' if success else '✗'} {msg}")
        if success:
            ok += 1
        else:
            fail += 1
        if i < len(args.ids):
            time.sleep(args.delay)

    print(f"\nDone: {ok} ok, {fail} failed")
    raise SystemExit(1 if fail else 0)


if __name__ == "__main__":
    main()
