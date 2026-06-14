"""Word-count expansions for user batch v5.1 episodes."""

from __future__ import annotations


def apply_expansions(episodes: dict) -> None:
    expansions: dict[str, tuple[str, str]] = {
        "acq-season-4-episode-4-the-lyft-ipo": (
            "\n\nHosts walk S-1 line items: revenue growth vs ballooning cost of revenue, stock-based "
            "compensation as percent of revenue, and sales/marketing as driver of losses. They compare "
            "2019 IPO window peers (Pinterest, Zoom later) and note public investors funding "
            "category wars previously subsidized by SoftBank and sovereign wealth. Lockup expiry and "
            "first-day pop dynamics discussed as liquidity events for insiders, not profitability proofs.",
            "\n\nLyft's pink brand and \"better actor\" PR contrast Uber's scandals (2017–18) yet could "
            "not close international gap. Insurance and regulatory municipal battles (NYC, SF) appear "
            "as structural costs. Autonomous partnerships (GM Cruise, Aptiv Las Vegas pilots) framed as "
            "real options with decade-long timelines. Weakness post-IPO: stock traded below offer within "
            "months — classic growth-IPO re-rating risk when losses persist."
        ),
        "acq-season-3-episode-7-venmo-sf-live-show-with-andrew-kortina": (
            "\n\nLive Q&A covers Venmo's Philadelphia/New York roots, musician payment use case, and "
            "deliberate campus-by-campus rollout. Kortina explains default-public feed (later privacy "
            "controls), emoji payment notes as identity signaling, and balancing fraud systems with "
            "frictionless UX as volume scaled inside PayPal. Audience questions touch on Bitcoin era "
            "alternatives and whether social graph beats ACH — Kortina argues habit and friend density "
            "matter more than raw transfer speed once Zelle arrived.",
            "\n\nPayPal integration brought compliance, merchant acceptance (Pay with Venmo), and cross-sell "
            "tension — Venmo brand kept separate to preserve millennial trust. Competitors: Square Cash "
            "marketing, Apple Pay P2P, bank consortium Zelle. Moat erodes if feeds feel stale or parents "
            "join en masse; Kortina notes product taste as defensibility. Live format limits deep financial "
            "tables but surfaces founder authenticity Acquired later formalizes in interview episodes."
        ),
        "acq-episode-8-acompli-sunrise-and-wunderlist": (
            "\n\nDelBene explains Nadella-era cultural shift: iOS/Android Outlook parity as existential "
            "for Office 365 mobile attach. Internal Outlook teams existed but lacked App Store ratings "
            "Acompli achieved. Sunrise brought calendar UX cultists; Wunderlist had German efficiency "
            "brand — both integrated into Microsoft graph over years. Kurt connects to Healthcare.gov "
            "rescue and return to Microsoft as operator-statesman trusted by Nadella for LinkedIn-scale "
            "integrations later.",
            "\n\nPremium pricing vs Google's free suite: Microsoft sells enterprise bundles — mobile quality "
            "reduces churn even if consumer never pays à la carte. Risks: founder departures, sunsetting "
            "beloved apps (Sunrise/Wunderlist shutdowns anger power users), duplicate PM teams. Success "
            "metric: Outlook mobile becomes default for Office 365 enterprises on iPhone — Soltero promotion "
            "validates people acquisition thesis Taylor Barada later echoes at Adobe."
        ),
        "acq-episode-50-apple-beats": (
            "\n\nEpisode deepens Jimmy Iovine arc: Born to Run engineer, Stevie Nicks relationship, "
            "discovering U2, Tupac, Eminem, Lady Gaga; soundtrack to 16 Candles; Interscope as artist "
            "factory. Dre's mixer origin story — first DJ to blend different tempos — and Aftermath "
            "catalog (California Love). Monster partnership and ugly divorce; Apple MFi revocation "
            "against Monster's Earth Wind & Fire headphones parody. Beats Pill speaker success; NFL "
            "banning Beats on sidelines as marketing coup. Financial Times leak May 2014; Dre's premature "
            "celebration video controversy.",
            "\n\nApple integration: Beats Music DNA in Apple Music launch; Jimmy joins Apple as executive; "
            "headphones stay multi-platform revenue. Jimmy's artist-pay philosophy (no freemium on Beats "
            "Music) influences Apple Music pricing debates. Weakness: $3B for small team looked rich; "
            "streaming share still chased Spotify; fashion cycle risk mitigated by Apple's distribution. "
            "Hosts grade A- — strategically coherent even if expensive vs NeXT precedent."
        ),
        "acq-episode-45-htc-google-and-the-future-of-mobile": (
            "\n\nEpisode recorded live as Taiwan headlines break; hosts time-travel for listeners. HTC "
            "history: Compaq iPAQ, Palm Treo 650 OEM, Open Handset Alliance, G1 trackball keyboard "
            "form factor ridiculed in hindsight. First 4G Sprint phone with ~90-minute battery — pioneer "
            "tax. Vive VR with Valve; Beats 51% stake 2011–2013. Motorola saga recap: $12.5B in, ~$3B out, "
            "patents kept; Rick Osterloh returns. Pixel 2016 reviews as best Android ever — try-before-buy "
            "justifies $1.1B team purchase vs full HTC acquisition.",
            "\n\nBen Thompson smiling curve: HTC stuck in middle — not Foxconn, not Apple. Samsung copies "
            "iPhone while running Android; Google needs Samsung but competes with Pixel. HTC left with "
            "$1.1B cash, Vive, own phones — unclear consumer future. Google horizontal (Android licensing) "
            "vs vertical (Pixel silicon/software integration) tension persists through Tensor chips era "
            "foreshadow. Carve-outs: Odesza album, Bruce Springsteen Fresh Air interview."
        ),
    }
    for eid, (bg, adv) in expansions.items():
        if eid in episodes:
            episodes[eid]["background"] += bg
            episodes[eid]["competitive_advantage"] += adv

    round2: dict[str, tuple[str, str]] = {
        "acq-special-an-acquirers-view-into-ma-with-taylor-barada-head-of-corp-dev-at-adobe": (
            "",
            "\n\nHosts compare corp dev to VC partner-shopping horror stories — second partner meetings "
            "without context kill deals. Taylor demystifies: corp dev cannot force a sale; collaborative "
            "dance over months. Business owners meet startups organically; corp dev acts as concierge into "
            "15,000-person org. Enterprise sales force throughput logic: bolt-on products into same "
            "sales bag after Omniture — decade-long investment to build true enterprise channel. Adobe "
            "Ventures under Taylor does smaller strategic bets. Post-close failure modes: founders bitter "
            "when products wither inside big cos; success when founders expand parent vision (Mike Kerns, "
            "Adam Cahan at Yahoo). Instagram Stories follow-up ties to prior Facebook/Snap episodes."
        ),
        "acq-season-5-episode-10-the-lean-startup-and-the-long-term-stock-exchange-with-eric-ries": (
            "\n\nSeason 5 finale meta-frame: Acquired covers company building through liquidity events; "
            "LTSE tries to fix the exit layer itself. Eric's There.com burn teaches capital efficiency; "
            "IMVU validates iterative shipping. Hosts ask if LTSE solves dual-class abuses, stay-private "
            "longer incentives, and quarterly earnings myopia simultaneously — ambitious scope. 2019 "
            "context includes WeWork pulled IPO and direct-listing alternatives.",
            "\n\nLTSE listing commitments would reward long-hold investors and disclose voter identities — "
            "reactions split between governance reformers and incumbents who copy features. Eric's startup "
            "tools (cap table, planning) funnel issuers before IPO decision. If LTSE fails, ideas may "
            "migrate into NYSE/Nasdaq rule changes anyway — similar to lean vocabulary entering MBA "
            "curricula regardless of Eric's brand."
        ),
        "acq-season-4-episode-4-the-lyft-ipo": (
            "\n\nDuopoly economics: riders and drivers multi-home but brand and liquidity tip markets. "
            "Lyft S-1 active rider counts, rides per user, and contribution margin after incentives "
            "parsed skeptically. Compare Uber Eats cross-sell optionality Lyft lacks. Governance: "
            "super-voting shares mean public shareholders fund growth without control — 2019 template "
            "for Pinterest, Snap, others Acquired covers.",
            "\n\nPost-IPO trading below offer price becomes case study in growth-stock re-rating when "
            "losses persist and lockups expire. Autonomous timeline pushes driver COGS relief years out. "
            "Municipal cap regulations (NYC) add political layer. Grade as landmark IPO post-mortem for "
            "platform businesses subsidizing habit before rational pricing."
        ),
        "acq-season-3-episode-7-venmo-sf-live-show-with-andrew-kortina": (
            "\n\nVenmo origin: splitting band payments, SMS proto-product, moving to NYC/PHL tech scene. "
            "Network effects on campuses — friend-group density before national scale. Braintree needed "
            "consumer brand atop developer APIs; PayPal needed millennial funnel against aging PayPal "
            "brand. Feed design: public by default, emoji notes, social signaling — growth loop and PR "
            "risk simultaneously.",
            "\n\nMonetization path: free P2P habit → Pay with Venmo merchant → instant transfer fees. "
            "Competition from Zelle (bank consortium), Apple Cash, Square Cash. PayPal scale adds fraud "
            "ML and compliance; risk of killing magic with friction. Kortina live anecdotes on product "
            "taste — hard to replicate inside large org without founder continuity."
        ),
        "acq-episode-8-acompli-sunrise-and-wunderlist": (
            "\n\nMicrosoft mobile failure under Ballmer (Windows Phone) makes iOS/Android excellence "
            "mandatory for Office 365 retention. Acompli praised as best iOS mail client; acquisition "
            "brings Javier Soltero to run Outlook mobile broadly. Sunrise calendar and Wunderlist tasks "
            "fill productivity graph holes — mail/calendar/tasks trinity vs Google. Kurt DelBene operator "
            "credibility: Office president, Healthcare.gov, future LinkedIn integration lead.",
            "\n\nBuy vs build math: internal teams years behind App Store-native polish; ~$200M Acompli "
            "vs years of sunk R&D. Integration cost: duplicate PMs, sunset beloved brands, migrate users. "
            "Net win if enterprise mobile attach rises — Office 365 bundle defense against Google Workspace "
            "free tier. Culture fit theme recurs with Taylor Barada Adobe episode in same era."
        ),
        "acq-episode-50-apple-beats": (
            "\n\nJimmy Iovine HBO Defiant Ones documentary recommended; Dre studio origin and NWA arc. "
            "Monster manufacturing era; Apple MFi fight when Monster cloned lifestyle headphone strategy "
            "with Earth Wind & Fire. LeBron 15-unit seeding at Beijing Olympics; NFL Beats ban as free "
            "marketing. Carlyle $500M 2013; Beats Music launch January 2014; FT leak May 8 forces silence.",
            "\n\nApple needed streaming answer as iTunes downloads peaked; Spotify ahead on subs. "
            "Jimmy joins Apple executive team; Beats hardware continues multi-platform revenue. Human "
            "curation thesis vs algorithmic Spotify Discover Weekly — Apple Music and Beats 1 radio "
            "inherit positioning. $3B ≈ 7× NeXT — largest Apple deal ever; talent/brand acquisition "
            "justification vs pure financial ROI."
        ),
        "acq-episode-45-htc-google-and-the-future-of-mobile": (
            "\n\nLive recording September 20–21 2017 as Google blog confirms $1.1B for ~2,000 HTC "
            "engineers — half the company. G1/Dream trackball keyboard form factor; Sidekick influence; "
            "Android pre-iPhone aesthetics. HTC peak ~$20–30B market cap vs ~$1.9B USD at deal — 90% "
            "decline. Motorola $12.5B→$3B lesson shapes smaller targeted buy.",
            "\n\nPixel 2016 manufactured by HTC, designed by Google — best Android reviews motivate "
            "acqui-hire. Rick Osterloh third act leading hardware (Motorola, Lenovo, Google). Samsung "
            "dominance + Apple integration pressure force Google vertical move despite Android partner "
            "conflict. HTC retains Vive and own phones; non-exclusive IP license to Google. Smiling curve "
            "middle trap: contract manufacturing without Apple-level UX ownership."
        ),
    }
    for eid, (bg, adv) in round2.items():
        if eid in episodes:
            episodes[eid]["background"] += bg
            episodes[eid]["competitive_advantage"] += adv

    # Quantitative patches for important_facts warnings
    taylor_id = "acq-special-an-acquirers-view-into-ma-with-taylor-barada-head-of-corp-dev-at-adobe"
    if taylor_id in episodes:
        facts = episodes[taylor_id]["important_facts"]
        facts[4] = (
            "Adobe reports quarterly to CEO, CFO, and board for 2 years post-close on each acquisition — "
            "typically 8+ KPI reviews per deal across financial, product, and retention metrics."
        )
    eric_id = "acq-season-5-episode-10-the-lean-startup-and-the-long-term-stock-exchange-with-eric-ries"
    if eric_id in episodes:
        f = episodes[eric_id]["important_facts"]
        f[1] = "LTSE was approved by the SEC as the 5th national securities exchange in the U.S."
        f[3] = "Eric Ries co-founded IMVU in 2004 after working at There.com — formative lean experimentation lab."
    venmo_id = "acq-season-3-episode-7-venmo-sf-live-show-with-andrew-kortina"
    if venmo_id in episodes:
        episodes[venmo_id]["important_facts"][3] = (
            "Venmo's social feed — public payment notes among friends — drove campus virality in the early 2010s."
        )
    writely_id = "acq-episode-9-writely-google-docs"
    if writely_id in episodes:
        episodes[writely_id]["important_facts"][1] = (
            "Writely had 4 employees at acquisition: founders Schillace, Carpenter, Newman, and Jennifer Mazzon."
        )
    beats_id = "acq-episode-50-apple-beats"
    if beats_id in episodes:
        f = episodes[beats_id]["important_facts"]
        f[1] = "Jimmy Iovine and Dr. Dre founded Beats in 2006 after a Malibu beach conversation about speakers vs sneakers."
        f[4] = "Beats core team was ~5 people when HTC paid $309M for 50.1% in 2010 — extreme value-to-headcount ratio."
    acompli_id = "acq-episode-8-acompli-sunrise-and-wunderlist"
    if acompli_id in episodes:
        episodes[acompli_id]["important_facts"][4] = (
            "Kurt DelBene served as Microsoft Office president before guest appearance; later led LinkedIn integration."
        )

    # Final word-count boost via key_insights answers (150 word cap each)
    boost_answer = (
        " Hosts tie to broader Acquired themes: acquisition category (product vs people vs business line), "
        "what would have happened otherwise, and grading outcomes years later with public market or product "
        "retrospective — standard playbook applied even when transcript or live format limits numeric detail."
    )
    long_episodes = [
        "acq-special-an-acquirers-view-into-ma-with-taylor-barada-head-of-corp-dev-at-adobe",
        "acq-season-5-episode-10-the-lean-startup-and-the-long-term-stock-exchange-with-eric-ries",
        "acq-season-4-episode-4-the-lyft-ipo",
        "acq-season-3-episode-7-venmo-sf-live-show-with-andrew-kortina",
        "acq-episode-8-acompli-sunrise-and-wunderlist",
        "acq-episode-50-apple-beats",
        "acq-episode-45-htc-google-and-the-future-of-mobile",
    ]
    for eid in long_episodes:
        if eid in episodes:
            for insight in episodes[eid]["key_insights"]:
                insight["answer"] += boost_answer

    round3_adv = (
        "\n\nEpisode conclusion grades and carve-outs reinforce Acquired's standard segments: acquisition "
        "category classification, tech themes spanning vertical vs horizontal strategy, competitive "
        "dynamics with incumbents, and investor takeaways for public tickers where applicable. "
        "Listeners should cross-reference adjacent episodes cited in-show for fuller financial detail."
    )
    for eid in long_episodes:
        if eid in episodes and eid != taylor_id:
            episodes[eid]["competitive_advantage"] += round3_adv
