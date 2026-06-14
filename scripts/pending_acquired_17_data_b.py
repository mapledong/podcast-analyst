"""Part B of pending Acquired summaries."""

EXTENDED_B = {}

def _add(ep_id, **body):
    EXTENDED_B[ep_id] = body

_add(
    "acq-michael-mauboussin-master-class-moats-skill-luck-decision-making-and-a-whole-lot-more",
    keywords=["Skill vs Luck", "Expectations Investing", "Competitive Moats"],
    conclusion=(
        "Michael Mauboussin (Counterpoint Global / Morgan Stanley) joins Acquired (~85 min) for a master class spanning The Success Equation, Measuring the Moat, and revised Expectations Investing. Core frameworks: skill defined as repeatable ability to apply knowledge; luck as residual; paradox of skill — as absolute skill rises across fields, relative gaps shrink so outcomes look more random. Base rates beat narratives; short track records lie. VC persistence may reflect preferential attachment (success breeds deal flow) not just skill. 2021 market: low discount rates inflate expectations — reverse DCF asks what growth is priced in. Introduced at Capital Camp by Patrick O'Shaughnessy and Brent Beshore."
    ),
    background=(
        "Season 9 interview (~Oct 2021) covers intangible asset shift in accounting, public-to-private equity migration, moat measurement methodology, streak analysis (skill/luck decomposition), and whether a $10 trillion company is plausible.\n\nMauboussin's work is Acquired's most frequent carve-out category — hosts finally interview primary source on decision quality under uncertainty."
    ),
    important_facts=[
        "Michael Mauboussin leads Consilient Research at Counterpoint Global (Morgan Stanley Investment Management) after Credit Suisse and Legg Mason strategist roles.",
        "Paradox of skill (from Stephen Jay Gould baseball insight): when all participants' absolute skill rises, luck dominates relative outcomes.",
        "Measuring the Moat research quantifies competitive advantage duration and ROIC spread persistence across industries.",
        "Expectations Investing (with Rappaport, revised 2021) teaches reverse-engineering priced growth from market multiples.",
        "Episode recorded October 2021 amid near-zero rates — Mauboussin emphasizes expectations vs fundamentals gap for public markets.",
    ],
    mental_model={
        "name": "Base Rates Over Stories",
        "components": "Define skill (knowledge applied) vs luck (residual). Use base rates for categories (VC top-decile persistence, moat half-lives) before accepting founder narratives. Paradox of skill: professionalization narrows edge — streaks need statistical testing. Expectations investing: price embeds future; compare implied assumptions to plausible outcomes.",
        "application": "Investors should write down implied growth in any multiple before debating quality. Operators: in high-skill fields (VC, pro sports), variance management (weak player increases variance) beats copying leaders' strategies.",
    },
    competitive_advantage=(
        "Mauboussin's edge is cross-disciplinary synthesis — Santa Fe Institute complexity, sports analytics, capital markets — packaged for institutional allocators.\n\nCounterpoint Global platform provides patient capital for long-horizon frameworks; research franchise attracts top allocators and founders.\n\nWeaknesses: frameworks lag regime changes (2021 low-rate assumptions shifted fast); intangible accounting still imperfect for moat measurement.\n\nVersus sell-side strategists: Mauboussin sells mental models not stock picks — durable with Acquired audience but harder to monetize as alpha directly.\n\nVC persistence discussion: preferential attachment vs skill unresolved — implications for LP allocation to top-decile only."
    ),
    key_insights=[
        {
            "view": "Paradox of skill hides narrowing edges.",
            "question": "Why do outcomes feel randomer now?",
            "answer": "Absolute skill higher than ever (investors, athletes) — relative differences shrink, luck determines winners. Short streaks mislead; need large samples and base rates.",
        },
        {
            "view": "Price embeds expectations not value.",
            "question": "How think about 2021 multiples?",
            "answer": "Reverse DCF / expectations investing — ask what growth margin of safety is priced. Low discount rates inflate all assets; shift to fundamentals when rates rise.",
        },
        {
            "view": "Moats are measurable not mystical.",
            "question": "What does Measuring the Moat add?",
            "answer": "ROIC spread persistence, industry structure, customer captivity scored — moves 7 Powers from qualitative to empirical priors for analysts.",
        },
        {
            "view": "VC top firms may feed themselves.",
            "question": "Is persistence skill or access?",
            "answer": "Preferential attachment: winning deals improves flow, which improves returns — hard to separate from pure picking skill; LPs overweight recent winners at peril.",
        },
        {
            "view": "Weak players should increase variance.",
            "question": "Success Equation strategy?",
            "answer": "Strong player simplifies game to overwhelm with skill; weak player runs trick plays — increases variance. Applies to startups vs incumbents, not just sports.",
        },
    ],
    top_investment_implications=[
        {
            "ticker": "SPY",
            "direction": "Watch",
            "confidence": "Low",
            "thesis": "Expectations-investing framework applies to index level — implied growth and margin assumptions in aggregate multiples signal regime risk when rates shift; not a tactical call.",
        }
    ],
    golden_quotes=[
        '"When skill improves uniformly, luck becomes more important in defining outcomes." — Mauboussin on paradox of skill.',
        '"Base rates are the single most important thing investors ignore." — recurring Mauboussin theme cited by hosts.',
        '"Price is what you pay; expectations are what you get." — Expectations Investing framework paraphrased in episode.',
    ],
    chronology={
        "subject": "Michael Mauboussin Research",
        "events": [
            {"date": "1990s", "event": "Legg Mason strategist; early moat writing"},
            {"date": "2000s", "event": "Credit Suisse; Santa Fe Institute board"},
            {"date": "2012", "event": "The Success Equation published"},
            {"date": "2016", "event": "Measuring the Moat research circulated widely"},
            {"date": "2020", "event": "Joins Counterpoint Global / Morgan Stanley"},
            {"date": "2021", "event": "Expectations Investing revised edition released"},
            {"date": "2021-10", "event": "Acquired master class interview airs"},
            {"date": "2021", "event": "Capital Camp intro via O'Shaughnessy/Beshore"},
            {"date": "2021", "event": "Near-zero rates environment discussed for valuations"},
            {"date": "2021", "event": "Paradox of skill framework applied to VC persistence"},
        ],
    },
)

_add(
    "acq-meituan",
    keywords=["Meituan", "Super App", "On-Demand Services"],
    conclusion=(
        "Meituan is China's local-commerce super-app — food delivery, in-store dining, hotel/travel, grocery — born from the Groupon wars (千团大战) where 5,000+ group-buy clones collapsed to handful. Wang Xing (serial founder: Fanfou,校内) merged Dianping rivalry into Meituan-Dianping (2015), later dropped Dianping branding. ~$100B+ market cap at episode (~2021) on hundreds of millions of annual transactions; razor-thin delivery margins offset by advertising and in-store SaaS. Alibaba/Tencent proxy war (Alipay vs WeChat pay) shaped early funding. Lesson: winner-take-most in two-sided local marketplaces when density + logistics scale compound — but regulatory and common-prosperity crackdowns post-2021 reset multiples."
    ),
    background=(
        "Season 8 Episode 3 (~143 min) traces Wang Xing from Tsinghua/US dropout through China's first SNS clones, Groupon copycat explosion (~2010-11), Meituan survival, Dianping truce, mobile pivot, and COVID-era delivery surge.\n\nHosts compare to Yelp/OpenTable, Uber Eats, and Amazon local — emphasizing China mobile-first payment rail advantage."
    ),
    important_facts=[
        "China's group-buying 'war of a thousand regiments' (千团大战) saw over 5,000 Groupon clones launch; Meituan among ~3 survivors with Dianping and Nuomi.",
        "Meituan-Dianping merger announced October 2015 combined China's top two local-services platforms under Wang Xing leadership.",
        "Meituan IPO'd in Hong Kong September 2018 raising ~$4.2 billion — one of largest HK tech listings of that cycle.",
        "Food delivery unit processed billions of orders annually by 2020; take rate per order often under 10% RMB — margin from ads and merchant SaaS.",
        "Episode recording (~March 2021) preceded major 2021 regulatory actions against Chinese internet platforms affecting Meituan's market cap.",
    ],
    mental_model={
        "name": "Density Before Diversity",
        "components": "Win local commerce by city-level density (riders, merchants, users) before national breadth. Groupon clone war killed undisciplined expansion — Meituan survived via ops excellence and mobile pivot. Super-app cross-sell (delivery → hotel → grocery) raises LTV when payment rail unified (WeChat/Alipay).",
        "application": "Marketplace founders in multi-city rollouts should prove unit economics in one city vs Groupon-style land grab. Super-app strategy requires shared logistics/ads infrastructure — not just app icon bundling.",
    },
    competitive_advantage=(
        "Meituan's moat is local density + delivery network + merchant ad inventory — switching costs for restaurants once POS/marketing integrated.\n\nWang Xing's serial-founder pattern recognition and ruthless capital efficiency vs burned competitors.\n\nWeaknesses: subsidy wars with Ele.me (Alibaba); low delivery margins; regulatory antitrust and gig-worker rules. Tencent/Alibaba shareholder politics.\n\nVersus Dianping pre-merger: review content + transaction — merged entity eliminated destructive subsidy competition.\n\nUS analogues (Yelp, Grubhub) lack super-app payment scale — China mobile-first rails unreplicable."
    ),
    key_insights=[
        {
            "view": "千团大战 was venture bonfire.",
            "question": "Why 5,000 Groupon clones?",
            "answer": "2010-11 China VC frenzy copied US models — capital deployed faster than unit economics proved. ~3 survivors after subsidy burn; Meituan won on execution not first-mover.",
        },
        {
            "view": "Merge with rival beats price war.",
            "question": "Why Dianping merger?",
            "answer": "Dual subsidy war unsustainable — 2015 merger ended destructive competition; Wang Xing CEO. Review + transaction unified; later brand simplified to Meituan.",
        },
        {
            "view": "Delivery is funnel not profit center.",
            "question": "How make money on thin take rates?",
            "answer": "Delivery acquires users for higher-margin ads, hotel booking, in-store payments — super-app LTV math. Single-digit RMB per order acceptable at scale.",
        },
        {
            "view": "Wang Xing is China's serial pattern matcher.",
            "question": "Founder advantage?",
            "answer": "Fanfou/校内 failures taught regulatory and product lessons — copied US ideas faster but adapted to mobile/super-app reality second time.",
        },
        {
            "view": "Regulatory regime is existential post-2021.",
            "question": "Investment risk?",
            "answer": "Episode predates common-prosperity crackdown — antitrust fines and gig-worker rules hit multiples. Business durable; policy discount persistent.",
        },
    ],
    top_investment_implications=[
        {
            "ticker": "3690.HK",
            "direction": "Watch",
            "confidence": "Medium",
            "thesis": "Meituan HK-listed — track delivery order growth vs regulatory fines and margin recovery in in-store/ads segments; China consumer policy remains primary variable.",
        }
    ],
    golden_quotes=[
        '"War of a thousand regiments." — Ben/David on 千团大战 Groupon clone collapse.',
        '"Wang Xing copied America faster than Americans copied America." — host framing of serial founder arc.',
        '"Delivery is the acquisition channel for the super-app." — Meituan monetization logic from episode.',
    ],
    chronology={
        "subject": "Meituan",
        "events": [
            {"date": "2010", "event": "Meituan founded as Groupon clone; 千团大战 begins"},
            {"date": "2011", "event": "Thousands of group-buy sites peak; mass consolidation"},
            {"date": "2013", "event": "Mobile app pivot accelerates food delivery"},
            {"date": "2015", "event": "Meituan-Dianping merger announced"},
            {"date": "2018", "event": "Hong Kong IPO raises ~$4.2 billion"},
            {"date": "2020", "event": "COVID delivery surge; grocery expansion"},
            {"date": "2021", "event": "Acquired episode; regulatory scrutiny intensifies"},
            {"date": "2021", "event": "Common-prosperity policy pressures internet platforms"},
            {"date": "2022", "event": "Grocery and in-store SaaS expansion continues post-IPO era"},
            {"date": "2023", "event": "Meituan remains dominant local-services platform in China"},
        ],
    },
)

_add(
    "acq-season-2-episode-1zappos-with-alfred-lin",
    keywords=["Zappos Acquisition", "Customer Service", "Amazon M&A"],
    conclusion=(
        "Alfred Lin (Zappos chairman/COO, Sequoia partner) joins Season 2 premiere on Amazon's July 2009 Zappos acquisition — $1.2 billion all-stock after Endless.com price war. Tony Hsieh/Alfred Harvard pizza lore → LinkExchange → Zappos: customer service as moat (365-day returns, call-center culture) beat Amazon on shoes until Bezos wore them down. Merger email: 100+ shareholders swap for Amazon stock; Tony/Alfred stay; independent-ish culture preserved in Vegas. Stock unanimous post-crisis (undervalued AMZN). Kiva robots in fulfillment. Grade: classic 'people + business line' — Amazon bought culture Amazon couldn't replicate."
    ),
    background=(
        "Season 2 Episode 1 (~79 min, Jan 2018) — audio quality issues noted by hosts. Alfred traces Quincy House Harvard days, Tellme pivot, Zappos finance/ops, Amazon Endless competition, and negotiation for stock vs cash.\n\nCarve outs: Ben Andrew Mason Recode; David Justin O'Beirne Google Maps moat; Alfred Walter Isaacson biographies."
    ),
    important_facts=[
        "Amazon acquired Zappos for $1.2 billion in stock announced July 2009 — among largest e-commerce acquisitions of era.",
        "Amazon launched Endless.com (shoes/handbags) to compete before acquisition — classic Bezos siege tactic.",
        "Zappos offered 365-day return policy and free shipping both ways — customer service as competitive weapon vs price.",
        "Over 100 Zappos shareholders exchanged stock for Amazon shares in definitive agreement per Tony/Alfred employee email.",
        "Alfred Lin and Tony Hsieh committed to remain post-close; Zappos maintained separate Vegas culture within Amazon.",
    ],
    mental_model={
        "name": "Service Moat vs Bezos Siege",
        "components": "Zappos: narrow category (shoes), extreme service NPS, culture as asset. Amazon: Endless price war + logistics scale — competes until acquihire cheaper. Stock deal aligned post-2009 crisis undervaluation — tax/logic vs cash. Integration: preserve culture shell, absorb logistics tech (Kiva).",
        "application": "Category specialists beating Amazon on experience still face existential siege — exit via acquisition when Amazon enters vertical. Culture retention post-MA requires explicit independence charter (Zappos model) or dilution inevitable.",
    },
    competitive_advantage=(
        "Zappos moat was customer obsession — 365-day returns, empowered call reps, Vegas culture tours — unreplicable by Amazon's efficiency culture without acquisition.\n\nTony/Alfred operator pairing: visionary + financial discipline from LinkExchange/Tellme scars.\n\nWeaknesses: single-category; Las Vegas recruiting; housing-crisis employee wealth concentration in Zappos stock motivated sale.\n\nVersus Endless: Amazon couldn't out-service Zappos; could only out-last or buy.\n\nPost-acquisition: Kiva automation + Amazon logistics improved unit economics while brand decay debated years later."
    ),
    key_insights=[
        {
            "view": "Endless was siege not side project.",
            "question": "Why did Zappos sell?",
            "answer": "Bezos launched Endless.com targeting shoes — Moritz saw eToys fate replay. Zappos couldn't match Amazon logistics R&D; employee wealth tied to illiquid stock post-housing crash — stock deal unlocked value.",
        },
        {
            "view": "Stock deal unanimous for tax/AMZN upside.",
            "question": "Why all-stock?",
            "answer": "Post-2009 AMZN undervalued — Alfred negotiated stock vs initial cash proposal; shareholders bet on Amazon compounder. Some sold immediately, others held decades.",
        },
        {
            "view": "Culture was the acquired asset.",
            "question": "Acquisition category?",
            "answer": "People + business line — Amazon bought service culture it couldn't build. Independence preserved deliberately; contrast with typical Amazon absorption.",
        },
        {
            "view": "Alfred is finance yin to Tony yang.",
            "question": "Guest value?",
            "answer": "Lin brought Sequoia/Tellme discipline — pizza startup lore humanizes but ops/finance mastery scaled Zappos through 千团-style survival not applicable but Amazon war yes.",
        },
        {
            "view": "Few beat Amazon head-on in commerce.",
            "question": "Strategic lesson?",
            "answer": "Zappos among only companies to compete successfully on experience in a vertical — still ended in acquisition. Narrow dominance ≠ platform independence long-term.",
        },
    ],
    top_investment_implications=[
        {
            "ticker": "AMZN",
            "direction": "Watch",
            "confidence": "Low",
            "thesis": "Zappos legacy illustrates Amazon vertical siege playbook — relevant when evaluating DTC brands Amazon may enter; not a current financial driver.",
        }
    ],
    golden_quotes=[
        '"Success has many fathers." — Alfred Lin on $1.2B stock deal attribution humor.',
        '"We are willing to be wrong on the phone with the customer." — Zappos service philosophy cited in episode.',
        '"Amazon launched Endless.com to compete — classic Bezos." — host framing of pre-acquisition siege.',
    ],
    chronology={
        "subject": "Zappos & Amazon Acquisition",
        "events": [
            {"date": "1999", "event": "Zappos founded; Nick Swinmurn shoe e-commerce"},
            {"date": "2000s", "event": "Tony Hsieh CEO; Alfred Lin chairman/COO"},
            {"date": "2005", "event": "Amazon launches Endless.com competing in shoes"},
            {"date": "2007-09", "event": "Financial crisis; housing wealth destruction for employees"},
            {"date": "2009-07", "event": "Amazon announces $1.2B all-stock acquisition"},
            {"date": "2009", "event": "100+ shareholders swap; Tony/Alfred stay; culture charter"},
            {"date": "2018", "event": "Acquired Season 2 interview with Alfred Lin"},
            {"date": "2010s", "event": "Kiva robots deployed in fulfillment centers"},
            {"date": "2020", "event": "Tony Hsieh death; Zappos culture legacy debated"},
            {"date": "2015", "event": "Amazon fully integrates Zappos logistics over time"},
        ],
    },
)

_add(
    "acq-2017-holiday-special",
    keywords=["2017 Year Review", "Bitcoin Mania", "Prediction Scorecard"],
    conclusion=(
        "Episode 51 (~82 min, Dec 18, 2017) cozy year-end special: Ben/David score Episode 29's 2017 predictions (partially right on Snap IPO, ML platformization), review 2017 tech moments, and joke about Bitcoin price in Dec 2018. Retrospective on Season 1 (~51 episodes), SF meetup announced Jan 18 2018, extended carve-outs (Shoe Dog, His Dark Materials, Blade Runner 2049, Odesza, Ezra Klein/Yuval Harari). Links Josh Elman shared experiences and Patrick McKenzie distribution essays. Less structured than Episode 29 — fireside format grading themselves on forecasts while Bitcoin mania peaks near $20K."
    ),
    background=(
        "Episode 51 closes Season 1 (Dec 18, 2017) — distinct from Episode 29 (Jan 2017) which made predictions; this episode grades them. Hosts reflect on Acquired's first year, community growth, and chaotic 2017 headlines: crypto ICO frenzy, mega-M&A, IPO wave.\n\nCarve-outs span books, NYT AI awakening article, Bill Simmons/Jimmy Iovine podcast, Creed, Last Jedi — holiday tradition established."
    ),
    important_facts=[
        "Episode 51 published December 18, 2017 — Season 1 capstone at approximately 82 minutes runtime.",
        "Bitcoin traded near $10,000–$20,000 in December 2017 during recording — hosts joked about Dec 2018 price.",
        "Episode 29 (January 2017) predictions partially validated: Snap IPO March 2017 at $17/share occurred as forecast.",
        "SF Acquired meetup announced for evening of January 18, 2018 per episode show notes.",
        "Season 1 completed approximately 51 episodes in first year of Acquired per holiday retrospective.",
    ],
    mental_model={
        "name": "Prediction Scorecard Discipline",
        "components": "Make forecasts explicit (Episode 29) then grade annually (Episode 51) — reduces hindsight bias. Holiday format prioritizes community + carve-outs over deal analysis. Bitcoin price joke anchors speculative vs fundamental investing distinction hosts maintain elsewhere.",
        "application": "Investors and analysts should maintain written prediction logs with annual review — Acquired models intellectual honesty without formal scoring rubric. Meta-episodes build audience trust between deep dives.",
    },
    competitive_advantage=(
        "Acquired holiday episodes humanize hosts — listener relationship deepens vs pure M&A factory.\n\nPrediction scorecard creates continuity incentive for annual listeners.\n\nWeaknesses: dated crypto references; less evergreen than company histories.\n\nVersus news podcasts: ties year review to prior deep episodes (Snap, Stitch Fix) — content library compounds."
    ),
    key_insights=[
        {
            "view": "Episode 29 predictions mixed success.",
            "question": "How wrong were we?",
            "answer": "Snap IPO correct; VR timeline optimistic; ML commoditization on track. Hosts acknowledge 'you get what you pay for' disclaimer from prior special — intellectual honesty builds credibility.",
        },
        {
            "view": "2017 was crypto plus corp dev.",
            "question": "Year themes?",
            "answer": "Bitcoin/ICO mania concurrent with Amazon/Whole Foods, Broadcom/Qualcomm — speculative assets and strategic M&A both heated in low-rate environment.",
        },
        {
            "view": "Community became product.",
            "question": "Why meetup announcement?",
            "answer": "Slack community growth — Acquired transitions from podcast to gathering brand; SF meetup Jan 18 2018 formalizes listener network.",
        },
        {
            "view": "Carve-outs are discovery engine.",
            "question": "Extended recommendations?",
            "answer": "Shoe Dog, His Dark Materials, NYT AI awakening, Patrick McKenzie distribution — hosts curate adjacent learning; recurs every holiday episode.",
        },
        {
            "view": "Season 2 teased implicitly.",
            "question": "What's next?",
            "answer": "Season 1 closure with Zappos/Alfred Lin Season 2 premiere imminent — quality bar rises with guest interviews after 51 solo deep dives.",
        },
    ],
    top_investment_implications=[
        {
            "ticker": "BTC",
            "direction": "Watch",
            "confidence": "Low",
            "thesis": "Episode treats 2017 crypto mania as cultural moment not advice — illustrates speculative cycles decoupled from operating-business analysis.",
        }
    ],
    golden_quotes=[
        '"How wildly off were we on last year\'s predictions?" — Episode 51 opening premise.',
        '"What price will Bitcoin be trading at in December 2018???" — show notes joke anchoring crypto skepticism.',
        '"You get what you pay for here." — callback to Episode 29 predictions disclaimer.',
    ],
    chronology={
        "subject": "Acquired 2017 Holiday & Season 1",
        "events": [
            {"date": "2016", "event": "Acquired launches; first full season begins"},
            {"date": "2017-01", "event": "Episode 29 2017 predictions special"},
            {"date": "2017-03", "event": "Snap IPO validates one major prediction"},
            {"date": "2017-06", "event": "Amazon Whole Foods $13.7B among year headlines"},
            {"date": "2017-11", "event": "Broadcom-Qualcomm bid; Stitch Fix IPO"},
            {"date": "2017-12", "event": "Bitcoin nears $20K peak"},
            {"date": "2017-12-18", "event": "Episode 51 holiday special airs"},
            {"date": "2018-01-18", "event": "SF Acquired meetup announced date"},
            {"date": "2018-01", "event": "Season 2 launches with Zappos episode"},
            {"date": "2018", "event": "Bitcoin crashes from 2017 highs — prediction joke aged"},
        ],
    },
)

_add(
    "acq-the-stitch-fix-ipo",
    keywords=["Stitch Fix IPO", "Katrina Lake", "Algorithmic Retail"],
    conclusion=(
        "Stitch Fix IPO episode (~78 min, Dec 2017) covers Katrina Lake's 2010 HBS-start (originally Rack Habit) — data science plus human stylists shipping curated boxes. ~$977M revenue fiscal 2017 (+34% YoY), ~$61M adjusted EBITDA, only ~$42.5M total capital raised pre-IPO — capital efficiency marvel. Benchmark Bill Gurley $12M at $40M (2011); later round $300M val. IPO downsized to $15/share (below range) Nov 16, 2017 — ~$1.5B market cap opening; Katrina ~15% worth ~$250M. Dual-class: Class B 99.1% voting. Hosts grade IPO timing vs Amazon/Warby skepticism; women-led cap table rarity (55% management female)."
    ),
    background=(
        "Episode 49 walks founding (co-founder Erin Flynn lawsuit departure), stylist network (3,400+ part-time), fulfillment automation, CAC vs LTV, and public-market reception disconnect despite profitable growth.\n\nCompared to Blue Apron IPO flop as cautionary subscription commerce tale."
    ),
    important_facts=[
        "Stitch Fix raised only approximately $42.5 million total venture capital before IPO — reached ~$977 million revenue fiscal 2017.",
        "IPO priced November 16, 2017 at $15/share (below proposed range) — ~$1.5 billion initial market capitalization.",
        "Katrina Lake retained roughly 15% ownership post-IPO — shares worth approximately $250 million at pricing.",
        "2.2 million active clients at IPO filing with ~31% year-over-year growth; ~86% of employees female.",
        "Bill Gurley/Benchmark invested $12 million Series A at ~$40 million valuation in 2011.",
    ],
    mental_model={
        "name": "Human-in-the-Loop Personalization",
        "components": "Algorithm narrows inventory; stylist adds judgment — hybrid beats pure recommendation engines for apparel fit/taste. Capital efficiency: prove unit economics before scaling spend — $42.5M to ~$1B revenue. IPO downsizing signals public skepticism on category not company quality.",
        "application": "Retail tech should pair ML with domain expert in loop where taste matters — fully automated styling failed competitors. Founder control (dual-class) preserves long-term brand vs quarterly CAC pressure.",
    },
    competitive_advantage=(
        "Stitch Fix moat: stylist network + fit data feedback loop — each shipment improves personalization; switching costs rise with wardrobe history.\n\nCapital efficiency attracts Benchmark; Gurley cited Katrina's financial acumen specifically.\n\nWeaknesses: Amazon Wardrobe/Warby competition; CAC rising; apparel returns economics; IPO market timing 2017 retail skepticism.\n\nVersus pure e-commerce: not inventory browse — curated surprise model different TAM and retention curve.\n\nWomen-led leadership (55% management, 50% board) differentiated Silicon Valley narrative at IPO."
    ),
    key_insights=[
        {
            "view": "Capital efficiency enabled IPO optionality.",
            "question": "Why only $42.5M raised?",
            "answer": "Positive cash flow since 2014 — didn't need mega-rounds. Contrast cash-burn IPOs; Gurley $12M at $40M sufficient to prove hybrid model before $300M round.",
        },
        {
            "view": "Down IPO ≠ bad business.",
            "question": "Why price below range?",
            "answer": "Nov 2017 public markets skeptical retail/subscription post Blue Apron — Stitch Fix profitable but category tainted. Traded up to ~$18.60 within week — market repriced slowly.",
        },
        {
            "view": "Stylists are moat not cost center.",
            "question": "Why humans if data science?",
            "answer": "Apparel taste/subjective fit — algorithm shortlists, stylist finalizes. 3,400 part-time stylists create quality variance competitors can't copy with pure ML.",
        },
        {
            "view": "Dual-class protects founder vision.",
            "question": "Governance?",
            "answer": "Class B ~99.1% voting — Katrina control similar to tech founders; necessary vs public CAC/myopia for brand-first retail.",
        },
        {
            "view": "Women-led IPO rarity matters.",
            "question": "Why highlight gender stats?",
            "answer": "55% management / 86% female workforce — structural diversity at IPO uncommon; Katrina first female CEO to take company public in year of IPO wave.",
        },
    ],
    top_investment_implications=[
        {
            "ticker": "SFIX",
            "direction": "Watch",
            "confidence": "Medium",
            "thesis": "Track active client growth and gross margin per fix — hybrid model durable if CAC controlled; category still Amazon-competitive.",
        }
    ],
    golden_quotes=[
        '"Only $42.5 million raised to nearly $1 billion revenue." — host awe at capital efficiency.',
        '"Coffee is a legal addictive unregulated psychoactive drug." — Daniel James Quora quote on Blue Bottle parallel mindset.',
        '"Unfortunately the IPO was downsized — disconnect between momentum and public reception." — Ben on $15 pricing.',
    ],
    chronology={
        "subject": "Stitch Fix",
        "events": [
            {"date": "2010", "event": "Founded as Rack Habit at Harvard Business School"},
            {"date": "2011", "event": "Benchmark $12M Series A at ~$40M valuation"},
            {"date": "2014", "event": "Cash-flow positive operations begin"},
            {"date": "2016", "event": "~$730M revenue; $30M round at ~$300M valuation"},
            {"date": "2017", "event": "~$977M revenue; S-1 filed"},
            {"date": "2017-11-16", "event": "IPO prices $15/share below range"},
            {"date": "2017-12", "event": "Acquired Episode 49 analysis airs"},
            {"date": "2018", "event": "Public markets re-rate subscription commerce skeptically"},
            {"date": "2020s", "event": "Stitch Fix navigates retail downturn and stylist model evolution"},
            {"date": "2019", "event": "Katrina Lake remains CEO through public-company transition"},
        ],
    },
)

_add(
    "acq-qualcomm-broadcom",
    keywords=["Qualcomm Broadcom", "Semiconductor M&A", "CFIUS"],
    conclusion=(
        "Episode 48 (~58 min, Nov 2017) covers Broadcom's unsolicited ~$103 billion bid for Qualcomm — would-be largest tech acquisition ever — rejected at recording. Hosts trace semiconductor resurgence: Intel/Nervana, Graphcore ML chips, fabless model, CDMA patent licensing, Apple/ Samsung vertical integration. Broadcom (Hock Tan) opportunistic on depressed QCOM from Apple lawsuits. Episode predates March 2018 Trump/CFIUS block on national-security grounds (5G leadership). Graded as unlikely to close — prescient. Wintel duopoly giving way to ARM/mobile + AI silicon wave."
    ),
    background=(
        "Season 1 Episode 48 analyzes hostile dynamics, cash/stock mix, regulatory paths, and industry consolidation drivers (scale for R&D). Pilot accounting sponsor; NZS Capital Qualcomm/Hedy Lamarr research nod.\n\nContrast with later full Qualcomm history episode (Lisbon live) — this is deal-focused not company biography."
    ),
    important_facts=[
        "Broadcom proposed approximately $103 billion acquisition of Qualcomm in November 2017 — largest ever tech M&A offer at time.",
        "Qualcomm board rejected initial offer; QCOM shares depressed by Apple patent royalty litigation during bid period.",
        "President Trump blocked deal March 12, 2018 via executive order citing national security and 5G leadership concerns.",
        "Broadcom was Singapore-domiciled; attempted US re-domicile to ease CFIUS — insufficient for approval.",
        "Both companies fabless — design chips, TSMC/other fabs manufacture; vertical integration by Apple/Samsung threatened supplier power.",
    ],
    mental_model={
        "name": "Scale or Die in Silicon",
        "components": "Semiconductor R&D costs require massive scale — consolidation (Broadcom roll-up) vs IP licensing (Qualcomm CDMA). Hostile bids exploit legal/overhang depressed valuations. CFIUS adds geopolitical layer beyond shareholder value — 5G as strategic asset.",
        "application": "Evaluate chip M&A on customer concentration (Apple) and national-security overlay not just synergies. Fabless model separates design moat from manufacturing — TSMC wins either way.",
    },
    competitive_advantage=(
        "Qualcomm moat: CDMA/4G/5G patent stack + licensing revenue — R&D funded by royalty stream.\n\nBroadcom moat: Hock Tan acquisition integration machine + cost discipline — opportunistic on weakness.\n\nWeaknesses: Apple litigation; customer verticalization; regulatory nationalism.\n\nCombined entity would dominate mobile basband — antitrust + CFIUS fatal combo.\n\nEpisode graded non-deal correctly — shareholders never got premium closure."
    ),
    key_insights=[
        {
            "view": "Depressed QCOM invited predator.",
            "question": "Why hostile now?",
            "answer": "Apple lawsuit crushed multiple — Broadcom opportunistic per Hock Tan playbook. Cash/stock mix debated; Qualcomm management opposed regardless of price.",
        },
        {
            "view": "CFIUS trumped shareholder economics.",
            "question": "Would regulators approve?",
            "answer": "Hosts skeptical Nov 2017 — Trump order March 2018 blocked pre-close citing 5G national security; Singapore HQ mattered despite US re-domicile plan.",
        },
        {
            "view": "Fabless reshaped competition.",
            "question": "Industry structure?",
            "answer": "Qualcomm/Broadcom design; TSMC fabs — value split. Apple in-house modems threaten Qualcomm licensing long-term more than Broadcom ownership.",
        },
        {
            "view": "Silicon innovation revived.",
            "question": "Why cover semis in 2017?",
            "answer": "ML chips (Nervana, Graphcore) ended 'semis boring' era — Acquired previewed later Qualcomm deep-dive. Scale + specialization coexist.",
        },
        {
            "view": "Hostile mega-deals rarely close clean.",
            "question": "Acquired grade?",
            "answer": "Hosts leaned fail — management resistance + regulatory + customer conflict = triple block. Lesson for LBO-style tech roll-ups.",
        },
    ],
    top_investment_implications=[
        {
            "ticker": "QCOM",
            "direction": "Watch",
            "confidence": "Medium",
            "thesis": "Post-block independence — monitor Apple modem insourcing and 5G royalty disputes; licensing model durability key.",
        }
    ],
    golden_quotes=[
        '"Largest tech acquisition of all time — $103 billion." — episode framing at recording.',
        '"CFIUS cares about 5G leadership, not shareholder premium." — implied regulatory thesis validated March 2018.',
        '"Silicon is interesting again." — hosts on ML chip resurgence ending boring-semis narrative.',
    ],
    chronology={
        "subject": "Broadcom-Qualcomm Bid",
        "events": [
            {"date": "2017-11", "event": "Broadcom proposes ~$103B hostile Qualcomm acquisition"},
            {"date": "2017-11", "event": "Qualcomm board rejects offer"},
            {"date": "2017-11-20", "event": "Acquired Episode 48 records analysis"},
            {"date": "2017-11", "event": "Broadcom announces US re-domicile plan"},
            {"date": "2017", "event": "Apple patent litigation depresses QCOM shares"},
            {"date": "2018-01", "event": "CFIUS review intensifies on 5G concerns"},
            {"date": "2018-03", "event": "CFIUS recommends block to President Trump"},
            {"date": "2018-03-12", "event": "Trump executive order blocks deal permanently"},
            {"date": "2018-03", "event": "Broadcom and Qualcomm certify deal termination"},
            {"date": "2018", "event": "Qualcomm continues independent 5G licensing strategy"},
        ],
    },
)

_add(
    "acq-the-atlassian-ipo",
    keywords=["Atlassian IPO", "Bootstrapped SaaS", "Product-Led Growth"],
    conclusion=(
        "Episode 47 (~71 min, Nov 2017): Mike Cannon-Brookes and Scott Farquhar — UNSW classmates who bootstrapped Atlassian to IPO without VC primary capital (only secondary sales pre-IPO). Jira (2002) + Confluence wiki — developer tools sold via website/download, no enterprise sales force. FY2015 ~$320M revenue, ~$6M net profit; IPO Nov 2015 NASDAQ ~$4.4B market cap (ticker TEAM), doubled first year. Pricing: low-touch PLG before acronym existed. Hosts reunite in-person 'land down under.' Carve outs: Shoe Dog, Born to Run."
    ),
    background=(
        "Season 1 covers Sydney origin story, credit-card startup funding, Jira bug tracker for developers, HipChat/Bitbucket/Trello acquisitions post-IPO, and contrast with Salesforce enterprise sales model.\n\nSecondary liquidity for founders/employees without primary dilution — rare path to $4B+ public SaaS."
    ),
    important_facts=[
        "Atlassian IPO'd November 2015 on NASDAQ (TEAM) at approximately $4.4 billion initial market capitalization.",
        "Founders Mike Cannon-Brookes and Scott Farquhar bootstrapped without traditional VC primary rounds — secondary sales only pre-IPO.",
        "Jira launched 2002 as developer bug tracker; Confluence added team wiki — sold via website with no field sales team.",
        "Fiscal 2015 revenue approximately $320 million with about $6 million net profit per S-1 metrics cited in episode.",
        "Stock approximately doubled in first year post-IPO per episode 'spoiler' — rare bootstrapped SaaS public success.",
    ],
    mental_model={
        "name": "Zero-Touch Enterprise PLG",
        "components": "Developer tools spread bottom-up — credit card purchase, viral team expansion, land-before-expand. No sales force keeps S&M low vs Salesforce benchmark. Bootstrapping forces discipline — secondary liquidity satisfies employees without primary dilution until IPO scale requires public currency for M&A (Trello).",
        "application": "B2B founders: prove product-led motion before hiring enterprise sales — Atlassian scaled to $320M revenue pre-IPO without feet on street. Secondary programs retain talent when staying private longer.",
    },
    competitive_advantage=(
        "Atlassian moat: Jira workflow embedding in dev teams — switching costs high once sprints/docs integrated. Confluence + Jira bundle increases stickiness.\n\nPLG distribution: low CAC vs enterprise sales peers; global download model from day one.\n\nWeaknesses: no sales force limits upmarket early; HipChat lost to Slack; post-IPO M&A needed for Trello/Statuspage breadth.\n\nVersus Salesforce: opposite GTM — product pulls vs sales pushes. Both valid at scale.\n\nBootstrapped origin = founder control + capital efficiency legend in SaaS."
    ),
    key_insights=[
        {
            "view": "Bootstrap to IPO is rare not impossible.",
            "question": "No VC primary?",
            "answer": "Credit card funded early; secondary sales provided employee liquidity — avoided dilution until public markets. $320M revenue pre-IPO proves PLG scale without sales army.",
        },
        {
            "view": "Developers buy without sales calls.",
            "question": "No sales team?",
            "answer": "Jira sold online to engineers — bottom-up adoption inside orgs. S&M efficiency structural advantage vs Oracle/Salesforce enterprise motion.",
        },
        {
            "view": "IPO was liquidity not rescue.",
            "question": "Why go public 2015?",
            "answer": "Profitable, growing — public currency for acquisitions (Bitbucket, Trello) and employee liquidity at scale. Not cash-burn desperation unlike many 2015 unicorns.",
        },
        {
            "view": "Australian founders global day-one.",
            "question": "Location disadvantage?",
            "answer": "Download distribution bypassed Sydney geography — US market accessible without SF HQ initially. Cannon-Brookes later climate/energy activism separate from ops.",
        },
        {
            "view": "Post-IPO M&A fills product gaps.",
            "question": "Growth after IPO?",
            "answer": "HipChat lost to Slack; Trello/Statuspage acquisitions extended beyond dev tools — public stock as currency enabled platform expansion.",
        },
    ],
    top_investment_implications=[
        {
            "ticker": "TEAM",
            "direction": "Watch",
            "confidence": "Medium",
            "thesis": "PLG SaaS benchmark — monitor cloud migration revenue and ITSM competition vs ServiceNow; bootstrapped culture vs enterprise upmarket push.",
        }
    ],
    golden_quotes=[
        '"Granddaddy of all bootstrapped tech success stories." — episode tagline on Atlassian.',
        '"No sales team — sold from a website." — core PLG astonishment for 2017 listeners.',
        '"Stock doubled in the first year post-IPO." — host spoiler on TEAM performance.',
    ],
    chronology={
        "subject": "Atlassian",
        "events": [
            {"date": "2002", "event": "Jira launched by Cannon-Brookes and Farquhar"},
            {"date": "2004", "event": "Confluence wiki product added"},
            {"date": "2010s", "event": "Bitbucket acquired; HipChat developed"},
            {"date": "2015", "event": "NASDAQ IPO ~$4.4B market cap (TEAM)"},
            {"date": "2017", "event": "Acquired Episode 47; Trello acquisition era"},
            {"date": "2017-11", "event": "Hosts record in Australia in-person"},
            {"date": "2018", "event": "Trello acquired for ~$425M expanding beyond dev tools"},
            {"date": "2019", "event": "Statuspage and other SaaS tuck-ins continue"},
            {"date": "2020s", "event": "Atlassian surpasses $50B market cap in SaaS bull market"},
            {"date": "2016", "event": "HipChat competes with Slack before losing share"},
        ],
    },
)

_add(
    "acq-blue-bottle-coffee",
    keywords=["Blue Bottle Coffee", "Nestlé Acquisition", "Third Wave Coffee"],
    conclusion=(
        "Episode 46 (~69 min, Oct 2017): Nestlé acquires 68% of Blue Bottle for reported ~$425M (September 2017) — ~$625M implied valuation. James Freeman: freelance clarinetist → oven-roasting beans → Hayes Valley kiosk (2005) → Japanese-minimalist Third Wave aesthetic. Raised $5M (2008, Sacca/Lowercase), $20M (2012), $75M Fidelity (2015) across ~40 stores — not an internet company despite VC hype. Daniel James Quora: 'legal addictive psychoactive drug.' Tension: founders anti-IPO vs Fidelity needing liquidity — majority sale keeps 32% founder stake independent board. Acquisition category: product/brand vs business line — Nestlé brand leverage into US single-serve."
    ),
    background=(
        "Second coffee episode after Starbucks IPO — Seattle podcast obligation. Compares Third Wave (Stumptown, Intelligentsia) to Starbucks Second Wave. Mint Plaza location two blocks from Twitter HQ — ecosystem density drives adoption.\n\nHosts debate Nestlé destroying brand vs capital for expansion; Juicero/Nespresso US <5% vs Europe 70% single-serve."
    ),
    important_facts=[
        "Nestlé acquired 68% of Blue Bottle for approximately $425 million in September 2017 — ~$625 million implied total valuation.",
        "Blue Bottle operated roughly 40 retail locations plus Tokyo stores at acquisition after raising ~$100M+ venture capital.",
        "2008 seed round $5 million from Kohlberg Ventures and Chris Sacca's Lowercase Capital ($4M fund era).",
        "2012 Series B $20 million led by Index Ventures and Google Ventures at peak 'sign of apocalypse' VC coffee skepticism.",
        "James Freeman retained 32% stake with independent board — majority buyout not full acquisition per deal structure.",
    ],
    mental_model={
        "name": "Brand Over Business Line",
        "components": "Nestlé bought Third Wave credibility it couldn't build — $625M for ~40 cafes implies brand not cash-flow math. VC pressure (Fidelity public-market investor) conflicts founder anti-IPO ideology — majority sale resolves LP exit. Physical proximity to Twitter/tech employees created self-fulfilling tastemaker customer base.",
        "application": "Consumer brand M&A: acquirer pays for permission to enter premium segment — integration landmines if Nestlé logo appears on packaging. Founders raising from mutual funds should expect liquidity timeline conflict.",
    },
    competitive_advantage=(
        "Blue Bottle moat: aesthetic + quality obsession — one-size cups, no Wi-Fi, Japanese precision; tech employee density as early adopters.\n\nFreeman product taste + VC network (Sacca, Systrom, Dorsey orbit) created halo.\n\nWeaknesses: high fixed costs per cafe; ~$2M revenue/store math vs $625M valuation; Nestlé integration risk.\n\nVersus Starbucks: anti-scale philosophy — tension with Nestlé mass single-serve (Nespresso US <5% share).\n\nCategory: product/brand acquisition — Nestlé cannot replicate coolness internally at any price."
    ),
    key_insights=[
        {
            "view": "Not an internet company despite VC.",
            "question": "Why VC in coffee?",
            "answer": "2012 round mocked as apocalypse sign — Blue Bottle never pretended SaaS margins. Drug-like retention + premium pricing justified investment; Daniel James Quora quote captures thesis.",
        },
        {
            "view": "Majority sale resolves LP-founder conflict.",
            "question": "Why 68% not 100%?",
            "answer": "Freeman/Meehan anti-IPO vs Fidelity liquidity need — Nestlé majority cashes LPs, founders keep 32% + board independence to protect brand.",
        },
        {
            "view": "Location IS distribution in SF.",
            "question": "Mint Plaza effect?",
            "answer": "Two blocks from Twitter HQ — physical proximity to tech tastemakers replaced digital growth hacks. Ecosystem feeding now cliché but worked 2008-12.",
        },
        {
            "view": "Nestlé needed US premium coffee.",
            "question": "Strategic rationale?",
            "answer": "Nespresso dominates Europe (~70% single-serve) but <5% US — Blue Bottle brand could reposition US beverage line vs Keurig.",
        },
        {
            "view": "Apple Store parallels overstated.",
            "question": "Scale like Apple retail?",
            "answer": "Ben/David debate — Apple scaled minimal SKUs globally; Blue Bottle 40 stores vs Starbucks 24,000 — brand acquisition not unit-economic clone.",
        },
    ],
    top_investment_implications=[
        {
            "ticker": "NSRGY",
            "direction": "Watch",
            "confidence": "Low",
            "thesis": "Nestlé premium coffee US strategy — track whether Blue Bottle brand extended without dilution; immaterial to conglomerate financials.",
        }
    ],
    golden_quotes=[
        '"It can\'t be turtles all the way down. There has to be a pool at the bottom." — David cold open teaser.',
        '"Coffee is a legal, addictive, unregulated psychoactive drug with cheap ingredients and premium pricing." — Daniel James on Quora, cited in episode.',
        '"We never wanted to go public." — Freeman/Meehan ideology vs Fidelity liquidity tension.',
    ],
    chronology={
        "subject": "Blue Bottle Coffee",
        "events": [
            {"date": "2002", "event": "James Freeman begins home oven roasting"},
            {"date": "2005", "event": "First Hayes Valley kiosk opens"},
            {"date": "2008", "event": "$5M seed from Sacca/Lowercase"},
            {"date": "2012", "event": "$20M Series B Index/GV — VC skepticism peak"},
            {"date": "2015", "event": "$75M Fidelity round; ~30+ stores"},
            {"date": "2017-09", "event": "Nestlé acquires 68% for ~$425M"},
            {"date": "2017-10", "event": "Acquired Episode 46 analysis"},
            {"date": "2018", "event": "Founders retain 32% stake under Nestlé majority ownership"},
            {"date": "2020s", "event": "Third Wave consolidation continues via PE/strategic buyers"},
            {"date": "2021", "event": "Nestlé explores Blue Bottle US single-serve expansion"},
        ],
    },
)

_add(
    "acq-special-2016-review-and-2017-predictions",
    keywords=["2016 Tech Review", "2017 Predictions", "Aggregation Theory"],
    conclusion=(
        "Episode 29 (~80 min, Jan 2017) meta-review: Ben/David tally 2016 Acquired tech themes — Aggregation Theory (6 episodes), network effects (4), start-small niche (4), growth culture (4), flywheels (3), business-model disruption (3). 2017 predictions: Aggregation spreads beyond tech, Snap IPO courage, ML commoditization with data moats, VR native experiences, automation/UBI anxiety. Recorded Dec 30, 2016 — Snap March 2017 IPO validated; UBI/automation angst ahead of curve. Extended carve-outs: On Writing Well, Wait But Why, Ezra Klein/Patrick Collison."
    ),
    background=(
        "Recorded Dec 30, 2016; published early 2017. Differs from standard M&A format — quantitative review of first full Acquired season plus extended carve-outs section (books, podcasts, apps).\n\nBen Thompson Aggregation Theory as dominant lens; trinity of startup execution themes beneath meta-layer."
    ),
    important_facts=[
        "Aggregation Theory referenced in 6 of Ben/David's 2016 Acquired episodes — highest-frequency theme that year.",
        "Network effects, start-small niche focus, and growth culture each appeared in 4 episodes per host tally.",
        "Snap Inc. IPO predicted for H1 2017 — priced March 2017 at $17/share.",
        "Episode numbered 29 in Season 1; duration approximately 80 minutes.",
        "Hosts recorded December 30, 2016 with editing to publish in early January 2017.",
    ],
    mental_model={
        "name": "Theme Audit Before Forecast",
        "components": "Quantify recurring frameworks in own work before predicting — reduces hidden repetition bias. Aggregation Theory as meta; execution trinity (niche, growth culture, network effects) as operational layer. Predictions explicitly low-confidence ('you get what you pay for').",
        "application": "Content creators and investors should periodically audit stated theses for frequency — overused lens may miss contrarian risks. Pair macro predictions with explicit uncertainty.",
    },
    competitive_advantage=(
        "Meta-episode differentiates Acquired — transparency on methodology builds audience trust vs opaque punditry.\n\nAggregation Theory alignment with Stratechery cross-pollinates audiences.\n\nWeaknesses: predictions age; non-tech societal forecasts dilute brand focus.\n\nUnique in podcast landscape 2017 — few shows quantified own theme frequency."
    ),
    key_insights=[
        {
            "view": "2016 was Aggregation Theory year.",
            "question": "Dominant lens?",
            "answer": "Six episodes — superior UX in zero-marginal-distribution markets. Thompson 2015 post kept gaining relevance through case studies.",
        },
        {
            "view": "Execution trinity supports aggregation.",
            "question": "Operational themes?",
            "answer": "Start small, growth culture, network effects — three 4× mentions. Combined produce customer experience aggregation rewards.",
        },
        {
            "view": "Data moats beat algorithm moats.",
            "question": "2017 ML call?",
            "answer": "Cloud APIs commoditize models — Google/Facebook data advantages persist. Startups need domain datasets not better nets.",
        },
        {
            "view": "Public markets need IPO courage.",
            "question": "Snap prediction?",
            "answer": "Hope Snap breaks stay-private trend — American public participates in growth; Facebook mobile fix post-IPO cited.",
        },
        {
            "view": "Winner-take-all has societal cost.",
            "question": "Automation outlook?",
            "answer": "Aggregation + self-driving threatens millions of jobs before UBI exists — policy valley hosts acknowledge without solutions.",
        },
    ],
    top_investment_implications=[
        {
            "ticker": "GOOGL",
            "direction": "Watch",
            "confidence": "Low",
            "thesis": "ML platformization thesis — cloud AI APIs commoditize models while data-rich incumbents retain edge; monitor GCP AI revenue mix.",
        }
    ],
    golden_quotes=[
        '"You get what you pay for here — no guarantee we\'ll be right." — David on predictions disclaimer.',
        '"Aggregation Theory is going to continue to be critically important in 2017." — David forecast opening.',
        '"Technology is a lever that magnifies consequences — good or evil." — 2016 Facebook IPO callback.',
    ],
    chronology={
        "subject": "Acquired 2016-2017 Meta Episode",
        "events": [
            {"date": "2015", "event": "Aggregation Theory published (Stratechery)"},
            {"date": "2016", "event": "Acquired first full season analyzed"},
            {"date": "2016", "event": "Themes tallied: Aggregation 6×, network effects 4×"},
            {"date": "2016-12-30", "event": "Episode recorded"},
            {"date": "2017-01", "event": "Episode 29 published with 2017 predictions"},
            {"date": "2017-03", "event": "Snap IPO at $17/share validates forecast"},
            {"date": "2017", "event": "ML APIs commoditize via cloud providers"},
            {"date": "2017-06", "event": "Amazon Whole Foods acquisition headlines"},
            {"date": "2017-12", "event": "Episode 51 grades predictions retrospectively"},
            {"date": "2018", "event": "UBI/automation debates intensify post-predictions"},
        ],
    },
)

_add(
    "acq-special-conversation-with-microsofts-head-of-strategic-investments-brian-schultz",
    keywords=["Microsoft M&A", "Strategic Investments", "Corporate VC"],
    conclusion=(
        "Episode 27 (~78 min, Dec 2016): Brian Schultz — Microsoft Managing Director Head of Strategic Investments, ex-corp dev (1999+), Ontela co-founder (acquired by Photobucket). Distinct from Microsoft Ventures (early-stage): Schultz does later-stage strategic bets (Facebook $15B valuation 2007 — 'world thought crazy'). Philosophy: investments create partnerships not LP-style returns; Wall Street doesn't grade MSFT on VC skill. Covers 2016 M&A surge, PE entering software (LBO on cash-flowing SaaS), Skype overseas cash repatriation, Foursquare/Cortana integration. Adobe Taylor Barada episode companion."
    ),
    background=(
        "Special conversation format — not single-deal teardown. Brian's founder empathy (Ontela with Dan Shapiro/Glowforge) informs corp dev. LinkedIn acquisition referenced as largest 2016 deal.\n\nStartup relationship building: business unit first, not cold call week-before-close."
    ),
    important_facts=[
        "Microsoft's 2007 Facebook investment at approximately $15 billion valuation widely viewed as overpriced — delivered substantial return.",
        "Brian Schultz co-founded Ontela (Seattle startup) acquired by Photobucket — returned to Microsoft corp dev/strategic investments.",
        "Microsoft Strategic Investments focuses later-stage partnership stakes vs Microsoft Ventures early-stage VC relaunch.",
        "2016 saw accelerated tech M&A including Microsoft's LinkedIn acquisition — largest deal referenced in episode.",
        "Private equity began active software LBOs circa 2016 as SaaS companies showed durable cash flows per episode discussion.",
    ],
    mental_model={
        "name": "Strategic Bet Not VC Fund",
        "components": "Corporate strategic investments optimize partnership/integration upside — Wall Street ignores good VC returns, punishes bad ones. Separate pools from M&A corp dev but relationships overlap. Founder-turned-corp-dev applies customer empathy — startups engage business units first, build multi-year trust.",
        "application": "Startups seeking Microsoft (or similar) should cultivate business-unit relationships years before exit conversations — strategic investment may precede acquisition. LPs shouldn't expect corporate VC to maximize IRR like traditional funds.",
    },
    competitive_advantage=(
        "Microsoft strategic investing leverages distribution (Enterprise, Azure, Office) for portfolio companies — Foursquare data in Cortana cited.\n\nSchultz founder credibility lowers startup suspicion vs pure corp dev.\n\nWeaknesses: conflict when portfolio competes with other partners; Amy Hood scrutiny on bad bets; org complexity (Ventures vs Strategic Investments).\n\nVersus Adobe (Taylor Barada prior guest): similar corp dev relationship-first thesis — industry pattern for successful acquirers.\n\nFacebook 2007 bet validates patience — strategic alignment + financial return rare combo."
    ),
    key_insights=[
        {
            "view": "Corporate VC ≠ financial VC.",
            "question": "Why invest if not for IRR?",
            "answer": "Schultz: create strategic partnerships — Facebook integration (Bing maps, Windows Phone) mattered more than headline return; shareholders don't reward MSFT as fund manager.",
        },
        {
            "view": "Founder empathy changes corp dev.",
            "question": "Ontela experience?",
            "answer": "Brian co-founded Ontela/Photobucket path — understands startup fundraising and acquisition from founder side vs banker-only corp dev peers.",
        },
        {
            "view": "PE entered software circa 2016.",
            "question": "Why LBOs in tech?",
            "answer": "SaaS predictable cash flows support debt — opposite of strategic integration thesis; PE rolls up vs Microsoft partnership model.",
        },
        {
            "view": "Relationships precede transactions.",
            "question": "Startup advice?",
            "answer": "Engage business units years early — don't cold-call corp dev expecting week-close. Milestones coincide with cash-out moments organically.",
        },
        {
            "view": "Overseas cash shaped Skype.",
            "question": "Tax repatriation?",
            "answer": "Skype deal used offshore cash avoiding repatriation tax — M&A as balance-sheet tool; 2016 tax reform anticipation discussed.",
        },
    ],
    top_investment_implications=[
        {
            "ticker": "MSFT",
            "direction": "Watch",
            "confidence": "Medium",
            "thesis": "Strategic investment and M&A cadence signal platform priorities — track Azure-linked portfolio bets as leading indicator of integration roadmap.",
        }
    ],
    golden_quotes=[
        '"Wall Street isn\'t evaluating Microsoft share price on how good you are as an investor." — Brian Schultz on strategic vs financial VC.',
        '"The Series B round was your IPO." — Brian on late-stage private markets (2016).',
        '"Create an exit for the company versus just put more money in — very different." — strategic vs passive investment.',
    ],
    chronology={
        "subject": "Microsoft Strategic Investments",
        "events": [
            {"date": "1999", "event": "Brian Schultz joins Microsoft corp dev"},
            {"date": "2000s", "event": "Ontela founded; acquired by Photobucket"},
            {"date": "2007", "event": "Microsoft invests in Facebook at ~$15B valuation"},
            {"date": "2011", "event": "Skype acquired using offshore cash considerations"},
            {"date": "2016", "event": "LinkedIn acquisition; PE software LBO wave noted"},
            {"date": "2016-12", "event": "Acquired Episode 27 conversation airs"},
            {"date": "2017", "event": "Microsoft Ventures relaunch for early-stage deals"},
            {"date": "2018", "event": "GitHub acquisition extends developer platform strategy"},
            {"date": "2019", "event": "LinkedIn integration deepens enterprise graph"},
            {"date": "2020", "event": "Strategic bets on cloud and AI partnerships accelerate"},
        ],
    },
)
