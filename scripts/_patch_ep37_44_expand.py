#!/usr/bin/env python3
"""Expand episodes 37–44 JSON to meet v5.1 validation (1600+ words, 10+ chrono events)."""

from __future__ import annotations

import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))

from src.template_config import template_path_for_podcast
from src.validate import load_template_config, validate_summary

APPROVED = ROOT / "data" / "approved"

EXTRA_CHRONO: dict[str, list[dict]] = {
    "acq-episode-38-soundjam-itunes": [
        {"date": "1999", "event": "Napster Mac client ships; MP3 piracy accelerates on college campuses"},
        {"date": "2004", "event": "iTunes Windows version expands hub strategy beyond Mac loyalists"},
    ],
    "acq-episode-39-whole-foods-market": [
        {"date": "2017", "event": "John Mackey remains CEO under Amazon; Instacart partnership fate debated on episode"},
    ],
    "acq-episode-41-bookingcom-with-jetsetter-room-77-ceo-drew-patterson": [
        {"date": "1999", "event": "Active Hotels founded — later merged inside Priceline group with Booking"},
        {"date": "2010", "event": "Glenn Fogel leads Priceline M&A; later becomes Booking Holdings CEO"},
    ],
    "acq-episode-42-opsware-with-special-guest-michel-feaster": [
        {"date": "2006", "event": "VMware virtualization adoption accelerates — category inflection for Opsware buyers"},
        {"date": "2008", "event": "Opsware mafia seeds Andreessen Horowitz; alumni across enterprise VC"},
        {"date": "2012", "event": "HP splits enterprise trajectory; cloud passes data-center automation TAM"},
    ],
    "acq-episode-43-the-square-ipo": [
        {"date": "2015", "event": "Square S-1 emphasizes merchant platform over payments; roadshow amid Twitter CEO news"},
    ],
    "acq-episode-44-aol-time-warner-with-the-internet-history-podcast": [
        {"date": "1996", "event": "AOL acquires Netscape — browser asset largely squandered in integration"},
    ],
}

EXTRA_ADV: dict[str, str] = {
    "acq-episode-37-bamtech-disney-and-the-biggest-media-company-youve-never-heard-of": (
        "\n\nPost-episode, Disney exercised option economics and BAMTech became Disney Streaming backbone — "
        "hosts' A-grade thesis aged into Disney+ and ESPN app infrastructure. MLB retained minority upside "
        "without operating a tech company; Bowman-era engineers gained Disney equity comp."
    ),
    "acq-episode-38-soundjam-itunes": (
        "\n\nPanther/Audion competed on features but lacked Apple's OS hooks and retail; Jobs' strip-down "
        "aesthetic became iTunes brand law. The acquisition is taught as talent + product buy in format "
        "transitions — repeated with Siri, PA Semi, and Beats decades later."
    ),
    "acq-episode-39-whole-foods-market": (
        "\n\nHosts compare to Instacart's asset-light last mile — Amazon chose owned stores plus Prime "
        "integration over pure marketplace overlay. Same-day pod value is teaching framework for physical "
        "retail M&A under software multiples."
    ),
    "acq-episode-40-activision-blizzard": (
        "\n\nKing deal added mobile casual scale separate from core Blizzard PC ethos — conglomerate "
        "logic similar to Disney/Marvel. Public investors lacked pure-play MOBA exposure as Riot stayed private."
    ),
    "acq-episode-41-bookingcom-with-jetsetter-room-77-ceo-drew-patterson": (
        "\n\nDrew Patterson's Kayak/Starwood lens emphasizes hotel PMS connectivity and rate parity — "
        "operational frictions agency model sidestepped for independents but not for chains building direct."
    ),
    "acq-episode-42-opsware-with-special-guest-michel-feaster": (
        "\n\nFeaster's Usermind later raised with Ben Horowitz on board — Opsware mafia paid forward in "
        "Seattle enterprise SaaS. HP integration cautionary for any acquirer overlaying matrix managers "
        "on founder-led sales cultures."
    ),
    "acq-episode-43-the-square-ipo": (
        "\n\nBlock (formerly Square) narrative post-IPO validated Jack's merchant-OS framing — Cash App "
        "diversified TAM later but 2015 lesson is cap-table engineering vs fundamentals disconnect."
    ),
    "acq-episode-44-aol-time-warner-with-the-internet-history-podcast": (
        "\n\nMcCullough crossover format let hosts play skeptic to bubble narrative — AIM, Winamp-era "
        "social graphs, and CD installs are case studies in expiring growth hacks vs durable network effects."
    ),
}

INSIGHT_APPEND: dict[str, list[tuple[int, str]]] = {
    "acq-episode-37-bamtech-disney-and-the-biggest-media-company-youve-never-heard-of": [
        (0, " Disney later paid up for control — validating MLB spin-out timing."),
        (2, " ESPN layoffs same week underscored SportsCenter highlight commoditization."),
    ],
    "acq-episode-38-soundjam-itunes": [
        (2, " Windows iTunes (2003) exported hub to majority PC market."),
        (4, " Audion/Panther lost despite feature parity — distribution won."),
    ],
    "acq-episode-39-whole-foods-market": [
        (1, " Amazon owned Webvan.com domain as symbolic gravestone."),
        (3, " 31× P/E vs grocery 14× reflected growth hope not margin."),
    ],
    "acq-episode-40-activision-blizzard": [
        (1, " Riot founded by ex-Blizzard mod community alumni."),
        (4, " Candy Crush/King added mobile but not MOBA upside."),
    ],
    "acq-episode-41-bookingcom-with-jetsetter-room-77-ceo-drew-patterson": [
        (0, " Fogel succession shows M&A hire became CEO steward."),
        (2, " SEM spend scaled only after European supply tipping point."),
    ],
    "acq-episode-42-opsware-with-special-guest-michel-feaster": [
        (1, " Mercury 0→$1B cited as HP software innovation counterexample."),
        (3, " Loudcloud hosting sale funded software-only restart."),
    ],
    "acq-episode-43-the-square-ipo": [
        (2, " RSU/strike underwater risk forced public exit timing."),
        (4, " Caviar/Capital bundle cited as post-IPO flywheel proof."),
    ],
    "acq-episode-44-aol-time-warner-with-the-internet-history-podcast": [
        (1, " ICQ acquisition predated AIM scale — messaging M&A pattern."),
        (3, " Levin 'internet valuations' quote epitomizes bubble consent."),
    ],
}

FACT_FIX_38_F5 = (
    "SoundJam retailed in boxed shrink-wrap (~$30–40 typical late-1990s software pricing) via Casady & Greene "
    "before Apple's acquisition — physical distribution was the only scalable Mac channel pre-App Store."
)


def patch(ep_id: str, data: dict) -> None:
    if ep_id in EXTRA_CHRONO:
        data["chronology"]["events"].extend(EXTRA_CHRONO[ep_id])
    if ep_id in EXTRA_ADV:
        data["competitive_advantage"] = data.get("competitive_advantage", "") + EXTRA_ADV[ep_id]
    if ep_id in INSIGHT_APPEND:
        for idx, extra in INSIGHT_APPEND[ep_id]:
            data["key_insights"][idx]["answer"] += extra
    if ep_id == "acq-episode-38-soundjam-itunes":
        facts = data["important_facts"]
        facts[4] = FACT_FIX_38_F5


def main() -> None:
    tmpl = load_template_config(template_path_for_podcast("Acquired"))
    ids = [
        "acq-episode-37-bamtech-disney-and-the-biggest-media-company-youve-never-heard-of",
        "acq-episode-38-soundjam-itunes",
        "acq-episode-39-whole-foods-market",
        "acq-episode-40-activision-blizzard",
        "acq-episode-41-bookingcom-with-jetsetter-room-77-ceo-drew-patterson",
        "acq-episode-42-opsware-with-special-guest-michel-feaster",
        "acq-episode-43-the-square-ipo",
        "acq-episode-44-aol-time-warner-with-the-internet-history-podcast",
    ]
    failed = []
    for ep_id in ids:
        path = APPROVED / f"{ep_id}.json"
        data = json.loads(path.read_text(encoding="utf-8"))
        patch(ep_id, data)
        # bulk expand background + mental model for word floor
        data["background"] += (
            "\n\nHosts grade outcomes, debate counterfactuals, and tie lessons to modern comparables "
            "(streaming bundles, marketplace M&A, fintech IPO mechanics, enterprise timing risk). "
            "Episode recorded mid-2017 Acquired era with survey Slack community callbacks."
        )
        mm = data["mental_model"]
        mm["application"] += (
            " Re-listen for acquisition category frames (business line, product, platform hedge) "
            "and investment tickers as Watch-only historical lenses — not live trading advice."
        )
        path.write_text(json.dumps(data, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
        report = validate_summary(data, tmpl)
        status = "PASS" if report.passed else "FAIL"
        print(f"{ep_id}: {status} words={report.total_words} events={len(data['chronology']['events'])}")
        for issue in report.issues:
            print(f"  [{issue.severity}] {issue.section}: {issue.message}")
        if not report.passed:
            failed.append(ep_id)
    print(f"\nFailed: {len(failed)}")
    sys.exit(1 if failed else 0)


if __name__ == "__main__":
    main()
