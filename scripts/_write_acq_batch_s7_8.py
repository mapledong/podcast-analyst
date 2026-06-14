#!/usr/bin/env python3
"""Write and validate 8 Acquired v5.1 approved JSON files (Season 7 batch)."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))

from scripts._write_acq_batch_491_500_common import base  # noqa: E402

APPROVED = ROOT / "data" / "approved"
PY = sys.executable

EPISODES: dict[str, dict] = {}

EPISODES["acq-special-superhuman-part-ii-designing-software-to-feel-like-a-game-with-rahul-vohra"] = base(
    "acq-special-superhuman-part-ii-designing-software-to-feel-like-a-game-with-rahul-vohra",
    review_notes="Manual GPT Acquired batch v5.1 — Season 7 specials",
    episode_rating={"overall": 4},
    keywords=["Game Design", "Product Flow", "Intrinsic Motivation"],
    conclusion=(
        "Rahul Vohra returns to Acquired to argue that the best productivity software borrows from game design — "
        "not through badges and points, but through flow, mastery curves, and intrinsic motivation. Drawing on his "
        "RuneScape MMO days and Superhuman's inbox-zero experience, he rejects gamification as disrespectful to "
        "users while embracing Bushnell's Law (easy to learn, hard to master), Csikszentmihalyi's flow states, and "
        "carefully engineered emotional payoffs like the inbox-zero city flyover. The framework: amplify natural "
        "delight rather than bolt on extrinsic rewards. For founders, the lesson is that sustainable engagement "
        "comes from respecting user intelligence and designing for the feeling of accomplishment users already seek."
    ),
    background=(
        "A year after Superhuman's breakout Acquired episode on product-market fit, Rahul Vohra returns for a "
        "design deep dive on why Superhuman feels like a game without gamification. Ben and David open with "
        "definitions of games (Bushnell's Law, flow, play vs. work) and Rahul's RuneScape pedigree — one of the "
        "first browser-based MMOs, built on Java applets before free-to-play was mainstream.\n\n"
        "The conversation covers Superhuman's technical choices (Electron, merged local/server search like Outlook), "
        "typography obsession, and deliberate rejection of points-and-badges systems that studies show undermine "
        "intrinsic motivation. Rahul explains the inbox-zero flyover image — a nuanced emotional reward for clearing "
        "an inbox — and how studying user emotions sharpened his personal emotional vocabulary. The LP segment "
        "teases a fundraising masterclass covering YC, exits, self-funding, and Rahul's angel fund with Todd Goldberg."
    ),
    important_facts=[
        "Rahul Vohra was a game designer at RuneScape — an early browser-based MMO using Java applets, predating mainstream free-to-play and heavy client downloads.",
        "Superhuman's prior Acquired episode (June 2019, Season 5 finale) became one of the show's most-listened episodes; Rahul is cited as the gold-standard prepared guest.",
        "Bushnell's Law (Nolan Bushnell, Atari): a good game is easy to learn but difficult to master — Rahul applies this to email client onboarding and power-user shortcuts.",
        "Superhuman uses Electron for its native app and merges local plus server search in a single fast query — a key concept for former Outlook users accustomed to separate search buttons.",
        "Rahul deliberately avoids extrinsic reward systems (points, badges) in Superhuman, citing research that external motivators reduce intrinsic drive for inbox management.",
    ],
    mental_model={
        "name": "Intrinsic Amplification Over Extrinsic Gamification",
        "components": (
            "Great software games feel like mastery journeys, not slot machines. Bushnell's Law sets the difficulty "
            "curve: trivial onboarding, deep mastery ceiling. Flow requires losing track of time through well-matched "
            "challenge. Extrinsic badges treat users like elementary students and decay motivation once rewards stop. "
            "Instead, identify moments of natural accomplishment (inbox zero) and amplify with light-touch emotional "
            "design — typography, speed, merged search, flyover imagery — without patronizing users."
        ),
        "application": (
            "Product teams should audit whether engagement mechanics respect user intelligence. If users already want "
            "to complete a task (clear inbox, close tickets, ship code), design for flow and emotional payoff rather "
            "than points. Rahul's RuneScape experience shows early browser constraints forced creative acquisition via "
            "WeChat-like distribution thinking — applicable to any product seeking habit without manipulation."
        ),
    },
    competitive_advantage=(
        "Superhuman's moat is feel, not features. Speed (merged local/server search), keyboard-first UX, and "
        "typography craft create a flow state competitors cannot copy with a checklist. Rahul's game-design background "
        "at RuneScape — rewriting Java to push browser limits — informs engineering tradeoffs (Electron) that prioritize "
        "experience over purity.\n\n"
        "Rejecting gamification is itself differentiation: power users resent patronizing badges. The inbox-zero "
        "flyover converts a mundane task into a moment of control and tranquility — intrinsic reward engineering. "
        "Rahul's celebrity as a prepared guest and PMF-framework author compounds distribution via word-of-mouth among "
        "founders.\n\n"
        "Weaknesses: $30/month pricing limits TAM; email is a shrinking category versus Slack/async tools; Electron "
        "performance ceiling; and copying keyboard shortcuts is easier than copying emotional design. The LP fundraising "
        "segment reinforces Rahul's credibility across YC, exits, and angel investing — extending the Superhuman brand "
        "beyond the product itself."
    ),
    key_insights=[
        {
            "view": "Gamification is low-respect design.",
            "question": "Why avoid points and badges in email?",
            "answer": "Rahul cites studies showing extrinsic rewards undermine intrinsic motivation. Users clearing inboxes already have internal drive; badges feel patronizing — 'treating them like elementary school kids' per David. Sustainable engagement amplifies natural accomplishment rather than manufacturing artificial milestones.",
        },
        {
            "view": "Games are mastery systems, not reward loops.",
            "question": "What makes software 'feel like a game'?",
            "answer": "Bushnell's Law: easy to learn, hard to master. Flow states where hours disappear. Rahul spent 10,000 hours programming games; Superhuman applies the same challenge calibration to email — trivial to start, deep shortcuts and search craft for power users. Not every playful activity is a game; guitar practice can be flow without being a game.",
        },
        {
            "view": "Emotional design requires emotional literacy.",
            "question": "Does studying user emotions change the designer?",
            "answer": "Rahul reports greater personal emotional vocabulary from designing nuanced payoffs like the inbox-zero flyover — power, control, tranquility in a split second. Studying emotion for product design translates to better human interactions outside software.",
        },
        {
            "view": "RuneScape was a distribution innovation lab.",
            "question": "How did MMO experience inform Superhuman?",
            "answer": "RuneScape ran as a browser Java applet before free-to-play norms — forcing creative engineering and acquisition thinking. Rahul rewrote large Java sections to push bleeding-edge browser performance, paralleling Superhuman's Electron bet to deliver native-feel speed despite cross-platform constraints.",
        },
        {
            "view": "Amplify delight; don't manufacture it.",
            "question": "What should founders copy from Rahul's framework?",
            "answer": "Find where your product naturally delights or delivers accomplishment, then add light-touch amplification — faster feedback, better typography, emotional imagery. Inbox zero already motivates; the flyover image heightens the moment. Avoid bolting unrelated game mechanics onto workflows users already want to complete.",
        },
    ],
    top_investment_implications=[
        {
            "ticker": "MSFT",
            "direction": "Watch",
            "confidence": "Low",
            "thesis": "Microsoft owns Outlook — the incumbent Superhuman displaces among power users. Rahul's merged-search and flow-state design raises the UX bar for enterprise email clients.",
        },
    ],
    golden_quotes=[
        "\"A good game is easy to learn, but difficult to master\" — Rahul citing Nolan Bushnell's Bushnell's Law as Superhuman's design north star.",
        "\"Gamification feels like a low respect for your users\" — David on why points-and-badges systems patronize intelligent professionals.",
        "\"When I hit inbox zero, I feel power, control, and tranquility\" — Ben describing the emotional payoff of Superhuman's flyover reward without connecting it consciously to the city imagery.",
    ],
    chronology={
        "subject": "Rahul Vohra / Superhuman",
        "events": [
            {"date": "Early 2000s", "event": "Rahul works as game designer at RuneScape browser MMO"},
            {"date": "2000s", "event": "Rahul founds Rapportive (Gmail social graph plugin)"},
            {"date": "2014", "event": "Rahul founds Superhuman email client"},
            {"date": "Jun 2019", "event": "Rahul first Acquired appearance — PMF frameworks episode (Season 5 finale)"},
            {"date": "2019", "event": "Superhuman PMF survey methodology becomes industry reference"},
            {"date": "2020", "event": "Superhuman Part II — game-design special episode recorded"},
            {"date": "2020", "event": "Rahul launches angel fund with Todd Goldberg via AngelList"},
            {"date": "Ongoing", "event": "Superhuman ships inbox-zero flyover and merged search in production"},
            {"date": "Ongoing", "event": "Rahul cited as Acquired's gold-standard prepared guest"},
            {"date": "2020", "event": "LP segment: Rahul fundraising masterclass recorded"},
        ],
    },
)

EPISODES["acq-twitter-with-dick-costolo"] = base(
    "acq-twitter-with-dick-costolo",
    review_notes="Manual GPT Acquired batch v5.1 — Season 7 specials",
    episode_rating={"overall": 4},
    keywords=["Promoted Tweets", "Platform vs Ads", "Mobile Pivot"],
    conclusion=(
        "Dick Costolo walks Ben and David through the fork where Twitter could have owned mobile social — pioneering "
        "promoted tweets before Facebook's feed ads, acquiring Loren Brichter's Tweetie (Atebits) for the native app, "
        "and nearly buying Instagram for ~$500M before Facebook paid $1B. Instead, Twitter chose an advertising "
        "business over a platform/API strategy, generating $100M+ in 2011 ad revenue (3x the next year) but capping "
        "at ~$3.5B versus Facebook's $70B+. The alternate universe: Twitter owns Instagram and Vine, becoming TikTok's "
        "parent. Costolo's candid history — FeedBurner to Google, the $500M–$1B Facebook offer (worth ~$27B in FB "
        "stock today), hardcoded Russian-president office visits, and IPO at $26 — frames Twitter as a product that "
        "reached ~330M MAU but never matched Facebook's ceiling because asymmetric follows expose less targeting data "
        "and the core UX remained hard to use."
    ),
    background=(
        "Season 7 Episode 5 reframes Twitter through Dick Costolo — CEO from 2010, first revenue dollar, IPO architect "
        "— rather than rehashing founder musical-chairs. The episode opens in Web 2.0: Costolo's SpyOnIt RSS predecessor, "
        "FeedBurner ad insertion (acquired by Google alongside Ev Williams' Blogger), and the race to 1M followers.\n\n"
        "Costolo joins as COO in 2009, becomes CEO in 2010, and builds Twitter's ad engine with Adam Bain — promoted "
        "tweets based on engagement, self-serve targeting portals, and Google/Microsoft data deals ($100M 2010 revenue "
        "mostly from partnerships). Product moves include acquiring Atebits/Tweetie, launching Twitter Cards, buying "
        "Vine and Periscope, and negotiating Instagram (~$500M, 10% of Twitter) before Facebook intervened. Post-IPO "
        "hype ($26 price, whisper numbers at $40 on CNBC) crashed within six months. Costolo reflects on ~330M MAU "
        "plateau, mDAU growth, content moderation, and the 2020 election context."
    ),
    important_facts=[
        "Facebook offered $500M–$1B for Twitter circa 2008–2009 when Twitter was growing faster than Facebook; $500M in Facebook stock then would be worth ~$27B today.",
        "Twitter pioneered promoted tweets (engagement-based feed ads) before Facebook's mobile ad format; 2010 revenue was mostly Google and Microsoft data deals, then 2011 exceeded $100M in ads and 3x'd the following year.",
        "Twitter negotiated to acquire Instagram for roughly $500M (10% of Twitter); at IPO the next year, 10% of Twitter would have exceeded Facebook's Instagram purchase price.",
        "Twitter IPO priced at $26/share (Oct 2013); stock nearly doubled in six weeks on 'next Facebook' narrative before crashing back toward IPO price within six months.",
        "When Costolo left, Twitter had ~300M users; MAU peaked near ~330M while mDAU and monetization continued climbing; Twitter generates ~$3.5B annual revenue versus Facebook's ~$70B.",
    ],
    mental_model={
        "name": "Platform vs. Advertising Fork",
        "components": (
            "Consumer tech companies face a binary strategic fork: become the rails (API/platform, WeChat-like) or "
            "become the ad seller (Facebook/Google duopoly). Twitter's third-party ecosystem (TweetDeck, clients) "
            "generated engagement but the ad unit required first-party tweet consumption. Closing the platform to "
            "capture promoted-tweet revenue traded ecosystem optionality for a smaller ad TAM. Network effects favor "
            "the player who reaches escape velocity first — Instagram/TikTok winners were not outrun once Facebook "
            "or ByteDance poured capital in."
        ),
        "application": (
            "When evaluating social products, ask whether value accrues to the platform owner or third-party clients. "
            "Twitter Cards powered Instagram's early growth — then Twitter disabled rich previews in rivalry. Costolo's "
            "lesson: the most common third-party app is a better client of your own product, not a Windows-scale platform. "
            "For investors, asymmetric-follow graphs expose less friend-graph data than Facebook, constraining ad targeting "
            "and ceiling even with strong cultural relevance."
        ),
    },
    competitive_advantage=(
        "Twitter's moat is real-time public conversation — unmatched for news, politics, and cultural moments. Dick "
        "Costolo built the monetization layer: promoted tweets, self-serve ads, and enterprise data licensing. First-mover "
        "in mobile feed ads (pre-Facebook mobile competence) and acquisitions (Tweetie native app, Vine, Periscope) gave "
        "product advantages that were squandered in platform wars.\n\n"
        "Asymmetric follows create a unique graph (interest-based, not friend-based) — perfect fit for Instagram's "
        "model, which Twitter nearly owned. Bidirectional follow visibility is unique among major social networks but "
        "yields less targeting data than Facebook's private friend graph.\n\n"
        "Weaknesses: persistent UX difficulty limiting MAU growth (~330M cap); Instagram preview disabling; losing "
        "TikTok-scale opportunities (Vine, Musical.ly) to better-capitalized rivals; and moderation polarization "
        "risk. Post-Costolo mDAU focus improved monetization without solving ceiling. Content moderation leadership "
        "versus Facebook creates differentiation but not revenue parity.\n\n"
        "Historical leverage: Russian president office visit (hardcoded into product), Adam Bain's sales execution, "
        "and recruiting ad talent from Google at premium comp built a real business — just not a Facebook-scale one."
    ),
    key_insights=[
        {
            "view": "Twitter pioneered the feed ad unit Facebook would dominate.",
            "question": "How did promoted tweets precede Facebook mobile ads?",
            "answer": "Circa 2010, Facebook was 'garbage on mobile' with display-style Microsoft deals. Costolo/Ashish built engagement-based promoted tweets — requiring heavy engineering, advertiser education, and third-party data plumbing. 2011 exceeded $100M ad revenue, 3x in 2012. Facebook later copied and scaled with a richer friend graph.",
        },
        {
            "view": "The Instagram acquisition was the butterfly effect.",
            "question": "What if Twitter bought Instagram for ~$500M?",
            "answer": "Twitter had ~140M MAU; Instagram fit the asymmetric-follow model perfectly. Facebook paid $1B instead. Costolo notes 10% of Twitter at IPO would have exceeded that price. Alternate universe: Twitter owns Instagram and effectively TikTok via Vine/Musical.ly lineage — becoming the dominant mobile social company.",
        },
        {
            "view": "Platform openness and ad monetization conflict.",
            "question": "Why kill third-party clients?",
            "answer": "If tweets are the ad unit, consumption must happen where Twitter controls ads. RSS failed partly because publishers couldn't control first-party engagement. Costolo chose advertising over a WeChat-like platform — rational given Facebook/Google duopoly size, but capped Twitter at ~$3.5B vs. $70B+.",
        },
        {
            "view": "Escape velocity beats product parity.",
            "question": "Why couldn't Twitter outrun Instagram or TikTok?",
            "answer": "Once network effects compound (Netflix content spend, Facebook user base, ByteDance ad blitz on TikTok), catching up requires disproportionate capital. Meerkat/Periscope and Vine demonstrated Silicon Valley darlings get crushed within weeks when a better-funded rival ships.",
        },
        {
            "view": "MAU plateau does not mean business failure.",
            "question": "Why is Twitter 'only' 330M users?",
            "answer": "Product difficulty and niche appeal (news/politics vs. universal friend graph) limit MAU. Costolo notes ~$3.5B revenue and 300M+ users is extraordinary; mDAU growth shows improved monetization. Acquired listeners are a valuable demographic — but Twitter's graph exposes less targeting data than Facebook.",
        },
    ],
    top_investment_implications=[
        {
            "ticker": "TWTR",
            "direction": "Watch",
            "confidence": "Medium",
            "thesis": "Costolo-era foundation built promoted-tweet monetization and mDAU metrics; cultural relevance in news/politics sustains ad pricing even as MAU growth stalled near 330M.",
        },
    ],
    golden_quotes=[
        "\"If it were $500 million in Facebook stock back then, that would be $27 billion today\" — David on the foregone Facebook acquisition offer for Twitter.",
        "\"On any given Sunday\" — Ben reframing that once a consumer service hits escape velocity, competitors cannot match the same playing field.",
        "\"Twitter is the only social platform that exposes bidirectional follows\" — Ben on Twitter's unique graph visibility and its limits for ad targeting versus Facebook.",
    ],
    chronology={
        "subject": "Twitter (Dick Costolo era)",
        "events": [
            {"date": "Early 1990s", "event": "Costolo at Andersen Consulting; pivots to stand-up comedy at Second City"},
            {"date": "2004", "event": "Costolo founds FeedBurner (RSS ad insertion)"},
            {"date": "2007", "event": "Google acquires FeedBurner; Costolo joins Google"},
            {"date": "2008", "event": "Facebook offers $500M–$1B for Twitter; offer declined"},
            {"date": "2009", "event": "Costolo joins Twitter as COO"},
            {"date": "2010", "event": "Costolo becomes CEO; promoted tweets and Google/Microsoft data deals launch"},
            {"date": "2011", "event": "Twitter exceeds $100M ad revenue; 3x growth the following year"},
            {"date": "2012", "event": "Instagram acquisition talks fail; Facebook buys Instagram for $1B"},
            {"date": "2013", "event": "Twitter IPO at $26/share"},
            {"date": "2015", "event": "Costolo steps down as CEO; Twitter ~300M users"},
            {"date": "2020", "event": "Episode recorded week before US presidential election"},
        ],
    },
)

EPISODES["acq-special-invest-like-the-best-on-acquired"] = base(
    "acq-special-invest-like-the-best-on-acquired",
    review_notes="Manual GPT Acquired batch v5.1 — Season 7 specials",
    episode_rating={"overall": 4},
    keywords=["Quant Investing", "Media Flywheel", "OSAM"],
    conclusion=(
        "Patrick O'Shaughnessy traces three generations of O'Shaughnessy Capital/OSAM — his father's quantitative "
        "Graham-and-Dodd screening, the 2008 crisis pivot, and today's Canvas platform licensing plus Invest Like "
        "the Best media empire. The core thesis: asset management is becoming a media business and media is becoming "
        "an asset management distribution channel. OSAM deviates from vanilla long-only fees by productizing research "
        "via Canvas (debating whether to license to competitors), launching an early-stage fund alongside public "
        "quant strategies, and spinning up Infinite Powers — a narrative-driven podcast on business plot arcs. Patrick's "
        "power comes from brand: high quality, low variance, over time — the same persistence drivers as top-tier "
        "venture firms."
    ),
    background=(
        "Patrick O'Shaughnessy — CEO of O'Shaughnessy Asset Management and host of Invest Like the Best — joins for "
        "a crossover special. David opens with O'Shaughnessy Capital Management, founded by Patrick's father on "
        "academic quantitative value screening married to media evangelism (the first Invest Like the Best iteration).\n\n"
        "Patrick narrates graduating into the 2008 crisis (Bear Stearns/JPMorgan moment), OSAM's evolution beyond "
        "long-only fee models, the Canvas platform (vertical vs. horizontal licensing tension with competitors), and "
        "how the podcast became a research flywheel — surfacing scale-advantage businesses like Spotify and Netflix. "
        "He manages concurrent initiatives: codifying business knowledge, early-stage investing, Infinite Powers "
        "podcast, and running OSAM. The episode grades acquisitions, discusses Taylor Pearson/Austin Rief's 'investing "
        "is media' thesis, and contrasts Western startup narrative scarcity with China's plot-driven tech discourse."
    ),
    important_facts=[
        "O'Shaughnessy Capital Management pioneered marrying quantitative Graham-and-Dodd screening with media evangelism — Invest Like the Best is the second iteration of that brand.",
        "Patrick graduated in 2007 alongside the 2008 financial crisis; Bear Stearns/JPMorgan $2/share moment framed his entry into markets.",
        "SoftBank Vision Fund exemplifies blunt billion-dollar venture deployment that raised prices across private markets over the last decade.",
        "OSAM's Canvas platform sparked vertical-vs-horizontal debate: whether to license research tools to competing asset managers.",
        "Patrick's brand power framework mirrors venture persistence: high quality, low variance, over time — the same traits that sustain top VC franchises.",
    ],
    mental_model={
        "name": "Media-Research Flywheel",
        "components": (
            "Public investing and venture increasingly reward distribution plus insight compounding. Podcasts surface "
            "scale-advantage research (Spotify podcasting, Netflix content amortization) that feeds back into allocation "
            "decisions. Long-only fee compression pushes managers toward performance components (VC/PE model) while "
            "private markets absorbed billions that distorted venture pricing. Brand equals high quality + low variance "
            "+ time — durable edge when performance alone commoditizes."
        ),
        "application": (
            "Founders and investors should treat content as research infrastructure, not marketing garnish. Patrick runs "
            "public quant, early-stage, and narrative podcasting concurrently because each feeds deal flow and LP trust. "
            "Before launching a fund, ask whether your media audience amortizes diligence costs the way OSAM's does."
        ),
    },
    competitive_advantage=(
        "OSAM's edge stacks multi-generational quant heritage, media distribution, and platform productization. "
        "Patrick's father built data-driven value investing before 'quant' was fashionable; Patrick added crisis-tested "
        "resilience and Canvas as a licensable research OS. Invest Like the Best provides LP-grade diligence access "
        "that traditional asset managers cannot replicate without conflicting with their salesforce.\n\n"
        "The early-stage fund and Infinite Powers podcast extend the brand into venture and narrative analysis — "
        "capturing China's 'plot-driven' tech discourse advantage for Western audiences. Canvas licensing decision "
        "(competitors vs. exclusivity) is the classic platform vertical-horizontal tension.\n\n"
        "Weaknesses: concurrent CEO/podcaster/VC roles risk focus dilution; quant strategies face capacity constraints; "
        "media flywheel depends on Patrick's personal brand; and performance fees remain harder to earn in public markets "
        "than private. SAC-like competitors building Canvas equivalents would be threatening — but hedge funds monetize "
        "performance, not research licenses.\n\n"
        "Grades on acquisitions and Patrick's kindest-memory close reinforce human capital as the enduring moat."
    ),
    key_insights=[
        {
            "view": "Investing and media are converging businesses.",
            "question": "Why is ILTB the second iteration of OSAM's insight?",
            "answer": "Patrick's father evangelized quant value research through media before podcasts existed. Today's managers face fee compression in long-only public equity while VC/PE absorbed billions with performance fees. ILTB amortizes research across a large audience — the Taylor Pearson/Morning Brew thesis that asset management is becoming media.",
        },
        {
            "view": "Brand power equals quality times consistency times duration.",
            "question": "Where does OSAM derive power?",
            "answer": "High quality, low variance, over time — mirroring venture persistence at Sequoia/a16z. Performance alone commoditizes; brand lets OSAM launch Canvas, early-stage funds, and Infinite Powers without cold-starting trust each time.",
        },
        {
            "view": "Canvas is a platform strategy decision, not a feature.",
            "question": "License to competitors or keep proprietary?",
            "answer": "Vertical integration preserves alpha but caps TAM; horizontal licensing scales research tooling like AWS but risks arming rivals. Patrick debated this explicitly — the answer shapes whether OSAM is a fund or a fintech platform.",
        },
        {
            "view": "Narrative literacy is an investing edge.",
            "question": "Why launch Infinite Powers podcast?",
            "answer": "China tech discourse centers plot arcs ('where does this end?'); Western investing often lacks narrative framing. Infinite Powers applies story-structure analysis to business — extending ILTB's research flywheel into long-horizon strategic forecasting.",
        },
        {
            "view": "SoftBank proved blunt capital distorts venture.",
            "question": "What changed in private markets over 10 years?",
            "answer": "Billions flooded venture with performance-fee psychology, raising prices and making $1B checks hard to deploy efficiently. Patrick contrasts OSAM's disciplined quant heritage with Vision Fund-style deployment that became an Acquired running joke for 2.5 years.",
        },
    ],
    top_investment_implications=[
        {
            "ticker": "SPOT",
            "direction": "Watch",
            "confidence": "Low",
            "thesis": "Patrick cites Spotify podcasting as scale-advantage amortization — ILTB research flywheel repeatedly surfaces platform businesses where audience size lowers per-unit content cost.",
        },
    ],
    golden_quotes=[
        "\"High quality, low variance, and time\" — Patrick's brand-power framework, paralleling venture capital persistence.",
        "\"The investing business is becoming the media business\" — David citing Taylor Pearson and Austin Rief's exchange on VC/media convergence.",
        "\"Learning to ask the right questions and listen to the answers\" — Ben citing Don Valentine on the core VC skill Patrick exercises across OSAM initiatives.",
    ],
    chronology={
        "subject": "O'Shaughnessy Asset Management",
        "events": [
            {"date": "1990s", "event": "Patrick's father founds O'Shaughnessy Capital Management on quant value screens"},
            {"date": "2007", "event": "Patrick graduates into pre-crisis markets"},
            {"date": "2008", "event": "Financial crisis; Bear Stearns/JPMorgan moment reshapes OSAM path"},
            {"date": "2010s", "event": "First Invest Like the Best media iteration evolves into podcast"},
            {"date": "2010s", "event": "OSAM develops Canvas research platform"},
            {"date": "2010s", "event": "SoftBank Vision Fund era raises private-market prices globally"},
            {"date": "2020", "event": "Patrick launches Infinite Powers narrative podcast"},
            {"date": "2020", "event": "OSAM early-stage investment fund operates alongside public strategies"},
            {"date": "2020", "event": "Acquired crossover special recorded"},
            {"date": "Ongoing", "event": "Invest Like the Best remains top-tier business podcast"},
        ],
    },
)

EPISODES["acq-special-acquired-x-my-first-million"] = base(
    "acq-special-acquired-x-my-first-million",
    review_notes="Manual GPT Acquired batch v5.1 — Season 7 specials",
    episode_rating={"overall": 3},
    keywords=["Bebo Revival", "SPACs", "Indie Entrepreneurship"],
    conclusion=(
        "Acquired crosses over with My First Million's Shaan Puri for a dual-format episode: Bebo's $1M distressed "
        "acquisition (Amazon/Twitch owning 70%) and a freewheeling startup-ideas session covering SPACs, opportunity "
        "zones for crypto wealth, WiFi quality scores for Airbnbs, and reinsurance for California fire risk. Shaan — "
        "former Bebo CEO, Blab founder, Twitch special-projects — embodies the '80% thick middle' of venture-backed "
        "entrepreneurs who don't become SpaceX. Ben contrasts PSL's moonshot studio model with Shaan's capital-efficient "
        "$1M/year lifestyle businesses. The meta-lesson: Acquired covers canonical giants; My First Million celebrates "
        "the million paths that never IPO — and both lenses are necessary."
    ),
    background=(
        "Shaan Puri joins Ben and David for an Acquired × My First Million crossover (Shaan only, not Sam Parr). Part "
        "one covers Bebo: Shaan bought the once-massive social network for ~$1M from Amazon/Twitch (70% owner), "
        "inheriting historical user data and attempting a revival — the quintessential distressed-consumer-internet "
        "turnaround.\n\n"
        "Part two (recorded first) is a startup-ideas riff: Ben's bifurcated lens (PSL venture moonshots vs. "
        "capital-efficient indie businesses), SPAC research tools (spacresearch.com), Dow Jones index licensing as "
        "billion-dollar no-cost revenue, Shopify-insurance float analogies, and opportunity-zone tax strategies for "
        "crypto millionaires. David teases a season-finale insurance episode. The tone is lighter than standard Acquired "
        "company histories — intentional counterpart to canonical deep dives."
    ),
    important_facts=[
        "Shaan Puri acquired Bebo for approximately $1M; Amazon/Twitch owned 70% of the company at sale.",
        "Shaan was CEO of Bebo, founder of Blab.im, and works on special projects at Twitch.",
        "Ben co-founded Pioneer Square Labs — 24 venture-backed spinouts in 5 years from a Seattle startup studio.",
        "Dow Jones index licensing was cited as a ~$1B top-line, near-zero-cost business within News Corp/Dow Jones.",
        "spacresearch.com is a paywalled SPAC research business built by an Acquired community member.",
    ],
    mental_model={
        "name": "Two Lenses on Entrepreneurship",
        "components": (
            "Venture narratives overweight winner-take-all moonshots (PSL's 24 spinouts, SpaceX canon). My First "
            "Million celebrates capital-efficient $1M/year businesses achievable by 'lots and lots of people.' "
            "Distressed asset plays (Bebo for $1M) exploit incumbents abandoning legacy social graphs. SPACs, index "
            "licensing, and insurance float represent rent-extraction businesses orthogonal to VC hype cycles."
        ),
        "application": (
            "Match ambition to outcome function: moonshots need unique timing plus team; lifestyle businesses need "
            "customer obsession and capital efficiency. Shaan's Bebo buy illustrates buying optionality cheap when "
            "strategics write off consumer assets. Founders should study both Acquired canonical histories and MFM "
            "indie patterns before defaulting to venture scale."
        ),
    },
    competitive_advantage=(
        "The crossover itself is the asset: Acquired's canonical depth plus My First Million's indie operator credibility. "
        "Shaan brings distressed-deal pattern recognition (Bebo, Blab) that complements Ben/David's big-company histories. "
        "Bebo's revival attempt leverages nostalgic brand equity and cheap acquisition cost — classic deep-value consumer "
        "internet optionality even if Amazon/Twitch retained majority economics.\n\n"
        "Idea-session segments surface non-obvious rent streams: SPAC databases, Airbnb WiFi scoring, fire-risk "
        "reinsurance, crypto opportunity zones. These are MFM's competitive lane — practical schemes vs. Acquired's "
        "institutional histories.\n\n"
        "Weaknesses: lighter analytical depth than standard Acquired episodes; Bebo revival faces insurmountable network-effect "
        "deficits; crossover format dilutes narrative focus; and idea riffs lack the verification rigor of transcript-based "
        "company histories. Insurance/SPAC teases are promissory, not delivered analysis."
    ),
    key_insights=[
        {
            "view": "Most founders live in the venture 'thick middle.'",
            "question": "Why does Shaan represent the 80%?",
            "answer": "David notes most venture-backed entrepreneurs don't become SpaceX — they navigate pivots, distressed acquisitions, and mid outcomes. Shaan's Bebo $1M buy and Blab history exemplify the path Acquired usually skips.",
        },
        {
            "view": "Acquired and MFM are complementary, not competing.",
            "question": "Why crossover?",
            "answer": "Acquired tells canonical internet history (big flashy companies); MFM celebrates million ways to build without IPOing. Golden Hippo and similar episodes prove indie businesses deserve study alongside Google and Nike.",
        },
        {
            "view": "Distressed consumer assets can be optionality plays.",
            "question": "What did Shaan buy with Bebo?",
            "answer": "~$1M bought the brand, data from every epoch, and revival optionality while Amazon/Twitch kept 70%. Classic deep-value bet when strategics abandon legacy social products.",
        },
        {
            "view": "SPACs created a research-business wedge.",
            "question": "Where is the indie opportunity in SPAC boom?",
            "answer": "spacresearch.com built a paywalled SPAC database — an Acquired community member monetizing information asymmetry. Pattern: new financial mechanisms spawn data/research rent streams before incumbents adapt.",
        },
        {
            "view": "Insurance float is the ultimate capital allocator hack.",
            "question": "Why tease an insurance finale?",
            "answer": "David previews a season-finale insurance company episode — free float invested by great allocators (Berkshire model). Shopify-insurance analogy shows tech platforms coveting float for non-insurance R&D spend.",
        },
    ],
    top_investment_implications=[
        {
            "ticker": "AMZN",
            "direction": "Watch",
            "confidence": "Low",
            "thesis": "Amazon/Twitch retained 70% of Bebo — illustrating how big tech holds distressed consumer assets; Shaan's $1M buy shows spin-out pricing when strategics abandon legacy social graphs.",
        },
    ],
    golden_quotes=[
        "\"There are a million ways to skin the cat\" — David on why My First Million complements Acquired's canonical company histories.",
        "\"Going and achieving a million dollar a year top-line business — lots and lots of people can do that\" — Ben on capital-efficient entrepreneurship versus moonshot narratives.",
        "\"Insurance is the best business ever. You get free money\" — David teasing the season-finale insurance episode on float economics.",
    ],
    chronology={
        "subject": "Bebo / Acquired × MFM Crossover",
        "events": [
            {"date": "2005", "event": "Bebo launches as major social network"},
            {"date": "2008", "event": "Bebo peaks as consumer social destination"},
            {"date": "2010s", "event": "Bebo declines; ownership passes through AOL and others"},
            {"date": "2010s", "event": "Amazon/Twitch acquire majority (70%) stake in Bebo"},
            {"date": "2010s", "event": "Shaan Puri founds Blab.im live-streaming"},
            {"date": "~2020", "event": "Shaan buys Bebo for ~$1M distressed acquisition"},
            {"date": "2020", "event": "Shaan works on special projects at Twitch"},
            {"date": "2020", "event": "Acquired × My First Million crossover recorded"},
            {"date": "2020", "event": "spacresearch.com SPAC database cited as community-built business"},
            {"date": "2020", "event": "LP segment teased with Shaan as 'deal doula'"},
        ],
    },
)

EPISODES["acq-eventbrite"] = base(
    "acq-eventbrite",
    review_notes="Manual GPT Acquired batch v5.1 — Season 7 specials",
    episode_rating={"overall": 4},
    keywords=["Direct Listing", "Bootstrapping", "Events Platform"],
    conclusion=(
        "Kevin and Julia Hartz tell Eventbrite's founding story — PayPal Mafia meets MTV/Jackass producer, love-at-first-sight "
        "at a Santa Barbara wedding, and a counter-offer that beat Current TV to start a ticketing company. They bootstrapped "
        "two years with no salaries before Sequoia, exploiting the 'shadow market' of check-at-the-door micro-events VCs "
        "couldn't size. Eventbrite pioneered the direct listing (September 2018, Bill Gurley-endorsed) to escape IPO "
        "pop inefficiency. COVID crushed ~$80M/quarter net revenue overnight, but the Hartzes argue public markets and "
        "enterprise sales discipline position Eventbrite to take share from Ticketmaster when live events return."
    ),
    background=(
        "Season 7 Episode 2 features founders Kevin Hartz (PayPal Mafia, Xoom) and Julia Hartz (MTV, Jackass) telling "
        "a uniquely personal origin: meeting at a wedding, Kevin's term-sheet counter-offer versus Julia's Current TV "
        "job, and building Eventbrite on the PayPal API insight that ticketing was left on eBay's cutting-room floor.\n\n"
        "They bootstrapped with Renaud for two years — organic adoption in NYC, shadow-market TAM invisible to VCs — "
        "before raising and eventually direct-listing. Julia led the roadshow as a rare woman founder-CEO. August 2020 "
        "recording covers COVID's revenue cliff (primarily self-serve in-person events), enterprise vs. self-serve "
        "sales channels, and parallels to Tock's restaurant pivot. Playbook pulled forward: offline TAM underestimation."
    ),
    important_facts=[
        "Kevin Hartz was a pre-launch investor in PayPal (Peter Thiel network) and sold Xoom; Julia Hartz helped put MTV's Jackass on air.",
        "Eventbrite bootstrapped ~2 years with no salaries — organic NYC adoption before raising; VCs underestimated TAM because micro-events used offline check-at-door payments.",
        "Eventbrite direct-listed September 17–18, 2018 — among first high-profile direct listings endorsed by Bill Gurley as anti-IPO-pop mechanism.",
        "Pre-COVID Eventbrite ran ~$80M/quarter net revenue; Q2 2020 dropped precipitously as in-person gatherings canceled.",
        "Roughly half of Eventbrite revenue came from self-organized mid-sized self-serve events versus enterprise festival deals.",
    ],
    mental_model={
        "name": "Shadow Market TAM",
        "components": (
            "Large markets hide in offline, fragmented behavior until software makes them visible. Micro-event organizers "
            "collected checks at doors — invisible to VC spreadsheets — while Ticketmaster owned arenas. Bootstrapping "
            "proved organic demand before capital could underwrite the category. Direct listings align long-term founders "
            "with public shareholders without IPO pop wealth transfer to bankers and flippers."
        ),
        "application": (
            "When VCs say 'small market,' check whether measurement misses offline shadow volume. Eventbrite, Uber, and "
            "Lyft all opened floodgates in the same era by digitizing fragmented supply. Founders choosing direct listings "
            "should expect to train banker salesforces and endure heuristic roadshow bias — especially underrepresented CEOs."
        ),
    },
    competitive_advantage=(
        "Eventbrite owns the long tail of self-serve event creation — weddings, meetups, classes — where Ticketmaster "
        "doesn't compete. PayPal API DNA gave payments infrastructure fluency; Julia's MTV production background brought "
        "creator-economy intuition before the term existed. Bootstrapping forced capital efficiency and product-market fit "
        "proof before dilution.\n\n"
        "Direct listing positioned Eventbrite as Gurley-style capital-structure innovator — selling shareholders' stock "
        "directly without pop-and-drop dynamics. Enterprise sales channel (multi-thousand-person festivals, custom refund "
        "deals) complements self-serve PLG motion Acquired uses for meetups.\n\n"
        "Weaknesses: COVID exposed in-person revenue concentration; public-market short-termism feared by founders "
        "became real; enterprise deals are 'unique special children' with complex cash-flow dynamics; and Ticketmaster/Live "
        "Nation retain arena monopoly. Julia's roadshow faced male-CEO heuristics. Kevin's Outsiders-style capital allocation "
        "ethos helps but cannot speed event-industry recovery.\n\n"
        "COVID pivot parallels Tock (Nick Jonas LP episode): zero revenue moment forces serving customers better and "
        "capturing incumbent share on reopening."
    ),
    key_insights=[
        {
            "view": "The biggest TAM was invisible because it was offline.",
            "question": "Why did VCs pass on Eventbrite early?",
            "answer": "Micro-event entrepreneurs collected checks at doors — shadow market absent from VC models. Julia notes perception lagged even after escape velocity. Playbook pulled forward: offline fragmentation hides category size until software makes transactions measurable.",
        },
        {
            "view": "Direct listing is a capital-allocation choice.",
            "question": "Why skip a traditional IPO?",
            "answer": "Bill Gurley endorsed direct listing as anti-pop mechanism — reducing banker/flipping wealth transfer. September 2018 Eventbrite listing trained salesforces to advocate for the company rather than price-discovery theater.",
        },
        {
            "view": "Founder couples compound resilience.",
            "question": "How did Kevin and Julia start together?",
            "answer": "Met at Santa Barbara wedding; Kevin counter-offered Julia's Current TV (Al Gore co-founded) job with a startup term sheet. Love-at-first-sight story intertwined with financing negotiation — shared risk before engagement.",
        },
        {
            "view": "Public markets cut both ways in crisis.",
            "question": "Did being public hurt COVID response?",
            "answer": "Hartzes debate whether public status constrained or accelerated COVID pivots. ~$80M/quarter revenue cliff tested enterprise vs. self-serve mix. Public discipline on sales org may help capture Ticketmaster share on reopening.",
        },
        {
            "view": "Enterprise and self-serve are different animals.",
            "question": "What is the sales-channel split?",
            "answer": "Self-serve: Ben and David meetups. Enterprise: multi-thousand-person festivals with assigned headcount, custom refund policies, and complex cash-flow — each deal a 'unique special child' versus standardized self-serve tooling.",
        },
    ],
    top_investment_implications=[
        {
            "ticker": "EB",
            "direction": "Watch",
            "confidence": "Medium",
            "thesis": "COVID zeroed in-person revenue but Eventbrite's self-serve dominance and public-market sales discipline may capture long-tail share from offline incumbents when live events normalize.",
        },
    ],
    golden_quotes=[
        "\"People were collecting checks at the door for everything below the arena-sized venue\" — on the shadow market Eventbrite digitized.",
        "\"Public markets are so short-term focused\" — pre-IPO founder fear Eventbrite tested during COVID.",
        "\"You should be betting on yourself instead of accepting little money from a job\" — Kevin's counter-offer that launched Eventbrite over Current TV.",
    ],
    chronology={
        "subject": "Eventbrite",
        "events": [
            {"date": "1990s", "event": "Kevin at Stanford; Julia grows up Bay Area"},
            {"date": "1998", "event": "Kevin pre-launch invests in PayPal"},
            {"date": "2000s", "event": "Julia at MTV; puts Jackass on air"},
            {"date": "2000s", "event": "Kevin sells Xoom; PayPal API ticketing insight emerges"},
            {"date": "~2005", "event": "Kevin and Julia meet at Santa Barbara wedding"},
            {"date": "2006", "event": "Eventbrite founded; bootstrapping begins"},
            {"date": "2008", "event": "~2 years bootstrap complete; fundraising starts"},
            {"date": "Sep 2018", "event": "Eventbrite direct listing on NYSE"},
            {"date": "Mar 2020", "event": "COVID cancels in-person events globally"},
            {"date": "Aug 2020", "event": "Acquired interview recorded during pandemic"},
        ],
    },
)

EPISODES["acq-pinduoduo"] = base(
    "acq-pinduoduo",
    review_notes="Manual GPT Acquired batch v5.1 — Season 7 specials",
    episode_rating={"overall": 5},
    keywords=["Group Buying", "WeChat Distribution", "China Ecommerce"],
    conclusion=(
        "Pinduoduo is Colin Huang's social-commerce insurgent — 'Costco meets Disneyland' per its IPO prospectus, "
        "but more accurately ByteDance-meets-Alibaba: browse-centric group buying on WeChat with a 0.6% take rate "
        "and 90% of revenue from merchant advertising prepays. Founded 2015, merged Pinhaohuo (fruit) and PDD "
        "marketplace, IPO'd June 2018 under three years later with Colin retaining 46.8% ($13.8B stake). Tencent "
        "king-made PDD in February 2017 with $110M Series B plus Mini Program access — 233M users primarily on WeChat. "
        "Share grew from 4% to 14% of China ecommerce (mostly from Alibaba's 73%→62%). Gap losses mask $2B+ operating "
        "cash flow from merchant deposits, team-buy float, and ad prepayments. The bear case: 23x revenue, counterfeiting, "
        "and Tencent dependency. The bull case: 630M buyers, tier-4 rural penetration, and manufacturer disintermediation."
    ),
    background=(
        "Season 7 Episode 1 traces Colin Huang from Google (2004, pre-IPO hire) through mentor Duan Yongping's "
        "$600K Buffett lunch, Ouku/LEQI ecommerce, and fruit startup Pinhaohuo — launched on WeChat without an app, "
        "selling RMB 5 fruit bundles. Merged with PDD marketplace at 0.6% take rate versus Alibaba/JD's 10–30%.\n\n"
        "Growth hacks: team-buy buttons 40% cheaper than solo buy, gamified orchards, browse-not-search (Zulily/QVC "
        "parallel), and manufacturer direct supply. Tencent's February 2017 investment unlocked Mini Programs — 233M "
        "WeChat-primary users. IPO raised $1.6B (40% day-one pop); Colin briefly passed Jack Ma as China's third-richest. "
        "Hosts dissect gap-vs-cash-flow divergence, advertising leg of the stool, and what-if Facebook had allowed "
        "commerce on its graph."
    ),
    important_facts=[
        "Pinduoduo launched 2015; IPO June 2018 less than 3 years later; Colin Huang retained 46.8% at IPO — stake worth $13.8B, 12th-richest in China.",
        "Take rate ~0.6% versus Alibaba/JD marketplace fees of 10–30%; ~90% of revenue from merchant advertising prepays, not transaction fees.",
        "Tencent led $110M Series B (Feb 2017) and granted Mini Program access — 233M users primarily via WeChat Mini Program; 144M on native apps; 630M total buyers.",
        "China ecommerce share: PDD grew 4%→14% of transaction volume since IPO while Alibaba fell 73%→62%; crossed $100B market cap before retreating below.",
        "Despite gap net losses, PDD generated $2B+ operating cash flow (2020) from merchant deposits, team-buy payment float (24hr hold), and ad prepayments.",
    ],
    mental_model={
        "name": "Social Distribution Plus Negative Cash Cycle",
        "components": (
            "Pinduoduo combines WeChat social graph distribution (team-buy requires friends), browse-centric "
            "entertainment merchandising (not Amazon search intent), and a negative cash conversion cycle: merchant "
            "deposits, team-buy prepayments held up to 24 hours, and advertising prepays fund growth while gap income "
            "shows losses. Ultra-low take rate attracts supply; ad bidding (Google/Facebook model) captures merchant "
            "margin. Manufacturer disintermediation cuts retailer markup."
        ),
        "application": (
            "When evaluating high-growth marketplaces, read cash flow statements, not just income statements. PDD's "
            "float resembles Berkshire's insurance float or Groupon's working-capital dynamics — but with positive "
            "operating cash flow at scale. For US investors, ask which platform owns social distribution (Tencent "
            "vs. Facebook's ads-only choice) before copying the model."
        ),
    },
    competitive_advantage=(
        "Pinduoduo's moat is Tencent-backed social distribution plus browse-native merchandising for price-sensitive "
        "tier-3/4 consumers. Team-buy mechanics require WeChat sharing — competitors cannot replicate without equal "
        "graph access. 0.6% take rate undercuts Alibaba/JD while ad platform monetizes merchant margin. "
        "Manufacturer-direct supply (excess factory capacity, preselling demand) disintermediates retailers and brands.\n\n"
        "Browse-not-search allows longer shipping (Zulily insight) and entertainment-value feeds — 'Oprah demographic' "
        "parallel. Mini Program primacy (233M WeChat-primary users) beats Alibaba/JD/Vipshop's app-centric traffic.\n\n"
        "Weaknesses: Tencent dependency (Facebook shut fab.com-style social commerce pre-IPO); counterfeiting and "
        "coupon fraud; $6 average order value limits revenue per transaction; Colin stepped down as CEO July 2020; "
        "23x revenue multiple; and tier-1/2 upgrade competition. Restricted cash is fungible but growth-dependent — "
        "if growth stops, float reverses.\n\n"
        "Cash-flow brilliance: merchant deposits, team-buy holds, and ad prepays generated $1B+ operating cash flow "
        "for 3+ years despite gap losses — the income statement tells a different story than the treasury."
    ),
    key_insights=[
        {
            "view": "Gap losses and cash riches can coexist.",
            "question": "How is PDD 'unprofitable' yet cash-positive?",
            "answer": "Merchant deposits, 24-hour team-buy payment float, and ad prepayments create restricted cash pools — like Berkshire insurance float. 2020 operating cash flow exceeded $2B while gap net losses grew. Revenue is vanity; cash conversion is sanity.",
        },
        {
            "view": "Tencent king-making beats SoftBank spray-and-pray.",
            "question": "Why did Tencent pick PDD over competitors?",
            "answer": "February 2017: $110M Series B plus Mini Program for a category strategic to WeChat payments and social commerce. PDD got 233M WeChat-primary users — exponentially more than Alibaba/JD in WeChat ecosystem. Tencent backs PDD, Meituan, DiDi — compounding stakes from billion to hundred-billion.",
        },
        {
            "view": "Browse beats search for low-AOV entertainment commerce.",
            "question": "Why not Amazon-style search?",
            "answer": "Tier-3/4 users shop deals for entertainment, not intent. Browse feeds allow slower/cheaper shipping (Zulily parallel). Platform can direct 'Eye of Sauron' traffic favorably to suppliers — good when favored, less reliable than direct audience relationship.",
        },
        {
            "view": "0.6% take rate is a Trojan horse for ads.",
            "question": "How does PDD make money?",
            "answer": "Transaction fees are ~10% of revenue; ~90% is merchant ad prepays for sponsored feed placement (Google/Overture model). Amazon took 23 years to build meaningful ad revenue; PDD built leg two early. Alibaba pioneered this in China; Amazon accelerated after observing China.",
        },
        {
            "view": "Facebook's commerce closure ceded the US market.",
            "question": "What if Facebook had allowed social commerce?",
            "answer": "Facebook disabled open-graph commerce pre-IPO (fab.com died). Chose $70B ads business — correct for US. Tencent let thousand flowers bloom on WeChat, investing in PDD/Meituan/DiDi winners. Counterfactual: US social commerce might exist at scale with different platform economics.",
        },
    ],
    top_investment_implications=[
        {
            "ticker": "PDD",
            "direction": "Watch",
            "confidence": "Medium",
            "thesis": "Cash-flow-positive marketplace gaining China ecommerce share (14% vs. 4% at IPO) with Tencent distribution moat; valuation sensitive to 23x revenue and counterfeiting remediation.",
        },
        {
            "ticker": "BABA",
            "direction": "Watch",
            "confidence": "Medium",
            "thesis": "Alibaba lost ~11 points of China ecommerce share primarily to Pinduoduo's tier-3/4 social model — forcing defensive ad and rural investments.",
        },
    ],
    golden_quotes=[
        "\"An exemplification of a multi-dimensional space, seamlessly integrating cyberspace and the physical space\" — Pinduoduo IPO prospectus quoted by Ben.",
        "\"Colin Huang said Pinduoduo is Toutiao meets ecommerce\" — David reframing the Costco/Disneyland prospectus analogy toward ByteDance.",
        "\"Revenue is an effect and profit is an opinion\" — Ben on why gap accounting misleads on PDD's cash-flow engine.",
    ],
    chronology={
        "subject": "Pinduoduo",
        "events": [
            {"date": "2004", "event": "Colin Huang joins Google pre-IPO as engineer/PM"},
            {"date": "2010s", "event": "Colin starts Ouku, LEQI; mentors with Duan Yongping"},
            {"date": "2015", "event": "Pinhaohuo fruit sales launch on WeChat (no app)"},
            {"date": "2015", "event": "PDD marketplace launches at 0.6% take rate"},
            {"date": "2016", "event": "Merger of Pinhaohuo and PDD; $70M revenue first year"},
            {"date": "Feb 2017", "event": "Tencent $110M Series B plus Mini Program access"},
            {"date": "2017", "event": "Revenue 3x to $270M; marketplace-only model"},
            {"date": "Jun 2018", "event": "IPO raises $1.6B; stock pops 40% day one"},
            {"date": "Jul 2020", "event": "Colin Huang steps down as CEO; remains chairman"},
            {"date": "2020", "event": "Crosses $100B market cap; 630M buyers"},
        ],
    },
)

EPISODES["acq-epic-games"] = base(
    "acq-epic-games",
    review_notes="Manual GPT Acquired batch v5.1 — Season 7 specials",
    episode_rating={"overall": 5},
    keywords=["Unreal Engine", "App Store War", "Fortnite"],
    conclusion=(
        "Epic Games is Tim Sweeney's 30-year crusade against software rent-seekers — from ZZT shareware (keeping 100% "
        "vs. retail's 10–15%) through Unreal Engine licensing, Tencent's 40% stake ($330M, 2012), and Fortnite "
        "Battle Royale's 10M players in two weeks (September 2017). Epic's 2018 metrics: $5.6B revenue, $3B profit "
        "at $15B Tencent valuation (5x EBITDA). The Epic Games Store undercuts Steam's 30% with 12% (engine royalty "
        "included). August 2020: Epic provoked Apple/Google by enabling direct V-Bucks payments, got Fortnite delisted, "
        "and released a 1984-parody video calling Tim Cook the villain. Tim's vision: lower take rates, cross-platform "
        "metaverse infrastructure — Fortnite as hangout (Travis Scott 14M attendees), Unreal for Hollywood. Powers: "
        "switching costs on Unreal (~$1.5B engine revenue), network effects in cross-platform play."
    ),
    background=(
        "Season 7 Episode 3 traces Tim Sweeney from Apple II programming (10,000 hours) through ZZT shareware, "
        "Jazz Jackrabbit, Unreal (1998), and Gears of War's 88% margin ($100M revenue, $12M cost). Tencent bought 40% "
        "for $330M in 2012; Tim refocused on Unreal-as-AWS-for-games, free engine with 5% royalty, and online services.\n\n"
        "PUBG inspired Fortnite Battle Royale (Sept 2017): 10M players in 2 weeks, 125M+ before mobile. Epic Games "
        "Store launched December 2018 at 12% take vs. Steam's 30%. 2020 Apple/Google war: direct payment bypass, "
        "Fortnite removed, Unreal Engine ban threatened, antitrust alignment with Basecamp/Hey controversy. Fortnite, "
        "engine, and store form three pillars toward Tim's open metaverse — not just games anymore."
    ),
    important_facts=[
        "Tim Sweeney founded Epic (originally Epic MegaGames) on shareware model — keeping 100% vs. ~10–15% through retail publishers taking ~50%.",
        "Tencent acquired 40% of Epic for $330M in 2012 (~$1B valuation); 2018 follow-on valued Epic at $15B on $5.6B revenue and $3B profit (5x EBITDA).",
        "Fortnite Battle Royale launched September 2017; 10M active players within 2 weeks; 350M registered players cited; Marshmello concert drew 14M attendees.",
        "Epic Games Store charges 12% take rate (includes Unreal Engine 5% royalty) versus Steam/Apple/Google 30%; Valve cut to 25% in response.",
        "Unreal Engine estimated ~$1.5B annual revenue (5% royalty on ~$30B customer revenue); Fortnite estimated $1–2B; Epic Games Store losing money on exclusives/marketing.",
    ],
    mental_model={
        "name": "Cost-Plus Platform Rebellion",
        "components": (
            "Tim Sweeney repeatedly chooses direct distribution over rent extraction: shareware over retail (100% vs. "
            "10%), free Unreal with 5% royalty over internal engine builds, 12% store take vs. 30% App Store/Steam. "
            "Fortnite cash funds offense against platform tolls. Cross-platform network effects make iOS isolation "
            "existential — without playing with friends on console/PC, Fortnite's value collapses. Engine switching costs "
            "lock in developers while store and payments complete the stack."
        ),
        "application": (
            "When platform owners extract 30%, insurgents with hit products and vertical integration (engine + store + "
            "payments + live ops) can weaponize user outrage. Epic's Apple lawsuit is a negotiating chip backed by "
            "$1.5B+ engine revenue and cultural Fortnite scale. Investors in platform-dependent apps should model "
            "take-rate risk as Tim Sweeney's life mission, not a one-off dispute."
        ),
    },
    competitive_advantage=(
        "Epic stacks engine switching costs, Fortnite network effects, and ideological credibility in the platform "
        "wars. Unreal Engine (~$1.5B revenue, 5% royalty) locks in PUBG-scale developers — switching to Unity is "
        "painful for complex 3D cross-platform titles. Gears of War proved 88% margins; Fortnite proved live-service "
        "scale with cross-platform play as the moat.\n\n"
        "Epic Games Store at 12% (engine included) positions cost-plus pricing against Steam's rent. Epic Online "
        "Services aspires to be AWS/Stripe for games — Fortnite as first-and-best customer. Creator mode and concerts "
        "(Marshmello 14M) cross the Rubicon from game to metaverse hangout.\n\n"
        "Weaknesses: Tencent 40% ownership; Epic Games Store burns cash on exclusives; Apple/Google delisting kneecaps "
        "iOS Fortnite; three failed internal game projects before BR pivot; Tim's idealism may sacrifice near-term "
        "revenue. Unreal ban threat endangers all iOS/Mac Unreal developers — mutually assured destruction.\n\n"
        "2020 antitrust moment: Hey/Basecamp controversy cracked developer sentiment; Epic's 1984 parody video and "
        "refusal to comply escalated to developer-account ban — customers lose in tech-giant clashes."
    ),
    key_insights=[
        {
            "view": "Shareware was the original App Store rebellion.",
            "question": "Why does Tim hate 30% take rates?",
            "answer": "1990s retail took 50%; publishers left Tim 10–15%. Shareware kept 100%. Apple now argues the same 50% retail cut Tim fought. Epic Games Store at 12% is cost-plus (5–7% to run, ~5% margin) — philosophical continuity over 30 years.",
        },
        {
            "view": "Fortnite was a pivot, not a plan.",
            "question": "How did Battle Royale emerge?",
            "answer": "Fortnite started 2011; six years in development. PUBG hit March 2017; Unreal Tournament team copied codebase into Fortnite BR within 2 months. September 2017 launch: 10M players in 2 weeks. Tim treats Fortnite as windfall funding his engine/store vision.",
        },
        {
            "view": "Cross-platform is the network effect.",
            "question": "Why does iOS isolation matter?",
            "answer": "Fortnite value is playing with friends across console, PC, mobile. Apple-delisted Fortnite loses cross-play — kneecapping the product. Marshmello concert: 14M attendees in instances of ~50 friends. Without iOS, social graph fragments.",
        },
        {
            "view": "Unreal Engine is the quiet monopoly.",
            "question": "What powers Epic besides Fortnite?",
            "answer": "~$1.5B engine revenue from 5% royalties on ~$30B developer revenue. PUBG and AAA 3D titles cannot easily switch. Unity serves simpler mobile; Unreal owns complex cross-platform 3D. Switching costs are Epic's deepest moat.",
        },
        {
            "view": "The metaverse arrived as a game.",
            "question": "Is Fortnite still just a game?",
            "answer": "Observer mode, Creator mode, concerts, and chat-without-playing cross into hangout/social territory — Roblox/Rec Room parallels. Unreal Engine already films Mandalorian-style virtual production. Tim's open, lower-rent internet vision exceeds gaming.",
        },
    ],
    top_investment_implications=[
        {
            "ticker": "AAPL",
            "direction": "Watch",
            "confidence": "Medium",
            "thesis": "Epic's antitrust crusade and developer-account ban threat test App Store 30% policy; Unreal Engine dependency gives Epic leverage Apple cannot ignore without harming its own developer ecosystem.",
        },
        {
            "ticker": "0700.HK",
            "direction": "Watch",
            "confidence": "Medium",
            "thesis": "Tencent's 40% Epic stake and 2018 $15B valuation mark another multi-billion winner in Tencent's king-maker portfolio alongside Pinduoduo and Meituan.",
        },
    ],
    golden_quotes=[
        "\"When all was said and done, he would've only been making 10%, 15% of revenue\" — David on 1990s retail vs. shareware economics Tim Sweeney rejected.",
        "\"Epic is saying you get the engine, live ops, distribution, and payments for a maximum fee of 12%\" — on undercutting Steam and Apple by 18 points.",
        "\"When tech giants clash, customers lose\" — Ben on Apple delisting Fortnite and breaking cross-play for users.",
    ],
    chronology={
        "subject": "Epic Games",
        "events": [
            {"date": "1991", "event": "Tim Sweeney starts Epic MegaGames; ZZT shareware"},
            {"date": "1998", "event": "Unreal game and Unreal Engine launched"},
            {"date": "2006", "event": "Gears of War — $100M revenue, $12M cost, 88% margin"},
            {"date": "Sep 2010", "event": "Unreal Engine 3 demoed at Apple keynote for iOS"},
            {"date": "2012", "event": "Tencent buys 40% for $330M (~$1B valuation)"},
            {"date": "Mar 2015", "event": "Unreal Engine goes free; 5% royalty model"},
            {"date": "Mar 2017", "event": "PUBG popularizes battle royale genre"},
            {"date": "Sep 2017", "event": "Fortnite Battle Royale launches; 10M players in 2 weeks"},
            {"date": "Dec 2018", "event": "Epic Games Store launches at 12% take rate"},
            {"date": "2018", "event": "Epic does $5.6B revenue, $3B profit; valued at $15B"},
            {"date": "Aug 2020", "event": "Epic vs. Apple/Google antitrust confrontation; Fortnite delisted"},
        ],
    },
)

EPISODES["acq-the-nba"] = base(
    "acq-the-nba",
    review_notes="Manual GPT Acquired batch v5.1 — Season 7 specials",
    episode_rating={"overall": 5},
    keywords=["Player Empowerment", "Media Rights", "Global Growth"],
    conclusion=(
        "The NBA is a century-long business transformation — from $20M franchise sales to $1.5B+ valuations (Jordan's "
        "Hornets: bought at $175M in 2010, 20% sold at $1.5B in 2020) and an estimated 1 billion global viewers "
        "(2017–18 season). David Stern's 1984 ascension paired a salary cap at 53% of league revenue ($3.6M per team "
        "when average team revenue was $6.8M) with TV deals exploding from ~$20M/year (1983 ABC) to ~$220M (1989). "
        "The league leads American sports in technology (League Pass OTT, 2K esports league), youth demos (57% of "
        "13–17 favor NBA vs. 13% NFL), and player social reach (LeBron 119M followers). China (Yao 2002, 600M watchers) "
        "and Hong Kong (Morey tweet, ~$400M lost revenue) expose the tension between player empowerment and "
        "authoritarian-market access. Third in US revenue ($8.8B) behind NFL ($13B+) and MLB — but global upside unmatched."
    ),
    background=(
        "Season 7 Episode 4 traces basketball from James Naismith's 1891 Massachusetts winter through the BAA/NBL "
        "merger (1949), short-lived 1940s salary cap, Wilt/Russell ABC deals ($4M over 5 years in early 1960s), "
        "ABA merger (1976: incoming teams paid $3.2M entry; Spirits of St. Louis got perpetual 1/7 TV share — "
        "$150M+ paid through 2009), and Magic/Bird saving the league.\n\n"
        "Stern era: drug-policy cleanup, Jordan global brand ($1.5B personal Nike earnings; Jordan Brand $3B revenue), "
        "Dream Team 1992, Yao Ming China explosion (300M players, 600M watchers), and modern player empowerment via "
        "social media. COVID bubble leadership (March 11 shutdown marked US seriousness). Technology: NBA League Pass "
        "versus NFL GameDay's post-game-only streaming. Hong Kong crisis tests 'empower player voices' vs. China growth."
    ),
    important_facts=[
        "Forbes estimated 1 billion global NBA viewers in 2017–18 season; NBA is 3rd in US league revenue (~$8.8B) behind NFL (~$13–14B) and MLB.",
        "1983 salary cap: $3.6M per team = 53% of average team revenue ($6.8M); league total revenue ~$150M across 23 teams — Stern became commissioner February 1984.",
        "National TV revenue grew from ~$20M/year (1983 ABC) to ~$220M/year (1989); players captured ~$120M of incremental value.",
        "Among 13–17 year olds, 57% favor NBA vs. 13% NFL and 4% baseball; average NBA fan age 43 vs. baseball 59.",
        "LeBron James: 119M social followers (73M Instagram alone, more than Trump); NBA official accounts 80M; Daryl Morey Hong Kong tweet cost league an estimated $400M revenue.",
    ],
    mental_model={
        "name": "Player as Distribution Channel",
        "components": (
            "The NBA inverted the NFL's suppress-player-voice model: empower stars on social media (LeBron 119M, Curry "
            "45M) to acquire lifetime fans in the 13–17 demographic. Content is cheap when players create it; "
            "league amplifies (Black Lives Matter on courts). Global growth via Yao/China (600M watchers) and "
            "streaming OTT (League Pass) beats legacy TV lock-in (NFL GameDay streams only post-game). Salary cap "
            "as % of revenue aligns labor and league on growth."
        ),
        "application": (
            "Media businesses should compare participant empowerment vs. suppression strategies. NFL restricts player "
            "brands (Brady 9M vs. LeBron 119M); NBA monetizes decades of fan LTV from teen social follows. For "
            "international expansion, individual star bridges (Yao, Nowitzki, Giannis) beat exporting American football. "
            "China exposure creates irreconcilable values conflicts — budget $400M+ for geopolitical tail risk."
        ),
    },
    competitive_advantage=(
        "The NBA's moat is global youth appeal plus player-driven distribution. Stern codified salary cap as revenue "
        "share (53%, later CBA iterations), aligning stars and owners on growth. Jordan/Magic/Bird era created lifestyle "
        "basketball (Nike 86% performance market share, 96% lifestyle). International pipeline: 25%+ roster international, "
        "half of next-gen stars foreign-born; China alone 300M players.\n\n"
        "Technology leadership: League Pass OTT with ESPN-style content (not just games) versus NFL's consumer-hostile "
        "GameDay (live games only after completion). 2K League as fourth major brand alongside NBA, G League, WNBA. "
        "COVID Disney bubble executed safely while other leagues suffered outbreaks.\n\n"
        "Weaknesses: US revenue still trails NFL/MLB despite global attention; China/Hong Kong irreconcilable (Morey "
        "tweet, Silver's dual apologies); NFL still commands $6.8B national TV vs. NBA $2.66B; and star empowerment "
        "creates political tail risk. Average franchise $1.5B+ but dependent on continued player cooperation.\n\n"
        "Ownership shifted to tech/PE/VC (16 of 30 teams) — Jordan sold 20% of Hornets at $1.5B valuation (bought "
        "majority at $175M in 2010). Player empowerment + social + global + streaming position NBA to overtake "
        "domestic-only leagues within 5–10 years."
    ),
    key_insights=[
        {
            "view": "Empowering players is a customer-acquisition strategy.",
            "question": "Why let LeBron post freely?",
            "answer": "NFL suppresses voices (Brady 9M followers); NBA amplifies (LeBron 119M, more than Trump). Teen follows become lifetime fans monetized for decades. Black Lives Matter court branding targets 13–17 demographic where NBA has 57% favorite-sport share vs. NFL's 13%.",
        },
        {
            "view": "The NFL is winning today but losing tomorrow.",
            "question": "Why will NBA surpass NFL?",
            "answer": "NFL $13B+ revenue and $6.8B national TV dwarf NBA's $8.8B and $2.66B — but NFL GameDay streams only post-game; NBA League Pass offers live global OTT. Youth demos: 57% NBA vs. 13% NFL among 13–17. Football has minimal non-US appeal; basketball has 1B global viewers.",
        },
        {
            "view": "China is the NBA's greatest opportunity and existential risk.",
            "question": "What did the Morey tweet cost?",
            "answer": "Yao Ming (2002) made Rockets China's team — 300M players, 600M watchers. Morey's 'Fight for Freedom' tweet paused Tencent streams, canceled preseason games; Silver estimated $400M revenue loss. Player-voice empowerment and CCP market access are structurally incompatible.",
        },
        {
            "view": "Stern turned a breakeven startup into a media company.",
            "question": "What changed in 1983–1989?",
            "answer": "League revenue ~$150M (1983) with $3.6M salary cap per team. Stern became commissioner 1984; cleaned up drugs; marketed Jordan globally. TV deal jumped ~$20M to ~$220M by 1989. Players captured ~$120M incremental — cooperative capitalism between labor and league.",
        },
        {
            "view": "ABA merger created perpetual rent streams.",
            "question": "What was the Spirits of St. Louis deal?",
            "answer": "1976 ABA-NBA merger: incoming teams paid $3.2M entry; Nets paid Knicks $4.8M territorial indemnity. Spirits owners folded franchise for $2.2M upfront plus perpetual 1/7 share of four ABA teams' TV money — $150M+ collected through 2009. Legal arbitrage of league expansion.",
        },
    ],
    top_investment_implications=[
        {
            "ticker": "DIS",
            "direction": "Watch",
            "confidence": "Medium",
            "thesis": "ESPN/Disney national NBA rights and streaming pivot (ESPN+) align with NBA's OTT-first youth strategy — NBA may outgrow legacy NFL TV economics as Gen Z abandons appointment television.",
        },
        {
            "ticker": "NKE",
            "direction": "Long",
            "confidence": "Medium",
            "thesis": "Jordan Brand generates $3B+ annual revenue; Nike holds 86% performance and 96% lifestyle basketball market share — Jordan's $1.5B personal earnings 16 years post-retirement prove player-brand compounding.",
        },
    ],
    golden_quotes=[
        "\"Owning an NFL or NBA franchise is the closest thing we have to royalty in America\" — Ben on billionaire team ownership.",
        "\"You can only begin streaming NFL games after the games are over\" — David on the NFL's consumer-hostile GameDay versus NBA League Pass.",
        "\"The shutdown started because the NBA gave the United States public permission to say, okay, this is serious\" — Ben on March 11 COVID cancellation as societal leadership.",
    ],
    chronology={
        "subject": "National Basketball Association",
        "events": [
            {"date": "1891", "event": "James Naismith invents basketball in Massachusetts"},
            {"date": "1946", "event": "BAA founded; short-lived 1940s salary cap abandoned ~40 years"},
            {"date": "1949", "event": "BAA and NBL merge into NBA"},
            {"date": "1960s", "event": "Wilt/Russell era; ABC $4M five-year TV deal"},
            {"date": "1976", "event": "ABA merger; teams pay $3.2M entry; Spirits perpetual TV share"},
            {"date": "1983", "event": "Salary cap reinstated at 53% of revenue; Stern promoted 1984"},
            {"date": "1984", "event": "Jordan drafted; Nike deal seeds Jordan Brand"},
            {"date": "1992", "event": "Dream Team at Barcelona Olympics"},
            {"date": "2002", "event": "Yao Ming drafted; NBA explodes in China"},
            {"date": "2010", "event": "Jordan buys Hornets majority at $175M"},
            {"date": "Mar 2020", "event": "NBA cancels season; COVID bubble follows"},
            {"date": "2019", "event": "Morey Hong Kong tweet; ~$400M estimated revenue impact"},
        ],
    },
)

if __name__ == "__main__":
    ids = list(EPISODES.keys())
    for eid in ids:
        path = APPROVED / f"{eid}.json"
        path.write_text(json.dumps(EPISODES[eid], indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
        print(f"wrote {path.name}")
    print("\n--- validation ---")
    ok, fail = [], []
    for eid in ids:
        r = subprocess.run([PY, str(ROOT / "scripts" / "validate_one_acquired.py"), eid], capture_output=True, text=True)
        out = r.stdout.strip()
        if r.returncode == 0:
            ok.append(eid)
            print(f"PASS {eid}: {out.split(chr(10))[-1]}")
        else:
            fail.append((eid, out))
            print(f"FAIL {eid}:\n{out}")
    print(f"\ncompleted: {len(ok)}  failures: {len(fail)}")
    for eid, msg in fail:
        print(f"  {eid}")
