#!/usr/bin/env python3
"""Write and validate 8 Acquired v5.1 approved JSON files (user batch)."""

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
NOTES = "Manual GPT Acquired batch v5.1 — user request 8 episodes"

EPISODES: dict[str, dict] = {}

EPISODES["acq-special-an-acquirers-view-into-ma-with-taylor-barada-head-of-corp-dev-at-adobe"] = base(
    "acq-special-an-acquirers-view-into-ma-with-taylor-barada-head-of-corp-dev-at-adobe",
    review_notes=NOTES,
    episode_rating={"overall": 4},
    keywords=["Corporate Development", "M&A Process", "Culture Fit"],
    conclusion=(
        "Taylor Barada opens Adobe's corp-dev playbook: most deals start as relationship-driven "
        "coffee chats, not auction processes — mirroring venture's \"always be raising\" and Mark "
        "Suster's invest-in-lines-not-dots. Adobe walks away from billion-dollar targets when culture "
        "misaligns; sub-10% of tracked opportunities close despite ~1,000 inbound pitches per year. "
        "LOIs carry 45–60-day no-shops, multi-day diligence, and integration owned inside corp dev so "
        "deals are growth bets, not press-release wins. Founders should partner with business owners "
        "and corp dev equally, avoid CEO partner-shopping, and treat closing day as day one — the "
        "episode's meta-lesson for anyone selling into strategic acquirers."
    ),
    background=(
        "Ben and David host Taylor Barada, Adobe VP of Corp Dev, Corp Strategy & Strategic Partnerships "
        "(joined 2013; prior Yahoo corp dev and Zynga VP Business; Bain JD-MBA; former pro soccer in "
        "England). Instead of grading one acquisition, they walk through how strategic M&A actually "
        "works inside a 15,000-person repeat buyer.\n\n"
        "Taylor compares corp dev to VC sourcing: warm intros, long courtships, and occasional "
        "competitive processes when another bidder forces a sale. Culture fit is non-negotiable — "
        "Adobe passed on nine-figure deals where founders would not embrace Adobe's broader vision. "
        "He details LOI mechanics, data-room diligence, business-owner vs. corp-dev roles, and "
        "post-close integration reporting to the board for two years. Contrasts Yahoo's slower "
        "bureaucracy, Zynga's two-hour fly-to-close speed, and Adobe's strategy-led Omniture-style "
        "adjacency bets using Bain's Profit-from-the-Core framework."
    ),
    important_facts=[
        "Taylor Barada leads Adobe corp dev after Yahoo and Zynga; Adobe employs roughly 15,000 people and completes about 4–10 acquisitions per year.",
        "Adobe has walked away from deals north of $1 billion when culture fit failed — culture is treated as a fourth pillar beside strategy, product, and financials.",
        "Taylor estimates fewer than 10% of seriously tracked M&A conversations close; Adobe receives roughly 2–5 inbound acquisition pitches per day (~1,000/year).",
        "Term sheets/LOIs at large strategics almost always include 45–60-day no-shop provisions, paralleling venture financing market terms.",
        "Adobe's M&A integration team sits inside corp dev; quarterly post-close reports to CEO, CFO, and board continue for two years on financial, product, and retention metrics.",
    ],
    mental_model={
        "name": "Lines Not Dots (Strategic M&A)",
        "components": (
            "Most acquirer-startup relationships begin as open-ended introductions in a small Valley "
            "network — not \"we're for sale\" calls. Credibility accrues when founders execute what they "
            "said over multiple touchpoints (Suster's lines). Competitive auctions are the ~20% case. "
            "Culture fit predicts post-close execution: founders must want to expand the acquirer's "
            "vision, not just cash out. Corp dev is a collaborative guide; business owners and corp dev "
            "both matter; premature CEO access can kill deals. Integration begins at term sheet — "
            "retention packages and org design are negotiated with post-close roles in mind."
        ),
        "application": (
            "Founders: take corp-dev meetings before you need a exit; diligence the buyer's culture. "
            "Never partner-shop to a second exec without context. Acquirers: keep integration inside "
            "deal teams to avoid \"throw over the wall\" behavior. Use adjacency discipline (Profit "
            "from the Core) so multi-step bets like Omniture are conscious, not random diversification."
        ),
    },
    competitive_advantage=(
        "Adobe's corp-dev edge is CEO Shantanu Narayen's founder-level passion (19 years at Adobe, "
        "9 as CEO) setting a high strategic bar — saying no preserves deal quality bankers notice. "
        "Repeat-player process (lawyers, templates, integration cadence) speeds diligence without "
        "sacrificing culture screens. Taylor's cross-company pattern recognition (Yahoo, Zynga, Adobe) "
        "and Bain adjacency framing help match deal type to corporate strategy — core tuck-ins vs. "
        "Omniture-scale pivots.\n\n"
        "Relationship sourcing beats auction fees for proprietary flow; entrepreneurs trust Adobe as "
        "steward when creative-to-marketing expansion stories resonate (Omniture, mobile tailwind "
        "theses). Integration-in-house aligns retention and product roadmaps early.\n\n"
        "Weaknesses: high no-rate can slow category moves; 15,000-person complexity still overwhelms "
        "founders; partnerships often disappoint startups expecting distribution miracles. Sub-10% close "
        "rate means corp dev bandwidth spent mostly on passes — cost of discipline."
    ),
    key_insights=[
        {
            "view": "Strategic M&A mirrors venture fundraising.",
            "question": "How do Adobe deals usually start?",
            "answer": "Warm intros and long relationships — \"not looking to sell, let's grab coffee.\" Auctions happen when another bidder forces the issue (~20%). Taylor explicitly parallels always-be-raising VC culture and Suster's lines-not-dots.",
        },
        {
            "view": "Culture fit is a financial variable, not HR fluff.",
            "question": "Why walk away from billion-dollar deals?",
            "answer": "Post-close value is execution on combined vision. Without aligned founders who embrace Adobe's roadmap, cash-flow forecasts fail. Taylor cites Yahoo Citizen Sports and IntoNow founders rising to SVP as positive counterexamples.",
        },
        {
            "view": "LOI/no-shop is the venture term sheet of M&A.",
            "question": "What changes after a term sheet?",
            "answer": "Knowledge circle expands; 1–3 day deep dives; data rooms; lawyers define market terms. No-shops typically 45–60 days. Early-stage legal messes (unsigned contractor agreements) still appear but rarely kill deals.",
        },
        {
            "view": "Partner-shopping kills deals faster than bad terms.",
            "question": "Should founders go straight to the CEO?",
            "answer": "Taylor and hosts compare to VC partner-shopping — second meetings without context destroy trust. Business owners and corp dev should frame the story before executive sponsors engage.",
        },
        {
            "view": "Integration ownership separates growth M&A from financial engineering.",
            "question": "How does Adobe measure success post-close?",
            "answer": "Corp dev owns integration; quarterly board reports for two years on financial, product, and retention KPIs. Taylor frames hit rate like baseball (~30%) not free throws — Adobe beats industry averages by pre-deal culture and strategy discipline.",
        },
    ],
    top_investment_implications=[
        {
            "ticker": "ADBE",
            "direction": "Watch",
            "confidence": "Medium",
            "thesis": "Episode reveals Adobe's selective, culture-first M&A machine supporting creative-cloud and marketing-cloud expansion — relevant when evaluating whether Experience Cloud M&A (Figma blocked, etc.) remains disciplined vs. desperate.",
        },
    ],
    golden_quotes=[
        "\"When you want money, ask for advice; when you want advice, ask for money\" — Taylor on why founders should meet acquirers before a sale process.",
        "\"We don't care about winning the press release\" — Taylor on value creation vs. announcement optics.",
        "\"It's not about the deal… it's a tool\" — Taylor on M&A serving strategy, not deal-making for its own sake.",
    ],
    chronology={
        "subject": "Taylor Barada & Adobe Corp Dev",
        "events": [
            {"date": "Pre-2008", "event": "Taylor plays professional soccer in England; Bain JD-MBA"},
            {"date": "2008–2009", "event": "Taylor joins Yahoo corp dev during restructuring era"},
            {"date": "2010s", "event": "Taylor leads corp dev at Zynga during hyper-growth social gaming M&A"},
            {"date": "2013", "event": "Taylor joins Adobe as VP Corp Dev, Strategy & Partnerships"},
            {"date": "2009", "event": "Adobe acquires Omniture — major marketing-cloud adjacency bet"},
            {"date": "Ongoing", "event": "Adobe completes ~4–10 deals/year; integration reports for 2 years post-close"},
            {"date": "2016-08-22", "event": "Acquired records special interview on M&A process with Taylor Barada"},
            {"date": "2016", "event": "Instagram Stories launches — hosts discuss as follow-up to prior Facebook/Snap episodes"},
            {"date": "Ongoing", "event": "Taylor cites Mark Suster lines-not-dots and Profit from the Core adjacency framework"},
            {"date": "Ongoing", "event": "Adobe walks away from $1B+ deals lacking culture fit"},
        ],
    },
)

EPISODES["acq-season-5-episode-10-the-lean-startup-and-the-long-term-stock-exchange-with-eric-ries"] = base(
    "acq-season-5-episode-10-the-lean-startup-and-the-long-term-stock-exchange-with-eric-ries",
    review_notes=NOTES,
    episode_rating={"overall": 4},
    keywords=["Lean Startup", "LTSE", "Public Markets"],
    conclusion=(
        "Eric Ries closes Acquired Season 5 by connecting The Lean Startup's build-measure-learn loop to "
        "the Long-Term Stock Exchange — an SEC-approved national exchange raising ~$68M to align "
        "public-company governance with long-horizon founders and investors. Nine years after IMVU and "
        "the 2011 book canonized MVP, pivot, and product-market fit, Ries argues today's private-market "
        "excess (mega-rounds, stay-private-longer, dual-class hegemony) needs institutional fixes, not "
        "just startup methodology. LTSE listing standards, voter disclosure, and long-term stakeholder "
        "commitments extend lean principles to capital markets — ambitious, polarizing, and exactly the "
        "kind of infrastructure play Acquired tracks when software eats finance."
    ),
    background=(
        "Recorded December 29, 2019, Ben and David host Eric Ries — IMVU co-founder, There.com alum, "
        "author of The Lean Startup (2011), and CEO of LTSE. The conversation spans Eric's Yale-to-"
        "startup path, the failure modes of pre-lean venture (large bets on unvalidated plans), and how "
        "minimum viable products and validated learning emerged from post-bubble experimentation.\n\n"
        "Ries then pivots to LTSE: conceived mid-flight between lean workshops as a \"new social "
        "contract\" between long-term companies and shareholders. SEC approval as the fifth U.S. national "
        "securities exchange makes the idea real. They debate whether LTSE can counter quarterly "
        "myopia, dual-class voting abuses, and IPO mis-incentives without becoming another niche venue — "
        "and how Eric's free software tools for startups parallel exchange infrastructure building."
    ),
    important_facts=[
        "Eric Ries published The Lean Startup in 2011; concepts like MVP, pivot, and product-market fit became canonical startup vocabulary.",
        "LTSE was approved by the SEC as the fifth national securities exchange in the U.S., aiming to reduce short-termism in public markets.",
        "LTSE raised approximately $68 million from top-tier venture investors to build exchange infrastructure and listing standards.",
        "Eric Ries co-founded IMVU after working at There.com — early experiences with large upfront investment and market misses informed lean methodology.",
        "Acquired recorded this episode December 29, 2019 as the Season 5 finale, linking startup building and exit mechanics.",
    ],
    mental_model={
        "name": "Build-Measure-Learn at Market Scale",
        "components": (
            "Lean Startup: hypotheses → MVP → validated learning → pivot or persevere. Waste is building "
            "features nobody wants. LTSE applies the same experimental mindset to public markets: if "
            "quarterly earnings myopia and misaligned shareholder incentives destroy long-term value, "
            "design an institution (a stock exchange) that binds companies and investors to multi-year "
            "commitments — listing standards as MVP, regulatory approval as scale milestone."
        ),
        "application": (
            "Founders should treat capital strategy as experimentation, not a one-shot IPO event. "
            "Investors evaluating LTSE-listed or long-term-governed companies should ask whether "
            "disclosure and voting rules actually change behavior or are marketing. Incumbents (NYSE, "
            "Nasdaq) may copy features — LTSE must win critical mass of quality issuers."
        ),
    },
    competitive_advantage=(
        "Eric Ries brings unmatched brand authority from The Lean Startup — LTSE recruits founders and "
        "VCs who already treat his frameworks as gospel. Regulatory approval as a national exchange is a "
        "formidable moat versus prior \"long-term\" governance startups lacking exchange status. LTSE's "
        "software tools for startups (cap-table, planning) create a funnel of companies familiar with "
        "the brand before IPO consideration.\n\n"
        "First-mover narrative on stakeholder capitalism and anti-short-termism aligns with 2019–2020 "
        "ESG and dual-class backlash discourse. $68M capitalization funds multi-year SEC and technology "
        "work incumbents could replicate but rarely prioritize.\n\n"
        "Weaknesses: chicken-and-egg liquidity — issuers need investors, investors need volume. "
        "Incumbent exchanges and direct listings may absorb LTSE's best ideas. Eric's polarizing "
        "public persona invites skepticism from traditional finance. Many LTSE principles may work "
        "better as contractual governance than as a separate exchange."
    ),
    key_insights=[
        {
            "view": "LTSE is lean methodology applied to Wall Street.",
            "question": "Why a stock exchange?",
            "answer": "Ries realized only a regulated institution can simultaneously bind issuers and investors to long-term rules — a term sheet between one company and its holders cannot replicate exchange-level standards.",
        },
        {
            "view": "Private-market excess mirrors pre-lean venture mistakes.",
            "question": "What problem does LTSE target?",
            "answer": "Mega-rounds, delayed IPOs, and dual-class structures let founders optimize liquidity without market discipline — echoing There.com-style big bets without validated learning.",
        },
        {
            "view": "Polarization signals importance.",
            "question": "Is LTSE realistic?",
            "answer": "Hosts note new ideas in finance attract fierce debate — same as lean startup in 2011. SEC approval validates seriousness even if adoption remains uncertain.",
        },
        {
            "view": "Software tools precede exchange network effects.",
            "question": "How does LTSE acquire companies?",
            "answer": "Eric returned to building free/cheap startup infrastructure tools while compliance teams pursued exchange approval — classic parallel build-measure-learn tracks.",
        },
        {
            "view": "Exits are part of the startup stack.",
            "question": "Why end Season 5 here?",
            "answer": "Acquired frames company building through acquisition and IPO; LTSE tries to fix the IPO layer itself — meta-capstone for a season on liquidity and governance.",
        },
    ],
    top_investment_implications=[
        {
            "ticker": "LTSE",
            "direction": "Watch",
            "confidence": "Low",
            "thesis": "Private exchange/governance platform — episode outlines thesis that long-term listing standards could attract founder-friendly IPOs if liquidity develops; no public ticker yet.",
        },
    ],
    golden_quotes=[
        "\"Wouldn't it be great if long-term oriented companies and long-term oriented investors could get together?\" — Eric Ries on LTSE's origin mid-flight.",
        "\"Build, measure, learn\" — hosts tie Eric's loop to both IMVU history and LTSE infrastructure rollout.",
        "\"Can LTSE help address endemic problems — excessive capital raising, stay-private-longer, dual-class founder hegemony?\" — Acquired show-note framing question.",
    ],
    chronology={
        "subject": "Eric Ries, Lean Startup & LTSE",
        "events": [
            {"date": "1990s–2000s", "event": "Eric Ries at Yale; joins There.com startup (high burn, market miss)"},
            {"date": "2004", "event": "Eric co-founds IMVU; develops early lean experimentation practices"},
            {"date": "2011", "event": "The Lean Startup published; MVP and pivot enter mainstream"},
            {"date": "2010s", "event": "Private markets swell — mega-rounds, delayed IPOs, dual-class shares proliferate"},
            {"date": "Mid-2010s", "event": "Eric conceives LTSE during lean workshops; begins regulatory path"},
            {"date": "2019", "event": "LTSE gains SEC approval as fifth U.S. national securities exchange"},
            {"date": "2019", "event": "LTSE raises ~$68M from venture investors"},
            {"date": "2019-12-29", "event": "Acquired Season 5 finale records with Eric Ries"},
            {"date": "Ongoing", "event": "LTSE builds listing standards and startup software tools in parallel"},
            {"date": "Ongoing", "event": "Lean Startup methodology taught globally in entrepreneurship programs"},
        ],
    },
)

# Continue in part 2 — imported below
from scripts._write_acq_batch_user_8_bodies import EPISODES as MORE  # noqa: E402

EPISODES.update(MORE)

for eid, patch in {
    "acq-special-an-acquirers-view-into-ma-with-taylor-barada-head-of-corp-dev-at-adobe": {
        "title": "Special: An Acquirer's View into M&A with Taylor Barada (Adobe Corp Dev)",
        "guest": "Taylor Barada",
        "guest_role": "Head of Corp Dev, Adobe",
        "date": "2016-08-22",
        "duration_minutes": 75,
    },
    "acq-season-5-episode-10-the-lean-startup-and-the-long-term-stock-exchange-with-eric-ries": {
        "title": "The Lean Startup and the Long-Term Stock Exchange (with Eric Ries)",
        "guest": "Eric Ries",
        "guest_role": "Season 5 · Episode 10",
        "date": "2019-12-29",
        "duration_minutes": 86,
    },
}.items():
    EPISODES[eid]["metadata"].update(patch)

# v5.1 word-count expansions (background + competitive_advantage)
_EXPANSIONS: dict[str, tuple[str, str]] = {
    "acq-special-an-acquirers-view-into-ma-with-taylor-barada-head-of-corp-dev-at-adobe": (
        "\n\nTaylor contrasts three corp-dev cultures in detail: Yahoo (2008–09) needed top-down "
        "executive-sponsor alignment during restructuring; transparency about internal hoops mattered "
        "because outsiders perceived slowness as bureaucracy. Zynga under Mark Pincus could fly to a "
        "meeting within two hours when talent was spotted — aggressive category expansion in social "
        "gaming. Adobe under Shantanu emphasizes strategy arcs: mobile as tailwind, B2B network effects "
        "via data/content assets, and Omniture as a conscious four-step adjacency (SaaS, enterprise "
        "sales, recurring revenue, new product) that became a $2B+ marketing cloud. He cites Bain "
        "Profit-from-the-Core stats: ~30–40% success one step from core, ~10% at three–four steps.",
        "\n\nOn integration, Taylor's team negotiates retention packages collaboratively — sometimes "
        "rewarding operational lieutenants more at close if their importance rises post-acquisition. "
        "Quarterly board reports for two years force honesty (not all-green scorecards). Yahoo deals "
        "like Citizen Sports (Mike Kerns) and IntoNow (Adam Cahan) show founders rising to SVP when "
        "they embrace parent vision; misaligned sales destroy founder morale. Carve-outs close on "
        "Carol Dweck's Mindset, Phil Knight's Shoe Dog, and Adam Grant's Originals — fitting for a "
        "conversation about growth versus fixed mindsets in M&A and entrepreneurship."
    ),
    "acq-season-5-episode-10-the-lean-startup-and-the-long-term-stock-exchange-with-eric-ries": (
        "\n\nEric recounts IMVU after There.com — large upfront capital without validated learning. "
        "Lean Startup codified MVP, pivot, build-measure-learn for post-2008 founders. LTSE listing "
        "standards target long-term stakeholder governance, voter transparency, and reducing quarterly "
        "short-termism that dual-class IPOs amplified in the 2010s private-market bubble. Hosts link "
        "2019 themes: WeWork cautionary tale, direct listings, and stay-private-longer mega-rounds.",
        "\n\nLTSE competes with NYSE/Nasdaq copying governance features — Eric's moat is brand with "
        "founders already practicing lean tools. SEC approval took years; parallel free startup software "
        "builds pipeline. Weakness: liquidity network effects favor incumbents; LTSE may remain niche "
        "unless tier-one issuers list. Polarization (per Deciphr/show notes) signals idea importance — "
        "same as lean in 2011. $68M venture raise funds exchange ops, not just advocacy."
    ),
}

for eid, (bg, adv) in _EXPANSIONS.items():
    if eid in EPISODES:
        EPISODES[eid]["background"] += bg
        EPISODES[eid]["competitive_advantage"] += adv

from scripts._write_acq_batch_user_8_expansions import apply_expansions  # noqa: E402

apply_expansions(EPISODES)

if __name__ == "__main__":
    results: dict[str, list] = {"completed": [], "failed": []}
    for eid, ep in EPISODES.items():
        path = APPROVED / f"{eid}.json"
        path.write_text(json.dumps(ep, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
        report = validate_summary(ep, TMPL)
        if report.passed:
            results["completed"].append(eid)
            print(f"PASS {eid} words={report.total_words}")
        else:
            results["failed"].append(
                {"id": eid, "issues": [f"{i.section}: {i.message}" for i in report.issues]}
            )
            print(f"FAIL {eid} words={report.total_words}")
            for issue in report.issues:
                print(f"  [{issue.severity}] {issue.section}: {issue.message}")
    print(f"\nCompleted: {len(results['completed'])} Failed: {len(results['failed'])}")
    for f in results["failed"]:
        print(f"  {f['id']}: {f['issues']}")
