#!/usr/bin/env python3
"""Write and validate Acquired v5.1 approved JSON for episodes 37–44."""

from __future__ import annotations

import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))

from scripts._write_acq_batch_491_500_common import base  # noqa: E402
from src.template_config import template_path_for_podcast  # noqa: E402
from src.validate import load_template_config, validate_summary  # noqa: E402

META_OVERRIDES = {
    "acq-episode-37-bamtech-disney-and-the-biggest-media-company-youve-never-heard-of": {
        "title": "BAMTech, Disney and the Biggest Media Company You've Never Heard Of",
        "guest": "BAMTech / Disney",
        "guest_role": "Episode 37",
    },
    "acq-episode-38-soundjam-itunes": {
        "title": "SoundJam → iTunes",
        "guest": "SoundJam / Apple",
        "guest_role": "Episode 38",
    },
    "acq-episode-39-whole-foods-market": {
        "title": "Whole Foods Market",
        "guest": "Whole Foods / Amazon",
        "guest_role": "Episode 39",
    },
    "acq-episode-40-activision-blizzard": {
        "title": "Activision Blizzard",
        "guest": "Activision Blizzard",
        "guest_role": "Episode 40",
    },
    "acq-episode-41-bookingcom-with-jetsetter-room-77-ceo-drew-patterson": {
        "title": "Booking.com (with Drew Patterson)",
        "guest": "Drew Patterson",
        "guest_role": "Episode 41 · Guest",
    },
    "acq-episode-42-opsware-with-special-guest-michel-feaster": {
        "title": "Opsware (with Michel Feaster)",
        "guest": "Michel Feaster",
        "guest_role": "Episode 42 · Guest",
    },
    "acq-episode-43-the-square-ipo": {
        "title": "The Square IPO",
        "guest": "Square",
        "guest_role": "Episode 43",
    },
    "acq-episode-44-aol-time-warner-with-the-internet-history-podcast": {
        "title": "AOL–Time Warner (with Brian McCullough)",
        "guest": "Brian McCullough",
        "guest_role": "Episode 44 · Guest",
    },
}


def shell(ep_id: str, **body):
    ep = base(ep_id, review_notes="Manual GPT Acquired batch v5.1 — episodes 37–44", **body)
    ov = META_OVERRIDES.get(ep_id, {})
    for k, v in ov.items():
        ep["metadata"][k] = v
        if k == "title":
            ep["metadata"]["guest"] = ov.get("guest", v)
    return ep


EPISODES = [
    shell(
        "acq-episode-37-bamtech-disney-and-the-biggest-media-company-youve-never-heard-of",
        episode_rating={"overall": 4},
        keywords=["Live Streaming", "Sports Tech", "Direct-to-Consumer"],
        conclusion=(
            "Major League Baseball Advanced Media (BAM) began in 2000 as a centralized IT shop for 30 team websites, "
            "failed on outsourced builds and audio-only streaming, then pivoted to live video in 2002 — years before "
            "YouTube or Netflix streaming. Ticketmaster ($10M upfront, 2002) and MLB.tv (~100K subscribers at $80/season) "
            "turned BAM into a ~$620M-revenue live-video engine powering ESPN3, HBO Now, and NHL rights. The August 2015 "
            "spin-out to BAMTech and Disney's August 2016 one-third stake at a $3.5B valuation gave Disney optionality on "
            "over-the-top sports and a hedge against cord-cutting — collapsing ESPN, Comcast, and content into one "
            "internet-age stack. Hosts grade Disney's minority investment an A: low revenue multiple on a stair-stepped "
            "platform that solved real problems one at a time."
        ),
        background=(
            "Ben and David trace BAM from Robert Bowman's 2002 in-house rebuild through Ichiro-driven Japan audio failure "
            "and same-season video experiments ($8M from a nine-game package), to MLB.tv's 2003 launch and featured Apple "
            "App Store demos. BAM white-labeled ESPN3 (2010) and HBO Now after Game of Thrones concurrency failures, "
            "then the NHL deal (7–10% equity stake) made BAM look like a next-gen cable net. MLB spun BAMTech in August "
            "2015; Disney bought one-third for ~$1B a year later with a path to majority control — mirroring the Hearst "
            "minority in ESPN.\n\n"
            "The episode frames BAMTech as the future of television: live latency, cross-device handoff, and rights "
            "ownership (including a rumored $50M/year Riot/League of Legends bet). Disney's cable EBITDA crown jewel "
            "needed a direct consumer pipe as bundles skinny; hosts debate rebundling fatigue versus unbundled subscriptions."
        ),
        important_facts=[
            "Thirty MLB teams capitalized BAM with $1M/year for four years ($120M committed); only ~$77M was drawn after early failures and the 2002 Ticketmaster deal.",
            "MLB.tv launched in 2003 at $80/season for out-of-market games and drew ~100,000 subscribers (~$8M) in year one — four years before Netflix streaming.",
            "Bowman cited ~$620M BAM revenue in 2012; pre-spin BAMTech was on pace for ~$900M with steady profit when Disney valued the spin-out at $3.5B (~4× revenue).",
            "Disney paid ~$1B for one-third of BAMTech (August 2016) with an announced option for majority control — same partial-ownership playbook as ESPN/Hearst.",
            "The NHL partnership included a rumored 7–10% equity stake in BAM and rights monetization — first time BAM moved from white-label vendor to rights holder.",
        ],
        mental_model={
            "name": "Stair-Step Platform From Vertical Pain",
            "components": (
                "BAM did not set out to invent internet television. It solved sequential real problems: bad team sites, "
                "Ticketmaster integration, Ichiro fans wanting video not audio, out-of-market MLB packages, then other "
                "leagues' streaming back ends. Each failure (outsourced sites, audio-only Japan) funded the next iteration "
                "within one seasonal window. Expertise compounded in live latency, CDN relationships, and cross-device "
                "continuity — niche at first, horizontal later. Spin-out plus Disney capital unlocked stock comp and "
                "rights buying without 30 baseball owners optimizing for tech upside."
            ),
            "application": (
                "Platform companies often emerge from a captive customer with acute pain, not a TAM slide. Spin out when "
                "equity incentives and horizontal sales conflict with the parent P&L. For media investors, live sports "
                "remain the cord-cutting moat — whoever owns streaming infra plus rights owns the ESPN-of-OTT option. "
                "Watch whether acquirers rebundle (Disney+) or stay aggregator-neutral."
            ),
        },
        competitive_advantage=(
            "BAMTech's moat is operational, not brand: fifteen daily live MLB feeds, sub-minute latency, blackout logic, "
            "and device handoff without score spoilers — hard-won from 2002 experiments. Apple repeatedly featured MLB "
            "apps at keynotes; HBO outsourced Game of Thrones concurrency after in-house melts. White-label deals (ESPN3, "
            "HBO Now) proved scale before NHL equity made BAM a rights holder.\n\n"
            "Versus Netflix/Amazon, BAMTech lacked a consumer portal but owned live sports know-how incumbents could not "
            "replicate quickly. Disney brought balance-sheet rights purchases (Riot) and minority-stake tolerance MLB "
            "owners needed. Versus cable, BAMTech shortens the value chain: content → subscription app, skipping Comcast.\n\n"
            "Weaknesses: MLB ownership capped upside until spin-out; live rights are capital-intensive; rebundling risk if "
            "Disney recreates cable online. Amazon/Twitch and Netflix remain fierce on VOD — hosts surprised Amazon did not "
            "outbid Disney given video-as-fourth-pillar rhetoric."
        ),
        key_insights=[
            {
                "view": "Spin-out was value creation, not divestiture.",
                "question": "Why wait until 2015–2016 to separate BAMTech?",
                "answer": "BAM needed ~$900M scale and a partner who would let MLB keep equity. Inside the league, no stock comp "
                "and no incentive to serve competing leagues. Disney's Hearst-style minority path unlocked August 2016 "
                "capital; hosts call keeping BAM vertical inside MLB value-destructive after ~2005 flirtations with bankers.",
            },
            {
                "view": "Live sports are the last bundle glue — and the first OTT prize.",
                "question": "Why does live video matter more than VOD here?",
                "answer": "Cord-cutting threatened cable only while sports stayed linear. BAM proved games could go direct with "
                "MLB.tv; NHL and Riot deals moved BAM from vendor to network. Latency and blackout rules are product moats "
                "YouTube-style VOD never needed — the same skills HBO lacked on Thrones premiere night.",
            },
            {
                "view": "Disney bought a hedge, not just infrastructure.",
                "question": "Is BAMTech a tech acquisition or a business line?",
                "answer": "Both — white-label CDN/encoder stack plus ESPN-of-the-internet strategic option. At ~4× revenue vs "
                "software multiples, Disney paid for cable-margin replacement as ESPN affiliate fees peaked. Direct "
                "subscription relationships (MLB.tv, NHL) finally let Disney touch consumers without Comcast or Netflix "
                "taking the relationship.",
            },
            {
                "view": "Problem-solving beats visionary decks.",
                "question": "How did a baseball IT shop beat Netflix to streaming?",
                "answer": "Iterative seasonality: one Rangers–Yankees test stream, then a pennant package, then full MLB.tv in "
                "one off-season. No 'future of TV' thesis — just Ichiro fans, ticket sales, and out-of-market demand. "
                "Contrast with Oculus-style vertical/horizontal conflicts; BAMTech post-spin could serve MLB competitors.",
            },
            {
                "view": "Bundling cycles repeat.",
                "question": "Will OTT recreate the cable bundle?",
                "answer": "Hosts cite Jim Barksdale ('bundle or unbundle') — consumers wanted unbundled Netflix/MLB/League Pass "
                "until subscription fatigue. Disney may rebundle live plus library for $30–40/month. Superior UX wins "
                "either way; danger is paying for unwanted channels again, not the delivery technology BAM mastered.",
            },
        ],
        top_investment_implications=[
            {
                "ticker": "DIS",
                "direction": "Watch",
                "confidence": "Medium",
                "thesis": "BAMTech underpinned Disney+ and ESPN DTC; live rights inflation and streaming profitability determine "
                "whether the 2016 $3.5B bet matches hosts' A-grade thesis — episode predates full DTC P&L disclosure.",
            }
        ],
        golden_quotes=[
            '"The biggest media company you\'ve never heard of." — Forbes on BAMTech, cited by hosts as the episode frame.',
            '"We knew we wanted BAMTech over the long term to be not just a vendor but also a rights holder." — Robert Bowman, on owning rights not just pipes.',
            '"There are two ways to make money in business: you can unbundle or you can bundle." — Jim Barksdale (via Ben), on OTT vs cable cycles.',
        ],
        chronology={
            "subject": "MLB Advanced Media / BAMTech",
            "events": [
                {"date": "2000", "event": "MLB forms Major League Baseball Advanced Media (BAM) to centralize 30 team websites"},
                {"date": "2002", "event": "Ticketmaster pays BAM $10M upfront; same year first live video tests after audio flop"},
                {"date": "2003", "event": "MLB.tv launches at $80/season; ~100K subscribers in year one"},
                {"date": "2010", "event": "BAM powers ESPN3 — first multi-league streaming backend deal"},
                {"date": "2012", "event": "Bowman cites ~$620M BAM revenue in interview"},
                {"date": "Apr 2015", "event": "HBO Now launches on BAM after in-house Game of Thrones streaming failures"},
                {"date": "Aug 2015", "event": "MLB announces BAMTech spin-out; seeks external investors"},
                {"date": "2015", "event": "NHL deal includes equity stake; BAM shifts from vendor to rights monetizer"},
                {"date": "Aug 2016", "event": "Disney acquires one-third of BAMTech for ~$1B at $3.5B enterprise value"},
                {"date": "2016", "event": "Disney announces direct-to-consumer ESPN service powered by BAMTech"},
                {"date": "2017", "event": "Episode recorded amid ESPN layoffs and SportsCenter highlight commoditization"},
            ],
        },
    ),
    shell(
        "acq-episode-38-soundjam-itunes",
        episode_rating={"overall": 4},
        keywords=["Digital Music", "Apple Acquisition", "Platform Hub"],
        conclusion=(
            "Apple's 2000 acquisition of SoundJam MP — Jeff Robbin and Bill Kincaid's Mac MP3 player published by Casady & Greene — "
            "became iTunes and the kernel of Apple's turnaround. SoundJam solved Mac users' post-Napster problem: decode MP3s, manage "
            "libraries, and ship in boxed software (manual by David Pogue). Jobs, permanent CEO from early 2000, executed the "
            "'digital hub' strategy: iTunes (2001) then iPod — Mac-only sync that drove hardware switching. Hosts frame the deal "
            "as product/technology: brushed-metal UI, visualizers, and encoding from CDs presaged a decade of Apple software taste. "
            "SoundJam's boxed publisher model (Casady & Greene) shows how distribution once required physical channels — a contrast "
            "to the iTunes Store and streaming era that followed."
        ),
        background=(
            "David and Ben rewind to WinAmp/Napster-era piracy and the Diamond Rio — Kincaid, racing Formula cars, heard NPR on "
            "MP3s and teamed with ex-Apple engineer Robbin (Conflict Catcher) to build SoundJam MP (late 1998). Casady & Greene "
            "shrink-wrapped the product; Macworld called it the most complete Mac MP3 tool. Apple noticed; Jobs acquired the team "
            "and stripped skins for iTunes 1.0, announced at Macworld 2001 with Jobs claiming visualizers as Apple's invention.\n\n"
            "The episode ties SoundJam to ecosystem strategy: iPod as lead-gen for Mac, CD ripping, and later FairPlay/store "
            "lock-in. Competitors Audion/Panther lost to Apple's distribution and Jobs' reality distortion. Tech themes: standing "
            "on pre-API giants' shoulders, UI paradigm swings (brushed metal → Aqua → flat), and buying the best Mac client in a "
            "category about to go platform-wide."
        ),
        important_facts=[
            "SoundJam MP shipped in late 1998 via publisher Casady & Greene; David Pogue wrote the product manual before NYT fame.",
            "Apple acquired SoundJam in 2000, shortly after Steve Jobs became permanent CEO (January 2000) — first move in the music hub strategy.",
            "iTunes debuted at Macworld 2001; iPod followed in 2001 as the portable extension of the iTunes library sync model.",
            "Kincaid built Mac support for the Diamond Rio MP3 player after NPR said the hardware skipped Mac — origin of the SoundJam team-up.",
            "SoundJam popularized Apple's brushed-metal QuickTime aesthetic and bundled visualizers Jobs later demoed as novel on stage.",
        ],
        mental_model={
            "name": "Digital Hub Wedge",
            "components": (
                "Apple did not buy a record label — it bought the best Mac-side workflow for a disruptive format (MP3). iTunes "
                "made Macs the center of rip-sync-play loops; iPod extended the hub to pockets and pulled PC-curious buyers toward "
                "Macs. Each layer (software → device → store → phone) reused the same library and taste advantages. Acquiring "
                "working product plus founders beat greenfield when format shifts create temporary category winners (SoundJam on Mac). "
                "Jobs removed gimmicks (skins) but kept speed, encoding, and industrial design cues."
            ),
            "application": (
                "In platform shifts, acquire the category-leading client on your OS before someone else owns the user relationship. "
                "Hub strategies need one killer daily use case (music management) before adjacent SKUs. Founders building dev tools "
                "today: distribution moats once lived in box publishers — now in app stores; either way, owning the workflow beats "
                "owning a feature."
            ),
        },
        competitive_advantage=(
            "SoundJam won Mac MP3 management on completeness: playback, CD ripping, encoding, skins, visualizers — when Mac OS 9 "
            "had no native codecs. Post-acquisition, Apple added FairPlay, store billing, and iPod-optimized sync competitors could "
            "not match without hardware.\n\n"
            "iTunes' moat became ecosystem lock-in: library investment, device pairing, and later iPhone activation. Audion/Panther "
            "demonstrated indie alternatives; Apple's retail, keynote demos, and OS integration crowded them out. Brushed-metal UI "
            "signaled 'Pro Mac' credibility to creative users.\n\n"
            "Weaknesses: early iTunes was Mac-only; Windows iTunes arrived later under pressure. Hosts note iTunes bloat in 2017 "
            "recording — the same hub that saved Apple became a punchline. Streaming (Spotify) eventually unbundled ownership; "
            "SoundJam-era insight was format transition, not perpetual dominance of local files."
        ),
        key_insights=[
            {
                "view": "Acquisition category was product, not revenue.",
                "question": "Why buy SoundJam instead of building?",
                "answer": "Robbin/Kincaid already shipped encoding, playback, and library UX Mac users paid for in boxes. Rebuilding "
                "would miss the 2000–2001 MP3 window. Apple bought team + codebase — same playbook as later Siri/PA Semi talent buys.",
            },
            {
                "view": "Publisher middlemen once gated software.",
                "question": "Why involve Casady & Greene at all?",
                "answer": "Pre-app-store distribution required shrink-wrap and retail shelf space. Apple acquired the product team; "
                "publisher economics explain two-company names in the deal history — a reminder distribution often matters as much as code.",
            },
            {
                "view": "Music was the wedge, not the endgame.",
                "question": "How did iTunes lead to Apple's scale today?",
                "answer": "Digital hub thesis: own the PC workflow for a converging media type, then hardware (iPod), then phone with "
                "same sync DNA. iPod buyers entered Apple stores — lead-gen cheaper than broad advertising. iTunes revenue was "
                "secondary to Mac and device gross margin.",
            },
            {
                "view": "UI paradigms ship via acquisitions.",
                "question": "Why does brushed metal matter?",
                "answer": "SoundJam imported QuickTime 4's metal skin into a mainstream app — Apple then over-applied the aesthetic "
                "across Finder until Aqua moderation. Acquisitions inject taste and patterns faster than internal labs; Forstall-era "
                "skeuomorphism has similar roots.",
            },
            {
                "view": "Reality distortion is a GTM strategy.",
                "question": "Did Apple invent visualizers?",
                "answer": "WinAmp and SoundJam had them first; Jobs presented iTunes visualizers as new at Macworld 2001. Hosts treat "
                "this as narrative control — useful for employees and customers even if historians wince. Founders should document "
                "IP and credit chains before keynotes rewrite lore.",
            },
        ],
        top_investment_implications=[
            {
                "ticker": "AAPL",
                "direction": "Watch",
                "confidence": "Low",
                "thesis": "SoundJam illustrates Apple's acquire-to-seed-platform playbook (later App Store, Services). Legacy read-through "
                "only — modern Apple music economics are streaming/subscription, not iTunes downloads.",
            }
        ],
        golden_quotes=[
            '"Of all the MP3 software available for the Mac, SoundJam MP is the most complete." — Macworld review, quoted by hosts.',
            '"Wouldn\'t it be cool if you could visualize your music? Well, we\'ve done it." — Steve Jobs at Macworld 2001 (visualizers existed in SoundJam first).',
            '"Listeners who have been listening a long time — we started as Ben and me drinking beer and recording ourselves." — David on Acquired\'s early days.',
        ],
        chronology={
            "subject": "SoundJam / iTunes",
            "events": [
                {"date": "1997", "event": "Kincaid hears NPR MP3/Rio segment; starts Mac player project"},
                {"date": "1998", "event": "SoundJam MP ships via Casady & Greene with Pogue manual"},
                {"date": "Jan 2000", "event": "Steve Jobs becomes permanent Apple CEO"},
                {"date": "2000", "event": "Apple acquires SoundJam; team joins Apple"},
                {"date": "Jan 2001", "event": "iTunes announced at Macworld San Francisco"},
                {"date": "2001", "event": "iPod launches as portable extension of iTunes library"},
                {"date": "2003", "event": "iTunes Store opens — legal downloads era"},
                {"date": "2007", "event": "iPhone ships with iTunes activation/sync heritage"},
            ],
        },
    ),
    shell(
        "acq-episode-39-whole-foods-market",
        episode_rating={"overall": 3},
        keywords=["Grocery Retail", "Amazon M&A", "Marketplace Logistics"],
        conclusion=(
            "Amazon's June 16, 2017 all-cash $13.7B Whole Foods acquisition ($42/share, ~27% premium) landed as a same-day "
            "emergency pod — hosts admit thin research and speculative grades. Whole Foods grew from Austin co-op roots "
            "(John Mackey's Saferway → 1978 Clarksville merger) via roll-up of regional natural grocers, riding organic "
            "tailwinds while same-store sales slipped versus Kroger/Trader Joe's. Jana Partners' ~8.3% activist stake forced "
            "a sale process; Amazon beat Albertsons rumors. The deal connects Webvan's cautionary tale, Kiva warehouse "
            "robots (ex-Webvan, bought 2012 for ~$800M), Amazon Fresh's slow city-by-city rollout, and Instacart (Whole "
            "Foods investor) as last-mile overlay. Retail trades near ~0.25× revenue vs tech multiples — grocery margins "
            "are razor-thin; thesis is density, Prime integration, and physical pickup nodes, not headline revenue."
        ),
        background=(
            "Recorded hours after the announcement, Ben and David sketch Mackey's hippie-to-CEO arc, acquisition-driven "
            "expansion, and activist pressure amid declining comps. They triangulate Amazon's decade-long grocery obsession: "
            "Fresh (2007, Seattle-only six years), cautious post-Webvan density lessons, Amazon Go pilots, and Kiva-powered "
            "fulfillment.\n\n"
            "Instacart's thin layer on existing store inventory contrasts with Webvan's vertically integrated failure (~$1B "
            "raised, ~$5B IPO market cap on ~$400K sales, 2001 bankruptcy). Whole Foods' $15.6B annual sales vs ~$13.7B "
            "price highlights retail valuation math foreign to software listeners. Hosts debate whether Amazon buys urban "
            "real estate, customer cohorts, or a supply chain wedge — grade deferred as 'too early' hot take."
        ),
        important_facts=[
            "Amazon agreed to acquire Whole Foods for $13.7B in cash at $42/share — a ~27% premium to the prior close (announced June 16, 2017).",
            "Whole Foods reported ~$15.6B in annual sales the prior year — the deal priced near 0.9× revenue vs software-style multiples.",
            "Jana Partners built an ~8.3% stake pushing for sale; Bloomberg had reported Amazon interest before activists accelerated the process.",
            "Webvan raised nearly $1B, IPO'd near a ~$5B market cap on under ~$400K lifetime sales, and filed Chapter 11 in mid-2001.",
            "Amazon acquired Kiva Systems (~$800M, 2012); founder Mick Mountz was ex-Webvan logistics — robots bring racks to pickers.",
        ],
        mental_model={
            "name": "Density Before National Grocery",
            "components": (
                "Grocery delivery fails when growth outruns route density — Webvan's lesson Amazon internalized by keeping Fresh "
                "Seattle-only for six years. Thin-margin categories need fixed-cost leverage per metro, not land-grab capex. "
                "Instacart externalizes inventory/risk to stores; Amazon Fresh/Kiva internalize fulfillment; Whole Foods adds "
                "premium urban footprints and affluent shoppers. Activist stakes (Jana) create auction dynamics that pull "
                "strategic buyers (Amazon) back when they paused."
            ),
            "application": (
                "Evaluate retail-tech deals on unit economics per market, not TAM slides. Physical roll-ups (Whole Foods "
                "acquiring hippie markets) differ from tech roll-ups — multiples reflect 2–4% margins. For Amazon, stores "
                "are nodes for pickup, Prime Now, and data — not standalone grocers. Founders: last-mile overlays beat "
                "rebuilding cold chain until density proves out."
            ),
        },
        competitive_advantage=(
            "Whole Foods' moat was brand trust in organic/natural — 'Whole Paycheck' pricing accepted by affluent urban "
            "cohorts until Trader Joe's/Kroger organic aisles commoditized the claim. Mackey stayed CEO post-deal; culture "
            "and perishables expertise do not port to Amazon overnight.\n\n"
            "Amazon brings Prime membership, Kiva/FC automation, and willingness to price below margin for strategic "
            "lock-in. Combined thesis: capture high-LTV customers' offline grocery wallet and feed ecommerce flywheel. "
            "Instacart partnership/investment complicates exclusivity.\n\n"
            "Weaknesses: grocery is low margin; same-store declines signaled brand fatigue; hosts lacked time for confident "
            "grading. Albertsons counterfactual might have rolled up conventional grocers instead. Episode is a snapshot "
            "before Amazon scaled 365/Prime integration outcomes."
        ),
        key_insights=[
            {
                "view": "Retail multiples punish revenue-only thinking.",
                "question": "Why pay 'only' ~1× sales?",
                "answer": "Grocery nets ~2–4% margins; public chains traded ~14× P/E vs Whole Foods ~31×. Boutique retail often "
                "sells near ~0.25× revenue — Whole Foods looked expensive vs grocers, cheap vs SaaS. Amazon paid for "
                "strategic optionality, not EBITDA arbitrage.",
            },
            {
                "view": "Webvan scar tissue shaped Amazon Fresh.",
                "question": "Why did Amazon wait a decade?",
                "answer": "Webvan proved demand exists but capex ahead of density kills — ~$1B burned, 2000 layoffs. Amazon "
                "Fresh stayed Seattle six years; former Webvan talent at Amazon/Kiva applied robotics to margin, not "
                "national blitz. Whole Foods leapfrogs owned urban shelf space.",
            },
            {
                "view": "Instacart vs vertically integrated Fresh.",
                "question": "Why not keep partnering?",
                "answer": "Instacart is marketplace overlay — stores keep inventory risk; Amazon Fresh owns logistics end-to-end "
                "with Kiva. Whole Foods investment in Instacart created awkward coopetition; acquisition internalizes customer "
                "and pickup data Amazon could not fully control via app layer.",
            },
            {
                "view": "Activists manufacture auctions.",
                "question": "How did Jana extract a premium?",
                "answer": "8.3% stake plus public sale process invited Albertsons rumors and revived Amazon interest reported "
                "pre-Jana. Nothing drives price like competing bidders — even when Amazon had looked before, activists "
                "reset the clock and leverage.",
            },
            {
                "view": "Hot-take episodes age as case studies.",
                "question": "Why grade with incomplete facts?",
                "answer": "Hosts explicitly defer confident grades — value is framework transfer (density, margins, Kiva lineage) "
                "not day-one verdict. Listener takeaway: separate strategic narrative (Bezos/Machine learning stores) from "
                "financial timing (premium to declining comps).",
            },
        ],
        top_investment_implications=[
            {
                "ticker": "AMZN",
                "direction": "Watch",
                "confidence": "Low",
                "thesis": "2017 emergency-pod lens: physical grocery as Prime/delivery nodes vs low-margin drag — episode predates "
                "post-acquisition integration outcomes; use for retail-density framework, not current price target.",
            }
        ],
        golden_quotes=[
            '"Podcasting is the new groceries." — Ben, opening the emergency Whole Foods episode.',
            '"Louis Borders who is the same Louis Borders who was cofounder and CEO of the Borders Bookstore." — David linking Webvan to books/retail history.',
            '"Boutique retail actually, the general valuation for that is around a quarter of your annual sales." — Ben on retail vs tech multiples.',
        ],
        chronology={
            "subject": "Whole Foods / Amazon acquisition",
            "events": [
                {"date": "1978", "event": "Saferway merges with Clarksville Natural Grocery → Whole Foods Market"},
                {"date": "1996", "event": "Webvan founded by Louis Borders in Bay Area"},
                {"date": "1999", "event": "Webvan IPO near ~$5B market cap; ~$400K cumulative sales"},
                {"date": "2001", "event": "Webvan Chapter 11; ~2000 employees laid off"},
                {"date": "2003", "event": "Kiva Systems founded by ex-Webvan logistics lead Mick Mountz"},
                {"date": "2007", "event": "Amazon Fresh launches in Seattle only"},
                {"date": "2012", "event": "Amazon acquires Kiva Systems for ~$800M"},
                {"date": "2016", "event": "Jana Partners builds ~8.3% Whole Foods stake; pushes for sale"},
                {"date": "2017-06-16", "event": "Amazon announces $13.7B all-cash Whole Foods acquisition"},
            ],
        },
    ),
    shell(
        "acq-episode-40-activision-blizzard",
        episode_rating={"overall": 4},
        keywords=["Video Games", "Franchise IP", "Esports"],
        conclusion=(
            "The December 2007 merger combined Activision (~$11B implied, Bobby Kotick's hit-publishing machine) with "
            "Vivendi Games/Blizzard (valued ~$8.1B; WoW at ~10M subs, ~$1.1B 2007 revenue, ~$520M operating profit). "
            "Blizzard's path — Davidson & Associates ($10M, 1994) through Cendant accounting fraud, French water-utility "
            "conglomerate Vivendi, and Seagram's/Universal — stayed creatively fertile: Warcraft, StarCraft, Diablo, Battle.net, "
            "WoW's ~$1B+/year subscription peak, and mod-community births of MOBA/esports (Defense of the Ancients) without "
            "Blizzard capturing League/DOTA2 value. Post-merger: StarCraft II, Hearthstone, Overwatch (30M+ players), MLG "
            "buy, King/Candy Crush ~$5.9B. Hosts grade ~B+/A- operationally but note ~2× market cap in ~10 years vs "
            "missed MOBA/Twitch flywheel pieces."
        ),
        background=(
            "David untangles Blizzard's 'Old Testament' ownership chain while Ben maps publisher vs developer economics. "
            "Highlights: Warcraft II LAN/WAN multiplayer; Diablo item economies; 1997 Battle.net as Xbox Live precursor; "
            "StarCraft's Korean esports culture (PC bangs, TV channels); Warcraft III mod → DOTA → Riot/Valve fortunes "
            "without Blizzard IP control; WoW (2004) 12M+ peak subs at ~$12–15/month.\n\n"
            "Activision side: third-party publisher since 1979 (Call of Duty, Guitar Hero, Tony Hawk). Merger gave Vivendi "
            "~63% of combined ~$18.9B entity. 2013 buyback reduced Vivendi to ~6%; Tencent invested. 2016: consumers spent "
            "~43B hours on Activision Blizzard content — hosts compare to Netflix/Snapchat attention. Grade framework: combined "
            "enterprise value vs independent counterfactuals."
        ),
        important_facts=[
            "Blizzard's first sale: Davidson & Associates paid ~$10M in 1994; Activision Blizzard later traded near a ~$44B market cap (episode date).",
            "World of Warcraft peaked above ~12M monthly subscribers at ~$12–15/month — over ~$1B/year recurring at summit.",
            "December 2007 merger valued Vivendi Games/Blizzard at ~$8.1B; combined company ~$18.9B (~31% premium to Activision).",
            "Defense of the Ancients (2003 Warcraft III mod) spawned MOBA genre; League of Legends and DOTA2 exceed 50% of esports hours watched.",
            "2016: Blizzard segment did ~$2.4B revenue (~$1.6B in 2015); consumers spent ~43B hours on Activision Blizzard content in 2016.",
        ],
        mental_model={
            "name": "Live Service Over Box Release",
            "components": (
                "Blizzard shifted gaming from one-time SKU sales to persistent worlds, subscriptions, and cosmetic monetization — "
                "mod tools exported creativity to users (DOTA) while Battle.net owned matchmaking. WoW paused studio output "
                "2004–2010 because recurring revenue beat new IP risk. Activision contributed hit factory discipline and "
                "retail relationships; merger aligned capital-intensive MMOs with marketing scale. Esports/viewing optimization "
                "(Overwatch League ~$20M franchise fees) extends the flywheel if you own platforms — Twitch stayed with Amazon."
            ),
            "application": (
                "In hits-driven media, acquisitions that lock franchise IP plus live ops beat pure distribution deals. "
                "Ask who captures mod/community innovation — open mod policy created MOBAs but lost Riot/Valve economics. "
                "Public-market gaming exposure (ATVI) often equals Blizzard live-services beta on esports tailwinds.",
            ),
        },
        competitive_advantage=(
            "Blizzard moats: decade-long franchises (Warcraft, StarCraft, Diablo), Battle.net distribution, and subscription "
            "trust. Korean esports culture proved StarCraft's spectator value years before Western leagues. Activision adds "
            "Call of Duty annual cadence and retail marketing — complementary hit calendars.\n\n"
            "Combined entity reports Blizzard as its own segment — proof of business-line logic. Disney-like IP flywheel "
            "(Warcraft film, merch) nascent vs Overwatch/League competition. King acquisition adds mobile casual scale.\n\n"
            "Weaknesses: missed MOBA ownership; Diablo III/Hearthstone/Titan kills show Kotick capital discipline vs pure "
            "creative bets; ~2× in 10 years underwhelms vs Tencent/Riot; Amazon owns Twitch — ESPN-analog hole in esports "
            "stack. Corporate genealogy exhausted hosts but illustrates IP durability through absurd owners."
        ),
        key_insights=[
            {
                "view": "Creative studio survived absurd ownership.",
                "question": "How did Blizzard outlive Vivendi/water utilities?",
                "answer": "Warcraft/StarCraft/Diablo teams kept executing through Cendant fraud sale, Havas, Vivendi/Seagram's "
                "conglomerate rolls — franchise IP and Battle.net mattered more than balance-sheet owner. Merger with "
                "Activision finally matched gaming-native capital markets.",
            },
            {
                "view": "Mods can create categories you do not capture.",
                "question": "Why isn't Blizzard in League/DOTA2?",
                "answer": "Warcraft III editor let Eul ship Defense of the Ancients; Blizzard did not control mod IP — Riot and "
                "Valve built MOBA economics. Open-platform goodwill vs capturing trillion-hour genres — Activision merger "
                "did not retroactively fix mod licensing.",
            },
            {
                "view": "Merger traded distribution for live services.",
                "question": "Why did Activision pay ~$8B for Blizzard?",
                "answer": "WoW proved recurring revenue beats annual box hits; Activision's marketing and retail could smooth "
                "Blizzard droughts. Vivendi wanted liquidity; Kotick wanted MMO/esports exposure before MOBA wave fully "
                "shifted value to Riot/Twitch.",
            },
            {
                "view": "Attention metrics rival social apps.",
                "question": "Is gaming 'small fry'?",
                "answer": "~43B consumer hours in 2016 — ~1.5× Snapchat time per ATVI disclosure. Hardcore players log 2–8 "
                "hours/day; esports viewership still concentrated in legacy titles (League ~23%, DOTA2 ~32% Twitch hours).",
            },
            {
                "view": "Flywheel missing broadcast layer.",
                "question": "Can ATVI be Disney without ESPN?",
                "answer": "MLG buy and Overwatch League attempt vertical integration, but Amazon/Twitch owns spectator distribution "
                "— analogous to Disney without owned cable. Grade B+/A- reflects ops fit, not full platform capture.",
            },
        ],
        top_investment_implications=[
            {
                "ticker": "ATVI",
                "direction": "Watch",
                "confidence": "Medium",
                "thesis": "Episode frames ATVI as public esports/MMO proxy pre-Microsoft acquisition era — Blizzard live ops plus "
                "Call of Duty; MOBA miss and platform dependence (Twitch) cap moat vs Tencent/Riot privates.",
            }
        ],
        golden_quotes=[
            '"You get a car. You get a car." — Oprah (mis-invoked joke in transcript); hosts compare WoW subscription scale instead.',
            '"Everything linear dies, everything on-demand wins." — Barry McCarthy analogy cited in other episodes; here hosts on live-service games.',
            '"This is literally like the Old Testament." — Ben on Blizzard\'s conglomerate genealogy.',
        ],
        chronology={
            "subject": "Blizzard / Activision Blizzard merger",
            "events": [
                {"date": "1994", "event": "Davidson & Associates acquires Blizzard for ~$10M"},
                {"date": "1996", "event": "Warcraft II; CUC/HFS merger forms Cendant"},
                {"date": "1997", "event": "Battle.net launches; Cendant accounting scandal"},
                {"date": "1998", "event": "Blizzard sold to Havas → Vivendi (ex-French water utility)"},
                {"date": "2002", "event": "Warcraft III ships with campaign editor enabling mods"},
                {"date": "2003", "event": "Defense of the Ancients mod popularizes MOBA genre"},
                {"date": "2004", "event": "World of Warcraft launches; subscription MMO peak begins"},
                {"date": "2007-12", "event": "Activision–Vivendi Games merger announced"},
                {"date": "2013", "event": "Buyback reduces Vivendi stake; Tencent invests"},
                {"date": "2015", "event": "Heroes of the Storm; esports infrastructure builds"},
                {"date": "2016", "event": "Overwatch launch; Major League Gaming acquired"},
                {"date": "2016", "event": "King (Candy Crush) acquired for ~$5.9B"},
            ],
        },
    ),
]

from scripts._write_acq_batch_ep37_44_bodies import EPISODES_41_44  # noqa: E402

EPISODES.extend(EPISODES_41_44)

if __name__ == "__main__":
    out = ROOT / "data" / "approved"
    tmpl = load_template_config(template_path_for_podcast("Acquired"))
    results = []
    for ep in EPISODES:
        path = out / f"{ep['episode_id']}.json"
        path.write_text(json.dumps(ep, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
        report = validate_summary(ep, tmpl)
        status = "PASS" if report.passed else "FAIL"
        results.append((ep["episode_id"], status, report.total_words, report.passed, report.issues))
        print(f"{ep['episode_id']}: {status} words={report.total_words} [{report.min_total_words}-{report.max_total_words}]")
        for issue in report.issues:
            print(f"  [{issue.severity}] {issue.section}: {issue.message}")
    failed = [r for r in results if not r[3]]
    print(f"\nCompleted: {len(results) - len(failed)}/{len(results)}  Failed: {len(failed)}")
    sys.exit(1 if failed else 0)
