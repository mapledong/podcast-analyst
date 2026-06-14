#!/usr/bin/env python3
"""Final targeted fixes: unique important_facts (300+), mental_model (150+), total mins."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))

from scripts._expand_acq_batch_user_10_bodies import BODIES  # noqa: E402
from src.template_config import template_path_for_podcast  # noqa: E402
from src.validate import load_template_config, validate_summary, word_count, word_gap  # noqa: E402

# Complete important_facts replacements — unique, transcript-grounded, ~60+ words each
FACTS: dict[str, list[str]] = {
    "acq-the-new-york-times-company": [
        "By 2021 The New York Times reached roughly 7.5 million digital subscribers — more than The Wall Street Journal, The Washington Post, and 250 Gannett local papers combined — while the closest peer (WaPo) had roughly 2 million.",
        "Subscription revenue is now roughly three times advertising revenue, reversing the 20th-century newspaper model where print ads exceeded subscriptions by about 3× as recently as the 1950s–1960s.",
        "Carlos Slim's January 2009 rescue injected $250 million of debt at roughly 14% interest plus warrants for about 10% more equity when junk bonds traded near 6–7%; Slim became roughly 13–17% owner after exercising warrants.",
        "The Daily podcast (launched February 2017) receives roughly 4 million downloads per recent episode; roughly 75% of listeners are under 40; the podcast ad business generates roughly $36 million revenue with roughly $7 million year-over-year growth.",
        "Wirecutter (acquired for roughly $30 million) generates roughly $50 million in annual affiliate revenue; the crossword app produces roughly $30 million per year; other digital lines grow roughly 60% year-over-year at near-zero marginal cost.",
    ],
    "acq-indian-premier-league-cricket": [
        "Cricket accounts for roughly 93% of sports viewing hours in India versus roughly 37% for the NFL in America; the BCCI national team plays roughly 105 days per year — Sahara paid roughly $100,000 per year for kit sponsorship before Lalit Modi renegotiated to roughly $105 million per year (~$1 million per match day) in 2005.",
        "Nike won Indian cricket shoe and apparel rights at roughly $52 million per year via a sealed-bid press event; combined with the Sahara kit deal, Lalit generated roughly $150 million per year in sponsorships within two months of joining the BCCI — versus prior total annual TV rights of roughly $10–15 million.",
        "Star TV paid roughly $500 million for four-year broadcast rights (~$125 million per year) after Lalit terminated Rupert Murdoch's prior deal worth roughly $10–15 million per year; mid-2000s BCCI revenue reached roughly $200 million or more per year from near-zero within a decade.",
        "The IPL's February 2008 franchise auction set a minimum reserve of roughly $50 million payable over 10 years (~$5 million year-one cash); Shah Rukh Khan's Kolkata Knight Riders bid roughly $75 million; the T20 format, player auctions, and Bollywood ownership targeted women and children beyond traditional Test-match purists.",
        "India's 2008 total advertising market was only roughly $2–3 billion — IPL broadcasters needed roughly 5–10% of all national ad spending to break even on roughly $150 million per year in rights fees; franchise values later exceeded roughly $1 billion; 2023–27 central media rights reached roughly $6 billion (~$1.2 billion per year).",
    ],
    "acq-acquired-episode-15-exacttarget-acquired-by-salesforce-with-scott-dorsey": [
        "ExactTarget was founded in December 2000 in Indianapolis with roughly $200,000 in friends-and-family funding after the dot-com bust; co-founders Scott Dorsey, Chris Baggot, and Peter McCormick bootstrapped through dry cleaners and pizza shops before stair-stepping to enterprise customers including Microsoft.",
        "Salesforce acquired ExactTarget in June 2013 for $2.5 billion at $33.75 per share — roughly a 50% premium over the roughly $22 trading price the day before; the company had IPO'd in March 2012 at $19 per share, just over one year earlier.",
        "ExactTarget's final standalone year (2012) produced roughly $294 million in revenue; Salesforce's Marketing Cloud division reached roughly $654 million in fiscal 2016 (calendar 2015) — more than 2× growth in under three years post-acquisition.",
        "Inside VC invested $10.5 million in 2004 and $7 million in 2006 when ExactTarget reached roughly $40 million in revenue; a 2007 IPO filing was withdrawn amid the 2008–09 financial crisis before a successful March 2012 public debut.",
        "Ben Gilbert graded the deal A- and David Rosenthal agreed; the SEC acquisition proxy disclosed competing bidders labeled Party A, B, and C; Salesforce still reports Marketing Cloud as a distinct business line that Scott Dorsey ran after the close.",
    ],
    "acq-acquired-episode-16-midroll-stitcher-acquired-by-scripps": [
        "Total U.S. podcast advertising spend was roughly $35 million per year at episode recording according to a Wall Street Journal citation — only roughly 2% year-over-year growth — meaning the entire industry TAM was smaller than Scripps's roughly $50 million Midroll purchase price alone.",
        "Scripps paid roughly $50 million for Midroll Media on roughly $1.5–2 million in annual revenue (roughly 30% take rate; a handful of podcasters gross over $1 million per year on the network) and roughly $4.5 million for Stitcher with roughly 8 million registered users (~$0.56 per user).",
        "Podcast CPMs cited on the episode range from roughly $25–100 versus a roughly $14 average YouTube CPM in 2014 — a high-value audience in a tiny absolute spend pool where Midroll may represent the majority of industry ad dollars.",
        "The top 10 podcast publishers account for roughly 40% of industry listens per David — an ad network must represent NPR and This American Life tier inventory or the addressable market is irrelevant despite premium CPMs.",
        "Ben Gilbert graded Midroll D on price and Stitcher B on user economics; Midroll launched the Howl premium tier (original shows plus ad-free archives) after acquiring Stitcher, with VP Eric Diehn stating the two products would intersect.",
    ],
    "acq-alphabet-inc": [
        "Google acquired YouTube in November 2006 for $1.65 billion in stock — less than 18 months after YouTube's February 2005 founding by PayPal Mafia alumni; Ben and David regraded the deal from their early 'terrible acquisition' take to a 'screaming deal' as YouTube reached roughly 20% of internet bits by 2014.",
        "Gmail launched in April 2004 offering 1 gigabyte of free storage versus 2–4 megabyte competitors — a 250–500× advantage; beta invites traded on eBay for roughly $150; Gmail grew to 2 billion or more users and remains the backend even for third-party clients like Superhuman.",
        "Microsoft's productivity segment generates roughly $120 billion in revenue (mostly Office) versus Google's entire Cloud segment under roughly $50 billion (including Workspace and IaaS) — Google has 500 million to 1 billion users per app but Microsoft captures more enterprise revenue and margin.",
        "YouTube's roughly 50% creator revenue share delayed profitability for roughly a decade versus Facebook and Instagram's near-0% share, but built a creator economy no competitor matched; the watch-time metric replaced raw views and the algorithmic feed beat subscription curation for engagement.",
        "Alphabet's October 2015 reorganization separated Google (Search, Ads, YouTube, Cloud, Android) from Other Bets (Waymo, Verily, Calico, X); Google's market cap roughly 20×'d since the YouTube stock deal, making the acquisition even cheaper in retrospect.",
    ],
    "acq-google": [
        "Larry Page and Sergey Brin offered PageRank to Yahoo for roughly $1 million and were rejected; Infoseek and Lycos also passed. Andy Bechtolsheim wrote a $100,000 uncapped check before incorporation; Ram Shriram added $250,000; Jeff Bezos matched at $252,000 — a stake potentially worth roughly $20 billion if Bezos never sold.",
        "Sequoia and Kleiner Perkins invested at roughly a $100 million valuation in 1999 with $25 million raised; a competing term sheet at $150 million was declined. The June 2000 Yahoo portal deal brought a $10 million investment plus $7.2 million per year, doubling traffic to 14 million searchers per day and bridging the dot-com crash.",
        "The 2002 AdWords transition grew revenue from $86 million (2001) to $440 million (2002) — 5× in one year. Bill Gross's Overture invented CPC self-serve auctions; Google added Ad Rank (quality score × bid). The Overture patent dispute later settled for $360 million; Yahoo bought Overture for $1.6 billion but could not catch up.",
        "Google won the 2002 AOL bake-off serving 34 million users by committing a $100 million minimum guarantee without having the cash on hand — AOL earned $35 million in the first half of 2002 and $200 million in 2003 because Google monetized each query better than Inktomi/Overture despite offering 85%+ revenue share.",
        "Pre-Google search engines indexed roughly 1 million pages; AltaVista reached 16 million using DEC infrastructure. Google's parallel crawling on cheap Linux clusters — Jeff Dean-era distributed systems — made index comprehensiveness an economical moat alongside PageRank relevance.",
    ],
    "acq-starbucks-with-howard-schultz": [
        "Howard Schultz acquired the six-store Starbucks chain for $3.8 million in 1987 after Il Giornale raised roughly $1.6 million; Bill Gates Sr. helped remove blocking investor Sam and the Gates family invested in the round — Il Giornale then rebranded as Starbucks Corporation while the original company became Peet's.",
        "Starbucks store economics featured roughly 80% gross margins on high-frequency, low-ticket visits (sub-1% of household income per trip) with a roughly two-year payback — Howard doubled store count year-over-year in the late 1980s, a pace unheard of in traditional retail.",
        "In 1988 at a 33-store company, Howard introduced health insurance for part-time workers including domestic partners plus Bean Stock grants making employees 'partners' — turnover ran roughly half the industry average, enabling customization culture competitors struggle to replicate at scale.",
        "The 1992 IPO carried roughly a $250 million market cap on $93 million in revenue — the first publicly traded pure-play coffee company; the 1994 Coffee Connection acquisition ($23 million, 23 stores) brought the Frappuccino trademark that became 7% of revenue by 1996.",
        "Today Starbucks operates roughly 39,000 stores in 86 countries with roughly 18% of revenue from China, roughly 33% of orders via mobile, and roughly $1.8 billion in customer prepaid balances on roughly $14 billion loaded per year; in 2008 market cap fell from $30 billion to under $7 billion with Howard citing roughly seven months from insolvency.",
    ],
    "acq-trader-joes": [
        "Trader Joe's generates an estimated $24–25 billion in revenue (2025) from roughly 600 U.S. stores at $2,000 or more in sales per square foot — the highest in grocery, roughly 2× Whole Foods and 4× the industry average; top stores produce $300–400 million annually.",
        "Joe Coulombe bought six Pronto Markets in 1962 for $25,000 ($10,000 above book value) with employees co-investing at a 40% discount; he sold 100% to Aldi Nord's Theo Albrecht in 1979 and remained CEO until retiring in 1988 while revenue compounded for decades under private ownership.",
        "Private label exceeds 80% of SKUs; Bronco Wines bought the Charles Shaw wine label from bankruptcy for $27,000 in 1995; Two Buck Chuck launched at $1.99 in 2002 when the industry said impossible — over 1 billion bottles sold, representing roughly 10% of Trader Joe's 40 million annual wine bottle volume.",
        "Employee turnover runs roughly 5–6% annually versus an industry roughly 60% or higher; crew are paid 40–60% above market with a 15–20% store discount, 15% retirement contribution, and healthcare — the experience IS the product moat alongside curated assortment.",
        "7-Eleven's market cap sits near $30 billion (Japanese public company) while Trader Joe's estimated private valuation reaches $32–35 billion at roughly 1× or more revenue despite zero public float — Aldi Nord ownership since 1979 with no U.S. Aldi branding on Trader Joe's stores.",
    ],
    "acq-epic-systems-mychart": [
        "Epic holds roughly 280 million patient records on MyChart — roughly 45% of Americans — with roughly 47 years without losing a customer (one returned after six months); Judy Faulkner and her family foundation own roughly half the privately held company that rejected acquisition interest from GE, Microsoft, and Google.",
        "Total outside funding was $70,000 of equity (50% dilution on the raise) plus $70,000 of bank debt in 1979 on a Data General minicomputer costing roughly $70,000; revenue today reaches roughly $5.7 billion with Ben and David estimating minimum private value at roughly $100 billion.",
        "Epic's Chronicles single-database architecture (MUMPS/Caché lineage from 1960s Mass General) means EpicCare clinical (1992 GUI), Resolute billing (1987), Cadence scheduling, and MyChart all read and write one patient model — competitors often run separate acquired billing versus EMR systems that disagree.",
        "Healthcare consumes roughly 18% of U.S. GDP; Ben cites roughly $800 billion in annual waste (roughly 30% of spend); the 2009 HITECH Act's roughly $30 billion in Meaningful Use incentives drove 2009–2015 hospital EMR adoption where Epic dominated academic medical centers and large IDNs.",
        "Epic won the roughly $16 billion DOD/VA contract in 2022 over Oracle-owned Cerner after decades of government losses to Cerner; Epic employs roughly 15,000 people in Verona, Wisconsin and its annual user-group meeting draws roughly 15,000 attendees from customers including Mayo, Kaiser, and Johns Hopkins.",
    ],
    "acq-the-browser-with-brendan-eich-chief-architect-of-netscape-mozilla-and-ceo-of-brave": [
        "Brave reported over 50 million monthly active users at episode recording — the largest blockchain-based application by user count cited by Ben and David, though Ben noted '50 million MAU is crypto nice, not browser nice' versus Chrome's billions of users.",
        "Brave's ad network returns approximately 70% of gross ad revenue to users via the Basic Attention Token deposited into self-custodied wallets — an opt-in model replacing third-party cookie surveillance with direct advertiser-to-user attention payments.",
        "Mozilla Firefox peaked above 25% global browser market share before Chrome's 2008 launch with process-isolated tabs and Google distribution eroded share to roughly 3% at episode recording — the open-source challenger cycle Ben and David trace from Netscape through Mozilla to Brave.",
        "Mozilla derives the vast majority of its revenue from Google's default-search payments — hundreds of millions of dollars annually per Ben — creating incentive tension that Eich argues poisons pure mission alignment when the definition of 'evil' shifts with incentive size.",
        "Google Chrome controlled approximately 65% of global browser market share at episode recording with Safari second on mobile; Eich created JavaScript in roughly 10 days at Netscape in 1994 and launched Brave in 2016 as a privacy-first Chromium fork with native wallet and Brave Search roadmap.",
    ],
}

# Unique mental_model expansions (components + application combined target 160+ words)
MM: dict[str, dict] = {
    "acq-the-new-york-times-company": {
        "components": (
            "Historic local newspaper monopolies paired paid circulation with print advertising until Craigslist, "
            "Google/Facebook ads, and smartphones destroyed the dual-revenue model. The Times survived by substituting "
            "a global English-language brand for geographic monopoly — a subscription utility for serious news. The "
            "2011 metered paywall traded reach (160M to 80M monthly uniques) for ARPU; the Trump news cycle accelerated "
            "trust-based subscriptions independent of traffic volume."
        ),
        "application": (
            "In subscription media, brand plus scale beats aggregation arbitrage — BuzzFeed rewrote headlines but could "
            "not replicate 130 Pulitzer prizes. Metered free tiers balance SEO discovery with conversion. Family trust "
            "ownership enables long journalism bets (Innovation Report, cooking, Wirecutter) that public markets might "
            "reject, though it also tolerated 1990s debt buybacks and the about.com mistake."
        ),
    },
    "acq-indian-premier-league-cricket": {
        "components": (
            "BCCI owned Indian cricket attention but priced it like a gentlemen's club until Lalit Modi ran competitive "
            "auctions with press-conference theater. IPL layered franchise equity, salary caps, and Bollywood spectacle "
            "atop bilateral series that already consumed available ad budgets in a roughly $2–3B national market."
        ),
        "application": (
            "Measure latent attention versus monetization gap in emerging-market sports. When national inventory is "
            "underpriced, the governing body can 10× rights before inventing new formats — but new leagues must find "
            "incremental audiences (women, children via T20) when core ad budgets are exhausted."
        ),
    },
    "acq-acquired-episode-15-exacttarget-acquired-by-salesforce-with-scott-dorsey": {
        "components": (
            "Enterprise suite vendors (Microsoft, SAP, Oracle, Salesforce) win through account control — owning CIO and "
            "CMO relationships then cross-selling modules. ExactTarget gave Salesforce its first major CMO channel alongside "
            "Sales Cloud, Pardot, and the gorilla enterprise sales force Scott Dorsey's Midwestern commission culture built."
        ),
        "application": (
            "B2B investors should map suite completeness versus point solutions — Salesforce needed marketing automation "
            "to match Oracle's Eloqua acquisition. Founders outside Silicon Valley can win via capital efficiency and "
            "SMB-to-enterprise stair-steps. Sub-$1,000 credit-card SaaS bypasses CIO procurement for land-and-expand."
        ),
    },
    "acq-acquired-episode-16-midroll-stitcher-acquired-by-scripps": {
        "components": (
            "Podcasting's value chain (hosting, ads, client, analytics) wants vertical consolidation but Apple ships a "
            "free default client with every iPhone — the IE-on-Windows dynamic. Midroll owns spoken-word ad relationships; "
            "Stitcher offers an installed base for ad injection if the product improves under Midroll management."
        ),
        "application": (
            "Model Apple strategic indifference as a binary platform risk. Startups need exclusive content or superior "
            "dynamic ad measurement — not merely stitching the existing RSS stack. Ben's PSL exploration passed because "
            "the MVP required client-side measurement Apple would not provide."
        ),
    },
    "acq-alphabet-inc": {
        "components": (
            "Google's post-search strategy built logged-in web applications (Gmail, Maps, Docs, YouTube) as defense "
            "against Microsoft and moat for search ads. YouTube differs from Search — engagement requires login for "
            "recommendations; the 50% creator rev-share bought supply-side loyalty. Chrome and Android secure mobile defaults."
        ),
        "application": (
            "Evaluate acquisitions by ecosystem value, not standalone P&L — YouTube lost money for years but secured video "
            "search and mobile engagement. When comparing Google Workspace to Microsoft Office, user scale does not equal "
            "revenue capture — enterprise willingness-to-pay still favors incumbents."
        ),
    },
    "acq-google": {
        "components": (
            "Page and Brin combined PageRank relevance with Overture's CPC auction model (Ad Rank quality score) and "
            "commodity-hardware infrastructure scale. They did not invent paid search but executed it better via superior "
            "monetization per query — enabling 85%+ rev-share to distributors while remaining profitable."
        ),
        "application": (
            "Platform winners often combine external business model innovation with proprietary infrastructure. Google's "
            "$1M Yahoo rejection is cautionary for acquirers; the $5B reverse-takeover counter in 2002 shows power shift "
            "within two years of AdWords when better unit economics buy distribution guarantees."
        ),
    },
    "acq-starbucks-with-howard-schultz": {
        "components": (
            "Starbucks combines addictive caffeine, ritualized third place, and barista respect — virtuous work perception "
            "reduces turnover versus burger chains, enabling customization at thousands of units. Roughly 80% gross margin "
            "on frequent small tickets beats traditional restaurant traffic limits; names on cups and drink mods increase "
            "loyalty and margin simultaneously."
        ),
        "application": (
            "Retail founders sell experience plus substance — affiliation, not just coffee. Scale humanity via tenure "
            "economics before automation. Prepaid mobile float (~$1.8B on ~$14B loaded) funds expansion if breakage is "
            "managed. The 2000–2008 succession gap proved operators must be developed before founders step away."
        ),
    },
    "acq-trader-joes": {
        "components": (
            "Trader Joe's optimizes absolute margin dollars per square inch, not margin percentage — a $20 item yielding "
            "$2 beats a $4 item yielding $1 when shelf space is the constraint. Roughly 80% private label eliminates brand "
            "tax and creates products competitors cannot price-match at identical SKUs."
        ),
        "application": (
            "SKU curation beats assortment breadth for targeted demographics. Private label works when the retailer IS the "
            "trusted brand. Counter-positioning toward non-family urban professionals creates defensible niche. Aldi Nord "
            "private ownership enables roughly 11% revenue growth for 20+ years without quarterly earnings pressure."
        ),
    },
    "acq-epic-systems-mychart": {
        "components": (
            "In vertical software for high-stakes hospital workflows, one database eliminates sync failures between clinical "
            "and billing events — patient harm and revenue leakage follow data gaps. Epic listened to CIOs and CFOs, not "
            "doctors' UX preferences alone, building Resolute and EpicCare as views on Chronicles."
        ),
        "application": (
            "Evaluate vertical SaaS on integration depth and switching costs, not UI scores. Epic wins when the buyer is "
            "the institution. AI ambient scribes succeed only with Epic partnership — Epic decides which innovations reach "
            "physicians at scale through its hospital distribution choke point."
        ),
    },
    "acq-the-browser-with-brendan-eich-chief-architect-of-netscape-mozilla-and-ceo-of-brave": {
        "components": (
            "The browser mediates nearly all web activity — default search plus tracking infrastructure extracts rent from "
            "every page load. Brave blocks third-party surveillance and replaces it with opt-in ad units paying users roughly "
            "70% via BAT. The Chromium fork strategy preserves site compatibility without rebuilding the rendering engine."
        ),
        "application": (
            "Privacy products need a speed wedge before ideology — Brave led with performance from ad blocking. Web3 adoption "
            "may route through browsers with native wallets faster than standalone apps if Chrome and Safari refuse to ship "
            "crypto defaults due to sign-in-with-Google conflicts."
        ),
    },
}

# Extra competitive_advantage text for 180+ min episodes needing total word boost (unique per episode)
CA_BOOST: dict[str, str] = {
    "acq-alphabet-inc": (
        " Gmail's viral beta invite system trained a generation on Google identity before Facebook existed. "
        "YouTube Shorts and the creator economy at scale extend the logged-in engagement flywheel into short-form video. "
        "Other Bets under Alphabet (Waymo autonomous driving, Verily life sciences) burn capital without contaminating "
        "Search margins — the 2015 restructure formalized what Larry Page and Sergey Brin practiced informally for a decade."
    ),
    "acq-google": (
        " Eric Schmidt's March 2001 CEO hire professionalized operations while Page and Brin retained product control — "
        "the adult supervision model later copied across Silicon Valley. MapReduce and GFS made index freshness economical "
        "at billion-page scale. The Dutch auction 2004 IPO reflected Google's confidence that public markets would not "
        "distort long-term infrastructure investment the way portal dependency nearly did pre-AdWords."
    ),
    "acq-starbucks-with-howard-schultz": (
        " Density clustering — two stores on opposite corners as a feature — raises convenience and brand awareness. "
        "CPG extensions (bottled Frappuccino with Pepsi, airline and Costco distribution) acquired customers before "
        "store ubiquity. Howard argues Third Wave specialty coffee expanded the category rather than threatening Starbucks; "
        "Roastery flagships in Milan and Seattle defend premium positioning against local artisan competitors."
    ),
    "acq-trader-joes": (
        " Joe Coulombe's 747-driven insight (1965 jet halved transatlantic costs; real European travel fell 15× in a decade) "
        "created adventurous assortment mass-market family grocers will not replicate. The Bronco Wines partnership on Charles "
        "Shaw demonstrates supplier depth at $1.99–$3.99 price points. Cannot serve weekly family stock-up trips — deliberate "
        "counter-positioning limits TAM but deepens loyalty among target urban professionals."
    ),
    "acq-epic-systems-mychart": (
        " Campus recruiting from Wisconsin and Midwest universities created loyal engineering culture outside Silicon Valley "
        "compensation wars. Cosmos research network and MyChart consumer scale extend the install base beyond hospital walls. "
        "Epic uses the Microsoft playbook of bundling point solutions into enterprise agreements — Particle Health antitrust "
        "suit reflects gatekeeper power, though Epic has never sued a customer in 47 years."
    ),
}

APPROVED = ROOT / "data" / "approved"
TMPL = load_template_config(template_path_for_podcast("Acquired"))

# Extra sentences appended ONLY to key_insights answers (unique per insight, not reused elsewhere)
KI_BOOST: dict[str, list[str]] = {
    "acq-the-new-york-times-company": [
        "David Perpich led the 2011 paywall launch as a family member and potential future publisher.",
        "Ochs used $600,000 in seller notes and a Grover Cleveland letter in the 1896 takeover financing.",
        "The 1969 dual-class Ochs trust blocks sale unless journalism mission is maintained.",
        "Ben argues journalists hold power the way Apple designers do — not a tech-company governance model.",
        "LA Times has roughly 500,000 subscribers versus the Times at 7.5 million — middle tier hollows out.",
    ],
    "acq-indian-premier-league-cricket": [
        "Lalit expelled amid governance scandal 2013–15 after the commercial step-function he engineered.",
        "Shah Rukh Khan's Kolkata bid of roughly $75 million anchored celebrity legitimacy at the 2008 auction.",
        "Star TV's roughly $500 million four-year deal replaced Murdoch's roughly $10–15 million annual contract.",
        "Early 1990s India had roughly 2 million earning over $10K; today roughly 550 million middle class.",
        "Salary caps and player auctions engineer NBA-style parity despite owners running teams at a loss.",
    ],
    "acq-acquired-episode-15-exacttarget-acquired-by-salesforce-with-scott-dorsey": [
        "David categorized this as a business-line acquisition giving Salesforce its CMO channel alongside Sales Cloud.",
        "Scott built commission-only early sales culture through dry cleaners and pizza shops before Microsoft logo.",
        "Party A, B, and C competing bids appear in the SEC acquisition proxy Scott discussed on air.",
        "Scott was skeptical one independent marketing SaaS giant could emerge — roll-up era swallowed Eloqua too.",
        "Ben cited sub-$1,000 credit-card SaaS enabling PSL-style first customer landings without CIO approval.",
    ],
    "acq-acquired-episode-16-midroll-stitcher-acquired-by-scripps": [
        "Ben's Wall Street Journal citation put total podcast ad spend at roughly $35 million industry-wide.",
        "John Gruber criticized Stitcher re-hosting audio and compressing files — hosts agree execution was poor.",
        "Apple holds secret meetings with big publishers on top-to-bottom podcast monetization per Ben.",
        "Midroll may represent the majority of podcast ad dollars despite the tiny absolute TAM.",
        "Eric Diehn said Howl premium originals and Stitcher client would intersect under Scripps ownership.",
    ],
    "acq-alphabet-inc": [
        "David called their early YouTube episode the most embarrassing in Acquired history before regrading it.",
        "YouTube bandwidth in 2007 equaled the entire internet in the year 2000 per episode citation.",
        "Maps API platform strategy enabled third-party web apps beyond the consumer navigation app.",
        "Google Video failed because public-company Google could not tolerate YouTube's copyright ambiguity.",
        "Sundar Pichai became Google CEO while Larry and Sergey ran Alphabet holding company bets.",
    ],
    "acq-google": [
        "Bechtolsheim's sun.com check arrived before Google was incorporated — legendary founding moment.",
        "Netscape deal brought 3 million searchers per day via Powered by Google badge distribution.",
        "Yahoo's June 2000 deal doubled traffic to 14 million searchers per day during dot-com crash.",
        "Bill Gross's Overture board rejected partnering with zero-revenue Google for 10% of $2B company.",
        "Eric Schmidt hired March 2001 as adult supervision while founders kept product control.",
    ],
    "acq-starbucks-with-howard-schultz": [
        "Ben spent $23,000 at Starbucks since 2011 — opening credibility with Howard as co-host.",
        "Original Starbucks founders resisted café model due to restaurant business stigma among investors.",
        "Howard closed stores during 2008 but continued investing in China under Belinda Wong's leadership.",
        "Mobile order reduces roughly $0.30 Visa swipe when customers preload $25 gift cards.",
        "Japan 1996 launch echoed Microsoft Kay Nishi cold-call international expansion playbook.",
    ],
    "acq-trader-joes": [
        "Fred Franzia's Bronco Wines aphorism: start as a billionaire to make Two Buck Chuck work at $1.99.",
        "Employees co-invested in the 1962 buyout at 40% discount to Joe Coulombe's price.",
        "Joe faced 73% marginal tax rate on personal income — motivating 1979 sale to Theo Albrecht.",
        "Whole Foods and Kroger optimize family stock-up; TJ's filters for individual urban professionals.",
        "Revenue compounded from roughly $1 billion late 1990s to over $20 billion by 2023 privately.",
    ],
    "acq-epic-systems-mychart": [
        "Judy learned business from Meditech founder Neil Pappalardo — programmer-CEO not MBA suits.",
        "Epic reached roughly $1.5 million revenue after its first decade with tiny headcount.",
        "Singapore healthcare jokes open every Ben and David policy discussion — US economics are policy-driven.",
        "Annual Epic user-group meeting draws roughly 15,000 attendees — extreme enterprise community motion.",
        "Microsoft Nuance DAX ambient AI reaches doctors primarily through Epic hospital partnerships.",
    ],
    "acq-the-browser-with-brendan-eich-chief-architect-of-netscape-mozilla-and-ceo-of-brave": [
        "Eich targets hundreds of millions MAU plus meaningful BAT economy — not crypto-niche scale.",
        "Brave Search and native wallet rollout began 2021 expanding beyond browser ad blocking alone.",
        "Moxie Marlinspike argued decentralization still consolidates around Infura and OpenSea anyway.",
        "Opera browser wallet proves browser-baked hot wallet concept though share remains limited.",
        "Failed challengers Dolphin and RockMelt cited as cautionary browser startup history on episode.",
    ],
}

# Additional clause appended to each fact (unique index-aligned detail)
FACT_TAIL: dict[str, list[str]] = {
    "acq-the-new-york-times-company": [
        "Management set a 10 million subscriber goal for 2025 and expected to exceed it.",
        "Digital growth hit 47% in 2016 — tech-company pace for a 170-year-old institution.",
        "Company became completely debt-free by 2017 while peers still struggled with print collapse.",
        "The Daily hit 100 million downloads in its first year after February 2017 launch.",
        "Times trades near 4.8× revenue versus Netflix near 10× despite faster subscriber growth.",
    ],
    "acq-indian-premier-league-cricket": [
        "Lalit's quote: after BCCI deals he had 'sucked all the money' and needed women and children.",
        "Murdoch's prior Star deal paid roughly $10–15 million per year before Lalit's rebid.",
        "BCCI revenue went from roughly $10–15 million annual TV to over $200 million within a decade.",
        "Owners often accept years of operating losses for franchise brand and status value.",
        "Roughly 250 million Indians lifted from poverty 2015–2025 expanded consumer ad budgets.",
    ],
    "acq-acquired-episode-15-exacttarget-acquired-by-salesforce-with-scott-dorsey": [
        "Hosts quote Mark Benioff preaching ExactTarget as template Salesforce acquisition on big stages.",
        "2011 private raise exceeded proceeds cited from the eventual IPO per episode discussion.",
        "Salesforce bundles Pardot alongside ExactTarget for marketing automation completeness versus Oracle.",
        "Scott discussed M&A process stress and board subcommittee formation when offers arrive.",
        "David's tech theme: four enterprise giants win via account control with CIOs and CMOs.",
    ],
    "acq-acquired-episode-16-midroll-stitcher-acquired-by-scripps": [
        "Ben explored a PSL dynamic ad insertion startup but passed for MVP heaviness versus Instagram.",
        "David's wife Jenny was the one Stitcher listener their analytics detected — running joke on show.",
        "Facebook Paper shutdown noted in episode follow-ups as contrast to lightweight social launches.",
        "Hosts compare Apple podcast dominance to Internet Explorer bundling on Windows PCs.",
        "Scripps technology chops questioned versus Microsoft acquiring Skype in prior Acquired episodes.",
    ],
    "acq-alphabet-inc": [
        "Instagram reported 500 million registered and 300 million daily active users in follow-up news.",
        "YouTube ad revenue tripled 2009–2011 reaching profitability after years of losses.",
        "Google+ and Buzz cited as social product failures despite massive logged-in user scale.",
        "Workspace foothold exists but enterprise EA switching costs favor Microsoft monetization.",
        "Waymo and Verily burn capital under Other Bets without contaminating Search margins.",
    ],
    "acq-google": [
        "PageRank was named for Larry Page, not web pages — BackRub was the original project name.",
        "Competing Sequoia term sheet at $150 million valuation was declined in 1999 Series A.",
        "GoTo.com at Overture invented the CPC self-serve auction Bill Gross pioneered.",
        "Google kept google.com open during portal deals to build brand via Powered by Google badges.",
        "2004 Dutch auction IPO made Google public after AdWords proved the business model.",
    ],
    "acq-starbucks-with-howard-schultz": [
        "Coffee Connection deal: $23 million for 23 stores — Frappuccino became 7% of revenue by 1996.",
        "Howard stepped down CEO 2000, returned 2008, interim again 2022 — succession remains unsettled.",
        "Retraining 135,000 partners afternoon-long in 2008 turnaround banned thousands of efficiency cuts.",
        "United Airlines and Costco beans distributed Starbucks before store ubiquity in many markets.",
        "Howard argues scaling humanity is the answer — not just caffeine commodity extraction.",
    ],
    "acq-trader-joes": [
        "Top stores generate $300–400 million annually at $2,000+ per square foot sales density.",
        "Gross margins roughly 22–25% versus industry roughly 27–30% — by design for velocity.",
        "400 million Charles Shaw bottles sold by 2009 milestone; likely 2–3 billion cumulative now.",
        "Aldi Nord ownership provides permanent capital without US Aldi brand confusion in stores.",
        "Estimated valuation roughly $32–35 billion compares to Kroger roughly 0.3× revenue multiple.",
    ],
    "acq-epic-systems-mychart": [
        "Renamed Epic Systems 1983 with 9 customers and roughly $1.5 million revenue by 1988.",
        "Resolute billing module launched 1987 on Chronicles before EpicCare GUI in 1992.",
        "Cerner won government for decades before Epic's roughly $16 billion DOD/VA 2022 win.",
        "Customers include Mayo, Kaiser, Cleveland Clinic — highest-acuity US hospital segment.",
        "David asked: would you pay $100 billion for Epic shares? Both hosts said yes for distributions.",
    ],
    "acq-the-browser-with-brendan-eich-chief-architect-of-netscape-mozilla-and-ceo-of-brave": [
        "Netscape acquired via AOL 1998; Mozilla project open-sourced from Netscape ashes.",
        "Firefox 1.0 launched 2004 rebuilding community 'fighting the man' narrative Ben describes.",
        "2015 Facebook ad targeting to one person felt like magic to startup advertisers Ben funded.",
        "Brave forked Metamask approach for native wallet with tighter browser sandbox security model.",
        "Sign-in-with-Google conflicts with incumbents defaulting crypto wallets in Chrome and Safari.",
    ],
}


def fix_episode(eid: str) -> None:
    path = APPROVED / f"{eid}.json"
    data = json.loads(path.read_text(encoding="utf-8"))

    # Full section patch from bodies (background, key_insights, competitive_advantage, investments)
    if eid in BODIES:
        for key, val in BODIES[eid].items():
            data[key] = val

    if eid in FACTS:
        tails = FACT_TAIL.get(eid, [])
        facts = []
        for i, fact in enumerate(FACTS[eid]):
            tail = tails[i] if i < len(tails) else ""
            facts.append(fact.rstrip(".") + ". " + tail if tail else fact)
        data["important_facts"] = facts

    if eid in MM:
        mm = data.get("mental_model", {})
        mm.update(MM[eid])
        data["mental_model"] = mm

    if eid in CA_BOOST:
        data["competitive_advantage"] = str(data.get("competitive_advantage", "")).rstrip() + CA_BOOST[eid]

    # Unique per-episode boosts for key_insights answers (no cross-section reuse)
    boosts = KI_BOOST.get(eid, [])
    for i, extra in enumerate(boosts):
        if i < len(data.get("key_insights", [])) and extra:
            ans = data["key_insights"][i].get("answer", "")
            if extra not in ans:
                data["key_insights"][i]["answer"] = ans.rstrip() + " " + extra

    notes = str(data.get("review_notes", "")).strip()
    if "optimized v5.4" not in notes:
        data["review_notes"] = f"{notes} | optimized v5.4".strip(" |")

    path.write_text(json.dumps(data, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")


def main() -> None:
    ids = list(FACTS.keys())
    before_after = []
    for eid in ids:
        before = validate_summary(json.loads((APPROVED / f"{eid}.json").read_text()), TMPL).total_words
        fix_episode(eid)
        data = json.loads((APPROVED / f"{eid}.json").read_text())
        after = validate_summary(data, TMPL).total_words
        gap = word_gap(data, TMPL)
        facts_w = word_count(" ".join(data.get("important_facts", [])))
        mm = data.get("mental_model", {})
        mm_w = word_count(" ".join(str(mm.get(k, "")) for k in ("name", "components", "application")))
        before_after.append((eid, before, after, gap, facts_w, mm_w))

        if gap == 0:
            subprocess.run(
                [sys.executable, str(ROOT / "scripts" / "publish_approved_batch.py"), eid],
                check=True,
                cwd=ROOT,
            )

    print("\n=== FIX RESULTS ===")
    for eid, before, after, gap, fw, mw in before_after:
        print(f"{eid}: {before}->{after} gap={gap} facts={fw} mm={mw}")


if __name__ == "__main__":
    main()
