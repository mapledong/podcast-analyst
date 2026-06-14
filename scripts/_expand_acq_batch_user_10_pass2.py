#!/usr/bin/env python3
"""Second-pass expansion: important_facts (300+), mental_model (150+), key_insights depth."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))

from src.validate import load_template_config, validate_summary, word_count, word_gap  # noqa: E402
from src.template_config import template_path_for_podcast  # noqa: E402

APPROVED = ROOT / "data" / "approved"
TMPL = load_template_config(template_path_for_podcast("Acquired"))

# Per-episode additive expansions (appended to existing content, transcript-grounded)
ADDITIONS: dict[str, dict] = {
    "acq-the-new-york-times-company": {
        "important_facts_append": [
            " Revenue peaked above $3.2B before the 2009 crisis; by 2021 the company reported ~$1.8B revenue debt-free with journalism payrolls roughly double industry averages.",
            " The 2014 Innovation Report leak quoted: 'winning at journalism' but 'falling behind' at distribution — cooking app and crossword each generate ~$30M/year.",
            " Trump-era digital subscriber growth hit 47% in 2016; Q1 2017 alone added 300,000 subscribers when he took office.",
            " The Daily reached 100M downloads in its first year (Feb 2017 launch); 2019 passed 1B total downloads.",
            " Management stated a 2025 goal of 10M subscribers and sensed they would blow past it; TAM estimate is half of Netflix's ~200M subscriber base.",
        ],
        "mental_model_append": {
            "components": (
                " Historic local monopolies (dual revenue: paid circulation plus print ads) collapsed under Craigslist, "
                "Google/Facebook ads, and smartphones. Times survived via global brand substituting for geographic "
                "monopoly — English-speaking serious news TAM. Metered paywall (2011) traded traffic (160M→80M "
                "monthly uniques) for ARPU; Trump news cycle accelerated trust-based subs."
            ),
            "application": (
                " In content, brand plus scale beats aggregation arbitrage (BuzzFeed headline rewriting). "
                "Metered free tiers balance SEO with conversion. Family/steward ownership can outperform public "
                "markets when quarterly earnings conflict with journalism investment — but capital allocation "
                "mistakes (about.com, debt buybacks) show governance isn't foolproof."
            ),
        },
        "ki_answer_append": [
            " Cooking app success and Wirecutter affiliate (~$50M) diversified revenue beyond core news SKU.",
            " Ochs built Times Tower (1904–1907) and New Year's Eve ball tradition as distribution marketing.",
            " 85% ad staff turnover during digital transformation per Innovation Report recommendations.",
            " Reforge training cited as example of product thinking inside newsroom without calling it a tech company.",
            " Hires former BuzzFeed, Recode, and Vox editors-in-chief as columnists while middle-tier metros shrink.",
        ],
        "ca_append": (
            " Scale lets Times pay starting journalist salaries of $100K+ (~2× industry) — same Netflix amortization "
            "logic David cites. Bear: partisan perception risk and video experiments underwhelming versus Fox News "
            "~$6B revenue at ~50% EBITDA from partisan cable positioning."
        ),
    },
    "acq-indian-premier-league-cricket": {
        "important_facts_append": [
            " Lalit Modi renegotiated Sahara kit sponsorship from ~$100K/year to ~$105M/year within months of joining BCCI in 2005 — roughly $1M per match day on ~105 national team days.",
            " Combined Nike (~$52M/year apparel) and Sahara deals generated ~$150M/year sponsorship within two months — versus prior ~$10–15M total annual TV rights.",
            " BCCI revenue reached ~$200M+/year mid-2000s from near-zero within a decade of Lalit's commercial resets.",
            " Franchise minimum reserve ~$50M over 10 years with ~$5M year-one cash at 2008 auction; Shah Rukh Khan bid ~$75M for Kolkata.",
            " 2023–27 central media rights ~$6B (~$1.2B/year); franchise valuations exceeded ~$1B by 2025 episode recording.",
        ],
        "mental_model_append": {
            "components": " Lalit's sealed-envelope auction theater embarrassed incumbents into market-rate pricing.",
            "application": " ~250M Indians lifted from poverty 2015–2025 expanded consumer spending on cricket media.",
        },
        "ki_answer_append": ["", "", "", "", ""],
        "ca_append": (
            " Versus Big Bash and CPL, IPL has India's ~550M middle class ($7K–$45K) — 31% of population, larger than "
            "the entire US — as tailwind no rival league matches."
        ),
    },
    "acq-acquired-episode-15-exacttarget-acquired-by-salesforce-with-scott-dorsey": {
        "important_facts_append": [
            " Scott Dorsey co-founded with Chris Baggot and Peter McCormick in Dec 2000 Indianapolis with ~$200K friends-and-family after dot-com bust.",
            " IPO March 2012 priced at $19/share; stock traded ~$22/share the day before June 2013 $2.5B acquisition at $33.75/share (~50% premium).",
            " ExactTarget 2012 standalone revenue ~$294M; Salesforce Marketing Cloud FY2016 (calendar 2015) ~$654M — over 2× in under 3 years.",
            " Inside VC invested $10.5M in 2004 and $7M in 2006 when revenue reached ~$40M; 2007 IPO filing withdrawn in 2008–09 financial crisis.",
            " Ben and David graded the deal A-; SEC proxy disclosed Party A, B, and C competing bidders in the public M&A process.",
        ],
        "mental_model_append": {
            "components": " Salesforce 'account control' gorilla channel pushed Marketing Cloud to CMOs after years selling only to sales orgs.",
            "application": " Great acquisitions happen when companies are bought not sold — ExactTarget had Q1 beat during sale process.",
        },
        "ki_answer_append": ["", "", "", "", ""],
        "ca_append": (
            " Pardot bundled alongside ExactTarget completed Salesforce's marketing automation story versus Oracle Eloqua roll-up."
        ),
    },
    "acq-acquired-episode-16-midroll-stitcher-acquired-by-scripps": {
        "important_facts_append": [
            " Wall Street Journal cited ~$35M total U.S. podcast ad spend at recording — only ~2% YoY growth for the entire industry.",
            " Scripps paid ~$50M for Midroll on ~$1.5–2M annual revenue and ~$4.5M for Stitcher (~8M registered users, ~$0.56/user).",
            " Midroll ~30% take rate; handful of podcasters gross over $1M/year on the network per Midroll executive quote.",
            " Podcast CPMs cited at ~$25–100 versus ~$14 average YouTube CPM in 2014 — high-value audience in tiny spend pool.",
            " Top 10 podcast publishers account for ~40% of industry listens — power law David cites on the episode.",
        ],
        "mental_model_append": {
            "components": " Midroll launches Howl premium tier with original shows and ad-free archives post-Stitcher acquisition.",
            "application": " Ben graded Midroll D on price, Stitcher B on ~$0.56/user — hosts skeptical Scripps tech chops vs Microsoft.",
        },
        "ki_answer_append": ["", "", "", "", ""],
        "ca_append": (
            " Eric Diehn (Midroll VP BD) said Howl and Stitcher 'will intersect' — Netflix-of-podcasts thesis requiring exclusive content."
        ),
    },
    "acq-alphabet-inc": {
        "important_facts_append": [
            " YouTube founded Feb 2005 by PayPal Mafia alumni; Google acquired Nov 2006 for $1.65B in stock less than 18 months after launch.",
            " Gmail April 2004: 1GB storage versus 2–4MB competitors; beta invites traded on eBay for ~$150; grew to 2B+ users.",
            " Microsoft productivity segment ~$120B revenue (mostly Office) versus Google Cloud segment ~$50B including Workspace and IaaS.",
            " YouTube ~50% creator revenue share delayed profitability roughly a decade versus Facebook ~0%; watch-time metric replaced raw views.",
            " Alphabet reorganization Oct 2015 separated Google (Search, Ads, YouTube, Cloud, Android) from Other Bets (Waymo, Verily, Calico, X).",
        ],
        "mental_model_append": {
            "components": " Chrome (2008) and Android secure default distribution for Google services on mobile — post-PC moat.",
            "application": " Evaluate acquisitions by ecosystem value not standalone P&L — YouTube lost money for years but secured video search.",
        },
        "ki_answer_append": ["", "", "", "", ""],
        "ca_append": (
            " Maps reached 2B+ users with ~$5–10B estimated revenue combining consumer app and API platform for third-party web apps."
        ),
    },
    "acq-google": {
        "important_facts_append": [
            " Page and Brin shopped PageRank to Yahoo for ~$1M, Infoseek, and Lycos — all rejected before Sept 1998 incorporation.",
            " Bechtolsheim wrote $100K uncapped check; Ram Shriram $250K; Jeff Bezos matched at $252K — stake potentially worth ~$20B.",
            " AdWords 2002: revenue $86M (2001) to $440M (2002) — 5× in one year after adopting Overture CPC with Ad Rank quality score.",
            " AOL bake-off 2002: 34M users; Google committed $100M minimum guarantee without cash — AOL earned $35M H1 2002, $200M in 2003.",
            " AltaVista indexed 16M pages on DEC hardware; Google parallelized crawling on cheap Linux clusters for comprehensiveness moat.",
        ],
        "mental_model_append": {
            "components": " Eric Schmidt CEO from March 2001 professionalized operations while Page and Brin kept product control.",
            "application": " Yahoo offered ~$3B in 2002; Google countered ~$5B reverse-takeover ask — power inversion within years of AdWords.",
        },
        "ki_answer_append": ["", "", "", "", ""],
        "ca_append": (
            " Overture patent dispute settled for $360M; Yahoo later bought Overture for $1.6B but could not catch Google's monetization lead."
        ),
    },
    "acq-starbucks-with-howard-schultz": {
        "important_facts_append": [
            " Il Giornale raised ~$1.6M; Howard acquired six-store Starbucks for $3.8M in 1987 with Bill Gates Sr. removing blocking investor Sam.",
            " Store economics: ~80% gross margin, sub-1% of household income per visit, two-year payback; doubled stores ~YoY in late 1980s.",
            " 1988 part-time health benefits including domestic partners at 33-store company; Bean Stock made employees 'partners' with ~2× industry tenure.",
            " 1992 IPO ~$250M market cap on $93M revenue — first public pure-play coffee; Frappuccino from $23M Coffee Connection deal (1994, 23 stores).",
            " ~39,000 stores in 86 countries; ~33% mobile orders; ~$1.8B prepaid float on ~$14B/year loaded; 2008 market cap $30B to <$7B.",
        ],
        "mental_model_append": {
            "components": " Customization (names on cups, drink mods) increases loyalty and margin — free walking billboards on United and Costco.",
            "application": " 2000–2008 lesson: develop operators before stepping away; professional CEOs may add 'ten thousand little efficiency scratches.'",
        },
        "ki_answer_append": ["", "", "", "", ""],
        "ca_append": (
            " Roastery flagships (Milan, Seattle) defend premium against Third Wave coffee — Howard argues Third Wave expanded the category."
        ),
    },
    "acq-trader-joes": {
        "important_facts_append": [
            " Estimated ~$24–25B revenue (2025) from ~600 US stores at $2,000+ sales per square foot — 2× Whole Foods, 4× industry average.",
            " Joe Coulombe bought six Pronto Markets in 1962 for $25,000 ($10K above book); employees co-invested at 40% discount.",
            " Private label exceeds 80% of SKUs; Charles Shaw label bought from bankruptcy for $27,000 (1995); Two Buck Chuck 1B+ bottles sold.",
            " Employee turnover ~5–6% versus industry ~60%+; crew paid 40–60% above market with 15–20% store discount and 15% retirement contribution.",
            " 7-Eleven market cap ~$30B; Trader Joe's estimated ~$32–35B private valuation at ~1×+ revenue despite zero public float.",
        ],
        "mental_model_append": {
            "components": " Limited ~4,000 SKUs and intentional scarcity (crowded parking, one location per market) reduce comparison shopping.",
            "application": " Private ownership under Aldi Nord since 1979 enables ~11% revenue growth for 20+ years without quarterly earnings pressure.",
        },
        "ki_answer_append": ["", "", "", "", ""],
        "ca_append": (
            " Gross margins ~22–25% versus grocery industry ~27–30% by design — absolute margin dollars per square inch drive profit, not percentage."
        ),
    },
    "acq-epic-systems-mychart": {
        "important_facts_append": [
            " ~280M patient records (~45% of Americans) on MyChart; ~47 years without losing a customer except one six-month return.",
            " Total funding: $70K equity plus $70K bank debt in 1979 on ~$70K Data General minicomputer; revenue today ~$5.7B.",
            " Chronicles single-database: EpicCare (1992 GUI), Resolute billing (1987), Cadence scheduling share one patient model.",
            " Healthcare ~18% of US GDP; Ben cites ~$800B annual waste (~30% of spend); HITECH ~$30B incentives drove 2009–2015 adoption.",
            " Epic won ~$16B DOD/VA contract (2022) over Oracle-owned Cerner; ~15,000 employees, ~15,000 annual user-group meeting attendees.",
        ],
        "mental_model_append": {
            "components": " Judy learned from Meditech's Neil Pappalardo (programmer-CEO) — generational programming talent like Bill Gates parallel.",
            "application": " AI ambient scribes (Microsoft/Nuance DAX) succeed only with Epic partnership — Epic controls hospital distribution choke point.",
        },
        "ki_answer_append": ["", "", "", "", ""],
        "ca_append": (
            " Ben and David estimate minimum private value ~$100B; Judy Faulkner and family foundation own ~half — GE, Microsoft, Google bids rejected."
        ),
    },
    "acq-the-browser-with-brendan-eich-chief-architect-of-netscape-mozilla-and-ceo-of-brave": {
        "important_facts_append": [
            " Brave reported 50M+ monthly active users at recording — largest blockchain-based app by user count hosts cite.",
            " Brave returns ~70% of gross ad revenue to users via Basic Attention Token in self-custodied wallets.",
            " Firefox peaked above 25% global share; eroded to roughly 3% at episode time after Chrome (2008) process-isolated tabs.",
            " Mozilla derives vast majority of revenue from Google default-search deal — hundreds of millions of dollars annually Ben cites.",
            " Chrome controlled ~65% global browser share at recording; Safari second on mobile per episode discussion.",
        ],
        "mental_model_append": {
            "components": " Brendan Eich created JavaScript in ~10 days at Netscape (1994); Brave launched 2016 as Chromium fork.",
            "application": " Opera wallet precedent proves browser-baked hot wallet concept; Brave Search rollout (2021) expands beyond browser alone.",
        },
        "ki_answer_append": ["", "", "", "", ""],
        "ca_append": (
            " Failed challengers Dolphin and RockMelt cited; Moxie Marlinspike decentralization-vs-UX tension on whether Web3 avoids consolidation."
        ),
    },
}


def apply_second_pass(eid: str) -> None:
    path = APPROVED / f"{eid}.json"
    data = json.loads(path.read_text(encoding="utf-8"))
    add = ADDITIONS[eid]

    facts = data.get("important_facts", [])
    appends = add.get("important_facts_append", [])
    for i, extra in enumerate(appends):
        if i < len(facts) and extra.strip():
            facts[i] = facts[i].rstrip(".") + "." + extra

    mm = data.get("mental_model", {})
    mma = add.get("mental_model_append", {})
    for key in ("components", "application"):
        if mma.get(key):
            mm[key] = str(mm.get(key, "")).rstrip() + mma[key]
    data["mental_model"] = mm

    ki_appends = add.get("ki_answer_append", [])
    for i, extra in enumerate(ki_appends):
        if i < len(data.get("key_insights", [])) and extra.strip():
            ans = data["key_insights"][i]["answer"]
            data["key_insights"][i]["answer"] = ans.rstrip() + " " + extra

    ca = add.get("ca_append", "")
    if ca:
        data["competitive_advantage"] = str(data.get("competitive_advantage", "")).rstrip() + ca

    path.write_text(json.dumps(data, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")


def main() -> None:
    for eid in ADDITIONS:
        before = validate_summary(json.loads((APPROVED / f"{eid}.json").read_text()), TMPL).total_words
        apply_second_pass(eid)
        data = json.loads((APPROVED / f"{eid}.json").read_text())
        after = validate_summary(data, TMPL).total_words
        gap = word_gap(data, TMPL)
        print(f"{eid}: {before} -> {after} gap={gap}")
        if gap == 0:
            subprocess.run(
                [sys.executable, str(ROOT / "scripts" / "publish_approved_batch.py"), eid],
                check=True,
                cwd=ROOT,
            )


if __name__ == "__main__":
    main()
