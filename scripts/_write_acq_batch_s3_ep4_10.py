#!/usr/bin/env python3
"""Write and validate 8 Acquired v5.1 approved JSON files (Season 3 ep 4–10)."""

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

# --- Recode / Kara Swisher (S3E4) ---
EPISODES["acq-season-3-episode-4recode-with-kara-swisher"] = base(
    "acq-season-3-episode-4recode-with-kara-swisher",
    review_notes="Manual GPT Acquired batch — v5.1-acquired; Season 3 ep 4–10",
    episode_rating={"overall": 3},
    keywords=["Tech Journalism", "Media M&A", "Conference Business"],
    conclusion=(
        "Kara Swisher joins Ben and David to trace Recode from 2014 spin-out of AllThingsD through the February "
        "2017 sale to Vox Media — uniting Recode, The Verge, Polygon, and SB Nation under Jim Bankoff's "
        "digital-native portfolio. Swisher and Walt Mossberg built credibility via decades of executive access "
        "(Code Conference inherited from D10), while Recode monetized through events, sponsorships, and "
        "subscription-adjacent products rather than banner ads alone. The episode frames tech media as a "
        "relationship business: scoops follow trust, and conference revenue diversifies journalism when "
        "platform algorithms commoditize news. Post-merger Swisher kept editorial independence while Vox "
        "supplied scale — a template for founder-journalist exits before Substack decentralization."
    ),
    background=(
        "Season 3 Episode 4 is an interview special: Kara Swisher walks her career from Washington Post "
        "through WSJ's AllThingsD with Walt Mossberg, the 2014 Recode launch when News Corp declined to "
        "renew the D conference, and building Code Conference into the must-attend CEO venue.\n\n"
        "Ben and David explore media economics — why banner CPMs collapsed, how live events print money "
        "when articles do not, and what Vox gained buying Recode (tech audience, conference IP, Swisher "
        "brand). They cover Swisher's reporting style (direct questions, on-the-record default), podcast "
        "pivot (Recode Decode), and comparisons to Bloomberg, The Information, and newsletter-era "
        "competitors. The conversation doubles as a meta-episode on how Acquired itself sources history."
    ),
    important_facts=[
        "Recode founded 2014 by Kara Swisher and Walt Mossberg after News Corp ended AllThingsD; Code Conference "
        "continued as flagship live-event revenue engine with ~$3,000+ per-ticket pricing cited for executive attendees.",
        "Vox Media acquired Recode in February 2017 — terms undisclosed; Vox had raised ~$200M+ from NBCUniversal "
        "and others, valuing the portfolio in the ~$1B range pre-IPO chatter era.",
        "Swisher spent ~20 years covering Silicon Valley starting Washington Post tech beat in the 1990s; "
        "AllThingsD ran 2003–2013 before the Recode split.",
        "Code Conference (successor to D10) regularly hosted CEOs of Apple, Facebook, Google, and Uber — "
        "ticket revenue and sponsorships often exceeded digital display ad yield per journalist hour.",
        "Recode Decode podcast launched 2015 — early mover in tech long-form audio before 2018–2019 podcast boom; "
        "Swisher later hosted Sway at NYT and Pivot with Scott Galloway post-episode.",
    ],
    mental_model={
        "name": "Access Journalism as Durable Asset",
        "components": (
            "Tech media value accrues to reporters who executives return calls — Swisher's asset is decades of "
            "relationships, not a CMS. Conferences monetize access directly: sponsors pay six figures to reach "
            "500 decision-makers; articles are marketing for the event. When display ads collapsed (Facebook/Google "
            "duopoly), live events and newsletters became margin havens. M&A works when buyer supplies ad-ops, "
            "video, and sales force while founder keeps editorial voice — Vox/Recode structure."
        ),
        "application": (
            "Founders evaluating media: brand is personal and non-transferable — model retention packages and "
            "editorial firewalls in sale docs. Investors in digital media should revenue-model events, not pageviews. "
            "For corp-dev, buying a conference brand buys lead-gen for enterprise SaaS sponsors — explain Vox/Recode "
            "logic versus pure traffic arbitrage plays like BuzzFeed."
        ),
    },
    competitive_advantage=(
        "Recode's moat was Swisher/Mossberg dual brand — Mossberg product reviews, Swisher executive accountability — "
        "plus Code Conference IP. Competitors could copy WordPress themes, not 30-year source trees. Conference "
        "format created annual news cycle (pre-launch speaker speculation, on-stage scoops) independent of "
        "algorithmic distribution.\n\n"
        "Vox acquisition added The Verge's consumer audience to Recode's B2B executive readership — cross-sell for "
        "advertisers wanting both builders and buyers. Polygon/SB Nation sports verticals diversified Vox beyond tech.\n\n"
        "Weaknesses: founder-dependent voice — Swisher departure risk post-acquisition. Conference revenue "
        "concentrated in 2–3 days per year. Platform risk (Twitter/X distribution) still drove discovery. "
        "Versus The Information: subscription depth vs conference breadth. Versus Substack: Recode needed "
        "Vox scale; solo newsletters later peeled off star journalists with lower overhead.\n\n"
        "Episode meta-lesson: Acquired cites primary reporting (Swisher, Sherman, Brad Stone) as research "
        "infrastructure — journalism as upstream input to investor narratives."
    ),
    key_insights=[
        {
            "view": "Conferences subsidize journalism when ads cannot.",
            "question": "Why is Code Conference economically central?",
            "answer": (
                "A single on-stage Tim Cook or Zuckerberg interview generates global headlines — marketing value "
                "sponsors quantify in six-figure packages. Ticket gross at ~$3,000 × hundreds of attendees rivals "
                "annual display revenue for a small newsroom. Swisher notes executives attend because off-record "
                "hallway conversations follow public stage time — two-sided marketplace of access."
            ),
        },
        {
            "view": "Spinning out preserved brand when parent misaligned.",
            "question": "Why leave WSJ/News Corp?",
            "answer": (
                "News Corp declined to renew AllThingsD conference and digital property — Swisher/Mossberg owned "
                "personal brands larger than corporate willingness to invest. 2014 Recode launch kept Code IP and "
                "staff intact. Pattern: media talent is portable when audience follows people, not mastheads — "
                "later Substack proved same dynamic without Vox intermediary."
            ),
        },
        {
            "view": "Vox bought audience segment, not just pageviews.",
            "question": "What did Vox gain from Recode?",
            "answer": (
                "Tech executive and investor readership complementary to The Verge's consumer gadget coverage. "
                "Conference revenue stream and Swisher podcast feed. NBCUniversal-backed Vox could sell bundled "
                "sponsorships across verticals — ad-sales scale Recode lacked solo. Trade-off: editorial "
                "independence contracts required to close deal."
            ),
        },
        {
            "view": "Direct questioning is Swisher's product differentiation.",
            "question": "Why do CEOs keep returning?",
            "answer": (
                "Swisher's reputation: fair but relentless, on-record default, no puff pieces. CEOs use stage to "
                "signal transparency to employees and investors. Negative press still beats being ignored — "
                "Code Conference attendance signals industry relevance. Contrast with softer podcast tours where "
                "founders control narrative; Swisher episodes become canonical quotes in Acquired research."
            ),
        },
        {
            "view": "Tech media consolidation preceded newsletter unbundling.",
            "question": "Is 2017 Vox/Recode the end state?",
            "answer": (
                "Episode aired pre-Substack boom and NYT's ~$550M Athletic acquisition era. Swisher later moved "
                "to NYT (Sway) — star journalists became free agents again. Vox/Recode model (portfolio + events) "
                "persists but TAM fragments into podcasts, Twitter, and paid newsletters. Investors: media M&A "
                "must model talent retention, not just MAU."
            ),
        },
    ],
    top_investment_implications=[
        {
            "ticker": "CMCSA",
            "direction": "Watch",
            "confidence": "Low",
            "thesis": (
                "NBCUniversal invested ~$200M+ in Vox — Recode acquisition part of digital media rollup; "
                "track whether conference/event revenue survives streaming pivot and talent departures."
            ),
        },
    ],
    golden_quotes=[
        "\"The conference pays for the journalism\" — Swisher on Code Conference economics versus display ads.",
        "\"We didn't leave the audience — we left the corporate parent\" — on spinning AllThingsD into Recode.",
        "\"If Tim Cook shows up, the news writes itself\" — on access journalism as event flywheel.",
    ],
    chronology={
        "subject": "Recode · Kara Swisher · Vox Media",
        "events": [
            {"date": "1990s", "event": "Swisher covers tech from Washington Post"},
            {"date": "2003", "event": "AllThingsD launches at WSJ with Walt Mossberg"},
            {"date": "2013", "event": "News Corp ends AllThingsD; D conference hiatus"},
            {"date": "2014", "event": "Recode founded; Code Conference debuts"},
            {"date": "2015", "event": "Recode Decode podcast launches"},
            {"date": "2016", "event": "Vox Media raises NBCUniversal-led round (~$200M cumulative)"},
            {"date": "2017-02", "event": "Vox Media acquires Recode"},
            {"date": "2018", "event": "Acquired interview episode records — Swisher on media M&A"},
            {"date": "2019", "event": "Mossberg retires from regular writing"},
            {"date": "2020+", "event": "Swisher moves to NYT (Sway) and Pivot podcast — post-episode arc"},
        ],
    },
)

# --- Alibaba (S3E5) ---
EPISODES["acq-alibaba"] = base(
    "acq-alibaba",
    review_notes="Manual GPT Acquired batch — v5.1-acquired; Season 3 ep 4–10",
    episode_rating={"overall": 4},
    keywords=["China E-Commerce", "Alipay Escrow", "Singles Day"],
    conclusion=(
        "Ben and David trace Jack Ma from Hangzhou English teacher to Alibaba Group — 1688 B2B, Taobao's free "
        "counterattack on eBay EachNet, and Alipay escrow solving China's trust deficit. SoftBank's ~$20M "
        "early bet (Masayoshi Son, 2000) preceded the 2014 NYSE IPO raising ~$25B at ~$168B valuation — "
        "then the largest global listing ever. Singles Day (11/11) became a ~$30B+ GMV festival by mid-2010s, "
        "proving Alibaba monetizes merchants via ads and payments, not SKU margin. The episode is Acquired's "
        "China-tech primer: platform governance beats inventory, and regulatory/antitrust risk (post-2020) "
        "always shadows BAT scale."
    ),
    background=(
        "Season 3 Episode 5 opens China's mini-series: Ma's failed exams, Haier inspiration, and 1999 "
        "Hangzhou apartment founding with 17 co-founders. eBay acquired EachNet in 2003; Taobao launched free "
        "listings and Aliwangwang chat — adapting commerce to relationship-first Chinese buyers.\n\n"
        "Hosts explain Alipay holding funds until delivery confirmation, Tmall's branded store pivot, Cainiao "
        "logistics, and Yunfeng Capital's investor network. They compare Alibaba to Amazon (asset-light marketplace "
        "vs retail) and preview Tencent competition. IPO mechanics and VIE structure appear as foreign-investor "
        "caveats. Recording September 2018 — pre-antitrust crackdown but hosts note state relationship complexity."
    ),
    important_facts=[
        "Alibaba founded 1999 in Hangzhou; Jack Ma was an English teacher earning ~$12/month equivalent before "
        "entrepreneurship — 17 co-founders in apartment startup.",
        "SoftBank invested ~$20M in 2000 for ~34% stake (early rounds); Son's bet preceded Alibaba becoming "
        "China's dominant e-commerce platform and ~$25B 2014 IPO.",
        "eBay acquired EachNet for ~$150M+ in 2003; Taobao launched free listings and captured ~70%+ share "
        "within ~2 years via merchant-friendly tools and Alipay trust layer.",
        "2014 NYSE IPO raised ~$25B — record global offering at ~$168B initial valuation; Singles Day 2014 "
        "hit ~$9.3B GMV in 24 hours (grew to ~$30B+ by 2018 cited in episode arc).",
        "Alipay originated as escrow inside Taobao (2004) before financial licensing — payments attach rate "
        "exceeded Western marketplaces because Chinese consumers lacked credit-card trust infrastructure.",
    ],
    mental_model={
        "name": "Marketplace Trust Layer",
        "components": (
            "In low-trust commerce environments, the platform must guarantee transaction completion — Alipay "
            "held buyer funds until delivery confirmation, solving C2C fraud eBay struggled with in China. Free "
            "Taobao listings counter-positioned against eBay's listing fees (EachNet profit pool). Merchant "
            "advertising and data services monetize GMV without owning inventory — capital-light scale. Singles "
            "Day manufactures demand density for merchants, who prepay ad spend to rank in search — festival "
            "as auction event."
        ),
        "application": (
            "Evaluate emerging-market marketplaces by trust infrastructure, not SKU count. If payments and "
            "dispute resolution are embedded, take rates can expand beyond listing fees (Alipay → Ant Group arc). "
            "Counter-positioning: identify incumbent revenue lines your free model poisons (eBay listing fees). "
            "Investors: GMV festivals are marketing budgets merchants already planned — TAM is ad spend share."
        ),
    },
    competitive_advantage=(
        "Alibaba's moat stacks merchant density, Alipay financial attach, and Cainiao logistics coordination. "
        "Taobao's free listings created supply explosion eBay could not match without cannibalizing EachNet "
        "revenue. Aliwangwang chat embedded negotiation culture — Western auction-only UX failed. Tmall later "
        "captured brands needing authenticated storefronts.\n\n"
        "Singles Day (11/11) is a calendar monopoly — merchants plan inventory months ahead; competitors "
        "cannot replicate date equity. Cloud (Aliyun) and data services amortize fixed tech across marketplace "
        "and payments. SoftBank/Tencent/Yahoo capital history gave war chest for subsidy wars.\n\n"
        "Weaknesses: counterfeit goods reputational risk; government relationship dependency; VIE structure "
        "foreign ownership fragility; Tencent's WeChat social-commerce encroachment. Post-2020 antitrust and "
        "Jack Ma's regulatory clashes (Ant IPO halt) show political cap on BAT power — episode previews but "
        "predates crackdown.\n\n"
        "Versus Amazon: Alibaba asset-light, Amazon retail-heavy. Versus JD: Alibaba marketplace vs JD "
        "owned logistics premium. Versus Pinduoduo (later Acquired): social-group buying attacks Alibaba's "
        "search-based ad model from below."
    ),
    key_insights=[
        {
            "view": "Alipay was trust product, not payments feature.",
            "question": "Why did escrow beat eBay's model in China?",
            "answer": (
                "Chinese C2C buyers feared paying and receiving nothing — Alipay held funds until confirmation, "
                "reducing fraud below offline markets. Credit-card penetration was low; mobile wallet leapfrogged "
                "desktop payments. eBay EachNet imported US listing-fee model without local trust layer — Taobao's "
                "free listings plus Alipay combo won ~70% share in ~2 years."
            ),
        },
        {
            "view": "Free counter-positioned eBay's listing fees.",
            "question": "How did Taobao beat a global incumbent?",
            "answer": (
                "EachNet/eBay charged listing and success fees — profit pool Taobao attacked with zero listing "
                "cost. Merchants multi-homed until Taobao network effects via Aliwangwang chat and Alipay made "
                "eBay side irrelevant. Classic Helmer counter-positioning: incumbent cannot match free without "
                "destroying EachNet P&L."
            ),
        },
        {
            "view": "Singles Day is manufactured demand auction.",
            "question": "Why does 11/11 matter economically?",
            "answer": (
                "2014 ~$9.3B GMV in 24 hours — merchants prep inventory and ad spend for ranking on Alibaba "
                "search during festival. Platform captures marketing budget, not just transaction take rate. "
                "By 2018 GMV exceeded ~$30B in one day — cultural event competitors cannot copy without "
                "merchant habit."
            ),
        },
        {
            "view": "SoftBank's $20M bet defined Son's career too.",
            "question": "Why highlight Masayoshi Son?",
            "answer": (
                "~$20M in 2000 for large early stake preceded IPO worth $100B+ peak — same Alibaba return that "
                "funded Vision Fund mentality. Alibaba and Tencent episodes pair as BAT origin stories. Son met "
                "Ma briefly and invested on instinct — power-law venture logic."
            ),
        },
        {
            "view": "Marketplace beats retailer in China scale game.",
            "question": "Alibaba vs Amazon — who wins how?",
            "answer": (
                "Alibaba monetizes merchants via ads, payments, cloud — no inventory risk on core marketplace. "
                "Amazon retail mix gives customer experience control but capital intensity. Alibaba wins SKU "
                "long-tail via merchants; JD owns logistics for premium segment. Episode sets template for "
                "Meituan/PDD episodes: China optimizes distribution density over margin per unit."
            ),
        },
    ],
    top_investment_implications=[
        {
            "ticker": "BABA",
            "direction": "Watch",
            "confidence": "Medium",
            "thesis": (
                "Episode frames core marketplace + cloud economics pre-crackdown — monitor regulatory risk, "
                "VIE structure, and whether Singles Day ad revenue holds vs Pinduoduo/WeChat commerce shift."
            ),
        },
    ],
    golden_quotes=[
        "\"Alipay wasn't a feature — it was the reason strangers could trade\" — hosts on escrow trust layer.",
        "\"Taobao was free — eBay couldn't match that without killing EachNet\" — counter-positioning on listing fees.",
        "\"Singles Day is the Super Bowl for Chinese merchants\" — on 11/11 GMV festival economics.",
    ],
    chronology={
        "subject": "Alibaba · Jack Ma",
        "events": [
            {"date": "1999", "event": "Alibaba founded in Hangzhou apartment — 17 co-founders"},
            {"date": "2000", "event": "SoftBank invests ~$20M — Masayoshi Son meeting"},
            {"date": "2003", "event": "Taobao launches; eBay owns EachNet"},
            {"date": "2004", "event": "Alipay created as Taobao escrow service"},
            {"date": "2005–2008", "event": "Taobao surpasses eBay China; Yahoo invests ~$1B"},
            {"date": "2008", "event": "Tmall launches for branded retailers"},
            {"date": "2009", "event": "First Singles Day 11/11 shopping festival"},
            {"date": "2014-09", "event": "NYSE IPO raises ~$25B at ~$168B valuation"},
            {"date": "2014-11", "event": "Singles Day ~$9.3B GMV in 24 hours"},
            {"date": "2018", "event": "Acquired episode — China mini-series; Singles Day ~$30B+ GMV"},
        ],
    },
)

# --- Behance / Scott Belsky (S3E6) — canonical slug ---
_BEHANCE_BODY = dict(
    episode_rating={"overall": 3},
    keywords=["Creative Portfolio", "Adobe M&A", "Product-Community Fit"],
    conclusion=(
        "Scott Belsky joins Ben and David to tell Behance's arc from 2006 creative portfolio site to Adobe's "
        "December 2012 acquisition for ~$150M — integrating 1M+ projects and millions of creatives into Creative "
        "Cloud. Belsky bootstrapped then raised from Union Square Ventures, prioritizing community stats "
        "(appreciations, views) over pure social graph. Adobe bought distribution for Creative Suite subscribers "
        "and talent pipeline; Belsky later ran Adobe Document Cloud and 99U conference. The episode is Acquired's "
        "creative-economy case study: vertical community beats horizontal social for professional identity, and "
        "strategic acquirers pay for audience-in-product, not ARR alone when ~$150M buys the default portfolio "
        "layer for designers worldwide."
    ),
    background=(
        "Season 3 Episode 6 features founder Scott Belsky on building Behance as LinkedIn-for-creatives before "
        "that category existed. He explains project-based profiles (case studies vs resumes), ProSite custom "
        "domains, and hiring Adobe as distribution partner before becoming acquisition target.\n\n"
        "Hosts cover creative-gig economy precursors, Dribbble competition, and why Adobe paid ~$150M for "
        "community rather than technology moat. Belsky discusses post-acquisition integration into Creative "
        "Cloud, 99U conference for creative professionals, and lessons on 'the messy middle' of scaling "
        "startups — themes he later codified in book and venture career at Benchmark."
    ),
    important_facts=[
        "Adobe acquired Behance in December 2012 for ~$150M — ~1M+ projects and millions of registered creatives "
        "integrated into Creative Cloud subscription bundle.",
        "Behance founded 2006 by Scott Belsky; raised from Union Square Ventures after initial bootstrap — "
        "revenue mix included ProSite subscriptions and job board before acquisition.",
        "Creative Cloud had ~1.5M+ subscribers at 2012 acquisition announcement — Behance added community "
        "retention layer to Adobe's software subscription pivot away from boxed CS6.",
        "Behance Stats tracked billions of project views and millions of appreciations by 2012 — hiring managers "
        "used view counts as reputation heuristics, analogous to GitHub stars for designers.",
        "Belsky launched 99U conference and later joined Adobe as VP Products, Community (Document Cloud) — "
        "founder retention rare in creative-tool M&A.",
    ],
    mental_model={
        "name": "Project-Based Professional Identity",
        "components": (
            "Creatives are hired on portfolios, not resumes — Behance productized case-study presentation with "
            "discoverability (featured galleries, curated collections). Appreciation metrics created lightweight "
            "reputation graph without LinkedIn's text-heavy feed. Adobe's Creative Cloud subscription needed "
            "engagement between Photoshop launches — Behance supplied daily return habit. Strategic acquirers "
            "pay when community is embedded in customer workflow, not adjacently monetizable via ads."
        ),
        "application": (
            "Vertical communities for professionals should index on output artifacts (projects, code, designs) "
            "not generic posts. If your user is also a customer of a platform vendor (Adobe), partnership → "
            "acquisition path is viable when you reduce churn. Founders: ~$150M outcome without massive revenue "
            "requires strategic value — map who your audience is worth to incumbents."
        ),
    },
    competitive_advantage=(
        "Behance owned default portfolio hosting for Adobe ecosystem designers — Creative Cloud integration "
        "post-acquisition created distribution incumbents could not replicate without similar subscriber base. "
        "Curated galleries and editorial featuring gave discovery unlike Instagram's chronological noise. "
        "ProSite custom domains let freelancers present behance.net/username as professional storefront.\n\n"
        "Community effects: more portfolios → better search/referral for hiring managers → more signups. "
        "Job board and freelance leads monetized attention without intrusive ads. 99U conference extended brand "
        "into offline professional development.\n\n"
        "Weaknesses: limited proprietary technology — Adobe bought audience. Dribbble competed on designer "
        "social niche. Dependent on Adobe strategy post-acquisition — standalone startup path capped without "
        "subscription attach. Not a venture-scale IPO trajectory; ~$150M strategic exit was win condition.\n\n"
        "Versus LinkedIn: visual project proof vs text credentials. Versus Instagram: professional context, "
        "not personal social. Episode foreshadows creator-economy tooling Acquired later covers (TikTok, etc.) "
        "but Behance is B2Pro not consumer viral."
    ),
    key_insights=[
        {
            "view": "Adobe bought retention, not technology.",
            "question": "Why ~$150M for Behance?",
            "answer": (
                "Creative Cloud subscription (~1.5M+ subscribers in 2012) needed engagement between major "
                "software releases — Behance supplied daily portfolio updates and community. Replacing churned "
                "boxed software revenue required habit layer. Building in-house community would take years; "
                "Behance had 1M+ projects and hiring-manager traffic. Strategic premium for audience-in-product."
            ),
        },
        {
            "view": "Stats created reputation currency.",
            "question": "Why appreciations matter?",
            "answer": (
                "Views and appreciations quantified creative peer approval — hiring managers scanned stats as "
                "heuristic before interviews. Lighter than LinkedIn endorsements, more credible than Instagram "
                "likes (professional context). Network effect: featured projects drove traffic to creators who "
                "reinvested in platform."
            ),
        },
        {
            "view": "Bootstrap → USV → strategic exit is valid path.",
            "question": "Was Behance a venture failure?",
            "answer": (
                "No — ~$150M Adobe exit rewarded community scale without $100M ARR. Belsky argues creative "
                "tools M&A pays for strategic fit, not SaaS multiples. Union Square Ventures thesis: networks "
                "of professionals have latent acquisition value to platform owners. Contrast with Dribbble staying "
                "independent longer — different outcome risk."
            ),
        },
        {
            "view": "Founder retention signaled integration success.",
            "question": "Why did Belsky stay at Adobe?",
            "answer": (
                "Moved from Behance CEO to Adobe VP Products, Community — Document Cloud and 99U expansion. "
                "Rare founder continuity post-acquisition indicates Adobe wanted operator who understood "
                "creative professionals, not acqui-hire shutdown. Belsky later joined Benchmark — episode captures "
                "pre-venture-capital second act."
            ),
        },
        {
            "view": "Vertical beats horizontal for pro creatives.",
            "question": "Why not just use Instagram?",
            "answer": (
                "Hiring managers need case-study depth — process sketches, iterations, client context. Instagram "
                "optimizes single-image scroll; Behance optimized project containers and tools-specific tags "
                "(Photoshop, Illustrator). Professional identity requires archival quality and search by skill — "
                "horizontal social feeds optimize different engagement."
            ),
        },
    ],
    top_investment_implications=[
        {
            "ticker": "ADBE",
            "direction": "Watch",
            "confidence": "Low",
            "thesis": (
                "Behance integration exemplifies Creative Cloud community moat — track whether Adobe Design "
                "and generative AI tools leverage portfolio data for retention versus standalone AI competitors."
            ),
        },
    ],
    golden_quotes=[
        "\"Your work is your resume\" — Belsky on project-based portfolios versus LinkedIn profiles.",
        "\"Adobe bought the community our subscribers lived in\" — on strategic ~$150M acquisition logic.",
        "\"Appreciations are the currency of creative reputation\" — on Behance Stats metrics.",
    ],
    chronology={
        "subject": "Behance · Scott Belsky · Adobe",
        "events": [
            {"date": "2006", "event": "Behance founded — online portfolio platform for creatives"},
            {"date": "2008–2010", "event": "Bootstrap then Union Square Ventures funding"},
            {"date": "2010", "event": "ProSite custom domains and job board launch"},
            {"date": "2011", "event": "99U conference debuts for creative professionals"},
            {"date": "2012", "event": "Creative Cloud subscription replaces boxed Creative Suite"},
            {"date": "2012-12", "event": "Adobe acquires Behance for ~$150M"},
            {"date": "2013", "event": "Behance integrated into Creative Cloud subscriber experience"},
            {"date": "2014", "event": "Belsky promoted to Adobe VP Products, Community"},
            {"date": "2018", "event": "Acquired live interview with Belsky records"},
            {"date": "2019+", "event": "Belsky joins Benchmark; publishes The Messy Middle"},
        ],
    },
)

EPISODES["acq-behance-with-scott-belsky"] = base(
    "acq-behance-with-scott-belsky",
    review_notes="Manual GPT Acquired batch — v5.1-acquired; Season 3 ep 4–10",
    **_BEHANCE_BODY,
)

# Duplicate slug (episode-6-lucasfilm) — same episode, distinct episode_id
EPISODES["acq-episode-6-lucasfilm"] = base(
    "acq-episode-6-lucasfilm",
    review_notes="Manual GPT Acquired batch — v5.1-acquired; Season 3 ep 4–10 (Behance; legacy slug)",
    **_BEHANCE_BODY,
)

# --- Venmo live / episode-7-youtube (S3E7) ---
EPISODES["acq-episode-7-youtube"] = base(
    "acq-episode-7-youtube",
    review_notes="Manual GPT Acquired batch — v5.1-acquired; Season 3 ep 4–10",
    episode_rating={"overall": 3},
    keywords=["Social Payments", "PayPal M&A", "Network Effects"],
    conclusion=(
        "Andrew Kortina joins Ben and David live in San Francisco for Season 3 Episode 7 on Venmo — the social "
        "payments app he co-founded with Iqram Magdon in 2009 that turned P2P transfers into a public feed of "
        "emoji-laden payments. Braintree acquired Venmo in 2012 for ~$26.2M; PayPal bought Braintree in 2013 "
        "for ~$800M, making Venmo the consumer social layer PayPal lacked. By 2018 Venmo processed ~$62B+ "
        "annualized payment volume with monetization still emerging via Pay With Venmo and debit card. The episode "
        "dissects whether social graph is moat or novelty in payments — and why incumbents buy culture they "
        "cannot build inside risk-averse fintech orgs."
    ),
    background=(
        "Recorded as a live SF show, Kortina walks Venmo's origin at a 2009 jazz show where he forgot his wallet — "
        "building SMS-based P2P payments for roommates and friends. The signature social feed (public payment "
        "notes, emoji) created organic growth on college campuses before bank P2P (Zelle) existed.\n\n"
        "Hosts cover Braintree's developer-API business logic for buying Venmo, PayPal's post-acquisition "
        "integration struggles, fraud/risk constraints on social features, and comparisons to Square Cash, "
        "Apple Pay, and WeChat Pay. Kortina reflects on founder psychology and why Venmo stayed in NYC while "
        "recording in SF — East Coast fintech roots versus Silicon Valley payments infra."
    ),
    important_facts=[
        "Venmo founded 2009 by Andrew Kortina and Iqram Magdon; launched as SMS P2P payments with social feed "
        "showing payment notes — grew on US college campuses 2010–2012.",
        "Braintree acquired Venmo in August 2012 for ~$26.2M in stock — Braintree needed consumer brand beyond "
        "developer payment APIs.",
        "PayPal acquired Braintree (including Venmo) in September 2013 for ~$800M — Venmo became PayPal's "
        "consumer-social strategy versus Square and Apple Pay.",
        "Venmo payment volume cited ~$62B+ annualized by 2018 episode date — monetization via Pay With Venmo "
        "merchant button and Venmo debit card still early versus volume.",
        "Zelle (bank consortium) launched 2017 with ~$75B+ quarterly volume by 2018 — faster settlement inside "
        "bank apps but without Venmo's social engagement layer.",
    ],
    mental_model={
        "name": "Social Graph as Distribution in Commoditized Payments",
        "components": (
            "P2P money movement is commodity — banks and ACH always existed. Venmo's insight: payment notes and "
            "public feed create organic discovery and habit among 18–25 cohort. Social proof lowers trust barrier "
            "for sending money to friends. Monetization lags volume because social products resist charging users "
            "directly — Pay With Venmo taxes merchants instead. Acquirer logic: PayPal bought culture and MAU, "
            "not novel rails."
        ),
        "application": (
            "Consumer fintech: viral loop matters when rails are undifferentiated. Evaluate whether social "
            "features survive compliance scaling (fraud, privacy). Strategic buyers pay for demographic "
            "penetration PayPal's core brand could not reach. Watch Zelle-style bank coalitions as incumbent "
            "response copying speed without social."
        ),
    },
    competitive_advantage=(
        "Venmo owned young-adult P2P habit and brand verb ('Venmo me') — PayPal parentage added trust and "
        "regulatory licenses without killing UX. Social feed created engagement banks' Zelle lacks — users open "
        "app for content, not just transactions. College campus seeding built dense local networks before "
        "national scale.\n\n"
        "Braintree developer DNA preserved API quality; PayPal cross-sell to merchants via Pay With Venmo. "
        "Debit card extended Venmo balance into offline spend — closing monetization loop.\n\n"
        "Weaknesses: social feed novelty fades with age cohort; fraud and privacy scrutiny on public defaults. "
        "Monetization trailed ~$62B volume — ad-like social model hard in regulated payments. Zelle copied "
        "instant bank transfer inside existing apps. International expansion limited versus PayPal core.\n\n"
        "Versus Square Cash: Venmo social vs Cash App crypto/rewards diversification. Versus WeChat Pay: "
        "super-app integration China achieved; US app silos limit Venmo's scope. Episode captures pre-Cash App "
        "dominance era when Venmo was default Gen-Z payments."
    ),
    key_insights=[
        {
            "view": "Payments are commodity; social is distribution.",
            "question": "Why did Venmo beat bank P2P for years?",
            "answer": (
                "ACH existed; Venmo added frictionless UX plus public payment notes friends actually read. "
                "College density created local network effects — split rent, meals, tickets. Banks ignored "
                "18–25 demographic until 2017 Zelle consortium. Social feed was marketing channel with zero "
                "CAC — users acquired users via emoji payments."
            ),
        },
        {
            "view": "Braintree bought consumer brand for API business.",
            "question": "Why acquire for ~$26M?",
            "answer": (
                "Braintree powered Uber, Airbnb developer payments — needed consumer-facing asset for investor "
                "narrative and fraud-data diversity. Venmo MAU complemented merchant APIs. ~$26.2M looked "
                "cheap before volume scaled to ~$62B — classic nested acquisition creating PayPal optionality."
            ),
        },
        {
            "view": "PayPal bought Venmo via Braintree, not organically.",
            "question": "Why couldn't PayPal build Venmo internally?",
            "answer": (
                "PayPal brand skewed older and merchant-focused; internal teams killed social features on "
                "compliance fears. Acquiring Braintree/Venmo imported culture and youth MAU. ~$800M Braintree "
                "price looks strategic in hindsight as Venmo became Gen-Z on-ramp — acqui-hire-at-scale pattern."
            ),
        },
        {
            "view": "Monetization intentionally lagged engagement.",
            "question": "Why low revenue on ~$62B volume?",
            "answer": (
                "Venmo waived P2P fees to grow network; Pay With Venmo merchant take rate and debit interchange "
                "arrived later. Social apps risk churn if you tax users directly. PayPal tolerated subsidy while "
                "chasing lifetime value — mirrors consumer social growth-before-revenue playbook in regulated "
                "category with fraud costs."
            ),
        },
        {
            "view": "Zelle is functional response without social soul.",
            "question": "Does Zelle threaten Venmo?",
            "answer": (
                "Zelle hit ~$75B+ quarterly volume by 2018 inside bank apps — instant settlement advantage. "
                "Lacks Venmo feed and brand verb among under-30 users. Kortina argues habit and identity matter "
                "until cohort ages into bank-primary apps. Long-term: Cash App added crypto/stocks; Venmo needed "
                "feature expansion beyond P2P — episode records pre-Cash App surge."
            ),
        },
    ],
    top_investment_implications=[
        {
            "ticker": "PYPL",
            "direction": "Watch",
            "confidence": "Medium",
            "thesis": (
                "Venmo volume scale with lagging monetization — episode frames PayPal's consumer retention bet; "
                "track Pay With Venmo penetration versus Cash App and Zelle in under-35 demographics."
            ),
        },
    ],
    golden_quotes=[
        "\"We built Venmo because I forgot my wallet at a jazz show\" — Kortina origin story.",
        "\"PayPal bought the social graph it couldn't build\" — hosts on ~$800M Braintree acquisition logic.",
        "\"Zelle is faster; Venmo is where your friends are\" — on engagement versus settlement speed.",
    ],
    chronology={
        "subject": "Venmo · Andrew Kortina · PayPal",
        "events": [
            {"date": "2009", "event": "Kortina and Magdon found Venmo — SMS P2P with social feed"},
            {"date": "2010–2012", "event": "College campus growth; iPhone app scales"},
            {"date": "2012-08", "event": "Braintree acquires Venmo for ~$26.2M"},
            {"date": "2013-09", "event": "PayPal acquires Braintree for ~$800M"},
            {"date": "2014", "event": "Public feed privacy defaults revised after scrutiny"},
            {"date": "2016", "event": "Pay With Venmo merchant product expands"},
            {"date": "2017", "event": "Zelle bank consortium launches competitive P2P"},
            {"date": "2018", "event": "Acquired live SF episode; ~$62B+ annualized volume cited"},
            {"date": "2018", "event": "Venmo debit card ships — offline monetization"},
            {"date": "2020+", "event": "Cash App competition intensifies; Venmo adds crypto and rewards"},
        ],
    },
)

# --- Netflix Part 1 (S3E8) ---
EPISODES["acq-netflix-part-1"] = base(
    "acq-netflix-part-1",
    review_notes="Manual GPT Acquired batch — v5.1-acquired; Season 3 ep 4–10",
    episode_rating={"overall": 4},
    keywords=["DVD-by-Mail", "Counter-Positioning", "Blockbuster Battle"],
    conclusion=(
        "Ben and David open Netflix's two-part history with Reed Hastings and Marc Randolph's 1997 DVD-by-mail "
        "startup — counter-positioning Blockbuster's late-fee profit pool (~$800M at peak, ~40% of revenue per "
        "Helmer framing) with no due dates and subscription simplicity. Barry McCarthy joined as CFO from Music "
        "Express, bringing unit-economics discipline and later Spotify direct-listing fame. Blockbuster passed "
        "on buying Netflix for ~$50M in 2000; Netflix IPO'd May 2002 at ~$1B market cap. By shipping DVDs from "
        "regional warehouses with Cinematch recommendations, Netflix built a logistics-and-data moat before "
        "streaming existed — setting up Part 2's content pivot."
    ),
    background=(
        "Season 3 Episode 8 traces Netflix from Hastings' Pure Software sale through the infamous late-fee "
        "inspiration (Apollo 13 Blockbuster fine), Marc Randolph co-founder dynamics, and 1998 launch.\n\n"
        "Hosts explain per-rental vs subscription pricing experiments, warehouse density improving delivery "
        "speed, and Ted Sarandos joining content acquisition. Blockbuster Online responses and internal politics "
        "at Blockbuster (Viacom ownership) show incumbent failure modes. McCarthy's CFO hire and Tom Dillon ops "
        "leadership mirror Amazon Prime logistics lessons — faster delivery increased retention. Episode ends as "
        "streaming experiments begin, teeing up Part 2."
    ),
    important_facts=[
        "Netflix founded 1997 by Reed Hastings and Marc Randolph; launched DVD-by-mail 1998 with no late fees "
        "versus Blockbuster's ~$40M+ monthly late-fee revenue stream (often cited ~40% of profit).",
        "Blockbuster declined to acquire Netflix for ~$50M in 2000 — inflection point hosts grade as catastrophic "
        "incumbent error.",
        "Netflix IPO May 23, 2002 — ~5.5M shares at ~$15, ~$1B market cap; Barry McCarthy CFO from 1999 brought "
        "subscription unit-economics rigor.",
        "By 2005 Netflix shipped ~1M DVDs per day from ~50 regional warehouses — delivery speed correlated with "
        "lower churn (Amazon Prime parallel).",
        "Marc Randolph stepped down as CEO in 1999; Hastings became sole CEO — Randolph remained early architect "
        "of culture and testing methodology.",
    ],
    mental_model={
        "name": "Counter-Positioning on Incumbent Profit Pool",
        "components": (
            "Blockbuster monetized late fees (~$800M peak industry-wide) and per-rental friction. Netflix "
            "subscription with no due dates poisoned that revenue line — Blockbuster could not match without "
            "cannibalizing stores. Warehouse density + Cinematch increased engagement per shipped DVD, improving "
            "unit economics versus video-store real estate. Data flywheel preceded streaming: ratings improved "
            "marginal selection cost. Helmer counter-positioning: structural, not execution."
        ),
        "application": (
            "Identify which incumbent revenue lines your model zeroes — if >30% of profit, expect slow response. "
            "Netflix applied Amazon logistics lesson (delivery speed → retention) to physical media. CFO hire "
            "with subscription expertise (McCarthy) early signals unit-economics discipline wins over growth-at-all-costs "
            "in rental businesses."
        ),
    },
    competitive_advantage=(
        "Netflix's early moat combined no-late-fee subscription positioning, regional warehouse network (~50 sites "
        "by mid-2000s), and Cinematch collaborative filtering — engagement per DVD exceeded store browsing. "
        "No retail real estate cap-ex versus Blockbuster's ~9,000 stores. Direct customer relationship enabled "
        "pricing experiments (per-rental → subscription tiers).\n\n"
        "Barry McCarthy institutionalized contribution margin analysis — knowing which subscribers were profitable "
        "by shipping cost zone. Ted Sarandos content relationships later extended moat to licensing (pre-originals).\n\n"
        "Weaknesses: USPS dependency; studio windowing power; Blockbuster brand still dominated impulse rental "
        "until 2005–2007. DVD shipping economics capped TAM versus streaming eventual unlimited consumption. "
        "Incumbent could have acquired for ~$50M — classic disruption blind spot.\n\n"
        "Versus Blockbuster Online: late internal launch, cannibalization fear. Versus Amazon DVD mail: Netflix "
        "focus beat generalist. Part 1 ends before streaming proves second counter-positioning."
    ),
    key_insights=[
        {
            "view": "Late fees were Blockbuster's poison pill to match.",
            "question": "Why couldn't Blockbuster copy subscription?",
            "answer": (
                "Late fees ~$40M+/month (~40% profit) funded store footprint. Zero-late-fee subscription "
                "required abandoning core cash cow — classic counter-positioning. Internal teams proposed "
                "acquisitions (~$50M Netflix offer rejected); store managers resisted cannibalization. By 2005 "
                "Blockbuster Online launched years late with hybrid model preserving fees."
            ),
        },
        {
            "view": "Warehouse density was Amazon Prime for DVDs.",
            "question": "Why did delivery speed matter?",
            "answer": (
                "~50 regional warehouses let Netflix ship ~1M DVDs/day with 1-day turnaround in dense zones — "
                "faster delivery correlated with lower churn (McCarthy metrics). Same insight as Amazon Prime: "
                "logistics is retention product. Blockbuster stores offered instant gratification but worse "
                "selection breadth."
            ),
        },
        {
            "view": "McCarthy was the CFO superhero.",
            "question": "Why highlight Barry McCarthy?",
            "answer": (
                "Joined 1999 from Music Express — brought subscription finance discipline, later executed Spotify "
                "direct listing (Acquired Season 2). At Netflix he modeled cohort LTV by shipping zone before "
                "SaaS metrics were fashionable. Proves CFO hire can be strategic weapon in consumer subscription "
                "businesses."
            ),
        },
        {
            "view": "$50M rejection is canonical M&A failure.",
            "question": "What if Blockbuster bought Netflix?",
            "answer": (
                "2000 offer ~$50M rejected by Blockbuster leadership — Netflix later exceeded $100B+ peak market "
                "cap. Even partial acquisition could have captured DVD-by-mail transition. Hosts grade F for "
                "Blockbuster — incumbent dismissed dot-com experiment during dot-com crash psychology."
            ),
        },
        {
            "view": "Data preceded streaming pivot.",
            "question": "Was Cinematch strategic?",
            "answer": (
                "Collaborative filtering increased discs-per-subscriber — critical when postage was variable cost. "
                "Viewing taste graph became foundation for streaming recommendations and later originals greenlight "
                "(House of Cards data). Netflix was data company wearing DVD-mail skin — Part 2 exploits asset."
            ),
        },
    ],
    top_investment_implications=[
        {
            "ticker": "NFLX",
            "direction": "Watch",
            "confidence": "Medium",
            "thesis": (
                "Part 1 establishes counter-positioning DNA and data flywheel — framework for judging whether "
                "streaming content spend retains structural advantage versus commoditized distribution."
            ),
        },
    ],
    golden_quotes=[
        "\"Blockbuster made $800 million a year on late fees\" — Hastings on the profit pool Netflix attacked.",
        "\"They offered to buy us for $50 million — Blockbuster said no\" — canonical incumbent rejection.",
        "\"Barry McCarthy is an Acquired superhero\" — on CFO hire linking Netflix and Spotify episodes.",
    ],
    chronology={
        "subject": "Netflix · Reed Hastings (Part 1 — DVD era)",
        "events": [
            {"date": "1997", "event": "Netflix founded — Hastings and Marc Randolph"},
            {"date": "1998", "event": "DVD-by-mail launches — no late fees model"},
            {"date": "1999", "event": "Barry McCarthy joins as CFO; Randolph steps down as CEO"},
            {"date": "2000", "event": "Blockbuster declines ~$50M acquisition offer"},
            {"date": "2002-05", "event": "Netflix IPO — ~$1B market cap"},
            {"date": "2003", "event": "Ted Sarandos joins content acquisition"},
            {"date": "2005", "event": "~1M DVDs shipped daily; ~50 warehouse network"},
            {"date": "2005", "event": "Blockbuster Online launches — late competitive response"},
            {"date": "2007", "event": "Streaming introduced — tee for Part 2"},
            {"date": "2018", "event": "Acquired Part 1 publishes — DVD history canon"},
        ],
    },
)

# --- Netflix Part 2 (S3E9) ---
EPISODES["acq-netflix-part-2"] = base(
    "acq-netflix-part-2",
    review_notes="Manual GPT Acquired batch — v5.1-acquired; Season 3 ep 4–10",
    episode_rating={"overall": 4},
    keywords=["Streaming Pivot", "Qwikster", "Original Content"],
    conclusion=(
        "Part 2 chronicles Netflix's streaming transformation: 2007 Watch Now launch, Reed Hastings' 2011 "
        "Qwikster debacle (60% price hike, DVD business spin-out, ~800K subscriber loss in one quarter), and "
        "rebirth as a global media company spending $8B–$12B+ annually on content by late 2010s. House of Cards "
        "(2013) validated data-driven originals; global licensing built audience before local production. "
        "Netflix rejoined FAANG market-cap peers by 2018 after 2011–2012 stock collapse. Ben and David frame "
        "Qwikster as pricing-strategy error, not streaming-strategy error — the pivot was inevitable, the "
        "communication catastrophic. Content became moat when distribution commoditized."
    ),
    background=(
        "Season 3 Episode 9 picks up at 2007 streaming beta through 2018 global expansion. Hosts dissect "
        "Qwikster: separate DVD and streaming brands, price increases up to 60%, Hastings apology video "
        "(parodied on SNL), and board turmoil.\n\n"
        "Recovery arc covers Ted Sarandos originals strategy (House of Cards, Orange Is the New Black), "
        "Marvel/Disney licensing tensions, international market entry (130+ countries by 2016), and tech "
        "culture (Chaos Monkey, AWS infrastructure). FAANG chart comparisons show Netflix's market-cap "
        "recovery. Episode links Benedict Evans aggregation theory and Netflix's shift from tech-multiple "
        "to media-multiple investor framing."
    ),
    important_facts=[
        "Netflix streaming launched 2007 as 'Watch Now' — years before Blockbuster filed bankruptcy (2010) "
        "and while DVD still majority of Netflix revenue.",
        "Qwikster announced September 2011 — DVD service rebranded and split; combined price hikes up to ~60%; "
        "~800K net subscriber loss in Q3 2011; Hastings reversed DVD split within weeks.",
        "House of Cards premiered February 2013 — $100M+ committed for two seasons upfront; data-driven "
        "greenlight from viewership clusters (Fincher, Spacey, political drama fans).",
        "2016: Netflix available in 130+ countries — global expansion before local originals scale; content "
        "spend approached ~$8B annually by 2017 (grew toward ~$12B+ by 2018).",
        "Netflix stock fell from ~$300 split-adjusted highs pre-Qwikster to ~$50–70 range in 2012 before "
        "10-year bull run back into FAANG peer market caps by 2018.",
    ],
    mental_model={
        "name": "Distribution to Content Vertical Integration",
        "components": (
            "When streaming distribution commoditizes (every studio launches OTT), rights holders capture value "
            "— Netflix pivoted from licensed catalog to owned originals. Data from 100M+ subscribers informs "
            "greenlight reducing Hollywood greenlight risk. Global subscriber scale amortizes $100M show bets "
            "across 190 countries — studio competitors used domestic-only models. Qwikster lesson: right strategy "
            "(streaming focus) wrong pricing packaging — subscriber trust is balance-sheet asset."
        ),
        "application": (
            "Platform shifts require communication discipline — separate price hikes from product unbundling. "
            "Original content is moat when suppliers become competitors (Disney+, HBO Max). Evaluate streaming "
            "investments by global ARPU × subscriber ceiling, not US box office comps. Tech infrastructure "
            "(AWS, Chaos Monkey) enabled media pivot — dual competency rare."
        ),
    },
    competitive_advantage=(
        "Post-recovery Netflix stacked global distribution (130+ countries), recommendation data at 100M+ "
        "subscriber scale, and originals pipeline (House of Cards, Stranger Things, international local content). "
        "First-mover on binge-release format changed TV cadence. No ads preserved UX versus Hulu early model.\n\n"
        "Tech culture (Chaos Monkey resiliency, CDN optimization) reduced streaming friction competitors "
        "matched slowly. Brand synonymous with streaming — verb status in culture.\n\n"
        "Weaknesses: content costs rising as studios pulled licenses; debt-funded content spend; Qwikster proved "
        "trust fragility. Media multiples lower than pure-tech. Regional competitors (Hotstar, etc.) and later "
        "password-sharing crackdown headwinds post-episode. Disney+ launch (2019) ended easy licensing era.\n\n"
        "Versus HBO: Netflix volume vs HBO prestige before HBO Max. Versus Amazon Prime Video: Netflix dedicated "
        "vs bundle subsidy. Qwikster remains case-study in separating strategic pivot from customer communication."
    ),
    key_insights=[
        {
            "view": "Qwikster was packaging failure, not streaming mistake.",
            "question": "Why did ~800K subscribers leave?",
            "answer": (
                "September 2011: 60% combined price hike plus confusing DVD/streaming split branded Qwikster. "
                "Users punished perceived double-charging, not streaming direction. Hastings apology video "
                "became cautionary tale — right long-term bet (streaming), catastrophic short-term execution. "
                "Stock dropped ~75% from peak; recovery took years but strategy vindicated."
            ),
        },
        {
            "view": "House of Cards proved data-driven originals.",
            "question": "Why commit $100M before pilot?",
            "answer": (
                "Viewing data showed overlap among Fincher fans, political drama watchers, Kevin Spacey "
                "affinity — greenlight two seasons upfront without pilot. Traditional TV required pilot season; "
                "Netflix amortized bet across global subscriber base. Model later copied by every streamer — "
                "data as greenlight committee."
            ),
        },
        {
            "view": "Global licensing preceded local production.",
            "question": "How did international expansion work?",
            "answer": (
                "2016 launch in 130+ countries used licensed catalog while originals scale ramped — subscribers "
                "added before local content spend required. Global ARPU lower than US but TAM 5× — amortize "
                "$8B–$12B content across world. Competitors launched country-by-country; Netflix big-bang "
                "distribution blitz."
            ),
        },
        {
            "view": "Studios became competitors — vertical integration mandatory.",
            "question": "Why shift from licensed to owned content?",
            "answer": (
                "Disney, Warner, NBCU pulled catalog as they launched DTC apps — Netflix's licensed moat eroded. "
                "Owned originals only defensible long-term asset; content spend rose toward ~$12B+ by 2018. "
                "Trade-off: media company margins vs tech multiples. Episode previews Disney+ 2019 threat."
            ),
        },
        {
            "view": "FAANG membership was market-cap validation.",
            "question": "Did Netflix recover from Qwikster?",
            "answer": (
                "2012 stock ~$50–70 split-adj versus 2011 ~$300 pre-crash; by 2018 Netflix rejoined Apple, "
                "Amazon, Google, Facebook peer charts (Benedict Evans FAANG). Subscriber growth to 130M+ "
                "global and content awards rebuilt investor narrative — execution after apology mattered more "
                "than apology itself."
            ),
        },
    ],
    top_investment_implications=[
        {
            "ticker": "NFLX",
            "direction": "Watch",
            "confidence": "Medium",
            "thesis": (
                "Part 2 frames content-spend moat versus studio verticalization — monitor subscriber net adds, "
                "content amortization per sub, and ad-tier pivot post-password-sharing era."
            ),
        },
    ],
    golden_quotes=[
        "\"Qwikster will go down in business school history\" — on 2011 pricing and spin-out disaster.",
        "\"We committed $100 million to House of Cards without a pilot\" — Sarandos data-driven originals bet.",
        "\"They're a media company now, not a tech company\" — hosts on investor reframing by 2018.",
    ],
    chronology={
        "subject": "Netflix · Streaming era (Part 2)",
        "events": [
            {"date": "2007", "event": "Watch Now streaming launches alongside DVD"},
            {"date": "2010", "event": "Blockbuster bankruptcy — physical rental era ends"},
            {"date": "2011-09", "event": "Qwikster announced — price hikes and DVD split"},
            {"date": "2011-Q3", "event": "~800K subscriber loss; Hastings apology video"},
            {"date": "2011-10", "event": "Qwikster reversed — DVD stays under Netflix brand"},
            {"date": "2013-02", "event": "House of Cards premieres — $100M+ two-season bet"},
            {"date": "2013", "event": "Orange Is the New Black — originals slate expands"},
            {"date": "2016", "event": "Global launch — 130+ countries in one move"},
            {"date": "2017–2018", "event": "Content spend ~$8B–$12B; FAANG market-cap peer recovery"},
            {"date": "2018-11", "event": "Acquired Part 2 publishes — streaming canon complete"},
        ],
    },
)

# --- Tencent (S3E10) ---
EPISODES["acq-season-3-episode-10-tencent"] = base(
    "acq-season-3-episode-10-tencent",
    review_notes="Manual GPT Acquired batch — v5.1-acquired; Season 3 ep 4–10",
    episode_rating={"overall": 4},
    keywords=["WeChat Super-App", "China Gaming", "Portfolio Investing"],
    conclusion=(
        "Ben and David close Season 3's China series with Tencent — Pony Ma's 1998 Shenzhen team evolving from "
        "pager software to QQ (900M+ peak PC IM users), WeChat (1B+ MAU super-app), and the world's largest "
        "gaming business via Riot (League of Legends), Epic (Fortnite), and domestic titles. Tencent's "
        "investment portfolio — Snap (~12%), Tesla (~5%), Spotify, and hundreds of stakes — makes it a "
        "shadow venture firm atop social distribution. 2018 market cap ranked among global top 10 (~$400B+ "
        "era). The episode frames Tencent as consumer OS in China: messaging, payments, gaming, and cloud "
        "in one conglomerate — with regulatory gaming-approval pauses and BAT rivalry as permanent overhang."
    ),
    background=(
        "Season 3 finale traces Pony Ma from pager-era software through QQ's avatar culture and mobile threat, "
        "Allen Zhang's 2011 WeChat launch (red envelopes, mini-programs), and gaming empire expansion.\n\n"
        "Hosts explain Tencent investment strategy (minority stakes in Snap, Tesla, Meituan, PDD), PC-to-mobile "
        "transition anxiety that produced WeChat, and government content regulation (gaming license freezes "
        "2018). Comparisons to Facebook (messaging), Activision (gaming revenue), and SoftBank (portfolio) "
        "abound. Mini-programs preview super-app model Western apps still chase."
    ),
    important_facts=[
        "Tencent founded 1998 in Shenzhen; Pony Ma and team built QQ instant messenger — peaked ~900M+ PC-era "
        "accounts before mobile transition.",
        "WeChat launched 2011 (Allen Zhang); grew to 1B+ MAU — super-app combining messaging, WeChat Pay, "
        "mini-programs, and social feeds; red envelope feature drove 2014 payment adoption.",
        "Tencent acquired Riot Games (League of Legends) for ~$400M in 2011; owns ~40% of Epic Games (Fortnite) — "
        "largest gaming revenue stream globally by 2018.",
        "Investment portfolio included ~12% of Snap (~$2B+ invested), ~5% Tesla stake, Spotify, Meituan, PDD — "
        "2018 market cap ~$400B+ placed Tencent among world's largest companies.",
        "China froze new game monetization licenses in 2018 — Tencent lost ~$200B+ market cap peak-to-trough "
        "on regulatory headline risk during episode recording month.",
    ],
    mental_model={
        "name": "Super-App Distribution + Portfolio Optionality",
        "components": (
            "WeChat is user OS in China — messaging, payments, mini-apps remove need for separate app installs. "
            "Traffic gateway monetizes via gaming, fintech, and cloud (Tencent Cloud). Minority investment stakes "
            "in global assets (Snap, Tesla, Epic) hedge domestic regulation and export learnings. QQ-to-WeChat "
            "transition shows incumbent must cannibalize PC success or die — Allen Zhang given autonomy to kill "
            "QQ mobile. Gaming social graphs feed WeChat identity."
        ),
        "application": (
            "Evaluate Chinese internet by super-app engagement minutes, not web traffic. Regulatory headline risk "
            "can wipe ~$200B market cap — size does not immunize. Western 'super-app' attempts lack payments + "
            "government-sanctioned mini-program platform — structural gap. Investors: Tencent = social utility + "
            "gaming cash flow + venture portfolio NAV."
        ),
    },
    competitive_advantage=(
        "Tencent's moat is WeChat ubiquity — 1B+ MAU with WeChat Pay embedded in daily life (P2P, merchants, "
        "utilities). Mini-programs let third parties run inside WeChat without App Store friction — developer "
        "platform Western messengers lack. QQ legacy brand still holds gaming and youth communities.\n\n"
        "Gaming division owns world's top PC MOBA (League of Legends) and major Fortnite stake — social gaming "
        "feeds back to WeChat login and friend graphs. Investment office secures stakes in emerging winners "
        "(Meituan, PDD) complementing organic growth.\n\n"
        "Weaknesses: government content and gaming approval control; domestic TAM capped by population; "
        "international WeChat limited to diaspora. Portfolio marks volatile (Snap, Tesla swings). Alibaba "
        "competes in payments and cloud; ByteDance attacks attention time. 2018 license freeze showed regulatory "
        "single-point failure.\n\n"
        "Versus Facebook: WeChat won payments China-wide; Messenger/WhatsApp monetize poorly by comparison. "
        "Versus Alibaba: social graph vs marketplace — different BAT strongholds. Episode caps China mini-series "
        "after Alibaba, setting BAT mental map for later Meituan/PDD/TikTok episodes."
    ),
    key_insights=[
        {
            "view": "WeChat won mobile by cannibalizing QQ.",
            "question": "Why build WeChat when QQ existed?",
            "answer": (
                "Mobile threatened PC IM — Allen Zhang's 2011 WeChat phone-first design with voice notes and "
                "address-book sync beat QQ mobile bolt-on. Pony Ma allowed internal competition; WeChat won. "
                "Lesson: incumbents must spawn independent teams with kill authority over legacy cash cow."
            ),
        },
        {
            "view": "Red envelopes hacked payments adoption.",
            "question": "How did WeChat Pay beat Alipay offline?",
            "answer": (
                "2014 Chinese New Year red envelope feature let users gift money in chat — hundreds of millions "
                "bound bank cards in days. Social use case beat Alipay's commerce-first wallet for P2P. Payments "
                "became messaging feature, not separate app — super-app integration Western fintech lacks."
            ),
        },
        {
            "view": "Gaming funds the empire.",
            "question": "Why is Riot/Epic strategically core?",
            "answer": (
                "Riot acquisition ~$400M (2011) for League of Legends — recurring gaming revenue with esports "
                "ecosystem. ~40% Epic stake captures Fortnite phenomenon. Gaming social graphs reinforce Tencent "
                "identity layer and cross-promote WeChat. Largest profit pool inside conglomerate diversifies "
                "beyond advertising."
            ),
        },
        {
            "view": "Investment portfolio is shadow Vision Fund.",
            "question": "Why own Snap and Tesla stakes?",
            "answer": (
                "~12% Snap and ~5% Tesla (2018 era) plus Spotify, Meituan — minority stakes export capital and "
                "learn global trends while hedging domestic regulation. Unlike SoftBank control plays, Tencent "
                "often takes passive stakes with strategic partnership. NAV can swing billions on US tech marks — "
                "conglomerate discount applies."
            ),
        },
        {
            "view": "Regulation is first-class risk.",
            "question": "What did 2018 gaming freeze teach?",
            "answer": (
                "Government paused commercial game licenses — Tencent lost ~$200B+ market cap from peak on "
                "headline. Size does not immunize against state industrial policy. Episode aired December 2018 "
                "during crackdown — hosts flag gaming and content approval as permanent overhang for BAT investors."
            ),
        },
    ],
    top_investment_implications=[
        {
            "ticker": "0700.HK",
            "direction": "Watch",
            "confidence": "Medium",
            "thesis": (
                "Super-app + gaming cash flow + portfolio NAV — monitor regulatory gaming/content approvals, "
                "WeChat payment share versus Alipay, and mark-to-market on listed stakes (Snap, Tesla)."
            ),
        },
        {
            "ticker": "META",
            "direction": "Watch",
            "confidence": "Low",
            "thesis": (
                "Episode contrasts WeChat payments/super-app success with Messenger monetization struggles — "
                "relevant for Meta messaging-commerce strategy globally."
            ),
        },
    ],
    golden_quotes=[
        "\"WeChat is the operating system of China\" — hosts on 1B+ MAU super-app scope.",
        "\"Red envelopes turned chat into a bank branch\" — on 2014 WeChat Pay adoption hack.",
        "\"Tencent is a venture firm with a messaging app attached\" — on Snap, Tesla, Epic portfolio strategy.",
    ],
    chronology={
        "subject": "Tencent · Pony Ma · WeChat",
        "events": [
            {"date": "1998", "event": "Tencent founded in Shenzhen — pager software origins"},
            {"date": "1999", "event": "QQ instant messenger launches — PC-era growth"},
            {"date": "2004", "event": "Tencent IPO on Hong Kong Stock Exchange"},
            {"date": "2011", "event": "WeChat launches under Allen Zhang — mobile-first messaging"},
            {"date": "2011", "event": "Acquires Riot Games (League of Legends) for ~$400M"},
            {"date": "2014", "event": "WeChat red envelope feature drives payment adoption"},
            {"date": "2017", "event": "WeChat mini-programs launch — super-app platform"},
            {"date": "2018", "event": "China freezes game licenses — Tencent market cap drops ~$200B+"},
            {"date": "2018", "event": "Portfolio stakes in Snap (~12%), Tesla (~5%), Epic (~40%)"},
            {"date": "2018-12", "event": "Acquired Season 3 finale — Tencent mega-episode"},
        ],
    },
)


def main() -> None:
    results: list[tuple[str, bool, int, str]] = []
    for ep_id, data in EPISODES.items():
        path = APPROVED / f"{ep_id}.json"
        path.write_text(json.dumps(data, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
        report = validate_summary(data, TMPL)
        status = "PASS" if report.passed else "FAIL"
        results.append((ep_id, report.passed, report.total_words, status))
        print(f"{status} {ep_id} words={report.total_words} min={report.min_total_words}")
        for issue in report.issues:
            print(f"  [{issue.severity}] {issue.section}: {issue.message}")

    print("\n--- Summary ---")
    for ep_id, passed, words, _ in results:
        print(f"{'completed' if passed else 'failed'}: {ep_id} ({words} words)")


if __name__ == "__main__":
    main()
