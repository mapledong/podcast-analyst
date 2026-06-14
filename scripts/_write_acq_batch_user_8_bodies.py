"""Episode bodies for _write_acq_batch_user_8.py (6 episodes)."""

from __future__ import annotations

from scripts._write_acq_batch_491_500_common import base

NOTES = "Manual GPT Acquired batch v5.1 — user request 8 episodes"

EPISODES: dict[str, dict] = {}

EPISODES["acq-season-4-episode-4-the-lyft-ipo"] = base(
    "acq-season-4-episode-4-the-lyft-ipo",
    review_notes=NOTES,
    episode_rating={"overall": 4},
    keywords=["Lyft IPO", "Ride-Hail Economics", "Dual-Class Shares"],
    conclusion=(
        "Ben and David dissect Lyft's March 2019 IPO — the first major ride-hail listing in a duopoly "
        "against Uber, priced at $72/share for a ~$24B valuation after raising billions privately. "
        "The episode walks through S-1 economics: massive losses, driver subsidies, insurance complexity, "
        "and whether network effects justify public-market faith. Dual-class super-voting shares preserve "
        "founder control while public shareholders fund growth — a governance pattern Acquired compares "
        "across tech IPOs. Lyft's pink brand, U.S. focus, and \"better actor\" narrative contrast Uber's "
        "global scale; neither unit economics nor autonomous timelines were proven at listing. Grade: "
        "landmark IPO event study for platform businesses burning cash to win categories."
    ),
    background=(
        "Recorded around Lyft's March 2019 public debut, Acquired applies its IPO playbook to the "
        "ride-hail wars. David traces Lyft's 2012 launch (Zimride roots, John Zimmer and Logan Green) "
        "versus Uber's 2009 head start, regulatory battles, and the duopoly consolidation after Sidecar "
        "and others exited.\n\n"
        "They parse the S-1: revenue growth, take rates, sales & marketing intensity, stock-based comp, "
        "and path-to-profitability skepticism. Autonomous-vehicle partnerships (GM, Aptiv) appear as "
        "optionality, not near-term P&L relief. Governance section covers dual-class structure and "
        "lockups. Hosts compare Lyft's narrower U.S./Canada footprint to Uber Eats and international "
        "complexity — framing 2019 as peak \"growth IPO\" era before WeWork and COVID repriced risk."
    ),
    important_facts=[
        "Lyft went public in March 2019 at $72 per share, targeting roughly a $24 billion valuation — among the largest tech IPOs of the cycle.",
        "Lyft and Uber together dominated U.S. ride-hail after years of subsidy wars; Lyft positioned as the #2 player with a friendlier brand versus Uber's global scale.",
        "Lyft's S-1 disclosed substantial net losses and heavy sales-and-marketing spend — typical of growth-stage marketplaces prioritizing share over profit.",
        "Dual-class super-voting shares gave founders outsized control post-IPO — a recurring Acquired theme in 2019 tech listings.",
        "Lyft IPO preceded Uber's May 2019 IPO — the ride-hail duopoly back-to-back tested public investor appetite for unprofitable platforms.",
    ],
    mental_model={
        "name": "IPO as Strategic Fundraising, Not Exit",
        "components": (
            "For category duopolists, IPO supplies capital to fund subsidies, insurance, R&D, and "
            "autonomous bets while private multiples compress. S-1 narrative sells TAM, network effects, "
            "and future autonomy — not current FCF. Dual-class preserves founder strategy against "
            "activists. Public shareholders bet on winner-take-most dynamics; bears cite perpetual "
            "losses and driver classification risk."
        ),
        "application": (
            "When analyzing marketplace IPOs, separate GMV growth from contribution margin after "
            "incentives. Ask whether duopoly stability reduces burn or prolongs price wars. Governance "
            "matters: super-voting delays accountability if unit economics never inflect."
        ),
    },
    competitive_advantage=(
        "Lyft's moat at IPO was duopoly position in core U.S. cities, brand differentiation (pink, "
        "community focus), and rider/driver liquidity in a two-player market. Smaller geographic scope "
        "vs. Uber reduced complexity but capped TAM story. Partnerships with GM on autonomy provided "
        "strategic narrative without proven COGS savings.\n\n"
        "First-mover IPO among pure-play ride-hail gave media and investor attention — \"Lyft vs Uber\" "
        "binary simplified the trade. Founder story (Zimride, sustainability) appealed to ESG-leaning "
        "2019 allocators.\n\n"
        "Weaknesses: no profitability, driver incentives as recurring cost, regulatory reclassification "
        "risk (employees vs contractors), and autonomous timelines uncertain. Uber's broader platform "
        "(Eats, freight, international) could out-scale Lyft if U.S. ride-hail commoditized."
    ),
    key_insights=[
        {
            "view": "Ride-hail IPOs test belief in eventual monopoly profits.",
            "question": "Why go public while deeply unprofitable?",
            "answer": "Duopoly players need public currency for M&A, employee retention, and continued subsidies; private markets at $15B+ still want liquidity events — IPO funds the war even if profits remain elusive.",
        },
        {
            "view": "Lyft's narrower footprint is feature and bug.",
            "question": "How does Lyft differ from Uber in the S-1 story?",
            "answer": "U.S./Canada focus simplifies ops and brand ('better actor') but limits TAM versus Uber's global multi-product stack — investors choose purity vs. optionality.",
        },
        {
            "view": "Dual-class is founder insurance on unproven models.",
            "question": "Why super-voting shares?",
            "answer": "Founders argue long-term autonomy bets (autonomy, pricing) require protection from quarterly pressure — Acquired notes tradeoff with public shareholder influence.",
        },
        {
            "view": "Autonomy is narrative hedge, not near-term margin.",
            "question": "Do self-driving partnerships fix economics?",
            "answer": "GM/Aptiv deals provide R&D narrative; hosts treat driver cost removal as uncertain timeline — S-1 economics still assume human drivers for years.",
        },
        {
            "view": "2019 IPO window was peak growth optimism.",
            "question": "How should we grade the IPO?",
            "answer": "As a case study in pricing duopoly dreams — success depends on post-IPO discipline and category rationalization, not day-one pop.",
        },
    ],
    top_investment_implications=[
        {
            "ticker": "LYFT",
            "direction": "Watch",
            "confidence": "Medium",
            "thesis": "Episode frames Lyft as duopoly #2 with governance and loss-making structure intact at IPO — useful baseline for judging later profitability targets and autonomous partnerships.",
        },
        {
            "ticker": "UBER",
            "direction": "Watch",
            "confidence": "Medium",
            "thesis": "Uber listed weeks later with broader platform story; Acquired contrasts scale vs. focus — pair trade on ride-hail rationalization and regulatory outcomes.",
        },
    ],
    golden_quotes=[
        "\"The ride-hail duopoly\" — hosts frame U.S. market consolidation after years of subsidy wars.",
        "\"Dual-class super-voting\" — recurring Acquired IPO theme preserving founder control at Lyft and peers.",
        "\"IPO as strategic fundraising, not exit\" — Ben/David on why unprofitable platforms still list.",
    ],
    chronology={
        "subject": "Lyft IPO & ride-hail industry",
        "events": [
            {"date": "2009", "event": "Uber founded; ride-hail category begins"},
            {"date": "2012", "event": "Lyft launches ride-sharing service (Zimride origins)"},
            {"date": "2010s", "event": "Subsidy wars; Sidecar and others exit; U.S. duopoly forms"},
            {"date": "2018", "event": "Lyft files confidential S-1; private valuation reaches ~$15B"},
            {"date": "2019-03", "event": "Lyft prices IPO at $72/share (~$24B valuation)"},
            {"date": "2019-03", "event": "Lyft begins trading on NASDAQ"},
            {"date": "2019-05", "event": "Uber follows with its IPO"},
            {"date": "2019", "event": "Acquired publishes Season 4 Lyft IPO episode"},
            {"date": "Ongoing", "event": "Autonomous-vehicle partnerships cited as long-term cost option"},
            {"date": "Ongoing", "event": "Driver classification legal battles continue nationally"},
        ],
    },
)

EPISODES["acq-season-3-episode-7-venmo-sf-live-show-with-andrew-kortina"] = base(
    "acq-season-3-episode-7-venmo-sf-live-show-with-andrew-kortina",
    review_notes=NOTES,
    episode_rating={"overall": 4},
    keywords=["Venmo", "Social Payments", "PayPal M&A"],
    conclusion=(
        "Recorded live in San Francisco with co-founder Andrew Kortina, Acquired tells Venmo's story from "
        "Ithaca College dorm experiment to PayPal-owned social payments default for millennials. Venmo "
        "won on frictionless P2P transfers and a public feed that turned transactions into culture — "
        "then navigated Braintree's 2012 acquisition and PayPal's 2013 $800M Braintree deal as a "
        "product inside a public-company machine. Kortina reflects on network effects among young users, "
        "regulatory constraints, and whether social graph beats ACH speed. The episode is a masterclass "
        "in category creation before \"fintech\" was a VC bucket — and in how acquirers preserve (or "
        "dilute) product soul post-close."
    ),
    background=(
        "Ben and David host a live SF audience Q&A with Andrew Kortina, Venmo co-founder (with Iqram "
        "Magdon-Ismail). They cover 2009 origins — musicians splitting payments, SMS-based proto-Venmo, "
        "and moving to Philadelphia/New York to build.\n\n"
        "Growth came through campus density and word-of-mouth: paying friends felt social, not "
        "financial. Braintree acquired Venmo in 2012 (~$26M reported) for payments infrastructure; "
        "PayPal bought Braintree in 2013 for $800M, bringing Venmo inside a much larger org. Kortina "
        "discusses feed design, fraud/risk scaling, monetization via Pay with Venmo, and competing "
        "against Square Cash and bank P2P. Live format adds founder anecdotes on product taste and "
        "post-acquisition autonomy."
    ),
    important_facts=[
        "Venmo was founded in 2009 by Andrew Kortina and Iqram Magdon-Ismail, initially targeting easy P2P payments among friends.",
        "Braintree acquired Venmo in 2012 for a reported ~$26 million, seeking a consumer brand atop its payments rails.",
        "PayPal acquired Braintree (including Venmo) in 2013 for approximately $800 million in cash.",
        "Venmo's social feed — public payment notes by default among friends — became a distinctive growth and engagement loop.",
        "Acquired recorded this episode as a live San Francisco show with Andrew Kortina (published October 29, 2018).",
    ],
    mental_model={
        "name": "Social Graph as Payment Network",
        "components": (
            "Venmo reframed P2P transfers as lightweight social acts — emoji notes, feeds, campus virality. "
            "Liquidity required density among trusted friend groups, not merchant acceptance. Braintree "
            "added compliance rails; PayPal added scale and risk systems. Monetization lagged engagement — "
            "classic consumer fintech: win behavior first, extract rent later via merchant/Pay with Venmo."
        ),
        "application": (
            "Consumer payment startups should optimize for habitual small-ticket use cases and visible "
            "social proof. Strategic acquirers buy engagement loops, not just licenses — but must "
            "protect product culture inside parent orgs or feed innovation dies."
        ),
    },
    competitive_advantage=(
        "Venmo's moat was youth mindshare and social habit — default verb \"venmo me\" on campuses. "
        "Feed created free marketing and FOMO; low friction beat clunky bank transfers pre-Zelle ubiquity. "
        "Braintree/PayPal added fraud, compliance, and merchant acceptance paths competitors lacked at "
        "similar brand warmth.\n\n"
        "First-mover in social P2P among millennials compounded through network effects in friend groups — "
        "multi-homing costly when your social graph lives on Venmo.\n\n"
        "Weaknesses: thin margins on free P2P; parent PayPal incentive to cross-sell PayPal brand; "
        "regulatory scrutiny on public feeds and privacy; Zelle and Apple Cash closed gap on speed and "
        "bank integration. Live-show format limits deep S-1-style numbers but highlights founder-led design "
        "advantage competitors couldn't copy quickly."
    ),
    key_insights=[
        {
            "view": "Venmo sold behavior, not payments plumbing.",
            "question": "Why did Braintree buy Venmo?",
            "answer": "Braintree had developer/API rails but no consumer love; Venmo supplied brand and social engagement atop infrastructure — classic business-line + technology pairing.",
        },
        {
            "view": "Social feed was growth engine and PR risk.",
            "question": "Was the public feed genius or liability?",
            "answer": "Kortina explains feed drove virality and cultural relevance; also invited privacy jokes and regulatory attention — tradeoff between growth and decorum.",
        },
        {
            "view": "Double acquisition preserved then scaled product.",
            "question": "Did PayPal kill Venmo's soul?",
            "answer": "Live discussion explores autonomy post-Braintree and PayPal — Venmo retained distinct brand while gaining fraud/compliance scale competitors lacked.",
        },
        {
            "view": "Campus density beats national TV ads.",
            "question": "How did Venmo grow cheaply?",
            "answer": "Friend-group liquidity on colleges spread organically; social proof mattered more than merchant acceptance in early years.",
        },
        {
            "view": "Monetization follows habit.",
            "question": "When does Venmo make money?",
            "answer": "Free P2P built habit; Pay with Venmo and merchant integrations monetize later — engagement-first fintech playbook.",
        },
    ],
    top_investment_implications=[
        {
            "ticker": "PYPL",
            "direction": "Watch",
            "confidence": "Medium",
            "thesis": "Venmo engagement under PayPal remains a millennial acquisition funnel; episode clarifies strategic logic of Braintree/Venmo rollup for consumer rails.",
        },
    ],
    golden_quotes=[
        "\"Venmo me\" — hosts on Venmo becoming a verb through campus social density.",
        "\"Social payments\" — Kortina on transactions as lightweight communication, not banking.",
        "\"Live from San Francisco\" — Acquired's first major live-audience format with a founder guest.",
    ],
    chronology={
        "subject": "Venmo & Andrew Kortina",
        "events": [
            {"date": "2009", "event": "Andrew Kortina and Iqram Magdon-Ismail found Venmo"},
            {"date": "2009–2011", "event": "Campus-led growth; social feed becomes core UX"},
            {"date": "2012", "event": "Braintree acquires Venmo (~$26M reported)"},
            {"date": "2013", "event": "PayPal acquires Braintree for ~$800M, including Venmo"},
            {"date": "2010s", "event": "Venmo scales inside PayPal; adds Pay with Venmo merchant features"},
            {"date": "2017+", "event": "Competition from Square Cash, Zelle, Apple Cash intensifies"},
            {"date": "2018-10-29", "event": "Acquired live SF episode with Andrew Kortina"},
            {"date": "Ongoing", "event": "Venmo processes tens of billions in annual payment volume"},
            {"date": "Ongoing", "event": "Regulators and users debate public feed privacy defaults"},
            {"date": "Ongoing", "event": "PayPal integrates Venmo brand across consumer stack"},
        ],
    },
)

EPISODES["acq-episode-9-writely-google-docs"] = base(
    "acq-episode-9-writely-google-docs",
    review_notes=NOTES,
    episode_rating={"overall": 3},
    keywords=["Google Docs", "Cloud Productivity", "Writely"],
    conclusion=(
        "Ben and David trace how Google assembled Docs, Sheets, and Slides through a string of ~$10M "
        "Ajax-era acquisitions — Writely (March 2006), 2Web, Tonic, Zenter — rather than one blockbuster "
        "deal. Writely's collaborative browser editing became Google Docs; the suite never displaced "
        "Microsoft's enterprise cash cow but established cloud collaboration norms. Hosts grade the effort "
        "C/B-: cheap and self-sustaining, yet a major focus distraction for an advertising company "
        "chasing a second leg Microsoft already defended with Office 365. Low-end disruption stalled — "
        "Google won usage, Microsoft won dollars."
    ),
    background=(
        "Season 1 Episode 9 rewinds to mid-2000s Web 2.0: Intuit alumni at Upstartle ship Writely, "
        "collaborative docs in the browser. Google buys Writely (~$10M rumored, March 2006) plus 2Web "
        "(Excel2Web), Tonic, and Zenter for presentations — full suite live by September 2007.\n\n"
        "Eric Schmidt publicly denied competing with Office; Kurt DelBene (later Microsoft) might have "
        "smiled. Ben and David apply Christensen: Google looked like a low-end disruptor but lacked "
        "Microsoft's existential focus — Larry Page's mindshare on ads/mobile vs Ballmer/Nadella on "
        "productivity. Dropbox/Box founded 2007 as Google Drive rumors swirled until 2012 launch. "
        "Bitglass data: Google Apps briefly led Office 365 share, then Microsoft cloud caught up."
    ),
    important_facts=[
        "Google acquired Writely (Upstartle) in March 2006 for an undisclosed amount rumored around $10 million.",
        "Writely founders Sam Schillace, Claudia Carpenter, and Steve Newman joined Google as PMs on Docs.",
        "Google acquired at least five small companies (Writely, 2Web, Tonic, Zenter, others) to assemble Docs, Sheets, and Slides by 2007.",
        "Google Drive did not launch until 2012 — years after the office suite, despite persistent \"G Drive\" rumors.",
        "By ~2016 Office 365 had overtaken Google Apps in cloud productivity market share (~25% vs ~23% per Bitglass cited on show).",
    ],
    mental_model={
        "name": "Buy-the-Prototype vs. Own-the-Castle",
        "components": (
            "Google bought Ajax experiments cheaply when cloud editing was a toy; Microsoft owned enterprise "
            "distribution and high-fidelity Word requirements. Low-end disruption needs a disruptor "
            "committed to climbing the feature ladder — Google treated productivity as optional second "
            "business while Microsoft treated it as core. Amazon later won cloud infra without owning "
            "email/docs — alternative path Google could have taken earlier."
        ),
        "application": (
            "Before copying a rival's product map, ask if your incentives match. Founders: incumbents "
            "with 90% executive focus beat diversifiers with 10%. Investors: separate user adoption from "
            "revenue capture in freemium suites."
        ),
    },
    competitive_advantage=(
        "Google's edge was free web collaboration, speed of iteration, and upsell into Google Workspace "
        "for SMBs. Real-time multi-cursor editing felt magical vs desktop Word. Acquisitions imported "
        "founder talent (Schillace et al.) faster than greenfield R&D.\n\n"
        "Search/ad cash subsidized free tiers — Microsoft couldn't match price, only bundle with "
        "enterprise agreements. Gmail integration gave distribution.\n\n"
        "Weaknesses: legal-grade Word fidelity still drives enterprise; Google lacked sales muscle vs "
        "Microsoft field org. Focus dilution — moonshots and Android vs Office war. YouTube and other "
        "bets consumed capital; Docs became profitable but sub-Google-scale. Dropbox/Box proved storage "
        "layer could have been partnered/acquired instead."
    ),
    key_insights=[
        {
            "view": "String-of-pearls beat one big buy.",
            "question": "Why five small acquisitions?",
            "answer": "Each component (docs, sheets, slides) was an immature Ajax startup; ~$10M each bought teams and prototypes faster than internal build — classic Google 2000s playbook.",
        },
        {
            "view": "Low-end disruption failed to unseat Office revenue.",
            "question": "Did Google Docs disrupt Microsoft?",
            "answer": "Usage grew (especially greenfield docs) but enterprise dollars stayed with Microsoft once Office 365 matched collaboration; Google fought an advertising company's war, not a productivity company's.",
        },
        {
            "view": "Focus is the scarcest resource.",
            "question": "Why grade C/B-?",
            "answer": "Financially cheap and self-sustaining, but opportunity cost enormous — same era Google could have doubled down on AWS-competitive cloud infra per hosts' counterfactual.",
        },
        {
            "view": "Storage was the missing piece.",
            "question": "Where was Google Drive?",
            "answer": "Suite launched 2007; Drive until 2012 — Dropbox/Box filled the gap; hosts speculate alternate history if Google acquired storage startups early.",
        },
        {
            "view": "Incentives determine defense intensity.",
            "question": "Why did Microsoft win the cloud productivity battle?",
            "answer": "Ballmer/Nadella 90% focus vs Larry Page ~10%; Microsoft had existential need to protect Office cash cow — Google did not need Docs to survive.",
        },
    ],
    top_investment_implications=[
        {
            "ticker": "GOOGL",
            "direction": "Watch",
            "confidence": "Medium",
            "thesis": "Episode frames Workspace as profitable but non-core vs ads — relevant when judging Google Cloud cross-sell and whether productivity still drives enterprise GCP deals.",
        },
        {
            "ticker": "MSFT",
            "direction": "Watch",
            "confidence": "Medium",
            "thesis": "Office 365 resurgence after dismissing Google threat validates incumbent focus; Azure linkage matters more than Docs user counts.",
        },
    ],
    golden_quotes=[
        "\"Google is an advertising company\" — Ben on misaligned incentives vs Microsoft productivity focus.",
        "\"Focus, focus, focus\" — David on the scarcest startup/big-co resource wasted on second-leg bets.",
        "\"The wrong battleground\" — hosts on fighting feature parity instead of cloud/platform economics.",
    ],
    chronology={
        "subject": "Google Docs / Writely acquisitions",
        "events": [
            {"date": "2005", "event": "Google acquires 2Web Technologies (Excel2Web)"},
            {"date": "2006-03", "event": "Google acquires Writely (~$10M rumored)"},
            {"date": "2006-06", "event": "Google Spreadsheets launches in Labs"},
            {"date": "2007", "event": "Google acquires Tonic Systems and Zenter for presentations"},
            {"date": "2007-09", "event": "Google Docs & Spreadsheets suite goes public"},
            {"date": "2007", "event": "Dropbox founded; G Drive rumors begin"},
            {"date": "2012", "event": "Google Drive finally launches"},
            {"date": "2016", "event": "Acquired publishes Writely / Google Docs episode (Episode 9)"},
            {"date": "2010s", "event": "Office 365 overtakes Google Apps enterprise share"},
            {"date": "Ongoing", "event": "Real-time collaboration becomes table stakes in productivity software"},
        ],
    },
)

EPISODES["acq-episode-8-acompli-sunrise-and-wunderlist"] = base(
    "acq-episode-8-acompli-sunrise-and-wunderlist",
    review_notes=NOTES,
    episode_rating={"overall": 4},
    keywords=["Microsoft Mobile", "Outlook", "Buy vs Build"],
    conclusion=(
        "Microsoft VP Kurt DelBene joins Acquired to dissect three mobile productivity acquisitions — "
        "Acompli, Sunrise, and Wunderlist — totaling roughly half a billion dollars that rebuilt Outlook "
        "mobile for iOS and Android. Javier Soltero (Acompli CEO) now runs Outlook; Sunrise calendar and "
        "Wunderlist tasks folded into Microsoft's cross-platform strategy under Satya Nadella's "
        "mobile-first, cloud-first era. DelBene contrasts Google's string-of-cheap-bets approach (prior "
        "episode) with Microsoft's premium talent buys when time-to-market and Apple platform presence "
        "were existential. Culture fit and founder retention drive outcomes — themes Taylor Barada later "
        "echoes at Adobe. Grade: strategic people-and-product acquisitions that let Microsoft compete on "
        "phones it didn't own."
    ),
    background=(
        "Episode 8 follows Episode 9's Google Docs story with the Microsoft counter-narrative. Kurt "
        "DelBene — former Microsoft Office president, Healthcare.gov fixer, returnee under Nadella — "
        "explains why Redmond bought email client Acompli (~$200M, 2014), calendar Sunrise (~$100M, "
        "2015), and tasks Wunderlist (~$100–150M, 2015) instead of rebuilding Outlook mobile internally.\n\n"
        "Acompli shipped a beloved iOS Gmail alternative with innovative UX; acquisition brought Javier "
        "Soltero to lead mobile Outlook. Sunrise had design cult following; Wunderlist was category leader "
        "in task apps. DelBene covers buy-vs-build calculus, integration timelines, and competing with "
        "Google's free apps while selling Office 365 bundles. Sets up his later LinkedIn acquisition role."
    ),
    important_facts=[
        "Microsoft acquired Acompli in 2014 for a reported ~$200 million; founder Javier Soltero later led Outlook mobile and broader Outlook efforts.",
        "Microsoft acquired Sunrise Calendar in 2015 for a reported ~$100 million.",
        "Microsoft acquired Wunderlist in 2015 for approximately $100–150 million.",
        "Combined price for the three deals is roughly $400–500 million — far above Google's ~$10M writely-era buys.",
        "Kurt DelBene, former Microsoft Office president, joined as guest; later led Microsoft LinkedIn acquisition integration.",
    ],
    mental_model={
        "name": "Premium Buy for Time on Foreign Platform",
        "components": (
            "When the OS isn't yours (iOS/Android), internal build cycles lose to native-feeling apps from "
            "focused startups. Microsoft paid premium prices for shipped product + founder talent to "
            "shortcut App Store credibility. Buy-vs-build shifts when delay costs Office 365 churn and "
            "enterprise mobile narrative. Post-acquisition success requires giving founders scope (Soltero "
            "running Outlook), not absorptive integration."
        ),
        "application": (
            "Platform owners without mobile OS share should budget nine-figure talent acquisitions for "
            "flagship apps. Acquirers must retain founder CEOs with P&L authority, not PM roles buried "
            "in hierarchy."
        ),
    },
    competitive_advantage=(
        "Microsoft's moat was Office enterprise distribution — Outlook mobile quality was the weak link "
        "on iPhone. Acompli/Sunrise/Wunderlist buys imported Silicon Valley design taste and App Store "
        "stars overnight. DelBene's operator credibility and Nadella's culture shift enabled cross-platform "
        "commitment unthinkable under Ballmer.\n\n"
        "Office 365 bundle cross-sell improved when mobile matched Google; Wunderlist/Sunrise filled "
        "productivity graph gaps (mail/calendar/tasks).\n\n"
        "Weaknesses: high price tags with shutdown risk (Sunrise, Wunderlist eventually retired); "
        "internal teams demoralized when outsiders leapfrog; duplicate product lines during integration. "
        "Google's free tier still pressures consumer upsell."
    ),
    key_insights=[
        {
            "view": "Mobile forced Microsoft to buy taste.",
            "question": "Why not build Outlook iOS in-house?",
            "answer": "Internal teams lacked App Store-native UX velocity; Acompli already won press and users — acquisition bought time and talent on Apple's platform.",
        },
        {
            "view": "Founder promotion beats acqui-hire burial.",
            "question": "Did Javier Soltero stay engaged?",
            "answer": "Yes — ran Outlook, mirroring Adobe/Yahoo pattern Taylor Barada cites: founders who expand parent vision succeed.",
        },
        {
            "view": "Buy-vs-build depends on platform ownership.",
            "question": "Contrast with Google Docs episode?",
            "answer": "Google bought cheap prototypes for web OS it controlled; Microsoft paid premiums because Windows phone failed and iOS/Android were foreign soil.",
        },
        {
            "view": "Suite gaps require targeted M&A.",
            "question": "Why three apps?",
            "answer": "Email (Acompli), calendar (Sunrise), tasks (Wunderlist) — each category had a loved startup; Office needed parity across productivity graph.",
        },
        {
            "view": "Integration honesty matters.",
            "question": "Were all products kept?",
            "answer": "Hosts note some apps sunset later — risk of buying users who feel betrayed; still net positive for Office 365 mobile story.",
        },
    ],
    top_investment_implications=[
        {
            "ticker": "MSFT",
            "direction": "Watch",
            "confidence": "Medium",
            "thesis": "Mobile productivity M&A under Nadella/DelBene underpins Office 365 retention — template for LinkedIn and GitHub later mega-deals.",
        },
    ],
    golden_quotes=[
        "\"Javier Soltero now runs Outlook\" — David linking Acompli outcome to founder retention theme.",
        "\"Half a billion dollars\" — Ben tallying Acompli, Sunrise, and Wunderlist vs Google's ~$10M writely buys.",
        "\"Mobile-first, cloud-first\" — Nadella strategy context for cross-platform acquisitions.",
    ],
    chronology={
        "subject": "Microsoft mobile productivity acquisitions",
        "events": [
            {"date": "2014", "event": "Microsoft acquires Acompli (~$200M); Javier Soltero joins"},
            {"date": "2014–2015", "event": "Acompli rebranded as Outlook for iOS/Android"},
            {"date": "2015", "event": "Microsoft acquires Sunrise Calendar (~$100M)"},
            {"date": "2015", "event": "Microsoft acquires Wunderlist (~$100–150M)"},
            {"date": "2015", "event": "Satya Nadella mobile-first cloud-first strategy accelerates"},
            {"date": "2016-02-29", "event": "Acquired publishes Episode 8 with Kurt DelBene"},
            {"date": "2016", "event": "Episode 9 covers Google Docs — intentional compare/contrast"},
            {"date": "Later", "event": "DelBene leads LinkedIn acquisition integration"},
            {"date": "Later", "event": "Sunrise and Wunderlist features absorbed; standalone apps retired"},
            {"date": "Ongoing", "event": "Outlook mobile remains core Office 365 mobile client"},
        ],
    },
)

EPISODES["acq-episode-50-apple-beats"] = base(
    "acq-episode-50-apple-beats",
    review_notes=NOTES,
    episode_rating={"overall": 5},
    keywords=["Apple Beats", "Apple Music", "Jimmy Iovine"],
    conclusion=(
        "Episode 50 celebrates Acquired's half-century with Apple's $3 billion Beats acquisition (May "
        "2014) — 7× larger than prior record NeXT. Jimmy Iovine and Dr. Dre built headphones as fashion "
        "and emotion, not audiophile reference gear, then added Mog/Beats Music streaming when Jimmy saw "
        "digital destroying labels. Apple gained headphones margin, cultural marketing engine, and a "
        "streaming service to fight Spotify — paying for talent Apple couldn't recruit: Dre's sound "
        "tuning and Iovine's artist relationships. HTC's 2010–2013 cap table detour (51% stake, Carlyle "
        "$500M) shows value created with ~5-person core team. Hosts grade A-: expensive but strategically "
        "coherent for post-iTunes Apple Music era."
    ),
    background=(
        "Ben and David go deep on music-industry legend Jimmy Iovine (Interscope, U2 iPod, Eminem, Lady "
        "Gaga) and Dr. Dre (NWA, Aftermath, headphone tuning on beach with Jimmy, 2006). Monster "
        "manufactured early Beats; artists tested prototypes at Interscope. LeBron Olympics seeding, NFL "
        "ban-as-marketing, and lifestyle ads with Richard Sherman/Kaepernick built category.\n\n"
        "HTC bought 50.1% for $309M (2010); Carlyle invested $500M buying HTC out (2013). Mog "
        "acquisition became Beats Music (human curation vs algorithms). Financial Times leak May 8, "
        "2014 forced Dre/Jimmy silence until Apple closed. Apple needed streaming credibility as iTunes "
        "downloads peaked — Beats supplied brand, hardware cash flow ($1B+ run rate), and music-industry "
        "politics."
    ),
    important_facts=[
        "Apple acquired Beats in May 2014 for approximately $3 billion — largest Apple acquisition ever at roughly 7× the prior NeXT record (~$400M).",
        "Jimmy Iovine co-founded Beats with Dr. Dre in 2006 after a beach conversation rejecting a sneaker deal in favor of speakers/headphones.",
        "HTC purchased a 50.1% stake in Beats for $309 million in 2010; Carlyle's 2013 investment helped buy HTC out before Apple deal.",
        "Beats acquired music service Mog and relaunched as Beats Music in January 2014 with artist-led curation.",
        "Beats exceeded a $1 billion revenue run rate on headphones before Apple acquisition; core team was only ~5 people during early HTC stake.",
    ],
    mental_model={
        "name": "Market the Product Like an Artist",
        "components": (
            "Jimmy applied label A&R playbook to hardware: prototypes with Interscope roster, music-video "
            "placements, athlete seeding, emotional bass tuning vs reference accuracy. Headphones became "
            "wearable billboards. Streaming (Beats Music) extended thesis — music is emotional, human "
            "curation beats pure algorithms (foreshadowing Apple Music/Beats 1). Apple bought culture "
            "and taste IP it couldn't internalize from Cupertino engineers."
        ),
        "application": (
            "Premium consumer hardware needs brand story beyond specs — especially when converting "
            "Android/Windows users to Apple ecosystem services. Streaming wars reward industry "
            "relationships, not just interface design."
        ),
    },
    competitive_advantage=(
        "Beats' moat combined Dre's sound signature, Jimmy's artist/marketing access, and celebrity "
        "distribution (LeBron, NFL, Olympics). Emotional tuning targeted mass market, not audiophile "
        "niche — vastly larger TAM. Interscope integration gave free influencer channel competitors "
        "couldn't replicate.\n\n"
        "Apple gained instant streaming catalog negotiation credibility and hardware margin in "
        "accessories attach. Post-close, Beats headphones remain dominant revenue while Apple Music "
        "replaces downloads.\n\n"
        "Weaknesses: $3B price for ~5-person core looked rich; Monster partnership ended messily; "
        "dependency on celebrity founders; streaming still trailed Spotify on subs after relaunch. "
        "Fashion brands risk fad cycles — Beats maintained via Apple distribution."
    ),
    key_insights=[
        {
            "view": "Apple bought music industry politics, not just headphones.",
            "question": "Why pay $3B?",
            "answer": "iTunes downloads declining; Spotify winning streaming; Jimmy/Dre supplied label relationships and artist curation Apple lacked — talent acquisition at scale.",
        },
        {
            "view": "Emotional sound beats reference accuracy.",
            "question": "Why did Beats beat Bose/Sony?",
            "answer": "Dre tuned for feeling, not studio reproduction; mass market wants drama in bass — audiophile niche too small for Jimmy's ambitions.",
        },
        {
            "view": "HTC/Carlyle cap table was sideshow.",
            "question": "What about HTC owning Beats?",
            "answer": "HTC sought smartphone audio branding; Carlyle helped unwind; value created by tiny team — Apple paid for brand/IP, not factory assets.",
        },
        {
            "view": "Leak almost killed deal.",
            "question": "Why did FT scoop matter?",
            "answer": "Jimmy begged Dre silence; Apple's secrecy culture — premature news risked walkaway; classic Acquired drama.",
        },
        {
            "view": "Human curation vs algorithm.",
            "question": "Beats Music thesis?",
            "answer": "Artist playlists and Jimmy's no-freemium artist-pay stance — DNA of Apple Music launch and Beats 1 radio.",
        },
    ],
    top_investment_implications=[
        {
            "ticker": "AAPL",
            "direction": "Watch",
            "confidence": "Medium",
            "thesis": "Beats underpins Services narrative — headphones margin plus Apple Music subscriber growth; benchmark for Apple paying up for culture/talent when internal build fails.",
        },
        {
            "ticker": "SPOT",
            "direction": "Watch",
            "confidence": "Medium",
            "thesis": "Episode frames 2014 streaming war context — Apple entered from weakness in subscriptions; compare post-Beats share gains vs Spotify scale.",
        },
    ],
    golden_quotes=[
        "\"Nobody cares what you wear on your feet — you should sell speakers\" — Jimmy to Dre on the beach, founding Beats.",
        "\"Market it like Tupac or U2\" — Jimmy on treating headphones like artist launches.",
        "\"Largest acquisition in Apple's history by an order of magnitude\" — hosts on $3B vs NeXT ~$400M.",
    ],
    chronology={
        "subject": "Beats Electronics & Apple acquisition",
        "events": [
            {"date": "2006", "event": "Jimmy Iovine and Dr. Dre found Beats on Malibu beach conversation"},
            {"date": "2008", "event": "First Beats by Dr. Dre Studio headphones launch via Monster manufacturing"},
            {"date": "2008", "event": "LeBron James seeds Beats for 2008 Beijing Olympics team"},
            {"date": "2010-08", "event": "HTC acquires 50.1% of Beats for $309 million"},
            {"date": "2012–2013", "event": "Beats ends Monster partnership; brings production in-house"},
            {"date": "2013", "event": "Carlyle invests $500M; buys out remaining HTC stake"},
            {"date": "2014-01", "event": "Beats Music streaming service launches (from Mog acquisition)"},
            {"date": "2014-05-08", "event": "Financial Times reports Apple-Beats talks; founders told to stay quiet"},
            {"date": "2014-05", "event": "Apple announces ~$3B Beats acquisition"},
            {"date": "2017-12-11", "event": "Acquired Episode 50 publishes deep dive on Apple-Beats"},
        ],
    },
)

EPISODES["acq-episode-45-htc-google-and-the-future-of-mobile"] = base(
    "acq-episode-45-htc-google-and-the-future-of-mobile",
    review_notes=NOTES,
    episode_rating={"overall": 4},
    keywords=["Google Pixel", "HTC", "Vertical Integration"],
    conclusion=(
        "Recorded live as news breaks (September 20–21, 2017), Acquired covers Google's $1.1B "
        "\"cooperation agreement\" — not a full company purchase — bringing ~2,000 HTC hardware "
        "engineers (half the firm) in-house to build Pixel phones. Rick Osterloh, who ran Motorola "
        "under Google then Lenovo, leads hardware again — Motorola déjà vu ($12.5B buy, ~$3B sell) "
        "but smaller, targeted, try-before-you-buy after Pixel 2016 success with HTC as ODM. HTC "
        "remains independent with Vive and own phones; Google gets Pixel team plus non-exclusive IP "
        "license. Hosts debate vertical vs horizontal Android strategy as Samsung dominates and Apple "
        "integrates silicon to software."
    ),
    background=(
        "Ben and David rush-record as Taiwan trading halts and leaks confirm Google hiring HTC's Pixel "
        "team. History: HTC founded 1997 Taiwan OEM (Compaq iPAQ, Palm Treo 650), built first Android "
        "phone HTC Dream/T-Mobile G1 (2008), first 4G Sprint device, owned 51% of Beats briefly (2011), "
        "partnered on Vive VR.\n\n"
        "Google's 2011 Motorola purchase ($12.5B) for patents and hardware failed — sold to Lenovo 2014 "
        "for ~$3B while keeping IP. Pixel 2016 outsourced to HTC but designed by Google; 2017 deal "
        "internalizes the A-team. HTC stock down ~90% from peak; $1.9B market cap in USD. Themes: "
        "Smiling curve (design vs contract manufacturing), Samsung copycat threat, and whether Google "
        "can be horizontal Android licensor and vertical Apple competitor simultaneously."
    ),
    important_facts=[
        "Google agreed to pay $1.1 billion cash to bring approximately 2,000 HTC employees — roughly half the company — into its hardware organization (September 2017).",
        "Deal included non-exclusive license to HTC intellectual property; HTC remained an independent company continuing Vive and own smartphone lines.",
        "HTC manufactured the first Android phone, the HTC Dream (T-Mobile G1), launched in 2008 as part of the Open Handset Alliance.",
        "Google previously acquired Motorola Mobility in 2011 for $12.5 billion and sold it to Lenovo in 2014 for under $3 billion while retaining patents.",
        "Rick Osterloh — former Motorola leader under Google/Lenovo — ran Google's hardware division including Pixel, Home, and Daydream at time of deal.",
    ],
    mental_model={
        "name": "Try-Before-You-Buy Vertical Integration",
        "components": (
            "Google outsourced Pixel to HTC, validated product-market fit (best Android phone 2016 reviews), "
            "then bought the team — lower risk than Motorola's big-bang vertical bet. Horizontal Android "
            "requires OEM partners; vertical Pixel requires owned hardware — Google tries both, angering "
            "Samsung. Middle of smiling curve (HTC's historical trap) is worst place: not Foxconn, not Apple."
        ),
        "application": (
            "Platform owners should pilot with ODMs before acqui-hiring hardware teams. Full vertical "
            "integration only pays off if software-services margin justifies capital intensity — else "
            "stay fabless like Qualcomm/ARM ecosystem."
        ),
    },
    competitive_advantage=(
        "Google's Pixel edge post-deal: tight HW/SW integration for Android reference design, fast updates, "
        "AI/Assistant showcase, and camera computational photography lead. HTC team proved execution on "
        "Pixel 1; bringing them in-house removes arm's-length friction.\n\n"
        "Patent license plus retained Motorola IP stack reduces litigation risk vs 2011 era. $1.1B price "
        "vs $12.5B Motorola is disciplined capital allocation lesson learned.\n\n"
        "Weaknesses: Samsung still owns Android high-end share; Google competes with OEM partners; HTC "
        "gutted may weaken ODM options. Rick Osterloh replay invites \"same movie\" skepticism. HTC left "
        "with cash but unclear consumer brand future — pattern of pioneering then divesting winners (Beats)."
    ),
    key_insights=[
        {
            "view": "Agreement, not acquisition — semantics matter.",
            "question": "Did Google buy HTC?",
            "answer": "No — hired ~2,000 engineers and licensed IP; HTC continues independently — structured to avoid partner freak-out vs full Motorola takeover.",
        },
        {
            "view": "Motorola scar shaped deal size.",
            "question": "Why only $1.1B?",
            "answer": "Google lost billions on Motorola hardware; Pixel tryout proved team before purchase — methodical vs 2011 aggression.",
        },
        {
            "view": "HTC repeats pioneer-then-miss pattern.",
            "question": "What happens to HTC?",
            "answer": "Hosts note history: G1, Beats stake, Vive — creates value others capture; $1.1B cash buys runway but brand future uncertain.",
        },
        {
            "view": "Vertical + horizontal tension persists.",
            "question": "Can Google compete with Samsung and license Android?",
            "answer": "Inherent conflict — Pixel success threatens OEMs; Samsung copies iPhone playbook while Google needs openness narrative.",
        },
        {
            "view": "Live episode captures market reaction.",
            "question": "Why record as news breaks?",
            "answer": "Acquired experiments with timely analysis — assumptions stated upfront, corrected when Google blog post confirms details mid-show.",
        },
    ],
    top_investment_implications=[
        {
            "ticker": "GOOGL",
            "direction": "Watch",
            "confidence": "Medium",
            "thesis": "Pixel/hardware vertical bet supports Services and AI showcase devices; episode frames capital discipline post-Motorola — watch Pixel share vs Samsung and Apple.",
        },
        {
            "ticker": "AAPL",
            "direction": "Watch",
            "confidence": "Low",
            "thesis": "Integrated model benchmark — Google's partial vertical move acknowledges Apple integration advantage without full stack ownership.",
        },
    ],
    golden_quotes=[
        "\"Cooperation agreement\" — Google/HTC avoid calling it an acquisition.",
        "\"Same people executing the playbook all over again\" — David on Rick Osterloh and Motorola déjà vu.",
        "\"Best Android phone ever made\" — widely cited Pixel 2016 reviews motivating the team purchase.",
    ],
    chronology={
        "subject": "HTC & Google hardware agreement",
        "events": [
            {"date": "1997", "event": "HTC founded in Taiwan as OEM contractor"},
            {"date": "2008", "event": "HTC Dream / T-Mobile G1 — first Android phone ships"},
            {"date": "2011", "event": "HTC acquires ~51% stake in Beats Electronics"},
            {"date": "2011", "event": "Google acquires Motorola Mobility for $12.5 billion"},
            {"date": "2014", "event": "Google sells Motorola to Lenovo for ~$3 billion; keeps patents"},
            {"date": "2016", "event": "Google Pixel launches; manufactured by HTC to Google design"},
            {"date": "2017-09-20", "event": "Leaks emerge; HTC trading halted ahead of announcement"},
            {"date": "2017-09-21", "event": "Google announces $1.1B agreement for HTC hardware team"},
            {"date": "2017-09-21", "event": "Rick Osterloh blog post confirms team joining Google hardware"},
            {"date": "2017-09-21", "event": "Acquired records live Episode 45 on HTC-Google deal"},
        ],
    },
)

# Patch metadata titles/dates/youtube where discovered catalog is wrong
_META_PATCHES = {
    "acq-season-4-episode-4-the-lyft-ipo": {
        "title": "The Lyft IPO",
        "guest": "The Lyft IPO",
        "guest_role": "Season 4 · Episode 4",
        "date": "2019-03-30",
        "duration_minutes": 90,
        "youtube_url": "https://www.youtube.com/watch?v=xmYekD6-PZ8",
    },
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
    "acq-season-3-episode-7-venmo-sf-live-show-with-andrew-kortina": {
        "title": "Venmo (SF Live Show with Andrew Kortina)",
        "guest": "Andrew Kortina",
        "guest_role": "Venmo Co-founder · Season 3 · Episode 7",
        "date": "2018-10-29",
        "duration_minutes": 90,
    },
    "acq-episode-9-writely-google-docs": {
        "title": "Writely (Google Docs)",
        "guest": "Writely (Google Docs)",
        "guest_role": "Season 1 · Episode 9",
        "date": "2016-03-01",
        "duration_minutes": 55,
    },
    "acq-episode-8-acompli-sunrise-and-wunderlist": {
        "title": "Acompli, Sunrise, and Wunderlist (w/ Kurt DelBene)",
        "guest": "Kurt DelBene",
        "guest_role": "Microsoft · Season 1 · Episode 8",
        "date": "2016-02-29",
        "duration_minutes": 75,
    },
    "acq-episode-50-apple-beats": {
        "title": "Apple - Beats",
        "guest": "Apple - Beats",
        "guest_role": "Season 1 · Episode 50",
        "date": "2017-12-11",
        "duration_minutes": 81,
    },
    "acq-episode-45-htc-google-and-the-future-of-mobile": {
        "title": "HTC, Google and the Future of Mobile",
        "guest": "HTC, Google and the Future of Mobile",
        "guest_role": "Season 1 · Episode 45",
        "date": "2017-09-21",
        "duration_minutes": 75,
    },
}

for eid, patch in _META_PATCHES.items():
    if eid in EPISODES:
        EPISODES[eid]["metadata"].update(patch)
        if patch.get("youtube_url"):
            EPISODES[eid]["metadata"]["links"]["youtube"] = patch["youtube_url"]
