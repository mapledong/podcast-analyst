"""One-off: write batch-2 Acquired v5.1 summaries. Run from repo root."""
from __future__ import annotations

import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "scripts"))
APPROVED = ROOT / "data" / "approved"
DISCOVERED = json.loads((ROOT / "data" / "discovered" / "acquired_episodes.json").read_text())

LINKS_BASE = {
    "apple_podcasts": "https://podcasts.apple.com/podcast/acquired/id1050462261",
    "spotify": "https://open.spotify.com/show/2HI3KdjtJnr3E8B4W8Y0Yx",
}

META = {e["id"]: e for e in DISCOVERED["episodes"]}


def links(ep: dict) -> dict:
    out = {
        "youtube": ep.get("youtube_url") or "",
        "acquired": ep["acquired_url"],
        **LINKS_BASE,
    }
    return out


def base(ep_id: str, **kwargs) -> dict:
    ep = META[ep_id]
    m = {
        "episode_number": ep["episode_number"],
        "title": ep["title"],
        "guest": ep["guest"],
        "guest_role": ep["guest_role"],
        "date": ep["date"],
        "duration_minutes": ep["duration_minutes"],
        "youtube_url": ep.get("youtube_url") or "",
        "links": links(ep),
    }
    return {
        "episode_id": ep_id,
        "podcast": "Acquired",
        "host": "Ben Gilbert & David Rosenthal",
        "metadata": m,
        "extraction_meta": {
            "model": "manual-gpt-agent-v4.7",
            "transcript_source": "acquired.fm",
            "status": "approved",
            "template_version": "5.1-acquired",
        },
        **kwargs,
    }


EPISODES: dict[str, dict] = {}

# --- acq-the-steve-ballmer-interview ---
EPISODES["acq-the-steve-ballmer-interview"] = base(
    "acq-the-steve-ballmer-interview",
    episode_rating={"overall": 5},
    keywords=["Enterprise Agreements", "Microsoft", "Steve Ballmer"],
    conclusion="Steve Ballmer's interview reframes Microsoft Volume II: he claims credit for inventing enterprise sales after IBM divorced Microsoft over OS/2, and argues the DOJ era and flat stock masked a business that tripled revenue and planted Azure. The IBM PC DOS deal — non-exclusive licensing that let Compaq clone the platform — remains the origin of Microsoft's scale; Ballmer raised his hand when Bill Gates did not want to sell to CIOs. The enterprise agreement bundled Windows, Office, Exchange, Active Directory, and SQL Server with honor-system true-ups on zero-marginal-cost software — email pulled the suite. Misses on mobile, search, and social cost trillions elsewhere, but Ballmer holds ~4% of Microsoft (~$140B+) and funds USAFacts philanthropy largely from dividends. Intuit Dome applies the same competitive intensity: $2B privately funded arena, acre-scale halo board, home-court design tuned via analytics.",
    background="Ben and David sit with Steve Ballmer at Intuit Dome after he listened to their two-part Microsoft history. Ballmer frames himself as founder of Microsoft's enterprise business — a narrative rarely discussed despite Microsoft today being a ~$3.5T company driven by cloud and enterprise licensing.\n\nThe conversation walks from the IBM PC DOS licensing deal through the OS/2 divorce, Ballmer's shift from OS division to worldwide sales, invention of the enterprise agreement, the developers-developers-developers era, missed bets on mobile and search, Azure's incubation outside Server & Tools, and his decision to hold Microsoft stock after leaving. Ballmer also draws parallels between Microsoft culture and owning the LA Clippers.",
    important_facts=[
        "Microsoft's market cap is ~$3.5T when recorded; Ballmer credits the 1981 IBM PC non-exclusive DOS licensing deal — Microsoft kept rights to sell the OS to clone makers like Compaq — as the deal that kickstarted the company; IBM thought BIOS would protect them from platform disintermediation.",
        "After IBM kicked Microsoft out of the OS/2 collaboration (~1992), Ballmer raised his hand to build enterprise sales Bill did not want; Microsoft ended 1992 at ~$2.8B revenue selling through OEMs and retail with almost no CIO relationships — government was among the first enterprise customers.",
        "The enterprise agreement bundled Windows, Windows Server, Active Directory, Exchange, Office, and SQL Server; customers self-reported usage for true-ups; email was the wedge that pulled the full stack — software's zero marginal cost made 'include everything' rational.",
        "Ballmer cites mobile, search, and social as near-misses worth trillions; Google earned more search revenue per PC user than Microsoft by ~2005; Azure began as Ray Ozzie incubation separate from Server & Tools ~2006, years before Ballmer left in 2014.",
        "Ballmer remains Microsoft's largest individual shareholder (~4%, ~$140B+); he held through a decade of flat stock while tripling the business; Intuit Dome cost ~$2B with no public funding — Ballmer calls it a 'cathedral of basketball' with the world's largest indoor screen (~1 acre).",
    ],
    mental_model={
        "name": "Bundle at Zero Marginal Cost",
        "components": "Once Microsoft owned the PC platform via non-exclusive DOS licensing, the durable profit pool shifted to applications and enterprise suites sold on top. Ballmer's enterprise agreement exploited software economics: infinite inclusion at near-zero marginal cost, with true-ups capturing expansion. Email became the trojan horse — every CIO wanted reliable Outlook/Exchange, and the license carried the rest of the stack. The same logic later applied to cloud EAs, but Ballmer's era also shows the incumbent's curse: Windows franchise strength did not transfer to mobile or search, and Azure required a skunkworks because Server & Tools could not disrupt itself.",
        "application": "When evaluating platform companies, separate distribution power from adjacency success. Microsoft's OEM and EA channels were unbeatable for desktop and datacenter; bets outside that wedge (Nokia ~$7B, aQuantive, Yahoo) consumed cash without strategic credit. Ballmer argues two 'tricks' (enterprise + cloud/gaming) beat chasing four; for investors, his continued MSFT hold implies belief Azure and AI monetize seeds planted during the 'lost decade.'",
    },
    competitive_advantage="Ballmer-era Microsoft's enterprise advantage was contractual and architectural, not product delight. Active Directory, Exchange, Office, and Windows interlocked — switching one piece meant re-platforming identity, mail, and documents. Enterprise agreements with all-you-can-eat licensing and true-ups made Microsoft the default expand vendor; competitors sold point products while Meditech-style best-of-breed stacks required integration tax.\n\nThe IBM divorce forced Microsoft to sell to CIOs directly; by the late 1990s the 'holy trinity' plus SQL Server ran the Fortune 500. OEM channel still fed consumer Windows share (>90% at peak), which made IE bundling decisive against Netscape — distribution beats feature parity when the platform owner competes.\n\nWeaknesses accumulated in parallel: stack ranking and internal gun-pointing culture, Longhorn/Vista execution failures, and consumer taste erosion while Google and Apple owned mobile and web developers. Ballmer acknowledges Azure's greatness early but the market did not believe until Satya Nadella's narrative reset.\n\nVersus AWS today, Microsoft's hybrid-cloud story and EA relationships remain switching-cost moats; versus Google in search or Meta in social, Microsoft simply arrived too late despite reasonable bets. Ballmer's Clippers ownership applies the same playbook: Intuit Dome's extreme home-court design (analytics-driven seating, visitor free-throw penalties) is competitive advantage as physical product.",
    key_insights=[
        {
            "view": "Ballmer founded Microsoft's enterprise business, not Bill.",
            "question": "Why did enterprise become Ballmer's job?",
            "answer": "Bill Gates loved platforms and developers but not CIO dinners. When IBM abandoned the OS/2 partnership (~1992), Microsoft still sold through OEMs and stores with ~$2.8B revenue and almost no enterprise relationships. Ballmer volunteered to 'go figure out what IBM does' — building sales muscle ahead of need, per his weight-room metaphor. The enterprise agreement, Exchange-led suite, and EA true-ups were his invention; Windows 95's consumer halo obscured that the profit engine was shifting to IT departments.",
        },
        {
            "view": "The IBM DOS deal was history's greatest licensing transaction.",
            "question": "Why did IBM give away the platform?",
            "answer": "IBM wanted language tools and an OS for the PC; Gary Kildall's CP/M path failed and Microsoft delivered DOS it did not yet fully own (QDOS). IBM insisted on non-exclusive rights — thinking BIOS lock-in would protect them — so Compaq and clones could ship DOS-compatible machines. Application developers standardized on DOS, then Windows, accruing network effects to Microsoft instead of IBM. IBM saw protection in hardware; Microsoft captured the software layer that became a ~$3.5T company.",
        },
        {
            "view": "Azure succeeded because it bypassed Server & Tools.",
            "question": "Why incubate cloud outside the server division?",
            "answer": "Ray Ozzie's Azure team (~2006) sat apart from the profitable Server & Tools business — the same pattern Ballmer wishes mobile had followed. Incumbents protect cash cows; Windows Server developers were not the web's future. Ballmer left in 2014; Satya inherited Azure already cash-flowing billions. The interview implies organizational separation matters more than capital when disrupting yourself.",
        },
        {
            "view": "Ballmer's 'lost decade' tripled the business anyway.",
            "question": "Why was the stock flat if revenue grew?",
            "answer": "Ballmer took over near an ~80x earnings peak during the dot-com bubble, DOJ breakup order, and options-expensing overhang. Revenue and profits roughly tripled 2000–2014, but multiple compression offset gains — plus consumer narrative focused on Zune, Bing, and Windows Phone misses. Ballmer argues Wall Street never heard the enterprise/Azure story; Satya's 'mobile-first, cloud-first' repetition fixed messaging, not fundamentals.",
        },
        {
            "view": "Two tricks beat four for mega-cap tech.",
            "question": "Which miss bothers Ballmer most?",
            "answer": "Mobile and search — Google monetized PC users better than Microsoft by ~2005; iPhone (2007) and Android captured the next platform. Ballmer wanted Facebook (~2008) but structure and price failed; social trillion-dollar outcomes happened outside Redmond. He counts Xbox/NVIDIA-scale gaming as a full 'trick' and Azure as the second; consumer failures did not destroy enterprise + cloud optionality — reason he never sold MSFT.",
        },
    ],
    top_investment_implications=[
        {
            "ticker": "MSFT",
            "direction": "Long",
            "confidence": "High",
            "thesis": "Ballmer's hold (~4%, ~$140B+) reflects belief that enterprise EA seeds and early Azure bets compound under Nadella; ~$3.5T market cap validates cloud + AI narrative on infrastructure he helped fund — not a consumer-success story but a distribution-and-suite story.",
        },
    ],
    golden_quotes=[
        "\"Microsoft is the most valuable company in the world, almost $3.5 trillion — and it's an enterprise company, and that's largely thanks to you\" — David opening the Ballmer interview frame.",
        "\"The licensing of Microsoft DOS… is the single greatest business deal in history\" — Ben on the IBM PC non-exclusive agreement that standardised DOS for clone makers.",
        "\"Strategy follows structure\" — Ballmer's weight-room metaphor for building enterprise muscle before IBM forced the divorce.",
    ],
    chronology={
        "subject": "Steve Ballmer · Microsoft Enterprise",
        "events": [
            {"date": "1980", "event": "Ballmer joins Microsoft as employee #30; IBM PC partnership negotiations begin"},
            {"date": "1981", "event": "Non-exclusive DOS licensing deal signed with IBM for the PC"},
            {"date": "1985–89", "event": "OS/2 collaboration with IBM; Windows as parallel Plan B"},
            {"date": "1992", "event": "IBM divorces Microsoft on OS/2; Ballmer shifts to build enterprise sales"},
            {"date": "1992–98", "event": "Enterprise agreement era — Exchange, Active Directory, Office suite 'lift-off'"},
            {"date": "1998", "event": "Ballmer becomes president; DOJ antitrust trial begins"},
            {"date": "2000", "event": "Ballmer CEO; Judge Jackson orders breakup (later reversed)"},
            {"date": "2007", "event": "iPhone launch; Microsoft mobile/search bets fail to win platform"},
            {"date": "2006–08", "event": "Azure incubation under Ray Ozzie, separate from Server & Tools"},
            {"date": "2013", "event": "Ballmer announces retirement; board lacks support for Nokia acquisition"},
            {"date": "2014", "event": "Satya Nadella CEO; Ballmer exits operating role"},
            {"date": "2014–15", "event": "Ballmer buys LA Clippers; begins Intuit Dome project (~$2B)"},
            {"date": "2024–25", "event": "Microsoft ~$3.5T; Ballmer still largest individual shareholder; Intuit Dome opens"},
        ],
    },
    review_notes="Manual GPT Acquired batch v2 — template v5.1-acquired",
)

# --- acq-epic-systems-mychart ---
EPISODES["acq-epic-systems-mychart"] = base(
    "acq-epic-systems-mychart",
    episode_rating={"overall": 5},
    keywords=["Electronic Health Records", "Judy Faulkner", "Vertical Software"],
    conclusion="Epic Systems is a privately held Wisconsin company whose Chronicles single-database architecture powers MyChart for roughly 280M+ patient records and ~45% of Americans. Judy Faulkner raised only $70K equity plus $70K debt in 1979; the company now does ~$5.7B revenue with almost no customer churn. Competitors glued billing and clinical systems via M&A; Epic built Resolute, EpicCare, and hundreds of modules on one database — reliability for hospitals that cannot tolerate data gaps. Policy tailwinds from Medicare/Medicaid (1965) and ARRA HITECH (2009) forced digitization; Epic won Cerner at DOD/VA (~$16B) and dominates academic medical centers. Ben and David estimate $100B+ private value; GE, Microsoft, and Google courted acquisitions that will never close. AI ambient documentation (Microsoft/Nuance) partners through Epic's choke-point role.",
    background="Ben and David trace Epic from Judy Faulkner's 1943 birth through MUMPS/Chronicles in 1970s Wisconsin, the 1979 founding as Human Services Computing, and decades of slow growth until GUI EpicCare (1992) and Resolute billing aligned clinical and revenue cycles on one database.\n\nAmerican healthcare's policy architecture — employer-sponsored insurance, Medicare documentation requirements, Meaningful Use incentives — created demand for integrated EMR plus billing. Epic's refusal of venture capital, campus hiring from Midwest universities, and customer-never-lost culture produced a vertical software monopoly Ben calls the most successful female-founded company in history.",
    important_facts=[
        "Epic holds ~280M patient records (~45% of Americans); ~47 years without losing a customer (one returned after six months); privately held with Judy Faulkner and family foundation owning ~half — GE, Microsoft, and Google acquisition interest consistently rejected.",
        "Total funding: $70K equity (50% dilution on $70K raise) plus $70K bank debt in 1979 on a Data General minicomputer (~$70K); revenue today ~$5.7B; Ben and David estimate minimum private value ~$100B with Judy as likely most successful female entrepreneur by wealth created.",
        "Chronicles single-database architecture (MUMPS/Caché lineage from 1960s Mass General) means all modules — EpicCare clinical, Resolute billing, Cadence scheduling, MyChart patient portal — read/write one database; competitors often run separate acquired billing vs EMR systems.",
        "Healthcare is ~18% of US GDP; Ben cites ~$800B annual waste (~30% of spend); ARRA HITECH (~$30B incentives) and 2009–2015 Meaningful Use drove hospital IT spend; Epic won ~$16B Cerner DOD/VA contract (2022) after decades of government losses to Cerner.",
        "Epic employs ~15,000+ in Verona, Wisconsin; annual user-group meeting draws ~15,000; customers include Mayo, Kaiser, Cleveland Clinic, Johns Hopkins; antitrust suits (e.g., Particle Health) ongoing but Epic has never sued a customer.",
    ],
    mental_model={
        "name": "Single Database Vertical Suite",
        "components": "In vertical market software for high-stakes workflows, depth beats breadth: one database eliminates sync failures between clinical and billing events — patient harm and revenue leakage follow data gaps. Epic listened to hospital CIOs/CFOs, not doctors' UX preferences alone. Policy sticks (Medicare audits, standardized claims) made integrated records mandatory; Epic's slow capital-efficient build (Judy as generational programmer) outlasted roll-up competitors. Zero churn plus enterprise license expansion mirrors Microsoft's EA playbook in one industry.",
        "application": "Evaluate vertical SaaS on integration depth and switching costs, not UI scores. Epic wins when the buyer is the institution, not the clinician. AI ambient scribes succeed only with Epic partnership — Epic decides which innovations reach physicians. Private-market buyers at $100B bet on install-base growth and module upsell, not new logos.",
    },
    competitive_advantage="Epic's moat is architectural monolithism in a regulated vertical. Cerner (Oracle), Meditech, and others assembled suites via acquisitions; clinical and billing data often disagree. Epic's Resolute (1987) and EpicCare GUI (1992) on Chronicles mean scheduling, clinical documentation, and claims share one truth — hospitals buy reliability when lives and reimbursements depend on it.\n\nPolicy reinforces stickiness: post-1965 Medicare required standardized documentation; HITECH paid hospitals to adopt certified EMRs Epic dominated among large IDNs and academic centers. Switching costs span decades of workflow customization, staff training, and interface investments — CIOs call Epic the 'choke point' for hospital software innovation.\n\nJudy's anti-VC stance preserved founder control and long-term R&D (Cosmos research network, MyChart consumer scale). Campus recruiting from Wisconsin/Midwest schools created a loyal, non-Silicon-Valley engineering culture. Weaknesses: clinician UX criticism, international lower willingness-to-pay, and interoperability pressure — though Epic uses the Microsoft playbook of bundling point solutions into the EA.\n\nVersus horizontal platforms (Microsoft Office model), Epic proves vertical integration wins when failure modes are catastrophic and payers (Medicare, insurers) demand auditability.",
    key_insights=[
        {
            "view": "Epic wins because billing and clinical share one database.",
            "question": "Why not best-of-breed like other industries?",
            "answer": "Bad data flow kills patients and claims. Competitors' billing systems often came from separate M&A — integration gaps cause revenue cycle errors and clinical risk. Epic's 1970s Chronicles insight was one patient model at center; Resolute, Cadence, and EpicCare are views on same data. In vertical software with regulatory sticks, integrated beats modular when discontinuity is unacceptable.",
        },
        {
            "view": "Judy Faulkner is the most successful female founder in history.",
            "question": "How did capital structure enable that?",
            "answer": "Only $70K raised in 1979 — Judy kept ~half the company and never took VC that fired founders in that era. She learned business from Meditech's Neil Pappalardo (programmer-CEO) not MBA 'suits.' Generational programming talent (Bill Gates parallel) let Epic build with tiny headcount for years — $1.5M revenue after decade one, then GUI/PC era acceleration without dilution.",
        },
        {
            "view": "Policy created the EMR market; Epic captured the upmarket.",
            "question": "Why Singapore in every healthcare research joke?",
            "answer": "US healthcare economics are policy-driven: 1942 wage controls spawned employer insurance; 1965 Medicare/Medicaid required auditable records; 2009 HITECH spent ~$30B forcing digitization. Epic targeted complex academic hospitals needing Unix/minicomputer infrastructure first, then rode mandates to community hospitals. Understanding US health policy is prerequisite to understanding Epic's TAM.",
        },
        {
            "view": "Epic is enterprise sales on steroids with zero churn.",
            "question": "What makes hospital sales different?",
            "answer": "Multi-year cycles, buyer (CIO/CFO) ≠ user (doctor), no credit-card PLG. Epic's annual UGM (~15K attendees) and dedicated account teams mirror extreme enterprise motion. Once live, modules expand within the EA-like license; no customer left in 47 years because switching re-platforms the hospital's operational brain.",
        },
        {
            "view": "AI must go through Epic to reach doctors.",
            "question": "Is Epic a platform yet?",
            "answer": "Epic historically built everything in-house but partners on ambient AI (Microsoft/Nuance DAX) while controlling hospital distribution. CIOs describe a future where EHR fades to background AI OS — speculative, but Epic's gatekeeper role means startups need Epic approval to reach physicians at scale. Antitrust tension (Particle Health suit) reflects that power.",
        },
    ],
    top_investment_implications=[
        {
            "ticker": "MSFT",
            "direction": "Watch",
            "confidence": "Medium",
            "thesis": "Microsoft/Nuance ambient clinical AI reaches hospitals primarily via Epic partnership — Epic's choke point amplifies MSFT healthcare AI TAM without owning the EHR; watch Nuance DAX adoption through Epic install base.",
        },
        {
            "ticker": "ORCL",
            "direction": "Watch",
            "confidence": "Low",
            "thesis": "Oracle owns Cerner after ~$28B acquisition but Epic won DOD/VA (~$16B) and dominates large IDNs; Cerner integration risk leaves Oracle playing catch-up in the highest-acuity US hospital segment.",
        },
    ],
    golden_quotes=[
        "\"They have never lost a customer\" — Ben and David on Epic's 47-year retention (one six-month exception).",
        "\"$70,000 of equity capital and $70,000 of bank debt\" — total outside funding for a company doing ~$5.7B revenue today.",
        "\"If somebody offered you shares in Epic at $100 billion, would you pay it?\" — David's rubric; both hosts say yes for profit distributions.",
    ],
    chronology={
        "subject": "Judy Faulkner · Epic Systems",
        "events": [
            {"date": "Aug 1943", "event": "Judy Faulkner born in New Jersey; father runs pharmacy/soda fountain"},
            {"date": "1960s", "event": "Studies math/programming; Computers in Medicine course at Wisconsin with Dr. Slack"},
            {"date": "1970s", "event": "Builds Chronicles single-database EMR at Wisconsin medical center"},
            {"date": "1979", "event": "Human Services Computing founded; $70K equity + $70K debt raised"},
            {"date": "1983", "event": "Renamed Epic Systems; 9 customers, ~$1.5M revenue by 1988"},
            {"date": "1987", "event": "Resolute billing module launches on Chronicles"},
            {"date": "1992", "event": "EpicCare — first GUI ambulatory EMR in industry"},
            {"date": "2000s", "event": "MyChart patient portal scales; campus hiring model matures"},
            {"date": "2009", "event": "HITECH Act Meaningful Use incentives drive hospital EMR adoption"},
            {"date": "2010s", "event": "Cosmos research network; dominant share at top US hospital systems"},
            {"date": "2022", "event": "Epic wins ~$16B DOD/VA contract over Cerner"},
            {"date": "2025", "event": "~$5.7B revenue; ~280M patient records; still private, Judy still CEO"},
        ],
    },
    review_notes="Manual GPT Acquired batch v2 — template v5.1-acquired",
)

EPISODES["acq-indian-premier-league-cricket"] = base(
    "acq-indian-premier-league-cricket",
    episode_rating={"overall": 4},
    keywords=["IPL", "BCCI", "Lalit Modi"],
    conclusion="The Indian Premier League turned cricket into a franchise sports product by concentrating BCCI commercial rights and borrowing American league design. Lalit Modi raised Sahara's kit sponsorship from ~$100K/year to ~$105M/year (~$1M per match day) within months of joining the board, then re-bid TV rights from ~$10–15M to ~$500M over four years (~$125M/year). IPL's 2008 launch used city franchises (minimum ~$50M over 10 years), player auctions, cheerleaders, and Bollywood ownership to expand beyond Test-match purists to women and children — essential when India's 2008 ad market was only ~$2–3B total. Franchise values reached ~$1B+; media deals escalated to ~$6B for 2023–27. Ben and David frame IPL as Lalit's commercialization of latent demand in a cricket-obsessed nation whose middle class grew from ~2M earning >$10K in the early 1990s to ~550M today.",
    background="Ben and David open in Singapore — shorthand that US healthcare research ends where Singapore's system begins — then pivot to cricket's religious status in India (~93% of sports viewing hours vs NFL ~37% in America).\n\nThey trace BCCI's historically under-monetized national team (Sahara paid ~$100K/year for jersey rights on ~105 match days), Lalit Modi's 2005–08 sponsorship and broadcast resets, and IPL's 2008 franchise auction engineered with Shah Rukh Khan's Kolkata Knight Riders as anchor tenant. The episode compares IPL to NBA/NFL structure while noting India's unique ad-market constraints and Bollywood integration.",
    important_facts=[
        "Cricket holds ~93% of sports viewing hours in India vs ~37% for NFL in America; BCCI national team plays ~105 days/year — Sahara paid ~$100K/year for kit sponsorship before Lalit Modi renegotiated to ~$105M/year (~$1M per match day) in 2005.",
        "Nike won Indian cricket shoe/apparel rights at ~$52M/year via sealed-bid press event; combined with Sahara, Lalit generated ~$150M/year in sponsorships within two months of joining BCCI — vs prior ~$10–15M total annual TV rights.",
        "Star TV paid ~$500M for four-year broadcast rights (~$125M/year) after Lalit terminated Murdoch's ~$10–15M/year deal; mid-2000s BCCI revenue reached ~$200M+/year from near-zero within a decade.",
        "IPL 2008 franchise auction: minimum reserve ~$50M payable over 10 years (~$5M year-one cash); Shah Rukh Khan's Kolkata franchise ~$75M bid; player auction and T20 format targeted women/children beyond traditional Test audience.",
        "India's 2008 total ad market ~$2–3B — IPL broadcasters needed ~5–10% of all national advertising to break even on ~$150M/year rights; franchise values later exceeded ~$1B; 2023–27 media rights ~$6B (~$1.2B/year).",
    ],
    mental_model={
        "name": "Monetize the National Team First",
        "components": "BCCI owned the scarce asset — Indian cricket attention — but left billions on the table through gentleman-amateur pricing ($20K per race fee era parallels). Lalit treated sponsorship and broadcast like American sports leagues: competitive bidding, media events, and price resets. IPL layered franchise equity, salary caps, and entertainment packaging atop bilaterals already sucking ad budgets dry. Without BCCI cash flow, IPL franchises could not afford star salaries or stadium debt.",
        "application": "In emerging-market sports media, measure latent attention vs monetization gap. When national inventory is underpriced, the governing body can 10x rights before inventing new formats — but new leagues must find incremental ad dollars (women/children) when core budgets are exhausted. Franchise model transfers capex to billionaires while BCCI keeps central media upside.",
    },
    competitive_advantage="IPL competes for Indian attention against Bollywood and bilateral Tests, not other cricket leagues initially. BCCI's monopoly on elite Indian players and calendar control lets IPL slot T20 windows without rival national commitments. Franchise brands (KKR, Mumbai Indians, CSK) built local fandom via Bollywood owners, city identity, and star auctions — cricket version of NBA draft drama.\n\nT20 format lowered time commitment vs five-day Tests; cheerleaders, music, and night matches imported American spectacle without copying baseball's pastoral tone. Lalit's sealed-envelope auctions created price transparency that embarrassed incumbents into paying market rates.\n\nWeaknesses: governance scandals (Lalit expelled), franchise debt from player salary inflation, and dependence on broadcasters profiting from cricket-specific ad sales in thin national ad pools. No global competitor matches India's cricket obsession scale — IPL's advantage is national cultural monopoly plus BCCI governance of talent supply.\n\nVersus NFL/NBA, IPL skipped decades of under-monetization in one Lalit-era step function; versus other cricket leagues (Big Bash, CPL), IPL has largest talent pool, richest franchises, and first-mover on Indian T20 fandom.",
    key_insights=[
        {
            "view": "BCCI was the most under-monetized asset in global sports.",
            "question": "How bad was old pricing?",
            "answer": "Negotiations started at ~$10–20K per race-equivalent match fees; Sahara paid ~$100K/year for ~105 national team days — pennies for ~93% national sports attention share. Lalit treated this as arbitrage: same inventory, competitive auctions, press-conference theater. Within months sponsorship alone exceeded prior total BCCI revenue — proof attention ≠ revenue without commercial operator.",
        },
        {
            "view": "IPL needed new audiences because BCCI drained ad budgets.",
            "question": "Why target women and children?",
            "answer": "Lalit's quote: after raising BCCI aggregate rights toward ~$1B potential, 'all the money in the market was consumed.' India's 2008 ad TAM ~$2–3B; assigning ~$150M/year broadcast meant needing ~5–10% of every ad rupee. T20 + Bollywood + entertainment expanded cricket beyond male Test purists — incremental inventory, not substitution.",
        },
        {
            "view": "Franchise auctions transferred risk to local tycoons.",
            "question": "How did Shah Rukh Khan get a team?",
            "answer": "Lalit set ~$50M minimum reserve over 10 years with ~$5M year-one payment — affordable headline for celebrities. Khan's ~$75M Kolkata bid anchored legitimacy; owners accepted years of losses on player salaries for brand/status. Same playbook as American sports: league collects central media, franchises eat operating losses for asset appreciation (~$1B+ values later).",
        },
        {
            "view": "Cricket's India scale exceeds any historical empire's reach.",
            "question": "How big is the middle class tailwind?",
            "answer": "Early 1990s ~2M Indians earned >$10K; today ~550M 'middle class' ($7K–$45K) — 31% of population, larger than entire US. ~250M lifted from poverty 2015–today. Cricket monetization rode consumer spending and mobile TV growth; IPL timing matched inflection, not just format innovation.",
        },
        {
            "view": "Competitive balance requires obsessive league design.",
            "question": "Why salary caps and auction rules matter?",
            "answer": "IPL mixes American franchise mechanics (salary cap, auctions, revenue share) with cricket-specific constraints — preventing dynasties while keeping star movement for drama. Owners spend hundreds of millions on players while often running teams at loss — league must engineer parity or fan interest collapses in small-city franchises.",
        },
    ],
    top_investment_implications=[
        {
            "ticker": "Private:BCCI/IPL",
            "direction": "Watch",
            "confidence": "Medium",
            "thesis": "Central media rights (~$6B 2023–27) and ~$1B+ franchise values reflect India's ad-market growth; no pure-play public equity — watch Disney/Star successor and franchise-adjacent consumer brands benefiting from cricket attention monopoly.",
        },
    ],
    golden_quotes=[
        "\"Cricket is 93% of sports watched in India\" — contextualizing BCCI's under-monetization vs American sports share.",
        "\"I had already sucked that money out… I needed women and children\" — Lalit Modi on why IPL needed new audiences after BCCI bilaterals consumed ad budgets.",
        "\"Minimum bid is $500 million for four years\" — Lalit terminating Murdoch's Star deal to re-auction broadcast rights.",
    ],
    chronology={
        "subject": "BCCI · Indian Premier League",
        "events": [
            {"date": "1990s", "event": "BCCI earns ~$10–15M/year TV; kit deals ~$100K/year amid cricket mania"},
            {"date": "2005", "event": "Lalit Modi joins BCCI; Sahara deal rises to ~$105M/year"},
            {"date": "2005–06", "event": "Nike wins apparel rights ~$52M/year via public sealed bids"},
            {"date": "2006–08", "event": "Star TV rights rebid ~$500M/4 years; BCCI revenue ~$200M+/year"},
            {"date": "Feb 2008", "event": "IPL franchise auction; Kolkata ~$75M; T20 league announced"},
            {"date": "Apr 2008", "event": "IPL inaugural season launches with city franchises and player auction"},
            {"date": "2010s", "event": "Franchise values soar; Bollywood/corporate ownership normalizes"},
            {"date": "2013–15", "event": "Lalit Modi scandal and exile; governance reforms debated"},
            {"date": "2023", "event": "Media rights ~$6B for five years (~$1.2B/year)"},
            {"date": "2025", "event": "Franchise valuations ~$1B+; IPL central to Indian sports economy"},
        ],
    },
    review_notes="Manual GPT Acquired batch v2 — template v5.1-acquired",
)

from _batch2_episodes_rest import REST  # noqa: E402

EPISODES.update(REST)

if __name__ == "__main__":
    for eid, data in EPISODES.items():
        path = APPROVED / f"{eid}.json"
        path.write_text(json.dumps(data, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
        print(f"wrote {path.name}")

