"""Part 2: a16z I/II and Ethereum."""
EPISODES_PART2 = {}

EPISODES_PART2["acq-andreessen-horowitz-part-i"] = {
    "keywords": ["Netscape", "Loudcloud", "Opsware"],
    "conclusion": "Part I traces Marc Andreessen and Ben Horowitz from opposite origins — Ben's Berkeley Black Panthers-adjacent childhood vs. Marc's rural Iowa $6.25/hour NCSA Mosaic — through Netscape's 16-month IPO ($3B market cap, 80% browser share), Microsoft IE bundling, and Loudcloud/Opsware survival. Netscape did $85M/$346M/$534M revenue 1995–97; Loudcloud sold infrastructure to EDS for $63.5M, pivoted Opsware (pimp-themed internal tool 'Jive'), sold to HP for $1.6B (~$14.25/share). Benchmark Series A drama ($6M Marc personal check) planted a16z seeds. Super-angel era: 36 deals in 3 years, ~$200K checks. IM exchange ending Part I: 'We ought to start a VC firm.'",
    "background": "Season 9 opens a16z two-parter. David discloses Kindergarten Ventures LPs include a16z GPs.\n\nBen Horowitz born London 1966 to radical activist father David Horowitz (Ramparts, Black Panthers); Marc from New Lisbon, Wisconsin (~2,554 people). Mosaic: 12 users Feb 1993 → 1M by early 1994 (~10% of internet). Netscape IPO Aug 1995 priced $28, opened $75, closed $58 (~$3B cap).",
    "important_facts": [
        "Marc Andreessen paid $6.25/hour at NCSA; Mosaic hit ~1M users by early 1994 from 12 in February 1993.",
        "Netscape IPO August 1995: priced $28/share, first trade $75, closed $58 — ~$3B market cap; 16 months from founding.",
        "Netscape revenue: $85M (1995), $346M (1996), $534M (1997) — enterprise server division led by Ben Horowitz.",
        "Loudcloud sold infrastructure business to EDS for $63.5M (~10¢ on dollar vs. prior raises); Opsware sold to HP 2007 for ~$1.6B.",
        "Marc/Ben angel portfolio pre-firm: 36 deals in ~3 years at ~$200K max check including Twitter, Facebook, LinkedIn, Zynga.",
    ],
    "mental_model": {
        "name": "Open the Closed Thing",
        "components": "Marc's repeated playbook: Mosaic opened academic internet to masses; Netscape free browser + paid server; Loudcloud/AWS-before-AWS (too early); a16z will open VC services to founders. Counter-positioning vs. closed guilds (NCSA bureaucracy, Microsoft's IE bundling, Benchmark 'professional CEO' dogma). Survive until market catches up — Opsware at $28M market cap with $63.5M cash + $20M EDS contract.",
        "application": "When incumbents gate specialized tools, mass-market wrapper plus distribution wins — but timing matters (Loudcloud CapEx killed before AWS demand). Founder-operator credibility beats finance-only VC if you productize services.",
    },
    "competitive_advantage": "Pre-a16z, Marc/Ben compound network from Netscape celebrity, Loudcloud/Opsware scar tissue, and super-angel density.\n\nMarc on Facebook board (2008) after advising Zuckerberg to reject $1B Yahoo offer — only voice against sale.\n\nBen's Opsware turnaround proves operating credibility Benchmark questioned.\n\nMichael Ovitz Loudcloud board seat → CAA-of-VC inspiration for a16z services model.\n\nWeaknesses: Marc poor operator instincts (Time barefoot cover, leaked strategy email); Loudcloud nearly bankrupt; Ning white-label social ahead of time.",
    "key_insights": [
        {"view": "Mosaic growth proved mass-market internet.", "question": "Why did academics resist Mosaic?", "answer": "Internet elite wanted research-only purity — Marc: 'only smart people should use internet.' Mosaic went 12→1,000→10,000→1M users in ~12 months on dial-up TAM. Al Gore's 1991 bill funded Marc's $6.25/hour salary."},
        {"view": "Free browser rewrote software economics.", "question": "Why wasn't Netscape sold in boxes?", "answer": "NCSA retained Mosaic IP; Netscape inverted model — free browser, paid servers (aggregation theory precursor). Microsoft licensed Spyglass/Mosaic for IE, paid only ~$8M total — bundling killed Netscape distribution."},
        {"view": "Benchmark feud seeded a16z positioning.", "question": "What happened at Loudcloud Series A?", "answer": "Marc's $6M personal check raised post-money; Benchmark partner Byrne attacked Ben's CEO fitness in front of team. Marc/Ben alienated from Benchmark except Andy Rachleff — explicit later counter-positioning vs. classic VC."},
        {"view": "Opsware proved Ben can salvage CapEx disasters.", "question": "How recover from Loudcloud?", "answer": "Sold servers for $63.5M; rebuilt provisioning software for EDS ($20M/year contract). Stock at $0.35 (~$28M cap) with $63.5M cash — five years later HP paid ~$1.6B. Doug Leone called Ben to learn turnaround mechanics."},
        {"view": "Super-angel density preceded firm formation.", "question": "Why start a16z in 2009?", "answer": "While Sequoia wrote RIP Good Times, Marc/Ben did ~36 angel deals — most active 'VCs' who weren't a firm. Zuckerberg quote: Marc only advisor saying don't sell to Yahoo. IM to Marc: 'We ought to start a VC firm.'"},
    ],
    "top_investment_implications": [
        {"ticker": "META", "direction": "Watch", "confidence": "Low", "thesis": "Marc Andreessen board tenure since 2008 began with anti-Yahoo-sale advice — illustrative of a16z founder-friendly governance thesis, not a current Marc pick."}
    ],
    "golden_quotes": [
        '"We ought to start a venture capital firm." / "I was thinking the same thing." — Ben Horowitz IM to Marc Andreessen, ~2008.',
        "\"When I got to the Valley in 1993/1994, I thought I had missed the whole thing.\" — Marc Andreessen on perpetual too-late feeling.",
        '"I guess we\'re not going to wait until the 5th to launch the strategy." — Ben email to Marc after premature strategy leak to press.',
    ],
    "chronology": {
        "subject": "Marc Andreessen & Ben Horowitz (Part I)",
        "events": [
            {"date": "1966", "event": "Ben Horowitz born London; Marc born rural Wisconsin 1971"},
            {"date": "1993", "event": "Mosaic launches — 12 users February, 1M by early 1994"},
            {"date": "1994", "event": "Netscape founded with Jim Clark; Mozilla codename"},
            {"date": "Aug 1995", "event": "Netscape IPO ~$3B market cap; Windows 95 six days later"},
            {"date": "1998", "event": "Mozilla open-sourced; AOL acquires Netscape"},
            {"date": "1999", "event": "Loudcloud founded — cloud before AWS"},
            {"date": "2002", "event": "Loudcloud sells infrastructure to EDS for $63.5M"},
            {"date": "2007", "event": "HP acquires Opsware for ~$1.6B"},
            {"date": "2007–09", "event": "Marc/Ben super-angel era — ~36 deals, ~$200K checks"},
            {"date": "2009", "event": "IM decision to start Andreessen Horowitz"},
        ],
    },
    "review_notes": "Manual GPT Acquired batch — v5.1-acquired; a16z Part I of II",
}

EPISODES_PART2["acq-andreessen-horowitz-part-ii"] = {
    "keywords": ["Andreessen Horowitz", "Venture Platform", "Silicon Valley VC"],
    "conclusion": "Part II covers a16z from July 2009 launch ($300M fund — large for first-time) through platform VC reinvention. 2.5% of $300M = ~$7.5M/year fees; Marc/Ben took no salary two years. First check Apptio; September 2009 $50M Skype stake (1.8% for $50M → ~$153M in ~18 months at ~$8.5B Microsoft sale). Okta Series A → ~18% at ~$6B IPO (~$33B later). Counter-positioned Benchmark: founder CEOs, no signaling doctrine (Instagram→Benchmark A after a16z seed PicPlz), services army (PR, recruiting, corp dev). a16z branding: alphabetized press lists, Charlie Rose launch, New Yorker 'Tomorrow's Advance Man.' Expanded to crypto, bio, growth; media company parallel.",
    "background": "Opens on 2009 IM — 'We have to start a VC firm.' David notes firm only ~11–12 years old at recording yet reshaped VC.\n\nOvitz inspiration for 'CAA of venture.' Paul Holland Foundation Capital quote on 60–70 investments. Kindergarten Ventures disclosure repeats.",
    "important_facts": [
        "Andreessen Horowitz Fund I: $300M (December 2009) — very large first-time fund; 2.5% management fee ≈ $7.5M/year; founders took no salary ~2 years.",
        "September 2009: $50M into Skype spinout for 1.8% alongside Silver Lake — returned ~$153M (~3×) when Microsoft bought Skype ~$8.5B (~18 months).",
        "Okta Series A lead → ~18–20% ownership; ~$6B IPO valuation (~$33B market cap later in episode context).",
        "Pre-firm angel track: 36 deals in 3 years, ~$200K max check — a16z later formalized seed program without board seats to reduce signaling fear.",
        "Skype investment = 16.7% of $300M fund in one company — violated classic ownership-percentage norms but returned quick DPI.",
    ],
    "mental_model": {
        "name": "Platform VC vs. Partnership VC",
        "components": "Benchmark: small partnership, equal carry, no platform — counter-positioned Kleiner. a16z counter-counter-positions: spend management fees on services so technical founders become 'professional CEOs' without replacement. Marketing as new VC discipline ('introduced marketing to VC'). Alphabetized 'Andreessen Horowitz' beats 'Benchmark' in press lists. Signaling risk overblown — Instagram raised Benchmark A after a16z chose PicPlz competitor.",
        "application": "When evaluating VC brands, ask if fees fund LP-aligned DPI or founder services that increase ownership value. a16z bet that multi-stage + media + regulatory lobbying beats pure partnership lean model at scale.",
    },
    "competitive_advantage": "a16z wins on founder selection of brand — Marc's Netscape mythos, Ben's Hard Things credibility, and visible services.\n\nSkype/Okta prove non-traditional checks (growth PE in Fund I, enterprise SaaS) can return fund-scale outcomes.\n\nWeaknesses: Instagram/PicPlz miss; Skype concentration; criticism on valuations and fund size arms race they started. Incumbents copied platform play.\n\nVersus Sequoia: a16z publicly counter-positioned Benchmark, rarely Sequoia ('come at the king, you best not miss').",
    "key_insights": [
        {"view": "Management fees should buy founder outcomes.", "question": "Why hire 60+ staff at a VC?", "answer": "Marc/Ben saw VCs telling founders to take $50K–60K salaries while partners earned millions in fees regardless of DPI. a16z redeployed ~$7.5M/year into recruiters, PR, regulatory — synthetic network for technical CEOs."},
        {"view": "Signaling effect hurts VCs more than founders.", "question": "Does seed without Series A follow-on kill companies?", "answer": "Instagram seeded as PicPlz competitor; a16z passed Instagram — Benchmark led Series A, Facebook acquired ~$1B. Signaling narrative overstates VC follow-on importance."},
        {"view": "Skype trade was DPI engineering.", "question": "Why $50M for 1.8%?", "answer": "Classic VC math says need 20% ownership — a16z bought ~1.8% of Skype for $50M (16.7% of fund) and returned ~$153M quickly. Proved firm could do growth PE, not only classic Series A."},
        {"view": "Brand is distribution.", "question": "Why 'Andreessen Horowitz' not 'a16z' officially?", "answer": "Alphabetical press ordering, Charlie Rose launch, New Yorker profile — Marc as 'Tomorrow's Advance Man.' a16z used in media; legal name retained on Sand Hill signage."},
        {"view": "Ovitz model for conflict-heavy industries.", "question": "Where did services idea originate?", "answer": "Michael Ovitz joined Loudcloud board after Disney — Hollywood agent packaging applied to startup CEO support. Punch competitors in mouth metaphor for competitive fundraising."},
    ],
    "top_investment_implications": [
        {"ticker": "OKTA", "direction": "Watch", "confidence": "Medium", "thesis": "Canonical a16z Fund I enterprise win — ~18% at IPO from Series A lead; verify identity-platform moat vs. Microsoft/Google bundling."},
        {"ticker": "WORK", "direction": "Watch", "confidence": "Low", "thesis": "Slack exemplified a16z seed-then-growth model (~$3B exit to Salesforce context in episode) — illustrative of messaging portfolio construction."},
    ],
    "golden_quotes": [
        '"Literally, we introduced a new concept to the field of VC, which was called marketing." — Ben Horowitz.',
        '"If I were one of those guys whose company stumbles… will they be there to help me?" — Paul Holland, Foundation Capital (2009 NYT), on a16z portfolio size.',
        '"We have to start a venture capital firm." — Marc Andreessen IM reply to Ben, 2009.',
    ],
    "chronology": {
        "subject": "Andreessen Horowitz",
        "events": [
            {"date": "2009", "event": "Marc/Ben IM — decide to start VC firm"},
            {"date": "Jul 2009", "event": "Firm planning; Ovitz/CAA playbook influences services model"},
            {"date": "Dec 2009", "event": "$300M Fund I closes; NYT launch profile"},
            {"date": "Sep 2009", "event": "$50M Skype investment — 1.8% stake with Silver Lake"},
            {"date": "2010", "event": "Okta Series A lead; early Apptio check"},
            {"date": "2011", "event": "Instagram miss (PicPlz); Facebook buys Instagram ~$1B"},
            {"date": "2011", "event": "Microsoft acquires Skype ~$8.5B — a16z ~3× on $50M"},
            {"date": "2017", "event": "Okta IPO ~$6B valuation"},
            {"date": "2010s", "event": "Fund size expansion; crypto fund; media/content arm grows"},
            {"date": "2021", "event": "Acquired Part II — firm ~11 years old, industry transformed"},
        ],
    },
    "review_notes": "Manual GPT Acquired batch — v5.1-acquired; a16z Part II of II",
}

EPISODES_PART2["acq-ethereum"] = {
    "keywords": ["Ethereum", "Smart Contracts", "DeFi"],
    "conclusion": "Ethereum extends Bitcoin's calculator into a Turing-complete world computer — Vitalik Buterin's 2013 white paper after Mastercoin rejected general-purpose scripting. July 2014 crowd sale: ~$18.3M for ~60M ether in two weeks. July 2015 Frontier launch; ICO boom followed (64 ICOs raised >$100M in 2016; 2300 ICOs ~$11B in H1 2018). 2016 DAO hack forced hard fork (ETH vs. ETC). Mid-2021: ~$350B+ ETH market cap, gas $50–70, throughput ~Raspberry Pi — Eth2 proof-of-stake/sharding still pending. Packy McCormick bull case: EIP-1559 fee burn, DeFi/NFT composability; bear: scalability trilemma, mining pool concentration, government risk.",
    "background": "Season 8 finale after Bitcoin and Berkshire trilogy. Camila Russo's The Infinite Machine primary source. Vitalik: Toronto, Bitcoin Magazine, Mastercoin/Colored Coins Israel trip, Ethereum Foundation in Zug.\n\nPacky joins analysis for bull/bear, 7 Powers, grading on protocol success not ETH trade.",
    "important_facts": [
        "July 22–Aug 2014 crowd sale: ~$18.3M raised selling ~60M ether — largest crypto crowd sale to that point; Ethereum Foundation Swiss non-profit structure.",
        "July 30, 2015 Frontier release — first public Ethereum; first ICO on ETH two weeks later.",
        "2016: 64 ICOs raised >$100M; 2017 CryptoKitties peaked at ~15% of all Ethereum transactions — invented NFT concept.",
        "Mid-2021 gas fees hit ~$50–70 per transaction; Ethereum global throughput ~15–65 TPS vs. Eth2 target ~100,000 TPS (still unreleased).",
        "Three mining pools (Ethermine, F2Pool, Nanopool) combined ~60% hash rate — collusion risk distinct from censorship resistance.",
    ],
    "mental_model": {
        "name": "World Computer with Gas",
        "components": "Bitcoin = calculator; Ethereum = computer with two account types (users + contracts holding code and money). Gas paid in ether incentivizes validators. Composability: Uniswap, AMMs, DeFi legos on shared state. Bootstrapped via illicit-adjacent use cases (ICOs like Silk Road for Bitcoin). Scalability trilemma: decentralization, security, scalability — pick two. Vitalik as benevolent technical leader without CEO title.",
        "application": "Protocol investing requires separating ETH token economics from developer ecosystem moat. Switching costs from Solidity/EVM, ETH as base trading pair, and NFT/DeFi liquidity compound — but negative network effects when congestion raises fees for all users.",
    },
    "competitive_advantage": "Ethereum leads on developer mindshare, EVM compatibility, and DeFi/NFT liquidity at mid-2021.\n\nSmart contracts + contract accounts unprecedented — code holds its own money.\n\nWeaknesses: Eth2 delay (Serenity since roadmap 2015); Raspberry-Pi-level compute; mining pool concentration; government securities scrutiny survived via commodity gas argument (Grundfest).\n\nVersus Solana/other L1s: multi-chain coexistence plausible (AWS/Snowflake analogy) — ETH is settlement/trading pair hub even if apps migrate execution.",
    "key_insights": [
        {"view": "Mastercoin rejection birthed Ethereum.", "question": "Why not build on Bitcoin?", "answer": "Vitalik proposed general-purpose scripting to Mastercoin founder — told to finish core functions first. Colored Coins and Israel trip showed need for new chain, not Swiss Army knife on Bitcoin chassis."},
        {"view": "Foundation structure was regulatory arbitrage.", "question": "Why Swiss non-profit?", "answer": "SEC former commissioner Grundfest accepted gas/commodity analogy — ether needed utility (pay validators) to avoid securities classification. C-corp founders left; Vitalik held veto-like moral authority at 20."},
        {"view": "ICOs were killer app for bootstrapping.", "question": "Why 2017–18 bubble?", "answer": "Every token sale needed ETH — demand loop like Silk Road for Bitcoin. 2300 ICOs raised ~$11B in H1 2018 alone. Utility for ETH even when many ICOs were scams."},
        {"view": "DAO fork proved governance is human.", "question": "What broke immutability?", "answer": "2016 DAO hack drained funds; community hard-forked to bail out investors — ETH vs. ETC split. Contrasts Bitcoin ossification; Vitalik human element vs. alien-tech Satoshi stash."},
        {"view": "Congestion is bearish and bullish.", "question": "Why hasn't Eth2 shipped?", "answer": "Open-source foundation governance slow vs. startup; Fred Wilson frustration template. High fees prove demand but push developers to Solana/etc. — threading scalability needle without killing decentralization is second 'rabbit from hat.'"},
    ],
    "top_investment_implications": [
        {"ticker": "ETH", "direction": "Watch", "confidence": "Low", "thesis": "ETH value tied to gas burn (EIP-1559), DeFi/NFT activity, and Eth2 delivery — monitor L2 migration reducing L1 fee pressure; not investment advice."},
        {"ticker": "COIN", "direction": "Watch", "confidence": "Low", "thesis": "Exchange revenue correlates with ETH/BTC trading volumes and ICO-era retail participation — regulatory overhang persists."},
    ],
    "golden_quotes": [
        '"Bitcoin is a calculator, let\'s build a computer." — Vitalik\'s Ethereum premise (paraphrased in episode).',
        '"The relative power of the computer that is Ethereum is roughly equivalent to a Raspberry Pi on home broadband." — mid-2021 throughput reality check.',
        '"Bootstrapping the network with illegitimate use cases." — playbook theme (Silk Road/ICOs) then legitimate apps follow.',
    ],
    "chronology": {
        "subject": "Ethereum",
        "events": [
            {"date": "2011", "event": "Vitalik Buterin starts writing for Bitcoin Magazine"},
            {"date": "Nov 2013", "event": "Ethereum white paper first draft emailed to crypto insiders"},
            {"date": "Jan 2014", "event": "Miami Bitcoin conference — Ethereum announced; founding team forms"},
            {"date": "Jul 2014", "event": "Crowd sale raises ~$18.3M for ~60M ether"},
            {"date": "Jul 2015", "event": "Frontier mainnet launch"},
            {"date": "2016", "event": "DAO hack and hard fork — ETH/ETC split"},
            {"date": "2017", "event": "CryptoKitties — ~15% of network txs; NFT concept born"},
            {"date": "2018", "event": "ICO peak — 2300 ICOs raise ~$11B in H1"},
            {"date": "2021", "event": "DeFi summer; gas ~$50–70; ETH market cap ~$350B+ context"},
            {"date": "2021", "event": "Acquired Season 8 finale with Packy McCormick analysis"},
        ],
    },
    "review_notes": "Manual GPT Acquired batch — v5.1-acquired; Season 8 finale",
}
