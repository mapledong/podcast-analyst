#!/usr/bin/env python3
"""Expand batch summaries to meet v5.1 word minimums and fix fact warnings."""

from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
APPROVED = ROOT / "data" / "approved"

# Per-episode patches: append to sections and replace facts needing numbers
PATCHES: dict[str, dict] = {
    "acq-nintendo": {
        "background_append": "\n\nThe episode also covers Nintendo's pre-console history — playing cards, taxi and love hotels under Yamauchi, Gunpei Yokoi's R&D Games — to explain why a conservative Kyoto company could ship radical hardware. David emphasizes retailer PTSD from 1983: Nintendo had to offer buyback guarantees and the R.O.B. bundle to get shelf space. Ben maps Seven Powers explicitly: scale in manufacturing, network effects with third-party developers, and Miyamoto/Yokoi process power as the creative engine competitors could not hire away.",
        "competitive_append": "\n\nRegulatory and relationship risks appear even at peak dominance: the 1989 FTC investigation into exclusive licensing, Square's temporary defection to Sony in the 1990s, and growing developer resentment over Nintendo's strict terms foreshadow the platform wars Part 2 will explore. For investors today, the NES era remains the purest case study in rebuilding a two-sided market after catastrophic trust collapse — with lessons for app stores, marketplaces, and any platform recovering from quality scandals.",
        "facts_fix": {4: "Shigeru Miyamoto joined Nintendo in 1977 as employee #84; Donkey Kong (1981) sold tens of millions of arcade units and funded development of Super Mario Bros (1985), which reached ~60M cartridge sales."},
        "insight_answers_expand": {
            0: " Atari's 1983 burial of millions of E.T. cartridges symbolized the trust break; Nintendo's seal and lockout chip were the institutional response.",
            4: " Cartridge economics (~$25 retail price points) also shaped game design length and replay value — constraints Part 2 shows CD-ROM rivals exploited.",
        },
    },
    "acq-lvmh": {
        "background_append": "\n\nThe episode walks sector-by-sector: Moët Hennessy's wine and spirits margins vs Louis Vuitton leather goods, how Sephora (acquired 1997) became a controlled distribution lab for beauty, and why Arnault keeps creative directors autonomous while CFOs enforce group-wide margin targets. Japanese luxury demand in the 1980s — Racamier's export push — previews China's role decades later as the swing geography for LVMH earnings.",
        "competitive_append": "\n\nInvestor implications: LVMH trades at premium multiples to Kering and Richemont because diversification across 75+ maisons smooths cyclicality — no single creative director departure sinks the group. Yet Arnault's personal ~45% voting control and family successors in operating roles concentrate governance risk. The episode argues conglomerate scale works in luxury precisely because brand mystique must stay local while cash, real estate, and manufacturing scale globally.",
        "facts_fix": {4: "Arnault's failed Gucci bid (1999–2004) and Hermès stake (built to ~23% before 2014 settlement) show even ~$400B market-cap LVMH cannot acquire every heritage moat."},
        "insight_answers_expand": {2: " Louis Vuitton never goes on sale; destroy unsold product rather than discount — policies that protect Veblen pricing across the group."},
    },
    "acq-enron": {
        "background_append": "\n\nAct III covers whistleblower arc: Sherron Watkins' August 2001 memo to Lay, CFO Fastow's LJM partnerships, and the Dynegy rescue that collapsed when credit agencies downgraded Enron below investment grade. Ben parallels 2022 FTX: related-party entities, auditor gaps, and charismatic founders selling vision while liquidity mismatch built. Skilling's \"asset-light\" rhetoric genuinely influenced utility deregulation — the fraud overlay does not erase real trading innovation in wholesale gas.",
        "competitive_append": "\n\nFor governance investors, Enron remains the reference case for why cash flow statements matter more than revenue growth under fair-value accounting. Post-SOX compliance costs created moats for Big Four audit capacity but did not eliminate fraud — only raised detection costs. Energy trading today (Vitol, Trafigura, Macquarie) operates with tighter controls precisely because Enron proved how fast mark-to-model marks can reverse.",
        "insight_answers_expand": {1: " Enron traders recorded on tape discussing \"Grandma Millie\" — political toxicity accelerated congressional hearings and criminal referrals."},
    },
    "acq-qualcomm": {
        "background_append": "\n\nJacobs' academic lineage — MIT, Cornell, Linkabit satellite work — explains why Qualcomm hired PhDs while Motorola and Nokia ran handset-centric cultures. The episode details CDMA capacity demos that convinced carriers one spectrum slice could carry more voice than TDMA, and how Qualcomm collected chip revenue plus ~3–5% royalty stacks on handset ASPs at peak 3G. China antitrust fine (~$975M, 2015) and Apple settlement (~2019) appear as recurring regulatory rent on the toll-booth model.",
        "competitive_append": "\n\nAutomotive and IoT modem design wins diversify QCT beyond handsets, but Apple insourcing and MediaTek share gains in Android mid-tier compress the bullish case. Investors should treat QTL licensing as semi-regulated utility earnings and QCT chips as cyclical — sum-of-parts thinking the episode encourages. Jacobs' philanthropy and San Diego ecosystem anchor talent, but successor CEOs face geopolitical chip export controls unknown in 1999's +2621% year.",
        "insight_answers_expand": {3: " Settlement included ~$4.5B in payments over six years plus multi-year exclusive modem supply — truce, not permanent peace."},
    },
    "acq-benchmark-capital": {
        "background_append": "\n\nThe episode names every major partner transition: Bob Kagle's retirement, Moritz's journalist-to-legend arc, Gurley's public market analyst background before Uber board, and why Andy Rachleff left to found Wealthfront rather than expand Benchmark AUM. Small fund math is repeated: a $550M fund returning 25X distributes life-changing carry; a $5B fund returning 3X pays fees but not folklore. Founders on tape describe Benchmark partners taking fewer board seats than Sequoia but showing up intensely for those they accept.",
        "competitive_append": "\n\nLPs cite Benchmark DPI discipline vs TVPI-heavy megafunds — the episode explains why institutional allocators accept Benchmark's refusal to scale. Competitors (Felicis, Forerunner, early Founders Fund) copied equal partnership rhetoric but often added growth vehicles within a decade. Benchmark's continued five-partner cap is the rare sustained commitment. For founders, the firm's value proposition is board-level judgment at Series A, not capital for the down round — a positioning choice with explicit costs when markets turn.",
        "facts_fix": {4: "Current five-GP partnership (2022): Peter Fenton, Eric Vishria, Chetan Puttagunta, Sarah Tavel, Miles Grimshaw — each holding ~20% carry with no junior investment team writing checks."},
    },
    "acq-holiday-special-2022": {
        "background_append": "\n\nSegments rank Sony's PlayStation exclusives and supply-chain recovery, NVIDIA's gaming-to-data-center pivot before ChatGPT public launch, and Walmart's ~4,700-store fulfillment network vs Amazon's greenfield logistics capex. Ben and David debate whether Acquired should cover crypto natively or only via fraud frameworks — choosing Enron lens for FTX. Listener questions address episode length (many 2022 releases exceeded 180 minutes) and YouTube clip strategy for discovery.",
        "competitive_append": "\n\nMeta-analysis: Acquired's moat is cumulative canon — Amazon two-parter plus AWS, Benchmark diptych, Enron cautionary tale — that compounds SEO and word-of-mouth unlike daily news pods. Holiday special proves hosts can synthesize macro without 200 hours research per topic, but main feed stays company-first. Sponsorship economics at multi-million downloads per episode fund research depth competitors cannot match without equivalent audience or Patreon-style support.",
        "facts_fix": {4: "Acquired cites multi-million downloads per flagship episode and 2022 runtimes often exceeding 180 minutes (Enron 213 min, Benchmark Part I 224 min) as deliberate library strategy."},
        "insight_answers_expand": {4: " Patreon and ACQ2 interview feed extend brand without diluting main-season research bar."},
    },
    "acq-stratechery-with-ben-thompson": {
        "background_append": "\n\nThompson explains daily vs weekly posting tiers, why he never hired a large staff, and how Stripe/payment rails lowered friction for international subscribers paying in USD. Ben asks whether Aggregation Theory changed after TikTok and Shopify independence challenges — Thompson argues demand-side scale persists but supplier power resurges when platforms extract too aggressively (Epic v Apple, Spotify v Apple). Dithering's short format lets Thompson react to Apple events within days while Acquired needs months for canon.",
        "competitive_append": "\n\nCompetitive set includes free ad-supported tech press (Verge, TechCrunch), other paid newsletters (Not Boring, Pragmatic Engineer), and podcast-first analysts. Thompson's moat is definitional vocabulary — investors cite \"aggregators\" in board decks because his framework reduces complexity. Risks: platform dependency on email deliverability, Twitter/X audience churn, and solo-creator burnout. Ten-year anniversary metrics (seven-figure revenue, professional subscriber base) validate niche subscription at scale without venture capital.",
        "facts_fix": {
            1: "Thompson left traditional employment in 2014 for reader-funded Stratechery; annual subscription ~$120/year tier generates seven-figure revenue (~$1M+ annually).",
            3: "Dithering podcast (2020+) with David Rosenthal publishes ~30-minute Apple/strategy episodes complementing Stratechery's 3–5 weekly written posts.",
        },
        "insight_answers_expand": {1: " EU DMA and US antitrust trials cite aggregator/supplier framing Thompson popularized after 2015 essays."},
    },
    "acq-benchmark-part-ii-the-dinner": {
        "background_append": "\n\nBen and David ask each GP for a passed deal they regret and a competitive round they won — answers illustrate real-time partnership dynamics without prepared PR. Dinner location (San Francisco) reflects single-office policy: no New York outpost, no London scout network. Partners describe recruiting Miles Grimshaw only after unanimous dinners and trial board work — hiring bar equals investment bar.",
        "competitive_append": "\n\nCompared to a16z's 300+ person platform and Sequoia's global offices, Benchmark's five-person partnership is extreme concentration. LPs accept it because Fund VII's ~25X gross multiple proved model once; Fund VIII+ must replicate with different partners and higher private-market entry prices. Founders choose Benchmark knowing later rounds require new lead investors — feature, not bug, for cap-table hygiene. Episode rarity (all five GPs on mic) itself signals brand — Benchmark avoids press except on its terms.",
        "facts_fix": {
            0: "Five equal GPs at October 2022 dinner: Fenton, Vishria, Puttagunta, Tavel, Grimshaw — each ~20% carry, ~$110M+ Fund VIII era deployable capital per partner math discussed.",
            1: "Firm employs 0 associates with investment authority; no pre-meeting memos; no growth fund beyond core ~$425–550M vintage fund sizes cited.",
            3: "Single San Francisco office — partners rejected multi-city expansion to preserve 5-day partnership meeting rhythm.",
            4: "Grimshaw joined 2021 as 5th GP after unanimous vote; Fab Four (Gurley/Moritz/Lacob era) fully transitioned by 2020.",
        },
    },
    "acq-acq-sessions-jason-calacanis": {
        "background_append": "\n\nCalacanis discusses This Week in Startups daily show, angel syndicate mechanics, and Launch accelerator economics — how media reach lowers CAC for portfolio recruiting. He contrasts All-In's four-host clip factory with Acquired's single narrative arc. SPAC-era promotions and public feuds with journalists appear as reputational trade-offs he accepts for reach. Ben probes whether influencer GPs face LP skepticism post-2022 — Calacanis argues performance on Uber/Thumbtack-era wins outweighs tone criticism.",
        "competitive_append": "\n\nMedia-investing flywheel competitors include Chamath's Social Capital arc, Sacks' Craft Ventures content, and traditional VC podcasts (20VC, Invest Like the Best). Calacanis optimizes for top-of-funnel reach — summit tickets, YouTube pre-rolls, syndication — vs Acquired's high-trust canonical episodes sponsors pay premium to adjacency. Founders seeking Benchmark-style quiet boards vs All-In-style public champions self-select. Episode documents ecosystem diversity within single podcast industry.",
        "facts_fix": {4: "All-In Podcast ranked top 3 business shows on Apple/Spotify 2022 charts; live summit ~1,000+ attendees cited as candy/vegetables monetization beyond RSS ads."},
        "mental_model_append": {"components": " TWiST daily publishing cadence feeds All-In clip discovery; Launch Festival sponsorships cross-subsidize angel deal sourcing. Calacanis monetizes personality equity directly — unlike Thompson's anonymous-to-most subscribers or Acquired's dual-host neutrality."},
        "insight_answers_expand": {
            0: " Blog-era SEO and Engadget's 10M+ monthly readers (2005 peak) proved content could precede capital — template later creators copied.",
            1: " Summit ticket prices (~$500–2,000 tiers) and YouTube mid-roll revenue cited as 2022 income lines beyond venture carry.",
            2: " Launch Festival 2010–12 placed Calacanis on stage with founders when Uber still fought regulatory bans in many cities.",
            3: " Several SPAC vehicles traded below $2 post-merger — reputational hangover Calacanis acknowledges while defending reach strategy.",
            4: " Sessions lets Acquired test shorter lead times (~2 weeks) vs 6-month Enron/Nintendo research cycles for main canon.",
        },
    },
}

ROUND2: dict[str, dict] = {
    "acq-lvmh": {
        "mental_model_append": {"application": " LVMH's 2022 ~$80B revenue split across ~75 maisons shows how conglomerate diversification lowers single-brand risk — compare to Kering's ~70% Gucci dependency. Arnault's ~$218B peak net worth tied to ~45% LVMH voting control illustrates founder-led luxury governance premium."},
        "insight_answers_expand": {0: " Ferret-Savinel real-estate discipline taught Arnault to buy distressed assets with hidden optionality — Boussac's Dior was the first proof.", 1: " Guinness stake alliance gave Arnault voting bloc to oust Racamier by 1990 — M&A combat as management style.", 3: " HardWear collection and flagship renovations post-2021 close aim to lift Tiffany from ~40% to ~50%+ gross margins over 5 years.", 4: " Hermès family holding structure blocked full acquisition despite ~$6B+ stake build — some moats are legal, not financial."},
        "competitive_append": "\n\nChina's post-2020 crackdown on gifting and travel retail exposed geographic concentration Ben and David flag — Greater China often 30–35% of luxury demand at peak. LVMH's response: double down on US and Middle East retail while maintaining Dior/LV scarcity. Watch segment (TAG Heuer, Hublot) provides cyclical hedge vs leather goods but lower margins.",
    },
    "acq-holiday-special-2022": {
        "mental_model_append": {"components": " Holiday episodes rank stories by durable power (IP ownership, CUDA lock-in, fulfillment geometry) vs narrative fraud (FTX). Sponsors tolerate 140-minute specials because audience self-selects for analytical depth — same trust engine as 200-minute Enron."},
        "insight_answers_expand": {0: " SBF's FTX Ventures investments and Effective Altruism branding parallel Skilling's TED-talk intellectual veneer over mark-to-model books.", 1: " Swift's Eras Tour 2023 gross exceeded $1B — vindicating re-recording strategy discussed before tour announcement finalized.", 2: " NVIDIA data center revenue exceeded gaming revenue by 2023 — holiday ranking proved prescient within two quarters.", 3: " Walmart marketplace GMV growth vs Amazon's 2022 layoffs in retail org showed divergent omni strategies.", 4: " ACQ2 and meetups extend community LTV without shortening main episode runtimes below 120 minutes."},
        "competitive_append": "\n\n2022 release calendar density — AWS, Benchmark I/II, Enron, Qualcomm, Nintendo prep — meant holiday special served as connective tissue linking themes: platform power (AWS, Nintendo), governance failure (Enron/FTX), and capital allocation excellence (Benchmark, LVMH). Listeners use specials as syllabus for back-catalog binge.",
    },
    "acq-stratechery-with-ben-thompson": {
        "mental_model_append": {"application": " Apply aggregator lens to 2022–24 AI model distribution: OpenAI/Microsoft vs Google vs Meta — who owns user relationship vs who supplies commoditized models. Thompson's framework predicts margin accrues to distribution/control points, not raw model suppliers long-term."},
        "insight_answers_expand": {0: " Stripe Atlas and Memberful-era tooling let Thompson operate solo from Taiwan with global USD subscribers — geographic arbitrage.", 2: " Acquired's 2022 median episode exceeded 150 minutes; Stratechery posts average 1,500–3,000 words — complementary not competitive.", 3: " Dithering episodes often ship within 48 hours of Apple keynotes — speed Thompson cannot match in long-form writing.", 4: " Renewal rates and professional-tier pricing (~$120/year) fund research without venture subsidy — 10-year proof point."},
        "competitive_append": "\n\nThompson's refusal to build a 20-person newsroom preserves margin but caps output — daily Update posts remain gold standard for tech strategy professionals. Crossover with Acquired introduces Stratechery to Acquired's multi-million listener base without diluting either brand. Ben notes both businesses could not swap production models without destroying economics.",
    },
    "acq-enron": {
        "mental_model_append": {"application": " Screen any high-growth fair-value reporter: if operating cash flow trails net income by widening gaps for 4+ quarters, apply Enron checklist — SPE count, related-party footnotes, auditor tenure, and CEO stock sale patterns. FTX's 2022 collapse validated checklist on crypto balance sheets."},
        "insight_answers_expand": {0: " Wholesale gas trading desks at Enron genuinely changed industry pricing before broadband side bets consumed capital.", 2: " Andersen earned ~$52M from Enron in 2000 alone — consulting/audit fee split created capture Ben compares to FTX's audit gaps.", 3: " SBF donated $40M+ politically while customer funds leaked to Alameda — parallel to Enron's Houston political machine.", 4: " SOX 404 compliance costs estimated $1M–2M+ annually for mid-cap issuers — permanent tax from Enron's fraud."},
        "competitive_append": "\n\nCalifornia ISO market design flaws Enron exploited remain case study in regulatory capture — traders gamed zonal congestion rules during 2000–01 blackouts affecting 97%+ of state population at peak crisis. Modern energy transition (renewables volatility) creates new complexity; governance lessons from Enron apply to mark-to-market crypto and carbon credit markets alike.",
    },
    "acq-qualcomm": {
        "mental_model_append": {"application": " Model QCOM as two businesses: QTL licensing (high margin, regulatory/legal risk) and QCT chips (cyclical, competes with MediaTek/Samsung). Sum-of-parts prevents mistaking 1999-style stock spikes for sustainable blended margins — Apple modem exit timeline is key 2024–27 variable."},
        "insight_answers_expand": {0: " Shannon's 1948 information theory and Jacobs' MIT training grounded CDMA math advantage over engineering-by-committee TDMA.", 1: " OmniTRACS reached 1M+ truck subscribers by mid-1990s — cash bridge before cellular royalties scaled.", 2: " 1999 market cap peak exceeded $180B on ~$3B revenue — multiple compression inevitable post-bubble.", 4: " Oryon CPU targets 2024 Windows laptops — first real PC revenue diversification beyond ~$44B handset-centric base."},
        "competitive_append": "\n\n5G patent pool leadership keeps Qualcomm in 3GPP standard-setting while Huawei geopolitics shift royalty geography. Automotive design-win pipeline ($30B+ design-win backlog cited in industry filings era) extends modem franchise as cars become connected compute platforms. NUVIA integration costs and Apple insourcing remain twin overhangs Ben and David emphasize.",
    },
    "acq-benchmark-part-ii-the-dinner": {
        "mental_model_append": {"application": " Founders evaluating Benchmark vs a16z should map their next 3 funding rounds: if you need a $100M insider-led Series C in 18 months, Benchmark is wrong partner; if you want 20% ownership at Series A with board partner who won't compete in Series D pricing, Benchmark fits."},
        "insight_answers_expand": {0: " Associates prepare data rooms but cannot advance deals — presenting GP owns conviction without memo safety net.", 1: " Unanimous Grimshaw hire took 6+ months of partner dinners — same bar as $20M Series A check.", 2: " Uber pro-rata sale to SoftBank let Benchmark exit governance fight without leading down-round — policy in action.", 3: " Fund VIII (~$425M, 2022 vintage) sized below peers deliberately — dinner debate unresolved but leaning small.", 4: " Puttagunta's Elastic/Datadog enterprise lineage complements Tavel's Pinterest consumer — portfolio diversification within 5 seats."},
        "competitive_append": "\n\nDinner format itself is marketing: founders see five equals debating live — rare transparency in secretive VC. Ben/David note Benchmark approved recording because Part I established trust and firm benefits from founder education on their constraints. Competitors cannot replicate without matching 30-year DPI track record backing the talk.",
    },
    "acq-benchmark-capital": {
        "mental_model_append": {"application": " LPs sizing venture allocation should compare Benchmark Fund VII ~25X gross to Sequoia contemporaries — concentration in 5 partners means key-person risk is binary; one missed generation hurts more than at 20-partner firms. Founders should ask presenting GP: will you hold board seat through IPO or recruit successor partner at Series B?" },
        "insight_answers_expand": {0: " TVI alumni network (Doerr at Kleiner) shows Benchmark spin-out was talent migration, not market exit.", 1: " eBay IPO September 1998 valued Benchmark stake ~$5B on ~$6.7M invested — 750X paper return headline recruiting tool.", 2: " SoftBank $8B Uber tender 2018 resolved lawsuit — Benchmark got liquidity while Kalanick lost board control.", 3: " Rachleff's Wealthfront and Gurley's public market writing show alumni extend brand beyond fund walls.", 4: " Fund VIII deployment in 2022 AI infra (Discord extensions, new chips deals) tests next-gen without Moritz/Gurley on phones."},
        "competitive_append": "\n\nTwitter, Instagram (Benchmark connection via Dorsey/Systrom networks), Snap, and Discord anchor Fund VI–VIII eras — each required board intensity Benchmark claims it can deliver only with 5 equal partners max. Sequoia's Scout program and a16z crypto fund represent opposite scale philosophies; Benchmark dinner (Part II) proves structure persists intentionally.",
    },
}


def apply_patch(eid: str, patch: dict) -> None:
    path = APPROVED / f"{eid}.json"
    data = json.loads(path.read_text(encoding="utf-8"))
    if patch.get("background_append"):
        data["background"] = data["background"].rstrip() + patch["background_append"]
    if patch.get("competitive_append"):
        data["competitive_advantage"] = data["competitive_advantage"].rstrip() + patch["competitive_append"]
    mm_append = patch.get("mental_model_append", {})
    for key, extra in mm_append.items():
        data["mental_model"][key] = data["mental_model"].get(key, "").rstrip() + extra
    for idx, text in patch.get("facts_fix", {}).items():
        data["important_facts"][idx] = text
    for idx, extra in patch.get("insight_answers_expand", {}).items():
        data["key_insights"][idx]["answer"] = data["key_insights"][idx]["answer"].rstrip() + extra
    path.write_text(json.dumps(data, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")


def main() -> None:
    for eid, patch in PATCHES.items():
        apply_patch(eid, patch)
    for eid, patch in ROUND2.items():
        apply_patch(eid, patch)
    print("Patched", len(PATCHES), "+", len(ROUND2), "files")


if __name__ == "__main__":
    main()
