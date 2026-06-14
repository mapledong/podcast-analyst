#!/usr/bin/env python3
"""Write and validate 8 Acquired v5.1 approved JSON files (episodes 28–36 batch)."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))

from scripts._write_acq_batch_491_500_common import base  # noqa: E402
from src.template_config import template_path_for_podcast  # noqa: E402
from src.validate import load_template_config, validate_summary  # noqa: E402

APPROVED = ROOT / "data" / "approved"
PY = sys.executable
REVIEW = "Manual GPT Acquired batch v5.1 — episodes 28–36"

EPISODES: dict[str, dict] = {}

EPISODES["acq-episode-28-the-amazon-ipo-with-original-amazon-board-member-tom-alberg"] = base(
    "acq-episode-28-the-amazon-ipo-with-original-amazon-board-member-tom-alberg",
    review_notes=REVIEW,
    episode_rating={"overall": 4},
    keywords=["Long-Term Flywheel", "IPO Capital", "Founder Discipline"],
    conclusion=(
        "Tom Alberg joins Ben and David to walk through Amazon's May 15, 1997 IPO at $18/share — "
        "$54 million raised, $438 million initial market cap — less than three years after founding and "
        "two years after the July 1995 site launch. Revenue exploded from ~$500,000 in 1995 to $16 million "
        "in 1996 and $148 million in 1997; the flywheel (selection → experience → traffic → sellers → "
        "lower prices) was already legible in the S1. Frank Quattrone and Bill Gurley at Deutsche Bank led "
        "the deal; Jeff's first shareholder letter codified long-term thinking. Today Amazon trades near "
        "$363 billion (Dec 2016 recording) — not quite 1,000× the IPO cap but proof that going public "
        "enabled the capital and discipline to survive the dot-com crash and compound for decades."
    ),
    background=(
        "Episode 28 brings Madrona cofounder Tom Alberg — Amazon's first outside investor and longest-serving "
        "board member after Jeff — to retell the IPO arc. Jeff left D.E. Shaw in 1994; the site launched "
        "July 1995 after a year of build. Tom led the angel round before launch; Kleiner Perkins and John "
        "Doerr joined in 1996 with a formal three-person board. By late 1996 Joy Covey was CFO and the board "
        "chose a 1997 IPO when public markets were open.\n\n"
        "Deutsche Bank (Quattrone/Gurley) won lead-left over Goldman/Morgan Stanley. Shares priced at $18, "
        "traded to $23.50 day one, then drifted until Q2 1997 revenue of $28 million re-accelerated the stock. "
        "Tom discusses the 1999 $1.25 billion convertible debt that helped Amazon weather the bubble burst, "
        "and how early customer-obsession and market size conviction made the IPO inevitable rather than optional."
    ),
    important_facts=[
        "Amazon IPO: May 15, 1997 at $18/share — $54M raised, ~$438M market cap; closed first day at $23.50.",
        "Revenue: ~$500K (1995 first half-year), $16M (1996), $148M (1997 full year); Q2 1997 alone was $28M.",
        "Tom Alberg led the first angel round before the July 1995 launch; Kleiner Perkins led a 1996 venture round with John Doerr joining the board.",
        "Lead bankers: Frank Quattrone and Bill Gurley (then Deutsche Bank); associate Jeff Blackburn later joined Amazon's senior team.",
        "Dec 2016 market cap ~$363 billion versus ~$438M at IPO — Tom notes Jeff's 1997 letter said 'day one' for the internet and Amazon.",
    ],
    mental_model={
        "name": "Flywheel + Long-Term Public Markets",
        "components": (
            "Amazon's early model: superior selection and customer experience drive traffic, which attracts "
            "third-party sellers and lowers prices, reinforcing selection. Jeff's shareholder letter translated "
            "that loop into investor language before 'flywheel' was colloquial. Going public at ~$438M cap with "
            "hypergrowth funded expansion and set cultural expectations for decades-long investment. Debt in 1999 "
            "($1.25B convertible) forced cost discipline ahead of peers during the crash."
        ),
        "application": (
            "Founders targeting large markets need capital structures matching decade-long compounding — not "
            "just late-stage private rounds. IPO timing balances visibility, liquidity, and quiet-period "
            "constraints. Board members like Tom who bet on founder long-termism over near-term profitability "
            "patterns matter as much as metrics. Investors: read annual letters; Amazon's 1997 template still "
            "informs aggregation-theory winners."
        ),
    },
    competitive_advantage=(
        "Amazon's moat in 1997 was customer obsession at internet scale — not logistics prowess yet.\n\n"
        "Books were a $10B+ category with millions of SKUs impossible in physical stores; online selection "
        "was the wedge. Repeat purchase behavior and word-of-mouth lowered acquisition cost versus TV-era "
        "retail. Jeff understood infinite distribution and low marginal delivery cost before most incumbents.\n\n"
        "Public listing added brand credibility for suppliers and recruits. Post-IPO AWS and marketplace "
        "layers compounded the original loop — but the 1997 advantage was simply 'best experience wins' in a "
        "vast, under-penetrated market.\n\n"
        "Weaknesses then: no profits, single category, bubble-dependent capital markets. Survivors needed "
        "balance-sheet flexibility — Amazon's 1999 debt and frugality culture (door desks) became advantages "
        "when rivals vanished."
    ),
    key_insights=[
        {
            "view": "IPO was the only path at Amazon's burn and ambition.",
            "question": "Could Amazon have stayed private longer?",
            "answer": "Tom and the hosts conclude alternatives were exhausted — growth required public capital and "
            "the 1997 window was open. Private late-stage markets of the 2010s did not exist; Jeff's long-term "
            "stance needed shareholders who opted in via the S1 narrative, not just angels.",
        },
        {
            "view": "Flywheel was investor-ready before AWS.",
            "question": "Did early investors see beyond books?",
            "answer": "The S1 and Jeff's letter framed selection and experience loops applicable to any category. "
            "Tom emphasizes large-market math: even with execution risk, bookstore TAM justified aggressive "
            "reinvestment. Everything-store expansion was implicit in the model, not a surprise pivot.",
        },
        {
            "view": "Quattrone/Gurley bank choice was contrarian.",
            "question": "Why Deutsche Bank, not Goldman?",
            "answer": "Facebook-era jockeying between Goldman and Morgan Stanley contrasts with Amazon picking "
            "Quattrone's team. Relationship and analyst quality (Gurley later at Benchmark) mattered; IPO fees "
            "were table stakes versus ongoing investor access.",
        },
        {
            "view": "Convertible debt saved the culture.",
            "question": "How did Amazon survive the bubble burst?",
            "answer": "1999's $1.25B convertible provided runway and creditor pressure to cut costs before "
            "emergency layoffs killed peers. Stock fell toward ~$5 but operating discipline learned in 2000–2002 "
            "enabled later M&A (Zappos, Quidsi) when targets were distressed.",
        },
        {
            "view": "Tom's pattern-match lesson for VCs.",
            "question": "What does Madrona look for post-Amazon?",
            "answer": "Tom seeks founders with long-term genetic commitment — not every company goes public, but "
            "sell-out when a wave is building forfeits compounding. Amazon's IPO grade is reflexively an A because "
            "alternative histories feel unnatural.",
        },
    ],
    top_investment_implications=[
        {
            "ticker": "AMZN",
            "direction": "Watch",
            "confidence": "Medium",
            "thesis": "Canonical case study in public-market compounding — monitor AWS/retail mix and whether "
            "corporate innovation (AWS-scale bets) continues under post-Bezos leadership.",
        }
    ],
    golden_quotes=[
        "\"You get the investors you ask for\" — Tom on Jeff shaping Amazon's patient shareholder base via the "
        "annual letter.",
        "\"Day one for the internet and for Amazon\" — Jeff's 1997 shareholder letter framing decades of investment.",
        "\"It feels unnatural to think about an alternative history\" — Ben on grading an IPO with 800×+ outcome.",
    ],
    chronology={
        "subject": "Amazon · founding through IPO",
        "events": [
            {"date": "1994", "event": "Jeff Bezos leaves D.E. Shaw; Amazon founded in Seattle"},
            {"date": "Jul 1995", "event": "Amazon.com launches after ~1 year of site build"},
            {"date": "1995", "event": "~$500K revenue in first half-year of operations"},
            {"date": "1996", "event": "Kleiner Perkins round; John Doerr joins board; $16M revenue"},
            {"date": "Late 1996", "event": "Joy Covey hired as CFO; board prepares for IPO"},
            {"date": "May 15, 1997", "event": "IPO at $18/share; $438M market cap; raises $54M"},
            {"date": "Summer 1997", "event": "Q2 revenue $28M reignites stock after post-IPO drift"},
            {"date": "1997", "event": "First Jeff Bezos annual shareholder letter published"},
            {"date": "1999", "event": "$1.25B convertible debt — last primary capital before bubble burst"},
            {"date": "2000–02", "event": "Dot-com crash; stock near $5; survival and cost discipline"},
            {"date": "Dec 2016", "event": "~$363B market cap as episode records — Tom as board veteran"},
        ],
    },
)

EPISODES["acq-episode-30-pa-semi-authentec"] = base(
    "acq-episode-30-pa-semi-authentec",
    review_notes=REVIEW,
    episode_rating={"overall": 4},
    keywords=["Vertical Integration", "ARM Silicon", "TouchID Security"],
    conclusion=(
        "Ben and David pair Apple's 2008 P.A. Semi acquisition ($278M cash) with its 2012 AuthenTec buy "
        "($356M, ~58% premium) to explain the A-series chip and TouchID secure enclave inside the iPhone. "
        "P.A. Semi founder Dan Dobberpuhl — StrongARM legend — was blindsided by Apple's 2005 Intel Mac switch "
        "but his team accelerated the in-house ARM project that debuted in the 2010 iPad A4. AuthenTec's "
        "decade of fingerprint R&D shipped in the iPhone 5s (~1 year post-close) and underpins Apple Pay. "
        "David estimates ~720M iPhone 4–6 units at ~$600 ASP — 5% attribution to silicon/security still "
        "implies ~$10B incremental gross profit versus ~$634M deal spend. Grade: A- for execution; open "
        "question whether on-device ML wins the next wave versus cloud-first rivals."
    ),
    background=(
        "Episode 30 marks Acquired #30 and the iPhone's 10th anniversary by covering two semiconductor deals. "
        "P.A. Semi (Palo Alto Semiconductor → Santa Clara) raised ~$86M building ultra-low-power PowerPC chips; "
        "Apple bought them in 2008 after Samsung supplied early iPhone processors. AuthenTec spun from Harris "
        "Corp (Melbourne, FL) in 1998, went public 2007, and sold to Apple July 2012 days after Samsung "
        "announced a flagship fingerprint partnership.\n\n"
        "Hosts explain ARM vs x86 for listeners: mobile's power budget favors ARM. Apple stopped P.A. Semi's "
        "standalone products and put the team on internal ARM work. AuthenTec's secure enclave processes "
        "TouchID locally — never hitting main CPU or servers — enabling FBI standoffs and Apple Pay trust."
    ),
    important_facts=[
        "P.A. Semi acquired April 2008 for $278M cash; had raised ~$86M; only shipped one PowerPC chip before Apple killed standalone roadmap.",
        "AuthenTec acquired July 27, 2012 for $356M — ~58% premium over market; $20M termination fee; Samsung had just announced flagship fingerprint integration.",
        "A4 chip introduced with original iPad (2010); iPhone 4 generation onward used Apple silicon path; first iPhones used Samsung processors.",
        "David estimates iPhone 4 through 6 sold ~720M units at ~$600 ASP; 5% feature attribution → ~$10B incremental gross profit vs ~$634M combined deal cost.",
        "Geekbench cited: A10 Fusion single-core performance rivals Intel laptop CPUs — Apple silicon trajectory from 416 MHz Samsung iPhone 1 chip.",
    ],
    mental_model={
        "name": "Own the Stack Where Differentiation Lives",
        "components": (
            "Apple buys talent (P.A. Semi — Dan Dobberpuhl) and mature technology (AuthenTec) when horizontal "
            "suppliers cannot deliver integrated security/performance. Secure enclave + TouchID + Apple Pay form "
            "a vertically integrated trust layer Android OEMs struggle to replicate. Fabless model kept capex low "
            "($86M raised at P.A. Semi). Timing: wave of smartphone maturation rewarded custom silicon; next wave "
            "(ML services) may favor cloud data, not on-device differential privacy."
        ),
        "application": (
            "Platform companies should internalize components that touch user trust or 10× experience gaps — "
            "not entire supply chains. Startups should stand on giants' shoulders; Apple-scale firms must "
            "transition like Google (TPU/data centers) or Amazon (AWS). M&A: people deals vs technology deals "
            "need different integration playbooks (P.A. Semi vs AuthenTec retention)."
        ),
    },
    competitive_advantage=(
        "Apple's integrated silicon + biometrics moat is privacy, performance, and payment trust in one package.\n\n"
        "A-series control lets Apple tune watch (S2), AirPods (W1), and T-bar (T1) from a common architecture "
        "— competitors buy Qualcomm/MediaTek bundles. Secure enclave isolation meant San Bernardino FBI could not "
        "compel remote fingerprint extraction.\n\n"
        "AuthenTec snatched from Samsung at premium price removed Android's near-term parity on payments-grade "
        "fingerprinting. P.A. Semi talent accelerated Samsung independence — critical when supplier is also "
        "competitor.\n\n"
        "Weaknesses: Apple services/ML DNA lags Google; differential privacy on-device may lose versus data-rich "
        "cloud models. Smartphone power gains face diminishing returns — 'what got you here won't get you there' "
        "for next computing wave."
    ),
    key_insights=[
        {
            "view": "Two deals, two integration modes.",
            "question": "People vs technology acquisition?",
            "answer": "P.A. Semi was a talent grab — existing ARM project accelerated by low-power legends. AuthenTec "
            "was buy-the-R&D: un-Apple go-to-market (HP SimplePass logos on website) but decade of fingerprint IP "
            "shipped in iPhone 5s within ~12 months of close.",
        },
        {
            "view": "Intel Mac pivot nearly killed P.A. Semi.",
            "question": "Why acquire a PowerPC shop after Intel switch?",
            "answer": "WWDC 2005 Intel announcement blew up P.A. Semi's MacBook bid; Apple still bought the team "
            "in 2008 for iPhone trajectory as Samsung supplier conflict loomed. Hidden ARM project became A4.",
        },
        {
            "view": "Samsung loss was strategic.",
            "question": "Why pay 58% premium for AuthenTec?",
            "answer": "Samsung had announced flagship fingerprint deal July 2012; Apple closed July 27. ~$356M is "
            "tiny versus iPhone gross profit pool; hosts fault Samsung for not counter-bidding. Payment roots in "
            "AuthenTec NFC work were under-reported at announcement.",
        },
        {
            "view": "ROI math supports A- not NeXT-tier.",
            "question": "How good were these acquisitions financially?",
            "answer": "David's 5% attribution on 720M units × $600 ASP × ~40% gross margin ≈ $10B vs $634M spend "
            "(plus ~$500M follow-on semi acquisitions). Massive win for 2010–2014 iPhone era; less clear for AR/ML "
            "future where Apple lacks data-scale services.",
        },
        {
            "view": "Alan Kay quote applies.",
            "question": "Software serious → own hardware?",
            "answer": "Google (TPU, data centers), Amazon (AWS), Microsoft, Facebook follow same pattern at scale. "
            "Xiaomi tried too early. Apple modular supply chain elsewhere; silicon/biometrics are where vertical "
            "integration pays.",
        },
    ],
    top_investment_implications=[
        {
            "ticker": "AAPL",
            "direction": "Watch",
            "confidence": "Medium",
            "thesis": "Custom silicon still differentiates iPhone margins; monitor whether on-device AI strategy "
            "keeps pace with cloud ML leaders as smartphone unit growth matures.",
        }
    ],
    golden_quotes=[
        "\"Apple buys smaller technology companies from time to time\" — standard Steve Dowling acquisition statement on AuthenTec.",
        "\"If you're really serious about software, you need to make your own hardware\" — Alan Kay, quoted via Steve Jobs.",
        "\"What got you here won't get you there\" — Ben on whether silicon leadership transfers to ML-services era.",
    ],
    chronology={
        "subject": "Apple silicon & TouchID acquisitions",
        "events": [
            {"date": "1998", "event": "AuthenTec spun out of Harris semiconductor division"},
            {"date": "2003", "event": "P.A. Semi founded (Palo Alto Semiconductor)"},
            {"date": "Jun 2005", "event": "WWDC: Apple announces Intel Mac switch — blindsides P.A. Semi"},
            {"date": "2007", "event": "AuthenTec goes public; iPhone launches with Samsung CPU"},
            {"date": "Apr 2008", "event": "Apple acquires P.A. Semi for $278M"},
            {"date": "2010", "event": "A4 chip debuts in original iPad"},
            {"date": "Jul 2012", "event": "Samsung announces AuthenTec fingerprint deal"},
            {"date": "Jul 27, 2012", "event": "Apple acquires AuthenTec for $356M (~58% premium)"},
            {"date": "Sep 2013", "event": "iPhone 5s ships with TouchID"},
            {"date": "2016", "event": "A10 Fusion rivals Intel laptop single-core per Geekbench"},
            {"date": "2017", "event": "Episode records; hosts debate ML-wave readiness"},
        ],
    },
)

EPISODES["acq-episode-31-the-uber-didi-chuxing-merger-with-brad-stone-author-of-the-upstarts-the-everything-store"] = base(
    "acq-episode-31-the-uber-didi-chuxing-merger-with-brad-stone-author-of-the-upstarts-the-everything-store",
    review_notes=REVIEW,
    episode_rating={"overall": 4},
    keywords=["China Rideshare War", "Scorched Earth", "Strategic Retreat"],
    conclusion=(
        "Brad Stone joins to dissect Uber's 2016 surrender in China: after burning ~$2 billion, Uber sold "
        "its China operations to Didi for a 17% stake plus a $1 billion Didi investment in Uber — netting "
        "roughly 2–3× cash deployed in illiquid equity. The war featured 30+ copycat apps, Tencent backing "
        "Didi and Alibaba Kuaidi, subsidies so deep drivers earned more than riders paid, and Didi investing "
        "in Lyft/Ola/Grab as a global anti-Uber alliance. Hosts grade B+ for both sides: rational truce, but "
        "scorched-earth culture left weak moats. Brad's The Upstarts frames Travis Kalanick and Cheng Wei "
        "as equally relentless with opposite public personas — a cautionary tale on capital as faux advantage."
    ),
    background=(
        "Episode 31 welcomes Bloomberg's Brad Stone (The Everything Store, The Upstarts) to cover the "
        "Uber–Didi merger — under-covered in Western press despite shaping global rideshare. Chinese "
        "entrepreneurs copied Hailo before UberX existed; Didi and Kuaidi merged in ~700 days after raising "
        "billions from BAT (Baidu, Alibaba, Tencent). Uber tested China clandestinely from 2013, launched "
        "with Baidu maps, hit ~30% share, and Travis offered Cheng Wei a 40% 'investment' that was effectively "
        "a cheap buyout — rejected.\n\n"
        "Saudi PIF fed Uber $3.5B; Didi raised $7B. By summer 2016 Didi claimed 85% share in 400 cities "
        "versus Uber's 100. Investors forced peace; Didi later invested $100M in Brazil's 99. Recording "
        "Feb 2017 — story ongoing."
    ),
    important_facts=[
        "Uber–Didi truce ~2016: Uber sells China ops for 17% of Didi; Didi invests $1B in Uber; Uber spent ~$2B in China.",
        "Subsidy war: Uber raised $3.5B from Saudi PIF; Didi raised $7B; both paid drivers more than riders paid fares.",
        "Didi–Kuaidi merger ~60/40 to Didi; ~700 days from founding to combination; Tencent/Alibaba anchored cap table.",
        "Uber hit ~30% share at launch with Baidu; Didi reclaimed dominance to ~85% by summer 2016 across ~400 cities.",
        "Didi invested in Lyft, Ola, Grab as global alliance; Feb 2017 announced $100M in Brazil's 99 — war continues abroad.",
    ],
    mental_model={
        "name": "Scorched Earth vs Durable Moats",
        "components": (
            "Rideshare in China proved capital and subsidies are not moats — drivers multi-home, promotions "
            "copy instantly, BAT portals tilt distribution. Network effects are local pockets, not global "
            "like Airbnb travel. Uber's retreat preserved capital into Didi equity in the world's largest "
            "market; Didi gave up 17% to end burn. Founder DNA (Travis win-at-all-costs vs Cheng Wei) shaped "
            "product aggression but not defensibility."
        ),
        "application": (
            "Marketplace founders: ask if N+1 city is easier than city N — if not, subsidies only buy time. "
            "Corporate venture (Tencent/Alibaba) alters competitive dynamics versus US. Investors: illiquid "
            "strategic stakes can beat operating losses but don't fix core moat. Brad's lens — culture and "
            "customer delight vs scorched earth — predicts later Uber crises."
        ),
    },
    competitive_advantage=(
        "Didi's China advantage blended local execution, regulatory familiarity, and BAT war chests — not "
        "technology alone.\n\n"
        "Uber brought global brand and product polish but faced copying within days (TechCrunch-driven "
        "clones). Driver multi-homing neutralized density claims. Cheng Wei's alliance with Lyft/Ola/Grab "
        "attacked Uber's fundraising narrative globally.\n\n"
        "Post-deal Uber holds 17% of the prize market; Didi kept control but diluted. Neither built Airbnb-like "
        "cross-border network effects.\n\n"
        "Weaknesses: both relied on subsidies; Uber culture alienated drivers/riders/regulators; Didi gave "
        "20% to end fight. Self-driving and municipal caps (Brad notes Chinese cities limiting car growth) "
        "shift battlefield again."
    ),
    key_insights=[
        {
            "view": "China pace dwarfs US rideshare fights.",
            "question": "How fast vs Uber's path to $1B valuation?",
            "answer": "Uber ~4 years seed (2009) to ~$1B; Chinese counterparts ~2 years. Thirty companies in a "
            "subsidy bloodbath made US Uber–Lyft look like 'kids in a sandbox.'",
        },
        {
            "view": "Travis's 40% offer was a takeout.",
            "question": "What happened in the first Cheng–Travis meeting?",
            "answer": "Travis framed 40% investment as cheap control; Cheng rejected. Nuclear phase followed — "
            "taste-testers and lockdown culture on both sides per Brad.",
        },
        {
            "view": "Capital raising was not a moat.",
            "question": "Did billions in funding help either side durably?",
            "answer": "Brad and hosts echo The Upstarts: subsidies bought share, not loyalty. Drivers chased "
            "bonuses across apps; Didi's 85% came from execution, capital, and subtle regulatory tilt — not "
            "locked-in network effects.",
        },
        {
            "view": "Uber's China exit was PE-positive.",
            "question": "Was $2B burn worth 17% of Didi?",
            "answer": "Ben frames as 2–3× cash-on-cash in illiquid stock if Didi grows — good for conglomerate "
            "logic, weak for Uber product strategy. B+ grades: right truce, should never have escalated.",
        },
        {
            "view": "Founder DNA is destiny.",
            "question": "How do Travis and Cheng Wei compare?",
            "answer": "Both failed before; both relentless. Travis outwardly combative, Cheng opaque. Uber lacked "
            "early values (contrast Airbnb); culture of winning at all costs foreshadowed 2017 engineering "
            "scandals discussed on episode.",
        },
    ],
    top_investment_implications=[
        {
            "ticker": "UBER",
            "direction": "Watch",
            "confidence": "Low",
            "thesis": "China exit preserved capital but moat still unclear — monitor Didi stake value, self-driving "
            "bets, and whether culture reform enables sustainable unit economics.",
        }
    ],
    golden_quotes=[
        "\"If you can't beat 'em, join 'em\" — David on Uber's China motto, crediting Brad's reporting.",
        "\"Kids in the sandbox\" — hosts on US Uber–Lyft vs China's 30-company subsidy war.",
        "\"You get the investors you ask for\" — echo from Amazon episode; Uber attracted growth-at-all-costs capital.",
    ],
    chronology={
        "subject": "Uber vs Didi in China",
        "events": [
            {"date": "2013", "event": "Uber begins clandestine China tests; Travis texts SF team from China"},
            {"date": "2014", "event": "Chinese rideshare copycats explode; BAT invest in rivals"},
            {"date": "2015", "event": "Didi–Kuaidi merge; Cheng Wei CEO of combined entity"},
            {"date": "2015", "event": "Uber launches in China with Baidu; reaches ~30% share"},
            {"date": "2015", "event": "Travis offers 40% 'investment'; Didi rejects"},
            {"date": "2016", "event": "Saudi PIF $3.5B to Uber; Didi raises $7B; subsidy war peaks"},
            {"date": "Summer 2016", "event": "Didi claims ~85% share in ~400 cities"},
            {"date": "Fall 2016", "event": "Uber sells China business for 17% of Didi"},
            {"date": "Feb 2017", "event": "Episode records; Didi invests $100M in Brazil's 99"},
            {"date": "2017", "event": "Brad Stone publishes The Upstarts documenting Uber and Airbnb"},
        ],
    },
)

EPISODES["acq-episode-32-the-snap-inc-ipo"] = base(
    "acq-episode-32-the-snap-inc-ipo",
    review_notes=REVIEW,
    episode_rating={"overall": 4},
    keywords=["Camera Company Narrative", "Zero-Vote IPO", "Brand Advertising"],
    conclusion=(
        "Recorded March 3, 2017 — one day after Snap priced at $17 (above $15–16 range), popped 44% to "
        "$24.48, and hit ~$34B market cap on day two. Revenue grew ~10× in two years to ~$400M but user "
        "growth stalled after Instagram Stories (Aug 2016): Snap added 15M DAU in seven months while "
        "Instagram added 100M. S-1 positioned Snap as a camera company pursuing TV brand budgets, not "
        "Facebook performance ads — with zero-vote public shares (unprecedented) and a $625M Evan Spiegel "
        "IPO bonus. Gross margins were negative on ~$3B Google/AWS hosting through 2016. Hosts grade IPO "
        "execution A; strategic outcome TBD — 'Do you trust me?' public offering."
    ),
    background=(
        "Episode 32 is Acquired's real-time Snap IPO reaction (refer listeners to Episode 12 for founding "
        "and rejected $3B Facebook offer). Fall 2014: 50M DAU, Stories launched, Reggie Brown lawsuit settled. "
        "By IPO: Discover, Lenses, Spectacles, Bitmoji, ad API (Oct 2016). S-1 'kindness' passage and "
        "roadshow video broke mold — marketing document to non-user investors.\n\n"
        "Three-class structure: public gets 0 votes, VCs get 1, Evan/Bobby get 10 with proxy on death. "
        "Infrastructure: $2B Google Cloud + $1B AWS over five years; Lenses and video storage drove cost. "
        "Narratives section debuts: company story (camera, brand ads, product genius) vs press (growth stall, "
        "infra burn, Instagram competition)."
    ),
    important_facts=[
        "IPO priced March 1, 2017 at $17/share (~$24B cap); opened ~$24; day-one close $24.48 (+44%); ~$34B cap day two.",
        "~158M daily active users at filing; ~18 app opens/day; ~25–30 minutes/day engagement per S-1.",
        "Revenue ~$400M run-rate after first monetization dollar in late 2014; ~80× sales multiple vs Facebook IPO ~28×.",
        "First public company IPO with zero-vote shares; Evan received ~3% extra equity (~$625M) 'CEO Award' for completing IPO.",
        "Gross margin negative until recently — ~$452M cost of revenue in 2016; ~$3B committed cloud spend (Google + AWS).",
    ],
    mental_model={
        "name": "Narrative IPO as Seed Deck at Scale",
        "components": (
            "Snap sold belief in Evan/Bobby's product invention — camera company, AR Lenses, Spectacles — "
            "not current social-graph metrics. Zero-vote structure and CEO bonus signaled 'trust us' like "
            "late-stage private round. Brand advertising thesis attacks TV budgets ($5–10yr lag vs digital "
            "engagement). Counter-risk: Instagram copies Stories; communication-heavy graph limits viral "
            "coefficient vs broadcast social media."
        ),
        "application": (
            "IPO teams can use S-1/roadshow as positioning weapon — comp against Apple not Twitter. "
            "Investors must separate execution grade (pop, capital raised) from moat grade (Facebook's "
            "existing graph + gun-to-knife-fight). Founders: infra outsourcing buys speed but linear COGS "
            "scales with users — Snap paid premium for nimbleness.",
        ),
    },
    competitive_advantage=(
        "Snap's moat thesis is product invention + youth graph + camera-native AR — not scale versus Facebook.\n\n"
        "Lenses used by ~⅓ of DAU daily; technology lead over Instagram (then). Ephemeral messaging creates "
        "intimacy but weak international viral loops (Snow in Asia). Brand ad format privacy-first vs "
        "Facebook targeting — appeals to CPG TV budgets shifting digital in 2017.\n\n"
        "Spectacles and full-stack camera narrative support AR optionality. Evan's secrecy and internal "
        "competing teams mirror Apple product culture.\n\n"
        "Weaknesses: Facebook copies features at scale; gross-margin-negative infra; domestic saturation; "
        "zero-vote IPO alienates activists but not if growth stalls. Communication graph ≠ media graph for "
        "advertiser reach."
    ),
    key_insights=[
        {
            "view": "Camera company framing avoids Facebook comp.",
            "question": "Why 'camera company' not social network?",
            "answer": "Reframes investor multiples away from Twitter disaster toward Apple/innovation. Lenses, "
            "Spectacles, and AR infra spend support story; S-1 user manual teaches product before financials.",
        },
        {
            "view": "Instagram Stories froze growth.",
            "question": "What happened Q2 2016 onward?",
            "answer": "DAU curve flattened after Instagram Stories — Instagram +100M DAU in 7 months while Snap "
            "+15M. Kevin Systrom openly borrowed format; Facebook brings entire existing graph.",
        },
        {
            "view": "IPO execution was brilliant.",
            "question": "Did Snap leave money on the table?",
            "answer": "~$1B left via pop — but momentum helps hiring and brand. Priced above range and last private "
            "round; avoided Facebook 2012 technical disaster. Hosts give execution A despite strategic uncertainty.",
        },
        {
            "view": "Gross-margin-negative IPO is rare.",
            "question": "Why such heavy cloud spend?",
            "answer": "Lenses + video storage + outsourced infra = linear COGS. Bull case: speed to experiment; "
            "bear case: should own data centers by 2017. ~$3B Google/AWS commitments vs ~$400M revenue.",
        },
        {
            "view": "Zero-vote shares change accountability.",
            "question": "Who did Snap attract?",
            "answer": "Public buyers get no activist recourse — Evan/Bobby keep control like private company with "
            "public currency. Tom Alberg echo: you get investors you ask for; Snap asked for believers not governors.",
        },
    ],
    top_investment_implications=[
        {
            "ticker": "SNAP",
            "direction": "Watch",
            "confidence": "Low",
            "thesis": "Post-IPO story hinges on AR/camera differentiation vs Meta copying — high variance; "
            "not a traditional fundamentals long at 80× sales in 2017 framing.",
        }
    ],
    golden_quotes=[
        "\"We are a camera company\" — Snap S-1 positioning away from social-network comps.",
        "\"Do you trust me?\" — Ben summarizing the IPO as Evan facing public markets.",
        "\"Selling dollars for 50 cents\" — hosts on gross-margin-negative operations pre-IPO.",
    ],
    chronology={
        "subject": "Snap · path to March 2017 IPO",
        "events": [
            {"date": "2011", "event": "Snapchat founded; ephemeral messaging"},
            {"date": "Late 2013", "event": "Facebook offers ~$3B; Spiegel declines"},
            {"date": "Fall 2014", "event": "50M DAU; Stories; Reggie Brown suit settled"},
            {"date": "Late 2014", "event": "First revenue dollar"},
            {"date": "Oct 2016", "event": "Ad API launch; Instagram Stories ships"},
            {"date": "Feb 2, 2017", "event": "S-1 filed publicly"},
            {"date": "Mar 1, 2017", "event": "IPO priced $17; ~$24B market cap"},
            {"date": "Mar 2, 2017", "event": "First trading day +44%; ~200M shares traded"},
            {"date": "Mar 3, 2017", "event": "Episode recorded; stock ~$29 range"},
            {"date": "2016", "event": "Spectacles launch — Snap positions as hardware/camera company"},
        ],
    },
)

EPISODES["acq-episode-33-overture-with-the-internet-history-podcast"] = base(
    "acq-episode-33-overture-with-the-internet-history-podcast",
    review_notes=REVIEW,
    episode_rating={"overall": 4},
    keywords=["Paid Search Origin", "B2B vs B2C", "Engineering Culture"],
    conclusion=(
        "Brian McCullough (Internet History Podcast) joins a crossover episode on Yahoo's July 2003 "
        "acquisition of Overture (formerly GoTo.com) for ~$1.4B — 15% premium, >10% of Yahoo's ~$11B "
        "market cap. Bill Gross invented pay-per-click search advertising but Overture remained a B2B "
        "syndicator while Google built a superior B2C engine with PageRank, click-quality optimization, "
        "and second-price auctions. Yahoo paused Overture customers for Project Panama, ceding ground; "
        "patents yielded little versus engineering deficit. Hosts grade Yahoo D; ecosystem A+++ — Hadoop, "
        "Jeff Weiner, Stewart Butterfield (Slack), and countless alumni from failed Panama effort."
    ),
    background=(
        "Episode 33 double-runs on Internet History Podcast. Post-bubble 2003: GoTo/Overture pioneered "
        "paid placement when organic search barely existed — every result was an ad. Gross's insight: marry "
        "PPC model to portal traffic. Google later copied model but invested in relevance, GSE appliance "
        "hardware partnerships, then AdWords quality score.\n\n"
        "Yahoo bought Overture believing search ads were a media-company adjacency; Paul Graham's 'What "
        "Happened to Yahoo?' frames media vs engineering culture clash. Integration froze Overture "
        "marketplace during Panama rebuild — Google swooped. Brian's Gary Flake episode noted horizontal "
        "providers lack power without first-party traffic."
    ),
    important_facts=[
        "Yahoo acquired Overture for ~$1.4B (2003) — ~15% premium; ~10%+ of Yahoo's ~$11B market cap.",
        "GoTo.com (1998) showed only paid results — invented PPC; Overture syndicated to Yahoo, MSN, others.",
        "Google improved with PageRank, click-through optimization, second-price auction — revenue per search leap.",
        "Yahoo Project Panama multi-year rebuild paused Overture ecosystem — customers fled to Google.",
        "Hadoop emerged from Yahoo's Google-compete engineering; alumni include Jeff Weiner, Stewart Butterfield (Slack).",
    ],
    mental_model={
        "name": "Product Model vs Business Model Ownership",
        "components": (
            "Overture nailed paid search product model as B2B pipes; Google owned B2C destination + "
            "algorithmic relevance — capturing majority of value chain. Vertical Yahoo buying horizontal "
            "Overture destroyed partner neutrality without shipping superior tech. Engineering-centric "
            "cultures win search; media-banner mindset mispriced performance ads. Ecosystem value (Hadoop, "
            "talent spinouts) can exceed acquirer salvage."
        ),
        "application": (
            "When syndicating innovation, assume customers become competitors — diversify or build "
            "first-party destination. Acquirers must choose: run acquired biz or integrate — Yahoo tried "
            "both, succeeded at neither. Startups: B2B pioneering may train acquirer who eats your lunch.",
        ),
    },
    competitive_advantage=(
        "Google's moat combined PageRank relevance with auction mechanics aligning advertiser, user, and "
        "Google incentives — everyone feels they get a deal.\n\n"
        "Overture lacked traffic and eventually technology lead; Yahoo's media identity deprioritized search "
        "engineering. Patents on bid-for-placement proved less valuable than continuous ML iteration.\n\n"
        "Microsoft Windows OEM analogy: horizontal software can discipline hardware partners without own device — "
        "Overture had no such leverage once Google owned users.\n\n"
        "Weaknesses for Yahoo: should have sold to Google early per PG; Panama rebuild; missed Facebook. "
        "Display ads (DoubleClick path) fit Yahoo better than search — counterfactual rarely explored."
    ),
    key_insights=[
        {
            "view": "Overture invented the cash machine.",
            "question": "Who created search ads?",
            "answer": "Bill Gross's GoTo/Overture proved PPC pre-Google dominance. Market was non-obvious — "
            "keyword auctions were not inevitable. Google copied model, won on engineering and destination.",
        },
        {
            "view": "Yahoo chose media over math.",
            "question": "Why did Panama fail?",
            "answer": "PG thesis: Yahoo became 'grown-up' media company selling banner impressions; search was "
            "traffic funnel not core competency. Engineering talent could not match Google research output "
            "(papers → open source lag ~3 years).",
        },
        {
            "view": "Integration freeze killed marketplace.",
            "question": "What broke Overture post-deal?",
            "answer": "Pausing Overture engineers for Panama starved three-sided marketplace (advertisers, "
            "publishers, searchers). Google captured advertisers with better ROI; cold-start problem returned.",
        },
        {
            "view": "B2B caps upside in single-industry syndication.",
            "question": "Could Overture have won standalone?",
            "answer": "Ben argues B2B search syndication naturally smaller than largest B2C engine — unless "
            "multi-industry platform. Missing B2C after GoTo failure locked ceiling.",
        },
        {
            "view": "Failure spawned Silicon Valley infrastructure.",
            "question": "Any upside for Yahoo?",
            "answer": "David grades ecosystem A+++: Hadoop, Hortonworks/Cloudera lineage, executive alumni. "
            "Yahoo shareholder value later mediocre, but innovation externality huge.",
        },
    ],
    top_investment_implications=[
        {
            "ticker": "GOOGL",
            "direction": "Watch",
            "confidence": "Medium",
            "thesis": "Search cash cow born in Overture-era competition — monitor regulatory risk to auction "
            "model; lesson validates owning end-user relationship.",
        }
    ],
    golden_quotes=[
        "\"Everybody getting a good deal\" — Ben on sustainable platforms (Google, Amazon) vs zero-sum Uber.",
        "\"Turn lead into gold\" — Brian on PPC invention feeling like alchemy.",
        "\"What happened to Yahoo?\" — Paul Graham essay referenced throughout; media vs tech identity.",
    ],
    chronology={
        "subject": "Overture & Yahoo search",
        "events": [
            {"date": "1998", "event": "GoTo.com launches — paid-results-only search"},
            {"date": "2000–01", "event": "Dot-com crash; portals wounded"},
            {"date": "2002", "event": "Overture syndicates PPC across major portals"},
            {"date": "2003", "event": "Yahoo acquires Overture for ~$1.4B"},
            {"date": "2004–06", "event": "Google AdWords quality gains; Yahoo starts Project Panama"},
            {"date": "2006–08", "event": "Panama delayed; Google cements search ad dominance"},
            {"date": "2006", "event": "Hadoop born inside Yahoo"},
            {"date": "2010s", "event": "Yahoo talent seeds Slack, LinkedIn leadership, Cloudera/Hortonworks"},
            {"date": "2017", "event": "Verizon acquisition era — search long irrelevant to Yahoo"},
            {"date": "2000", "event": "Google AdWords launches with relevance and auction innovations"},
        ],
    },
)

EPISODES["acq-episode-34-starbucks-ipo-with-dan-levitan"] = base(
    "acq-episode-34-starbucks-ipo-with-dan-levitan",
    review_notes=REVIEW,
    episode_rating={"overall": 4},
    keywords=["Retail IPO", "Partner Culture", "Customer Loyalty"],
    conclusion=(
        "Dan Levitan — Maveron cofounder with Howard Schultz — joins for Starbucks' June 1992 IPO at $17/share "
        "and ~$225M market cap on ~$93M revenue year, raising $25M. Howard bought six Seattle stores for "
        "$3.8M in 1987 after Il Giornale raised ~$1.6M; revenue jumped from $1.2M (1987) to $10.2M (1988) "
        "post-merger, doubling through early '90s. Goldman won a beauty contest (59/60 investors said yes); "
        "pricing debate: $16 vs $17. Today ~$83B market cap (~18,000% since IPO). Hosts grade A — IPO enabled "
        "national expansion, brand visibility, and disciplined store growth with partner equity culture."
    ),
    background=(
        "Episode 34 lands on the 25th anniversary of Starbucks going public (near Howard's retirement). "
        "Origins: 1971 Pike Place roasters; Howard's 1983 Milan trip inspired café model; Il Giornale "
        "merged 1987. Pre-IPO equity ~$30M+ raised — large for era, modest vs today's unicorns. Part-time "
        "health benefits and Bean Stock for all partners including baristas.\n\n"
        "Dan met Howard 1991 in New York; roasting-plant tour was diligence theater. S1 emphasized lifetime "
        "customer loyalty in a category that did not exist (coffee to-go). Post-IPO: mobile app, gift-card "
        "float, technology as loyalty lever — but IPO capital funded geographic land grab before copycats."
    ),
    important_facts=[
        "IPO June 1992: priced $17/share, ~$225M market cap; raised $25M on ~$93M revenue year.",
        "Howard acquired Starbucks retail for $3.8M (1987); Il Giornale had raised ~$1.6M; revenue $1.2M → $10.2M in year one post-merger.",
        "Goldman won IPO beauty contest; 59 of 60 investors accepted allocation; pricing fight at $16 vs $17.",
        "Pre-IPO equity raised exceeded $30M; part-time partner health benefits from 1988 onward.",
        "Market cap ~$83B at episode recording — ~18,000% appreciation from IPO; first pure-play public coffee company.",
    ],
    mental_model={
        "name": "Growth + Delight Dual Engine",
        "components": (
            "Starbucks paired aggressive store expansion with exceeding customer expectations every visit — "
            "Howard/Bezos/Jobs 'moat' of founder-led obsession. High-frequency, low-ticket habit (~60 meetings "
            "in 100 days per S1 anecdote) funds clustering strategy. IPO visibility unlocked national rollout "
            "faster than private capital; pricing at $17 signaled confidence. Third-wave coffee later "
            "disaggregated artisanal, but second-wave Starbucks rode experience retail."
        ),
        "application": (
            "Retail IPOs: grade on capital use for expansion + brand event, not day-one pop only. "
            "Investment bankers earn trust via domain curiosity (roasting plant tour). Founders: loyalty "
            "metrics in S1 must reflect repeat behavior, not novelty. Dan/Maveron lens — consumer VC needs "
            "founder who scales humanity, not just units.",
        ),
    },
    competitive_advantage=(
        "Starbucks' moat in 1992 was habit + 'third place' experience before scale became self-reinforcing.\n\n"
        "Customization, partner culture, and clustering raised switching costs versus diner coffee. No "
        "national competitor matched capital + playbook at IPO moment — copycats emerged after public "
        "visibility. Howard's founder premium on investor roadshow (59/60 yes) reflected scarcity of "
        "repeat-purchase retail with 80%-ish gross margin potential.\n\n"
        "Technology later amplified via app prepaid float (~$1.8B discussed in later Howard episode) but 1992 "
        "edge was physical ritual.\n\n"
        "Weaknesses: succession risk; ubiquity erodes magic; IPO priced growth that required flawless "
        "same-store execution for 100 consecutive months post-offering per hosts' grading note."
    ),
    key_insights=[
        {
            "view": "IPO was national expansion fuel.",
            "question": "Why go public vs private in 1992?",
            "answer": "No late-stage hedge funds; $25M funded store frenzy into new markets with brand pedigree "
            "from IPO buzz. Dan: DNA was growth — slower path would cede ground to emerging copycats.",
        },
        {
            "view": "Loyalty was the S1 thesis.",
            "question": "What moat did Dan cite?",
            "answer": "Lifetime repeat visits in a category that did not exist pre-Starbucks. Howard/company "
            "understood customer ritual better than JC Penney-era retail peers on same exchanges.",
        },
        {
            "view": "Goldman earned the mandate.",
            "question": "What was the beauty contest?",
            "answer": "6–8 page checklist; roasting facility tour tested genuine interest. Small deal for Goldman "
            "but Howard picked partners with chemistry and sector respect — not just fee table.",
        },
        {
            "view": "$17 pricing mattered symbolically.",
            "question": "Why fight over $1 on IPO price?",
            "answer": "Damaged goods stigma if deal stumbles; $17 signaled quality. Pop modest vs Snap — but "
            "years of steady appreciation without 'oh crap' moment post-IPO.",
        },
        {
            "view": "Coffee waves mirror tech waves.",
            "question": "David's Folgers → Starbucks → third-wave analogy?",
            "answer": "First wave bad one-size (Folgers/AOL); second wave good one-size with friends (Starbucks/"
            "Facebook); third wave personalized artisanal (local roasters / Instagram Stories disaggregation).",
        },
    ],
    top_investment_implications=[
        {
            "ticker": "SBUX",
            "direction": "Watch",
            "confidence": "Medium",
            "thesis": "IPO template for experience retail — monitor same-store traffic and whether mobile "
            "loyalty sustains post-Howard eras; 1992 lesson is expansion + delight, not just units.",
        }
    ],
    golden_quotes=[
        "\"59 out of 60 said yes\" — Dan on IPO allocation demand.",
        "\"Selling drugs to your customers\" — David jokes on caffeine repeat-purchase model.",
        "\"Growth and exceeding customer expectations\" — dual drives David cites for magical consumer companies.",
    ],
    chronology={
        "subject": "Starbucks · IPO era",
        "events": [
            {"date": "1971", "event": "Pike Place roastery founded — beans only"},
            {"date": "1982", "event": "Howard Schultz joins"},
            {"date": "1983", "event": "Milan trip inspires espresso bar vision"},
            {"date": "1987", "event": "Il Giornale buys Starbucks for $3.8M"},
            {"date": "1988", "event": "Part-time health benefits; Bean Stock begins"},
            {"date": "1991", "event": "Dan Levitan meets Howard; IPO planning starts"},
            {"date": "Jun 1992", "event": "IPO at $17; ~$225M market cap; raises $25M"},
            {"date": "1990s", "event": "National expansion; tens of months same-store growth"},
            {"date": "2017", "event": "Episode on 25th IPO anniversary; Howard retirement month"},
            {"date": "Recording", "event": "~$83B market cap cited"},
        ],
    },
)

EPISODES["acq-episode-35-oculus"] = base(
    "acq-episode-35-oculus",
    review_notes=REVIEW,
    episode_rating={"overall": 3},
    keywords=["VR Platform Bet", "Facebook FOMO", "Vertical vs Horizontal"],
    conclusion=(
        "Facebook acquired Oculus in March 2014 for $2.3B ($400M cash, $1.6B stock, $300M earnout) — "
        "weeks after Andreessen Horowitz's $75M Series B at ~$300–400M valuation (~8–10× in 3 months). "
        "Palmer Luckey's 2012 Kickstarter raised $2.5M on a $250K goal; John Carmack demo at E3 catalyzed "
        "momentum. Post-deal: ZeniMax won $500M IP judgment (2017); Valve/HTC Vive shipped superior hand "
        "tracking and room-scale VR in 2016. Hosts grade C so far — right to buy preeminent VR asset, weak "
        "execution vs Valve; integrating Oculus into Menlo Park risks horizontal Facebook prioritizing vertical "
        "hardware (iMessage trap). Zuckerberg bet on social VR; Snap pursues camera AR instead."
    ),
    background=(
        "Episode 35 covers Palmer Luckey's garage prototypes, USC ICT lab background, Carmack leaving id "
        "for Oculus CTO, and Brendan Iribe's Scaleform/Gaikai team. Mark Zuckerberg flew to Irvine after "
        "Snap/Snapchat pattern of demanding demos on startup turf. Acquisition cemented Facebook's aggressive "
        "M&A after Instagram/WhatsApp — buying next computing wave early.\n\n"
        "Palmer later left Facebook; Brendan stepped down as CEO to run PC VR. Team relocated to Menlo Park — "
        "tighter integration than Instagram. Ben argues technology acquisition defending ad network access; "
        "David says business line. Both agree Valve out-executed on product; Android/Google cited as horizontal "
        "OS analogy."
    ),
    important_facts=[
        "Facebook acquired Oculus March 2014 for $2.3B total ($400M cash, $1.6B stock, $300M earnout).",
        "Kickstarter Aug 2012: $2.5M raised vs $250K goal; DK1 sold 4–5 units/minute at $300 on website post-campaign.",
        "Series A $16M (Jun 2013); Series B $75M led by a16z Dec 2013 — Marc Andreessen on boards of both Facebook and Oculus.",
        "ZeniMax lawsuit: $500M judgment Feb 2017 over Carmack/id IP; potential Rift sales injunction discussed.",
        "Valve/HTC Vive launched April 2016 with hand controllers and room-scale lighthouses — hosts say out-executed Rift.",
    ],
    mental_model={
        "name": "Horizontal Platform Insurance Policy",
        "components": (
            "Facebook buys Oculus so no future platform can block its social graph — analogous to Google "
            "Android preventing Apple from taxing search. Risk: vertical hardware tempts prioritizing Oculus-only "
            "features (Office-on-iPad mistake). Palmer claimed 5–10 years acceleration with Facebook resources. "
            "VR killer app may be social (Rec Room, Zuckerberg thesis) but wave unbroken — AR/camera may win first "
            "(Snap Spectacles, Apple rumors)."
        ),
        "application": (
            "Mega-horizontals should insure distribution, not assume hardware monopoly. Integrate acquisitions "
            "that protect core business while keeping best talent (Valve poached by independence). VR still "
            "<1M DAU 2017 vs billions mobile — grades carry high variance. Founders: Kickstarter + community "
            "(Meant to be Seen forums) can attract Carmack-level validators.",
        ),
    },
    competitive_advantage=(
        "Oculus under Facebook offered capital, brand for developers, and consumer Rift — but not durable "
        "hardware leadership.\n\n"
        "Carmack talent and DK2 quality impressed; consumer Rift March 2016 beat Vive by a week but lacked "
        "controllers until Dec 2016. Facebook's social VR demos compete with Valve's Steam distribution moat "
        "and HTC manufacturing.\n\n"
        "IP judgment and Palmer's political controversies (Nimble America) complicated brand. Integration "
        "moved team to Menlo — talent retention risk vs Valve's flat culture.\n\n"
        "Weaknesses: requires $1,000+ PC towers; mobile VR separate bet; horizontal Facebook may starve Oculus "
        "priority conflicts. Snap and Apple pursue camera/AR paths with clearer user bases."
    ),
    key_insights=[
        {
            "view": "Acquisition was FOMO on next platform.",
            "question": "Why $2.3B pre-revenue?",
            "answer": "Post-mobile scare (2012 pivot) — Facebook bought waves early (Instagram late, WhatsApp "
            "threat). VR years from consumer scale but cheaper than missing platform shift.",
        },
        {
            "view": "Valve execution beat Facebook capital.",
            "question": "Who won product 2015–2017?",
            "answer": "Vive's hand tracking + room scale set bar; Oculus needed Facebook money to stay in game. "
            "Gabe Newell backed Oculus in Kickstarter video then partnered with HTC — brilliant end-around.",
        },
        {
            "view": "Technology not business line for Ben.",
            "question": "Acquisition category?",
            "answer": "Defensive tech to ensure Facebook on all VR platforms — not revenue from Rift sales. "
            "Integrating deeper risks iMessage-style vertical bias.",
        },
        {
            "view": "ZeniMax IP is costly footnote.",
            "question": "Legal outcome?",
            "answer": "$500M damages pushes effective price toward $2.8B; Carmack NDA/id code allegations. "
            "Board includes Cal Ripken, Leslie Moonves, Robert Trump per hosts' research digression.",
        },
        {
            "view": "Social may be VR killer app.",
            "question": "Is Zuckerberg right on social VR?",
            "answer": "Rec Room and GoldenEye nostalgia support social games; Snap's camera AR reaches billions "
            "sooner. David: right thesis, poor execution to date — grade C with variance.",
        },
    ],
    top_investment_implications=[
        {
            "ticker": "META",
            "direction": "Watch",
            "confidence": "Low",
            "thesis": "Reality Labs spend is long-dated option on spatial computing — success requires horizontal "
            "discipline and product parity with Apple/Valve; not near-term earnings driver in 2017 framing.",
        }
    ],
    golden_quotes=[
        "\"Developers, developers, developers\" — Ballmer echo; Palmer duct-taped DK1 at E3.",
        "\"5 years ahead of where we would have been\" — Palmer on Facebook resources post-acquisition.",
        "\"Can Facebook be horizontal and vertical at once?\" — hosts cite Office/iPad and iMessage traps.",
    ],
    chronology={
        "subject": "Oculus · founding to Facebook acquisition",
        "events": [
            {"date": "2010", "event": "Palmer Luckey prototypes HMDs; works at USC ICT"},
            {"date": "Jun 2012", "event": "Carmack demos Doom 3 on Rift at E3"},
            {"date": "Aug 2012", "event": "Kickstarter raises $2.5M; company formed with Brendan Iribe"},
            {"date": "Jun 2013", "event": "$16M Series A; Carmack joins as CTO"},
            {"date": "Dec 2013", "event": "$75M Series B led by Andreessen Horowitz"},
            {"date": "Mar 2014", "event": "Zuckerberg demos in Irvine; Facebook buys for $2.3B"},
            {"date": "Mar 2016", "event": "Consumer Rift ships"},
            {"date": "Apr 2016", "event": "HTC Vive ships with controllers + room scale"},
            {"date": "Feb 2017", "event": "ZeniMax $500M judgment"},
            {"date": "Mar 2017", "event": "Episode records; Palmer departure noted in update"},
        ],
    },
)

EPISODES["acq-episode-36-the-la-clippers"] = base(
    "acq-episode-36-the-la-clippers",
    review_notes=REVIEW,
    episode_rating={"overall": 3},
    keywords=["Sports Franchise Scarcity", "NBA Media Rights", "Owner Economics"],
    conclusion=(
        "Steve Ballmer bought the LA Clippers for $2B in 2014 after Donald Sterling's lifetime ban — "
        "3.5× the prior NBA record (Milwaukee Bucks $550M) and 3.5× Forbes' $575M valuation. Franchise "
        "history: Buffalo Braves (1970) → San Diego → LA (1984, via lawsuit); worst winning % in major "
        "American sports under Sterling. Post-sale: six straight playoff years, five with 50+ wins, but "
        "no Western Conference finals; Forbes 2017 still $2B while Knicks rose to $3.3B. Hosts grade B+ "
        "(David) — scarce LA 'real estate,' NBA youth demographics, and TV rights growth justify price "
        "even if S&P returned ~21% vs flat team valuation."
    ),
    background=(
        "Episode 36 applies Acquired lens to sports: Ballmer's third NBA attempt after failed Seattle "
        "Sonics/Kings bids. Sterling bought team for $12.5M (1981); TMZ tape (Apr 25, 2014) forced Adam "
        "Silver's lifetime ban and ¾-owner vote to sell. Oprah, Mayweather, Magic, and Ballmer bid; Shelly "
        "Sterling ran sale with odd perks (10 tickets, 3 championship rings clause).\n\n"
        "Analysis covers NBA as business line: ~10× revenue and ~15× operating income multiples vs 3–5× "
        "SaaS; leagues capture ESPN + direct League Pass upside as only must-watch live TV. Tech themes: "
        "Moneyball-style on-court innovation (Warriors), Ballmer vs Zuck acquisition styles, Doc Rivers "
        "dual coach/GM structure."
    ),
    important_facts=[
        "Ballmer paid $2B (2014) — 3.5× prior NBA record $550M (Milwaukee Bucks); Forbes valued Clippers at $575M.",
        "Sterling bought Clippers for $12.5M (1981); franchise worst winning % in major US sports over his tenure.",
        "Post-Ballmer: 6 straight playoff appearances; 5 seasons with 50+ wins; still no Western Conference finals.",
        "Forbes 2017: Clippers still $2B (#6); Knicks #1 at $3.3B (up from $1.4B in 2014).",
        "NBA audience ~half under 35 per Nielsen — youngest major US sport; franchises trade ~10× revenue, ~15× operating income.",
    ],
    mental_model={
        "name": "Scarce Real Estate + Media Rights Option",
        "components": (
            "NBA teams are limited-supply assets in mega-markets — like airport gates (Alaska/Virgin episode). "
            "Distressed Sterling sale still drew premium because LA + youth demographics + escalating TV/digital "
            "rights compound cash flows. Player contracts depreciate for tax but brand and market position "
            "appreciate. Active owners (Ballmer) spend above NPV for trophy utility; passive owners free-ride "
            "league growth."
        ),
        "application": (
            "Treat sports franchises as media businesses with monopoly league structures — not operating "
            "companies. Ballmer overbid rationally if franchise values track Knicks comp (+175% in 3 years). "
            "Tech founders buying teams: customer relationship play (Ballmer) differs from ROI maximization. "
            "Investors: compare to bonds/index only if liquidity matters; trophy assets trade on scarcity.",
        ),
    },
    competitive_advantage=(
        "Clippers' competitive position improved from league punchline to playoff regular — but Lakers still "
        "own Staples schedule priority and LA mindshare.\n\n"
        "Ballmer capital retained Chris Paul, DeAndre Jordan; upgraded engagement vs Sterling heckling players. "
        "NBA league-wide advantages: youngest TV audience, live-sports bundling power vs cord-cutting, BAMTech "
        "direct subscriptions duplicating ESPN dollars.\n\n"
        "On-court: Lob City era talent without deep bench or finals appearances — Doc Rivers dual role may "
        "limit GM depth.\n\n"
        "Weaknesses: $2B entry with flat 2017 Forbes mark; West conference depth; dependent on league CBA and "
        "media renewals not team-specific moat. Ballmer involvement can disrupt operations per insider anecdote."
    ),
    key_insights=[
        {
            "view": "Fire sale still fetched premium.",
            "question": "Why $2B for distressed asset?",
            "answer": "Limited NBA supply + LA market + billionaire trophy demand. Oprah/Magic/Mayweather bidding "
            "proved elasticity; Ballmer 20% over next bid like Skype playbook.",
        },
        {
            "view": "League lifted all boats.",
            "question": "Did Ballmer overpay?",
            "answer": "Clippers flat at $2B 2017 but Knicks +135% — league media tailwind rewards any seat. "
            "S&P ~21% beat Clippers mark short-term but NBA multiples expanded.",
        },
        {
            "view": "NBA is innovating on court.",
            "question": "Why NBA vs NFL?",
            "answer": "Warriors three-point pace; analytics adoption beats MLB/NFL conservatism. Youngest "
            "audience supports ad/revenue growth thesis Ben cites (with esports caveat).",
        },
        {
            "view": "TV rights double-dip.",
            "question": "Why are rights worth more?",
            "answer": "Live sports last cord-cutting anchor; leagues also sell League Pass direct — ESPN juice "
            "plus DTC until model shifts. Ben Thompson symbiosis auto/beer/TV breaking.",
        },
        {
            "view": "Owner model matters.",
            "question": "Ballmer vs Sterling operational delta?",
            "answer": "Unlimited-check reputation vs Sterling's penny-pinching; Doc Rivers dual role may lack GM "
            "pipeline — listener warned on Blake/CP3 free agency. Grade B+ balances trophy utility vs roster depth.",
        },
    ],
    top_investment_implications=[
        {
            "ticker": "MSFT",
            "direction": "Watch",
            "confidence": "Low",
            "thesis": "Ballmer Clippers hold is personal asset — immaterial to MSFT; illustrates post-CEO capital "
            "allocation into scarce experiential assets, not financial return maximization.",
        }
    ],
    golden_quotes=[
        "\"I love this company!\" — Ballmer arena energy applied to Clippers.",
        "\"At least you're not as bad as the Clippers\" — franchise as cultural punchline pre-2014.",
        "\"Six parking spaces in perpetuity\" — Shelly Sterling deal terms ridiculed by hosts.",
    ],
    chronology={
        "subject": "LA Clippers · franchise timeline",
        "events": [
            {"date": "1970", "event": "Buffalo Braves founded as NBA expansion team"},
            {"date": "1978", "event": "Moves to San Diego Clippers; Celtics ownership swap"},
            {"date": "1981", "event": "Donald Sterling buys team for $12.5M"},
            {"date": "1984", "event": "Sterling moves team to LA despite NBA opposition"},
            {"date": "2013", "event": "First division title; CP3, Griffin, Jordan core"},
            {"date": "Apr 2014", "event": "Sterling TMZ tape; players protest"},
            {"date": "Apr 2014", "event": "Adam Silver lifetime ban; forced sale process"},
            {"date": "Aug 2014", "event": "Ballmer buys Clippers for $2B"},
            {"date": "2014–17", "event": "Six straight playoffs; five 50-win seasons"},
            {"date": "2017", "event": "Forbes values Clippers at $2B unchanged; episode airs"},
        ],
    },
)


def main() -> None:
    tmpl = load_template_config(template_path_for_podcast("Acquired"))
    results: list[tuple[str, bool, int, list[str]]] = []

    for ep_id, data in EPISODES.items():
        # Fix metadata for guest episodes
        guests = {
            "acq-episode-28-the-amazon-ipo-with-original-amazon-board-member-tom-alberg": ("Tom Alberg", "Amazon board member · Madrona cofounder"),
            "acq-episode-31-the-uber-didi-chuxing-merger-with-brad-stone-author-of-the-upstarts-the-everything-store": ("Brad Stone", "Bloomberg · author of The Upstarts"),
            "acq-episode-33-overture-with-the-internet-history-podcast": ("Brian McCullough", "Internet History Podcast"),
            "acq-episode-34-starbucks-ipo-with-dan-levitan": ("Dan Levitan", "Maveron cofounder · Starbucks IPO banker"),
        }
        if ep_id in guests:
            g, role = guests[ep_id]
            data["metadata"]["guest"] = g
            data["metadata"]["guest_role"] = role

        nums = {
            "acq-episode-28-the-amazon-ipo-with-original-amazon-board-member-tom-alberg": (28, "2016-12-01"),
            "acq-episode-30-pa-semi-authentec": (30, "2017-01-01"),
            "acq-episode-31-the-uber-didi-chuxing-merger-with-brad-stone-author-of-the-upstarts-the-everything-store": (31, "2017-02-01"),
            "acq-episode-32-the-snap-inc-ipo": (32, "2017-03-03"),
            "acq-episode-33-overture-with-the-internet-history-podcast": (33, "2017-03-01"),
            "acq-episode-34-starbucks-ipo-with-dan-levitan": (34, "2017-03-01"),
            "acq-episode-35-oculus": (35, "2017-03-01"),
            "acq-episode-36-the-la-clippers": (36, "2017-04-01"),
        }
        if ep_id in nums:
            n, d = nums[ep_id]
            data["metadata"]["episode_number"] = n
            if not data["metadata"].get("date"):
                data["metadata"]["date"] = d

        titles = {
            "acq-episode-28-the-amazon-ipo-with-original-amazon-board-member-tom-alberg": "The Amazon IPO (with Tom Alberg)",
            "acq-episode-30-pa-semi-authentec": "P.A. Semi & AuthenTec",
            "acq-episode-31-the-uber-didi-chuxing-merger-with-brad-stone-author-of-the-upstarts-the-everything-store": "The Uber–Didi Merger (with Brad Stone)",
            "acq-episode-32-the-snap-inc-ipo": "The Snap Inc. IPO",
            "acq-episode-33-overture-with-the-internet-history-podcast": "Overture (with Internet History Podcast)",
            "acq-episode-34-starbucks-ipo-with-dan-levitan": "The Starbucks IPO (with Dan Levitan)",
            "acq-episode-35-oculus": "Oculus (Facebook acquisition)",
            "acq-episode-36-the-la-clippers": "The LA Clippers (Steve Ballmer)",
        }
        data["metadata"]["title"] = titles.get(ep_id, data["metadata"]["title"])

        out = APPROVED / f"{ep_id}.json"
        out.write_text(json.dumps(data, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
        report = validate_summary(data, tmpl)
        msgs = [f"[{i.severity}] {i.section}: {i.message}" for i in report.issues]
        results.append((ep_id, report.passed, report.total_words, msgs))
        status = "PASS" if report.passed else "FAIL"
        print(f"{status} {ep_id} words={report.total_words} ({report.min_total_words}-{report.max_total_words})")
        for m in msgs:
            print(f"  {m}")

    failed = [r for r in results if not r[1]]
    print(f"\n{len(results) - len(failed)}/{len(results)} passed")
    raise SystemExit(1 if failed else 0)


if __name__ == "__main__":
    main()
