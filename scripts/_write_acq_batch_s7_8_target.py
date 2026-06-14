#!/usr/bin/env python3
"""Write and validate 8 Acquired v5.1 approved JSON files (target batch)."""

from __future__ import annotations

import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))

from src.template_config import template_path_for_podcast  # noqa: E402
from src.validate import load_template_config, validate_summary  # noqa: E402
from scripts._write_acq_batch_491_500_common import base  # noqa: E402

APPROVED = ROOT / "data" / "approved"
TMPL = load_template_config(template_path_for_podcast("Acquired"))
NOTES = "Manual GPT Acquired batch v5.1 — Season 7/8 target batch"

EPISODES: dict[str, dict] = {}

EPISODES["acq-special-sequoia-capitals-investment-playbook-with-alfred-lin"] = base(
    "acq-special-sequoia-capitals-investment-playbook-with-alfred-lin",
    review_notes=NOTES,
    episode_rating={"overall": 4},
    keywords=["Prepared Mind", "Venture Sourcing", "Unit Economics"],
    conclusion=(
        "Alfred Lin distills Sequoia's \"prepared mind\" doctrine: partners do proactive landscape work "
        "before pitches arrive, then debate whether a cute seed idea (Airbnb air beds) becomes a global "
        "category. He contrasts Don Valentine's early Apple sale ($6M profit vs. holding) with today's "
        "multi-stage, multi-geo partnership — seed through growth, US plus China, India, and Europe. "
        "The US early-stage practice is only ~8 people, kept small to limit communication overhead. "
        "Lin sits on boards including Airbnb and DoorDash, tying this interview directly to Acquired's "
        "IPO week coverage. For founders: reach out with a specific problem and timing thesis; for "
        "investors: market size and gross margins still gate opportunities, but winners often reveal "
        "network effects after supply and demand scale globally."
    ),
    background=(
        "Recorded January 2021, this special follows Acquired's two-part Sequoia history and features "
        "partner Alfred Lin — Zappos COO, Venture Frogs co-founder with Tony Hsieh, now Sequoia's US "
        "early-stage lead. Ben and David probe how personal fascination (food delivery, timeshares) "
        "bubbles into firm-wide theses before entrepreneurs walk in the door.\n\n"
        "Lin walks through landscape diligence: what market change is occurring, what specific problem "
        "is solved, and whether timing is right. He recounts internal debates over Brian Chesky's "
        "hotels vision, financing Airbnb's expensive European ground war against Wimdu, and when global "
        "network effects became obvious. The conversation covers seed vs. growth entry points, "
        "cross-geo learning without drowning in meetings, hiring partners Don Valentine-style, and "
        "why Amazon's 21st post-IPO year can exceed its first 20 combined — a reminder that venture "
        "returns concentrate in the out years."
    ),
    important_facts=[
        "Acquired's Sequoia history cited portfolio companies worth over $3.3 trillion versus a ~$10 trillion Nasdaq at recording — both figures materially higher by 2021.",
        "Alfred Lin manages Sequoia's US early-stage practice with roughly 8 people — intentionally small relative to the firm's global partnership.",
        "Sequoia's early Apple investment reportedly netted ~$6 million profit on a pre-IPO stake — a sale Lin cites as long-run suboptimal versus holding compounding winners.",
        "Lin references Amazon generating as much or more profit in its 21st year after IPO as in the prior 20 years combined — illustrating venture return curvature.",
        "Alfred Lin serves on boards including Airbnb, DoorDash, Houzz, Instacart, Reddit, and Zipline — linking this playbook episode to Acquired's concurrent IPO coverage.",
    ],
    mental_model={
        "name": "Prepared Mind Before the Pitch",
        "components": (
            "Sequoia partners do proactive landscape work — market change, problem specificity, timing — "
            "before founders arrive. Internal debates (is Airbnb more than cute?) precede term sheets. "
            "Multi-stage and multi-geo options let the firm back winners at seed or growth depending on "
            "whether category leaders already exist. Unit economics and gross margin still filter ideas; "
            "network effects often emerge after global supply-demand scale. Small team size limits "
            "coordination tax while global offices share insights."
        ),
        "application": (
            "Founders should articulate market change and problem precision, not just traction slides. "
            "Investors should separate seed optionality from growth proof — and avoid selling winners "
            "early as Sequoia did with Apple. When evaluating marketplaces, ask when cross-side network "
            "effects become defensible (Airbnb global liquidity) versus local density alone."
        ),
    },
    competitive_advantage=(
        "Sequoia's edge is the prepared-mind pipeline plus multi-decade reputation that attracts "
        "founders before competitors see deals. Proactive sector work lets partners price conviction when "
        "conventional wisdom says \"cute.\" Multi-stage funds capture seed upside and growth scale.\n\n"
        "Alfred Lin embodies operator-investor credibility — Zappos COO, Venture Frogs, boards on Airbnb "
        "and DoorDash. US early team at ~8 preserves partner time for sourcing versus internal meetings.\n\n"
        "Weaknesses: selling Apple early remains cautionary; fund size pushes consensus; prepared-mind "
        "work fails if landscapes shift faster than memos update."
    ),
    key_insights=[
        {
            "view": "Great founders rarely see the full 10-year picture at seed.",
            "question": "Did Brian Chesky know Airbnb would overtake hotels?",
            "answer": "Lin says seed-stage founders seldom articulate decade-end states; Sequoia debates whether air beds become a global category. Conviction builds through supply growth, international ground wars (Wimdu), and emerging cross-border network effects — not day-one pitch clarity.",
        },
        {
            "view": "Network effects often reveal after scale, not at investment.",
            "question": "When did Sequoia see Airbnb's global moat?",
            "answer": "Global network effects became clearer as supply and demand compounded across countries — Hamilton Helmer 7 Powers framing Acquired uses elsewhere. Early thesis centered on market change and problem; defensibility strengthened with liquidity depth over years.",
        },
        {
            "view": "Market size and gross margins still gate venture.",
            "question": "Does Don Valentine's framework hold?",
            "answer": "Lin affirms no huge businesses start in small markets and high gross marginability still matters — even with proactive sourcing. Unit economics discipline pairs with prepared-mind theses; both must pass before capital deploys at seed or growth.",
        },
        {
            "view": "Stage and geography multiply entry options.",
            "question": "Seed a new entrant or back the growth winner?",
            "answer": "Sequoia chooses per market structure: if a category winner exists with room to compound, growth checks make sense; if disruption is early, seed partnerships win. China, India, and Europe insights flow back to US partners without requiring uniform global plays.",
        },
        {
            "view": "Venture returns live in the out years.",
            "question": "Why cite Amazon's 21st-year profits?",
            "answer": "Lin uses Amazon to warn against short-term exits: area under the compounding curve concentrates late. Sequoia's Apple sale is the negative example; holding Airbnb/DoorDash through IPO week is the positive — patience and position sizing matter as much as entry price.",
        },
    ],
    top_investment_implications=[
        {
            "ticker": "SEQ",
            "direction": "Watch",
            "confidence": "Low",
            "thesis": "Not a public stock — episode frames how Sequoia's prepared-mind process and multi-stage hold discipline produce outsized private-market outcomes; relevant for LPs evaluating top-tier VC franchises.",
        },
    ],
    golden_quotes=[
        "\"We get it wrong in the beginning and in the end\" — David on venture timing, echoed in Lin's Apple sale vs. hold discussion.",
        "\"No one ever started a huge business in a small market\" — Don Valentine framework Lin reaffirms for market-size screening.",
        "\"The real returns come much, much, much later\" — Ben on compounding curves, citing Amazon's 21st-year profits versus its first 20.",
    ],
    chronology={
        "subject": "Sequoia Capital / Alfred Lin",
        "events": [
            {"date": "1972", "event": "Sequoia founded; Don Valentine era begins"},
            {"date": "1970s", "event": "Early Apple investment; later sale nets ~$6M profit"},
            {"date": "1990s–2000s", "event": "Prepared-mind and sector-proactive culture institutionalized"},
            {"date": "2009", "event": "Sequoia seeds Airbnb amid RIP Good Times memo"},
            {"date": "2010s", "event": "Alfred Lin joins; boards Airbnb, DoorDash, Instacart, others"},
            {"date": "2010s", "event": "Global expansion: China, India, Europe practices mature"},
            {"date": "2020", "event": "Airbnb and DoorDash approach IPO; Lin's first two portfolio IPOs"},
            {"date": "2021-01", "event": "Acquired records Investment Playbook special with Alfred Lin"},
            {"date": "Ongoing", "event": "US early-stage practice kept near ~8 partners"},
            {"date": "Ongoing", "event": "Multi-stage funds deploy seed through growth globally"},
        ],
    },
)

# Remaining 7 episodes written in continuation file import
from scripts._write_acq_batch_s7_8_target_bodies import EPISODES as MORE  # noqa: E402

EPISODES.update(MORE)

if __name__ == "__main__":
    results = {"completed": [], "failed": []}
    for eid, ep in EPISODES.items():
        path = APPROVED / f"{eid}.json"
        path.write_text(json.dumps(ep, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
        report = validate_summary(ep, TMPL)
        if report.passed:
            results["completed"].append(eid)
            print(f"PASS {eid} words={report.total_words}")
        else:
            results["failed"].append({"id": eid, "issues": [f"{i.section}: {i.message}" for i in report.issues]})
            print(f"FAIL {eid} words={report.total_words}")
            for issue in report.issues:
                print(f"  [{issue.severity}] {issue.section}: {issue.message}")
    print(f"\nCompleted: {len(results['completed'])} Failed: {len(results['failed'])}")
    for f in results["failed"]:
        print(f"  {f['id']}: {f['issues']}")
