"""Episode body content for acq batch 491-500."""
from scripts._write_acq_batch_491_500_common import base

EPISODES: dict[str, dict] = {}

EPISODES["acq-rolex"] = base(
    "acq-rolex",
    episode_rating={"overall": 5},
    keywords=["Vertical Integration", "Quartz Crisis", "Luxury Scale"],
    conclusion=(
        "Rolex sells over a million watches annually at ~$13,000 average retail — yet maintains waitlists and "
        "secondary-market premiums that pure luxury houses like Hermès cannot replicate at comparable unit volume. "
        "Ben and David trace a century from Hans Wilsdorf's 1905 London import business through the Hans Wilsdorf "
        "Foundation's 1960 ownership structure, the 1970s quartz crisis that destroyed 85% of Swiss market share, "
        "and deliberate restraint on production and advertising that turned scarcity into brand equity. Rolex now "
        "captures ~30% of Swiss watch industry revenue — triple Cartier or Omega — while remaining privately held "
        "with an estimated $50B+ cash hoard. The 2023 Bucherer acquisition verticalizes retail without abandoning "
        "the authorized-dealer model. The paradox: a tool-watch company that became the world's most desired luxury "
        "brand by refusing to optimize margins the way a public company would."
    ),
    background=(
        "Ben and David open with Rolex's central paradox: top-tier luxury status combined with million-unit annual "
        "production, waitlists despite selling ~$11B in watches, and movements that lose to a $10 Casio on accuracy. "
        "The episode traces Hans Wilsdorf founding Wilsdorf & Davis in 1905, pioneering waterproof Oyster cases and "
        "Perpetual self-winding movements, and transferring ownership to the Hans Wilsdorf Foundation in 1960 to "
        "ensure perpetual independence.\n\n"
        "The quartz crisis nearly destroyed Swiss mechanical watchmaking — market share fell from 85% (1945) to 15% "
        "(1980) — but Rolex doubled down on mechanical quality, vertical integration of movement production, and "
        "lifestyle marketing through explorers, pilots, and athletes rather than product-feature advertising. "
        "Updated analysis covers Morgan Stanley estimates of 30.3% Swiss industry revenue share, ~$3–4B estimated "
        "annual pre-tax earnings, the Paul Newman Daytona secondary-market catalyst (1986), and 2023's $5B rumored "
        "marketing spend plus Bucherer retail acquisition."
    ),
    important_facts=[
        "Rolex sells over 1 million watches annually at ~$13,000 average retail (~$11B revenue), capturing an estimated 30.3% of Swiss watch industry revenue — versus Cartier and Omega at 7.5% each and Patek Philippe at 5.6%. Morgan Stanley estimates the Swiss industry at $35B revenue with ~29% operating margins industry-wide; Rolex likely exceeds that.",
        "The 1970s quartz crisis collapsed Swiss global market share from 85% (1945 peak of 90M units) to 15% by 1980; Swiss firms fell from ~2,000 (1960) to fewer than 500 (1980). Rolex survived by vertically integrating movement production and refusing to chase fashion-quartz at $25 price points.",
        "Hans Wilsdorf transferred Rolex to the Hans Wilsdorf Foundation in 1960 — a charitable trust that owns the company today, donates ~300M Swiss francs annually, and accumulates an estimated $50B+ cash hoard from decades of ~$2–4B annual free cash flow with no public shareholders.",
        "Paul Newman's 1968 Daytona gift to his daughter's boyfriend sold for $17.5M (2017); Italian dealers in 1986 drove Paul Newman Daytonas from ~$200 to $30,000+, catalyzing modern watch collecting. Rolex brand awareness rose from ~20% (1978) to ~80% (1998) through sports sponsorship rather than product-feature ads.",
        "Rolex's 2023 Bucherer acquisition brought ~8% of retail distribution in-house; rumored marketing spend ~$5B annually. Paul Newman's personal Daytona sold for $17.5M (2017). Ben and David estimate plausible private valuation range of $40B–$200B with $100B+ as consensus floor.",
    ],
    mental_model={
        "name": "Controlled Scarcity at Scale",
        "components": (
            "Rolex multiplies two large numbers — meaningful luxury price (~$13K ASP) times meaningful volume (~1M units) — "
            "rather than optimizing either ultra-rare haute horlogerie or mass fashion watches. Vertical integration of "
            "movement production (the TSMC of watchmaking) ensures quality control and supply independence. The Hans "
            "Wilsdorf Foundation removes quarterly margin pressure, enabling decades-long brand investment. Authorized "
            "dealer networks and deliberate under-production create waitlists that reinforce desirability without "
            "traditional luxury advertising of product features."
        ),
        "application": (
            "When evaluating luxury businesses, distinguish managed scarcity from genuine rarity. Rolex proves a "
            "foundation-owned structure can compound brand equity across generations without IPO pressure — similar "
            "to Hermès family control but at higher unit volume. For investors, no public equity exists; the lesson "
            "generalizes to any category where vertical integration plus brand restraint beats margin maximization."
        ),
    },
    competitive_advantage=(
        "Rolex's moat stacks vertical integration, brand, and governance. In-house movement production — honed through "
        "the quartz crisis when competitors outsourced or quit — ensures supply security and quality consistency across "
        "a concentrated catalog of ~9 core models. The Oyster case, Perpetual rotor, and Cerachrom bezel create "
        "identifiable product language without annual fashion churn.\n\n"
        "Marketing invests in achievement association (explorers, tennis, golf, cinema) rather than spec sheets — "
        "building aspiration accessible to upper-middle-class professionals, not just billionaires. Authorized dealers "
        "maintain price discipline; grey-market premiums validate demand without Rolex capturing secondary gains "
        "directly.\n\n"
        "The Hans Wilsdorf Foundation structure eliminates takeover risk and short-term earnings pressure — enabling "
        "$5B marketing spend and Bucherer retail integration without shareholder revolt. Estimated $50B+ cash provides "
        "infinite runway.\n\n"
        "Weaknesses: counterfeiting, smartwatch time-telling obsolescence for utility buyers, and dealer-relationship "
        "tension when waitlists frustrate customers. Tudor (~<1% of production) serves as experimentation zone. "
        "Smartwatches (~80M units/year) compete for wrist real estate but not status signaling.\n\n"
        "Retail integration accelerated in 2023: Bucherer brought ~8% of distribution in-house while preserving authorized "
        "dealer network — solving service consistency without sacrificing scarcity signaling. Estimated $50B+ cash hoard "
        "and foundation ownership let Rolex absorb cyclical downturns (2008, 2020) without production panic that damaged "
        "competitors who discounted into weakness."
    ),
    key_insights=[
        {
            "view": "Rolex is luxury that scales like a car company, not a handbag house.",
            "question": "How does Rolex sell 1M units and stay exclusive?",
            "answer": "Average selling price ~$13,000 hits aspirational professionals — doctors, lawyers, finance, tech — not just the 0.1%. Hermès Birkin production is orders of magnitude smaller. Rolex multiplies two large numbers: price times volume. Mercedes/BMW analogy fits better than Ferrari; waitlists add scarcity without limiting to hundreds of units.",
        },
        {
            "view": "The quartz crisis was Rolex's defining strategic fork.",
            "question": "Why didn't Rolex die like most Swiss makers?",
            "answer": "When Seiko's quartz destroyed 85% Swiss share (1945–1980), Rolex refused the $25 fashion-watch path. They vertically integrated movements, maintained mechanical quality, and invested in brand. Swatch survived differently via cheap quartz; Rolex preserved mechanical prestige. By 1973 Swiss production peaked at 90M units then collapsed — Rolex emerged as the dominant survivor.",
        },
        {
            "view": "Foundation ownership is the ultimate competitive advantage.",
            "question": "Why does private structure matter?",
            "answer": "Hans Wilsdorf transferred Rolex to a charitable foundation in 1960 — no public shareholders, no LVMH takeover, no quarterly margin calls. Decades of ~$2–4B annual cash generation produced an estimated $50B+ hoard. Marketing spend (~$5B rumored) and Bucherer acquisition need no investor approval. Hermès trades at 60x earnings; Rolex would likely match but cannot be bought.",
        },
        {
            "view": "Movements are the semiconductor layer of watchmaking.",
            "question": "Why vertical integration?",
            "answer": "Case and dial are aesthetics; movement is performance — like TSMC for chips. Rolex produces movements in-house after the quartz crisis while competitors outsourced or exited. This ensures supply during boom cycles and quality consistency. Tudor shares movement technology at ~$4,000 price points as brand laboratory.",
        },
        {
            "view": "Secondary markets do Rolex's ultra-luxury marketing for free.",
            "question": "Why not raise retail prices to match grey market?",
            "answer": "Paul Newman Daytonas went from $200 to $30,000+ in 1986 without Rolex participation. Premiums on steel sports models signal desirability while retail stays accessible. Precious-metal models were easier to buy during 2020–22 hype because demand concentrated on steel. Secondary market lets Rolex participate in $100K+ segment without catalog complexity.",
        },
    ],
    top_investment_implications=[
        {
            "ticker": "RMS",
            "direction": "Watch",
            "confidence": "Medium",
            "thesis": "Hermès (~€290B market cap, ~60x earnings) is the closest public comp for foundation-like luxury with multi-decade brand compounding — useful benchmark for Rolex's estimated $100B+ private value, though Hermès lacks Rolex's unit volume.",
        },
        {
            "ticker": "CFR",
            "direction": "Watch",
            "confidence": "Low",
            "thesis": "Richemont (Cartier, 7.5% Swiss share) shows the gap: even a strong #2 captures a quarter of Rolex's revenue share — illustrating winner-take-most dynamics in accessible luxury watches.",
        },
    ],
    golden_quotes=[
        "\"Rolex is 30% of the revenue in the entire Swiss watch industry\" — Ben on Morgan Stanley/LuxeConsult estimates showing Rolex triples the nearest competitor.",
        "\"If you're a movement maker, you're like TSMC here\" — David on why vertical integration of calibers is the performance moat, not case aesthetics.",
        "\"There are plausible scenarios all the way from $40 billion to $200 billion\" — Ben on private valuation range for a company that will never trade publicly.",
    ],
    chronology={
        "subject": "Rolex · Hans Wilsdorf",
        "events": [
            {"date": "1905", "event": "Hans Wilsdorf and Alfred Davis found Wilsdorf & Davis in London"},
            {"date": "1926", "event": "Oyster waterproof case patented — proves viability by Mercedes Gleitze Channel swim"},
            {"date": "1931", "event": "Perpetual self-winding rotor introduced"},
            {"date": "1945", "event": "Swiss industry produces 19M of 21.5M global wristwatches — 85% share"},
            {"date": "1960", "event": "Hans Wilsdorf Foundation established; Rolex ownership transferred"},
            {"date": "1967", "event": "Sea-Dweller developed with COMEX for deep-sea saturation diving"},
            {"date": "1973", "event": "Swiss production peaks at ~90M units before quartz disruption"},
            {"date": "1980", "event": "Swiss global market share collapses to ~15%; Rolex doubles down on mechanical"},
            {"date": "1986", "event": "Italian dealers drive Paul Newman Daytona prices from ~$200 to $30,000+"},
            {"date": "1998", "event": "Rolex brand awareness reaches ~80% globally from ~20% in 1978"},
            {"date": "2012", "event": "Rolex moves to new Geneva campus; vertical integration accelerates"},
            {"date": "2020–22", "event": "Pandemic hype creates multi-year waitlists; steel models trade at premiums"},
            {"date": "2023", "event": "Rolex acquires Bucherer retail group; rumored ~$5B marketing spend"},
            {"date": "2025", "event": "Estimated ~$11B revenue; ~30.3% Swiss industry share; ~1M units at ~$13K ASP"},
        ],
    },
)

EPISODES["acq-costco"] = base(
    "acq-costco",
    episode_rating={"overall": 5},
    keywords=["Membership Model", "Sol Price", "Negative Cash Cycle"],
    conclusion=(
        "Costco is Sol Price's retail philosophy perfected at scale: treat customers as smart, cap markups at 14%, "
        "pay employees well, and let membership fees fund the model. Kirkland Signature (~$52B revenue) is the world's "
        "largest consumer packaged brand; the $1.50 hot dog combo unchanged for 47 years symbolizes institutional "
        "commitment to value over margin extraction. Ben and David trace FedMart → Price Club → Costco merger (1993), "
        "showing how negative cash conversion cycles, limited SKUs (~3,700 vs. 100,000+ at Walmart), and 93% US "
        "renewal rates compound into ~$230B revenue and ~$7.5B operating income at ~11% gross margins. The lesson: "
        "low margin percentage plus high trust equals one of retail's most durable franchises — Charlie Munger's "
        "favorite company for good reason."
    ),
    background=(
        "Ben and David frame Costco as the opposite of typical due diligence — the deeper you dig, the better it gets. "
        "The episode traces Sol Price's lineage from 1916 Bronx origins through Fedco-inspired FedMart (1954), Hugo "
        "Mann's hostile takeover that fired Sol at age 60, Price Club's 1976 warehouse launch, Jim Sinegal and Jeff "
        "Brotman's 1983 Costco, and the 1993 pseudo-merger-of-equals with Price Club.\n\n"
        "Core mechanics: membership as profit center (~70% of operating income), 14% markup cap, no loss leaders, "
        "manufacturer-direct delivery eliminating logistics costs, negative cash conversion cycle, and employee "
        "policies (avg $26/hr, 7% hourly attrition vs. 20% retail norm) that reduce shrink and training costs. "
        "Today: ~$1,800 revenue per square foot (3x Walmart), ~$269M average warehouse sales, and executive team "
        "tenures exceeding 25 years."
    ),
    important_facts=[
        "Kirkland Signature generates ~$52B annual revenue — edging Nike by ~$1B and excluding Kirkland gas — making it the world's largest consumer packaged brand. Costco operates ~$230B revenue with ~$7.5B operating income at ~11% gross margins capped at 14% markup.",
        "Membership economics: ~$60 base / ~$120 executive tiers; 93% US renewal rate; membership fees provide ~70% of operating income while retail contributes ~30%. Executive members (~45% of sales) receive 2% cashback capped at $1,000 — break-even designed around ~$3,000 annual household spend.",
        "Negative cash conversion cycle: net-30 supplier terms mean Costco often sells inventory before paying vendors — vendors effectively finance inventory. Combined with limited SKUs (~3,700 vs. 100,000+ at Walmart), average warehouse generates ~$269M/year at ~$1,800/sq ft (Walmart ~$600; Target ~$450).",
        "Employee economics: average hourly wage $26 vs. Walmart $19.50; 7% hourly attrition after year one vs. 20% retail norm; 36% of US employees have 10+ years tenure; 85%+ of managers promoted internally. Jim Sinegal started as FedMart grocery bagger; Craig Jelinek began as hourly employee.",
        "Sol Price lineage: first FedMart (1954) did $3M year-one sales vs. $1M expectation; Price Club launched 1976 after Sol was fired from FedMart; Costco-Price Club merger (1993) split 52/48 equity at ~$16B combined revenue growing from $3B (1989) in four years.",
    ],
    mental_model={
        "name": "Membership-Aligned Low Margin",
        "components": (
            "Costco caps markups at 14% and passes 89% of supplier savings to members — making membership the profit "
            "engine, not merchandise margin. High wages reduce turnover, shrink, and training costs — interlinked "
            "trade-offs Sol Price pioneered at FedMart. Limited SKUs (~3,700) concentrate buying power; "
            "manufacturer-direct delivery eliminates distribution. Negative cash conversion cycles turn inventory into "
            "float income. The $1.50 hot dog signals institutional commitment: we will not extract margin here."
        ),
        "application": (
            "Evaluate retailers on renewal rates and cash conversion, not gross margin percentage. Costco proves "
            "11% gross margin can produce ~$7.5B operating income when membership fees, turnover economics, and "
            "vendor financing align. The model requires decades of cultural reinforcement — competitors copying "
            "individual tactics without the full system fail."
        ),
    },
    competitive_advantage=(
        "Costco's moat is systemic, not any single tactic. Membership creates selection bias toward loyal, high-spend "
        "customers (93% renewal) while fees fund operations — Sam's Club and BJ's lack the same cultural commitment "
        "to markup caps. Kirkland Signature (~$52B) converts house-brand trust into margin-free customer value.\n\n"
        "Supply chain design eliminates Costco-owned logistics — manufacturers deliver to warehouses; business members "
        "(originally) and consumers pick up pallets. Negative cash conversion cycles and net-30 terms generate float.\n\n"
        "Employee economics reduce shrink and training costs: 7% attrition vs. 20% industry; internal promotion pipeline "
        "preserves Sol Price merchant culture across decades. Executive team stability (25+ year tenures) prevents "
        "consultant-driven margin expansion.\n\n"
        "Weaknesses: limited e-commerce versus Amazon; geographic saturation in US; no loss-leader flexibility versus "
        "Walmart promotional culture; and thin margins leave little room for operational errors. $1.50 hot dog subsidy "
        "is feature, not bug — but requires discipline everywhere else.\n\n"
        "Sam's Club and BJ's compete on warehouse format but neither matches the 14% markup cap codified in Costco's "
        "code of ethics — written under Washington State Liquor Board scrutiny in the 1980s. Wall Street perennially "
        "undervalued the model until membership economics and negative cash conversion became impossible to ignore; "
        "Charlie Munger's board seat and Berkshire-adjacent evangelism cemented Costco as the canonical trust-based retailer."
    ),
    key_insights=[
        {
            "view": "Costco makes money on memberships, not merchandise.",
            "question": "Is retail really break-even?",
            "answer": "Not quite — retail contributes ~30% of operating income. But ~70% comes from nearly 100% margin membership fees (~$4.5B). The popular 'retail is break-even' narrative captures the spirit: 11% gross margin merchandise exists to deliver member value, not extract margin. Executive 2% rewards program is designed to break even at ~$3,000 annual spend.",
        },
        {
            "view": "Sol Price invented both discount retail and warehouse clubs.",
            "question": "Why does lineage matter?",
            "answer": "FedMart (1954) pioneered for-profit membership clubs and no-loss-leader discipline before Walmart copied the discounter format. Fired at 60 by Hugo Mann (who wanted real estate, not operations), Sol created Price Club's warehouse model. Jim Sinegal learned 'everything' from Sol. Sam Walton admitted stealing more ideas from Sol than anyone else.",
        },
        {
            "view": "High wages are a cost-saving strategy.",
            "question": "Why pay $26/hour in low-margin retail?",
            "answer": "7% hourly attrition vs. 20% industry norm reduces training and onboarding costs. Low shrink — merchandise doesn't walk out the door. Internal promotion (85%+ managers) preserves culture. Harvard Business Review's 'High Cost of Low Wages' documented the Costco-Walmart comparison. Higher per-employee cost, lower total labor cost per dollar sold.",
        },
        {
            "view": "The hot dog is a governance mechanism.",
            "question": "Why keep $1.50 for 47 years?",
            "answer": "Hebrew National supplied the original cart; Costco now makes hot dogs in-house and sells 130M annually at $1.50 with soda refill. Refusing to raise price signals institutional commitment to member value over margin extraction — the anti-loss-leader philosophy. If you won't raise hot dog prices in 47 years of inflation, members trust you won't sneak margin elsewhere.",
        },
        {
            "view": "Negative cash conversion is the hidden engine.",
            "question": "How does 11% gross margin work financially?",
            "answer": "Net-30 payment terms mean Costco sells — sometimes 2-3 turns — before paying suppliers. Vendors finance inventory; Costco earns float. Combined with membership fee upfront cash and limited capital expenditure per SKU, the balance sheet works despite thin margins. Walmart invested tens of billions in logistics; Costco outsourced distribution to manufacturers.",
        },
    ],
    top_investment_implications=[
        {
            "ticker": "COST",
            "direction": "Long",
            "confidence": "High",
            "thesis": "Costco's ~$230B revenue, 93% renewal, and membership-funded model produce ~$7.5B highly defensible operating income — premium valuation (1.6x revenue) reflects multi-decade compounding at ~8% growth with unmatched trust.",
        },
        {
            "ticker": "WMT",
            "direction": "Watch",
            "confidence": "Medium",
            "thesis": "Sam's Club competes on price but lacks Costco's markup cap culture and Kirkland scale; Walmart's 2M+ employees vs. Costco's ~300K shows the productivity gap (~$1,800 vs. ~$600 sq ft revenue).",
        },
    ],
    golden_quotes=[
        "\"I didn't learn a lot, I learned everything\" — Jim Sinegal on Sol Price, capturing the direct lineage of Costco's philosophy.",
        "\"If you're going to ever do loss leaders, you're violating that tenet and saying we're going to get one over on our customers\" — Ben on why Costco refuses promotional retail tactics.",
        "\"Shoot me first\" — Warren Buffett's hijacker joke about hearing Charlie Munger's Costco speech one more time before dying.",
    ],
    chronology={
        "subject": "Costco · Sol Price",
        "events": [
            {"date": "1916", "event": "Solomon 'Sol' Price born in Bronx to Belarusian immigrant parents"},
            {"date": "1954", "event": "First FedMart opens San Diego — $3M year-one sales vs. $1M expected"},
            {"date": "1976", "event": "Sol Price and son Robert found Price Club after Sol fired from FedMart"},
            {"date": "1983", "event": "Jim Sinegal and Jeff Brotman found Costco in Seattle with $7.5M raised"},
            {"date": "1985", "event": "$1.50 hot dog and soda combo launched — price unchanged 47 years later"},
            {"date": "1989", "event": "Costco reaches $3B revenue — fastest company to milestone at the time"},
            {"date": "1993", "event": "Costco merges with Price Club — 52/48 equity split at ~$16B combined revenue"},
            {"date": "1997", "event": "Company renamed Costco Wholesale Corporation"},
            {"date": "2000s", "event": "Kirkland Signature becomes world's largest CPG brand by revenue"},
            {"date": "2010s", "event": "International expansion accelerates; e-commerce added cautiously"},
            {"date": "2020s", "event": "Revenue exceeds $230B; ~$1,800/sq ft; avg wage $26/hr; 93% US renewal"},
        ],
    },
)

# Part 2 - remaining episodes
EPISODES["acq-10-years-of-acquired-with-michael-lewis"] = base(
    "acq-10-years-of-acquired-with-michael-lewis",
    episode_rating={"overall": 4},
    keywords=["Podcast Economics", "Circle of Competence", "Partnership"],
    conclusion=(
        "Ten years in, Ben and David invite Michael Lewis to the Menlo Park garage where Google started to ask why "
        "Acquired succeeded where 99% of podcasts fail. The answer blends Berkshire-style circle of competence, "
        "Sequoia-like partnership discipline, and Hermès-inspired quality scarcity — only ~15 episodes per year, "
        "each consuming a month of research. Lewis reframes their work as narrative non-fiction with a business "
        " lens: find obscurity-to-ubiquity hero journeys with secrets hiding in plain sight. The episode meta-analyzes "
        "Acquired's sponsor strategy (enterprise deals, not CPM ads), true subscriber distribution without algorithmic "
        "disintermediation, and terror-driven quality control. Unlike Lewis's books that create phenomena from obscurity, "
        "Acquired covers companies audiences already love — the craft is revealing the machine behind familiar brands."
    ),
    background=(
        "Recorded in Google's original Menlo Park garage during the Fall 2025 season finale, Ben and David depart from "
        "holiday-special tradition to examine Acquired itself with Michael Lewis — author of Moneyball, Liar's Poker, "
        "and host of Against the Rules. Lewis probes why studying great companies might have osmosed into Acquired's "
        "own durability.\n\n"
        "The conversation covers David's French-literature thesis on Dom Pérignon (later becoming the LVMH episode), "
        "Ben's venture background versus David's storytelling strength, lessons from Berkshire (circle of competence, "
        "too-hard pile), Sequoia (partnership as profane alternative to solo host), Hermès (quality and scarcity), "
        "and the economics of premium sponsorship targeting multimillion-dollar enterprise deals rather than programmatic ads."
    ),
    important_facts=[
        "Acquired launched in 2015; by 2025 the show produces ~15 episodes per year versus weekly schedules at most podcasts — each episode requiring roughly a month of research, reflecting Hermès-inspired quality scarcity.",
        "David went full-time on Acquired in 2020; Ben followed full-time in late 2023/early 2024 — a five-year staggered transition mirroring Sequoia's partnership patience.",
        "True podcast subscription differs from YouTube/Twitter follows: Apple Podcasts and Spotify subscribers receive every episode without algorithmic disintermediation — Ben cites ~4 billion global internet users making any niche massive online.",
        "Sponsor strategy targets companies doing multimillion-dollar annual enterprise deals; Ben and David report sponsors often ROI-positive from a single large customer acquired via Acquired plus co-hosted events — planning partners 1–2 years ahead.",
        "Lewis recorded in the literal garage where Google started (~$4T company); the venue caps the three-part Google series season. First ad sold was chosen specifically to signal quality brand perception.",
    ],
    mental_model={
        "name": "Scarcity-Quality Compounding",
        "components": (
            "Acquired applies lessons from subjects it covers: Berkshire's circle of competence (large too-hard pile), "
            "Hermès quality scarcity (~15 episodes/year), Sequoia partnership discipline (two hosts, non-negotiable), "
            "and Costco-style trust (no loss-leader content). True podcast subscriptions create direct audience "
            "relationships without algorithmic intermediation. Terror of disappointing subscribers drives quality. "
            "Enterprise sponsor model aligns with B2B companies where one incremental deal repays annual sponsorship."
        ),
        "application": (
            "For media businesses, frequency and quality trade off more sharply than growth metrics suggest. "
            "Acquired proves niche topics reach millions globally on the internet. Partnership structures beat solo "
            "host fragility for decade-long compounding. Sponsor selection as brand signal — not just revenue — "
            "reinforces positioning."
        ),
    },
    competitive_advantage=(
        "Acquired's moat is research depth plus brand trust accumulated over 10 years. ~15 episodes annually creates "
        "scarcity that weekly competitors cannot replicate without diluting quality. Two-host partnership (Ben analysis, "
        "David narrative) prevents single-point-of-failure and enables month-long production cycles.\n\n"
        "True subscriber distribution on Apple/Spotify bypasses algorithmic risk plaguing YouTube-first creators. "
        "Audience follows from LVMH to Epic Systems to healthcare IT — cross-topic loyalty rare in podcasting.\n\n"
        "Enterprise sponsor model (multimillion-dollar deal targets, co-hosted events) selects for B2B brands where "
        "Acquired delivers measurable pipeline — avoiding CPM race-to-bottom. First sponsor chosen for brand elevation, "
        "not maximum rate.\n\n"
        "Weaknesses: production intensity caps scale; dependency on two hosts; no algorithmic discovery engine for "
        "new audience; and meta-episode risk of naval-gazing. Lewis notes Acquired covers known brands versus his "
        "obscurity-to-fame book model — different creative challenge.\n\n"
        "Live events (Chase Center ~6,000 attendees, AWS re:Invent Venetian Theater CEO series) extend the brand beyond "
        "audio without diluting episode scarcity. Ben and David's complementary skills — venture/product analysis versus "
        "French-literature narrative research — mirror Berkshire's Munger-Buffett division of cognitive labor applied "
        "to media."
    ),
    key_insights=[
        {
            "view": "Acquired applies its subjects' playbooks to itself.",
            "question": "What did Berkshire teach the show?",
            "answer": "Circle of competence and a large too-hard pile — intelligent nos. Not every company deserves an episode. Buffett's durability lesson also resonated: lean into compounding over decades after initially undervaluing that frame. Quality over frequency.",
        },
        {
            "view": "Partnership is non-negotiable.",
            "question": "Why two hosts for 10 years?",
            "answer": "David went full-time 2020; Ben followed ~2024. Acquired has always been two people — 'profane' to consider otherwise, echoing Sequoia's partnership model. Ben brings analysis and products background; David brings narrative and research storytelling. Complementary, not interchangeable.",
        },
        {
            "view": "True subscription beats algorithmic follow.",
            "question": "Why does podcast distribution matter?",
            "answer": "Apple/Spotify subscribers receive every episode — unlike YouTube or Twitter where follow is algorithm input, not guarantee. When Acquired publishes, the base comes along: LVMH listeners learn healthcare IT on Epic Systems. Cross-topic loyalty requires direct subscription relationship.",
        },
        {
            "view": "Three ingredients for great episodes.",
            "question": "What makes a company Acquired-worthy?",
            "answer": "Ben's framework: (1) hero's journey from obscurity to ubiquity, (2) secret hiding in plain sight — Costco gears visible after listening, (3) compelling protagonist. Differs from Lewis's model of creating phenomena from obscurity — Acquired reveals machinery behind brands audiences already love.",
        },
        {
            "view": "Enterprise sponsors match the audience.",
            "question": "Why not maximize ad inventory?",
            "answer": "Sponsors must target multimillion-dollar annual enterprise deals — one incremental customer repays sponsorship. Co-hosted events put sponsors next to best prospects. First ad sold specifically to signal quality brand. Planning sponsors 1-2 years ahead like strategic partnerships, not programmatic CPM.",
        },
    ],
    top_investment_implications=[
        {
            "ticker": "SPOT",
            "direction": "Watch",
            "confidence": "Low",
            "thesis": "Spotify's podcast investments compete on volume; Acquired's model suggests durable value accrues to direct-subscriber shows with premium production — a niche within Spotify's broader podcast strategy.",
        },
    ],
    golden_quotes=[
        "\"Why Acquired worked when 99% of podcasts do not\" — Ben framing the meta-episode with Michael Lewis.",
        "\"It would be profane for it to be anything other than the two of us\" — David on Acquired's partnership structure.",
        "\"There's a secret hiding in plain sight like Costco\" — Ben's framework for great episodes where listeners see gears turning after the show.",
    ],
    chronology={
        "subject": "Acquired · Ben Gilbert & David Rosenthal",
        "events": [
            {"date": "2015", "event": "Acquired launches; first episodes published"},
            {"date": "2015", "event": "Dom Pérignon vintage released — same year show started; David's thesis topic"},
            {"date": "2020", "event": "David goes full-time on Acquired"},
            {"date": "2021–23", "event": "Show adopts quality scarcity — ~15 episodes per year"},
            {"date": "2023–24", "event": "Ben goes full-time; Chase Center live event era begins"},
            {"date": "2024", "event": "Hermès, Costco, NFL remaster — peak production values"},
            {"date": "2025", "event": "Three-part Google series; 10-year anniversary"},
            {"date": "2024", "event": "Chase Center live show with Jamie Dimon; ~6,000 in-person attendees"},
            {"date": "Fall 2025", "event": "AWS re:Invent Venetian Theater CEO interview series at Reinvent"},
            {"date": "Dec 2025", "event": "Michael Lewis interview recorded in Google's original garage"},
        ],
    },
)

EPISODES["acq-coca-cola"] = base(
    "acq-coca-cola",
    episode_rating={"overall": 5},
    keywords=["Franchise Bottling", "Brand Marketing", "Secret Formula"],
    conclusion=(
        "Coca-Cola is syrup, sugar, and water — yet a ~$300B company serving 2.2 billion drinks daily across a "
        "system generating ~$175B in total revenue. Ben and David trace 139 years from Atlanta pharmacist John Pemberton "
        "through Asa Candler's $2,300 full acquisition (1891), the $1-per-gallon perpetual bottler contracts that "
        "nearly destroyed the company, Robert Woodruff's Depression-era marketing genius, and the New Coke disaster. "
        "The asset-light bottling franchise — 200 partners, 950 facilities — produces 60% gross margins on $47B "
        "concentrate revenue while bottlers take capital intensity. Munger's $2M-to-$2T thought experiment fails: "
        "Coca-Cola threw off billions in dividends but growth slowed to 3–4% post-1998. The enduring lesson is "
        "brand plus distribution architecture beats product complexity — though sugar headwinds and Pepsi competition "
        "prevent the Lollapalooza outcome Charlie imagined."
    ),
    background=(
        "Ben and David frame Coca-Cola through Charlie Munger's thought experiment: build a non-alcoholic beverage "
        "company from $2M to $2T with massive dividends along the way. The episode covers Pemberton's 1886 cocaine-wine "
        "precursor, Candler's fountain-syrup franchise model, the mistaken 1899 $1-per-gallon bottling contract sold "
        "for $1, Woodruff's WWII global expansion (5–10B bottles to troops), Pepsi's 1975 blind taste test era, "
        "New Coke (1985), and Buffett's $1.3B stake now worth ~$28B with ~$1B annual dividends.\n\n"
        "Modern Coca-Cola Company ($47B revenue, ~$10.6B net income, 23% net margins) owns brands while bottlers deploy "
        "capital. Thirty $1B+ brands — 15 created organically, 3 acquired at scale, 12 grown from small — serve "
        "2.2B daily servings in a 65B daily global beverage market. US share fell from ~60% (1948) to competitive parity with Pepsi."
    ),
    important_facts=[
        "Coca-Cola serves 2.2 billion beverage servings daily from 200 bottling partners operating 950 facilities; the Coca-Cola Company itself reports $47B revenue and ~$10.6B net income (23% margin) on concentrate, while the total system generates ~$175B revenue.",
        "Asa Candler acquired full Coca-Cola ownership for $2,300 (1891); first official year (1892) spent ~$20K on production and ~$10K on advertising against ~$250K marketplace gross revenue at soda fountains charging $6.40/gallon — 80% fountain margins drove adoption.",
        "The 1899 $1-per-gallon perpetual bottling contract (sold for $1) locked syrup pricing for decades; inflation made $1/gallon untenable until renegotiation. By 1948 Coca-Cola held ~60% US soft drink share; Pepsi's 1975 Challenge and Steel-era marketing eroded this to ~35% by 1955.",
        "WWII global expansion: 64 portable bottling plants shipped abroad; 5–10 billion bottles distributed to troops, seeding international brand recognition. Diet Coke became #1 diet drink in America by end of 1983 first full year; New Coke (1985) retained only ~3% share after Classic relaunch.",
        "Buffett's Berkshire bought ~$1.3B stake (1988–89), now ~9.5% worth ~$28B — 22x gross return but ~8% IRR underperforming S&P 500's ~11% including dividends; however Berkshire receives ~$800M–$1B annual dividends (~60–80% yield on original investment).",
    ],
    mental_model={
        "name": "Asset-Light Brand Franchise",
        "components": (
            "Coca-Cola sells branded concentrate, not finished drinks — bottlers provide capital, logistics, and local "
            "relationships while the company maintains 60% gross margins on syrup. Fountain sales (80% retailer margins) "
            "created initial adoption; bottling scaled distribution but the $1/gallon contract mistake nearly broke economics. "
            "Marketing invests in lifestyle association (happiness, Americana, Santa Claus) not ingredient claims. "
            "Portfolio strategy: 30 $1B+ brands across categories reduce single-product sugar exposure."
        ),
        "application": (
            "Separate brand ownership from capital deployment when scaling physical goods globally. Coca-Cola's mistake "
            "— perpetual fixed-price bottling contracts — teaches that franchise terms must inflation-adjust. For "
            "investors, KO is a dividend compounder with mature 3–4% growth, not a Munger Lollapalooza — brand moat "
            "remains but category growth constrained."
        ),
    },
    competitive_advantage=(
        "Coca-Cola's moat is brand plus distribution architecture spanning 139 years. The secret formula mythology, "
        "contour bottle (99% American recognition by 1940s), and consistent red identity create switching costs in "
        "consumer habit, not product taste — blind tests favored Pepsi yet Coke retained share for decades.\n\n"
        "Asset-light concentrate model generates 60% gross margins while 200 bottling partners deploy capital globally. "
        "Fountain channel (80% retailer margins) aligned incentives for early drugstore adoption; WWII planted global "
        "infrastructure via 64 portable plants.\n\n"
        "Marketing mastery under Woodruff and Goizueta: Santa Claus imagery, Olympic sponsorship, and 'share a Coke' "
        "campaigns maintain cultural relevance. Portfolio diversification (Monster 20% stake, $4B Glaceau, 30 $1B brands) "
        "extends beyond core cola.\n\n"
        "Weaknesses: sugar/health headwinds, Pepsi competitive parity, New Coke brand-trust scar, and Buffett investment "
        "underperforming S&P on IRR despite massive dividends. Plastic bottle environmental concerns; Munger's $2T target "
        "unreachable by 2036 150th birthday at 3–4% growth.\n\n"
        "Goizueta-era diversification (Minute Maid, Columbia Pictures briefly, global bottler refranchising) showed "
        "management could extend beyond cola — but core concentrate economics remain the engine. Monster Energy stake "
        "(20%, $2B+ invested) and BodyArmor acquisition reflect continued portfolio hedging against core cola stagnation "
        "in developed markets."
    ),
    key_insights=[
        {
            "view": "The bottling contract almost killed the golden goose.",
            "question": "What was the $1/gallon mistake?",
            "answer": "Candler sold bottling rights in 1899 for $1 with perpetual $1/gallon syrup pricing — no inflation adjustment. As costs rose, economics broke until renegotiation. The franchise model was genius (no capital investment, 80% fountain margins for drugstores) but fixed pricing nearly destroyed concentrate profitability.",
        },
        {
            "view": "Brand beats taste in blind tests.",
            "question": "Why did New Coke fail despite winning taste tests?",
            "answer": "Pepsi's Challenge (1975–85) showed consumers preferred Pepsi in blind tests; Coke share declined every year. New Coke (1985) tested better but abandoned 100 years of brand identity — Classic relaunch saved the company while New Coke retained ~3% share. Identity and habit trump palate.",
        },
        {
            "view": "WWII was Coca-Cola's global distribution event.",
            "question": "How did a US soda become worldwide?",
            "answer": "Woodruff pledged Coke at 5¢ for every serviceman; 64 portable bottling plants shipped to Europe, Asia, and North Africa. 5–10 billion bottles reached troops who returned home with brand loyalty. The US government loved leaving American symbol worldwide. Seeded infrastructure competitors couldn't replicate quickly.",
        },
        {
            "view": "Buffett's KO stake is a dividend miracle, not IRR triumph.",
            "question": "Was Berkshire's Coca-Cola investment great?",
            "answer": "~$1.3B invested (1988–89), now ~9.5% worth ~$28B — 22x gross but ~8% IRR vs. S&P ~11% with dividends. However ~$800M–$1B annual dividends equal 60–80% yield on original cost. Munger's Lollapalooza frame captures dividends; IRR frame shows mature-brand limits.",
        },
        {
            "view": "Munger's $2T thought experiment reveals the ceiling.",
            "question": "Why isn't Coca-Cola worth $2T?",
            "answer": "At ~$300B market cap with 3–4% post-1998 growth, reaching $2T by 2036 requires impossible compounding. The company executed Munger's playbook — global brand, bottler franchise, massive dividends — but category saturation and health trends cap upside. Pre-1998 history is the remarkable era.",
        },
    ],
    top_investment_implications=[
        {
            "ticker": "KO",
            "direction": "Watch",
            "confidence": "Medium",
            "thesis": "Coca-Cola remains a dividend aristocrat with ~$1B flowing to Berkshire annually — brand moat intact but 3–4% growth limits capital appreciation; mature compounder not Lollapalooza.",
        },
        {
            "ticker": "PEP",
            "direction": "Watch",
            "confidence": "Medium",
            "thesis": "PepsiCo's Frito-Lay diversification and Gatorade (~60%+ sports drink share) provide growth Coca-Cola lacks — different risk profile despite cola parity.",
        },
    ],
    golden_quotes=[
        "\"We're about to do a four hour podcast on syrup, sugar, and water\" — Ben opening on a ~$300B company built from three ingredients.",
        "\"99% of America could look at it and say that's a Coke bottle\" — on the contour bottle's instant recognition achieved by the 1940s.",
        "\"Make Coca-Cola the most American thing in America\" — Robert Woodruff's lieutenants on the brand's deliberate cultural positioning.",
    ],
    chronology={
        "subject": "Coca-Cola",
        "events": [
            {"date": "1886", "event": "John Pemberton creates Coca-Cola in Atlanta pharmacy"},
            {"date": "1891", "event": "Asa Candler acquires full company for $2,300"},
            {"date": "1899", "event": "Bottling rights sold for $1 with perpetual $1/gallon syrup contract"},
            {"date": "1915", "event": "Contour bottle designed — 99% US recognition by 1940s"},
            {"date": "1923", "event": "Robert Woodruff becomes president; begins modern marketing era"},
            {"date": "1941–45", "event": "WWII global expansion — 64 portable plants; 5–10B bottles to troops"},
            {"date": "1975", "event": "Pepsi Challenge launches — blind taste tests erode Coke share"},
            {"date": "Apr 1985", "event": "New Coke launched; Classic returns after consumer revolt"},
            {"date": "1988–89", "event": "Buffett buys ~$1.3B stake — now ~9.5% of company"},
            {"date": "2015", "event": "Coca-Cola invests $2B+ in Monster Energy — becomes largest shareholder"},
            {"date": "2025", "event": "~$300B market cap; 2.2B daily servings; 3–4% growth; 30 $1B+ brands"},
        ],
    },
)

EPISODES["acq-trader-joes"] = base(
    "acq-trader-joes",
    episode_rating={"overall": 5},
    keywords=["Private Label", "Aldi Nord", "Merchant Culture"],
    conclusion=(
        "Trader Joe's is a ~$24–25B private grocery business doing $2,000+ per square foot — double Whole Foods and "
        "4x industry average — with ~80% private label, deliberately small stores, and cult customer loyalty. Ben and "
        "David trace Joe Coulombe's 1967 Pronto Markets buyout ($25,000, employees co-invested), the 1960s "
        "747-driven globalization insight, and 1979 sale to Aldi Nord's Theo Albrecht — who let Joe run it another "
        "decade. Two Buck Chuck (Charles Shaw label bought for $27,000; 1B+ bottles sold) exemplifies the model: "
        "absolute margin dollars over margin percentages, curated SKUs (~4,000), and crew paid 40–60% above market "
        "with ~5–6% turnover. The episode reveals why Aldi-owned Trader Joe's avoids Aldi branding — and why estimated "
        "~$32–35B private valuation rivals 7-Eleven despite no public markets."
    ),
    background=(
        "Ben and David open with 7-Eleven trivia — Southland invented the to-go coffee cup and self-serve soda fountain; "
        "7-Eleven Japan eventually bought its American parent — before pivoting to Joe Coulombe's 1958 Rexall Pronto "
        "Markets and 1962 employee-backed buyout. The 747 (1965) halved European travel costs 50% and cut real costs "
        "15x within a decade — Joe bet educated Americans would want adventurous private-label foods.\n\n"
        "Core tactics: ~80% Trader Joe's private label, flexible markup focused on absolute margin dollars per square "
        "inch, wine merchant strategy (Two Buck Chuck via Bronco Wines' $27,000 label purchase), small stores with "
        "intentionally crowded parking, and counter-positioning toward non-family urban shoppers. Aldi Nord acquired "
        "100% in 1979; revenue grew from ~$1B (late 1990s) to $20B+ (2023) at ~10% store growth and ~11% revenue growth."
    ),
    important_facts=[
        "Trader Joe's estimated ~$24–25B revenue (2025) from ~600 US stores at $2,000+ sales per square foot — highest in grocery, 2x Whole Foods and 4x industry average; top stores generate $300–400M annually.",
        "Joe Coulombe bought six Pronto Markets in 1962 for $25,000 ($10K above book); employees co-invested at 40% discount to his price. Sold 100% to Aldi Nord's Theo Albrecht in 1979; Joe remained CEO until 1988 retirement.",
        "Private label exceeds 80% of SKUs; Charles Shaw wine label bought from bankruptcy for $27,000 (1995); Two Buck Chuck launched 2002 — 1B+ bottles sold (likely 2–3B now), representing ~10% of Trader Joe's 40M annual wine bottle sales.",
        "Employee turnover ~5–6% annually vs. industry ~60%+; crew paid 40–60% above market with 15–20% store discount, 15% retirement contribution, and healthcare. Gross margins ~22–25% vs. grocery industry ~27–30% — lower margins by design.",
        "7-Eleven market cap ~$30B (Japanese public company); Trader Joe's estimated ~$32–35B private valuation at ~1x+ revenue — comparable scale despite zero public float. Aldi Nord ownership since 1979 with no Aldi branding in US.",
    ],
    mental_model={
        "name": "Curated Private Label Density",
        "components": (
            "Trader Joe's optimizes absolute margin dollars per square inch, not margin percentage — a $20 item with "
            "$2 margin beats $4 item with $1 margin if shelf space is the constraint. ~80% private label eliminates "
            "brand tax and creates unique products competitors cannot price-match. Small stores, limited SKUs (~4,000), "
            "and intentional scarcity (crowded parking, single locations per market) reduce comparison shopping. "
            "Overpaid employees (~5–6% turnover) deliver experience that IS the product."
        ),
        "application": (
            "In retail, SKU curation beats assortment breadth for targeted demographics. Private label works when the "
            "retailer IS the trusted brand — not as generic store-brand discount. Counter-positioning (non-family urban "
            "shoppers vs. suburban family grocers) creates defensible niche. Private ownership enables decades-long "
            "compounding without quarterly earnings pressure."
        ),
    },
    competitive_advantage=(
        "Trader Joe's moat is merchant culture plus private-label density in a counter-positioned demographic. "
        "Joe Coulombe's educated-consumer insight (747 travel, UCLA demographics research) created adventurous "
        "assortment competitors won't replicate for mass-market families.\n\n"
        "Private label (~80%) eliminates national brand slotting fees and creates products only available at TJ's — "
        "Charles Shaw ($27K label, 1B+ bottles) demonstrates extreme case. Flexible markup optimizes shelf economics, "
        "not category margin targets.\n\n"
        "Aldi Nord ownership since 1979 provides permanent capital without US Aldi brand confusion. ~11% revenue "
        "growth for 20+ years with ~10% annual store growth compounds quietly.\n\n"
        "Weaknesses: limited geographic footprint (primarily US coastal/urban); no e-commerce scale; small stores "
        "frustrate bulk buyers; and succession risk after Joe's 1988 departure (mitigated by Aldi patience). "
        "Cannot serve family weekly-stock-up trips — deliberate counter-positioning limits TAM.\n\n"
        "Estimated ~$32–35B valuation on ~$24–25B revenue compares to Kroger (~0.3x revenue) and Albertsons (~0.1x) "
        "despite faster growth — private ownership and Aldi Nord patience command premium multiples similar to Costco's "
        "1.6x despite lower absolute scale. The Bronco Wines partnership on Charles Shaw demonstrates supplier "
        "relationship depth competitors cannot replicate at $1.99–$3.99 price points."
    ),
    key_insights=[
        {
            "view": "Shelf square inches are the scarce resource.",
            "question": "Why not optimize margin percentage?",
            "answer": "Trader Joe's focuses absolute margin dollars per shelf inch — $20 item yielding $2 beats $4 item yielding $1. Paper towels and bulky low-density goods avoided. Wine, cheese, and specialty items maximize revenue density. Opposite of Costco's warehouse volume strategy applied to small urban stores.",
        },
        {
            "view": "Two Buck Chuck is the perfect TJ's product.",
            "question": "How does a $27,000 label sell billions?",
            "answer": "Charles Shaw brand bought from bankruptcy (1995) for $27,000 — label only, no winery. Bronco Wines' Fred Franzia launched at $1.99 (2002) when industry said impossible. 1B+ bottles sold; ~10% of TJ's 40M annual wine bottles. Absolute margin on high-velocity wine drives profit without premium positioning.",
        },
        {
            "view": "The 747 changed grocery assortment.",
            "question": "Why exotic foods in 1967?",
            "answer": "Boeing 747 (1965) cut transatlantic travel costs 50%; real European travel costs fell 15x in a decade. Joe Coulombe read UCLA demographics — educated Americans would travel and want imported foods at home. Pronto Markets pivoted to Trader Joe's (1967) with Hawaiian shirts and adventurous private label.",
        },
        {
            "view": "Aldi ownership enables patience.",
            "question": "Why sell to Aldi Nord in 1979?",
            "answer": "Joe faced 73% marginal tax rate on personal income flowing through; Aldi Nord's Theo Albrecht bought 100% while Joe stayed CEO until 1988. Revenue grew ~$1B to $20B+ under Aldi without US Aldi branding conflict. Private ownership avoids quarterly pressure that would force margin expansion.",
        },
        {
            "view": "Crowded stores are a feature.",
            "question": "Why terrible parking lots?",
            "answer": "Counter-positioning toward non-family urban professionals — individual servings, small carts, crowded aisles filter for target customer. Whole Foods and Kroger optimize for family stock-up; TJ's optimizes for experience density. 5–6% employee turnover preserves culture that defines the brand.",
        },
    ],
    top_investment_implications=[
        {
            "ticker": "PRIVATE",
            "direction": "Watch",
            "confidence": "Medium",
            "thesis": "Trader Joe's (~$32–35B estimated, Aldi Nord-owned) demonstrates private grocery can compound at ~11% revenue growth without public markets — no direct investment but benchmark for Sprouts/Fresh Market niche players.",
        },
    ],
    golden_quotes=[
        "\"Start as a billionaire\" — the winemaker aphorism for Bronco Wines' Fred Franzia, who made Two Buck Chuck work at $1.99.",
        "\"$27,000\" — David on Bronco Wines buying the Charles Shaw label from bankruptcy, now 1B+ bottles sold through Trader Joe's.",
        "\"Crowded stores? Great. Small parking lots? Great. Individual servings? Great\" — Trader Joe's counter-positioning against family-focused grocers.",
    ],
    chronology={
        "subject": "Trader Joe's · Joe Coulombe",
        "events": [
            {"date": "1958", "event": "Joe Coulombe joins Rexall Pronto Markets in Los Angeles"},
            {"date": "1962", "event": "Joe and employees buy six Pronto stores for $25,000"},
            {"date": "1967", "event": "Pronto Markets renamed Trader Joe's — Hawaiian shirt branding begins"},
            {"date": "1979", "event": "Theo Albrecht (Aldi Nord) acquires 100%; Joe remains CEO"},
            {"date": "1988", "event": "Joe Coulombe retires; Aldi Nord continues private ownership"},
            {"date": "1995", "event": "Bronco Wines buys Charles Shaw label from bankruptcy for $27,000"},
            {"date": "2002", "event": "Two Buck Chuck launches at $1.99 — industry thought impossible"},
            {"date": "2009", "event": "400M Charles Shaw bottles sold; growth accelerating"},
            {"date": "2023", "event": "Revenue exceeds $20B; ~600 stores; CEO reports on Acquired"},
            {"date": "2025", "event": "Estimated ~$24–25B revenue; $2,000+ sq ft sales; ~$32–35B valuation"},
        ],
    },
)

EPISODES["acq-google-the-ai-company"] = base(
    "acq-google-the-ai-company",
    episode_rating={"overall": 5},
    keywords=["DeepMind", "Transformer", "Gemini"],
    conclusion=(
        "Google Part III argues the search company was always an AI company — and that buying DeepMind for $550M "
        "(2014) may be worth $500B today while indirectly birthing OpenAI. Ben and David trace Brain's cat paper "
        "(2012), the Hinton auction ($40M+ to Google), Transformer authors (2017), and the organizational split "
        "between DeepMind London and Google Brain that delayed product integration. DeepMind's acquisition triggered "
        "Elon Musk and Sam Altman to found OpenAI when researchers wanted open publication Google wouldn't allow. "
        "Gemini finally unifies the stacks under Sundar Pichai, but the episode's tension is clear: Google invented "
        "the modern AI era yet nearly gave it away through talent exodus and product paralysis between 2013 and 2023."
    ),
    background=(
        "The third Google episode opens at the 2024 Gemini demo and rewinds to show Google employed Ilya Sutskever, "
        "Geoff Hinton, the Transformer paper's eight authors, and DeepMind's Demis Hassabis before any became external "
        "competitors. Brain's 2012 cat-recognition paper and AlexNet (40% better than next ImageNet entry) proved "
        "deep learning worked at scale; Google won the Hinton auction against Baidu and Microsoft.\n\n"
        "DeepMind ($550M, 2014) stayed independent in London while Brain integrated into products. Musk, Thiel, and "
        "Altman founded OpenAI (2015) after DeepMind's closed research model frustrated open-science advocates. "
        "Transformer (2017) emerged from Google Brain; GPT followed elsewhere. Gemini merges DeepMind and Brain "
        "(2023) as Google's response to ChatGPT — ending a decade where Google launched everything except search "
        "(2003–2013) then nearly nothing new until Gemini."
    ),
    important_facts=[
        "Google acquired DeepMind for $550M (2014); Ben and David estimate standalone value ~$500B today — comparing to YouTube ($1.65B, 2006) as greatest acquisition tier. Geoff Hinton's DNN Research auction reached ~$40M+ with Baidu and Google bidding; Hinton ran structured hourly auction.",
        "AlexNet (2012) achieved 40% better ImageNet accuracy than next competitor using two GPUs retailing ~$1,000 each — proving deep learning scaled. Brain's cat paper (2012) trained on 10M YouTube frames across 2,000 computers with 16,000 cores.",
        "Eight Google researchers co-authored 'Attention Is All You Need' (2017 Transformer paper); all eight eventually left — founding Character.AI, Cohere, OpenAI contributions, and other labs. Google invented the architecture powering ChatGPT but didn't productize it first.",
        "OpenAI founded 2015 with ~$1B pledged (Musk, Altman, Thiel, Hoffman) after DeepMind acquisition closed research; ~7 researchers left Google initially. Elon offered to buy DeepMind with Tesla stock when Facebook bid ~$800M; Larry Page won at $550M.",
        "Google's 2003–2013 decade launched Gmail, Maps, Android, Chrome, YouTube acquisition, and AdSense; 2013–2023 produced no major new consumer products until Gemini — while AI talent and architectures originated inside Google.",
    ],
    mental_model={
        "name": "Invent Here, Ship Elsewhere Risk",
        "components": (
            "Google repeatedly hires or acquires frontier AI talent (Hinton auction, DeepMind, Transformer authors) "
            "but organizational separation and publication restrictions push breakthroughs external. DeepMind in London "
            "with independent board vs. Brain in Mountain View created duplicate efforts. Closed research post-DeepMind "
            "triggered OpenAI's open-science pitch. Transformer architecture originated at Google Brain but GPT "
            "productized it first. Jeff Dean's PHIL infrastructure enabled AdSense-scale ML deployment internally "
            "while consumer AI products lagged."
        ),
        "application": (
            "When evaluating tech incumbents in platform shifts, distinguish research leadership from product "
            "velocity and talent retention. Google's $550M DeepMind bet may be worth $500B but created OpenAI as "
            "unintended consequence. Merging research orgs (Gemini unification) addresses structural delay — "
            "pattern repeats across Bell Labs, Xerox PARC, and Microsoft Research."
        ),
    },
    competitive_advantage=(
        "Google's AI advantage is stacked talent, data, compute, and distribution — if organizationally unified. "
        "Search queries, YouTube videos (10M training frames), Gmail/Maps logged-in users, and TPU infrastructure "
        "provide training data and deployment surfaces competitors lack at scale.\n\n"
        "DeepMind's AlphaGo (2016), AlphaFold, and data-center cooling optimizations prove research converts to "
        "value when deployed. AdSense and search ranking already run on neural nets — Google monetized AI internally "
        "before ChatGPT without consumer-facing credit.\n\n"
        "Gemini unification merges Brain and DeepMind under Pichai, ending decade of duplication. Full-stack control: "
        "TPUs, Cloud, Android, Search, and Workspace provide distribution no startup matches.\n\n"
        "Weaknesses: Transformer author exodus; OpenAI/Anthropic brand leadership in consumer AI; organizational "
        "inertia 2013–2023; DeepMind-London independence delayed integration; and Musk-Altman rift traced to DeepMind "
        "acquisition. 'Invent here, ship elsewhere' nearly cost the platform shift.\n\n"
        "TPU custom silicon and Google Cloud provide deployment surfaces OpenAI lacks without Microsoft partnership. "
        "AlphaFold, data-center cooling, and search ranking integration prove Brain/DeepMind research monetizes internally "
        "even when consumer products lag. Gemini's 2023 unification under Pichai addresses the decade-long organizational "
        "split that Ben and David identify as Google's self-inflicted AI delay."
    ),
    key_insights=[
        {
            "view": "DeepMind's acquisition created OpenAI.",
            "question": "Why did Musk and Altman start OpenAI?",
            "answer": "After Google bought DeepMind for $550M (2014) and closed research, Musk and Altman pitched researchers: join a nonprofit with open publication. ~7 Google researchers left initially; Ilya Sutskever became OpenAI chief scientist. Elon had invested in DeepMind seed round via Founders Fund — Google's acquisition frustrated open-AI advocates.",
        },
        {
            "view": "Google wrote the Transformer but OpenAI shipped GPT.",
            "question": "How did Google lose the LLM race?",
            "answer": "'Attention Is All You Need' (2017) came from eight Google Brain researchers — all eventually departed. Google prioritized search quality integration over consumer chat product. OpenAI productized the architecture while Google debated safety and organizational boundaries between DeepMind and Brain.",
        },
        {
            "view": "The Hinton auction foreshadowed everything.",
            "question": "Why did Google win the 2013 AI auction?",
            "answer": "Hinton ran structured hourly bidding among Google, Baidu, Microsoft, and DeepMind (dropped out). Google paid ~$40M+ for DNN Research — three researchers including Ilya. A few percent improvement on tens of billions in ad revenue justifies almost any price. Same pattern as PageRank: small algorithmic edge, massive economic leverage.",
        },
        {
            "view": "2003–2013 was Google's product golden decade.",
            "question": "What happened after 2013?",
            "answer": "Gmail, Maps, Android, Chrome, YouTube, AdSense — all launched in one decade. Then ~10 years without major new consumer products until Gemini. AI research continued (AlphaGo 2016, Transformer 2017) but product launches stalled. Ben and David frame this as organizational sclerosis between Brain and DeepMind.",
        },
        {
            "view": "Gemini is merger, not startup.",
            "question": "Can Google catch OpenAI?",
            "answer": "Gemini unifies DeepMind and Brain — ending duplicate teams and conflicting mandates. Google has TPU compute, Search/YouTube data, Android distribution, and ~$100B+ quarterly revenue funding capex. Question is execution velocity and talent retention, not capability. DeepMind estimated ~$500B value validates the assets exist.",
        },
    ],
    top_investment_implications=[
        {
            "ticker": "GOOGL",
            "direction": "Long",
            "confidence": "Medium",
            "thesis": "Google owns Transformer-era IP, DeepMind, TPUs, and distribution — Gemini unification addresses decade of organizational delay; AI monetization on ~$100B+ quarterly revenue base is underpriced if product velocity matches research leadership.",
        },
        {
            "ticker": "MSFT",
            "direction": "Watch",
            "confidence": "Medium",
            "thesis": "OpenAI partnership gives Microsoft consumer AI brand leadership Google lacked — but Google retains fuller stack (TPU, data, Search); competitive outcome depends on Gemini execution vs. ChatGPT/Copilot distribution.",
        },
    ],
    golden_quotes=[
        "\"If we rewind 10 years before the Transformer paper, all of the following people were Google employees\" — David opening the talent exodus frame.",
        "\"The YouTube of AI\" — David's framing of DeepMind relative to Google's $550M acquisition versus ~$500B estimated value today.",
        "\"2003–2013 they launched everything you know of at Google except search; then 2013–2023 they basically didn't launch any new products until Gemini\" — Ben on the product drought between golden decades.",
    ],
    chronology={
        "subject": "Google · DeepMind · AI",
        "events": [
            {"date": "2012", "event": "Brain cat paper — deep learning on 10M YouTube frames across 2,000 computers"},
            {"date": "2012", "event": "AlexNet wins ImageNet by 40%; Hinton/Sutskever/Krizhevsky prove GPU scaling"},
            {"date": "2013", "event": "Google wins Hinton DNN Research auction for ~$40M+ against Baidu and Microsoft"},
            {"date": "2014", "event": "Google acquires DeepMind for $550M; independent oversight board established"},
            {"date": "2015", "event": "OpenAI founded after DeepMind acquisition closes research; Musk, Altman, Thiel pledge ~$1B"},
            {"date": "2016", "event": "AlphaGo defeats Lee Sedol — DeepMind's public breakthrough"},
            {"date": "Jun 2017", "event": "Transformer paper published — eight Google Brain authors"},
            {"date": "2022", "event": "ChatGPT launches — OpenAI productizes Transformer architecture externally"},
            {"date": "2023", "event": "Google merges Brain and DeepMind; Gemini announced"},
            {"date": "2024–25", "event": "Gemini integrated across Search, Workspace, and Android; AI capex accelerates"},
        ],
    },
)

EPISODES["acq-alphabet-inc"] = base(
    "acq-alphabet-inc",
    episode_rating={"overall": 5},
    keywords=["Other Bets", "YouTube", "Web Applications"],
    conclusion=(
        "Google Part II covers the innovation factory era: Gmail, Maps, Docs, Android, Chrome, and the $1.65B "
        "YouTube acquisition that Ben and David regrade from 'terrible' to 'screaming deal.' The 2015 Alphabet "
        "reorganization separated Google's cash engine from Other Bets — Waymo, Verily, X — while preserving Larry "
        "and Sergey's long-term bets. YouTube consumed more bandwidth than the entire 2000 internet by 2007 and "
        "20% of internet bits by 2014; the 50% creator rev-share delayed profitability a decade but built an "
        "ecosystem no competitor matched. Workspace has billions of users but Microsoft's Office segment (~$120B) "
        "still dwarfs Google's Cloud segment (~$50B). The episode ends at AI's dawn — Google's moat is logged-in "
        "web applications feeding search and ads, with YouTube as the ultimate logged-in engagement flywheel."
    ),
    background=(
        "Picking up after Google's AdWords breakthrough, Ben and David trace the 2000s strategy of owning rich web "
        "applications as defense against Microsoft and moat for search. Gmail (2004, 1GB free storage vs. 2–4MB "
        "competitors), Maps (2004, now 2B+ users and ~$5–10B estimated revenue), Docs/Sheets, Chrome, and Android "
        "follow. YouTube (acquired 2006 for $1.65B) succeeded where Google Video failed because a startup could "
        "ignore copyright until Google-scale infrastructure and ad monetization made it viable.\n\n"
        "Alphabet (2015) formalized separation between Google (Search, Ads, YouTube, Cloud) and Other Bets. "
        "YouTube profitability came ~2009–2011 after years of losses; creator 50% rev-share built supply side. "
        "Microsoft Office retains revenue dominance (~$120B productivity segment) despite Google's user scale."
    ),
    important_facts=[
        "Google acquired YouTube for $1.65B (Nov 2006), less than 18 months after launch; Ben and David regrade from prior 'terrible acquisition' to 'screaming deal' — YouTube estimated 20% of internet bits (2014) and now generates tens of billions annually.",
        "Gmail launched April 2004 with 1GB free storage vs. 2–4MB competitors; beta invites traded on eBay for ~$150. Gmail grew to 2B+ users — still best backend even for third-party clients like Superhuman.",
        "Microsoft productivity segment (~$120B revenue, mostly Office) vs. Google Cloud segment (~$50B including Workspace and IaaS) — Google has more users (500M–1B per app) but Microsoft captures more revenue and margin.",
        "YouTube's 50% creator revenue share delayed profitability ~decade versus Facebook/Instagram (~0% rev share) but built creator economy no competitor matched. Watch-time metric replaced raw views; algorithmic feed beat subscription model for engagement.",
        "Alphabet reorganization (2015) separated Google (Search, Ads, YouTube, Cloud, Android) from Other Bets (Waymo, Verily, Calico, X). Google's market cap ~20x'd since YouTube deal — stock payment made acquisition even cheaper in retrospect.",
    ],
    mental_model={
        "name": "Logged-In Web Application Moat",
        "components": (
            "Google's 2000s strategy: build rich web apps (Gmail, Maps, Docs, YouTube) that require login, creating "
            "identity layer search alone doesn't need. Logged-in users enable personalization, cross-product integration, "
            "and ad targeting. YouTube differs from Search — engagement requires login for recommendations; "
            "50% creator rev-share bought supply-side loyalty. Android and Chrome ensure Google services remain default "
            "on mobile and web. Other Bets provide optionality without contaminating core P&L."
        ),
        "application": (
            "Platform companies should evaluate acquisitions by ecosystem value, not standalone P&L. YouTube lost "
            "money for years but secured video search and mobile engagement. When comparing Google vs. Microsoft "
            "productivity, user scale ≠ revenue capture — enterprise willingness-to-pay still favors incumbents. "
            "Alphabet structure preserves long-term R&D optionality."
        ),
    },
    competitive_advantage=(
        "Google's post-search moat layers web applications on advertising infrastructure. Gmail's 1GB launch "
        "redefined email storage economics and created logged-in identity. Maps (2B+ users, ~$5–10B revenue) "
        "combines consumer app with API platform enabling third-party web apps.\n\n"
        "YouTube's acquisition corrected Google Video's failure — startup tolerance for copyright ambiguity plus "
        "Google's infrastructure and ads created unbeatable video platform. 50% creator rev-share was expensive but "
        "built supply-side lock-in. Mobile shift made logged-in YouTube engagement more valuable than anonymous search.\n\n"
        "Android and Chrome secure distribution defaults. Workspace provides enterprise foothold despite Microsoft's "
        "revenue lead. Alphabet structure isolates Waymo/Verily bets from Search cash flow.\n\n"
        "Weaknesses: YouTube algorithm incentive misalignment; creator rev-share margin drag; Workspace revenue "
        "gap vs. Microsoft (~$120B vs. ~$50B cloud segment); Other Bets burn rate; and social/product launch "
        "failures (Google+, Buzz). User scale without monetization parity remains gap.\n\n"
        "Chrome and Android secure default distribution for Google services on mobile — the post-PC moat Microsoft "
        "fought via IE bundling but lost on phones. Waymo and Other Bets under Alphabet provide autonomous-driving "
        "and life-sciences optionality without contaminating Search margins; the 2015 restructure formalized what "
        "Larry and Sergey practiced informally for a decade."
    ),
    key_insights=[
        {
            "view": "YouTube was the acquisition Google had to make.",
            "question": "Why couldn't Google Video win?",
            "answer": "As public company, Google couldn't tolerate YouTube's copyright ambiguity — startups could. YouTube scaled embeds and UGC while Google Video required human review. By Nov 2006, YouTube consumed bandwidth equal to entire 2000 internet; Google paid $1.65B for lightning in a bottle rather than rebuild.",
        },
        {
            "view": "50% rev-share was expensive and correct.",
            "question": "Why give creators half?",
            "answer": "YouTube paid ~50% to creators vs. Facebook's ~0% — delaying profitability ~decade. But creator economy lock-in became unreplicable. AdSense heritage made Google comfortable sharing revenue with content producers. Watch-time metric and algorithmic feed beat subscription curation for engagement.",
        },
        {
            "view": "Google has users; Microsoft has revenue.",
            "question": "Why does Office still win financially?",
            "answer": "Docs/Sheets/Slides each have 500M–1B users vs. Office's ~200M+. But Microsoft productivity segment generates ~$120B vs. Google's entire Cloud segment under ~$50B. Enterprise EA switching costs and willingness-to-pay exceed consumer free-product scale.",
        },
        {
            "view": "Gmail was the original logged-in moat.",
            "question": "Why did 1GB storage matter?",
            "answer": "April 2004: Gmail offered 1GB vs. 2–4MB competitors — 250–500x advantage. Beta invites traded at ~$150 on eBay. Logged-in email created identity layer for Maps, Docs, and later YouTube personalization. Search never required login; Gmail made logged-inness valuable.",
        },
        {
            "view": "Alphabet preserves optionality.",
            "question": "Why restructure in 2015?",
            "answer": "Separate Google's cash-generating Search/Ads/YouTube from Other Bets (Waymo, Verily, X) for transparency and long-term betting. Larry and Sergey maintained control while Sundar ran Google. Structure lets moonshots burn capital without contaminating core margins — Berkshire-like separation.",
        },
    ],
    top_investment_implications=[
        {
            "ticker": "GOOGL",
            "direction": "Long",
            "confidence": "High",
            "thesis": "YouTube regraded as screaming deal plus Search/Ads cash engine funds AI capex — Alphabet structure preserves Waymo/Cloud optionality while core generates ~$100B+ quarterly revenue.",
        },
        {
            "ticker": "MSFT",
            "direction": "Watch",
            "confidence": "Medium",
            "thesis": "Microsoft's ~$120B productivity segment vs. Google's ~$50B cloud segment shows enterprise monetization gap — Workspace growth constrained despite user parity; Azure hybrid story competes with Google Cloud.",
        },
    ],
    golden_quotes=[
        "\"The most embarrassing thing in Acquired history was our early episode on YouTube\" — David before regrading the acquisition.",
        "\"YouTube consumed as much bandwidth as the entire internet did in the year 2000\" — 2007 report cited during acquisition analysis.",
        "\"Google has all the users and Microsoft has all the money\" — on Workspace vs. Office revenue disparity despite user scale.",
    ],
    chronology={
        "subject": "Google · Alphabet · YouTube",
        "events": [
            {"date": "Apr 2004", "event": "Gmail launches with 1GB storage — viral beta invite system"},
            {"date": "2004–05", "event": "Google Maps and Docs development; API platform strategy begins"},
            {"date": "Feb 2005", "event": "YouTube founded by PayPal Mafia alumni (Hurley, Karim, Chen)"},
            {"date": "Nov 2006", "event": "Google acquires YouTube for $1.65B in stock"},
            {"date": "2008", "event": "Chrome browser launches; Android announced"},
            {"date": "2009–11", "event": "YouTube ad revenue triples; platform reaches profitability"},
            {"date": "2012", "event": "YouTube estimated ~$4B revenue; approaching break-even to profitable"},
            {"date": "Oct 2015", "event": "Alphabet holding company structure announced; Sundar Pichai CEO of Google"},
            {"date": "2015–25", "event": "YouTube Shorts, creator economy scale; Maps reaches 2B+ users"},
            {"date": "2025", "event": "Episode ends at AI era dawn; Google Cloud ~$50B segment revenue"},
        ],
    },
)

EPISODES["acq-the-jamie-dimon-interview"] = base(
    "acq-the-jamie-dimon-interview",
    episode_rating={"overall": 4},
    keywords=["Fortress Balance Sheet", "Risk Culture", "JPMorgan Chase"],
    conclusion=(
        "Jamie Dimon tells Acquired's Chase Center audience how he built JPMorgan Chase into a ~$800B fortress "
        "after being fired from Citigroup in 1998 — the heir-apparent discarded, restarting at troubled $30B "
        "market-cap Bank One in Chicago. He invested $60M of personal capital (half his net worth), fixed risk "
        "culture and a 21-person board, then merged into JPMorgan (2004) where Bank One shareholders received 42%. "
        "The fortress balance sheet — conservative accounting, excess capital, planning for four-sigma disasters — "
        "enabled Bear Stearns and Washington Mutual rescues in 2008 and First Republic in 2023. Dimon cites risk "
        "discipline, internal incentive realignment, and diversified businesses feeding each other as separation "
        "drivers; a 15-point efficiency ratio advantage compounds reinvestment. At 68 minutes, the interview compresses "
        "twenty years into live conversation rather than archival deep dive."
    ),
    background=(
        "Recorded live at Chase Center with ~6,000 attendees during Summer 2025, Ben and David walk Dimon from his "
        "1998 Citigroup firing through Bank One turnaround, the 2004 JPMorgan merger, 2006 risk pullback before the "
        "crisis, Bear Stearns and WaMu acquisitions, and 2023 First Republic rescue.\n\n"
        "Dimon emphasizes risk culture above all: plan for worst-case scenarios, maintain fortress balance sheet with "
        "excess capital, and align internal incentives so division heads don't bet the firm. He raised $11B equity "
        "during the 2008 crisis when markets trusted JPMorgan alone. Efficiency ratio advantage (~15 cents more profit "
        "per dollar vs. competitors) compounds over decades."
    ),
    important_facts=[
        "Dimon fired from Citigroup (1998) after 13 years building the Sandy Weill conglomerate model; became CEO of Bank One ($30B market cap vs. Citi's ~$200B), investing $60M personal capital — roughly half his net worth — upon taking the job.",
        "Bank One–JPMorgan merger (2004): Bank One shareholders received 42% of combined company — 'merger of equals' that effectively imported Dimon's culture into JPMorgan. He became chairman and CEO of combined firm by 2006.",
        "2006: Dimon pulled JPMorgan back on risk while Wall Street accelerated — same incentives, different behavior. Bear Stearns rescue (2008) cost ~$15–20B all-in; WaMu acquisition proved profitable. Raised $11B equity at crisis bottom when only JPMorgan could.",
        "Fortress balance sheet strategy: conservative accounting, excess capital reserves, planning for four-sigma events as inevitable not theoretical. Dimon asks if private credit (~$1T+) resembles pre-2008 shadow banking risks.",
        "JPMorgan market cap ~$800B when recorded; efficiency ratio ~15 points better than competitors — 'for every dollar you make, you keep 15 cents more as profit' — enabling reinvestment compounding. First Republic acquired 2023 applying 2008 lessons.",
    ],
    mental_model={
        "name": "Fortress Balance Sheet Discipline",
        "components": (
            "Dimon's core principle: the worst case will happen, so build capital and culture to survive it. "
            "Conservative accounting, excess reserves, and saying no to near-the-line risk bets — even when "
            "competitors earn higher short-term returns. Internal incentives aligned so business heads don't "
            "implicitly bet the firm. Diversified businesses (consumer, investment bank, payments, asset management) "
            "feed each other. Reputation from 2008 enables opportunistic acquisitions (WaMu, First Republic)."
        ),
        "application": (
            "For financial institutions, short-term ROE sacrifices buy survival optionality worth more in crises. "
            "Dimon's Bank One playbook — fix board governance, risk culture, then merge from strength — applies to "
            "any turnaround where culture precedes strategy. Efficiency ratio advantages compound when reinvested "
            "across cycles."
        ),
    },
    competitive_advantage=(
        "JPMorgan's moat combines scale, diversification, and reputation earned in 2008. Fortress balance sheet "
        "enabled acquisitions when peers failed — WaMu deposits, Bear Stearns assets, First Republic — at prices "
        "only JPMorgan could finance. ~$800B market cap reflects crisis-era trust premium.\n\n"
        "Dimon's risk culture imported from Bank One: 21-person board trimmed, auto-loan and trading limits enforced, "
        "compensation structures penalizing blow-ups. Same Wall Street incentives (2006) produced different behavior.\n\n"
        "Diversified revenue streams — consumer, corporate banking, trading, payments (~$18B annual revenue per "
        "Acquired's Reinvent interview), asset management — reduce single-business dependency. Efficiency ratio "
        "advantage (~15 points) funds technology and talent reinvestment.\n\n"
        "Weaknesses: regulatory scrutiny of too-big-to-fail scale; political visibility (Dimon floated for policy "
        "roles); private credit shadow banking concerns; and key-man dependency after 20 years. Competitors copied "
        "fortress rhetoric but not always practice.\n\n"
        "Payments franchise (~$18B annual revenue per Acquired's Reinvent interview with Max Neukirchen) illustrates "
        "technology businesses embedded inside banking — a diversification dimension peers lack. Chase Center live "
        "interview with ~6,000 attendees underscored reputational capital no competitor could replicate during the "
        "2008 or 2023 regional banking crises."
    ),
    key_insights=[
        {
            "view": "Getting fired was the inflection point.",
            "question": "Why did Dimon join Bank One?",
            "answer": "Fired from Citigroup (1998) despite being heir-apparent to Sandy Weill's conglomerate. Passed on glamorous NYC options for troubled Chicago Bank One ($30B vs. Citi $200B). Invested $60M personal — half net worth — aligning incentives. Fixed 21-person board and risk culture before JPMorgan merger imported the playbook.",
        },
        {
            "view": "Same incentives, different culture in 2006.",
            "question": "Why didn't JPMorgan blow up?",
            "answer": "Dimon pulled risk back in 2006 while peers accelerated — same bonus structures, different internal limits. Auto-loan comp changes and trading desk culture imported from Bank One. He had same information and incentives as other CEOs but behaved differently because culture enforced don't-blow-up discipline.",
        },
        {
            "view": "Fortress balance sheet buys crisis optionality.",
            "question": "Why could only JPMorgan rescue Bear and WaMu?",
            "answer": "Excess capital and conservative accounting meant JPMorgan could raise $11B equity at crisis bottom. Bear cost ~$15–20B all-in but bought reputation worth more. WaMu proved profitable. 2023 First Republic applied same playbook. Competitors couldn't move because they lacked capital and trust.",
        },
        {
            "view": "Efficiency ratio compounds silently.",
            "question": "Why is JPMorgan worth ~$800B?",
            "answer": "For every revenue dollar, JPMorgan keeps ~15 cents more profit than competitors — not from one secret but operational discipline across divisions. That gap reinvested in technology, talent, and acquisitions compounds over decades. Dimon declined to reveal all secrets on stage.",
        },
        {
            "view": "Private credit may be the next risk.",
            "question": "What worries Dimon today?",
            "answer": "Dimon flagged private credit (~$1T+) as potentially problematic — shadow banking echoes pre-2008. Also regulatory/political cycles every four years create uncertainty. But fortress balance sheet philosophy unchanged: plan for worst case, maintain excess capital, survive to acquire when others fail.",
        },
    ],
    top_investment_implications=[
        {
            "ticker": "JPM",
            "direction": "Long",
            "confidence": "Medium",
            "thesis": "Fortress balance sheet and crisis-acquired scale produce ~15-point efficiency ratio advantage compounding reinvestment — ~$800B market cap reflects durable trust premium, though key-man and regulatory risks persist.",
        },
    ],
    golden_quotes=[
        "\"How did he do it? Banks fail. Financial firms often have spectacular blowups\" — Ben opening the Chase Center interview frame.",
        "\"I invested half my net worth in this company\" — Dimon on putting $60M into Bank One stock upon becoming CEO.",
        "\"For every dollar that you make compared to your competitors, you get to keep 15 cents more of that dollar as profit\" — Ben on JPMorgan's efficiency ratio advantage.",
    ],
    chronology={
        "subject": "Jamie Dimon · JPMorgan Chase",
        "events": [
            {"date": "1985–98", "event": "Dimon builds Citigroup conglomerate model with Sandy Weill"},
            {"date": "1998", "event": "Fired from Citigroup; passes on Amazon CEO exploration"},
            {"date": "2000", "event": "Becomes Bank One CEO; invests $60M personal capital"},
            {"date": "2004", "event": "Bank One merges with JPMorgan; Bank One shareholders get 42%"},
            {"date": "2006", "event": "Dimon chairman/CEO; pulls firm back on risk pre-crisis"},
            {"date": "Mar 2008", "event": "Acquires Bear Stearns in weekend rescue (~$15–20B all-in cost)"},
            {"date": "Sep 2008", "event": "Acquires Washington Mutual; raises $11B equity at crisis bottom"},
            {"date": "2023", "event": "Acquires First Republic after regional banking crisis"},
            {"date": "2010s", "event": "JPMorgan passes Bank of America and Citigroup in market cap through cycle reinvestment"},
            {"date": "2025", "event": "Live Acquired interview at Chase Center; JPMorgan ~$800B market cap"},
        ],
    },
)

EPISODES["acq-google"] = base(
    "acq-google",
    episode_rating={"overall": 5},
    keywords=["PageRank", "AdWords", "Search Infrastructure"],
    conclusion=(
        "Google Part I traces search from Larry Page's 1996 BackRub thesis through PageRank, the $1M Yahoo rejection, "
        "Andy Bechtolsheim's $100K uncapped check, and AdWords — the business model that 5x'd revenue in one year "
        "(2001: $86M → 2002: $440M). Ben and David show Google won on three axes: relevance (PageRank), scale "
        "(distributed crawling on cheap hardware), and monetization (AdWords auction with Ad Rank quality score). "
        "Yahoo passed on buying PageRank for $1M; later floated $3B acquisition while Google asked $5B — no deal. "
        "The AOL 2002 bake-off committed $100M minimum when Google barely had the cash, validating that superior "
        "monetization beats distribution alone. Page and Brin's genius was adopting the best external ideas — Overture's "
        "CPC model, not inventing everything — while building infrastructure competitors couldn't match."
    ),
    background=(
        "Ben and David open Google Part I at the 2025 garage where the company started, tracing Larry Page and Sergey "
        "Brin's 1995 Stanford meeting through BackRub (PageRank named for Larry, not web pages), the failed sale to "
        "Yahoo/Infoseek/Lycos for ~$1M, and September 1998 founding with Bechtolsheim's legendary sun.com check.\n\n"
        "Infrastructure innovations — cheap commodity hardware, parallel crawling, Linux clusters — enabled index scale "
        "rivals couldn't match (AltaVista's 16M pages). Portal deals (Netscape 3M searchers/day, Yahoo $10M investment "
        "plus $7.2M/year) bridged the dot-com crash until AdWords (2002) transformed economics via self-serve CPC "
        "auctions with quality-adjusted Ad Rank."
    ),
    important_facts=[
        "Page and Brin offered PageRank to Yahoo for ~$1M and were rejected; Infoseek and Lycos also passed. Andy Bechtolsheim wrote $100K uncapped check before incorporation; Ram Shriram added $250K; Jeff Bezos matched at $252K — stake potentially worth ~$20B if Bezos never sold.",
        "Sequoia/Kleiner Series A at ~$100M valuation (1999) with $25M in bank; competing term sheet at $150M declined. Yahoo portal deal (June 2000): $10M investment plus $7.2M/year — traffic doubled to 14M searchers/day, bridging dot-com crash.",
        "AdWords transition (2002): revenue grew from $86M (2001) to $440M (2002) — 5x in one year. Overture invented CPC self-serve; Google added Ad Rank (quality score × bid). Overture patent dispute settled for $360M; Yahoo later bought Overture for $1.6B.",
        "AOL bake-off (2002): 34M users; Google committed $100M minimum guarantee without having the cash — AOL made $35M first half 2002, $200M in 2003. Google offered 85%+ rev share because superior monetization made it profitable.",
        "Index scale: pre-Google engines indexed ~1M pages; AltaVista reached 16M. Google's parallel crawling on cheap Linux hardware enabled comprehensiveness rivals couldn't match — index size as important as algorithm quality.",
    ],
    mental_model={
        "name": "Adopt Best Idea Plus Infrastructure Scale",
        "components": (
            "Page and Brin combined PageRank relevance with Overture's CPC auction model (Ad Rank quality score) "
            "and commodity-hardware infrastructure scale. They didn't invent paid search but executed it better via "
            "superior monetization per query — enabling 85%+ rev-share to distributors while remaining profitable. "
            "Portal deals (Netscape, Yahoo, AOL) bought distribution until google.com brand stood alone. "
            "Distributed systems on cheap hardware made index comprehensiveness a moat."
        ),
        "application": (
            "Platform winners often combine external business model innovation with proprietary infrastructure advantage. "
            "Google's $1M Yahoo rejection is cautionary for acquirers; $5B reverse-takeover ask shows power shift within "
            "two years of AdWords. When monetization per user exceeds competitors, distribution partnerships become "
            "profitable even at 100%+ rev-share."
        ),
    },
    competitive_advantage=(
        "Google's search moat stacks algorithm, infrastructure, and monetization. PageRank used links as citations — "
        "relevance competitors couldn't match with keyword counting. Parallel crawling on cheap Linux clusters enabled "
        "index scale (16M+ pages vs. ~1M for predecessors) that made relevance meaningful.\n\n"
        "AdWords Ad Rank (quality score × bid) improved user experience while maximizing revenue — self-serve "
        "democratized advertiser access. Superior monetization per query let Google outbid rivals for distribution "
        "(AOL $100M guarantee, 85%+ rev-share) while remaining profitable.\n\n"
        "Portal dependency ended as google.com brand grew via 'Powered by Google' badges. Yahoo's $3B offer and "
        "Google's $5B counter (2002) showed power inversion — Yahoo buying Overture for $1.6B couldn't catch up.\n\n"
        "Weaknesses: portal revenue dependency pre-2002; Overture patent settlement ($360M); initial reluctance to "
        "build consumer brand; and nearly selling core technology for $1M. Luck and timing (Yahoo deal during dot-com "
        "crash) bridged gap before AdWords.\n\n"
        "Eric Schmidt's CEO era (2001–2011) professionalized operations while preserving Page/Brin product control — "
        "the adult supervision model later copied across Silicon Valley. Jeff Dean-era distributed systems (MapReduce, "
        "GFS) made index freshness and scale economical; without infrastructure moat, PageRank alone would not have "
        "won as AltaVista and others copied link analysis concepts."
    ),
    key_insights=[
        {
            "view": "Yahoo's $1M rejection is history's costliest pass.",
            "question": "Why didn't Google sell PageRank?",
            "answer": "Page and Brin shopped BackRub to Yahoo (~$1M), Infoseek, and Lycos — all passed. They viewed it as licensing technology, not building a search engine. Within years AdWords generated $440M annually. Yahoo later offered $3B; Google floated $5B — effectively a reverse takeover that killed the deal.",
        },
        {
            "view": "AdWords was adoption, not invention.",
            "question": "Did Google invent paid search?",
            "answer": "Bill Gross's Overture invented CPC self-serve auctions at GoTo.com. Overture board rejected Google partnership — wouldn't give 10% of $2B company to zero-revenue startup. Google adopted model, added Ad Rank quality score, 5x'd revenue in 2002. Settled patent dispute for $360M later.",
        },
        {
            "view": "Infrastructure was the hidden moat.",
            "question": "Why did index size matter?",
            "answer": "Best algorithm fails if index covers 1M pages while web has millions. AltaVista reached 16M pages using DEC infrastructure. Google parallelized crawling on cheap Linux clusters — Jeff Dean-era distributed systems made comprehensiveness economical. Speed plus scale plus relevance beat competitors on all three axes.",
        },
        {
            "view": "Better monetization buys distribution.",
            "question": "Why guarantee AOL $100M without cash?",
            "answer": "Google monetized each search better than Inktomi/Overture split. If you earn more per query, 85% rev-share still beats competitors' 70%. AOL made $35M first half 2002, $200M in 2003. Superior unit economics let Google buy distribution unprofitably for rivals.",
        },
        {
            "view": "Powered by Google trained a generation.",
            "question": "Why keep google.com open during portal deals?",
            "answer": "Netscape deal brought 3M searchers/day via 'Powered by Google' badge. Shutting google.com would anger existing users but every portal visitor saw Google brand. Yahoo deal doubled traffic to 14M/day. Brand building through OEM distribution before direct traffic dominated.",
        },
    ],
    top_investment_implications=[
        {
            "ticker": "GOOGL",
            "direction": "Long",
            "confidence": "High",
            "thesis": "Search AdWords economics — born from 2002's $86M-to-$440M transition — still fund Alphabet's AI and Other Bets; PageRank plus infrastructure moat remains durable despite distribution shift to mobile and AI interfaces.",
        },
    ],
    golden_quotes=[
        "\"They tried to sell PageRank to Yahoo for $1 million and were rejected\" — on the first of many Yahoo-Google near-misses.",
        "\"Jeff Bezos is in for $252,000\" — matching Ram Shriram's $250K after asking what Ram was in for; stake potentially ~$20B.",
        "\"Revenue grew from $86 million to $440 million in one year\" — David on the 2002 AdWords transition that created Google's business model.",
    ],
    chronology={
        "subject": "Google · PageRank · AdWords",
        "events": [
            {"date": "1995", "event": "Larry Page and Sergey Brin meet at Stanford; BackRub research begins"},
            {"date": "1996–97", "event": "PageRank algorithm developed; links as web citations modeled"},
            {"date": "1997–98", "event": "PageRank shopped to Yahoo (~$1M), Infoseek, Lycos — all reject"},
            {"date": "Sep 1998", "event": "Google incorporated; Bechtolsheim $100K check; Bezos invests $252K"},
            {"date": "1999", "event": "Sequoia/Kleiner invest at ~$100M valuation; $25M raised"},
            {"date": "Jun 2000", "event": "Yahoo deal: $10M investment plus $7.2M/year; 14M searchers/day"},
            {"date": "Mar 2001", "event": "Eric Schmidt hired CEO; dot-com crash survival mode"},
            {"date": "2002", "event": "AdWords launches; revenue $86M → $440M; AOL bake-off won"},
            {"date": "2002", "event": "Yahoo offers ~$3B; Google counters ~$5B — no acquisition"},
            {"date": "2004", "event": "IPO via Dutch auction; Google becomes public company"},
            {"date": "2025", "event": "Acquired records Part I in original Menlo Park garage"},
        ],
    },
)
