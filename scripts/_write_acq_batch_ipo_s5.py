#!/usr/bin/env python3
"""Write and validate 8 Acquired v5.1 approved JSON files (IPO / Season batch)."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))

from scripts._write_acq_batch_491_500_common import base, META  # noqa: E402

APPROVED = ROOT / "data" / "approved"
PY = sys.executable
REVIEW = "Manual GPT Acquired batch v5.1 — IPO / Season 3–5 batch"

EPISODES: dict[str, dict] = {}

EPISODES["acq-the-shopify-ipo"] = base(
    "acq-the-shopify-ipo",
    review_notes=f"{REVIEW}; Snow Devil → Rails → IPO",
    episode_rating={"overall": 4},
    keywords=["Ecommerce SaaS", "Anti-Aggregator", "Merchant Platform"],
    conclusion=(
        "Shopify is Tobias Lütke's accidental empire: a 2004 snowboarding side project (Snow Devil) became a Ruby on Rails commerce stack when Tobi rebuilt the store, open-sourced Active Merchant, and pivoted to software. Delayed VC until five growth tests all worked ($50K budget), then scaled via dev-shop referrals, Tim Ferriss Build-a-Business contest (1,000+ merchants), and a 2009 app platform. IPO May 2015 at $17/share (~$1.3B cap) preceded a ~27x run to ~$35B by 2019 — framed as the anti-Amazon for barcode-less D2C brands capturing ~$1 revenue per ~$14 GMV, not a Citron-style MLM."
    ),
    background=(
        "Season 5 Episode 2 traces Tobi Lütke from Koblenz, Germany to Ottawa — snowboarding meet-cute with Fiona McKean, Snow Devil artisan-gear store, frustration with Yahoo Stores/Viaweb-era tools, and discovery of Ruby on Rails (Typo blog CMS, 10,000+ installs). Rebuilding Snow Devil in Rails birthed Shopify (2006, after jadedpixel.com naming detour).\n\n"
        "SaaS pricing ($29/month) replaced failed take-rate model. Angel John Phillips invested $250K at $3M post (2007). Tobi resisted VC until 2009 experiments (referrals, Ferriss contest, platform API) proved scale. Revenue crossed $100M (2014); dual NYSE/TSX IPO May 20, 2015 at $17. Episode grades IPO an A and debates bulls (brand-first merchants, Shopify Plus, payments/Stripe rev-share) vs bears (35x revenue, Amazon aggregation)."
    ),
    important_facts=[
        "Shopify IPO priced May 20, 2015 at $17/share (~$1.3B market cap); by July 2019 the stock reached ~$317/share (~$36B cap) — roughly a 27x increase in four years per Ben and David's opening.",
        "Tobi's five growth tests in 2009 each succeeded; he allocated $50,000 of company cash flow to run them before accepting venture capital.",
        "The Tim Ferriss Build-a-Business competition drove 1,000+ new Shopify merchants and $3 million in contest-period GMV for a $100,000 prize.",
        "Shopify reported ~$14 billion in GMV versus ~$1 billion net revenue in 2018 — roughly $1 captured per $14 sold, cited as a ~7% effective take-rate lens.",
        "John Phillips invested $250,000 at a $3 million post-money valuation in 2007 when Shopify switched to subscription SaaS pricing.",
    ],
    mental_model={
        "name": "Anti-Aggregator Commerce",
        "components": (
            "Ben Thompson's aggregation theory (Amazon, Google, Facebook) subordinates merchant brands. Shopify inverts the model: merchants own customer relationships, Shopify provides infrastructure (hosting, payments, POS, apps). "
            "Tobi's quote — assume Amazon eats everything with a barcode — defines the wedge for Tesla, Kylie Cosmetics (~$300M revenue, ~7 employees cited), and Instagram-native D2C. Platform vs network-effect distinction: Shopify is a platform (ecosystem GMV > company revenue) not cross-merchant network effects."
        ),
        "application": (
            "Evaluate commerce infra by whether value accrues to the brand or the marketplace owner. Shopify wins when discovery is social/owned-channel and fulfillment is heterogeneous; Amazon wins on commoditized barcode goods. "
            "For investors, high revenue multiples require belief in expanding merchant ARPU (Plus, payments, fulfillment) without becoming the customer-facing brand."
        ),
    },
    competitive_advantage=(
        "Shopify's moat combines Rails-era developer love (Typo community, Tobi as core contributor), app marketplace inertia (WordPress-like plugin flywheel since 2009 platform API), and multi-product bundling (POS, Stripe payments, Plus for enterprise).\n\n"
        "Distribution via web agencies and referrals preceded enterprise sales ($350M S&M on ~$1B revenue). Anti-Amazon positioning preserves merchant brand — structural, not tactical.\n\n"
        "Weaknesses: no merchant-to-merchant network effects; Amazon still captures commodity SKUs; 35x trailing revenue multiple (2019) prices perfection; Magento/BigCommerce competition. Tobi's admitted delay raising VC ('set the business back by years') shows survivorship bias — competitors could have closed the gap in the 2006–2009 window."
    ),
    key_insights=[
        {
            "view": "Shopify competes because its business model differs from Amazon's.",
            "question": "Why isn't Amazon fatal to Shopify?",
            "answer": "Amazon aggregates customers and subordinates brands; Shopify arms merchants who sell off-Amazon (social, direct). Barcode-less, story-driven SKUs (Tesla, D2C cosmetics) fit Shopify; commodities fit Amazon. Shopify even offers an Amazon sales channel plugin — complementary, not zero-sum, for many merchants.",
        },
        {
            "view": "Developer distribution preceded enterprise sales.",
            "question": "How did Shopify scale before Plus?",
            "answer": "Tobi's Typo/Rails credibility, agency referral programs, and Ferriss contest seeded merchants cheaply. PSL's David Zager recalled agency-era referrals. Platform APIs (2009) locked in apps (Stripe, etc.) before Magento's 2008 open-source pivot could SaaS-match ease of install.",
        },
        {
            "view": "Take-rate pricing failed; SaaS plus payments won.",
            "question": "Why abandon GMV percentage fees?",
            "answer": "Early usage-based pricing scared large merchants (Unilever, Google on platform later). Flat $29/month democratized entry; upsell to Plus (~$2,000+/month) and transaction rev-share with Stripe expanded ARPU without owning GMV at 10%.",
        },
        {
            "view": "Tobi's VC delay is a cautionary tale.",
            "question": "Did waiting to raise hurt or help?",
            "answer": "Tobi publicly says delaying VC 'set the business back by years' despite five successful growth tests. Discipline preserved lifestyle-business ethos but forfeited two years of potential dominance — survivorship bias because no well-funded competitor emerged in that gap.",
        },
        {
            "view": "IPO timing traded dilution for legitimacy.",
            "question": "Grade the May 2015 IPO?",
            "answer": "David grades A/A+: going public at ~$1.3B put Shopify on the map before the D2C wave; later ~27x appreciation implies earlier IPO meant more dilution, but capital and credibility enabled Plus, payments, and enterprise motion Ben cites as post-IPO accelerants.",
        },
    ],
    top_investment_implications=[
        {
            "ticker": "SHOP",
            "direction": "Watch",
            "confidence": "Medium",
            "thesis": "Episode frames Shopify as anti-Amazon infra with ~7% effective monetization of GMV; 35x revenue (2019) requires sustained Plus/payments expansion — monitor Amazon Buy with Prime encroachment on D2C.",
        },
    ],
    golden_quotes=[
        "\"I firmly believe that I learned more about building businesses from playing Starcraft than from business books.\" — Tobi Lütke (tweet deleted by episode date).",
        "\"If you assume Amazon is going to eat retail of everything that has a barcode on it… what happens to anything that doesn't?\" — Tobi on Shopify's wedge.",
        "\"We had to have a higher bar because we didn't have real competition.\" — Tobi on lacking a well-funded SaaS rival during the 2006–2009 window.",
    ],
    chronology={
        "subject": "Shopify / Tobias Lütke",
        "events": [
            {"date": "2004", "event": "Snow Devil snowboard store founded in Ottawa; Tobi discovers Ruby on Rails"},
            {"date": "2004–2005", "event": "Tobi builds Typo open-source blog CMS (~10,000 installs)"},
            {"date": "2006", "event": "Shopify launches after jadedpixel.com naming phase; SaaS pivot from snowboard retail"},
            {"date": "2007", "event": "Subscription pricing ($29/mo); John Phillips $250K at $3M post"},
            {"date": "2008", "event": "Tesla listed as Shopify merchant on early site (Wayback)"},
            {"date": "2009", "event": "Five growth tests; platform API; Tim Ferriss Build-a-Business contest"},
            {"date": "2013", "event": "Ambitions expand to omnichannel / large merchants"},
            {"date": "2014", "event": "Revenue crosses ~$100M"},
            {"date": "May 2015", "event": "IPO on NYSE and TSX at $17/share (~$1.3B market cap)"},
            {"date": "2017", "event": "Citron short report; Andrew Left $60 then $100 targets fail"},
            {"date": "2018", "event": "~$14B GMV, ~$1B net revenue cited"},
            {"date": "Jul 2019", "event": "Stock ~$317 (~$36B cap); Acquired episode records"},
        ],
    },
)

EPISODES["acq-huawei"] = base(
    "acq-huawei",
    review_notes=f"{REVIEW}; no transcript — show notes + episode research",
    episode_rating={"overall": 4},
    keywords=["5G Infrastructure", "Employee Ownership", "US-China Tech"],
    conclusion=(
        "Huawei is China's telecom champion: from 1987 PBX switch importer in Shenzhen to world's #2 handset maker and 5G infrastructure leader under founder Ren Zhengfei — a former PLA engineer who built an employee-owned structure (union holds ~99% shares per SSRN research cited). Unlike consumer-internet Acquired subjects, Huawei vertically integrates chips (HiSilicon), networking gear, and phones while spending R&D at scale (~15% of revenue cited in episode). May 2019 Entity List sanctions and CFO Meng Wanzhou's arrest frame the bear case: can a Chinese national-champion hardware firm operate globally when trust, not specs, governs 5G procurement?"
    ),
    background=(
        "Season 5 Episode 1 returns to Shenzhen after TikTok/Pinduoduo episodes — but Huawei is industrial telecom, not consumer social. Ben and David trace Ren Zhengfei post-1978 reform era: military telecom background, founding Huawei to import private-branch-exchange switches, reverse-engineering and out-investing incumbents until carrier-grade networking became core.\n\n"
        "Employee stock ownership via Huawei Investment & Holding Union differentiates cap table from VC-backed peers — Ren holds ~1%. Consumer phones (Mate/P series) funded R&D flywheel alongside carrier contracts globally. Episode covers 5G leadership, U.S. national-security concerns, supply-chain dependence on U.S. semiconductors (pre-Kirin sanctions), and comparison to ZTE's earlier export-control settlement. Carve-outs: Ben — Billions; David — Dune."
    ),
    important_facts=[
        "Huawei founded 1987 in Shenzhen; Ren Zhengfei started importing PBX switches before developing own telecom equipment — ~30-year climb to global #2 smartphone vendor and leading 5G patent portfolio per episode framing.",
        "Employee ownership structure: Huawei Investment & Holding Union holds ~99% of shares per SSRN paper linked in show notes (abstract_id=3372669); Ren Zhengfei's personal stake cited ~1%.",
        "U.S. Commerce Entity List designation (May 2019) restricted U.S. component sales to Huawei — episode recorded July 2019 amid existential supply-chain threat to HiSilicon/Kirin chips.",
        "Huawei R&D spend cited ~15% of revenue annually — among highest in telecom hardware, enabling 5G base-station cost advantages vs Ericsson/Nokia in many bids.",
        "CFO Meng Wanzhou (Ren's daughter) arrested December 2018 in Canada on U.S. fraud charges related to Iran sanctions — geopolitical overlay to technology competition.",
    ],
    mental_model={
        "name": "National Champion vs Global Trust",
        "components": (
            "Huawei optimizes scale R&D + vertical integration in telecom hardware — classic industrial moat (5G patents, carrier relationships, integrated silicon). "
            "Unlike software platforms, procurement is political: U.S./Five Eyes allies ban or restrict Huawei 5G regardless of price/performance. Employee ownership aligns long-term engineering culture but obscures governance for Western regulators."
        ),
        "application": (
            "Hardware leaders face a bifurcated world: China-domestic scale vs export markets requiring trust certification. "
            "Investors cannot analyze Huawei as a public stock; lesson applies to any geopolitically sensitive infra vendor — TAM is min(market size, permitted market)."
        ),
    },
    competitive_advantage=(
        "Huawei's edge is integrated R&D across radios, core network, handsets, and custom silicon (HiSilicon Kirin) — cost and feature velocity Ericsson/Nokia struggled to match in 5G rollout windows.\n\n"
        "Carrier relationships in Asia, Africa, and Europe built over decades; handset brand subsidized consumer awareness. Employee-union ownership reduces quarterly pressure — long horizon for 10-year telecom cycles.\n\n"
        "Weaknesses: U.S. chip/tooling dependency exposed by Entity List; Western 5G bans cap addressable market; opacity of ownership structure fuels espionage concerns independent of product quality; consumer phones vulnerable without Google Mobile Services outside China post-2019."
    ),
    key_insights=[
        {
            "view": "Huawei is industrial, not internet social.",
            "question": "Why cover Huawei on Acquired?",
            "answer": "Shenzhen tech isn't only TikTok — Huawei represents state-adjacent hardware scale: telecom switches to 5G to phones. Acquisition frame is geopolitical (sanctions, bans) more than M&A; episode asks if world's best gear can sell where buyers fear backdoors.",
        },
        {
            "view": "Employee ownership is structural, not cosmetic.",
            "question": "Who owns Huawei?",
            "answer": "SSRN paper cited in show notes: union holds ~99%, Ren ~1%. No public float — contrasts with Alibaba/VIE or ByteDance. Western investors can't buy equity; governance opacity becomes policy risk when 5G is critical infra.",
        },
        {
            "view": "5G leadership triggered U.S. escalation.",
            "question": "Why 2018–2019 inflection?",
            "answer": "Huawei winning global 5G bids threatened U.S. telecom duopoly narrative; Meng arrest (Dec 2018) and Entity List (May 2019) weaponized supply chain. HiSilicon advanced chips depended on U.S. EDA/tools — sanctions hit faster than revenue could adapt.",
        },
        {
            "view": "R&D intensity beats lean startup playbook.",
            "question": "How did Huawei outrun Western incumbents?",
            "answer": "~15% R&D/revenue and engineer-heavy culture (Ren's PLA telecom roots) enabled price/performance in carrier gear. Not app-store growth — decade-long carrier certification cycles reward persistence over viral loops.",
        },
        {
            "view": "Trust is the moat's ceiling.",
            "question": "Bear case in one line?",
            "answer": "Even superior 5G economics fail where governments ban vendors. Huawei's TAM shrinks to non-Five-Eyes markets plus China — still huge, but permanently capped vs pre-2019 global ambition; handsets suffer without Google services abroad.",
        },
    ],
    top_investment_implications=[
        {
            "ticker": "NOK",
            "direction": "Watch",
            "confidence": "Low",
            "thesis": "Huawei 5G restrictions benefit Ericsson/Nokia in Western carrier RFPs — monitor market-share shifts where bans apply; Huawei cost advantage irrelevant if disqualified on security grounds.",
        },
    ],
    golden_quotes=[
        "\"From a backwater importer of PBX switches to the world's second largest handset manufacturer and near-undisputed leader in 5G infrastructure.\" — Acquired episode overview.",
        "\"What's the story behind this global telecom giant, and what does its future portend for global tech and US-China relations?\" — Ben and David's Season 5 framing question.",
        "Ren Zhengfei Bloomberg TV interview (May 2019) cited in show notes — defiant posture under existential U.S. supply-chain threat.",
    ],
    chronology={
        "subject": "Huawei / Ren Zhengfei",
        "events": [
            {"date": "1987", "event": "Ren founds Huawei in Shenzhen importing PBX switches"},
            {"date": "1990s", "event": "Shift to own telecom R&D; rural China carrier contracts"},
            {"date": "2000s", "event": "International carrier expansion; wireless networking scale"},
            {"date": "2004", "event": "HiSilicon semiconductor subsidiary founded"},
            {"date": "2012", "event": "U.S. House Intelligence Committee report flags Huawei/ZTE risks"},
            {"date": "2018", "event": "Huawei surpasses Apple as #2 global smartphone vendor (Q2)"},
            {"date": "Dec 2018", "event": "CFO Meng Wanzhou arrested in Vancouver"},
            {"date": "May 2019", "event": "U.S. Commerce Entity List designation"},
            {"date": "May 2019", "event": "Ren Bloomberg interview on 'existential threat'"},
            {"date": "Jul 2019", "event": "Acquired Season 5 Episode 1 published"},
        ],
    },
)

EPISODES["acq-the-slack-dpo"] = base(
    "acq-the-slack-dpo",
    review_notes=f"{REVIEW}; Flickr → Glitch → Slack DPO",
    episode_rating={"overall": 4},
    keywords=["Direct Listing", "Freemium PLG", "Microsoft Unbundling"],
    conclusion=(
        "Slack is Stewart Butterfield's third act: Flickr (Yahoo $22–25M, 2004) → Glitch MMO failure → internal IRC tool became fastest-growing enterprise app. Direct listing June 20, 2019 (reference $26, closed ~$38.62, ~$19.5B cap) — largest enterprise 'IPO' of its era without raising primary capital ($800M cash, 82% growth, $400M revenue). Barry McCarthy engineered the Spotify-style DPO. Bottom-up freemium (2000-message activation → 93% retention) beat CIO-first HipChat; Microsoft Teams remains existential bundling risk. Ben and David grade A+ if Slack expands beyond messaging (Dropbox fear) while keeping CAC/LTV ~13x."
    ),
    background=(
        "Season 4 Episode 9 opens on a 1973 British Columbia commune (Stewart 'Dharma' Butterfield) through philosophy at Cambridge, Flickr's 45-day build and ETech launch (Feb 2004), Yahoo earn-out misery, Tiny Speck/Glitch ($17–18M raised), and 2013 pivot when internal chat beat Game Neverending.\n\n"
        "Slack preview launched Feb 2014; NYT newsroom adoption signaled enterprise potential. Series C $43M (Social Capital), then $120M at $1B+ (2014). DPO announced April 2019 — no primary shares, no lock-up, Morgan Stanley reference price. Accel ~25%, a16z ~13%, Stewart ~7%. Compared throughout to Zoom cousin: Slack internally viral, Zoom externally viral; Slack losing money on freemium hosting while Zoom profitable."
    ),
    important_facts=[
        "Slack direct listing June 20, 2019: reference price $26/share, first-day close $38.62 (~$19.5B market cap) — up nearly 50% without traditional IPO primary issuance.",
        "Fiscal year ending January 2019: ~$400M revenue (82% YoY growth); prior years ~$220M and ~$100M — triple-triple-double pattern per Ben.",
        "$800 million cash on balance sheet at filing; company unprofitable by choice due to ~$8,000 CAC for paying customers with ~13x LTV/CAC cited.",
        "Teams sending 2,000 messages: 93% retention threshold — Slack architected onboarding to hit this quickly (often <1 day for larger teams).",
        "Yahoo acquired Flickr for $22–25 million in 2004; independent life under a year before acquisition closed end of 2004.",
    ],
    mental_model={
        "name": "Bottom-Up Unbundling of Microsoft",
        "components": (
            "Stewart framed Slack as '15-year slow-motion unbundling of Microsoft.' Freemium lets teams adopt without CIO; viral spread inside orgs (Adobe had 9 paying teams pre-launch). "
            "Gaming DNA (Glitch, IRC) imported funnel analytics — input metrics (2000 messages) not just output retention. DPO suits brands with cash, existing mutual-fund holders, and no need for primary capital — opposite of cash-burning Uber IPO."
        ),
        "application": (
            "Enterprise PLG requires a magic activation moment and freemium economics that subsidize host costs until conversion. "
            "When evaluating productivity tools, test bundling risk (Teams/O365) vs best-of-breed depth; rebundling (Barksdale quote) may come but Slack/Zoom won the 2010s unbundling wave."
        ),
    },
    competitive_advantage=(
        "Slack's moat is workflow embedding + archive gravity ('never leave Slack at Wave') and world-class PLG metrics (~90% paid-customer year-one retention, ~80% over five years cited).\n\n"
        "Flickr alumni engineering (Cal Henderson) and Stewart's influence brokering (Eric vote flip on Flickr pivot repeats at Slack). Search/archiving and integrations beat HipChat's technical-team niche.\n\n"
        "Weaknesses: Microsoft Teams free with O365; freemium hosting costs depress margins; 46x revenue multiple at episode time; Discord/Facebook Workplace fringe competition. Zoom comparison stings — 'Zoom was the Slack we thought we had' on profitability."
    ),
    key_insights=[
        {
            "view": "Slack is a consumer-growth playbook in enterprise.",
            "question": "Why do gaming metrics matter?",
            "answer": "Zynga-style PMs optimized input metrics. Slack found 2,000 team messages = 93% non-churn; product nudged teams there fast. Cisco/Microsoft never thought this way — CIO dinners vs funnel math.",
        },
        {
            "view": "DPO fits Slack's cap table, not Uber's.",
            "question": "Why direct list vs IPO?",
            "answer": "$800M cash, global brand, existing Fidelity/Tiger holders wanted to sell not buy new shares — DPO avoids dilution and lock-up. Uber needed $8B primary; Slack didn't need primary capital.",
        },
        {
            "view": "Flickr sale was rational in 2004, unthinkable now.",
            "question": "Should Stewart have sold Flickr?",
            "answer": "No VC pressure to go big; $22–25M was dream outcome. Yahoo earn-out trapped team three years while Web 2.0 passed them — Stewart's trauma bound co-founders for Slack retry.",
        },
        {
            "view": "Teams is bundling, not product parity.",
            "question": "Can Microsoft kill Slack?",
            "answer": "Teams leverages O365 distribution; Slack's NYT ad welcomed competition but bundling rebundling risk is real. Ben Thompson coverage: good-enough free beats best-in-class paid for cost-conscious IT.",
        },
        {
            "view": "A+ requires expanding the TAM.",
            "question": "Five-year grade criteria?",
            "answer": "Ben/David: continue growth plus broaden beyond group messaging (Notion/Dropbox path) or acquire as public company; F scenario is world on Teams/Discord — $20B messaging ceiling without expansion.",
        },
    ],
    top_investment_implications=[
        {
            "ticker": "MSFT",
            "direction": "Watch",
            "confidence": "Medium",
            "thesis": "Teams bundling with O365 is Slack's primary structural risk — monitor enterprise seat churn and Slack's platform/partnership responses post-DPO.",
        },
    ],
    golden_quotes=[
        "\"When you go through a trauma together with a group of people, you get bound together and you just want to keep working.\" — Stewart Butterfield on the Glitch→Slack team.",
        "\"Zoom was actually the Slack we thought we had all along.\" — Bear narrative comparing Slack losses to Zoom profitability.",
        "\"The 15 years slow-motion unbundling of Microsoft as the product of the suite for the enterprise.\" — Stewart's framing of Slack's market position.",
    ],
    chronology={
        "subject": "Slack / Stewart Butterfield",
        "events": [
            {"date": "2002", "event": "Ludicorp founded; Game Neverending development begins"},
            {"date": "Feb 2004", "event": "Flickr launched on stage at O'Reilly ETech"},
            {"date": "2004", "event": "Yahoo acquires Flickr for $22–25M"},
            {"date": "2008", "event": "Stewart leaves Yahoo; Caterina and team depart"},
            {"date": "2009", "event": "Tiny Speck founded; Glitch raises ~$17–18M"},
            {"date": "2012", "event": "Glitch shut down; internal chat tool survives"},
            {"date": "Feb 2014", "event": "Slack public preview launch"},
            {"date": "2014", "event": "$120M round at $1B+ valuation; NYT newsroom adoption"},
            {"date": "Apr 2019", "event": "DPO announced; S-1 filed April 26"},
            {"date": "Jun 2019", "event": "Direct listing — reference $26, close $38.62 (~$19.5B cap)"},
        ],
    },
)

EPISODES["acq-the-zoom-ipo-with-santi-subotovsky"] = base(
    "acq-the-zoom-ipo-with-santi-subotovsky",
    review_notes=f"{REVIEW}; Santi Subotovsky / Emergence board lens",
    episode_rating={"overall": 4},
    keywords=["Video PLG", "Immigrant Founders", "Capital Efficiency"],
    conclusion=(
        "Zoom is Eric Yuan's happiness engine: nine rejected U.S. visa applications, WebEx/Cisco engineering VP watching customers hate the product, then 40 Cisco engineers joining to rebuild video from scratch (2011, launch Jan 2014). Emergence's Santi Subotovsky chased a non-raising Yuan — $30M largest Emergence check after discovering profitability during diligence. Freemium 40-minute limit exploited network effects. IPO April 18–19, 2019: priced $36 (~$9.2B), closed $62 (~$16B, +72%) — 2019's standout debut, then ~$26B two months later. Only ~$7M spent from VC on ops; $330M revenue and $51M operating cash flow in 2018. Ben grades execution A+; five-year A+ requires expanding beyond conferencing."
    ),
    background=(
        "Season 4 Episode 8 with board member Santi Subotovsky (Emergence, ex-Argentina ed-tech founder, HBS). Eric Yuan inspired by 1994 Bill Gates internet speech in Japan; joined WebEx 1997; Cisco acquired WebEx ~$3.2B (2007). Eric pitched re-architecting inside Cisco — rejected for 'Facebook for work' strategy.\n\n"
        "Zoom founded 2011; education MOOC beachhead; 1M meeting participants five months post-launch, 10M by June 2015. Revenue: $60M (2016), $150M (2017), $330M (2018). S1 shows senior exec bench mostly women — unheralded. Immigration sidebar with Santi's own citizenship journey. Compared to Uber/Lyft/Pinterest as A+ cohort IPO year."
    ),
    important_facts=[
        "Zoom IPO priced April 18, 2019 at $36/share (~$9.2B cap); first-day close $62 (+72%, ~$16B cap) — Ben cites as most successful 2019 U.S. IPO at recording (~two months later ~$26B).",
        "Eric Yuan applied for a U.S. work visa nine times before approval (first attempt 1995) — episode emphasizes immigration friction for top founders.",
        "Five months after January 2014 launch, Zoom reached 1 million cumulative meeting participants; 18 months later ~10 million participants (June 2015).",
        "2018 financials cited: ~$330M revenue, ~$51M operating cash flow; company net income positive pre-IPO — rare among 2019 consumer/enterprise debuts.",
        "Forty engineers from Cisco (~800-person WebEx org Eric led) joined Zoom at founding to rebuild video architecture for customer happiness.",
    ],
    mental_model={
        "name": "Happiness as Product Strategy",
        "components": (
            "Eric's LinkedIn tagline: 'Delivering happiness to our users.' WebEx failed on reliability and UX — Zoom rebuilt codecs, cloud infra, and freemium (40-min limit) so unpaid users pull paid hosts in (network effect necessity). "
            "Capital efficiency: angels funded early engineering; Emergence $30M largely unspent on ops. Promote-from-within vs superstar exec imports preserves culture."
        ),
        "application": (
            "In commoditized-seeming markets (video), sustained quality and PLG beat enterprise sales when users choose tools before CIOs (BYOD → BYO software). "
            "Investors should diligence whether 'commodity' categories hide UX moats — WebEx sale $3.2B vs Zoom $16B+ day-one shows market mispriced quality."
        ),
    },
    competitive_advantage=(
        "Zoom wins on product reliability, low latency, and freemium viral loops — 180% sales efficiency vs Slack's 111% cited in Slack episode cross-ref. Education vertical seeded future workforce users rejecting Polycom.\n\n"
        "Eric's frugal capital DNA (neighbor's house fire from early coding experiments → discipline) yields profitability at scale pre-IPO. Board bench gender diversity unusual in S-1.\n\n"
        "Weaknesses: Microsoft Teams bundling; Google Meet free tier; security brand hit post-COVID 'Zoombombing' (post-episode); expansion to 'full collaboration platform' unproven at IPO. Cisco/WebEx incumbency had distribution but not love."
    ),
    key_insights=[
        {
            "view": "Video conferencing wasn't a commodity.",
            "question": "Why did WebEx sell for $3.2B but Zoom IPO at $16B?",
            "answer": "Cisco optimized enterprise suite bundling; Eric saw unhappy customers firsthand. Rebuilt architecture beat legacy codecs. Market assumed commodity; Zoom proved NPS and reliability are monetizable at massive scale.",
        },
        {
            "view": "Freemium 40 minutes is engineered network effect.",
            "question": "Why cut meetings at 40 minutes?",
            "answer": "Forces hosts to experience value with free participants — video has zero solo value. Unpaid users recruit paid hosts seamlessly; competitors charged gate upfront, limiting viral spread.",
        },
        {
            "view": "Emergence chased Zoom; Zoom wasn't shopping.",
            "question": "How did Santi win the deal?",
            "answer": "Eric wasn't raising; Santi did tech-support diligence, found profitability surprise, wrote largest Emergence check. Pattern-match: best investments often non-auction processes with operator-founders who don't need capital.",
        },
        {
            "view": "Immigration policy is industrial policy.",
            "question": "Why nine visa rejections matter?",
            "answer": "Episode argues 2019's top IPO founder nearly couldn't enter U.S. — nine applications before 1997 arrival. Santi's parallel path underscores talent friction cost for Silicon Valley.",
        },
        {
            "view": "SMB beachhead → enterprise standard.",
            "question": "Uber on Zoom S-1 stat?",
            "answer": "Uber ran 14M meeting minutes/month on Zoom per S-1 — classic land-expand: team adoption → paid plans → CIO standardization. Same playbook as ExactTarget dry-cleaner origin Scott Dorsey described.",
        },
    ],
    top_investment_implications=[
        {
            "ticker": "ZM",
            "direction": "Watch",
            "confidence": "Medium",
            "thesis": "Capital-efficient PLG with pre-IPO profitability rare in 2019 cohort — thesis hinges on expanding platform ARPU beyond meetings without Teams bundling eroding pricing power.",
        },
    ],
    golden_quotes=[
        "\"Your happiness is my happiness.\" — Eric Yuan LinkedIn philosophy cited by David.",
        "\"The most successful IPO in the US of 2019.\" — David on Zoom's April 2019 debut.",
        "\"We did not dip into any of that $130 million to build the business.\" — Eric Yuan (capital-efficiency episode echo; Zoom similarly lean on VC spend).",
    ],
    chronology={
        "subject": "Zoom / Eric Yuan",
        "events": [
            {"date": "1994", "event": "Eric hears Bill Gates internet speech in Japan"},
            {"date": "1997", "event": "Eric joins WebEx in U.S. after visa approval"},
            {"date": "2007", "event": "Cisco acquires WebEx for ~$3.2B"},
            {"date": "2011", "event": "Eric leaves Cisco; founds Zoom with ~40 ex-WebEx engineers"},
            {"date": "Jan 2014", "event": "Zoom launches publicly"},
            {"date": "2014", "event": "Emergence leads ~$30M round; 1M participants by mid-year"},
            {"date": "2018", "event": "~$330M revenue; ~$51M operating cash flow"},
            {"date": "Mar 2019", "event": "S-1 filed"},
            {"date": "Apr 2019", "event": "IPO $36 → close $62 (~$16B cap)"},
            {"date": "Jun 2019", "event": "Market cap ~$26B at Acquired recording"},
        ],
    },
)

EPISODES["acq-the-electronic-arts-ipo-with-trip-hawkins"] = base(
    "acq-the-electronic-arts-ipo-with-trip-hawkins",
    review_notes=f"{REVIEW}; Trip Hawkins interview; 1989 IPO throwback",
    episode_rating={"overall": 4},
    keywords=["Game Publishing", "Developer-as-Artist", "EA Sports"],
    conclusion=(
        "Electronic Arts is Trip Hawkins' bet that game developers are artists deserving Hollywood-style publishing: Apple employee #68, Harvard jock-coder, GSB, then 1982 departure to found EA with Don Valentine's $2M (only private capital — Trip put $200K). Hollywood-style album packaging, Dr. J vs Larry Bird (first athlete-licensed game), Madden (1988, eleven-on-eleven) became a $4B+ franchise by 2013. Woz joined board 1983. EA reverse-engineered Sega Genesis against Nintendo's lockout — Madden as Genesis killer app. Profitable from inception; 1989 IPO enabled acquisitions for decades. Trip grades IPO an A — liquidity for M&A currency, though earlier IPO might have been 10–20x cheaper."
    ),
    background=(
        "Season 4 Episode 7 recorded in Santa Barbara with founder Trip Hawkins — throwback to when IPO meant profitable industrial growth, not cash-burning unicorns. Trip: Southern California sports kid, D&D, Harvard football + late-night coding, early Apple (Lisa team, VisiCalc era), Don Valentine lunch ('bring fire back').\n\n"
        "EA incorporated as Amazin' Software, renamed Electronic Arts — 'we're about the arts but not the artists.' EA Sports: John Madden insisted on 11 players per side; Trip flew Madden to EA HQ. Sega alliance after Nintendo licensing knife-fight. IPO ~1989 after seven profitable years; Trip later founded 3DO (cautionary). Contrasts with 2019 A+ IPO cohort on capital intensity and profitability."
    ),
    important_facts=[
        "Trip Hawkins raised $2 million from Sequoia (Don Valentine) with $200,000 personal co-investment — only private capital EA took before 1989 IPO per Trip interview.",
        "Dr. J vs Larry Bird (1983) cited as first celebrity/athlete-endorsed video game — sports simulation thread predates EA Sports label.",
        "John Madden Football shipped 1988 after years negotiating 11-on-11 authenticity; Madden franchise surpassed ~$4 billion lifetime revenue by 2013 per Ben.",
        "Steve Wozniak joined EA board in 1983 alongside Trip and Don Valentine — independent credibility for developer-friendly publisher positioning.",
        "EA profitable from company start; IPO ~1989 (~7 years post-founding) provided public stock for acquisitions Trip cites as major post-IPO strategic unlock.",
    ],
    mental_model={
        "name": "Treat Developers Like Recording Artists",
        "components": (
            "Trip imported record-industry packaging and royalties to games when publishers treated devs as vendors. "
            "Platform power shifts: Nintendo's NES lockout (no published SDK) forced EA to reverse-engineer Genesis — bet on Sega openness; Madden + Montana titles drove 16-bit share. Artist autonomy + distribution scale = EA flywheel."
        ),
        "application": (
            "In creative tech, publisher value is credibly committing to talent brand and retail/distribution — until digital storefronts (Steam, App Store) disintermediate. "
            "Modern analog: platforms extracting 30% vs Trip's developer advocacy — Fortnite/App Store fights echo EA-Nintendo negotiations."
        ),
    },
    competitive_advantage=(
        "EA's early moat: Trip's Apple/Valentine network, sports licenses (Madden exclusivity became decades-long annuity), and technical guts (Genesis reverse-engineering, 11-player Madden when tech 'couldn't').\n\n"
        "EA Sports broadcast camera angle (Madden) defined genre visual language copied in real NFL games. Annual release cadence exploits sports seasons for recurring revenue.\n\n"
        "Weaknesses: Console platform owners extract rent; licensed sports IP costly today; Trip's later 3DO burn shows risk of hardware bets. Nintendo relationship adversarial — power ultimately with platform gatekeepers."
    ),
    key_insights=[
        {
            "view": "EA invented developer dignity as strategy.",
            "question": "Why 'Electronic Arts'?",
            "answer": "Trip modeled Hollywood/records — developers as artists on album covers. Don Valentine started EA in Sequoia office to 'control' young founder but Trip stood up to fire — Woz board seat reinforced indie credibility vs Nintendo vendor model.",
        },
        {
            "view": "Madden was a multi-year authenticity bet.",
            "question": "Why did Madden take so long?",
            "answer": "John Madden demanded 11 vs 11 when competitors shipped 7-on-7 '80/20 football.' Trip flew Madden to HQ; technical leap plus coach credibility created franchise still annual-decades later — $4B+ cited by 2013.",
        },
        {
            "view": "Genesis alliance was calculated platform politics.",
            "question": "Why reverse-engineer Sega?",
            "answer": "Nintendo refused licensing terms (~$10/unit, limited releases). EA bluffed Sega into favorable deal using reverse-engineered dev kit — Madden drove Genesis adoption; platform choke points determine publisher economics.",
        },
        {
            "view": "1989 IPO ≠ 2019 IPO.",
            "question": "Why go public profitable in seven years?",
            "answer": "Trip: shareholders wanted liquidity; public stock became acquisition currency for roll-ups that built modern EA. Contrast Uber 2019 — raise $8B while losing money; EA needed no growth capital, needed M&A flexibility.",
        },
        {
            "view": "Sports games are perfect recurring SKUs.",
            "question": "Why annual Madden?",
            "answer": "Real rosters, rules, and broadcast presentation refresh yearly — natural sequel engine before live-service. Trip's jock + gamer identity merged in EA Sports — category looked obvious retrospectively, uncertain pre-Dr. J title.",
        },
    ],
    top_investment_implications=[
        {
            "ticker": "EA",
            "direction": "Watch",
            "confidence": "Low",
            "thesis": "Trip-era lesson: licensed sports annuities and studio portfolio scale persist — monitor live-service transition and platform fee pressure (console/mobile 30%) on legacy publishing model.",
        },
    ],
    golden_quotes=[
        "\"I'm going to bring the fire and you've got to bring the fire right back.\" — Don Valentine to Trip Hawkins before Sequoia investment.",
        "\"We're about the arts but we're not the artists.\" — Trip on EA naming and publisher role.",
        "\"Madden had done $4 billion in revenue as a franchise\" — Ben citing cumulative Madden economics through ~2013.",
    ],
    chronology={
        "subject": "Electronic Arts / Trip Hawkins",
        "events": [
            {"date": "1978", "event": "Trip joins Apple early employee; Lisa/Mac era"},
            {"date": "1982", "event": "Trip leaves Apple; founds Amazin' Software / EA"},
            {"date": "1983", "event": "Sequoia $2M; Woz joins board; Dr. J vs Larry Bird ships"},
            {"date": "1984", "event": "Macintosh ships — Trip notes weak initial Mac sales"},
            {"date": "1988", "event": "John Madden Football releases after multi-year dev"},
            {"date": "1989", "event": "EA IPO after ~7 profitable years"},
            {"date": "1990", "event": "Sega Genesis alliance; reverse-engineered dev kit enables third-party publishing"},
            {"date": "1990s", "event": "Genesis Madden/Montana drive 16-bit sports dominance"},
            {"date": "2013", "event": "Madden franchise ~$4B+ cumulative revenue cited"},
            {"date": "2019", "event": "Acquired interview with Trip Hawkins published"},
        ],
    },
)

EPISODES["acq-the-uber-ipo"] = base(
    "acq-the-uber-ipo",
    review_notes=f"{REVIEW}; IPO-day episode; Travis → Dara arc",
    episode_rating={"overall": 4},
    keywords=["Marketplace Wars", "Stay-Private Capital", "Governance Crisis"],
    conclusion=(
        "Uber's May 10, 2019 IPO ($45 price, opened ~$42, down 7% day one) caps a decade of Garrett Camp's 'Uber' black-car idea → Travis Kalanick's operational blitz → $20B+ raised private war chest. Ben and David trace taxis (1889 SF) through Scour/Red Swoosh trauma, Cabulous rejection of Benchmark, and peer-to-peer pivot after Lyft/Sidecar. SoftBank/Saudi capital opened stay-private floodgates Uber pioneered. Post-2017: Susan Fowler, Holder Report, Benchmark sues Travis, Dara Khosrowshahi CEO. Bull: global ride-share + Eats + AV optionality + $18B stakes in Didi/Grab/Yandex. Bear: growth deceleration, subsidy wars, governance overhang. A+ requires contribution-margin-positive ride-hailing plus Eats leverage on shared driver supply."
    ),
    background=(
        "Season 4 Episode 6 recorded IPO day — longest Acquired history tour: 1907 NYC taxi strikes, Taxi Magic, Garrett at Best Buy incubator (Cabulous), Ryan Graves/Craigslist hire, Paris jam sessions with Travis, Camp's $200K seed. Benchmark's Bill Gurley pursued company after missing Cabulous.\n\n"
        "2014–2018: Fidelity/Tiger/SoftBank rounds; DiDi/Grab/Yandex equity stakes (~20% of Uber value); Otto/Waymo scandal; #DeleteUber JFK surge playbook correction; Dara cleanup. IPO raises ~$8B primary. Contrasts Pinterest/Lyft ~$15B valuations. Brad Stone's The Upstarts primary source."
    ),
    important_facts=[
        "Uber IPO May 10, 2019: priced $45/share; opened ~$42, down ~7% from open on first day per Ben and David recording live.",
        "Uber raised over $20 billion cumulatively pre-IPO; IPO added approximately $8 billion primary — Ben compares to half of Lyft's entire market cap.",
        "2017 SoftBank tender offered ~$48B valuation vs prior $68B post-DiDi round — cleaned cap table, dropped Benchmark lawsuit, Travis reduced role.",
        "Uber S-1 equity stakes cited: ~15% DiDi (China), ~38% Yandex Taxi (Russia), ~23% Grab (Southeast Asia) — ~$18B aggregate 'holding company' value per Ben.",
        "Ride-hailing revenue growth: ~100% (2016–2017) → ~42% (2017–2018) → roughly flat recent quarters pre-IPO per bear narrative.",
    ],
    mental_model={
        "name": "Global Ambition, Local Network Effects",
        "components": (
            "Uber assumed winner-take-all global ride-sharing; reality is nationally fragmented markets without cross-border network effects (Ben: 'series of markets'). "
            "Capital as weapon (SoftBank, Saudis) delayed IPO but didn't settle US/LATAM subsidy wars vs Lyft. Marketplace playbook (supply acquisition, surge, playbooks) works locally; international 'merge not compete' (DiDi swap) admits limits."
        ),
        "application": (
            "When evaluating super-app or marketplace TAM, test whether network effects cross geographies or require re-fighting supply/demand per city. "
            "Governance and culture debt compound — Uber's 2017 crisis shows operational excellence can't outrun HR/legal blowback; Dara's peacemaker role is part of bull case."
        ),
    },
    competitive_advantage=(
        "Uber's strengths: first-mover brand, dense driver/rider liquidity in top cities, multi-product leverage (Rides + Eats shares driver infrastructure per bull case), and strategic stakes in consolidated foreign markets.\n\n"
        "Travis-era city launch playbooks (Brian Tolkin LP guest) and Benchmark/Gurley board capital access created template startups copied worldwide.\n\n"
        "Weaknesses: subsidies required vs Lyft; AV timeline uncertain; Otto/Waymo legal hangover; driver classification regulation; $20B+ capital raised sets high exit hurdle; ride-sharing not globally unified network — DiDi/Grab ownership is admission of defeat in all-out conquest."
    ),
    key_insights=[
        {
            "view": "Uber opened the stay-private floodgates.",
            "question": "Why IPO in 2019 after $20B raised?",
            "answer": "Uber pioneered Fidelity/Tiger/SoftBank private rounds — Fidelity June 2014 changed startup financing. Eventually employees/LPs need liquidity; Uber still needed ~$8B primary while Slack/Zoom didn't. Era of A+ IPOs clustered as late-stage funds exhausted patience.",
        },
        {
            "view": "Travis's Scour trauma shaped Uber aggression.",
            "question": "Why so much Uber backstory?",
            "answer": "Michael Ovitz lawsuit, MPAA $250B suit scare, Red Swoosh sale to Akamai — Travis learned hardball early. Garrett's James Bond/black-car insight met operator willing to fight regulators and Lyft simultaneously — culture cost arrived 2017.",
        },
        {
            "view": "#DeleteUber misfired but fuel was real.",
            "question": "JFK surge controversy — what happened?",
            "answer": "Slack episode follow-up correction: Uber turned surge OFF during taxi strike protest, not on — but years of driver/consumer ill will made any spark combustible. Susan Fowler blog weeks later was separate catalyst for Holder Report.",
        },
        {
            "view": "20% of Uber is a fund of taxis.",
            "question": "Bull case on international?",
            "answer": "Instead of winning every market, Uber holds ~$18B in Didi/Grab/Yandex stakes — call option on consolidated foreign ride-share plus US core. Bear: stakes illiquid; US still subsidized vs Lyft.",
        },
        {
            "view": "Dara's peace is the bull case hinge.",
            "question": "Five-year A+ scenario?",
            "answer": "Contribution-margin-positive rides plus Eats sharing supply-side spend — knife fight ends when subsidies stop (Lyft public pressure). F scenario: capital markets close before unit economics work; AV never arrives to justify losses.",
        },
    ],
    top_investment_implications=[
        {
            "ticker": "UBER",
            "direction": "Watch",
            "confidence": "Medium",
            "thesis": "IPO-day framing: global ride-share + Eats + equity stakes vs slowing growth and perpetual subsidy risk — Dara must prove marketing spend can ramp down without losing US share to Lyft.",
        },
    ],
    golden_quotes=[
        "\"Uber just raised $8 billion, or approximately one half of Lyft's entire market cap in its IPO.\" — Ben's IPO-day intro.",
        "\"This whole era we're in now of all these new sources of capital… was opened up really by Uber.\" — David on Fidelity/SoftBank private-market floodgates.",
        "\"20% of the value of this company is actually a holding company.\" — Ben on Didi/Grab/Yandex stakes in S-1.",
    ],
    chronology={
        "subject": "Uber",
        "events": [
            {"date": "2008", "event": "Garrett Camp seeds black-car idea; Travis Kalanick angel involved"},
            {"date": "2010", "event": "UberCab launches San Francisco; Ryan Graves CEO then Travis"},
            {"date": "2011", "event": "Benchmark invests; expansion to NYC, Seattle"},
            {"date": "2012", "event": "Lyft/Sidecar peer-to-peer pivot response"},
            {"date": "2014", "event": "Fidelity first major crossover round; China war begins"},
            {"date": "2016", "event": "DiDi merger in China; Otto acquisition"},
            {"date": "Jan 2017", "event": "#DeleteUber controversy; Susan Fowler Feb blog"},
            {"date": "Aug 2017", "event": "Dara Khosrowshahi named CEO"},
            {"date": "2018", "event": "SoftBank tender ~$48B valuation cleanup"},
            {"date": "May 2019", "event": "IPO priced $45; opens ~$42 down ~7%"},
        ],
    },
)

EPISODES["acq-the-pinterest-ipo"] = base(
    "acq-the-pinterest-ipo",
    review_notes=f"{REVIEW}; no transcript — S-1 + episode research",
    episode_rating={"overall": 3},
    keywords=["Visual Discovery", "Intent Graph", "Non-Social Network"],
    conclusion=(
        "Pinterest is Ben Silbermann's anti-Facebook: a 'productivity tool for planning your dreams' built from hobby collecting (stamp cataloging) in Iowa/Salt Lake blogging community — not a social graph product. IPO April 2019 at ~$19 (opened ~$24, ~$12B+ cap) after FirstMark-led early rounds. Users pin future intent (weddings, remodels) vs sharing past moments — ARPU lags Instagram/Facebook but ad intent can be higher quality. Bears: US-heavy, monetization late, labeled 'next Facebook' incorrectly. Bulls: differentiated discovery graph, shoppable pins, long session planning behavior. Kevin Hartz (Eventbrite) quoted in show notes calling it best Pinterest breakdown."
    ),
    background=(
        "Season 4 Episode 5 — second in Acquired's A+ IPO series after Lyft. Ben and David contrast Pinterest with Facebook/Instagram: fewer friends, more cataloging aspirations. Origin: Ben's medical-school-parent path, Yale, Google I/O 2003 inspiration, Cold Brew Labs, early mobile failure Tote → Pinterest pivot with Evan Sharp (architecture background).\n\n"
        "Growth via design/blog community (Salt Lake bloggers), SEO for pin pages, and Apple iOS attention. S-1 shows majority US users, international monetization immature. IPO narrative: not social network — visual search/discovery engine competing for Google Shopping and Instagram ads, not friend feed time."
    ),
    important_facts=[
        "Pinterest IPO April 18, 2019 priced ~$19/share; first trade ~$24+ (~$12–15B market cap range) — 'A+' cohort alongside Uber, Zoom, Slack 2019 per Acquired framing.",
        "FirstMark Capital led Pinterest's 2011 Series A (same vintage as Shopify investment Ben cross-referenced on Shopify episode) — long hold through 2019 IPO.",
        "2018 revenue ~$756M (S-1 era cited in episode research) with ~60% YoY growth but net losses — monetization ramped via shoppable/product pins post-US user saturation concerns.",
        "Pinterest reported ~250M+ MAU pre-IPO with majority US users — international users monetize at fraction of US ARPU per bear case.",
        "Average revenue per user substantially below Facebook/Instagram (~$25–30 US ARPU TikTok episode benchmark) — bull case requires closing gap via intent-based ads.",
    ],
    mental_model={
        "name": "Intent Graph vs Social Graph",
        "components": (
            "Facebook/Instagram monetize who you know and what you did; Pinterest monetizes what you plan to do — weddings, recipes, home projects. "
            "Lower viral coefficients but higher commercial intent per session. Not 'next Facebook' — different engagement loop (planning vs posting) implies different ad products and MAU ceiling."
        ),
        "application": (
            "Evaluate consumer apps by graph type: social (relationship), interest (TikTok), or intent (Pinterest). "
            "Intent graphs monetize closer to search/shopping — compare to Google Shopping and Instagram checkout, not Snap streaks."
        ),
    },
    competitive_advantage=(
        "Pinterest owns planning-phase mindshare — users assemble boards over weeks (wedding, nursery) creating durable intent signals advertisers crave vs ephemeral Stories.\n\n"
        "SEO long-tail pin URLs drive organic acquisition cheaply vs paid social growth. Design-forward UI (Evan Sharp) differentiated from utilitarian early social apps.\n\n"
        "Weaknesses: smaller MAU than FB/Instagram; international monetization lag; Amazon/Google shopping encroachment; user base skews female — TAM narratives debated; late shoppable ads vs Instagram."
    ),
    key_insights=[
        {
            "view": "Pinterest is not a social network.",
            "question": "Why 'non-social social network'?",
            "answer": "Users catalog interests for themselves — asymmetric follows, no friend obligation. Ben's collecting hobby DNA. Investors mislabeled 'next Facebook' — engagement and ARPU mechanics differ; Kevin Hartz praised episode for clarifying category.",
        },
        {
            "view": "Intent beats attention for certain ads.",
            "question": "Bull case on monetization?",
            "answer": "Planning a kitchen remodel beats scrolling past friend vacation photos for Home Depot ads. Closing ARPU gap to FB requires shoppable pins and measurement — 2019 IPO priced optionality on intent quality vs scale.",
        },
        {
            "view": "US-first is bearish near-term.",
            "question": "Why MAU geography matters?",
            "answer": "Majority US users with mature digital ad market — international MAU large but barely monetized pre-IPO. Bears ask if Pinterest is US lifestyle niche or global discovery engine.",
        },
        {
            "view": "Tote → Pinterest is classic pivot.",
            "question": "Origin story lesson?",
            "answer": "Mobile shopping app Tote failed on payment friction; users kept pinning products. Team followed behavior — same pattern as Flickr/Slack pivots in Acquired canon: internal/user pull beats original thesis.",
        },
        {
            "view": "2019 IPO cohort shared PLG DNA.",
            "question": "Link to Zoom/Slack episodes?",
            "answer": "Zoom noted Pinterest as pivot; Acquired grouped 2019 debuts as A+ cohort — Pinterest least 'hot' media darling vs Uber but capital-efficient relative to ride-share burn; grades depend on ARPU expansion five years out.",
        },
    ],
    top_investment_implications=[
        {
            "ticker": "PINS",
            "direction": "Watch",
            "confidence": "Medium",
            "thesis": "Intent-graph monetization vs social-graph scale — watch US ARPU growth, international ad rollout, and Amazon/Google shopping competition post-IPO.",
        },
    ],
    golden_quotes=[
        "\"The planet's largest non-social social network.\" — Acquired episode overview tagline.",
        "\"A productivity tool for planning your dreams.\" — Pinterest positioning cited by Ben and David.",
        "\"The Pinterest episode is an excellent breakdown — the best I've heard to date.\" — Kevin Hartz quote in Acquired show notes.",
    ],
    chronology={
        "subject": "Pinterest / Ben Silbermann",
        "events": [
            {"date": "2009", "event": "Cold Brew Labs; Tote mobile shopping app"},
            {"date": "2010", "event": "Pinterest beta; Evan Sharp co-founder"},
            {"date": "2011", "event": "FirstMark and angel rounds; iPhone app growth"},
            {"date": "2012", "event": "Site redesign; Time '50 Best Websites'"},
            {"date": "2015", "event": "Visual search and buyable pins expand"},
            {"date": "2017", "event": "Lens visual search launch; 200M+ MAU milestone"},
            {"date": "2018", "event": "~$756M revenue (~60% YoY growth) per pre-IPO S-1 metrics"},
            {"date": "Mar 2019", "event": "S-1 filed"},
            {"date": "Apr 2019", "event": "NYSE IPO ~$19 price, ~$12B+ initial cap"},
            {"date": "2019", "event": "Acquired Season 4 Episode 5 published"},
        ],
    },
)

# Tesla — fix corrupted discovered metadata
_tesla_meta = dict(META["acq-season-3-episode-1tesla"])
_tesla_meta.update(
    {
        "title": "Tesla",
        "guest": "Tesla",
        "guest_role": "Season 3 · Episode 1",
        "date": "2018-07-16",
        "duration_minutes": 120,
        "links": {
            "acquired": "https://www.acquired.fm/episodes/season-3-episode-1tesla",
            "apple_podcasts": "https://podcasts.apple.com/podcast/acquired/id1050462261",
            "spotify": "https://open.spotify.com/show/2HI3KdjtJnr3E8B4W8Y0Yx",
        },
    }
)

EPISODES["acq-season-3-episode-1tesla"] = {
    "episode_id": "acq-season-3-episode-1tesla",
    "podcast": "Acquired",
    "host": "Ben Gilbert & David Rosenthal",
    "metadata": _tesla_meta,
    "extraction_meta": {
        "model": "manual-gpt-agent-v5.1-acquired",
        "transcript_source": "acquired.fm",
        "status": "approved",
        "template_version": "5.1-acquired",
    },
    "review_notes": f"{REVIEW}; no transcript — Season 3 premiere; corrected metadata",
    "episode_rating": {"overall": 4},
    "keywords": ["EV Manufacturing", "Elon Musk", "NUMMI Factory"],
    "conclusion": (
        "Tesla is America's first automotive startup since Ford to matter at scale: Martin Eberhard and Marc Tarpenning's lithium-ion Roadster dream met Elon Musk's capital and will — IPO June 2010 (~$17, ~$1.7B cap) after near-death 2008 Christmas Eve financing. Acquired Season 3 premiere traces AC Propulsion tzero → Roadster (Lotus Elise chassis) → Model S (2012) → Gigafactory → Model 3 production hell. Fremont NUMMI factory (Toyota/GM JV) symbolizes manufacturing ambition. Ben asks Elon vs Tony Stark; David covers multiple near-bankruptcies Musk funded personally. Bears: capital intensity, autonomy timelines; bulls: vertical integration, brand, energy storage optionality."
    ),
    "background": (
        "Season 3 Episode 1 (July 2018) — two-hour Tesla history from founding through post-IPO era (pre-2018 profitability swing). Eberhard/Tarpenning Silicon Valley engineers; Elon led Series A and became face after internal conflicts (Eberhard departed 2007). Roadster proved EV could be desirable; Model S sedan validated luxury EV TAM.\n\n"
        "2010 NASDAQ IPO raised capital for Model S tooling; 2016 Model 3 reveal created reservation wave and production hell (2017–2018). SolarCity merge, Autopilot, Supercharger network, and Musk pay package featured. Episode compares to Ford heritage and asks if Tesla is tech company or automaker — vertical integration (batteries, software OTA) as moat narrative."
    ),
    "important_facts": [
        "Tesla IPO June 29, 2010 at $17/share (~$226M raised, ~$1.7B initial market cap) — first American car company IPO since Ford per Acquired framing.",
        "Roadster (2008) based on Lotus Elise; only ~2,450 Roadsters built — proof-of-concept before Model S platform (deliveries began 2012).",
        "Model 3 announced March 2016; ~325,000 reservations (~$14B implied value) within weeks — production hell 2017–2018 ramp dominated post-IPO narrative.",
        "Tesla acquired NUMMI plant in Fremont, California (former Toyota/GM joint venture) for ~$42M in 2010 — manufacturing bet incumbents thought impossible for startup.",
        "Elon Musk led 2008 Christmas Eve financing round (~$40M) when Tesla weeks from bankruptcy — Musk personally capitalized prior rounds (PayPal proceeds).",
    ],
    "mental_model": {
        "name": "Startup Car Company Capital Stack",
        "components": (
            "Automotive requires manufacturing learning curves (NUMMI), working capital, and regulatory compliance — far heavier than software. "
            "Tesla sequenced risk: Roadster (low volume proof) → Model S (factory, brand) → Model 3 (mass market, production hell) → energy/storage. OTA software updates amortize features across fleet — partial software economics inside hardware shell."
        ),
        "application": (
            "EV competitors must match capital endurance and integration depth, not just specs. "
            "Investors price Tesla partly as tech (FSD optionality, energy) vs GM/Ford multiples — episode asks which comp dominates as production scales."
        ),
    },
    "competitive_advantage": (
        "Tesla's moat narrative: Supercharger network early lead, battery cost curve (Gigafactory scale), brand as EV synonym, and software/Ota velocity incumbents struggled to copy.\n\n"
        "Direct sales model and Musk marketing eliminated dealer margin but invited regulatory fights state-by-state.\n\n"
        "Weaknesses: capital intensity and dilution; quality variance during ramps; autonomy promises vs delivery gap; incumbent EV awakening (2018+); key-person risk. Production hell showed manufacturing is not Moore's Law — bottlenecks are physical."
    ),
    "key_insights": [
        {
            "view": "Tesla survived capital winter repeatedly.",
            "question": "2008 near-death lesson?",
            "answer": "Weeks from bankruptcy until Christmas Eve 2008 round — Musk put in personal capital repeatedly. Unlike 2019 software IPOs, Tesla needed public markets in 2010 to fund factories, not for liquidity alone.",
        },
        {
            "view": "Roadster was proof, Model 3 is business.",
            "question": "Why sequence Roadster → S → 3?",
            "answer": "Lotus-based Roadster (~2,450 units) proved lithium-ion desirability; Model S validated luxury sedan manufacturing at Fremont; Model 3 reservations (~325K in weeks) proved mass demand — then production hell tested whether startup could build at volume.",
        },
        {
            "view": "NUMMI was symbolic and strategic.",
            "question": "Why buy a GM/Toyota plant?",
            "answer": "~$42M for Fremont NUMMI gave Tesla Bay Area manufacturing credibility — retooled Toyota/GM line for EVs when analysts assumed contract manufacturing. Vertical integration thesis starts with owning the factory floor.",
        },
        {
            "view": "Elon vs Tony Stark is marketing mirror.",
            "question": "Who came first — Musk or Stark?",
            "answer": "Episode spoiler: Elon — Iron Man filmmakers used Musk as inspiration for Tony Stark portrayal; mutual celebrity reinforced Tesla brand without traditional auto advertising spend.",
        },
        {
            "view": "Tech multiple on auto risk.",
            "question": "Bull vs bear at episode time (2018)?",
            "answer": "Bulls: energy storage, autonomy software margin, Supercharger standard. Bears: Model 3 ramp, cash burn, incumbent EV response. 2018 sat in production hell — grade contingent on proving mass manufacturing.",
        },
    ],
    "top_investment_implications": [
        {
            "ticker": "TSLA",
            "direction": "Watch",
            "confidence": "Low",
            "thesis": "Season 3 framing: vertical integration + brand vs capital intensity and production ramp risk — 2018 episode predates sustained profitability; monitor Model 3 cadence and FSD monetization proof.",
        },
    ],
    "golden_quotes": [
        "\"America's most successful automotive startup since The Ford Motor Company.\" — Acquired Season 3 overview.",
        "\"Who came first, Elon Musk or Tony Stark? (Spoiler: Elon)\" — Episode teaser on Musk-Iron Man symbiosis.",
        "\"Two-hour extravaganza on America's most successful automotive startup.\" — Ben and David's Season 3 premiere pitch.",
    ],
    "chronology": {
        "subject": "Tesla",
        "events": [
            {"date": "2003", "event": "Martin Eberhard and Marc Tarpenning incorporate Tesla Motors"},
            {"date": "2004", "event": "Elon Musk leads Series A; joins board"},
            {"date": "2007", "event": "Eberhard departs; Musk assumes leadership amid Roadster delays"},
            {"date": "2008", "event": "Roadster deliveries begin; near-bankruptcy Christmas Eve financing"},
            {"date": "2010", "event": "NUMMI Fremont purchased for ~$42M; IPO June 29 at $17/share"},
            {"date": "2012", "event": "Model S deliveries begin"},
            {"date": "2014", "event": "Gigafactory Nevada announced with Panasonic partnership"},
            {"date": "Mar 2016", "event": "Model 3 unveiled; ~325K reservations in weeks"},
            {"date": "2017–2018", "event": "Model 3 production hell ramp"},
            {"date": "Jul 2018", "event": "Acquired Season 3 Episode 1 published"},
        ],
    },
}


def main() -> None:
    results: dict[str, str] = {}
    for ep_id, body in EPISODES.items():
        path = APPROVED / f"{ep_id}.json"
        path.write_text(json.dumps(body, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
        proc = subprocess.run(
            [PY, str(ROOT / "scripts" / "validate_one_acquired.py"), ep_id],
            capture_output=True,
            text=True,
        )
        status = "completed" if proc.returncode == 0 else "failed"
        results[ep_id] = status
        print(f"{ep_id}: {status}")
        if proc.stdout:
            print(proc.stdout.rstrip())
        if proc.stderr:
            print(proc.stderr.rstrip(), file=sys.stderr)

    print("\n--- Summary ---")
    for ep_id, status in results.items():
        print(f"{status.upper():8} {ep_id}")
    failed = [k for k, v in results.items() if v == "failed"]
    raise SystemExit(1 if failed else 0)


if __name__ == "__main__":
    main()
