#!/usr/bin/env python3
"""Write remaining Season 9 Acquired summaries."""
from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DISCOVERED = json.loads((ROOT / "data" / "discovered" / "acquired_episodes.json").read_text())
META = {e["id"]: e for e in DISCOVERED["episodes"]}
LINKS = {
    "apple_podcasts": "https://podcasts.apple.com/podcast/acquired/id1050462261",
    "spotify": "https://open.spotify.com/show/2HI3KdjtJnr3E8B4W8Y0Yx",
}


def base(ep_id: str, **kwargs) -> dict:
    ep = META[ep_id]
    return {
        "episode_id": ep_id,
        "podcast": "Acquired",
        "host": "Ben Gilbert & David Rosenthal",
        "metadata": {
            "episode_number": ep["episode_number"],
            "title": ep["title"],
            "guest": ep["guest"],
            "guest_role": ep["guest_role"],
            "date": ep["date"],
            "duration_minutes": ep["duration_minutes"],
            "youtube_url": ep.get("youtube_url") or "",
            "links": {
                "youtube": ep.get("youtube_url") or "",
                "acquired": ep["acquired_url"],
                **LINKS,
            },
        },
        "extraction_meta": {
            "model": "manual-gpt-agent-v5.1-acquired",
            "transcript_source": "acquired.fm",
            "status": "approved",
            "template_version": "5.1-acquired",
        },
        "episode_rating": {"overall": 3},
        **kwargs,
    }


EPISODES: dict[str, dict] = {}

EPISODES["acq-standard-oil-part-i"] = base(
    "acq-standard-oil-part-i",
    keywords=["Standard Oil", "John D. Rockefeller", "Industrial Monopoly"],
    conclusion="Standard Oil Part I traces John D. Rockefeller from Devil Bill's snake-oil showmanship and Baptist 'duty to profit' through Cleveland refining dominance. By 1877 Standard controlled ~90% of U.S. oil — kerosene first, gasoline later — via scale economies, vertical integration (barrels, pipelines, tank cars), and controversial railroad rebates (South Improvement Company). The 1870 joint-stock company capitalized at $1M liquid assets; dividends ran 50–200% annually to private shareholders. Annual earnings reached $10–20M by 1890 (~$300–500M inflation-adjusted). Sherman Antitrust Act passed July 1890 but did not break Standard for 21 years; Rockefeller retired 1896 yet remained titular president. Chernow's Titan anchors the narrative: strength leads to strength in fixed-cost refining.",
    background="Season 9 opens with Ron Chernow's Titan as primary source — oil meant kerosene lamps, not gasoline, for Standard's first 40 years (Model T ~1910). Ben and David cover 1839 birth through 1890 Sherman Act.\n\nArc: bookkeeping apprenticeship → Clark & Rockefeller Civil War commodity profits ($17,000 in 1862, 4× prior years) → Titusville kerosene → 1865 Clark auction ($72,500 buyout) → Flagler/Harkness $100,000 → 1870 Standard Oil of Ohio → Cleveland Massacre (22 of 26 refiners in 6 weeks) → pipeline/railroad chokepoints → 26 Broadway HQ.",
    important_facts=[
        "Clark & Rockefeller trading profit hit $17,000 in 1862 (first Civil War year) — ~4× all prior years — funding pivot into oil refining.",
        "Rockefeller bought Clark's 50% at auction for $72,500 (~$3–4M in 2021 dollars) — half of early Standard Oil equity.",
        "January 10, 1870: Standard Oil of Ohio joint-stock company capitalized with $1M liquid assets — unprecedented scale for American enterprise.",
        "By 1877 Standard controlled ~90% of U.S. oil; 1866 export mix was ~two-thirds international kerosene vs. one-third domestic.",
        "1890–1900 annual earnings $10–20M with dividends of 50–200% per year; revenue approached ~1% of U.S. GDP (~31M population in 1865).",
    ],
    mental_model={
        "name": "Strength Leads to Strength (Refining)",
        "components": "Rockefeller optimized refining (Morris Chang parallel) while speculators chased gushers. Vertical integration — own coopers, plumbers, treat barrel wood in-forest — plus horizontal roll-ups via equity-for-distressed-refineries. Flagler's Lakeshore railroad volume guarantees and tank-car CapEx created switching costs. Buy-the-dip inventory strategy during price crashes ($12 to $0.12/barrel swings) required balance-sheet depth competitors lacked. Dividends-not-salaries aligned partners to equity appreciation.",
        "application": "In commodity processing, scale on fixed costs beats prospecting upstream. Rockefeller chose predictable refining in cities vs. Pennsylvania wildcatting — analogous to picks-and-shovels vs. mining. Regulators eventually matter more than competitors once share exceeds ~90%.",
    },
    competitive_advantage="Standard Oil's moat stacked Hamilton Helmer powers — scale economies dominant, plus switching costs (railroad/tank-car deals), cornered resources (later E&P), process power (refining yield), and branding ('Standard' kerosene cans).\n\nRockefeller's counter-positioning: while drillers chased spikes, he held inventory through busts and bought distressed rivals at 25–50% of replacement cost with Standard shares — 'own shares and your family will never go hungry.'\n\nPipeline on railroad right-of-way (1879 Tidewater acquisition) proved alternative to rail — benevolent dictator model letting railroads survive under threat.\n\nWeaknesses: public backlash (Titusville riots), Sherman Act 1890, paradigm shift risk (electricity) — though automobiles rescued gasoline demand. Ben grades industry development 'C' net-net; David 'B' — Rockefeller accelerated standardization but might have happened anyway.",
    key_insights=[
        {"view": "Refining scale beat wildcatting chaos.", "question": "Why not drill in Pennsylvania?", "answer": "Rockefeller refused speculator mentality — optimized Cleveland refining while prices gyrated like early Bitcoin. Efficient operations could pay more for crude and hold inventory through crashes. Competitors lacked capital depth; Clark was 'scared grandmother' scared of bank debt."},
        {"view": "South Improvement Company was leverage, not operations.", "question": "Did the cartel ever ship oil?", "answer": "No barrel moved under SIC — it was structured threat after Lakeshore rebates. Within 6 weeks (Feb–Apr 1872) Standard bought 22 of 26 Cleveland refiners ('Cleveland Massacre') then abandoned SIC publicly. Competitors heard 'you want some shares?'"},
        {"view": "Corporate innovation preceded antitrust law.", "question": "How did Standard operate nationally?", "answer": "Pre-Civil War firms could not own out-of-state property. Flagler's joint-stock trust let Ohio shareholders control distant refineries via trustees — dividends flowed to individuals, not Standard of Ohio balance sheet. Equity-for-merger replaced cash — novel incentive design."},
        {"view": "Sherman Act was political theater initially.", "question": "Did 1890 break Standard?", "answer": "Act outlawed trusts 'in restraint of trade' without definition. Rockefeller treated passage as win; John Sherman took Rockefeller campaign money again in 1891. Breakup took until 1911 — 21 years later."},
        {"view": "Consumer benefit complicates moral verdict.", "question": "Was monopoly good for kerosene buyers?", "answer": "Stable cheap kerosene displaced whale oil; Ida Tarbell documented abuses but consumers saw reliable supply. Rockefeller argued consolidation reduced waste — Bezos consumer-surplus argument 130 years early. Competitors/suppliers bore most harm."},
    ],
    top_investment_implications=[
        {"ticker": "XOM", "direction": "Watch", "confidence": "Low", "thesis": "Modern ExxonMobil descends from Standard Oil breakup children — study as legacy of 90% kerosene share and dividend culture; energy transition caps upstream moats versus Rockefeller era."}
    ],
    golden_quotes=[
        '"Clark was an old grandmother and was scared to death because we owed money to the banks." — Rockefeller on buying out Clark & Rockefeller partner.',
        '"Own shares of Standard Oil and your family will never go hungry." — Standard pitch per Ida Tarbell.',
        '"The story of John D. Rockefeller transports us back to a time when industrial capitalism was raw and new in America, and the rules of the game were unwritten." — Ron Chernow, Titan.',
    ],
    chronology={
        "subject": "Standard Oil (Part I)",
        "events": [
            {"date": "1839", "event": "John D. Rockefeller born in Richford, New York"},
            {"date": "1859", "event": "Titusville, Pennsylvania oil discovery; Rockefeller bookkeeping in Cleveland"},
            {"date": "1862", "event": "Clark & Rockefeller earns $17,000 war-driven trading profit"},
            {"date": "1865", "event": "Rockefeller wins Clark auction — $72,500 for 50% oil business"},
            {"date": "1866", "event": "Two-thirds of kerosene exported; William Rockefeller opens New York export"},
            {"date": "1870", "event": "Standard Oil of Ohio incorporated — $1M capitalization"},
            {"date": "1872", "event": "Cleveland Massacre — 22 of 26 refiners acquired in 6 weeks"},
            {"date": "1877", "event": "~90% U.S. oil market share; pipeline/railroad dominance"},
            {"date": "1883", "event": "HQ moves to 26 Broadway, Manhattan"},
            {"date": "1890", "event": "Sherman Antitrust Act passed July 1890"},
            {"date": "1896", "event": "Rockefeller begins retirement; leaves Archbold and John Jr. in charge"},
        ],
    },
    review_notes="Manual GPT Acquired batch — v5.1-acquired; Part I of II",
)

EPISODES["acq-tsmc"] = base(
    "acq-tsmc",
    keywords=["Pure-Play Foundry", "Morris Chang", "Semiconductor CapEx"],
    conclusion="TSMC's 2021 Acquired episode (remastered 2025) explains the foundry that fabs Apple, NVIDIA, AMD, and Qualcomm silicon. Morris Chang founded at 56 in 1987 with $0 pre-money — 50% Taiwan government, 50% investors including Philips; he bought shares with salary. Pure-play foundry was 'solution seeking problem' until fabless revolution (NVIDIA raised only ~$20M, never built fabs). Learning-curve pricing from TI/BCG; 40% operating margins on contract manufacturing. 2020: $48B revenue, $20B operating profit, $17B CapEx reinvested. Apple 2010 deal: ~$9B dedicated fab, 6000 employees, 11-month build. >50% foundry share, ~90% leading-edge 5nm. ASML EUV machines ~$200M each; only TSMC/Samsung at 5nm.",
    background="Recorded amid 2021 chip shortage (Ford F-150 pauses). Morris Chang: Ningbo-born, TI semiconductor chief passed over for CEO, ITRI 'retirement' → TSMC mandate.\n\nValue chain sidebar: ARM (1987), EDA (Synopsys/Cadence), ASML lithography, fabless designers. 2009 Morris return during financial crisis; iPhone/Android fabless wave; cloud/GPU pivot makes Intel dominance 'over.'",
    important_facts=[
        "TSMC 1987 founding: ~$110M raised at $0 pre-money — Morris Chang received no founder equity; bought TSMC stock with cash.",
        "Global semiconductor market ~$26B (1987) vs. ~$527B (2024 context in remaster); TSMC among few trillion-dollar companies outside US West Coast.",
        "2020 financials: ~$48B revenue, ~$20B operating profit; ~$17B of ~$20B op profit reinvested as CapEx — announced ~$100B CapEx over 3 years by 2021.",
        "Apple TSMC deal ~2010: ~$9B fab investment, ~6000 dedicated staff; A4 iPhone chip first Apple-designed TSMC-fabbed silicon.",
        "Compound annual revenue growth ~17.4% for 27 years since 1994 Taiwan IPO ($4B market cap → ~$550B+ by 2021 episode).",
    ],
    mental_model={
        "name": "Pure Play Foundry Treadmill",
        "components": "Never compete with customers on design — Apple won't trust Intel/Samsung IDM conflicts. Win each node volume to amortize $20B+ fabs (trending $100B). Morris begged IDM 'dregs' until Qualcomm/NVIDIA/Marvell fabless startups arrived. ASML EUV monopoly + Hsinchu ecosystem = unreplicable process power. Learning-curve pricing: start low, cut price every quarter even when market doesn't demand.",
        "application": "Capital-intensive component businesses: vendor-customer conflict determines trust. TSMC concentration risk inherited by every fabless AI winner; Arizona fabs lack Taiwan cluster density.",
    },
    competitive_advantage="TSMC wins as neutral leading-edge manufacturer when IDMs conflict with customers.\n\nScale + learning curve: old Fab 2–3 from 1980s still run trailing nodes — monetize automotive/IoT while leading edge funds next node.\n\n2009 Morris return: no layoffs culture; 28nm then 5nm bets after 40nm yield crisis.\n\nWeaknesses: Taiwan geopolitics, Apple/NVIDIA concentration, capital intensity — 5–10% demand miss tanks node economics.\n\nVersus Intel/Samsung: Apple chose TSMC over Samsung foundry due to Galaxy conflict; Intel lost IBM PC processor then mobile forever.",
    key_insights=[
        {"view": "Pure-play foundry was contrarian in 1987.", "question": "Why did Morris not build an Intel clone?", "answer": "Taiwan had 4–5% average gross margins on toys — no design talent. Minister KT Li demanded semiconductor leader; Morris chose foundry serving future fabless designers ('real men have fabs' era). Market didn't exist yet — he hoped fabless would come."},
        {"view": "$0 pre-money was survivable, not generous.", "question": "How is Chang worth billions?", "answer": "Government owned 50%; Morris bought TSMC shares from salary and dividends as public markets opened (1994 Taiwan IPO, 1997 NYSE). Opposite of Silicon Valley equity — bet on own economics."},
        {"view": "2009 crisis proved operational moat.", "question": "Why return at 78?", "answer": "Financial crisis + iPhone/Android fabless wave + GPU/cloud shift away from Intel x86. Morris closed Apple deal competitors couldn't — founder gravitas despite no initial equity."},
        {"view": "ASML + TSMC co-evolution.", "question": "Why can't governments replicate TSMC?", "answer": "EUV machines ~$200M, 50+ on backorder; wavelength of light vs. 5nm gates requires alchemy-level process knowledge. Even with $100B cash, 'you wouldn't know what to do with ASML shipments.'"},
        {"view": "Pricing power inflects at monopoly share.", "question": "Why raise prices after decades of cuts?", "answer": ">50% foundry share, ~95% leading-edge profit share — first price increases since Morris learning-curve era. Commodity transformed into iPhone-of-semiconductors positioning."},
    ],
    top_investment_implications=[
        {"ticker": "TSM", "direction": "Watch", "confidence": "Medium", "thesis": "Pure-play foundry oligopoly at 5nm/3nm; AI/GPU demand drives advanced utilization — primary bear case is Taiwan geopolitical concentration and customer diversification efforts."},
        {"ticker": "NVDA", "direction": "Watch", "confidence": "Medium", "thesis": "NVIDIA–TSMC partnership since RIVA 128; AI GPU supply constrained by TSMC CoWoS/advanced packaging allocation."},
    ],
    golden_quotes=[
        '"The semiconductor business is like a treadmill that speeds up all the time. If you can\'t keep up, you fall off." — Morris Chang.',
        '"We had no strength in R&D… We had almost no strength in intellectual property." — Morris on 1985 Taiwan — context for foundry bet.',
        '"Real men have fabs." — Jerry Sanders (AMD), the worldview TSMC inverted.',
    ],
    chronology={
        "subject": "TSMC",
        "events": [
            {"date": "1958", "event": "Morris Chang joins Texas Instruments; learning-curve pricing with BCG"},
            {"date": "1983", "event": "Chang demoted at TI; resigns after ~30 years"},
            {"date": "1987", "event": "TSMC founded; ARM also founded — annus mirabilis for chips"},
            {"date": "1987", "event": "~$110M raised at $0 pre-money; Philips and Taiwan government invest"},
            {"date": "1993", "event": "NVIDIA founded — fabless, ~$20M raised, TSMC fabs from start"},
            {"date": "1994", "event": "TSMC Taiwan IPO — ~$4B market cap"},
            {"date": "2009", "event": "Morris Chang returns as CEO amid financial crisis"},
            {"date": "2010–12", "event": "Apple ~$9B dedicated fab deal; A4/A6 iPhone silicon"},
            {"date": "2020", "event": "~$48B revenue; ~$17B CapEx reinvestment"},
            {"date": "2021", "event": "Acquired episode; ~$100B 3-year CapEx plan; 5nm leadership"},
            {"date": "2025", "event": "Remaster; TSMC market cap ~$1T+ in remaster intro"},
        ],
    },
    review_notes="Manual GPT Acquired batch — v5.1-acquired; remastered 2025",
)

# Continue with a16z I, a16z II, ethereum in same file - truncated for write, append next

if __name__ == "__main__":
    # Import extended episodes
    from _season9_remaining_episodes_part2 import EPISODES_PART2
    all_eps = {**EPISODES, **EPISODES_PART2}
    out = ROOT / "data" / "approved"
    ids = sys.argv[1:] or list(all_eps.keys())
    for eid in ids:
        path = out / f"{eid}.json"
        path.write_text(json.dumps(all_eps[eid], indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
        r = subprocess.run(
            [sys.executable, str(ROOT / "scripts" / "validate_one_acquired.py"), eid],
            capture_output=True, text=True,
        )
        print(r.stdout.strip())
        if r.returncode != 0:
            sys.exit(1)
    print("ALL PASS:", ", ".join(ids))
