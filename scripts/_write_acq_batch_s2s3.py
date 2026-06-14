#!/usr/bin/env python3
"""Write Acquired v5.1 summaries for Season 2–3 batch (7 episodes)."""
from __future__ import annotations

import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))
sys.path.insert(0, str(ROOT / "scripts"))

from _write_acq_batch_491_500_common import base  # noqa: E402
from src.template_config import template_path_for_podcast  # noqa: E402
from src.validate import load_template_config, validate_summary  # noqa: E402

APPROVED = ROOT / "data" / "approved"
TMPL = load_template_config(template_path_for_podcast("Acquired"))

EPISODES: dict[str, dict] = {}

# --- Sonos IPO ---
EPISODES["acq-season-3-episode-3the-sonos-ipo"] = base(
    "acq-season-3-episode-3the-sonos-ipo",
    episode_rating={"overall": 3},
    keywords=["Home Audio", "Hardware IPO", "Platform Risk"],
    conclusion=(
        "Ben and David trace Sonos from 2002 Santa Barbara wireless-audio pioneer through its August 2018 IPO — "
        "priced at $15 (below the $17–19 range), raising ~$208M on ~$992M FY2017 revenue and 61% gross margins, "
        "yet still unprofitable on a GAAP basis. The bull case is a premium, multi-room software layer with "
        "100+ streaming integrations and loyal households; the bear case is Apple, Amazon, and Google subsidizing "
        "smart speakers that commoditize hardware while controlling voice assistants. Sonos sued Google over patent "
        "infringement shortly after the episode aired. The IPO narrative is classic Acquired: a beloved product "
        "company hitting public markets just as platform giants turn its category into a loss-leader feature."
    ),
    background=(
        "Season 3 Episode 3 covers Sonos end-to-end: founders John MacFarlane, Craig Shelburne, Tom Cullen, and "
        "Trung Mai building networked speakers when Wi‑Fi was immature, through the 2000s premium retail expansion, "
        "partnerships with every major music service, and the 2018 IPO filing during peak smart-speaker hype.\n\n"
        "Hosts contrast Sonos's open, multi-service architecture with Apple HomePod, Amazon Echo, and Google Home — "
        "each giant willing to sell hardware near cost to own the voice OS. They walk S-1 metrics (revenue growth, "
        "margins, losses), product line evolution (Play:1 through Beam and Amp), and why Wall Street punished the "
        "stock on day one despite strong brand NPS. The episode is a hardware IPO case study at the moment "
        "software platforms invade the living room."
    ),
    important_facts=[
        "Sonos IPO priced at $15/share on August 1, 2018 — below the marketed $17–19 range — raising ~$208M; "
        "shares opened ~$19.40 but fell ~13% on the first day as Apple HomePod competition dominated headlines.",
        "FY2017 revenue was ~$992.5M (up from ~$468M in 2013); gross margin ~61% — premium hardware economics — "
        "but the company remained GAAP unprofitable with ~$178M net loss in FY2017 due to R&D and growth spend.",
        "Sonos integrated 100+ streaming services (Spotify, Apple Music, Pandora, etc.) via software — a deliberate "
        "agnostic platform play versus single-ecosystem speakers from Apple or Amazon Alexa.",
        "Smart-speaker market share data cited in the episode: Amazon Echo ~70%+ of US unit share by 2018, "
        "Google Home growing fast — compressing Sonos's addressable market from below on price.",
        "Founders retained significant control via dual-class structure; John MacFarlane stepped down as CEO in "
        "2017 (replaced by Patrick Spence) but remained executive chairman through the IPO transition.",
    ],
    mental_model={
        "name": "Open Platform vs Subsidized Walled Garden",
        "components": (
            "Sonos bet that audiophile households want best-in-class sound plus service neutrality — one app "
            "controlling every streaming source. Apple, Amazon, and Google bet voice assistants and retail flywheels "
            "justify selling speakers at or below cost, capturing data, commerce, and subscription lock-in. When "
            "platform owners also control OS defaults (Siri, Alexa, Google Assistant), neutral hardware becomes "
            "a feature, not a category. Gross margins above 60% do not protect you if giants price at 0% margin "
            "and your product requires their cooperation (Spotify on HomePod delays, Google patent disputes)."
        ),
        "application": (
            "Evaluate hardware startups by asking who captures the software margin above the device. If answer is "
            "Apple/Amazon/Google, IPO multiples should discount platform risk even with great NPS. Sonos-like "
            "companies need either regulatory intervention (patent suits, antitrust), a killer proprietary layer "
            "(Trueplay tuning, multi-room sync), or pivot to services revenue — Sonos eventually added subscriptions "
            "post-episode. Investors should map each giant's incentive to clone versus partner."
        ),
    },
    competitive_advantage=(
        "Sonos's moat was experiential, not structural: synchronized multi-room audio, Trueplay room tuning, and "
        "a decade of brand trust with affluent homeowners and custom installers. Software updates extended hardware "
        "life — a rare consumer-electronics virtue. Partnership breadth (100+ services) meant Sonos was the "
        "Switzerland of streaming before smart speakers existed.\n\n"
        "Retail presence in Apple Stores, Best Buy, and premium audio dealers reinforced premium positioning versus "
        "$49 Echo Dots. Professional installer channel created switching costs in whole-home deployments. "
        "Acquired hosts note Sonos customers often owned 3+ devices — ecosystem depth within the home.\n\n"
        "Weaknesses were obvious by 2018: no owned voice OS, dependence on Apple/Google for mobile control apps, "
        "and giants subsidizing 'good enough' audio. HomePod's delayed Spotify support still threatened because "
        "Apple users default to Apple hardware. Patent litigation against Google (2018–2020) was defensive, not "
        "offensive growth. Public-market investors saw a hardware OEM in a software-platform war.\n\n"
        "Versus Bose: similar premium audio but Sonos won on network effects in the home. Versus Amazon: "
        "Sonos sound quality and openness vs Alexa convenience and price. Post-IPO, Sonos leaned into home-theater "
        "soundbars (Beam, Arc) where smart-speaker substitutes matter less — a niche-up strategy Acquired would "
        "later recognize in other episodes."
    ),
    key_insights=[
        {
            "view": "Premium hardware IPOs face platform-timing risk.",
            "question": "Why did Sonos stock fall despite a 'successful' IPO?",
            "answer": (
                "The $15 pricing (below range) signaled weak banker demand. First-day pop to ~$19.40 looked fine, "
                "but Apple HomePod launch narrative and Echo dominance (~70% share) reframed Sonos as a feature "
                "vendor, not a platform. Public investors pay for TAM expansion; smart speakers looked like a "
                "winner-take-most market owned by subsidized giants. Sonos's 61% gross margin was impressive for "
                "hardware but irrelevant if unit growth stalled."
            ),
        },
        {
            "view": "Service neutrality was Sonos's strategic wedge — until voice.",
            "question": "Why integrate 100+ streaming apps?",
            "answer": (
                "Early Sonos solved a real pain: one controller for Pandora, Spotify, NAS libraries, and radio. "
                "Neutrality attracted audiophiles locked across ecosystems. Voice assistants inverted the stack: "
                "the OS became the aggregator, not the speaker firmware. Once users said 'Alexa, play X,' Sonos's "
                "integration depth mattered less than mic presence. The episode previews patent fights when "
                "Google allegedly copied multi-room tech."
            ),
        },
        {
            "view": "Revenue scale without profits is tolerable pre-IPO, punished after.",
            "question": "How did S-1 financials tell two stories?",
            "answer": (
                "Revenue nearly doubled from ~$468M (2013) to ~$992M (2017) — a growth story. Yet ~$178M net loss "
                "in FY2017 showed the cost of staying ahead on R&D and marketing against zero-margin competitors. "
                "Acquired walks through why hardware companies go public anyway: liquidity for investors, currency "
                "for M&A, and brand validation — even when GAAP earnings are years away."
            ),
        },
        {
            "view": "Founder transitions before IPO are governance signals.",
            "question": "Why did MacFarlane step down as CEO in 2017?",
            "answer": (
                "MacFarlane moved to executive chairman; Patrick Spence (ex-Apple, RIM) became CEO ahead of the "
                "2018 filing. Pattern: product-founder to operator-CEO before public scrutiny. Dual-class shares "
                "kept founder control — common in consumer tech IPOs of the era (Snap, Dropbox). Hosts note "
                "investors accept control premiums when growth remains strong."
            ),
        },
        {
            "view": "Custom installer channel is underrated moat — until mass-market price war.",
            "question": "Who were Sonos's early adopters?",
            "answer": (
                "Affluent homeowners and AV integrators wiring whole-home audio in the 2000s–2010s. High NPS and "
                "3+ device households created word-of-mouth in zip codes Echo later penetrated from the kitchen "
                "counter. Installer relationships added switching costs (in-wall wiring, Sonos Amp). Mass-market "
                "smart speakers skipped installers entirely — $49 impulse purchase vs $499 Play:5."
            ),
        },
    ],
    top_investment_implications=[
        {
            "ticker": "SONO",
            "direction": "Watch",
            "confidence": "Medium",
            "thesis": (
                "Episode frames Sonos as premium open-audio play in a subsidized smart-speaker war — useful for "
                "assessing whether soundbar/home-theater pivot and subscription layer can offset platform risk."
            ),
        },
    ],
    golden_quotes=[
        "\"Sonos is Switzerland for music services\" — hosts on the 100+ integration strategy versus walled-garden speakers.",
        "\"Apple doesn't need to make money on HomePod\" — David on why platform owners price hardware as a feature.",
        "\"They priced the IPO at $15 — below the range\" — on banker caution entering a HomePod/Echo news cycle.",
    ],
    chronology={
        "subject": "Sonos",
        "events": [
            {"date": "2002", "event": "Sonos founded in Santa Barbara — wireless multi-room audio vision"},
            {"date": "2005", "event": "First products ship — ZP100 amplifier and CR100 controller"},
            {"date": "2009–2012", "event": "Play series launches; streaming partnerships expand"},
            {"date": "2013", "event": "Revenue ~$468M — baseline for IPO-era growth narrative"},
            {"date": "2017", "event": "MacFarlane steps down as CEO; Patrick Spence appointed"},
            {"date": "2017", "event": "Apple announces HomePod; smart-speaker platform war accelerates"},
            {"date": "2018-07", "event": "S-1 filed; FY2017 revenue ~$992M, ~61% gross margin"},
            {"date": "2018-08-01", "event": "IPO prices at $15/share, raises ~$208M"},
            {"date": "2018-08-02", "event": "First trading day — shares fall ~13% on platform competition fears"},
            {"date": "2018-08", "event": "Sonos files patent suit against Google over multi-room technology"},
        ],
    },
    review_notes="Manual GPT Acquired batch — v5.1-acquired; Season 2–3 batch",
)

# --- Xiaomi IPO ---
EPISODES["acq-season-3-episode-2the-xiaomi-ipo"] = base(
    "acq-season-3-episode-2the-xiaomi-ipo",
    episode_rating={"overall": 4},
    keywords=["China Tech", "Hardware Margin", "Triathlon Model"],
    conclusion=(
        "Ben and David decode Xiaomi's July 2018 Hong Kong IPO — ~$54B valuation on ~$18B 2017 revenue — as Lei Jun's "
        "deliberate inversion of Apple: ~5% hardware net margins, internet services and IoT for profit, and "
        "100M+ phone shipments at ASPs a fraction of iPhone. The 'triathlon' (hardware + internet services + new "
        "retail) targets 20% of China's population as fans, not customers. MIUI's 300M+ MAUs monetize via ads and "
        "app store; 90+ IoT SKUs extend the ecosystem. Hosts debate whether thin-margin scale is durable or a "
        "race-to-bottom when Huawei/Oppo/Vivo compete on price. The IPO opened ~flat — skepticism about services "
        "profit and US-China risk — but the episode remains the clearest primer on China's hardware-as-channel model."
    ),
    background=(
        "Season 3 Episode 2 walks Xiaomi from Lei Jun's 2010 founding (ex-Kingsoft, ex-Google China talent) through "
        "the flash-sale growth era, MIUI Android skin, IoT expansion, and the long-delayed Hong Kong listing.\n\n"
        "Acquired contrasts Apple (70%+ gross margin hardware, services attach) with Xiaomi's ~5% hardware net margin "
        "promise to users — making money on MIUI ads, fintech, and cloud services instead. They cover the 90+ product "
        "categories (phones, scooters, rice cookers, TVs), Mi Home retail stores, and why Lei Jun calls fans 'Mi Fans.' "
        "IPO mechanics: dual-primary listing concerns, valuation haircut from earlier private rounds, and first-day "
        "trading that disappointed bulls expecting a pop."
    ),
    important_facts=[
        "Xiaomi IPO July 9, 2018 in Hong Kong valued the company at ~$54B; 2017 revenue ~$18B with ~100M+ smartphones "
        "shipped — largest Chinese smartphone IPO of the era.",
        "Lei Jun publicly caps hardware net margin at ~5% — profits intended from internet services (ads, app store, "
        "fintech) and IoT; MIUI reported 300M+ monthly active users at IPO time.",
        "Xiaomi sells products across 90+ hardware categories beyond phones — TVs, fitness bands, rice cookers, "
        "scooters — leveraging shared supply chain and Mi Fan community for cross-sell.",
        "Smartphone ASP ~$224 vs iPhone ASP ~$700+ in the episode's comparison — Xiaomi wins on volume and "
        "China/India share, not premium margin per unit.",
        "First-day trading: shares opened ~flat to slightly down versus IPO price — unusual for hot Chinese tech "
        "listings; investors questioned services profitability and trade-war overhang.",
    ],
    mental_model={
        "name": "Hardware as Distribution (Triathlon Model)",
        "components": (
            "Lei Jun's triathlon: (1) hardware sold near cost to acquire users, (2) internet services monetize the "
            "installed base via MIUI ads, app store take rate, and financial services, (3) new retail (Mi Home) "
            "provides experiential upsell for IoT SKUs. Unlike Apple, Xiaomi does not rely on 60%+ hardware margin — "
            "it relies on frequency of touchpoints across 90+ categories. Community ('Mi Fans') lowers CAC via "
            "flash sales and social hype. Risk: Oppo/Vivo/Huawei copy price strategy; services margin must scale "
            "faster than hardware commoditizes."
        ),
        "application": (
            "When analyzing consumer hardware in emerging markets, separate unit economics from ecosystem LTV. "
            "Xiaomi-like models work if software MAUs and ARPU grow while BOM costs fall via scale. If services "
            "stay <10% of revenue (true at IPO), public markets apply handset multiples — the bet is optionality. "
            "Compare to Amazon Fire tablets: subsidized hardware, profit elsewhere."
        ),
    },
    competitive_advantage=(
        "Xiaomi's edge is supply-chain velocity and community-led demand at China scale. Lei Jun recruited ex-Google "
        "and Kingsoft engineers; MIUI iterated weekly when OEMs shipped yearly. Flash-sale scarcity drove organic "
        "marketing — CAC near zero at peak hype. Vertical integration with Foxconn-class partners kept BOM low.\n\n"
        "IoT breadth creates household lock-in: Mi Band, air purifier, router, TV share Mi Home app — data flywheel "
        "for cross-sell. Mi Home stores (targeting thousands globally) mimic Apple retail at 1/10 the ASP. India "
        "expansion (#1 or #2 share in periods post-episode) proved model exports beyond China.\n\n"
        "Weaknesses: 5% margin cap is a promise, not a law — competitive pressure can force losses. US market "
        "largely closed (politics, IP). Services revenue mix was still small at IPO — bulls bet on future, bears "
        "saw low-margin handset OEM. Huawei's rise (later sanctions) showed national-champion risk. IP controversy "
        "('Apple of China' design echoes) lingered in Western press.\n\n"
        "Versus Apple: Xiaomi wins on price and SKUs; Apple wins on margin and brand prestige. Versus Samsung: "
        "similar scale play but Xiaomi's internet-native ops faster. Post-IPO, EV entry (2021+) extends triathlon "
        "to cars — logical if you believe hardware is just user acquisition."
    ),
    key_insights=[
        {
            "view": "5% hardware margin is a feature, not a bug.",
            "question": "Why would Lei Jun cap margins publicly?",
            "answer": (
                "Trust with Mi Fans: Xiaomi positions as consumer ally against fat-margin incumbents. Low hardware "
                "margin forces scale — 100M+ phones — to matter. Profit must come from MIUI ads, app store, fintech, "
                "and IoT attach. Acquired compares to Costco's markup discipline: constraint as strategy. "
                "Investors must believe services ARPU rises as MAUs grow past 300M."
            ),
        },
        {
            "view": "MIUI is the real product; phones are the shipping container.",
            "question": "Why skin Android so aggressively?",
            "answer": (
                "Weekly updates, built-in app store, ads, and cloud services keep users in Xiaomi's P&L. 300M+ MAUs "
                "at IPO mirror Facebook's emerging-market playbook — monetize attention, not BOM. Hardware refreshes "
                "bring users back; MIUI retains them. This inverts Apple's model where iOS monetizes premium hardware."
            ),
        },
        {
            "view": "90+ categories is ecosystem defense against phone commoditization.",
            "question": "Why sell rice cookers and scooters?",
            "answer": (
                "Shared supply chain and brand let Xiaomi capture wallet share in the connected home before "
                "Alibaba/Tencent own the user entirely. Each SKU feeds Mi Home data and cross-sell. Low ASP items "
                "train purchase habit — flash-sale culture extends beyond phones. Bears say distraction; bulls say "
                "Amazon-like everything-store logic."
            ),
        },
        {
            "view": "Hong Kong IPO flat open signaled skepticism, not failure.",
            "question": "Why no first-day pop?",
            "answer": (
                "~$54B valuation already priced growth; US-China trade tensions (2018) hurt sentiment. Services "
                "profitability unproven at scale — hardware still >80% of revenue. Flat open forced discipline on "
                "Lei Jun's narrative versus private-round hype. Acquired notes Chinese IPO pops are cultural; "
                "Xiaomi's restraint matched 'efficient market' framing hosts prefer."
            ),
        },
        {
            "view": "India expansion proved exportability.",
            "question": "Does triathlon work outside China?",
            "answer": (
                "Xiaomi reached #1 smartphone share in India (~2017–2018 periods cited) with same low-margin, "
                "high-volume playbook. Online-first flash sales translated; Mi Fan community replicated on social. "
                "Western markets harder — carrier channels and Apple brand moat. Episode frames Xiaomi as "
                "emerging-market champion more than global Apple killer."
            ),
        },
    ],
    top_investment_implications=[
        {
            "ticker": "1810.HK",
            "direction": "Watch",
            "confidence": "Low",
            "thesis": (
                "Triathlon model only works if services/IoT mix rises above handset dependence — episode useful "
                "framework for tracking MIUI monetization and margin-cap discipline over cycles."
            ),
        },
    ],
    golden_quotes=[
        "\"Hardware net margin will never exceed 5%\" — Lei Jun's public promise, central to the triathlon model.",
        "\"They're not selling phones — they're shipping MIUI\" — hosts reframing Xiaomi's core product.",
        "\"The triathlon: hardware, internet services, and new retail\" — Lei Jun's three-pillar strategy label.",
    ],
    chronology={
        "subject": "Xiaomi",
        "events": [
            {"date": "2010", "event": "Xiaomi founded by Lei Jun and team — MIUI Android skin first"},
            {"date": "2011", "event": "First smartphone launch — flash-sale distribution model"},
            {"date": "2014", "event": "Becomes China's #1 smartphone vendor by shipments (periodic rankings)"},
            {"date": "2016–2017", "event": "IoT expansion to 90+ categories; Mi Home retail rollout"},
            {"date": "2017", "event": "Revenue ~$18B; 100M+ phones shipped in 2017"},
            {"date": "2018-05", "event": "Hong Kong IPO prospectus filed — triathlon narrative formalized"},
            {"date": "2018-07-09", "event": "IPO lists in Hong Kong at ~$54B valuation"},
            {"date": "2018-07-09", "event": "First-day trading flat — services-profit skepticism"},
            {"date": "2018", "event": "India market share leadership validates export model"},
            {"date": "2018", "event": "MIUI 300M+ MAUs cited as services monetization base"},
        ],
    },
    review_notes="Manual GPT Acquired batch — v5.1-acquired; Season 2–3 batch",
)

# --- Rover-DogVacay ---
EPISODES["acq-season-2-episode-10the-rover-dogvacay-merger-with-rover-ceo-aaron-easterly"] = base(
    "acq-season-2-episode-10the-rover-dogvacay-merger-with-rover-ceo-aaron-easterly",
    episode_rating={"overall": 3},
    keywords=["Marketplace M&A", "Pet Economy", "Network Effects"],
    conclusion=(
        "Aaron Easterly joins Ben and David to dissect the 2017 Rover–DogVacay merger — combining the #1 and #2 US "
        "pet-sitting marketplaces after burning ~$100M+ collectively in a winner-take-most race. Rover (Seattle, 2011) "
        "and DogVacay (SF, 2012) had nearly identical models: ~20% take rate, supply-constrained sitter networks, "
        "and insurance/trust layers. Easterly argues consolidation was inevitable — dual national sales forces "
        "funding customer acquisition for the same host-side liquidity pool. Post-merger: ~$125M raised, path to "
        "profitability via reduced CAC, expansion into dog walking and grooming. The episode is Acquired's clearest "
        "marketplace merge playbook — when duopoly economics destroy venture returns unless one cap table wins."
    ),
    background=(
        "Season 2 Episode 10 is an interview format with Rover CEO Aaron Easterly, walking the merger rationale "
        "months after close. Ben and David frame pet services as a ~$70B+ US market still offline — fragmented "
        "kennels and word-of-mouth — ripe for marketplace aggregation.\n\n"
        "Both companies raised significant venture capital (Rover from Foundry, Menlo, etc.; DogVacay from Benchmark, "
        "First Round) and competed city-by-city on sitter supply. Easterly explains due diligence, cultural integration, "
        "brand retention (Rover name won), and why 'grow into profitability' failed when two well-funded players "
        "fought for the same hosts. Hosts draw Airbnb parallels — supply-side liquidity is the moat."
    ),
    important_facts=[
        "Rover and DogVacay merged in 2017; combined entity kept Rover brand — together they had raised ~$100M+ "
        "pre-merger across both cap tables before additional post-merger funding.",
        "Marketplace take rate ~20% on bookings — standard for managed marketplaces with insurance and vetting layers.",
        "US pet industry spending ~$70B+ annually (2018 figures cited) — majority still offline kennels and informal "
        "referrals, implying long runway for online penetration.",
        "Rover founded 2011 Seattle (Aaron Easterly, Greg Gottesman); DogVacay founded 2012 San Francisco (Aaron "
        "Hirschhorn) — parallel trajectories with near-identical product.",
        "Post-merger Rover raised ~$125M total at various stages — Easterly cites reduced duplicate CAC as primary "
        "synergy: one national sales team buying supply instead of two bidding up Google/Facebook keywords.",
    ],
    mental_model={
        "name": "Duopoly Burn in Winner-Take-Most Markets",
        "components": (
            "Two-sided marketplaces with local network effects often produce #1 and #2 players separated by "
            "fundraising, not product. When both raise $50M+, they subsidize the same sitters and pet owners — "
            "CAC arms race without differentiated supply. Merger captures liquidity benefits (more sitters per search) "
            "and cuts duplicate opex. Alternative is years of losses until one starves — Easterly chose combine. "
            "Key metric: supply density per zip code, not national brand awareness."
        ),
        "application": (
            "When evaluating competing marketplaces, ask if merge is cheaper than continued CAC war. Due diligence "
            "focus: host overlap by city, take-rate parity, insurance liabilities, and brand NPS. Investors in #2 "
            "should model acquihire/merge probability, not independent IPO. Post-merger, expansion SKUs (walking, "
            "grooming) reuse same supply — classic Uber Eats playbook."
        ),
    },
    competitive_advantage=(
        "Rover's moat post-merger is supply density and trust infrastructure: background checks, $25K vet guarantee, "
        "24/7 support, and review systems that offline kennels cannot match at scale. Pet owners repeat annually; "
        "LTV rises with multi-pet households. Sitter side: incremental income gig — Rover provides demand they cannot "
        "self-market.\n\n"
        "National brand after merger eliminates 'which app has sitters in my city?' friction. SEO and partnerships "
        "(PetSmart investments later) extend distribution. Data on pet preferences enables upsell to walking, "
        "daycare, and grooming — higher frequency than overnight boarding alone.\n\n"
        "Weaknesses: low-frequency use (vacations, weekends) vs daily ride-hail — harder habit loop. Wag and "
        "local sitters compete on walking; offline neighbors still win on trust for many owners. Take rate capped "
        "~20% before sitters defect to off-platform repeat. Insurance claims and incident PR are existential tail "
        "risks.\n\n"
        "Versus Airbnb: pets add liability layer; supply is more regulated emotionally. Versus offline kennels: "
        "Rover wins on convenience and price transparency; kennels win on professional facility trust. Merger "
        "removed the only other scaled national competitor — classic roll-up logic."
    ),
    key_insights=[
        {
            "view": "Merger was economics, not desperation.",
            "question": "Why combine instead of fighting to the death?",
            "answer": (
                "Both companies were supply-constrained — doubling spend did not double sitters in a city. Duplicate "
                "national sales teams (~100M+ combined burn) bought the same Google keywords. Easterly frames merger "
                "as rational VC outcome: one liquidity pool, one cap table, faster path to breakeven. Hosts compare "
                "to if Uber and Lyft merged in 2016 — saved billions in CAC."
            ),
        },
        {
            "view": "Trust products are the real margin driver.",
            "question": "Why not just Craigslist for pets?",
            "answer": (
                "Insurance ($25K guarantee), background checks, and 24/7 vet hotline justify 20% take rate. "
                "Pet owners pay premium for peace of mind leaving family members. Offline kennels charge similar "
                "all-in but lack discovery and reviews. Marketplace value is risk underwriting + reputation, not "
                "the listing UI."
            ),
        },
        {
            "view": "Supply-side liquidity is local, not national.",
            "question": "What metric actually mattered?",
            "answer": (
                "Sitters available within 5 miles of searcher — national TV brand irrelevant if Austin has supply "
                "and Dallas does not. City-by-city launch playbook mirrored Uber early days. Merger instantly doubled "
                "supply in overlapping metros — Easterly cites this as day-one synergy, not cost cuts alone."
            ),
        },
        {
            "view": "Category expansion reuses acquired supply.",
            "question": "What's after overnight sitting?",
            "answer": (
                "Dog walking (daily frequency), daycare, grooming — same sitter profile, higher utilization. "
                "Lower AOV but more transactions per year improves LTV/CAC. Wag competed on walking first; "
                "Rover post-merger could cross-sell to existing hosts without new supply acquisition."
            ),
        },
        {
            "view": "Pet spend is recession-resilient but venture-scale is hard.",
            "question": "Is this a venture outcome or lifestyle business?",
            "answer": (
                "$70B TAM sounds large but fragmented and offline-heavy. Take rate and frequency cap revenue per "
                "user vs ride-hail. Easterly argues winner-take-most within online slice justifies scale; hosts "
                "note IPO path required merger first — independent DogVacay/Rover IPO unlikely at burn rates."
            ),
        },
    ],
    top_investment_implications=[
        {
            "ticker": "Private",
            "direction": "Watch",
            "confidence": "Low",
            "thesis": (
                "Rover eventually SPAC'd (2021) — episode merger logic explains why duopoly pet marketplaces "
                "consolidate before public markets; monitor take-rate and walking attach for unit economics."
            ),
        },
    ],
    golden_quotes=[
        "\"We were both spending money to acquire the same sitters\" — Easterly on duplicate CAC driving merger logic.",
        "\"This is a winner-take-most market\" — on why #1 and #2 could not coexist profitably at scale.",
        "\"Pets are family — trust is the product\" — on insurance and vetting justifying 20% take rate.",
    ],
    chronology={
        "subject": "Rover · DogVacay",
        "events": [
            {"date": "2011", "event": "Rover founded in Seattle — peer-to-peer dog boarding marketplace"},
            {"date": "2012", "event": "DogVacay founded in San Francisco — parallel model"},
            {"date": "2013–2016", "event": "Both raise venture rounds; city-by-city supply land grab"},
            {"date": "2016", "event": "Combined burn ~$100M+ as #1 and #2 compete nationally"},
            {"date": "2017", "event": "Merger announced and closed — Rover brand survives"},
            {"date": "2017", "event": "Post-merger funding brings total raised to ~$125M+ range"},
            {"date": "2018", "event": "Acquired interview with Easterly on integration and synergies"},
            {"date": "2018", "event": "Expansion into dog walking and grooming SKUs"},
            {"date": "2019", "event": "PetSmart strategic investment deepens retail distribution"},
            {"date": "2021", "event": "Rover SPAC merger (post-episode) — public listing path completes"},
        ],
    },
    review_notes="Manual GPT Acquired batch — v5.1-acquired; Season 2–3 batch",
)

# --- T-Mobile / Sprint ---
EPISODES["acq-season-2-episode-8t-mobile-sprint"] = base(
    "acq-season-2-episode-8t-mobile-sprint",
    episode_rating={"overall": 4},
    keywords=["Telecom M&A", "Spectrum Assets", "Uncarrier Strategy"],
    conclusion=(
        "Ben and David analyze T-Mobile's $26B all-stock bid for Sprint (announced April 2018) — combining the #3 "
        "and #4 US carriers into a ~$146B enterprise value challenger to Verizon and AT&T. John Legere's Uncarrier "
        "strategy (2012–2018) added 40M+ customers by eliminating contracts and shaming incumbents; Sprint brought "
        "2.5GHz spectrum critical for 5G but SoftBank-owned dysfunction and ~$32B debt. Hosts walk 120 years of "
        "telecom consolidation from Bell System breakup to today — every merger faces DOJ/FCC scrutiny because "
        "spectrum is finite. Deal closed 2020 after years of regulatory theater. Episode frames wireless as "
        "infrastructure oligopoly where scale, not innovation, wins."
    ),
    background=(
        "Season 2 Episode 8 is a classic Acquired deep history: Sprint's origin as Brown Telephone Company (1899), "
        "MCI competition, Nextel merger, SoftBank's 2013 acquisition for ~$21.6B, and T-Mobile's metamorphosis under "
        "Deutsche Telekom and CEO Legere.\n\n"
        "The 2018 merger thesis: only four national carriers could become three viable 5G builders — T-Mobile's "
        "marketing prowess plus Sprint's mid-band spectrum beats Verizon/AT&T capex alone. Hosts explain spectrum "
        "auctions, MVNO economics, and why Dish was floated as fourth competitor to satisfy regulators. Political "
        "timeline (Trump admin vs later Biden review) previewed years of uncertainty."
    ),
    important_facts=[
        "April 29, 2018: T-Mobile announces $26B all-stock merger with Sprint — combined ~$146B enterprise value; "
        "T-Mobile shareholders ~63%, Sprint ~37% of newco.",
        "John Legere's Uncarrier (2012 launch) added 40M+ net customers by eliminating service contracts, offering "
        "device financing, and aggressive pricing — T-Mobile passed Sprint for #3 spot.",
        "SoftBank acquired Sprint in 2013 for ~$21.6B; Masayoshi Son viewed Sprint as US beachhead for global "
        "strategy — integration struggles and debt load persisted.",
        "Sprint's 2.5GHz spectrum holdings cited as primary strategic asset for 5G deployment — mid-band 'goldilocks' "
        "coverage vs mmWave.",
        "US wireless HHI and four-player market structure — DOJ blocked AT&T/T-Mobile merger in 2011; regulators "
        "demanded Dish as fourth carrier and MVNO concessions in final 2020 approval.",
    ],
    mental_model={
        "name": "Spectrum Scale Oligopoly",
        "components": (
            "Wireless is capital-intensive natural oligopoly: finite licensed spectrum, tower density economics, "
            "and device ecosystem lock-in. Four national players are one too many for stable ROI — mergers reduce "
            "competition but enable 5G capex spread across larger subscriber base. Uncarrier proved marketing can "
            "shift share without owning best network — but 5G requires spectrum depth Sprint had and T-Mobile "
            "needed. SoftBank's Sprint ownership added governance debt and urgency to sell."
        ),
        "application": (
            "Telecom M&A analysis starts with spectrum maps, not brand. Mid-band (2.5GHz) trumps marketing in "
            "5G era — explains why T-Mobile wanted Sprint despite weaker financials. Regulators trade competition "
            "count for infrastructure promises — model Dish as structural remedy, not real challenger. Investors: "
            "post-merger TMUS became #2 by subscribers — episode predicted scale wins over Legere theatrics long-term."
        ),
    },
    competitive_advantage=(
        "T-Mobile's Uncarrier brand broke industry norms — no contracts, transparent pricing, CEO Twitter persona — "
        "acquiring price-sensitive and urban millennials. Network investment lagged Verizon but 'good enough' LTE "
        "plus marketing closed gap. MetroPCS acquisition (2013) added prepaid scale.\n\n"
        "Sprint's advantage was spectrum, not operations — 2.5GHz holdings for 5G, but network quality ranked last "
        "in many markets. SoftBank capital funded losses but culture clash stalled turnaround. Combined entity "
        "promises best mid-band 5G footprint in US — structural advantage Verizon/AT&T must match via auction spend.\n\n"
        "Weaknesses: integration risk (Nextel/Sprint history of failed tech merges), regulatory delay cost synergies, "
        "Dish fourth-carrier remedy may be paper competitor. Post-Legere T-Mobile faces brand cooling. Cable MVNOs "
        "(Comcast, Charter) add pricing pressure on fringes.\n\n"
        "Versus Verizon: premium network and enterprise; T-Mobile wins on consumer value post-merger with spectrum "
        "depth. Versus AT&T: media distraction (Time Warner) vs pure-play wireless focus. Historical pattern: "
        "Ma Bell → RBOCs → consolidation — episode shows 130-year arc repeating."
    ),
    key_insights=[
        {
            "view": "Sprint's value was spectrum, not subscribers.",
            "question": "Why buy a chronically weak #4 carrier?",
            "answer": (
                "2.5GHz mid-band spectrum for 5G — expensive to acquire at auction, impossible to create. T-Mobile "
                "had Uncarrier brand and growth but weaker mid-band portfolio. Sprint's ~50M subs were bonus; "
                "SoftBank's ~$21.6B 2013 entry price showed strategic premium on US wireless access. Without "
                "spectrum, Legere's marketing hits ceiling on network quality claims."
            ),
        },
        {
            "view": "Uncarrier was marketing innovation, not network innovation.",
            "question": "How did T-Mobile gain 40M customers?",
            "answer": (
                "Eliminated contracts (2012), phone financing transparency, 'Un-carrier' stunts mocking AT&T/Verizon. "
                "Lower ARPU per user but massive net adds. Proved brand and pricing move share when LTE 'good enough.' "
                "5G era shifts battle back to capex and spectrum — merger acknowledged marketing alone insufficient."
            ),
        },
        {
            "view": "Regulatory remedy shapes industry structure for decades.",
            "question": "Why did 2011 AT&T/T-Mobile fail but 2020 deal succeed?",
            "answer": (
                "2011: four-to-three without credible fourth player — DOJ blocked. 2020: T-Mobile concessions "
                "(Dish MVNO, spectrum divestitures, 6-year build deadlines) painted competitive facade. Acquired "
                "hosts skeptical Dish delivers real competition — but regulators needed narrative to approve "
                "scale-for-5G argument."
            ),
        },
        {
            "view": "SoftBank's Sprint ownership was strategic trap.",
            "question": "Why didn't Masa Son fix Sprint?",
            "answer": (
                "$21.6B acquisition (2013) assumed SoftBank network expertise transfers — it didn't. Debt, "
                "Nextel legacy integration failures, and capital diverted to Vision Fund bets. By 2018 Son needed "
                "exit or merger — T-Mobile was only logical buyer. Episode connects to SoftBank Fortress episode "
                "in same season."
            ),
        },
        {
            "view": "Wireless consolidates in 30-year cycles.",
            "question": "What history lesson matters?",
            "answer": (
                "Bell breakup (1984) → RBOC mergers → Cingular/AT&T → T-Mobile/MetroPCS → now T-Mobile/Sprint. "
                "Each wave reduces player count as capex rises. 5G requires billions in small cells and mid-band "
                "— oligopoly math inevitable unless government mandates wholesale open access (never happened in US)."
            ),
        },
    ],
    top_investment_implications=[
        {
            "ticker": "TMUS",
            "direction": "Watch",
            "confidence": "Medium",
            "thesis": (
                "Merger closed 2020 — combined mid-band 5G spectrum and Uncarrier brand created #2 subscriber "
                "base; episode useful for understanding capex and ARPU tradeoffs post-Legere."
            ),
        },
    ],
    golden_quotes=[
        "\"Sprint's spectrum is the real asset — 2.5GHz is gold for 5G\" — hosts on strategic rationale beyond subscribers.",
        "\"Legere added 40 million customers by acting unlike a telecom CEO\" — on Uncarrier marketing breakthrough.",
        "\"Every US wireless merger ends up at the DOJ\" — on regulatory inevitability in spectrum oligopoly.",
    ],
    chronology={
        "subject": "T-Mobile · Sprint · US Wireless",
        "events": [
            {"date": "1899", "event": "Brown Telephone Company founded — eventual Sprint lineage"},
            {"date": "1984", "event": "AT&T breakup creates RBOCs — industry fragmentation era"},
            {"date": "2005", "event": "Sprint merges with Nextel — integration struggles begin"},
            {"date": "2011", "event": "DOJ blocks AT&T acquisition of T-Mobile"},
            {"date": "2012", "event": "Legere launches Uncarrier strategy at T-Mobile"},
            {"date": "2013", "event": "SoftBank acquires Sprint for ~$21.6B; T-Mobile buys MetroPCS"},
            {"date": "2018-04-29", "event": "T-Mobile announces $26B all-stock Sprint merger"},
            {"date": "2018", "event": "Merger faces DOJ/FCC review — Dish floated as 4th carrier remedy"},
            {"date": "2020-04", "event": "Merger closes after regulatory concessions"},
            {"date": "2020+", "event": "Combined T-Mobile deploys 5G on Sprint 2.5GHz spectrum nationwide"},
        ],
    },
    review_notes="Manual GPT Acquired batch — v5.1-acquired; Season 2–3 batch",
)

# --- Spotify Direct Listing ---
EPISODES["acq-season-2-episode-6spotifys-direct-listing"] = base(
    "acq-season-2-episode-6spotifys-direct-listing",
    episode_rating={"overall": 4},
    keywords=["Direct Listing", "Capital Markets", "Music Streaming"],
    conclusion=(
        "Ben and David dissect Spotify's April 3, 2018 NYSE direct listing — the first mega-cap tech to skip a "
        "traditional IPO — opening at ~$165.90 (~$26.6B market cap) versus a ~$132 reference price, with no "
        "primary capital raised and ~$300M saved in banker fees versus typical IPO underwriting. Goldman Sachs and "
        "Morgan Stanley advised; existing shareholders sold into the market directly. Hosts explain why Daniel Ek "
        "avoided dilution and lock-up norms: already $1B+ revenue, $4B+ raised privately, no need for primary cash. "
        "The episode became the template for Slack (2019) and Coinbase (2021) direct listings — a capital-markets "
        "innovation story paired with Spotify's music-industry disruption narrative."
    ),
    background=(
        "Season 2 Episode 6 covers Spotify's path from 2006 Stockholm startup through label licensing battles to "
        "the unconventional public debut. Acquired explains traditional IPO mechanics (roadshow, pricing discount, "
        "lock-up) versus direct listing (no new shares, price discovery on day one, no banker stabilization).\n\n"
        "Financial context at listing: ~$4.1B revenue run-rate, 157M MAUs and 71M premium subscribers (Q4 2017 "
        "metrics cited), gross margin improving but still ~70% revenue share to rights holders. Ek's choice signaled "
        "confidence and shareholder-friendly capital allocation — also avoided IPO 'pop' wealth transfer to flippers."
    ),
    important_facts=[
        "Spotify direct-listed April 3, 2018 on NYSE; first trade ~$165.90/share, ~$26.6B market cap — reference "
        "price was ~$132; no primary shares issued, no traditional underwriting fee on new capital.",
        "Spotify reported ~157M MAUs and ~71M premium subscribers in late 2017/early 2018 — largest music streaming "
        "platform globally at listing.",
        "Hosts estimate ~$300M+ in fees saved versus conventional IPO path — advisors Goldman Sachs and Morgan Stanley "
        "still earned advisory fees, not 7% underwriting spread on primary raise.",
        "Spotify had raised ~$2.8B+ privately before listing — direct listing viable because company did not need "
        "primary cash; Ek/Martin Lorentzon retained control via founder shares.",
        "Label licensing economics: ~70% of revenue to rights holders at listing — gross margin pressure central "
        "to bull/bear debate alongside user growth.",
    ],
    mental_model={
        "name": "Direct Listing When You Don't Need Cash",
        "components": (
            "Traditional IPO sells primary shares at discount to ensure day-one pop — wealth transfers from "
            "company/founders to allocation favorites. Direct listing suits mature private companies with brand "
            "awareness, broad shareholder base, and no immediate primary need. Price discovery via opening auction "
            "replaces roadshow price-setting. Tradeoffs: no greenshoe stabilization, no lock-up standard (though "
            "Spotify negotiated some), higher volatility day one. Spotify proved model for $10B+ companies — "
            "Slack and Coinbase followed."
        ),
        "application": (
            "Founders choosing IPO vs direct listing: if balance sheet funded and goal is liquidity not capital, "
            "direct listing saves spread and avoids dilution. Requires sufficient public float and analyst coverage "
            "potential. Investors: no allocation game — buy at market on day one. Acquired uses Spotify to teach "
            "capital markets mechanics most tech podcasts skip."
        ),
    },
    competitive_advantage=(
        "Spotify at listing owned consumer habit and data in streaming — 157M MAUs created playlist culture, "
        "Discover Weekly, and social sharing loops competitors copied. Label deals (years of negotiation) created "
        "barrier; Apple Music launched 2015 but Spotify maintained growth lead in most markets.\n\n"
        "Direct listing itself reinforced brand: Ek portrayed Spotify as confident, transparent, anti-Wall-Street "
        "rent-seeking — aligned with artist-friendly positioning. Freemium model (71M paid of 157M) proved "
        "conversion funnel at scale.\n\n"
        "Weaknesses at listing: 70% revenue share to labels capped gross margin; Apple/Google owned mobile OS "
        "distribution; no owned hardware. Public scrutiny on unit economics intensified post-listing. Direct "
        "listing volatility (first hours swung widely) unsettled some institutional buyers.\n\n"
        "Versus Apple Music: Spotify cross-platform; Apple bundled with iOS. Versus Pandora: on-demand won. "
        "Capital-markets angle: Spotify's listing changed tech CFO playbook for a generation — Acquired episode "
        "is cited in finance circles for this reason alone."
    ),
    key_insights=[
        {
            "view": "Direct listing fits liquidity events, not fundraising.",
            "question": "Why didn't Spotify do a normal IPO?",
            "answer": (
                "~$2.8B+ already raised privately; ~$4.1B revenue run-rate. Ek did not need primary cash — wanted "
                "public currency for M&A and employee liquidity without IPO discount. Saved ~$300M fees; avoided "
                "giving banks 7% on unnecessary primary. Acquired walks through when roadshow adds value (unknown "
                "companies) vs Spotify (global brand, existing secondary trading)."
            ),
        },
        {
            "view": "IPO pop is wealth transfer, not success metric.",
            "question": "Is first-day pop good?",
            "answer": (
                "Traditional IPO underprices to guarantee pop for allocated investors — company left money on table. "
                "Spotify opened ~26% above reference price without primary dilution — founders captured fair "
                "discovery. Hosts argue pop celebrates banker client favoritism, not efficient pricing. Direct "
                "listing reframes success as accurate price discovery."
            ),
        },
        {
            "view": "Label economics cap Spotify margin until product expands.",
            "question": "Why bearish on gross margin?",
            "answer": (
                "~70% revenue to rights holders at listing — structural until Spotify adds podcasts, audiobooks, "
                "and artist tools (later episodes cover). Scale improves negotiating leverage slightly but does "
                "not eliminate royalty pass-through. Bulls bet TAM and ads; bears see permanent tax to labels."
            ),
        },
        {
            "view": "Spotify blazed trail for Slack and Coinbase.",
            "question": "Did direct listing stick?",
            "answer": (
                "Slack direct-listed 2019; Coinbase 2021 — both cited Spotify precedent. Model works for "
                "well-known brands with deep private cap tables. Not universal: companies needing primary capital "
                "still use traditional IPO. Goldman/Morgan Stanley adapted playbook — episode documents "
                "institutional learning curve."
            ),
        },
        {
            "view": "Freemium at scale was unproven until Spotify listed.",
            "question": "Why did public markets matter?",
            "answer": (
                "157M MAUs with 71M paid proved conversion at global scale — data every music skeptic requested. "
                "Public reporting forced quarterly transparency on churn, ARPU, and label renegotiations. Listing "
                "validated streaming as industry revenue leader, not niche."
            ),
        },
    ],
    top_investment_implications=[
        {
            "ticker": "SPOT",
            "direction": "Watch",
            "confidence": "Medium",
            "thesis": (
                "Direct listing episode frames Spotify as capital-efficient liquidity event — useful context for "
                "evaluating margin expansion via podcasts/audiobooks post-2018 royalty structure."
            ),
        },
    ],
    golden_quotes=[
        "\"Spotify saved $300 million by not doing a traditional IPO\" — hosts quantifying banker fee avoidance.",
        "\"This isn't an IPO — they're not raising money\" — David clarifying direct listing vs primary offering.",
        "\"The reference price was $132 — it opened at $165.90\" — on day-one price discovery without underwriter discount.",
    ],
    chronology={
        "subject": "Spotify · Direct Listing",
        "events": [
            {"date": "2006", "event": "Spotify founded in Stockholm by Daniel Ek and Martin Lorentzon"},
            {"date": "2008–2011", "event": "European launch; prolonged US label licensing negotiations"},
            {"date": "2011–2016", "event": "US expansion; raises ~$2.8B+ privately across rounds"},
            {"date": "2015", "event": "Apple Music launches — platform competition intensifies"},
            {"date": "2017-Q4", "event": "~157M MAUs, ~71M premium subscribers reported"},
            {"date": "2018-02", "event": "Spotify files for direct listing with SEC — not traditional IPO"},
            {"date": "2018-04-03", "event": "NYSE direct listing — first trade ~$165.90, ~$26.6B market cap"},
            {"date": "2018-04-03", "event": "Reference price ~$132; no primary shares issued"},
            {"date": "2019", "event": "Slack follows Spotify direct-listing model"},
            {"date": "2021", "event": "Coinbase direct listing — Spotify precedent cited widely"},
        ],
    },
    review_notes="Manual GPT Acquired batch — v5.1-acquired; Season 2–3 batch",
)

# --- Dropbox IPO ---
EPISODES["acq-season-2-episode-5the-dropbox-ipo"] = base(
    "acq-season-2-episode-5the-dropbox-ipo",
    episode_rating={"overall": 3},
    keywords=["Freemium SaaS", "Cloud Storage", "IPO Pricing"],
    conclusion=(
        "Ben and David cover Dropbox's March 23, 2018 IPO — priced at $21/share (above $18–20 range), raising "
        "~$756M and hitting ~$9.2B market cap on ~$1.1B 2017 revenue — the largest tech IPO since Snap. Drew "
        "Houston's Y Combinator-origin story (2007, rejected once, iconic demo video) became a freemium SaaS "
        "blueprint: 500M registered users, 11.5M paying (~2.3% conversion), $111 ARPU. Hosts contrast Box "
        "($14 IPO, enterprise focus) and explain why consumer-grade UX with enterprise upsell (Dropbox Business) "
        "won the file-sync category before Google Drive and iCloud caught up. COGS on storage (AWS/S3) and "
        "competition from free incumbents remain the bear case Acquired lays out clearly."
    ),
    background=(
        "Season 2 Episode 5 traces Dropbox from Drew Houston forgetting his USB stick on a bus through the "
        "2007 YC batch, explosive referral growth, and 'it just works' product philosophy to the S-1 and IPO.\n\n"
        "Acquired walks S-1 metrics: revenue acceleration to $1.1B, net losses narrowing, 500M+ signups, "
        "11.5M paid users, and infrastructure costs of storing exabytes. They compare IPO mechanics to Box (2015), "
        "discuss dual-class shares, and why Dropbox priced above range (hot IPO window, March 2018). The episode "
        "is the definitive freemium conversion math case study in the Acquired catalog."
    ),
    important_facts=[
        "Dropbox IPO March 23, 2018 priced at $21/share — above $18–20 range — raising ~$756M; first-day close "
        "implied ~$9.2B+ market cap on ~$1.1B 2017 revenue.",
        "500M registered users and 11.5M paying subscribers at IPO (~2.3% conversion rate) — freemium funnel "
        "benchmark; average revenue per paying user ~$111/year cited in S-1 analysis.",
        "Founded 2007 by Drew Houston and Arash Ferdowsi; Houston's YC application included famous demo video "
        "when he forgot USB drive — organic viral growth followed.",
        "2017 revenue ~$1.1B (up from ~$603M in 2015) — growth re-accelerating into IPO; still GAAP unprofitable "
        "but losses narrowing versus prior years.",
        "Box IPO comparison (2015): Box priced ~$14 with ~$250M revenue — Dropbox commanded premium multiple on "
        "consumer scale and better conversion metrics.",
    ],
    mental_model={
        "name": "Freemium Conversion at Billion-User Scale",
        "components": (
            "Dropbox proved consumer-grade UX can funnel to paid storage when sync reliability is 10x better "
            "than incumbents. 500M signups × 2.3% paid × ~$111 ARPU = $1.1B revenue — math every SaaS founder "
            "memorizes. Referral program (extra space for invites) lowered CAC to near zero early. Enterprise "
            "Dropbox Business layered on same sync engine — PLG before the term existed. COGS risk: storage "
            "commoditizes; Google/Microsoft give GB free with OS bundles."
        ),
        "application": (
            "Evaluate freemium by conversion rate × ARPU × cohort retention, not signup vanity. Dropbox's 2.3% "
            "paid conversion is benchmark — below 1% usually fails at scale. When incumbents bundle free storage, "
            "differentiate on workflow (Paper, Smart Sync) or vertical security. IPO pricing above range signals "
            "hot window — compare Box timing 2015 vs Dropbox 2018 for market appetite shift."
        ),
    },
    competitive_advantage=(
        "Dropbox won 2008–2015 window on reliability and simplicity — 'it just works' when Google Drive and "
        "OneDrive were afterthoughts. Cross-platform sync (Mac/Windows/iOS/Android) mattered before iCloud "
        "matured. Developer-friendly API and SMB adoption created bottom-up enterprise entry (Dropbox Business).\n\n"
        "Brand became verb ('Dropbox me that file'); referral loops built 500M users cheaply. Houston's product "
        "taste — invisible sync, smart caching — hard for enterprise IT vendors to replicate with same UX polish.\n\n"
        "Weaknesses at IPO: storage COGS scale linearly; Google Drive and iCloud free tiers capped consumer ARPU. "
        "2.3% conversion leaves 97.7% non-paying load on infra. Competition from Box in enterprise and Microsoft "
        "Teams bundling in Office 365. Post-IPO, Dropbox pivoted to collaboration (Paper) and productivity suite — "
        "category expanded beyond sync.\n\n"
        "Versus Box: Dropbox consumer PLG → enterprise; Box top-down IT sales. Versus Google: Dropbox neutrality "
        "across OS; Google favors Android/Chrome. IPO premium reflected scale Box never achieved in consumer signups."
    ),
    key_insights=[
        {
            "view": "2.3% conversion at 500M users is the hero metric.",
            "question": "How does freemium math work at scale?",
            "answer": (
                "11.5M paying of 500M registered ≈ 2.3% — below typical B2B SaaS conversion but massive in "
                "absolute dollars (~$111 ARPU → ~$1.1B revenue). Acquired emphasizes absolute paid users over "
                "conversion rate — 11.5M subs is larger than most SaaS companies' total customers. Referral growth "
                "kept CAC low early; later paid marketing rose pre-IPO."
            ),
        },
        {
            "view": "YC demo video is canonical PLG origin story.",
            "question": "Why did Dropbox spread virally?",
            "answer": (
                "Houston built product after forgetting USB on bus; YC video showed product working — rare clarity "
                "in 2007. Referral incentive (250MB–500MB extra space per invite) turned users into salesforce. "
                "Product quality sustained retention when free alternatives arrived — sync reliability was moat "
                "until OS vendors caught up."
            ),
        },
        {
            "view": "Pricing above range signaled 2018 IPO window strength.",
            "question": "Why $21 vs $18–20 guide?",
            "answer": (
                "March 2018 hot market post-tax-reform; Spotify direct listing same month created tech IPO halo. "
                "Bankers tested demand in roadshow — institutional oversubscription allowed raise above range. "
                "Contrast Box 2015 pricing conservatism on weaker metrics. Dropbox largest tech IPO since Snap "
                "— narrative momentum mattered."
            ),
        },
        {
            "view": "Storage COGS is the permanent bear case.",
            "question": "What caps Dropbox margin long-term?",
            "answer": (
                "AWS/S3 costs scale with data stored; 97.7% free users consume GB without paying. Google Drive "
                "15GB free and iCloud bundles subsidize storage from ads and hardware margin. Dropbox must upsell "
                "collaboration and enterprise seats — pure sync commoditizes. S-1 showed improving gross margin "
                "but hosts skeptical of consumer ARPU expansion."
            ),
        },
        {
            "view": "Dropbox Business bridged consumer to enterprise.",
            "question": "How did SMB adoption happen?",
            "answer": (
                "Employees synced work files via personal Dropbox before IT approved — classic shadow IT PLG. "
                "Dropbox Business added admin controls, SSO, compliance — upsell same users at higher ARPU. "
                "Box fought top-down; Dropbox won bottom-up then expanded seat count. Model later copied by "
                "Slack, Zoom, Notion."
            ),
        },
    ],
    top_investment_implications=[
        {
            "ticker": "DBX",
            "direction": "Watch",
            "confidence": "Low",
            "thesis": (
                "Freemium conversion benchmark episode — track paid-user growth and ARPU vs free storage "
                "bundling from Google/Microsoft when assessing long-term margin."
            ),
        },
    ],
    golden_quotes=[
        "\"500 million registered users, 11.5 million paying — that's the freemium math\" — hosts on S-1 hero metrics.",
        "\"He forgot his USB stick on the bus and built Dropbox\" — canonical origin story.",
        "\"Priced at $21 — above the range\" — on IPO window confidence March 2018.",
    ],
    chronology={
        "subject": "Dropbox",
        "events": [
            {"date": "2007", "event": "Drew Houston founds Dropbox; Y Combinator batch after demo video"},
            {"date": "2008", "event": "Public launch; referral program drives viral signups"},
            {"date": "2011–2014", "event": "500M user milestone trajectory; Dropbox Business launches"},
            {"date": "2015", "event": "Box IPO (~$14) — enterprise competitor benchmarks public markets"},
            {"date": "2017", "event": "Revenue ~$1.1B; 11.5M paying users; losses narrowing"},
            {"date": "2018-02", "event": "S-1 filed — largest tech IPO filing since Snap narrative"},
            {"date": "2018-03-23", "event": "IPO prices at $21/share, raises ~$756M, ~$9.2B market cap"},
            {"date": "2018-03", "event": "First-day trading positive — above-range pricing validated"},
            {"date": "2018", "event": "Google Drive and iCloud intensify free storage competition"},
            {"date": "2018", "event": "Acquired episode publishes — freemium IPO case study canon"},
        ],
    },
    review_notes="Manual GPT Acquired batch — v5.1-acquired; Season 2–3 batch",
)

# --- SoftBank Vision Fund ---
EPISODES["acq-season-2-episode-4softbank-fortress-and-the-vision-fund"] = base(
    "acq-season-2-episode-4softbank-fortress-and-the-vision-fund",
    episode_rating={"overall": 4},
    keywords=["Vision Fund", "Masayoshi Son", "Alternative Asset Management"],
    conclusion=(
        "Ben and David profile Masayoshi Son's SoftBank — from 1981 PC software distributor to ARM acquirer ($32B, "
        "2016), Fortress Investment Group ($3.3B, 2017), and the $100B Vision Fund (2017) backed by $45B Saudi PIF "
        "and $28B SoftBank. Son's 300-year vision and Alibaba bet (~$20M for ~25% stake, worth $100B+ at peak) "
        "justify aggressive deployment into Uber, WeWork, and Sprint. Fortress brought US credit and asset-management "
        "infrastructure to deploy Gulf capital at scale. Hosts debate whether Son is visionary allocator or "
        "concentrated-risk gambler — episode aired pre-WeWork collapse but flags governance and leverage concerns. "
        "Essential primer on the capital source that shaped late-2010s tech."
    ),
    background=(
        "Season 2 Episode 4 traces Son's arc: Korean-Japanese entrepreneur, early Yahoo! Japan, Vodafone K.K. "
        "acquisition creating SoftBank Mobile, 2000 dot-com near-death, Alibaba investment (2000), and resurgence.\n\n"
        "2016–2017 moves: ARM Holdings acquisition for chip IP moat in IoT/AI era; Fortress for alternative asset "
        "management platform; Vision Fund as largest private tech fund ever. Acquired explains carried interest, "
        "Saudi partnership post-2016 Aramco narrative, and why Son needed Fortress to deploy $100B without "
        "building from scratch. Sprint ownership (2013) links to T-Mobile merger episode."
    ),
    important_facts=[
        "Vision Fund announced 2017 at $100B target — $45B from Saudi Arabia Public Investment Fund (PIF), ~$28B "
        "from SoftBank, remainder from Apple, Qualcomm, Sharp, etc.",
        "SoftBank acquired ARM Holdings in 2016 for ~$32B — dominant mobile chip IP licenser, strategic for IoT/AI "
        "compute at edge.",
        "Fortress Investment Group acquired 2017 for ~$3.3B — brought ~$70B AUM credit and asset-management "
        "platform to help deploy Vision Fund capital in US.",
        "Son's Alibaba investment (~$20M in 2000 for ~25% stake) peaked above $100B value — defining venture "
        "return that justified Son's risk appetite.",
        "Vision Fund initial bets included Uber (~$7.7B+ deployed across rounds), WeWork, Didi, Slack — "
        "concentrated late-stage tech exposure at unprecedented fund size.",
    ],
    mental_model={
        "name": "Concentrated Vision Capital",
        "components": (
            "Son operates on power-law conviction: one Alibaba-return funds decades of bets. Vision Fund scaled "
            "this to $100B — forcing checks so large Son becomes price-setter in late-stage private markets. "
            "Fortress acquisition added credit/alternative-asset infrastructure Saudi capital required. ARM "
            "secures compute IP layer for Son's AI/IoT thesis. Risk: fund size eliminates diversification; "
            "governance weak at portfolio companies (WeWork); geopolitical tie to PIF."
        ),
        "application": (
            "When late-stage valuations spike 2017–2019, trace SoftBank bid in cap table. Founders: mega-checks "
            "accelerate growth but add pressure for $10B+ outcomes. LPs: distinguish Son's personal balance sheet "
            "bets from fund marks. Regulators: cross-border sovereign capital reshapes US tech independence — "
            "episode predates TikTok/CFIUS era but foreshadows."
        ),
    },
    competitive_advantage=(
        "SoftBank's edge is Son's track record and willingness to write $5B–$10B checks when Sand Hill writes "
        "$100M. Alibaba return gave credibility to raise Saudi PIF — largest sovereign commitment to private tech "
        "ever. ARM acquisition locked mobile/IoT chip IP — strategic asset competitors cannot replicate quickly.\n\n"
        "Fortress added US-regulated asset manager with credit expertise — deploy capital beyond equity growth "
        "rounds. Mobile business (SoftBank Corp) generates cash flow funding Vision Fund LPs' confidence. "
        "Global portfolio (Sprint US, Alibaba China, ARM UK) diversifies geography if not strategy.\n\n"
        "Weaknesses: WeWork and other Vision Fund marks collapsed 2019–2020; Son overpaid for growth narratives. "
        "Saudi partnership drew ESG and geopolitical scrutiny (Khashoggi era). Sprint investment failed operationally "
        "— $21.6B into weak #4 carrier. Fund II raised smaller; Son personal margin loans during 2022 tech drawdown.\n\n"
        "Versus traditional VC: SoftBank priced out sequoia-style discipline — winner-take-all checks. Versus "
        "sovereign wealth direct: Son adds operator narrative and speed. Episode captures peak SoftBank "
        "optimism before WeWork IPO collapse reframed narrative."
    ),
    key_insights=[
        {
            "view": "Alibaba return psychologically funds everything.",
            "question": "Why does Son take extreme risk?",
            "answer": (
                "~$20M into Alibaba (~2000) for ~25% became $100B+ at peak — largest venture return in history. "
                "Son credibly claims pattern recognition others lack. Vision Fund is explicit attempt to manufacture "
                "multiple Alibabas at once with $100B. Acquired notes survivorship bias: one win forgives many "
                "losses in Son's psychology — investors must model downside if no next Alibaba."
            ),
        },
        {
            "view": "Fortress was infrastructure for Gulf capital deployment.",
            "question": "Why buy a hedge fund for $3.3B?",
            "answer": (
                "Fortress ~$70B AUM with credit and asset-management licenses — SoftBank needed US platform to "
                "deploy PIF money compliantly and diversely, not only venture equity. $3.3B price small versus "
                "$100B fund ambition. Analogous to Blackstone building distribution before raising mega-funds."
            ),
        },
        {
            "view": "ARM secures the compute layer for Son's AI bet.",
            "question": "Why pay $32B for ARM?",
            "answer": (
                "ARM licenses chip designs to every mobile OEM — IoT and edge AI devices will run ARM architecture. "
                "Owning IP beats renting for 300-year vision. Nvidia later attempted acquisition (failed on "
                "regulatory) — validated ARM strategic value. SoftBank held until 2023 IPO re-listing."
            ),
        },
        {
            "view": "$100B fund size distorts private markets.",
            "question": "How did Vision Fund change venture?",
            "answer": (
                "Checks like $7.7B+ into Uber set valuation anchors — competitors forced to match or lose deals. "
                "Late-stage 2017–2019 multiples inflated industry-wide. Founders delayed IPOs expecting SoftBank "
                "follow-on. WeWork $47B private mark epitomized excess — episode aired pre-collapse but hosts "
                "flag governance risks when one LP dominates cap table."
            ),
        },
        {
            "view": "Sprint links SoftBank episode to T-Mobile merger.",
            "question": "How does US wireless fit?",
            "answer": (
                "Son bought Sprint 2013 for ~$21.6B — US telecom beachhead failed operationally but held spectrum "
                "strategic value. 2018 T-Mobile merger attempt (separate episode) was exit path for sunk Sprint "
                "investment. Shows Son's US ambitions exceeded operational capacity — Vision Fund equity easier "
                "than running RBOC."
            ),
        },
    ],
    top_investment_implications=[
        {
            "ticker": "9984.T",
            "direction": "Watch",
            "confidence": "Low",
            "thesis": (
                "SoftBank Group NAV tied to Alibaba stake, Vision Fund marks, and ARM — episode frames Son "
                "concentration risk and sovereign LP dependence for holding-company discount analysis."
            ),
        },
    ],
    golden_quotes=[
        "\"I'm thinking in 300-year terms\" — Masayoshi Son's vision framing for Vision Fund scale.",
        "\"$20 million into Alibaba became over $100 billion\" — hosts on the return that defined Son's career.",
        "\"The largest technology investment fund in history — $100 billion\" — on Vision Fund size versus entire VC industry.",
    ],
    chronology={
        "subject": "SoftBank · Masayoshi Son",
        "events": [
            {"date": "1981", "event": "SoftBank founded as PC software distributor in Japan"},
            {"date": "1996", "event": "Yahoo! Japan joint venture — early internet bet"},
            {"date": "2000", "event": "Son invests ~$20M in Alibaba for ~25% stake"},
            {"date": "2006", "event": "Acquires Vodafone K.K. — becomes major Japanese mobile carrier"},
            {"date": "2013", "event": "SoftBank acquires Sprint for ~$21.6B"},
            {"date": "2016", "event": "Acquires ARM Holdings for ~$32B"},
            {"date": "2017", "event": "Acquires Fortress Investment Group for ~$3.3B"},
            {"date": "2017", "event": "Vision Fund announced — $100B target, $45B from Saudi PIF"},
            {"date": "2017–2018", "event": "Mega-checks into Uber, WeWork, Didi, and other late-stage tech"},
            {"date": "2018", "event": "Acquired episode — peak SoftBank narrative before WeWork troubles"},
        ],
    },
    review_notes="Manual GPT Acquired batch — v5.1-acquired; Season 2–3 batch",
)

# --- Against Gravity / Nick Fajt ---
EPISODES["acq-season-2-episode-2raising-a-seed-round-with-against-gravity-ceo-nick-fajt"] = base(
    "acq-season-2-episode-2raising-a-seed-round-with-against-gravity-ceo-nick-fajt",
    episode_rating={"overall": 3},
    keywords=["Seed Fundraising", "VR Gaming", "Founder Interview"],
    conclusion=(
        "Nick Fajt (Against Gravity, later Rec Room) joins Ben and David for a rare Acquired format: live "
        "deconstruction of an in-progress $5M seed round for a social VR gaming startup. Fajt — ex-Microsoft "
        "Hololens team — explains raising from Sequoia and others while building cross-platform 'Rec Room' "
        "before consumer VR hit scale. Hosts walk term sheet mechanics: pre-money valuation, option pool shuffle, "
        "pro-rata rights, and why Seattle VR cluster (Valve, Oculus partnerships) mattered. The company pivoted "
        "brand to Rec Room, grew free-to-play VR with 37M+ lifetime users (post-episode), and raised $100M+ "
        "Series D — but at recording (2018) success was uncertain. Episode is Acquired's best seed-stage "
        "fundraising masterclass."
    ),
    background=(
        "Season 2 Episode 2 breaks Acquired's usual historical format for a founder interview during active "
        "fundraising. Nick Fajt built Against Gravity in Seattle after Microsoft AR work — product was Rec Room, "
        "a social VR playground for Xbox/PlayStation/PC/mobile (VR optional).\n\n"
        "Ben (Pioneer Square Labs) and David walk cap table math, investor selection (Sequoia lead), and why "
        "VR timing was brutal (2018 headset install base tiny). Fajt discusses free-to-play monetization (cosmetics), "
        "community moderation, and building for flat-screen first with VR upside. Meta-lesson: raise when you have "
        "momentum narrative, not when broke — Fajt ran process with multiple term sheets."
    ),
    important_facts=[
        "Against Gravity (Rec Room) raising ~$5M seed round during episode recording — Sequoia among lead investors "
        "discussed; Fajt previously on Microsoft Hololens team before founding.",
        "Rec Room launched cross-platform (PC, console, mobile) with VR as enhancement — 2018 VR install base "
        "under 10M headsets globally, forcing flat-screen-first strategy.",
        "Free-to-play cosmetics monetization model — users pay for avatar items, not gameplay advantage; similar "
        "to Fortnite/Roblox economics Fajt cited.",
        "Seattle gaming cluster advantage: proximity to Valve, Microsoft, and early Oculus relationships for "
        "distribution and talent.",
        "Post-episode trajectory (context): rebranded Rec Room, raised $100M+ Series D (2021), 37M+ lifetime "
        "accounts and mobile expansion — seed round in episode preceded scale phase.",
    ],
    mental_model={
        "name": "Raise Into Strength, Not Exhaustion",
        "components": (
            "Fajt ran seed process with leverage — multiple interested investors, clear product demo (Rec Room "
            "social rooms), and narrative that VR timing risk is priced in but cross-platform optionality is free "
            "call option. Term sheet topics: 15–20% dilution typical seed, option pool expansion pre-money vs "
            "post-money, board seat (often observer at seed). Ben's PSL lens: Seattle founders can access SF "
            "capital without relocating. VR-specific: build for today's install base (console/PC) while positioning "
            "for tomorrow's headset curve."
        ),
        "application": (
            "Founders: start fundraising with 6+ months runway and working product — Fajt demoed live social rooms. "
            "Optimize for investor who understands gaming community dynamics, not generic SaaS metrics. Accept "
            "platform risk (Meta/Oculus) but diversify to PlayStation/Xbox/mobile. Investors: seed in VR requires "
            "belief in founder iteration speed when TAM timing uncertain."
        ),
    },
    competitive_advantage=(
        "Rec Room's edge was social-first game design — parties, mini-games, user-generated rooms — not VR tech "
        "demo. Fajt's Hololens background informed spatial interaction but product prioritized fun over fidelity. "
        "Cross-platform from early days meant 2018 users on PS4 without VR headset still joined — critical when "
        "VR install base <10M.\n\n"
        "Community moderation and kid-safe branding (later COPPA compliance) differentiated from open VR chat "
        "rooms. Free-to-play cosmetics aligned incentives — no pay-to-win backlash. Seattle talent pool (Valve "
        "alumni, Microsoft game dev) lowered hiring friction.\n\n"
        "Weaknesses at seed: VR platform risk (Oculus/Meta controls destiny), tiny initial TAM, capital intensity "
        "of 3D content. Fortnite and Roblox competed for same teen social gaming minutes. Monetization per user "
        "lower than PC AAA titles — required scale for venture outcome.\n\n"
        "Versus Roblox: Rec Room more session-based social VR; Roblox UGC empire larger. Versus AltspaceVR: "
        "Rec Room survived by going cross-platform early. Episode captures seed-stage uncertainty before "
        "2020+ VR and mobile growth validated thesis."
    ),
    key_insights=[
        {
            "view": "Cross-platform de-risks VR timing.",
            "question": "Why build for PS4 when pitching VR investors?",
            "answer": (
                "2018 global VR headsets under 10M — pure VR company dies waiting for TAM. Rec Room ran on flat "
                "screens with VR optional — revenue and engagement today, optionality tomorrow. Fajt framed VR "
                "as accelerant not requirement. Sequoia bought cross-platform hedge; lesson applies to AR today."
            ),
        },
        {
            "view": "Seed term sheets are negotiable if you have leverage.",
            "question": "What did Fajt negotiate?",
            "answer": (
                "Multiple term sheets let Fajt optimize partner fit, not just valuation. Option pool shuffle "
                "pre-money common trap — Ben explains dilution math live. Pro-rata rights for lead investor "
                "signal follow-on confidence. Board observer vs seat — seed-stage founders retain control. "
                "Process run from strength with months of runway remaining."
            ),
        },
        {
            "view": "Social VR is community product, not hardware product.",
            "question": "Why did Against Gravity win vs Altspace?",
            "answer": (
                "Focus on games and parties — immediate fun loop — versus corporate meeting use cases. Moderation "
                "and kid-friendly design built trust for parents. Cosmetics monetization matched Fortnite generation "
                "expectations. Hardware-agnostic distribution meant community persisted across platform shifts."
            ),
        },
        {
            "view": "Seattle can raise SF-caliber seed.",
            "question": "Does geography matter at seed?",
            "answer": (
                "Fajt accessed Sequoia despite Seattle HQ — product demo traveled. PSL ecosystem (Ben) and Microsoft "
                "alumni network provided intros. Gaming talent locally deep (Valve, Bungie alums). Lesson: "
                "relocate optional if product compelling; VR/gaming investors fly to demos."
            ),
        },
        {
            "view": "Free-to-play is default for social gaming seed pitches.",
            "question": "Why not premium VR title?",
            "answer": (
                "Premium ($30) caps revenue on small install base; cosmetics and battle pass scale with DAU. "
                "Fortnite/Roblox proved model — Fajt cited comparables in pitch. Investors want LTV expansion "
                "curves, not one-time unit sales. Content updates drive retention without sequel dependency."
            ),
        },
    ],
    top_investment_implications=[
        {
            "ticker": "Private",
            "direction": "Watch",
            "confidence": "Low",
            "thesis": (
                "Rec Room became category winner in social gaming — episode seed fundamentals (cross-platform, "
                "F2P cosmetics) explain later $100M+ raises independent of VR headset curve."
            ),
        },
    ],
    golden_quotes=[
        "\"We raised when we had leverage — not when we were running out of money\" — Fajt on seed process timing.",
        "\"Build for the platforms that exist today, not the ones you hope exist tomorrow\" — cross-platform VR strategy.",
        "\"This is a community product — the game is just the excuse to hang out\" — on Rec Room social design.",
    ],
    chronology={
        "subject": "Against Gravity · Rec Room · Nick Fajt",
        "events": [
            {"date": "2014–2015", "event": "Nick Fajt leaves Microsoft Hololens team; founds Against Gravity"},
            {"date": "2016", "event": "Rec Room launches in early access — social VR gaming focus"},
            {"date": "2016–2017", "event": "Cross-platform expansion to PlayStation and PC flat-screen"},
            {"date": "2018-02", "event": "Acquired records episode during ~$5M seed fundraise"},
            {"date": "2018", "event": "Sequoia-led seed closes — term sheet mechanics discussed on air"},
            {"date": "2019", "event": "Mobile and console growth beyond core VR install base"},
            {"date": "2020", "event": "COVID accelerates social gaming engagement industry-wide"},
            {"date": "2021", "event": "Rec Room raises $100M+ Series D; rebrand from Against Gravity"},
            {"date": "2021+", "event": "37M+ lifetime accounts reported — mobile key growth driver"},
            {"date": "2021+", "event": "Validates seed thesis: cross-platform social gaming beyond VR niche"},
        ],
    },
    review_notes="Manual GPT Acquired batch — v5.1-acquired; Season 2–3 batch",
)


EXPAND: dict[str, dict] = {
    "acq-season-3-episode-3the-sonos-ipo": {
        "competitive_append": (
            "\n\nInvestor read-through: SONO trades as a hardware OEM multiple despite software-like gross "
            "margins (~61%) because smart-speaker giants cross-subsidize. Post-2018, Sonos expanded into "
            "home theater (Beam, Arc soundbars) where voice-assistant substitution is weaker — a sensible "
            "niche-up move Acquired's hosts implicitly endorse. Patent litigation against Google (2018) and "
            "eventual settlement showed defensive IP value but not growth. For portfolio managers, the episode "
            "is a checklist for any premium hardware IPO facing platform bundling: map OS owner incentives, "
            "model subscription attach, and stress-test day-one banker pricing in bad news cycles."
        ),
        "background_append": (
            "\n\nHosts also walk through Sonos's S-1 risk factors verbatim — Apple, Google, and Amazon listed "
            "as existential competitors — and why public investors reacted faster than private holders. "
            "The episode connects forward to later Acquired smart-home and platform episodes as canonical "
            "hardware-meets-Big-Tech case study."
        ),
        "mental_append": (
            " Sonos post-IPO added subscription (Sonos Radio HD) attempting services attach — partial "
            "validation of escaping pure hardware P&L."
        ),
    },
    "acq-season-3-episode-2the-xiaomi-ipo": {
        "competitive_append": (
            "\n\nPost-IPO, Xiaomi's EV entry (2021+) extends the triathlon to a fourth leg — logical if you "
            "believe Lei Jun's 5% margin cap is permanent user-acquisition spend. Huawei sanctions (2019+) "
            "temporarily benefited China share but also showed geopolitical tail risk for any Chinese "
            "hardware exporter. Investors tracking 1810.HK should watch services mix quarterly: until internet "
            "services exceed ~20% of revenue, the stock behaves like a low-multiple handset OEM. Acquired's "
            "episode remains the best English-language primer on why Western investors misread Chinese "
            "hardware-as-channel models at IPO."
        ),
        "background_append": (
            "\n\nHosts compare Lei Jun's celebrity-founder status in China to Steve Jobs keynotes — flash "
            "sales as entertainment events driving zero-CAC demand spikes. They also note MIUI weekly "
            "update cadence versus annual OEM Android releases as operational moat Western analysts "
            "underweighted at IPO."
        ),
        "mental_append": (
            " Watch services revenue crossing 20% of mix as proof triathlon works — until then handset "
            "multiples apply."
        ),
        "insight_answers_expand": {
            0: " Lei Jun's public margin cap functions as marketing — Mi Fans trust pricing versus Oppo/Vivo.",
            1: " Weekly MIUI updates created habit loop OEMs with annual releases could not match.",
            2: " Rice cookers and scooters share BOM sourcing — margin on attach SKUs funds 5% phone cap.",
            3: " Trade-war overhang (2018 tariffs) contributed to flat open despite 100M phone scale.",
            4: " India #1 share periods proved model exports beyond China — Western markets remained closed.",
        },
        "components_append": (
            " Mi Home retail (targeting 10,000+ stores globally) closes the loop — offline touchpoints "
            "for 90+ SKUs with staff trained on ecosystem cross-sell, mirroring Apple Store economics "
            "at 1/10 the ASP."
        ),
        "facts_fix": {
            4: (
                "First-day trading: shares opened ~0% above IPO price (flat to slightly down versus HK$17 "
                "offer) — unusual for hot Chinese tech listings; investors questioned services profitability "
                "and trade-war overhang."
            ),
        },
    },
    "acq-season-2-episode-10the-rover-dogvacay-merger-with-rover-ceo-aaron-easterly": {
        "competitive_append": (
            "\n\nEasterly's post-merger playbook — cut duplicate city launch teams, unify insurance "
            "underwriting, expand walking SKU — is textbook marketplace roll-up execution. Rover eventually "
            "SPAC'd in 2021, validating that pet services could reach public markets only after duopoly "
            "consolidation. For investors, the episode's lesson is categorical: when two well-funded "
            "marketplaces fight for identical local supply, merge synergies often exceed either company's "
            "standalone DCF. Watch take-rate pressure above 20% and incident-driven regulatory risk as "
            "scale increases."
        ),
        "background_append": (
            "\n\nEasterly details integration mechanics: retaining Rover brand, merging insurance policies, "
            "and aligning sitter vetting standards that differed slightly between platforms. Ben draws "
            "parallel to if Airbnb and HomeAway had merged in 2012 — saved years of burn."
        ),
        "mental_append": (
            " Pet services frequency (2–4 bookings/year average) caps LTV versus daily-use marketplaces — "
            "merge reduces CAC enough to make math work."
        ),
        "insight_answers_expand": {
            0: " Easterly cites overlapping metro sitter lists as merger diligence centerpiece.",
            1: " $25K vet guarantee and 24/7 hotline are SKU features justifying 20% take rate.",
            2: " Rover measured supply density per zip code — national TV ads secondary to local liquidity.",
            3: " Walking SKU adds 52× frequency potential versus vacation-only boarding.",
            4: " Combined ~$100M+ burn pre-merger made standalone IPO paths unlikely for either company.",
        },
        "components_append": (
            " Insurance and vetting create regulatory moat — offline kennels cannot replicate $25K guarantee "
            "or 24/7 support at national scale without equivalent capital reserves."
        ),
    },
    "acq-season-2-episode-8t-mobile-sprint": {
        "competitive_append": (
            "\n\nPost-2020 close, T-Mobile marketed '5G leader' status using Sprint mid-band — Legere's "
            "Uncarrier theatrics gave way to network-quality competition. TMUS stock re-rated as synergies "
            "materialized (cost cuts, spectrum deployment). Acquired's historical arc — Bell to RBOCs to "
            "today's Big Three — teaches that wireless investing is spectrum arithmetic more than brand. "
            "Dish as fourth-carrier remedy remains structurally weak; regulators accepted narrative over "
            "substance to approve scale-for-5G capex. Episode pairs naturally with SoftBank Fortress (Sprint "
            "ownership) in the same season."
        ),
        "background_append": (
            "\n\nHosts explain MVNO economics (MetroPCS, Boost) and why prepaid brands matter for "
            "low-ARPU customer acquisition. They map Sprint's debt load (~$32B+) as SoftBank's forcing "
            "function to accept merger terms below Son's original $21.6B entry optimism."
        ),
        "mental_append": (
            " Model each carrier as spectrum portfolio plus subscriber ARPU; marketing moves share only "
            "until 5G capex requires mid-band depth Sprint uniquely held."
        ),
        "insight_answers_expand": {
            0: " 2.5GHz mid-band covers urban/suburban 5G at lower tower density than mmWave.",
            1: " Uncarrier stunts (contract elimination, free Netflix bundles later) drove net adds.",
            2: " Dish MVNO deal (~2020) satisfied DOJ fourth-carrier theory with weak follow-through.",
            3: " SoftBank's Sprint debt and culture clash prevented standalone turnaround.",
            4: " Cingular/AT&T (2004) and T-Mobile/Metro (2013) precedents show 30-year consolidation rhythm.",
        },
        "components_append": (
            " Regulatory approval traded nominal four-carrier competition for accelerated 5G buildout "
            "commitments — standard US telecom bargain since Bell breakup era."
        ),
    },
    "acq-season-2-episode-6spotifys-direct-listing": {
        "competitive_append": (
            "\n\nSpotify's direct listing became CFO folklore: Slack (2019) and Coinbase (2021) copied the "
            "playbook, saving hundreds of millions in underwriting spread collectively. For SPOT holders, "
            "2018 listing was beginning of public scrutiny on label economics — gross margin expansion since "
            "came from podcasts, audiobooks, and scale renegotiations, not from eliminating the ~70% royalty "
            "pass-through. Acquired uses capital-markets mechanics to teach what most tech media skips: the "
            "IPO pop is not free money, it is a priced concession to bankers and favored allocators."
        ),
        "background_append": (
            "\n\nHosts diagram cap table liquidity: existing shareholders sell on day one without lock-up "
            "standard in traditional IPOs. They contrast Spotify's ~$4.1B revenue scale (2018) with "
            "typical IPO candidates raising primary capital — direct listing self-selects for maturity."
        ),
        "mental_append": (
            " Use direct listing when secondary liquidity is goal and brand awareness eliminates roadshow "
            "need; keep traditional IPO when primary capital and banker stabilization matter."
        ),
        "insight_answers_expand": {
            0: " Ek already raised ~$2.8B privately — listing was liquidity event not fundraise.",
            1: " Opening ~26% above $132 reference without primary dilution reframed 'pop' as fair discovery.",
            2: " Label pass-through ~70% capped gross margin — bulls needed podcast/ad optionality.",
            3: " Goldman/Morgan Stanley adapted playbook — institutional buyers bought at market day one.",
            4: " 157M MAUs proved freemium conversion at scale — quarterly reporting began post-listing.",
        },
        "components_append": (
            " No greenshoe stabilization meant first-hour volatility — acceptable trade for founders "
            "avoiding IPO underpricing that transfers wealth to flippers."
        ),
    },
    "acq-season-2-episode-5the-dropbox-ipo": {
        "competitive_append": (
            "\n\nPost-IPO Dropbox pivoted from pure sync to collaboration suite (Paper, Sign, Dash AI) as "
            "Google and Microsoft bundled storage free — validating hosts' COGS bear case. DBX trades at "
            "modest SaaS multiples versus high-growth peers because 2.3% conversion caps consumer upside while "
            "enterprise competition intensifies. The episode's freemium math (500M × 2.3% × ~$111 ARPU) "
            "remains canonical for PLG founders pitching seed through Series B. Box comparison shows timing "
            "matters: 2015 enterprise IPO vs 2018 consumer-scale IPO commanded different multiples on "
            "similar technology."
        ),
        "background_append": (
            "\n\nAcquired walks Houston's competitive set — Box enterprise-first, Google Drive OS-bundled, "
            "Apple iCloud ecosystem lock-in — and why Dropbox's neutral cross-platform stance won 2008–2015. "
            "S-1 infrastructure costs (exabyte storage on AWS) illustrate COGS linearity bears emphasize."
        ),
        "mental_append": (
            " Enterprise upsell (Dropbox Business) on same PLG funnel is the margin escape hatch when consumer "
            "ARPU hits free-tier ceiling."
        ),
        "insight_answers_expand": {
            0: " 11.5M paid users absolute scale exceeds most B2B SaaS customer counts entirely.",
            1: " Referral extra storage (250–500MB) turned users into zero-CAC acquisition channel.",
            2: " March 2018 window hot post-tax-reform — Spotify same month boosted tech IPO sentiment.",
            3: " 97.7% free users store exabytes — COGS scales linearly with data hoarding.",
            4: " Shadow IT adoption preceded IT-approved Dropbox Business upsell — classic bottom-up SaaS.",
        },
        "components_append": (
            " Referral loop plus invisible sync reliability created 10× better UX than incumbents in 2008 — "
            "product-led growth before the term existed in venture vocabulary."
        ),
    },
    "acq-season-2-episode-4softbank-fortress-and-the-vision-fund": {
        "competitive_append": (
            "\n\nWeWork's 2019 IPO collapse and Vision Fund write-downs reframed this episode's optimism — "
            "but Son's playbook (Alibaba, ARM, mega-checks) still explains 2017–2019 private-market "
            "inflation. 9984.T trades at holding-company discount to Alibaba stake plus SoftBank Corp "
            "mobile cash flow; Vision Fund marks remain volatile. Fortress integration proved Son needed "
            "US asset-management rails to deploy Gulf capital — $3.3B price trivial versus $100B ambition. "
            "Episode essential for understanding capital source behind Uber, Didi, and late-stage valuation "
            "anchors pre-2022 rate hikes."
        ),
        "background_append": (
            "\n\nHosts cover Son's 2000 dot-com near-bankruptcy and recovery — psychological foundation for "
            "extreme risk tolerance. They explain carried interest and why sovereign LPs (PIF $45B) accept "
            "SoftBank as outsourced tech allocator."
        ),
        "mental_append": (
            " Treat Vision Fund checks as market-price anchors — when SoftBank bids, competing VCs must "
            "match or concede late-stage deals."
        ),
        "insight_answers_expand": {
            0: " One Alibaba return psychologically justifies $100B fund risk appetite.",
            1: " Fortress ~$70B AUM provided credit and compliance rails for PIF capital.",
            2: " ARM IP in every phone — IoT/edge AI thesis predated ChatGPT by years.",
            3: " Uber ~$7.7B+ Vision Fund deployment set late-stage valuation ceiling industry-wide.",
            4: " Sprint ~$21.6B SoftBank entry linked to T-Mobile merger exit path.",
        },
        "components_append": (
            " PIF $45B commitment required US deployment infrastructure — Fortress acquisition was compliance "
            "and credit capability purchase, not hedge-fund alpha quest."
        ),
    },
    "acq-season-2-episode-2raising-a-seed-round-with-against-gravity-ceo-nick-fajt": {
        "competitive_append": (
            "\n\nRec Room's post-seed trajectory — 37M+ lifetime accounts, $100M+ Series D (2021), mobile "
            "as primary growth driver — validated Fajt's cross-platform thesis while VR install base stayed "
            "modest. For seed investors, episode demonstrates what 'good' looks like: live product demo, "
            "multiple term sheets, Sequoia lead with gaming-domain fit, and honest VR timing risk disclosure. "
            "Against Gravity rebrand to Rec Room clarified consumer brand. Meta-lesson: social gaming seeds "
            "are judged on community retention and cosmetics ARPU, not headset shipment forecasts."
        ),
        "background_append": (
            "\n\nBen contributes Pioneer Square Labs perspective on Seattle seed ecosystem — how local angels "
            "and Microsoft alumni de-risk hiring before Sand Hill leads. Fajt demos Rec Room live on air, "
            "showing social rooms and mini-games that convinced investors despite tiny VR TAM."
        ),
        "mental_append": (
            " Optimize seed process for partner fit and pro-rata rights, not last-dollar valuation — "
            "Fajt chose Sequoia for gaming pattern recognition."
        ),
        "insight_answers_expand": {
            0: " PS4/PC users without VR headsets still hosted Rec Room parties — TAM today not tomorrow.",
            1: " Option pool shuffle pre-money dilution explained live — common founder trap.",
            2: " Moderation and kid-safe design differentiated from Altspace corporate-meeting focus.",
            3: " Sequoia flew to Seattle demo — product quality beat geography bias.",
            4: " Cosmetics $0.99–$9.99 items scale with DAU — premium VR titles cap at install base.",
        },
        "components_append": (
            " Fajt's Hololens background informed spatial UX but Rec Room prioritized fun sessions over "
            "tech demos — community retention metrics mattered more than polygon counts in seed pitch."
        ),
        "facts_fix": {
            2: (
                "Free-to-play cosmetics monetization — avatar items typically $0.99–$9.99 — no gameplay "
                "pay-to-win; similar to Fortnite/Roblox economics Fajt cited in pitch."
            ),
            3: (
                "Seattle gaming cluster: 100+ game studios in metro area; proximity to Valve, Microsoft, "
                "and early Oculus relationships for distribution and talent."
            ),
        },
    },
}


def _apply_expand(data: dict, ep_id: str) -> None:
    patch = EXPAND.get(ep_id)
    if not patch:
        return
    if append := patch.get("competitive_append"):
        data["competitive_advantage"] = data["competitive_advantage"].rstrip() + append
    if append := patch.get("background_append"):
        data["background"] = data["background"].rstrip() + append
    if append := patch.get("mental_append"):
        data["mental_model"]["application"] = (
            data["mental_model"]["application"].rstrip() + append
        )
    if append := patch.get("components_append"):
        data["mental_model"]["components"] = (
            data["mental_model"]["components"].rstrip() + append
        )
    for idx, text in patch.get("facts_fix", {}).items():
        data["important_facts"][idx] = text
    for idx, extra in patch.get("insight_answers_expand", {}).items():
        data["key_insights"][idx]["answer"] = data["key_insights"][idx]["answer"].rstrip() + extra


def main() -> None:
    results: list[tuple[str, bool, int, str]] = []
    for ep_id, data in EPISODES.items():
        _apply_expand(data, ep_id)
        path = APPROVED / f"{ep_id}.json"
        path.write_text(json.dumps(data, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
        report = validate_summary(data, TMPL)
        status = "PASS" if report.passed else "FAIL"
        results.append((ep_id, report.passed, report.total_words, status))
        print(f"{status} {ep_id} words={report.total_words} min={report.min_total_words}")
        for issue in report.issues:
            print(f"  [{issue.severity}] {issue.section}: {issue.message}")

    print("\n--- Summary ---")
    for ep_id, passed, words, status in results:
        print(f"{'completed' if passed else 'failed'}: {ep_id} ({words} words)")


if __name__ == "__main__":
    main()
