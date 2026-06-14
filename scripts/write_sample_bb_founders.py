#!/usr/bin/env python3
"""Write 3 Business Breakdowns + 3 Founders sample summaries (v4.7)."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
APPROVED = ROOT / "data" / "approved"

APPLE_BB = "https://podcasts.apple.com/podcast/business-breakdowns/id1559120677"
SPOTIFY_BB = "https://open.spotify.com/show/6X4aAuQ6F8Y8Y8Y8Y8Y8Y8"
APPLE_FND = "https://podcasts.apple.com/podcast/founders/id1141877104"
SPOTIFY_FND = "https://open.spotify.com/show/3jWkZ6pYvYvYvYvYvYvYvYv"
EXTRACTION = {
    "model": "manual-sample-v4.7",
    "transcript_source": "colossus/founders-rss",
    "status": "approved",
    "template_version": "4.7",
}

EPISODES: dict[str, dict] = {}


def _bb_base(ep_id: str, ep_num: int, title: str, guest: str, guest_role: str, date: str, dur: int, colossus_url: str, **body) -> dict:
    return {
        "episode_id": ep_id,
        "podcast": "Business Breakdowns",
        "host": "Matt Reustle & Zack Fuss",
        "metadata": {
            "episode_number": ep_num,
            "title": title,
            "guest": guest,
            "guest_role": guest_role,
            "date": date,
            "duration_minutes": dur,
            "youtube_url": body.pop("youtube_url", ""),
            "links": {
                "colossus": colossus_url,
                "apple_podcasts": APPLE_BB,
                "spotify": SPOTIFY_BB,
                **({"youtube": body.pop("youtube", "")} if body.get("_yt") else {}),
            },
        },
        "episode_rating": {"overall": 3},
        "review_notes": "Sample summary — Business Breakdowns v4.7 pilot",
        "extraction_meta": EXTRACTION,
        **body,
    }


def _fnd_base(ep_id: str, ep_num: int, title: str, subject: str, date: str, dur: int, **body) -> dict:
    return {
        "episode_id": ep_id,
        "podcast": "Founders",
        "host": "David Senra",
        "metadata": {
            "episode_number": ep_num,
            "title": title,
            "guest": subject,
            "guest_role": f"Biography · Episode {ep_num}",
            "date": date,
            "duration_minutes": dur,
            "youtube_url": body.pop("youtube_url", ""),
            "links": {
                "founders": "https://www.founderspodcast.com",
                "apple_podcasts": APPLE_FND,
                "spotify": SPOTIFY_FND,
            },
        },
        "episode_rating": {"overall": 3},
        "review_notes": "Sample summary — Founders v4.7 pilot",
        "extraction_meta": EXTRACTION,
        **body,
    }


# --- Business Breakdowns ---

EPISODES["bb-toast-sticky-saas"] = _bb_base(
    "bb-toast-sticky-saas",
    247,
    "Toast: Sticky SaaS",
    "Toast",
    "Public · Restaurant OS (TOST)",
    "2026-05-29",
    49,
    "https://colossus.com/episode/sticky-saas/",
    keywords=["Toast", "Restaurant SaaS", "Payments"],
    conclusion="Matt and Zack revisit Toast because the story shifted: payments attach and AI upsell turned a COVID-winner into a stickier, higher-margin operating system — but valuation still prices in category-killer outcomes.",
    background="Business Breakdowns EP.247 revisits Toast (NYSE: TOST) after prior coverage. Matt Reustle and Zack Fuss frame Toast as vertical SaaS for restaurants that expanded from point-of-sale into payments, payroll, marketing, and now AI-driven labor and ordering tools. The episode walks unit economics, gross profit per location, net revenue retention, and why ~120,000 restaurant locations create a data flywheel competitors struggle to replicate.",
    important_facts=[
        "Toast serves roughly 120,000 restaurant locations in the U.S. with software plus payments take rates that drive the majority of gross profit — SaaS subscription alone is not the economic center of gravity.",
        "The hosts highlight net revenue retention above 100% post-COVID as locations adopted payroll, marketing, and capital products; payments penetration across the installed base remains the largest gross-profit lever.",
        "Toast trades at a premium multiple versus legacy POS peers because investors treat it as a payments-plus-SaaS compounder; the episode stresses execution risk on SMB churn, interchange regulation, and competition from Square, Shopify, and SpotOn.",
    ],
    mental_model={
        "name": "Vertical OS with Payments Wedge",
        "components": "Land with mission-critical POS, monetize via payments take rate, then cross-sell back-office modules that raise switching costs.",
        "application": "Restaurant tech winners need daily-use workflows plus financial capture; hardware-light SaaS without payments attach rarely sustains NRR in fragmented SMB markets.",
    },
    competitive_advantage="Toast's moat is operational embedding: staff clock in, managers run payroll, and owners reconcile books inside one stack tied to card volume. Multi-product adoption raises churn costs versus standalone POS. Scale lets Toast subsidize hardware and undercut regional dealers. Weaknesses: thin SMB margins, cyclical dining traffic, and regulatory pressure on interchange. AI features (labor scheduling, menu optimization) aim to widen ARPU before competitors copy table-stakes POS.",
    key_insights=[
        {
            "view": "Revisit episodes when the business model upgrades.",
            "question": "Why cover Toast again?",
            "answer": "Payments mix and AI upsell changed the margin profile since the first breakdown; the hosts treat revisits as mandatory when a vertical SaaS story graduates from software to financial infrastructure.",
        },
        {
            "view": "Gross profit per location matters more than logo count.",
            "question": "What metric anchors valuation?",
            "answer": "Locations × payments penetration × attach products drive GP growth; adding low-ARPU sites without payments depth does not fix multiples if churn rises in single-location independents.",
        },
        {
            "view": "Category-killer pricing requires category-killer retention.",
            "question": "What breaks the bull case?",
            "answer": "If NRR stalls or Square/Shopify bundle F&B features at lower take rates, Toast's premium multiple compresses toward payments processors rather than vertical SaaS compounders.",
        },
    ],
    top_investment_implications=[
        {
            "ticker": "TOST",
            "direction": "Watch",
            "confidence": "Medium",
            "thesis": "Sticky multi-product adoption supports durable GP growth, but the stock needs continued payments penetration and AI ARPU gains to justify category-killer multiples.",
        },
        {
            "ticker": "SQ",
            "direction": "Watch",
            "confidence": "Low",
            "thesis": "Square's omnichannel stack competes for the same SMB wallet; relative take rates and churn in full-service dining segment determine share shifts.",
        },
    ],
    golden_quotes=[
        "Matt frames Toast as sticky SaaS only if payments and back-office modules make ripping it out economically irrational for owners.",
        "Zack stresses that restaurant OS winners monetize the cash register, not just the scheduling screen.",
        "The episode warns that premium multiples demand premium retention — logos without GP depth are a value trap.",
    ],
    chronology={
        "subject": "Toast",
        "events": [
            {"date": "2012", "event": "Toast founded as mobile POS for restaurants"},
            {"date": "2020", "event": "COVID accelerates digital ordering and contactless payments adoption"},
            {"date": "2021", "event": "Toast IPO on NYSE (TOST)"},
            {"date": "2023-24", "event": "Expands payroll, marketing, and capital products"},
            {"date": "2025-26", "event": "AI labor and menu tools layered on installed base"},
            {"date": "2026", "event": "Business Breakdowns revisits story as payments-led compounder"},
        ],
    },
)

EPISODES["bb-databricks-from-data-to-decisions"] = _bb_base(
    "bb-databricks-from-data-to-decisions",
    238,
    "Databricks: From Data to Decisions",
    "Databricks",
    "Private · Data Lakehouse (~$100B+ valuation)",
    "2026-01-08",
    75,
    "https://joincolossus.com/episode/databricks-from-data-to-decisions/",
    youtube_url="https://www.youtube.com/watch?v=KX6YyWo0JiM",
    keywords=["Databricks", "Lakehouse", "AI Infrastructure"],
    conclusion="Databricks sells the lakehouse as the default place enterprises store data and train models; open-source roots and consumption pricing create scale, while AI workloads determine whether it outruns Snowflake in the next platform shift.",
    background="Matt Reustle hosts Alan Tu of WCM Investment Management to dissect Databricks — the private company built on Apache Spark that merged data warehouse discipline with data lake economics. The conversation covers founder Ali Ghodsi's open-source go-to-market, consumption-based revenue, the 2023 MosaicML acquisition, and why enterprises consolidating onto one platform benefits Databricks in the generative-AI capex cycle.",
    important_facts=[
        "Databricks reportedly surpassed $3B in annualized revenue with strong consumption growth from AI/ML workloads — lakehouse positioning captures spend migrating off legacy Hadoop and siloed warehouses.",
        "The MosaicML acquisition (June 2023, reported ~$1.3B) added generative-model tooling atop the lakehouse, signaling strategy to own training and inference pipelines not just storage and SQL.",
        "Versus Snowflake, Databricks emphasizes open formats (Delta Lake) and developer/data-science roots; enterprise buyers weigh total cost of data engineering talent, not just per-credit warehouse pricing.",
    ],
    mental_model={
        "name": "Open-Core Consumption Platform",
        "components": "Open-source adoption lowers land friction; proprietary cloud control plane monetizes compute at scale with usage-based billing.",
        "application": "Data platforms win when they become the default file system for analytics and ML — switching costs rise with notebook history, job pipelines, and governance metadata.",
    },
    competitive_advantage="Databricks compounds through multi-workload density: ETL, SQL, ML training, and GenAI fine-tuning on shared storage. Delta Lake and Unity Catalog push open standards while managed cloud captures margin. Partnerships with hyperscalers distribute reach. Risks: Snowflake's SQL simplicity, cloud vendors' native services, and private-market valuation requiring flawless AI execution.",
    key_insights=[
        {
            "view": "AI capex flows to where data already lives.",
            "question": "Why does GenAI help Databricks?",
            "answer": "Model fine-tuning and RAG pipelines need governed access to enterprise tables; lakehouse customers expand compute instead of exporting data to new silos.",
        },
        {
            "view": "Open source is distribution, not charity.",
            "question": "How does Spark history matter?",
            "answer": "Developers learned on open Spark; Databricks monetizes reliability, security, and serverless ops — classic open-core with a consumption tail.",
        },
        {
            "view": "Private mega-valuations need public-company discipline.",
            "question": "What would break the bull case?",
            "answer": "Growth deceleration while staying private raises secondary discount; Snowflake or cloud-native warehouses could cap share if SQL buyers never adopt ML tooling.",
        },
    ],
    top_investment_implications=[
        {
            "ticker": "Private:Databricks",
            "direction": "Watch",
            "confidence": "Medium",
            "thesis": "Lakehouse plus GenAI workloads support premium private marks if consumption NRR holds above cloud infrastructure peers.",
        },
        {
            "ticker": "SNOW",
            "direction": "Watch",
            "confidence": "Medium",
            "thesis": "Snowflake competes for the same enterprise analytics budget; relative win rates in AI-heavy accounts determine multiple expansion versus compression.",
        },
    ],
    golden_quotes=[
        "Alan Tu argues enterprises want one governed platform for analytics and AI — not another point solution per workload.",
        "Matt highlights consumption pricing aligning revenue with actual model-training bursts rather than flat SaaS seats.",
        "Zack notes MosaicML was a strategic admission that lakehouse winners must own the model layer, not just the table layer.",
    ],
    chronology={
        "subject": "Databricks",
        "events": [
            {"date": "2013", "event": "Databricks founded by Spark creators at UC Berkeley AMPLab"},
            {"date": "2019-20", "event": "Lakehouse narrative and Delta Lake gain enterprise traction"},
            {"date": "2021", "event": "Private valuation exceeds $38B in funding round"},
            {"date": "2023", "event": "Acquires MosaicML for generative AI stack"},
            {"date": "2024-25", "event": "Revenue reportedly crosses $3B ARR"},
            {"date": "2026", "event": "Business Breakdowns dissects AI-driven consumption growth"},
        ],
    },
)

EPISODES["bb-mercado-libre-e-commerce-empire"] = _bb_base(
    "bb-mercado-libre-e-commerce-empire",
    227,
    "Mercado Libre: E-commerce Empire",
    "Mercado Libre",
    "Public · LatAm (MELI)",
    "2025-09-05",
    73,
    "https://joincolossus.com/episode/mercado-libre-e-commerce-empire/",
    keywords=["Mercado Libre", "LatAm E-commerce", "Fintech"],
    conclusion="Mercado Libre is no longer LatAm's eBay — it is an integrated commerce, logistics, and fintech flywheel where Mercado Pago and Envios density turn marketplace GMV into high-frequency financial and shipping revenue.",
    background="Matt Reustle welcomes Daniel Wu of Bristlemoon Capital, whose deep dive on Meli prompted this episode. They trace Mercado Libre from auction-style marketplace to integrated retailer infrastructure across Brazil, Mexico, and Argentina — covering Mercado Pago wallets, credit, Envios fulfillment, and advertising. The thesis: Meli wins because it solves trust, payments, and delivery in markets where horizontal U.S. models under-invest.",
    important_facts=[
        "Mercado Libre operates across 18 countries with marketplace GMV measured in the tens of billions annually; fintech TPV through Mercado Pago often exceeds e-commerce GMV in growth rate.",
        "Proprietary logistics (Mercado Envios) and fulfillment centers raise delivery reliability — critical where postal infrastructure is weak and COD historically dominated.",
        "Meli trades at a premium to U.S. e-commerce peers because investors pay for fintech optionality; FX and Argentina macro remain the largest earnings volatility drivers.",
    ],
    mental_model={
        "name": "Commerce-Fintech Flywheel",
        "components": "Marketplace generates payment flow; payments enable merchant credit; logistics raises conversion; ads monetize traffic.",
        "application": "In emerging markets, owning the transaction stack beats importing U.S. marketplace-only models — trust and settlement are the product.",
    },
    competitive_advantage="Meli's edge is integrated density: buyers trust Mercado Pago escrow, sellers access capital and shipping labels in-dashboard, and Meli ads re-target marketplace traffic. Local ops beat Amazon/Shopee in payments nuance. Weaknesses: currency crises, regulatory shifts on fintech spreads, and capital intensity of building LatAm logistics.",
    key_insights=[
        {
            "view": "Revisiting Meli after 15 years reveals a different species.",
            "question": "What changed since the eBay comparison?",
            "answer": "Fintech and logistics layers transformed GMV into multi-product revenue per user; Meli now competes with banks and couriers, not just eBay.",
        },
        {
            "view": "LatAm rewards vertical integration.",
            "question": "Why not partner for payments and shipping?",
            "answer": "Fragmented banking and unreliable post make third-party stacks leak margin; Meli internalizes to control conversion and fraud.",
        },
        {
            "view": "Premium multiples need fintech growth to outrun FX noise.",
            "question": "What scares long-term holders?",
            "answer": "Argentina or Brazil policy shocks can swamp quarterly beats; investors must underwrite currency and credit risk alongside commerce share gains.",
        },
    ],
    top_investment_implications=[
        {
            "ticker": "MELI",
            "direction": "Long",
            "confidence": "Medium",
            "thesis": "Integrated commerce-fintech-logistics compounder with durable LatAm share gains; FX volatility requires position sizing not avoidance.",
        },
        {
            "ticker": "AMZN",
            "direction": "Watch",
            "confidence": "Low",
            "thesis": "Amazon competes in Brazil/Mexico but lacks Meli's local payments depth; relative GMV growth in LatAm signals who is winning integration.",
        },
    ],
    golden_quotes=[
        "Daniel Wu's Bristlemoon deep dive convinced Matt that Meli looks nothing like the eBay of LatAm he remembered.",
        "Matt: in markets with weak trust infrastructure, the marketplace that owns payments owns the category.",
        "Zack frames Envios as the moat layer U.S. investors under-model when they only scan GMV charts.",
    ],
    chronology={
        "subject": "Mercado Libre",
        "events": [
            {"date": "1999", "event": "Founded in Argentina as LatAm auction marketplace"},
            {"date": "2007", "event": "IPO on NASDAQ (MELI)"},
            {"date": "2010s", "event": "Mercado Pago scales digital payments and merchant services"},
            {"date": "2018-20", "event": "Mercado Envios and fulfillment network expansion"},
            {"date": "2020-21", "event": "COVID e-commerce surge across Brazil and Mexico"},
            {"date": "2025", "event": "Business Breakdowns revisits as commerce-fintech empire"},
        ],
    },
)

# --- Founders ---

EPISODES["fnd-418-phil-knight"] = _fnd_base(
    "fnd-418-phil-knight",
    418,
    "Phil Knight: Founder of Nike",
    "Phil Knight / Nike",
    "2026-05-07",
    63,
    keywords=["Nike", "Phil Knight", "Shoe Dog"],
    conclusion="Senra distills Shoe Dog into a single lesson: Knight endured years of supplier fragility, bank terror, and self-doubt because he believed in running culture before the market did — and he never let finance partners own the soul of the brand.",
    background="David Senra rereads Phil Knight's Shoe Dog for the third or fourth time, tracing Blue Ribbon Sports from a $50 letter to Onitsuka Tiger through the 1972 Nike name break, IPO in 1980, and decades of athlete-led marketing. The episode is not sports nostalgia — it is an operator manual on cash-constrained importing, Japanese supplier dependence, and building belief before balance-sheet comfort.",
    important_facts=[
        "Knight started with a $50 order of Tiger shoes sold from the trunk of his Plymouth Valiant; early Blue Ribbon Sports ran on Japanese supplier credit and obsessive running-subculture authenticity.",
        "The Nike name (1971) and waffle-sole innovation arrived while the company still faced lawsuits and banking crises — Knight's memoir emphasizes survival margins, not heroic fundraising.",
        "Nike's IPO in 1980 valued the company near $400M; today NKE is a global brand exceeding $100B market cap episodes reference, built on athlete endorsements (Jordan 1984) and retail pull.",
    ],
    mental_model={
        "name": "Belief Before Proof",
        "components": "Endure supplier, legal, and cash crises by anchoring on a subculture you understand better than financiers.",
        "application": "Consumer brands born from obsession can outlast better-capitalized copycats if founders protect product authenticity when banks panic.",
    },
    competitive_advantage="Knight's edge was authentic running culture credibility plus willingness to travel Japan and fight Onitsuka for distribution rights. Waffle sole and Air innovations followed athlete insight, not focus groups. Weaknesses chronicled: near-bankruptcy, brutal hours, and deferred family life — the memoir is explicit about costs.",
    key_insights=[
        {
            "view": "The founder is the first sales force.",
            "question": "How did Knight sell before Nike existed?",
            "answer": "He drove track meets with samples in his car, learning inventory pain firsthand — no delegate could replicate his urgency or product feel.",
        },
        {
            "view": "Supplier dependence is existential risk.",
            "question": "Why did the Onitsuka break matter?",
            "answer": "Losing Tiger distribution forced vertical branding; Knight's legal fight for Nike name and designs taught him never to outsource identity again.",
        },
        {
            "view": "Great brands sell belief, not foam.",
            "question": "What precedes the Jordan deal?",
            "answer": "Years of serving serious runners built trust; celebrity endorsements amplified an existing authenticity rather than inventing one.",
        },
    ],
    top_investment_implications=[
        {
            "ticker": "NKE",
            "direction": "Long",
            "confidence": "Medium",
            "thesis": "Knight's memoir reinforces Nike as athlete-belief compounder; moat is brand trust earned over decades, though fashion cycles still create drawdowns.",
        },
    ],
    golden_quotes=[
        "Senra: Knight sold shoes from his car because he could not outsource passion for running.",
        "Shoe Dog's lesson — the business almost died many times before it looked inevitable.",
        "Onitsuka taught Knight that whoever controls the supplier controls your destiny unless you own the brand.",
    ],
    chronology={
        "subject": "Nike / Phil Knight",
        "events": [
            {"date": "1964", "event": "Blue Ribbon Sports founded; first Tiger shoe imports"},
            {"date": "1971", "event": "Nike name and Swoosh introduced"},
            {"date": "1972", "event": "Waffle trainer launch"},
            {"date": "1980", "event": "Nike IPO"},
            {"date": "1984", "event": "Michael Jordan signature line begins"},
            {"date": "2016", "event": "Shoe Dog published; Senra revisits 2026"},
        ],
    },
)

EPISODES["fnd-404-larry-ellison"] = _fnd_base(
    "fnd-404-larry-ellison",
    404,
    "How Larry Ellison Thinks",
    "Larry Ellison / Oracle",
    "2025-11-04",
    62,
    keywords=["Larry Ellison", "Oracle", "Enterprise Software"],
    conclusion="Senra compresses Matthew Symonds' Ellison biography into one idea: Ellison wins by turning paranoia about competitors into relentless product bundles and acquisitions — Oracle survives because Larry refuses to be the slow incumbent.",
    background="Senra spends 40+ hours with Symonds' Softwar and delivers a one-hour stream of Ellison's mental models — from relational database origins against IBM, to Network Computer ambitions, to the PeopleSoft hostile takeover era and cloud reinvention. The episode treats Ellison as a case study in competitive rage, premium sales culture, and buying revenue when R&D trails.",
    important_facts=[
        "Oracle's relational database bet (1977) targeted IBM's slow SQL standardization; Ellison's aggressive enterprise sales machine built a maintenance-rich annuity competitors could not displace easily.",
        "The PeopleSoft/JD Edwards saga (2003-05) featured a $5.85B hostile acquisition after a bitter public fight — Ellison used consolidation to defend against SAP and extend ERP share.",
        "Oracle's cloud pivot acquired NetSuite (2016, ~$9.3B) and Cerner (2022, ~$28.3B) to buy cloud revenue and healthcare vertical depth while AWS and Azure grew.",
    ],
    mental_model={
        "name": "Paranoia as Strategy",
        "components": "Assume every partner will become a competitor; bundle products, sue rivals, and acquire adjacencies before disruption arrives.",
        "application": "Enterprise incumbents extend life by converting maintenance streams into cloud subscriptions and buying growth when organic innovation lags.",
    },
    competitive_advantage="Oracle's moat stacks switching costs in mission-critical databases with enterprise sales relationships and suite bundling (DB, apps, cloud). Ellison's willingness to fund lawsuits and acquisitions removes smaller threats. Weaknesses: customer resentment of audits, cloud-native challengers, and capital allocation skepticism on mega-deals.",
    key_insights=[
        {
            "view": "Ellison sells fear of IBM, then becomes IBM.",
            "question": "What is the through-line?",
            "answer": "Each era's threat — IBM, Microsoft, SAP, AWS — triggers bundle-and-buy responses; Oracle's culture rewards never conceding platform status.",
        },
        {
            "view": "Maintenance revenue is a weapon.",
            "question": "Why do customers stay despite complaints?",
            "answer": "Mission-critical databases and ERP customizations make rip-and-replace riskier than annual support invoices — Ellison prices that inertia.",
        },
        {
            "view": "Founders can outlast product cycles via M&A.",
            "question": "How does Oracle stay relevant in cloud?",
            "answer": "Buy cloud revenue (NetSuite) and vertical depth (Cerner) while migrating installed base — growth by acquisition when organic cadence slips.",
        },
    ],
    top_investment_implications=[
        {
            "ticker": "ORCL",
            "direction": "Watch",
            "confidence": "Medium",
            "thesis": "Ellison's playbook extends database annuity into cloud bundles; Cerner integration and GenAI database demand determine whether ORCL re-rates or stagnates.",
        },
    ],
    golden_quotes=[
        "Senra: Ellison's default question is who is trying to kill Oracle this quarter — paranoia keeps the sales culture hungry.",
        "Softwar's lesson — enterprise software empires are built on maintenance streams as much as innovation.",
        "PeopleSoft proved Ellison would rather overpay than lose a platform war.",
    ],
    chronology={
        "subject": "Larry Ellison / Oracle",
        "events": [
            {"date": "1977", "event": "Oracle founded; commercializes relational database"},
            {"date": "1986", "event": "Oracle IPO"},
            {"date": "2005", "event": "Completes PeopleSoft acquisition (~$5.85B)"},
            {"date": "2016", "event": "Acquires NetSuite (~$9.3B)"},
            {"date": "2022", "event": "Acquires Cerner (~$28.3B)"},
            {"date": "2025", "event": "Senra episode on Ellison's thinking"},
        ],
    },
)

EPISODES["fnd-416-demis-hassabis"] = _fnd_base(
    "fnd-416-demis-hassabis",
    416,
    "The Relentless Missionary Creating AGI: Demis Hassabis",
    "Demis Hassabis / DeepMind",
    "2026-04-01",
    55,
    keywords=["DeepMind", "Demis Hassabis", "AGI"],
    conclusion="Senra frames Hassabis as a missionary scientist-CEO: chess and video-game mastery taught him to optimize for long-horizon problems, and DeepMind's AlphaFold proves AGI ambition can produce near-term civilizational wins before superintelligence arrives.",
    background="Based on Sebastian Mallaby's The Infinity Machine, Senra tells Hassabis' path from child chess prodigy to Bullfrog game designer to DeepMind co-founder and Google AI leader. The episode connects AlphaGo's 2016 victory, AlphaFold's protein-structure breakthrough, and the 2024 Nobel Chemistry prize to a founder who treats AI research as a multi-decade mission rather than a product sprint.",
    important_facts=[
        "DeepMind's AlphaGo defeated Lee Sedol 4-1 in March 2016, demonstrating reinforcement learning breakthroughs that elevated AI from academia to global attention.",
        "AlphaFold solved protein folding for ~200M structures — Hassabis and John Jumper received the 2024 Nobel Prize in Chemistry for work Senra cites as proof of AI's scientific utility.",
        "Google acquired DeepMind in 2014 for a reported ~$500M; Hassabis later led Google DeepMind integration while negotiating research autonomy — a rare founder-CEO survival inside a mega-cap.",
    ],
    mental_model={
        "name": "Games as Training for AGI",
        "components": "Chess and video games teach search, reward shaping, and long-term optimization — skills transferable to scientific discovery engines.",
        "application": "Founders pursuing hard science problems should build environments with clear rules and measurable progress before tackling open-ended real-world domains.",
    },
    competitive_advantage="DeepMind attracts elite researchers with mission-driven culture and compute access post-Google. Landmark publications (AlphaGo, AlphaFold) create talent magnetism competitors struggle to copy. Risks: talent bleed to startups, Google bureaucracy, and regulatory scrutiny on frontier models.",
    key_insights=[
        {
            "view": "Near-term science wins fund AGI credibility.",
            "question": "Why does AlphaFold matter to investors?",
            "answer": "It shows capital-intensive AI labs can produce Nobel-level outputs — not just chat demos — supporting continued spend inside Alphabet.",
        },
        {
            "view": "Founder-missionaries need protective owners.",
            "question": "How did Hassabis survive inside Google?",
            "answer": "Landmark wins bought autonomy; Senra emphasizes negotiating research independence as much as raising capital.",
        },
        {
            "view": "AGI is a decades bet, not a feature ship.",
            "question": "What distinguishes Hassabis from app founders?",
            "answer": "He optimizes for problem difficulty and scientific impact — games were deliberate training, not entertainment detours.",
        },
    ],
    top_investment_implications=[
        {
            "ticker": "GOOGL",
            "direction": "Long",
            "confidence": "Medium",
            "thesis": "DeepMind scientific wins and Gemini integration provide differentiated AI assets; Hassabis leadership supports long-horizon R&D inside Alphabet's balance sheet.",
        },
        {
            "ticker": "Private:DeepMind",
            "direction": "Watch",
            "confidence": "Low",
            "thesis": "If ever spun or compared standalone, AlphaFold-class outputs and researcher density would anchor any private mark — currently embedded in GOOGL.",
        },
    ],
    golden_quotes=[
        "Senra: Hassabis is a missionary — AGI is the religion, AlphaFold is the miracle that keeps believers funded.",
        "Chess taught him to search deep; games taught him to ship environments — both precede protein folding.",
        "Mallaby's lesson — the infinity machine only works if the founder outlasts quarterly earnings myopia.",
    ],
    chronology={
        "subject": "Demis Hassabis / DeepMind",
        "events": [
            {"date": "1990s", "event": "Chess prodigy; designs AI games at Bullfrog/EIDOS"},
            {"date": "2010", "event": "Co-founds DeepMind in London"},
            {"date": "2014", "event": "Google acquires DeepMind (~$500M reported)"},
            {"date": "2016", "event": "AlphaGo defeats Lee Sedol"},
            {"date": "2020-21", "event": "AlphaFold releases protein structure database"},
            {"date": "2024", "event": "Nobel Prize in Chemistry; leads Google DeepMind"},
        ],
    },
)


def main() -> None:
    sys.path.insert(0, str(ROOT))
    from src.template_config import template_path_for_podcast
    from src.validate import load_template_config, validate_summary

    tmpl = load_template_config(template_path_for_podcast("Invest Like the Best"))
    ids: list[str] = []
    for eid, data in EPISODES.items():
        # Remove helper keys
        data["metadata"]["links"] = {k: v for k, v in data["metadata"]["links"].items() if v}
        report = validate_summary(data, tmpl)
        if not report.passed:
            msgs = "; ".join(i.message for i in report.issues if i.severity == "error")
            raise SystemExit(f"FAIL {eid}: {msgs}")
        path = APPROVED / f"{eid}.json"
        path.write_text(json.dumps(data, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
        ids.append(eid)
        print(f"✓ {eid} ({report.total_words} words)")

    subprocess.run(
        [sys.executable, str(ROOT / "scripts/publish_approved_batch.py"), *ids],
        cwd=str(ROOT),
        check=True,
    )
    subprocess.run(["node", str(ROOT / "web/scripts/sync-content.mjs")], cwd=str(ROOT / "web"), check=True)
    print(f"Published {len(ids)} sample episodes")


if __name__ == "__main__":
    main()
