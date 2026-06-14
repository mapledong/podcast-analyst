"""Episode bodies for acq batch s7_8 target — imported by _write_acq_batch_s7_8_target.py."""

from __future__ import annotations

from scripts._write_acq_batch_491_500_common import base

NOTES = "Manual GPT Acquired batch v5.1 — Season 7/8 target batch"

EPISODES: dict[str, dict] = {}

EPISODES["acq-bitcoin"] = base(
    "acq-bitcoin",
    review_notes=NOTES,
    episode_rating={"overall": 5},
    keywords=["Proof of Work", "Digital Scarcity", "Monetary History"],
    conclusion=(
        "Ben and David trace Bitcoin from Renaissance banking and ACH batch delays to Satoshi's "
        "October 2008 whitepaper solving double-spend without trusted third parties. Mining rewards "
        "started at 50 BTC per ~10-minute block, halving toward a 21-million cap; price moved from "
        "sub-1¢ to over $30,000 by recording — a cited 3,000,000X decade return exceeding Naspers-Tencent "
        "or SoftBank-Yahoo-Alibaba 1000X outcomes. Silk Road, Mt. Gox (750,000+ client BTC lost), Winklevoss "
        "Facebook-stock pivot, and 2017–2020 institutional adoption (MicroStrategy's $250M treasury bet) "
        "frame the asset as ingenious protocol design wrapped in volatile speculation. The Satoshi paper's "
        "core problem is internet payments, not ideology — yet network-effect security and finite supply "
        "finite supply created a new monetary layer neither company nor government controls — hosts stress not "
        "Hosts stress to listeners this is not investment advice but protocol ingenuity stands apart from "
        "bubble cycles, pizza lore, and January 2021 Season 8 Episode 1 recording context."
    ),
    background=(
        "Season 8 Episode 1 opens with David paying 2021 taxes via 1995-era IRS UX — routing and account "
        "numbers that enable fraud — then rewinds through double-entry bookkeeping, paper banknotes, ACH's "
        "3–5-day batching, and credit cards' 2.9% plus 30¢ merchant tax. PayPal and Stripe improved rails "
        "but remained dollar-denominated trust layers atop centuries of banking hacks.\n\n"
        "The episode unpacks public-key cryptography, Nakamoto's October 2008 nine-page whitepaper, "
        "proof-of-work difficulty, and why miners earn BTC for securing the chain. History covers the "
        "10,000-BTC pizza (~$41), Satoshi's ~1M mined coins, Silk Road's 1.2M+ transactions, exchange "
        "blowups, Winklevoss twins turning $45M of 2008 Facebook stock into ~$300M by 2012, and COVID-era "
        "stimulus plus zero rates pushing capital into BTC. Domino's and pizza references thread through "
        "as comic relief while hosts stress: not investment advice, but the protocol's cleverness stands "
        "apart from bubble cycles."
    ),
    important_facts=[
        "Bitcoin rose from under 1¢ to over $30,000 in just over a decade — hosts cite a 3,000,000X return, exceeding Naspers-Tencent and SoftBank-Yahoo-Alibaba venture outcomes that turned ~$20–30M into ~$100–200B (roughly 1000X).",
        "Mining rewards began at 50 BTC per ~10-minute block, halving over time toward a hard cap of slightly under 21 million coins; reward was ~6.25 BTC per block by 2021 recording.",
        "Satoshi Nakamoto is believed to have mined roughly 1–1.5 million BTC early — potentially ~$50 billion at 2021 prices — then disappeared circa 2010–2011 after handing repos to early developers.",
        "Mt. Gox collapse permanently lost an estimated 750,000+ client bitcoins (~7% of circulation then) — roughly $22.5 billion at 2021 prices if private keys are gone forever.",
        "MicroStrategy disclosed $250 million in Bitcoin classified as treasury reserve assets in August 2020; Cameron and Tyler Winklevoss turned $45M of 2008 Facebook stock into ~$300M by 2012 before going all-in on crypto per episode narrative.",
    ],
    mental_model={
        "name": "Trustless Scarcity on a Public Ledger",
        "components": (
            "Traditional money requires banks and card networks as trusted third parties with reversible "
            "transactions and fraud overhead — credit cards charge merchants ~2.9% plus 30¢. Bitcoin uses "
            "public-key ownership, a global replicated ledger, and proof-of-work to make double-spend "
            "exponentially costly as hash power compounds. Miners earn halving block rewards for ordering "
            "valid transactions. Value accrues to holders as security spend grows — a network-effect commodity, "
            "not corporate cash flows. Silk Road processed 1.2M+ transactions; Mt. Gox lost 750K+ client coins. "
            "Hosts trace history from Renaissance banking through ACH batch delays to Satoshi's nine-page 2008 "
            "paper — commerce on the internet problem, not ideology-first manifesto."
        ),
        "application": (
            "Evaluate crypto by security budget, adoption rails (Coinbase, Square Cash, Gemini), and monetary "
            "policy credibility — not earnings multiples. Satoshi's whitepaper targets internet payments weakness; "
            "store-of-value narrative followed. Incumbent finance (Stripe, ACH 3–5-day batching) layers on old "
            "trust; Bitcoin replaces trust assumption. Watch drawdowns: 2018 down 72%, March 2020 below $4,000. "
            "Hosts open with tax-payment UX exposing routing-number fragility — everyday proof legacy rails "
            "were not built for internet-native commerce. Lightning and custody layers extend without changing "
            "base scarcity; Domino's pizza thread reminds listeners returns and protocol cleverness are separable."
        ),
    },
    competitive_advantage=(
        "Bitcoin's moat is first-mover liquidity and cumulative proof-of-work — rewriting history now requires "
        "more hash power than the chain's entire past. No company controls issuance; the 21-million cap contrasts "
        "with fiat debasement narratives that accelerated post-2020 stimulus. Exchange and custodian rails "
        "(Coinbase, Gemini, Square Cash) lowered onboarding friction without compromising base-layer neutrality.\n\n"
        "Developer and miner ecosystem decentralization resists single-point policy changes — upgrades require "
        "broad consensus (SegWit, Lightning layer-two). Brand and ticker recognition make BTC the default crypto "
        "macro hedge in institutional conversations; Winklevoss twins' pivot from $300M Facebook stock to crypto "
        "exemplifies smart-money narrative shifts.\n\n"
        "Versus altcoins and ICO scams washed out in 2018, Bitcoin survived as the trust anchor — hosts note "
        "decentralization is double-edged (no customer support when keys are lost) but also censorship-resistant. "
        "Traditional finance innovation (Stripe, PayPal) improves UX atop old trust; Bitcoin replaces the trust "
        "assumption entirely — a thicker technical moat once hash power scaled.\n\n"
        "Weaknesses: energy intensity, seven TPS base-layer limits, Mt. Gox-style custody failures, Silk Road "
        "stigma, and violent drawdowns (2018 down 72%; March 2020 below $4,000). Satoshi's ~1M idle coins and "
        "quantum-computing tail risks linger. Yet each cycle left a higher floor — 2013 ~$770, 2017 ~$20,000, "
        "2021 ~$30,000 — as infrastructure matured.\n\n"
        "Historical catalysts layered narrative atop protocol: 10,000-BTC pizza (~$41), Silk Road's 1.2M+ "
        "transactions moving ~10M BTC, Tim Draper buying Silk Road auction coins for $17M publicity, Cameron "
        "and Tyler's $45M Facebook-stock pivot to ~$300M then crypto all-in. Palantir grew from PayPal fraud "
        "fighting — same trust-problem family Bitcoin addresses at the base layer rather than middleware."
    ),
    key_insights=[
        {
            "view": "Satoshi targeted internet payments, not ideology.",
            "question": "What problem does the whitepaper actually solve?",
            "answer": "Opening paragraphs criticize trusted third parties and non-reversible online payments — not inflation doctrine. Nine-page paper proposes peer-to-peer timestamping; chargebacks plague internet merchants on 2.9%-plus-30¢ card rails. Libertarian culture followed engineering fix — hosts stress whitepaper is commerce problem first.",
        },
        {
            "view": "Mining converts electricity into ledger security.",
            "question": "Why do bitcoins have value?",
            "answer": "Holders own a claim on the cumulative hash power securing the chain. Block rewards fell from 50 to 6.25 BTC per ~10-minute block as halvings progressed toward 21 million cap. Miners validate ordering; difficulty rises with participation, making forgery exponentially costly — hosts compare to needing entire historical hash power plus margin to rewrite blocks.",
        },
        {
            "view": "Each bubble reset a higher floor.",
            "question": "How did price evolve 2011–2021?",
            "answer": "Silk Road and exchanges took BTC from ~$5 (2011) to ~$770 (2013); Mt. Gox collapse and ICO scammers crushed 2014–15 sentiment near $300–500. 2017 peaked near $20,000 on ICO-fueled hype; 2018 fell 72% to ~$3,700. COVID March 2020 briefly dipped below $4,000 despite 'digital gold' thesis — then fiscal stimulus, 0% rates, Square/Coinbase rails, and MicroStrategy treasury buys pushed recovery past $30,000 by January 2021.",
        },
        {
            "view": "Lost keys are permanent supply destruction.",
            "question": "What did Mt. Gox teach?",
            "answer": "750,000+ client coins vanished when exchange failed — keys gone, not merely illiquid. Hosts compare self-custody to stuffing millions in jacket pockets; Coinbase/Gemini custody became mainstream onboarding. Silk Road moved ~10M BTC across 1.2M+ transactions — illicit use spiked 2011–13 price before infrastructure matured.",
        },
        {
            "view": "Macro regimes drive institutional adoption waves.",
            "question": "Why 2020 corporate treasuries?",
            "answer": "0% rates and expanded M2 pushed investors from bonds toward equities and BTC. MicroStrategy's $250M treasury classification signaled balance-sheet legitimacy. March 2020 crash below $4,000 contradicted hedge narrative short-term; fiscal stimulus and Fed expansion reframed BTC as scarce asset vs. debasing fiat by January 2021.",
        },
    ],
    top_investment_implications=[
        {
            "ticker": "BTC",
            "direction": "Watch",
            "confidence": "Medium",
            "thesis": "Episode frames BTC as macro optionality when real rates are negative and fiscal expansion is high — not investment advice, but documents institutional treasury and retail-rail maturation.",
        },
        {
            "ticker": "COIN",
            "direction": "Watch",
            "confidence": "Low",
            "thesis": "Coinbase and peers built 2018–2020 custody/on-ramps that survived the ICO washout — picks-and-shovels beneficiary if BTC adoption continues without protocol risk.",
        },
        {
            "ticker": "SQ",
            "direction": "Watch",
            "confidence": "Low",
            "thesis": "Square Cash app native crypto buying (2018) mainstreamed retail access — incremental distribution layer on Bitcoin base protocol without replacing trust model.",
        },
    ],
    golden_quotes=[
        "\"Commerce on the internet has come to rely almost exclusively on financial institutions serving as trusted third parties\" — Satoshi whitepaper opener quoted by hosts.",
        "\"From less than 1¢ to over $30,000 — a 3,000,000X investment return\" — Ben on Bitcoin's first decade.",
        "\"Risk equals permanent capital loss\" — thematic parallel to Howard Marks via lost Mt. Gox keys and irreversible on-chain transfers.",
    ],
    chronology={
        "subject": "Bitcoin",
        "events": [
            {"date": "14th c.", "event": "Italian Renaissance banking and double-entry bookkeeping emerge"},
            {"date": "2008-10", "event": "Satoshi Nakamoto publishes Bitcoin whitepaper"},
            {"date": "2009", "event": "Genesis block; mining rewards begin at 50 BTC per block"},
            {"date": "2010-05", "event": "10,000 BTC pizza purchase (~$41)"},
            {"date": "2010–11", "event": "Satoshi disappears; hands repos to early developers"},
            {"date": "2011", "event": "BTC ~$5; Silk Road era begins"},
            {"date": "2013", "event": "Price peaks ~$770 before exchange crises"},
            {"date": "2014", "event": "Mt. Gox collapses; 750,000+ client BTC lost"},
            {"date": "2017–18", "event": "Run to ~$20,000 then 72% drawdown in 2018"},
            {"date": "2020-03", "event": "COVID crash below $4,000"},
            {"date": "2020-08", "event": "MicroStrategy holds $250M BTC as treasury reserve"},
            {"date": "2021-01", "event": "Acquired records; BTC trading above $30,000"},
        ],
    },
)

EPISODES["acq-special-acquired-x-indie-hackers"] = base(
    "acq-special-acquired-x-indie-hackers",
    review_notes=NOTES,
    episode_rating={"overall": 4},
    keywords=["Profitable Startups", "Stripe Acquisition", "Community Media"],
    conclusion=(
        "Courtland Allen's Indie Hackers crossover reframes wealth creation beyond VC unicorns: internet "
        "niches are globally addressable, so solo founders can build seven-figure businesses with less "
        "risk than Rockefeller-scale bets. After MIT, repeated YC applications, and Taskforce (a "
        "profitable task-list pivot), Courtland launched Indie Hackers in 2016 — interviews plus revenue "
        "transparency that \"exfiltrated\" Hacker News's bootstrap segment. Stripe acquired the community "
        "~3.5 years before recording; ~140,000 users at deal time grew toward 100,000+ new company profiles "
        "post-acquisition, with hosts estimating 15,000–20,000 Stripe-relevant startups influenced. "
        "Unlike Salesforce-Slack price-driven M&A, this was a talent-and-pipeline bet keeping Courtland "
        "autonomous — YouTube-to-Google playbook for developer go-to-market with 15%–20% of post-deal startups "
        "potentially Stripe-influenced per host estimates."
    ),
    background=(
        "Acquired hosts Courtland Allen, MIT alum and YC founder, for crossover with Indie Hackers podcast. "
        "Arc: childhood entrepreneurship, Hacker News participation, YC Taskforce batch, string of small products "
        "before 2016 Indie Hackers — interviews with real revenue and profit numbers.\n\n"
        "Ben and David contrast DoorDash/Airbnb IPO playbooks with thousands of replicable indie stories. "
        "Courtland explains platform risk, Stripe acquisition (~140K users, 100K+ profiles post-deal), deal "
        "structure over headline price, and shift from blog to software profiles. Stripe Press and Atlas cited "
        "as parallel in-house brand experiments vs. acquired community."
    ),
    important_facts=[
        "Courtland Allen attended MIT, applied to Y Combinator repeatedly, and co-founded Taskforce through YC before launching Indie Hackers as a 2016 media site with revenue-transparent founder interviews.",
        "Indie Hackers featured disclosed revenue and profit in every interview — a trust signal Courtland compares to Zillow-style price transparency before home-value estimates existed online.",
        "Stripe acquired Indie Hackers approximately 3.5 years before the December 2020 episode; roughly 140,000 users at deal time grew with 100,000-plus company profiles added post-acquisition.",
        "Hosts estimate 15%–20% of ~100,000 post-acquisition company profiles may owe major inspiration to Indie Hackers — implying 15,000–20,000 potential Stripe-adjacent startups influenced by the community.",
        "Courtland ran Indie Hackers solo with zero employees at sale — deal economics centered on personal vesting and alignment with Patrick Collison, not headline cash like Salesforce's $27.7 billion Slack bid.",
    ],
    mental_model={
        "name": "Optionality-Preserving Entrepreneurship",
        "components": (
            "VC's grow-at-all-costs path forecloses strategy; profitability-first indie hacking preserves "
            "option value to raise, sell, or compound forever. Internet niches are globally addressable — "
            "one narrow SaaS can exceed local dry-cleaner TAM. Community media (interviews + revenue data) "
            "builds trust faster than hype posts. Platform risk (HN, email, podcast alphabetic feeds) pushes "
            "owned audience relationships."
        ),
        "application": (
            "Sell into existing budgets; platforms buy communities for pipeline, not ARR. Structure deals for "
            "autonomy when asset is person-plus-brand. Document niche playbooks — 100K stories beat one Airbnb "
            "saga for operator learning. Courtland's HN exfiltration and email unlock mirror Acquired's Slack/"
            "newsletter platform-risk hedges. Stripe's 15%–20% influenced startup estimate quantifies ROI on "
            "community acquisition vs. paid developer marketing."
        ),
    },
    competitive_advantage=(
        "Indie Hackers' moat is curated revenue-transparent stories plus Courtland's credibility as "
        "builder-host — hard to clone without years of HN/YC/community participation. Stripe acquisition "
        "added payments distribution without killing brand independence (\"By Stripe\" light touch), "
        "analogous to YouTube staying YouTube inside Google while Google Video failed.\n\n"
        "Email and interview pipeline created repeat touchpoints — supply (founders sharing numbers) and "
        "demand (readers seeking playbooks) reinforce each other. Courtland's Taskforce-era lesson — stay alive "
        "until not dead — seeded persistence culture the community now teaches at scale.\n\n"
        "Versus VC-media (TechCrunch unicorn fixation), Indie Hackers documents $10K–$10M MRR paths with "
        "named tactics — higher signal for operators. Stripe estimates 15%–20% of post-acquisition company "
        "profiles may trace inspiration to IH, implying tens of thousands of payment customers influenced.\n\n"
        "Weaknesses: platform dependence on Stripe strategy; media scales with founder attention; Twitter/ "
        "Substack fragment discovery. Barbell economy may concentrate megacap platforms while long-tail grows — "
        "IH must keep trust as it scales past 100,000 stories.\n\n"
        "Courtland's Taskforce-to-Indie arc shows optionality: profitable task app could have been lifestyle "
        "business; community insight became strategic asset. Stripe Press, Atlas, and internal tools contrast "
        "with acquired community — YouTube-outlived-Google-Video template. HN exfiltration, email unlock, "
        "and podcast crossover distribution mirror Acquired's own platform-risk management playbook."
    ),
    key_insights=[
        {
            "view": "Indie hacking preserves strategic optionality.",
            "question": "How is this different from VC's default path?",
            "answer": "Raising venture forces growth trajectory; profitable start leaves raise/sell/stay options. PG hill-climbing: higher local maxima lead toward global maxima. Courtland's YC Taskforce could have been lifestyle business; Indie Hackers became strategic community asset worth Stripe acquisition.",
        },
        {
            "view": "Revenue disclosure is the trust primitive.",
            "question": "Why publish profit numbers?",
            "answer": "Readers needed proof advice worked — Zillow for home prices before estimates. Revenue/profit interviews closed loop on replicable playbooks. Bad data poisons model; transparency differentiated IH from motivational blogging and HN hype posts.",
        },
        {
            "view": "Stripe bought pipeline, not ARR.",
            "question": "Why acquire a media community?",
            "answer": "Stripe wanted founders building internet businesses who need payments — Courtland was pick #1 on a crazy-ideas list. Deal structured around autonomy and incentives, not headline dollars; corporate M&A comps (Salesforce-Slack) mislead for solo-founder sales.",
        },
        {
            "view": "Platform risk is universal.",
            "question": "How did Courtland manage HN dependence?",
            "answer": "He \"exfiltrated\" bootstrap content from Hacker News into owned site plus email — same playbook as Airbnb Craigslist growth but for community segment. Email unlocks supply (interviewees) and demand (readers) even with algorithmic feed risk.",
        },
        {
            "view": "Long-tail playbooks beat single unicorn myths.",
            "question": "Why crossover with Acquired?",
            "answer": "DoorDash/Airbnb tactics apply to few; 100,000 indie stories let founders copy a business three years ahead in their niche. Economic activity from indie entrepreneurs may rival classic industrial magnates in aggregate — with far more templates to learn from.",
        },
    ],
    top_investment_implications=[
        {
            "ticker": "STRIPE",
            "direction": "Watch",
            "confidence": "Low",
            "thesis": "Private company — Indie Hackers acquisition illustrates Stripe's developer GTM: buy communities that seed payment customers; hosts estimate 15K–20K influenced startups post-deal.",
        },
        {
            "ticker": "SHOP",
            "direction": "Watch",
            "confidence": "Low",
            "thesis": "Shopify ecosystem cited as parallel platform for indie merchants — long-tail entrepreneurship complements Stripe payments rails.",
        },
    ],
    golden_quotes=[
        "\"If you start by saying growth at all costs, don't make any money, you're on a very specific path\" — Ben on VC vs. indie optionality.",
        "\"Sell the things that have budgets\" — Courtland's sales lesson: sell into existing line items, don't create budget from scratch.",
        "\"With an Indie Hacker business, no, it's you\" — David contrasting Stripe-Indie Hackers deals with Salesforce's $27.7B Slack acquisition.",
    ],
    chronology={
        "subject": "Courtland Allen / Indie Hackers",
        "events": [
            {"date": "Childhood", "event": "Courtland's mother runs small business; early computer repair income"},
            {"date": "MIT era", "event": "Repeated YC applications; Hacker News community participation"},
            {"date": "YC batch", "event": "Taskforce task-list company through Y Combinator"},
            {"date": "2016", "event": "Courtland launches Indie Hackers site and interview blog"},
            {"date": "2016–17", "event": "Revenue-transparent interviews; email list becomes growth lever"},
            {"date": "~2017", "event": "Stripe acquires Indie Hackers; Courtland stays to run brand"},
            {"date": "2017–20", "event": "Community grows from ~140K users; software profiles added"},
            {"date": "2020-12", "event": "Acquired x Indie Hackers crossover recorded"},
            {"date": "Post-acq", "event": "100,000+ new company profiles added under Stripe ownership"},
            {"date": "Ongoing", "event": "Stripe Press, Atlas parallel in-house brand experiments"},
        ],
    },
)

EPISODES["acq-airbnb"] = base(
    "acq-airbnb",
    review_notes=NOTES,
    episode_rating={"overall": 5},
    keywords=["Global Network Effect", "Marketplace Liquidity", "Travel IPO"],
    conclusion=(
        "Airbnb's December 2020 IPO — raising $3.5B+ at a $47B+ initial valuation amid a pandemic — caps "
        "a 13-year arc from three air mattresses at a 2007 design conference ($80/night) to 220 countries, "
        "100,000 cities, $38B in prior-year bookings, 50M+ active guests, and 7M+ listings. Sequoia's 2009 "
        "seed ($585K at ~24% ownership) and ground-war financing against Samwer brothers' Wimdu built a "
        "global network effect CouchSurfing lacked because it never processed payments. Killer float — guests "
        "prepay weeks or months ahead — funded growth while DoorDash burned cash. COVID cut 2020 revenue "
        "~30% and forced layoffs, yet IPO readiness and brand trust enabled a travel company to go public "
        "during stay-at-home orders — proof marketplace liquidity and host supply depth matter as much as "
        "near-term GBV growth, especially contrasted with DoorDash logistics IPO the prior day."
    ),
    background=(
        "Season 7 finale covers Airbnb's IPO day with Brad Stone's The Upstarts as primary source. Founders "
        "Brian Chesky (RISD), Joe Gebbia, and Nate Blecharczyk (Harvard CS, ~$1M pre-college email marketing) "
        "pivot from Obama O's/Cap'n McCain's cereal stunt ($20K–$30K profit) through YC 2009 to Sequoia's "
        "Greg McAdoo seed during RIP Good Times.\n\n"
        "Episode contrasts CouchSurfing (no payments), Craigslist supply scraping, professional photography "
        "conversion lifts, European Wimdu clone wars, $112M Series B (2011, >$1B valuation), and years of IPO "
        "speculation. 2019 bookings growth slowed toward ~29%; 2020 pandemic cut revenue ~30% yet public "
        "markets welcomed a travel marketplace at tens of billions — juxtaposed with DoorDash logistics IPO "
        "the prior day. Alfred Lin — Sequoia board member on both companies — links to the concurrent "
        "Investment Playbook special."
    ),
    important_facts=[
        "Airbnb IPO (December 2020) raised over $3.5 billion at an initial valuation above $47 billion — a travel marketplace going public during peak pandemic stay-at-home orders when 2020 revenue fell roughly 30%.",
        "Platform spanned 220 countries, 100,000 cities, $38 billion in 2019 gross bookings, 50 million-plus active guests, and 7 million-plus listings at IPO — scale CouchSurfing never approached because it lacked payments.",
        "Sequoia's January 2009 seed invested $585,000 for approximately 24⅜% ownership during the financial crisis months after the RIP Good Times memo urged portfolio triage.",
        "Founders sold limited-edition Obama O's and Cap'n McCain's cereal for an estimated $20,000–$30,000 profit to fund rent before Y Combinator winter 2009 batch acceptance.",
        "By June 2012 cumulative nights booked jumped from 5 million to 10 million in six months; 2011 Series B from Andreessen Horowitz exceeded $112 million at over $1 billion valuation.",
    ],
    mental_model={
        "name": "Payments-Enabled Trust Marketplace",
        "components": (
            "CouchSurfing proved couch culture but without payments and professional photos couldn't monetize "
            "or scale trust. Airbnb added payment capture, host/guest reviews, identity verification, and "
            "photography — converting stranger danger into transaction confidence. Global cross-side network "
            "effects compound as supply and demand diversify geographically. Guest prepayment creates negative "
            "working capital (float) funding expansion — opposite of SaaS monthly billing."
        ),
        "application": (
            "Marketplaces must own payment moment to capture take rate and data flywheel. Photography and identity "
            "are conversion infrastructure. When clone wars arrive, liquidity depth matters more than features. "
            "IPO timing can decouple from near-term GBV if brand survives shocks — COVID proved host supply "
            "persistence. Contrast DoorDash capital intensity same IPO week: Airbnb could 'fly high' on float while "
            "logistics burned cash. Alfred Lin board ties to Sequoia playbook episode — prepared-mind seed in "
            "2009 crisis looks brilliant at $47B IPO despite 30% revenue dip."
        ),
    },
    competitive_advantage=(
        "Airbnb's moat is global two-sided liquidity — guests find unique inventory hotels cannot replicate; "
        "hosts access demand worldwide. Trust stack (reviews, verified ID, host guarantees, professional "
        "photos) raised conversion where couch-surfing failed. Take-rate economics plus guest prepayment float "
        "fund growth without per-city warehouse capex (vs. DoorDash).\n\n"
        "Brand and community ethos (belong anywhere) sustain pricing power in experiential travel. Sequoia, "
        "Andreessen, and Greylock capital let Airbnb outspend European Samwer clones (Wimdu) and buy time for "
        "network effects to lock in — Alfred Lin board role links to Sequoia playbook episode same week.\n\n"
        "Experiences and long-stay pivots post-COVID extend beyond nights booked; host supply survived 2020 "
        "shock while hotels closed — proof liquidity depth matters in downturns. Brad Stone sourcing anchors "
        "episode in documented history versus mythologized founding alone.\n\n"
        "Weaknesses: regulatory battles, party incidents, 2020 GBV collapse, 2019 linear bookings adds. "
        "Brian's IPO resistance vs. fund lifecycles; Google and hotel chain competition. Yet IPO at $47B+ "
        "after 30% revenue shock proved host supply and brand survived — competitors HomeAway sold to Expedia "
        "for ~$4B in effective surrender.\n\n"
        "Fundraising arc reinforces moat: seed $585K (24%), Series A $7.2M Greylock, $112M a16z Series B "
        "above $1B (2011), $500M TPG at $10B (2014), $1.5B rounds at $25B valuation (2015–16). Fred Wilson "
        "publicly regretted passing after USV intro. Expedia bought HomeAway ~$4B — admission no product "
        "competitor matched global liquidity. Experiences and long-stay pivots extend TAM beyond nights."
    ),
    key_insights=[
        {
            "view": "Payments separate winners from CouchSurfing.",
            "question": "Why did CouchSurfing not become Airbnb?",
            "answer": "CouchSurfing facilitated free stays with optional identity verification fees — no payment rail, no host income, no professional listing quality. Benchmark-backed CouchSurfing had reviews and photos but never processed transactions; Airbnb's $80/night airbeds at the 2007 design conference proved strangers would pay if trust infrastructure converted. Nate Blecharczyk's spam-marketing skills and payment stack closed the loop CouchSurfing's nonprofit model could not monetize at scale.",
        },
        {
            "view": "Float is a hidden balance-sheet weapon.",
            "question": "How does prepayment help?",
            "answer": "Guests book weeks or months ahead, handing Airbnb cash before stays — negative working capital funding supply growth. DoorDash burns cash per delivery; SaaS bills monthly. When GBV scaled to $38B (2019), float magnitude dwarfed early cereal profits. Pandemic tested model: revenue fell ~30% but host supply remained, enabling $47B IPO pricing on rebound optionality rather than trailing GBV alone.",
        },
        {
            "view": "Clone wars test global network effects.",
            "question": "How did Wimdu get beaten?",
            "answer": "Samwer brothers cloned Airbnb in Europe; Sequoia financed ground war while Greylock led $7.2M Series A. Airbnb won on cross-border supply-demand — guests planning international trips need 220-country liquidity, not Berlin-only inventory. Wimdu never matched; network economies of scale favored first mover with capital during 2011 $112M a16z round above $1B valuation.",
        },
        {
            "view": "COVID IPO was a narrative stress test.",
            "question": "Why go public during a pandemic?",
            "answer": "2020 revenue fell ~30% with layoffs; IPO still at $47B+ pricing rebound optionality. Brian resisted public markets for years; 2019 bookings growth slowed to ~29% with linear $8.5B incremental adds. Fund lifecycles forced bar mitzvah at 13 years — day after DoorDash IPO highlighted capital-model contrast.",
        },
        {
            "view": "Scrappy stunts don't predict enterprise value.",
            "question": "Do Obama O's matter?",
            "answer": "Cereal stunt generated $20K–$30K and PR — awesome only because Airbnb later worked. Designers poured Cheerios into custom boxes for margin; illustrates founder grit theme. Double-edged: furniture-sale profits at failed startups look identical in hindsight until liquidity proves otherwise.",
        },
    ],
    top_investment_implications=[
        {
            "ticker": "ABNB",
            "direction": "Watch",
            "confidence": "Medium",
            "thesis": "IPO at $47B+ embeds global liquidity and brand optionality post-COVID; monitor GBV re-acceleration vs. 2019's ~29% growth slowdown and regulatory drag.",
        },
        {
            "ticker": "EXPE",
            "direction": "Watch",
            "confidence": "Low",
            "thesis": "Expedia's ~$4B HomeAway purchase signaled surrender in alternative accommodations — indirect read on Airbnb's remaining competitive set in public markets.",
        },
        {
            "ticker": "BKNG",
            "direction": "Watch",
            "confidence": "Low",
            "thesis": "Booking Holdings exposure to hotel recovery vs. Airbnb experiential share shift — travel reopening trade with different inventory models.",
        },
    ],
    golden_quotes=[
        "\"Turning our place into a designer's bed and breakfast\" — Joe Gebbia's famous 2007 \"subletter\" email to Brian, origin of Airbnb.",
        "\"Payments are the thing CouchSurfing was missing\" — David on why monetization and trust infrastructure defined the category winner.",
        "\"13 years old — the bar mitzvah of Airbnb\" — Ben on IPO timing, 2020.",
    ],
    chronology={
        "subject": "Airbnb",
        "events": [
            {"date": "2007", "event": "Airbedandbreakfast.com launches for SF design conference; $80/night"},
            {"date": "2008", "event": "Obama O's/Cap'n McCain's raise $20K–$30K; YC Startup School with Bezos AWS talk"},
            {"date": "2009", "event": "YC winter batch; Sequoia seeds $585K for ~24% ownership"},
            {"date": "2010", "event": "700,000 nights booked; Greylock Series A"},
            {"date": "2011", "event": "1M nights booked; $112M Series B from a16z above $1B valuation"},
            {"date": "2012", "event": "Cumulative nights jump from 5M to 10M in six months"},
            {"date": "2014", "event": "$500M from TPG at ~$10B valuation"},
            {"date": "2016", "event": "~$14B bookings; $25B valuation round"},
            {"date": "2019", "event": "Bookings growth slows to ~29%; linear $8.5B adds"},
            {"date": "2020", "event": "COVID hits; revenue down ~30%; December IPO above $47B"},
        ],
    },
)

EPISODES["acq-doordash"] = base(
    "acq-doordash",
    review_notes=NOTES,
    episode_rating={"overall": 4},
    keywords=["Last-Mile Logistics", "Suburban Density", "Food Delivery"],
    conclusion=(
        "DoorDash's 2020 IPO caps a seven-year sprint from paloaltodelivery.com (2013) — a Stanford "
        "Design Garage class project with $6 flat delivery fees and Find My Friends courier tracking — to "
        "dominant US food delivery. Suburban San Jose expansion beat dense-city strategies because parking, "
        "queues, and 12th-floor drops punish urban ops; by early 2014 one in six Peninsula residents had "
        "ordered. SoftBank's 2018 $535M Series D at $1.4B post (38% dilution) followed a 2017 bridge when "
        "cash ran out; Sequoia repeatedly stepped up. Market share rose from 17% (Jan 2018) to 50% (Oct 2020) "
        "while Uber Eats and Postmates lagged. 2019: $885M net revenue, $8B GOV, 263M orders, 60% same-store "
        "sales growth. Pandemic March 2020 added 20%+ GBV in one month off an $8B base. DashPass (5M members, "
        "$10/month) and suburban logistics DNA explain why capital-intensive delivery may work — if gig "
        "economics and Prop 22 hold — Alfred Lin's second Sequoia portfolio IPO in two days after Airbnb."
    ),
    background=(
        "Tony Xu, Stanley Tang, Andy Fang, and Evan Moore start Palo Alto Delivery in Stanford's Design "
        "Garage class (2012–13), inspired by Square's smartphone-enabled merchants and absent suburban "
        "delivery outside pizza chains. Grubhub/Seamless owned NYC with restaurant-employed couriers — "
        "capital-light but geographically limited. DoorDash owned fulfillment with 1099 drivers.\n\n"
        "YC summer 2013 → $2.4M seed (Keith Rabois/Khosla). Series B: John Doerr, $40M at $600M (2015). "
        "SoftBank dump then darling: $535M at $1.4B (38% dilution), 2017 $60M bridge, recovery to $600M at "
        "$12.6B (2019). Caviar acquired from Square. S-1 reveals brutal capital path while share rose 17%→50% "
        "2018–2020. Recorded alongside Airbnb IPO week — Alfred Lin's second portfolio IPO in two days."
    ),
    important_facts=[
        "DoorDash US market share grew from 17% (January 2018) to 50% (October 2020) — surpassing Uber Eats, Grubhub, and Postmates in roughly 2¾ years per S-1 analysis.",
        "2019 metrics: $885 million net revenue (more than 3X year-on-year), $8 billion gross order value, 263 million orders, and 60% same-store sales growth excluding new markets and restaurant additions.",
        "SoftBank invested $535 million in 2018 at $1.4 billion post-money valuation — 38% dilution with per-share price still below John Doerr's 2015 Series B at $600 million post.",
        "By early 2014 one in six San Francisco Bay Peninsula residents had used DoorDash — roughly one year after first paloaltodelivery.com delivery to a Weed the People author.",
        "DashPass membership reached 5 million subscribers at $10 per month — a $600 million annual run-rate if fully paid, reducing consumer fees to build habit versus Uber Eats checkout sticker shock.",
    ],
    mental_model={
        "name": "Suburban Fulfillment at Lowest-Level Detail",
        "components": (
            "Food delivery is three-sided (consumer, restaurant, driver) vs. rideshare's two-sided match — "
            "parking, in-store queues, and apartment drops dominate unit economics. DoorDash won suburbs "
            "where Grubhub's restaurant-courier model failed density tests. Gig 1099 labor variabilizes "
            "off-peak cost. DashPass bundles habit; national chains (Yum!) scale supply after local grind. "
            "Average delivery time distributions matter — 53-minute tail kills NPS even if mean is 35."
        ),
        "application": (
            "Map real-world ops before TAM models — suburbs beat cities for delivery throughput. Watch dilution: "
            "2018 SoftBank 38% sale vs. 2019 <5% raise signals leverage cycles. Compare Meituan when US skeptics "
            "peak. Tony's Square DNA and Keith Rabois seed explain why Khosla funded when Sand Hill scoffed at "
            "food delivery. DashPass and Yum! partnerships nationalize after Peninsula land-grab where one in six "
            "residents ordered within a year of first delivery."
        ),
    },
    competitive_advantage=(
        "DoorDash's edge is suburban operational obsession — \"lowest level of detail\" on parking, routing "
        "(early Find My Friends), and restaurant onboarding — plus owning courier fulfillment while Grubhub "
        "aggregated restaurant drivers. Sequoia and SoftBank capital funded land-grab when Uber chased rides.\n\n"
        "DashPass ($10/month, 5M members) mirrors Prime habit formation, shaving fees consumers feel at "
        "checkout. Yum! Brands (Taco Bell, KFC) partnerships nationalize supply after city-by-city grind. "
        "Tony Xu's Square internship and Keith Rabois seed tie PayPal-mafia operating DNA to capital access.\n\n"
        "Pandemic accelerated adoption: 20%+ monthly GBV growth March 2020 off $8B annual base while "
        "competitors priced aggressively on thin margins. Meituan China proof point gave SoftBank conviction "
        "after 2018 dilution round — US skepticism reversed once share hit 50% by October 2020.\n\n"
        "Weaknesses: gig-worker legal risk (Prop 22 in California), persistent dilution, low early investor "
        "ownership in S-1, thin margins. Capital intensity means share gains must justify billions raised; "
        "suburban TAM finite without adjacent categories at scale.\n\n"
        "Capital table tells the story: $2.4M seed (Khosla/Keith Rabois), $40M Series B at $600M (Doerr), "
        "$125M+ 2015 round, $60M 2017 bridge, $535M SoftBank 2018 at $1.4B (38% dilution), $250M 2019 at "
        "less than 5% dilution, $600M at $12.6B, Caviar $410M from Square. Khosla/CRV/SV Angel/Pear from seed "
        "fell below 5% S-1 — extraordinary dilution path. Uber raised ~$8B lifetime; DoorDash won with "
        "hundreds of millions plus operational excellence."
    ),
    key_insights=[
        {
            "view": "Suburbs beat cities for delivery ops.",
            "question": "Why launch San Jose not SF?",
            "answer": "Dense cities mean parking tickets, restaurant queues, high-rise drops — killing throughput. San Jose suburban routes improved averages; Tony's quote: consumers remember 53-minute tails not 35-minute means. Peninsula land-grab hit one-in-six residents within a year. Find My Friends iPhone tracking was hacky real-time ops before dedicated logistics stack.",
        },
        {
            "view": "Fulfillment ownership was the category insight.",
            "question": "How was Grubhub different?",
            "answer": "Grubhub/Seamless (profitable, public since early 2000s) passed orders to restaurant couriers — worked in NYC bikes, not Palo Alto sprawl. DoorDash 1099 drivers unlocked suburbs and national chains. Initial $6 flat delivery fee model persisted in spirit; DashPass $10/month now reduces fee friction for 5M members.",
        },
        {
            "view": "SoftBank round was dilution shock then catalyst.",
            "question": "What happened in 2018?",
            "answer": "$535M at $1.4B post sold 38% — per-share price below 2015 Kleiner Series B at $600M post despite higher headline valuation. Capital funded share war vs. Uber Eats and Postmates; Meituan China proof gave SoftBank conviction. By March 2019 DoorDash raised $250M at less than 5% dilution — leverage returned after competitors stumbled.",
        },
        {
            "view": "Sequoia conviction through bridges.",
            "question": "Who saved the company in 2017?",
            "answer": "S-1 revealed $60M insider bridge when cash exhausted end of 2017 — Sequoia among backers keeping DoorDash alive pre-SoftBank. Alfred Lin committed up to $40M pro-rata at $1B cap before external pricer. Pattern built ~18% IPO stake through bridges and follow-ons when Sand Hill skeptics passed on food delivery.",
        },
        {
            "view": "Pandemic was hyper-growth on huge base.",
            "question": "How big was COVID bump?",
            "answer": "March 2020 delivered 20%+ GBV growth in one month off $8B+ prior-year GOV — seed-stage velocity at scale. Share rose 17%→50% by October 2020 while Uber Eats grew slower; DashPass retention and restaurant lockdowns shifted habits. Prop 22 preserved California 1099 model underpinning variable labor economics.",
        },
    ],
    top_investment_implications=[
        {
            "ticker": "DASH",
            "direction": "Watch",
            "confidence": "Medium",
            "thesis": "50% US share and DashPass habit offset capital intensity; monitor gig regulation and post-pandemic order retention vs. 2019's 3X revenue growth baseline.",
        },
        {
            "ticker": "UBER",
            "direction": "Watch",
            "confidence": "Low",
            "thesis": "Uber Eats lost share as DoorDash hit 50% — read on whether rides business can subsidize delivery or if separation is inevitable.",
        },
        {
            "ticker": "GRUB",
            "direction": "Watch",
            "confidence": "Low",
            "thesis": "Grubhub's capital-light restaurant-courier model lost to fulfillment-first DoorDash — legacy profitable aggregator vs. growth-share loser.",
        },
    ],
    golden_quotes=[
        "\"Averages in our industry are meaningless\" — Tony Xu on delivery-time distributions (quoted by David).",
        "\"One in six people on the Peninsula had used DoorDash\" — David on 2014 suburban land-grab metrics.",
        "\"We are a logistics company more so than a food company\" — DoorDash 2013 Medium post after $2.4M seed.",
    ],
    chronology={
        "subject": "DoorDash",
        "events": [
            {"date": "Fall 2012", "event": "Stanford Design Garage class; paloaltodelivery.com concept"},
            {"date": "Summer 2013", "event": "YC batch; renamed DoorDash; $2.4M seed led by Khosla"},
            {"date": "Early 2014", "event": "1 in 6 Peninsula residents orders; San Jose expansion"},
            {"date": "2015", "event": "$40M Series B from Kleiner at $600M; John Doerr joins board"},
            {"date": "2017", "event": "$60M insider bridge when cash exhausted"},
            {"date": "2018", "event": "SoftBank $535M at $1.4B post — 38% dilution"},
            {"date": "2019", "event": "$885M revenue; passes Grubhub; buys Caviar from Square"},
            {"date": "2019", "event": "$600M round at $12.6B valuation"},
            {"date": "2020-03", "event": "COVID drives 20%+ monthly GBV growth"},
            {"date": "2020", "event": "IPO; market share reaches 50% by October"},
        ],
    },
)

EPISODES["acq-slack-salesforce-emergency-pod-with-packy-mccormick-of-not-boring"] = base(
    "acq-slack-salesforce-emergency-pod-with-packy-mccormick-of-not-boring",
    review_notes=NOTES,
    episode_rating={"overall": 4},
    keywords=["Enterprise M&A", "Microsoft Teams", "SaaS Distribution"],
    conclusion=(
        "Hours after Salesforce announced a $27.7 billion acquisition of Slack ($45.86/share, ~55% premium "
        "to pre-leak price, ~85% above September earnings crash), Ben, David, and Packy McCormick unpack "
        "an emergency pod. Slack — DPO'd as the anti-Microsoft best-of-breed champion — sold after Teams "
        "bundling and go-to-market limits capped growth despite top-quartile SaaS metrics. Microsoft Teams "
        "competes more with Zoom than Slack per Packy, yet Microsoft markets Teams vs. Slack while giving "
        "O365 away. Salesforce positions the deal as anti-Microsoft consolidation for best-of-breed SaaS; "
        "hosts grade Slack's public tenure C- and debate whether $28B buys distribution or product atrophy "
        "(Heroku/Quip comps). Zoom's ~$130B market cap made stock merger impractical; Google sat out. Emergency "
        "pod recorded on YouTube Live two hours post-announcement with Packy McCormick."
    ),
    background=(
        "Recorded December 2020 amid DoorDash and Airbnb IPO week, this emergency episode features Not Boring's "
        "Packy McCormick — prominent Slack bull — hours after the Salesforce deal broke. Stewart Butterfield's "
        "\"We Don't Sell Saddles Here\" blog defined enterprise chat category creation; transaction is largest "
        "pure software M&A since IBM-Red Hat (2018).\n\n"
        "Debate covers Teams vs. Zoom positioning, why Zoom didn't bid at ~$130B market cap, Salesforce "
        "financing vs. Google's balance sheet, Slack staying independent post-close, and five-year A+ to F "
        "scenarios. Packy published bullish thesis two weeks prior cc'ing Benioff. Hosts grade Slack public "
        "tenure C- — above DPO price for bulls but below standalone upside."
    ),
    important_facts=[
        "Salesforce agreed to acquire Slack for $27.7 billion — $45.86 per share in roughly 55% cash and 45% stock, a 55% premium to pre-leak trading and ~85% above September 2020 earnings-crash lows.",
        "Deal was largest pure software acquisition since IBM bought Red Hat in 2018; Slack had direct-listed in 2020 rather than traditional IPO underwriting.",
        "Packy McCormick published a bullish Not Boring Slack piece two weeks before the deal, cc'ing Marc Benioff — referenced on Salesforce earnings call announcement day.",
        "Microsoft Teams bundled with Office 365 reached far larger reported seat counts than Slack paid workspaces — Packy argues Teams competes more with Zoom on video than Slack on async chat.",
        "Zoom's public market capitalization reached roughly $130 billion around deal time — making an all-stock Slack merger a disproportionate bite versus Salesforce's financed $27.7B offer.",
    ],
    mental_model={
        "name": "Distribution Beats Product in Enterprise",
        "components": (
            "Slack won product love and DPO narrative as best-of-breed; Microsoft won default deployment via "
            "O365 bundling and IT procurement. Teams marketed against Slack while addressing video/meetings "
            "competition vs. Zoom. Salesforce offers enterprise sales force to Slack; risk is Quip/Heroku "
            "atrophy. Public SaaS multiples and growth deceleration forced sale above DPO price but below "
            "bull-case standalone upside."
        ),
        "application": (
            "Category creators need GTM moats when hyperscaler bundles are free. Emergency M&A favors prepared "
            "analysts with live thesis. Compare product-led Slack vs. distribution-led Salesforce before synergy "
            "credit. Packy's pre-deal bull case and Benioff earnings-call callback show narrative shaping price. "
            "Grade C- public tenure: above DPO for bulls, below SaaS multiple potential. A+ requires Salesforce "
            "channel pumping revenue without Quip-style atrophy."
        ),
    },
    competitive_advantage=(
        "Slack's moat was developer-loved UX, integrations, and bottom-up adoption — pioneering enterprise "
        "chat as async collaboration. NPS and workflow embedding created switching costs among tech-forward "
        "teams; DPO preserved independence narrative versus traditional IPO underwriting.\n\n"
        "Salesforce adds CRM-adjacent distribution to Fortune 500 procurement — potentially unlocking seats "
        "Slack's direct sales could not reach. Deal keeps Slack independent (LinkedIn-structure) preserving "
        "brand separation; Stewart Butterfield stays CEO post-close.\n\n"
        "Packy's pre-deal bull case documented top-quartile SaaS metrics across Bessemer indices — product "
        "quality was not the failure mode; distribution was. Emergency pod two hours post-announcement "
        "captured live market confusion before S-4 filings reveal bidding history.\n\n"
        "Weaknesses: Microsoft Teams bundling eroded net-new seat growth; Slack required org-wide paid "
        "conversion unlike Zoom's individual upgrade path. Salesforce history (Quip vs. Notion, Heroku vs. "
        "raw AWS) warns of innovation stall. $27.7B price limits ROI unless channel re-accelerates revenue.\n\n"
        "Deal context: Salesforce lost LinkedIn to Microsoft years earlier; Google absent from bidding per "
        "public reports. 55% premium vs. leak, 85% vs. September low — yet Packy and hosts note price below "
        "bull-case standalone SaaS multiples. Stewart stays CEO; Slack independent like LinkedIn structure. "
        "Emergency pod recorded on YouTube Live two hours post-announcement — meta commentary on real-time M&A."
    ),
    key_insights=[
        {
            "view": "Microsoft competes on bundle, not chat UX.",
            "question": "Why did Teams beat Slack in seats?",
            "answer": "O365 enterprises got Teams bundled 'free'; internal accounts inflated growth metrics per Packy. Teams targets Zoom meetings more than Slack async — yet Microsoft markets vs. Slack strategically. Slack required org-wide paid conversion; Zoom and parents got individual paid accounts post-COVID.",
        },
        {
            "view": "Slack's public markets story failed.",
            "question": "How do hosts grade the DPO era?",
            "answer": "C- tenure: stock below hype though above first-trade DPO for Packy; growth deceleration and UI backlash signaled market lost confidence in standalone upside — forcing strategic sale at 55% premium that still disappointed bulls expecting SaaS-multiple expansion.",
        },
        {
            "view": "Zoom merger was plausible but impractical.",
            "question": "Why didn't Zoom buy Slack?",
            "answer": "Zoom's ~$130B market cap made stock deal a huge bite; Slack may have distrusted rich Zoom currency. Eric Yuan focus on video-platform-for-economy vs. distraction; org dev capacity limited vs. Salesforce's M&A machine.",
        },
        {
            "view": "Salesforce bets on anti-Microsoft alliance.",
            "question": "What is the A+ scenario?",
            "answer": "Salesforce becomes distribution channel for best-of-breed stack (Superhuman, Notion, Coda) with Slack as collaboration hub — catalyzing ecosystem without acquiring each player. Benioff positions against bundled mediocrity.",
        },
        {
            "view": "Integration risk is real.",
            "question": "What is the F scenario?",
            "answer": "Quip/Heroku pattern repeats: founders leave, UI stagnates, startups migrate to Discord/async alternatives; Salesforce CRM stench (overstated?) slows innovative seat growth — $28B buys revenue deceleration not category expansion.",
        },
    ],
    top_investment_implications=[
        {
            "ticker": "CRM",
            "direction": "Watch",
            "confidence": "Medium",
            "thesis": "Largest software deal since Red Hat tests Salesforce's ability to revive Slack growth via CRM channel; integration execution drives whether $27.7B beats internal ROI hurdles.",
        },
        {
            "ticker": "MSFT",
            "direction": "Watch",
            "confidence": "Low",
            "thesis": "Teams bundling forced Slack sale — evidence of hyperscaler distribution power; watch antitrust and Teams monetization vs. Zoom in video.",
        },
        {
            "ticker": "ZM",
            "direction": "Watch",
            "confidence": "Low",
            "thesis": "Zoom's ~$130B market cap made stock merger impractical — missed combination of async chat plus video platform for enterprise.",
        },
    ],
    golden_quotes=[
        "\"We Don't Sell Saddles Here\" — Stewart Butterfield blog post defining Slack's category-creation GTM (referenced by hosts).",
        "\"This is the anti-Microsoft consolidation\" — Ben's thesis on Salesforce-Slack versus Teams bundling.",
        "\"Slack has basically stopped updating the product\" — Ben's pre-deal Twitter draft joke on fit with Salesforce UI cadence.",
    ],
    chronology={
        "subject": "Slack / Salesforce acquisition",
        "events": [
            {"date": "2013–14", "event": "Slack emerges from Glitch game studio pivot"},
            {"date": "2019", "event": "Slack direct public listing"},
            {"date": "2020-09", "event": "Slack stock crashes post-earnings weak guidance"},
            {"date": "2020-11", "event": "Packy publishes bullish Not Boring piece; cc Marc Benioff"},
            {"date": "2020-12", "event": "Deal leaks; Salesforce announces $27.7B acquisition"},
            {"date": "2020-12", "event": "Acquired emergency pod with Packy hours after news"},
            {"date": "Deal terms", "event": "$45.86/share; ~55% premium; Slack to stay independent"},
            {"date": "Context", "event": "Largest pure software M&A since IBM-Red Hat 2018"},
            {"date": "Prior bid", "event": "Salesforce lost LinkedIn to Microsoft years earlier"},
            {"date": "Pending", "event": "Shareholder approval expected following year"},
        ],
    },
)

EPISODES["acq-virgin-galactic"] = base(
    "acq-virgin-galactic",
    review_notes=NOTES,
    episode_rating={"overall": 4},
    keywords=["Space Tourism", "XPRIZE", "SPAC Financing"],
    conclusion=(
        "Virgin Galactic's story spans Peter Diamandis's 1996 $10M XPRIZE (won 2004 by Burt Rutan's "
        "SpaceShipOne after Paul Allen's ~$20M secret funding) to Richard Branson's 2004 \"screw it, let's "
        "do it\" acquisition the night before the prize flight. Tickets started at $200,000; ~600 paid full "
        "price plus deposits on \"One Small Step.\" Sixteen years and $1B+ R&D later, suborbital tourism still "
        "awaits routine passenger flights — Branson SPAC'd the company in 2019 with Chamath (VG Acquisition "
        "Corp). Bull case: 1.8M humans with $10M+ net worth × 10% uptake × $250K ≈ $50B lifetime revenue "
        "potential; bear case: SpaceX reached orbit routinely while Virgin delayed through 2020 COVID and "
        "15th postponement culture. Feather reentry and White Knight mothership design remain ingenious; "
        "capitalization and market-existence risk do not — ASCEND 2020 live episode compares SpaceX orbital "
        "cadence to 16 years of Virgin schedule slips and November 2020 COVID test delay."
    ),
    background=(
        "Recorded live at ASCEND 2020, Ben and David trace prizes from 1919 Orteig ($25K → $400K R&D leverage) "
        "to Diamandis's $10M Ansari XPRIZE. Burt Rutan's feathered SpaceShipOne — dropped from White Knight at "
        "50,000 feet — won October 2004 after Paul Allen's ~$20M secret funding. Branson bought rights the "
        "eve of victory; tickets at $200K with ~600 full-price buyers.\n\n"
        "Accidents (2007 ground test, 2014 in-flight) and endless \"18 months\" promises followed. George "
        "Whitesides vertical integration and Spaceport America ($200M facility) professionalized ops. Chamath "
        "SPAC went public 2019; November 2020 test delayed for COVID. SpaceX comparison anchors bear case — "
        "orbital revenue vs. tourism TAM that did not exist at founding."
    ),
    important_facts=[
        "Ansari XPRIZE offered $10 million for reusable crewed spacecraft reaching 100 kilometers twice in two weeks — SpaceShipOne won in October 2004 after Paul Allen secretly funded roughly $20 million of development.",
        "Virgin Galactic sold suborbital tickets initially at $200,000 each; approximately 600 customers paid full price with additional One Small Step deposits before new sales paused.",
        "New Mexico financed a $200 million Spaceport America facility; Virgin Galactic pays about $5 million annual rent — roughly 40 years to recoup construction costs at that rate alone.",
        "Chamath Palihapitiya's 2019 SPAC merged Virgin Galactic public at roughly $2.3 billion first-day market cap versus approximately $1 billion cumulative capital invested in the program.",
        "Hosts model 1.8 million humans with $10 million-plus net worth; 10% uptake at $250,000 per ticket implies nearly $50 billion lifetime revenue potential if flight cadence scales.",
    ],
    mental_model={
        "name": "Prize-Seeded Tourism vs. Existing Launch Markets",
        "components": (
            "XPRIZE leveraged $10M into ~$400K+ competitor R&D spend — catalyzing SpaceShipOne. Virgin bet on "
            "non-existent space tourism TAM; SpaceX served government/commercial launch demand with revenue "
            "financing. Feather reentry reduces heat load; air-launch from mothership avoids vertical rocket "
            "complexity. Preorders fund marketing but restrict cash; SPACs provide lump-sum public capital for "
            "long-duration R&D."
        ),
        "application": (
            "Match financing to market existence — prizes bootstrap prototypes; launch revenue funds SpaceX iteration. "
            "Tourism TAM surveys need execution proof before DCF. Compare capital raised and flight cadence picking "
            "space exposure. SPAC suits high-beta pre-revenue capex; Chamath negotiated price avoids IPO roadshow "
            "delay. Government spaceport subsidies (New Mexico $200M) show public-private win-win when aligned on "
            "ecosystem jobs — playbook item hosts applaud."
        ),
    },
    competitive_advantage=(
        "Virgin Galactic's edge is first-mover suborbital tourism brand (Branson showmanship), unique feather "
        "reentry IP from Burt Rutan, and preorder backlog proving willingness to pay $200K–$250K for "
        "90-minute experiences with minutes of weightlessness and astronaut wings.\n\n"
        "Spaceport America subsidy ($200M facility, ~$5M annual rent) lowered facility capex burden. "
        "Whitesides vertical integration aligned airline and manufacturing — Apple-like control of core tech. "
        "White Knight air-launch avoids vertical rocket pad complexity for suborbital hops.\n\n"
        "SPAC financing via Chamath delivered negotiated public capital without roadshow — suited to "
        "high-beta option on tourism TAM. Point-to-point suborbital travel (Abu Dhabi ↔ New Mexico) remains "
        "upside if cadence reaches hundreds of flights yearly.\n\n"
        "Weaknesses: 16 years without commercial passenger service; 2007 ground and 2014 in-flight fatalities; "
        "endless schedule slips (November 2020 COVID delay). SpaceX captured orbital economics with 10X+ "
        "funding; 600 full-price buyers may exhaust early adopters. SPAC diluted retail (~50% to insiders).\n\n"
        "Execution timeline haunts bull case: Branson predictions from 2008 (18 months) repeated through 2020; "
        "2014 fatal test; feather design unchanged 16 years while SpaceX iterated Falcon 1→9→Heavy→Starship "
        "with government launch revenue. NASA tourist-training contracts diversify slightly but hardware remains "
        "suborbital. Branson launched VG Acquisition Corp SPAC October 2020 — full circle from SPAC target to "
        "SPAC sponsor."
    ),
    key_insights=[
        {
            "view": "Prizes multiply R&D dollars.",
            "question": "Why did XPRIZE work?",
            "answer": "$10M Ansari purse attracted ~$400K+ aggregate competitor spend — 40:1 leverage like 1919 Orteig. Catalyzed SpaceShipOne but not ongoing ops; Branson still needed $100M+ and later SPAC capital.",
        },
        {
            "view": "Branson bought the night before victory.",
            "question": "When did Virgin enter?",
            "answer": "Richard Branson twice declined funding XPRIZE; after Paul Allen's ~$20M secret backing succeeded, Branson bought IP the eve of winning flight — 'second best time is today' vs. Diamandis's earlier outreach when funding was not secured.",
        },
        {
            "view": "SpaceX served an existing market.",
            "question": "Why divergent outcomes vs. SpaceX?",
            "answer": "SpaceX ladder-climbed Falcon 1→9 with government/commercial launch revenue; Virgin targeted tourism TAM that did not exist yet. Orders-of-magnitude capitalization difference and market proof separated orbital cadence from suborbital delays.",
        },
        {
            "view": "SPAC fits long-horizon capex.",
            "question": "Why go public via Chamath?",
            "answer": "SPAC delivers negotiated lump-sum without roadshow — suited to high-beta, pre-revenue space bets. First-day ~$2.3B cap vs. ~$1B invested framed as 2X R&D option; dilution to sponsor/shareholders still material.",
        },
        {
            "view": "TAM bottom-up is seductive but unproven.",
            "question": "How big can tourism get?",
            "answer": "Hosts model 1.8M people with $10M+ net worth; 10% buying $250K tickets ≈ $50B lifetime revenue. Requires flight cadence (goal 1,000 passengers/year), safety record, and price persistence — none proven at scale by 2020 recording.",
        },
    ],
    top_investment_implications=[
        {
            "ticker": "SPCE",
            "direction": "Watch",
            "confidence": "Low",
            "thesis": "High-beta call on suborbital tourism execution; November 2020 test delay and 16-year slip history keep bear case alive despite preorder backlog.",
        },
        {
            "ticker": "SPACE",
            "direction": "Watch",
            "confidence": "Low",
            "thesis": "Private SpaceX not investable here — episode uses as execution benchmark; orbital launch revenue vs. Virgin tourism TAM contrast.",
        },
    ],
    golden_quotes=[
        "\"Screw it, let's do it\" — Sir Richard Branson's line when buying SpaceShipOne IP (quoted by hosts).",
        "\"Space is hard\" — George Whitesides refrain after 2014 fatal test and schedule slips.",
        "\"The first 90% all you have left is the second 90%\" — software aphorism applied to SpaceShipTwo commercialization.",
    ],
    chronology={
        "subject": "Virgin Galactic",
        "events": [
            {"date": "1996", "event": "Peter Diamandis proposes $10M XPRIZE for private reusable spaceflight"},
            {"date": "2001–03", "event": "Burt Rutan builds SpaceShipOne; Paul Allen funds ~$20M secretly"},
            {"date": "2004-10", "event": "SpaceShipOne wins XPRIZE with two flights in two weeks"},
            {"date": "2004", "event": "Branson announces Virgin Galactic; tickets at $200,000"},
            {"date": "2007", "event": "Ground test explosion kills three Scaled Composites workers"},
            {"date": "2010–11", "event": "Branson repeatedly predicts flights in 18 months"},
            {"date": "2014", "event": "SpaceShipTwo fatal in-flight accident"},
            {"date": "2010s", "event": "George Whitesides CEO; Spaceport America $200M facility"},
            {"date": "2019", "event": "Chamath SPAC takes Virgin Galactic public"},
            {"date": "2020-11", "event": "Test flight delayed for COVID; ASCEND episode recorded"},
        ],
    },
)

EPISODES["acq-superhuman"] = base(
    "acq-superhuman",
    review_notes=NOTES,
    episode_rating={"overall": 4},
    keywords=["Product-Market Fit", "Premium SaaS", "Sean Ellis Survey"],
    conclusion=(
        "This Acquired LP episode visits Superhuman HQ with CEO Rahul Vohra (Rapportive sold to LinkedIn 2012) "
        "on PMF science, not game design. Superhuman spent ~2½ years pre-launch (Feb 2015–summer 2017): a year "
        "sketching, a year designing, 14-person team before ship — heresy versus MVP dogma but rational when "
        "competing with Gmail and Outlook in an established market. Pricing locked at $30/month from Crossing "
        "the Chasm early-adopter framing; waitlist grew to 180,000 with weekly admission throttles. Rahul's "
        "Sean Ellis-inspired survey: users who'd be \"very disappointed\" without the product define PMF; four-step "
        "loop segments lovers, builds for them, surveys ~40% disappointment threshold, then grows. Second-time-founder "
        "discipline let the team ignore premature-launch pressure — relevant as Airbnb, DoorDash, and Slack IPO "
        "season framed the conversation."
    ),
    background=(
        "Ben and David record at Superhuman's California Street office with Rahul and team present. Rapportive "
        "Gmail plugin history (LinkedIn acquisition) explains Rahul's email-domain obsession and why plugins "
        "cannot build enduring companies on Gmail/Microsoft rails.\n\n"
        "Deep dive covers intentional slow launch vs. land-grab markets (Uber iOS moment), Tesla-not-EV1 "
        "positioning, merged local/server search, contrarian design-agency hire, and algorithmic PMF measurement "
        "from First Round Review essay. LP audience gets hiring pitch; hosts tease covering Superhuman IPO on "
        "main show — still private at recording."
    ),
    important_facts=[
        "Superhuman charged $30 per month from launch — a premium email client backed by Gmail, validated via Crossing the Chasm early-adopter pricing.",
        "Rahul Vohra sold Rapportive to LinkedIn in 2012 before founding Superhuman in 2014.",
        "First line of code ~February 2015; summer 2017 (~2½ years later) 14-person team still pre-general launch with intentional slow rollout.",
        "Waitlist reached roughly 180,000 prospective users; Superhuman admits a controlled number weekly to manage onboarding quality.",
        "PMF benchmark: Sean Ellis survey — target ~40% of users \"very disappointed\" if product disappeared before scaling growth.",
    ],
    mental_model={
        "name": "Measured PMF for Premium Markets",
        "components": (
            "In existing high-bar markets (email), slow craftsmanship beats embarrassing MVP — land-grab rules "
            "apply only when timing demands speed. Price signals early-adopter positioning ($30/mo). PMF loop: "
            "(1) find users who love you, (2) build for them, (3) measure very-disappointed %, (4) grow when "
            "~40% threshold hits. Waitlist throttle converts scarcity into onboarding quality. Second-time "
            "founders can ignore investor launch pressure."
        ),
        "application": (
            "Segment users who love product before broadening — avoid averaging feedback across lukewarm trials. "
            "Use disappointment survey as transmission metric; passion is engine, process is gearbox. When "
            "platform risk (Gmail) looms, own native experience even via Electron. Premium pricing filters "
            "serious users and funds artisanal product cycles."
        ),
    },
    competitive_advantage=(
        "Superhuman's moat is speed (merged local/server search), keyboard-first UX, and onboarding concierge "
        "— flow state Gmail/Outlook rarely match. $30/month selects professionals spending 3+ hours daily in "
        "email; willingness to pay funds small-team craftsmanship.\n\n"
        "Rahul's Rapportive pedigree and PMF methodology credibility attract founder-customers and press — "
        "distribution via reputation and waitlist hype without gamified badges.\n\n"
        "Weaknesses: Gmail platform dependency; $30 limits TAM; 2½-year stealth invites fast-follow clones; "
        "email category faces Slack/async erosion. Electron performance ceiling; Microsoft/Google can absorb "
        "features. Waitlist frustration (David disqualified as iPad-primary) risks brand heat."
    ),
    key_insights=[
        {
            "view": "MVP timing depends on market structure.",
            "question": "When is slow launch rational?",
            "answer": "Land-grab markets (post-iOS Uber moment) demand speed; entrenched high-quality incumbents (Gmail, Outlook) reward Tesla-style multi-year craft. Rahul shipped after 2½ years with 14 engineers — Reid Hoffman embarrassment rule rejected deliberately.",
        },
        {
            "view": "PMF is measurable, not mystical.",
            "question": "What is the four-step loop?",
            "answer": "Find users who love product; build only for them; run Sean Ellis 'very disappointed' survey; grow when ~40% threshold clears. Product changes guided by lover feedback — First Round Review essay codifies the algorithm.",
        },
        {
            "view": "Premium price is positioning.",
            "question": "Why $30/month?",
            "answer": "Crossing the Chasm early-adopter framing — price signals quality and filters serious professionals. Rahul unchanged pricing since launch; compares to iPhone plan psychology ($12.99 carrier tiers).",
        },
        {
            "view": "Waitlist is a control knob.",
            "question": "How manage 180,000 waitlist?",
            "answer": "Weekly admission quotas balance onboarding capacity with hype — deliberate scarcity vs. land-grab free tiers. Referral governors prevent uncontrolled floods; concierge onboarding preserves NPS.",
        },
        {
            "view": "Plugins cannot become platforms.",
            "question": "Why leave Rapportive for native app?",
            "answer": "Rapportive peaked as Gmail plugin sold to LinkedIn; Rahul cites rule — few huge companies built solely on another platform's rails. Superhuman needs owned client experience despite Gmail data dependency.",
        },
    ],
    top_investment_implications=[
        {
            "ticker": "GOOGL",
            "direction": "Watch",
            "confidence": "Low",
            "thesis": "Gmail incumbent Superhuman displaces among power users; Google's UX bar and workspace bundling determine whether premium email niche sustains.",
        },
    ],
    golden_quotes=[
        "\"If you're not embarrassed by the first version, you've launched too late\" — Reid Hoffman quote Rahul explicitly rejects for Superhuman's market.",
        "\"Very disappointed\" — Sean Ellis PMF survey threshold Rahul adopted as scaling gate.",
        "\"You can't build a big company on the back of somebody else's platform\" — David on Rapportive/Gmail plugin limits.",
    ],
    chronology={
        "subject": "Rahul Vohra / Superhuman",
        "events": [
            {"date": "2000s", "event": "Rahul builds games and Rapportive Gmail social graph plugin"},
            {"date": "2012", "event": "LinkedIn acquires Rapportive"},
            {"date": "2014", "event": "Rahul founds Superhuman"},
            {"date": "Feb 2015", "event": "First line of code; year of sketching begins"},
            {"date": "2016", "event": "Design phase; ~14-person team forms"},
            {"date": "Summer 2017", "event": "Still pre-launch; controlled user admissions"},
            {"date": "2018+", "event": "$30/month pricing; waitlist grows toward 180,000"},
            {"date": "2019", "event": "First Acquired main-show PMF episode (Season 5 finale)"},
            {"date": "2020", "event": "LP episode recorded at Superhuman HQ"},
            {"date": "Ongoing", "event": "PMF survey methodology published on First Round Review"},
        ],
    },
)
