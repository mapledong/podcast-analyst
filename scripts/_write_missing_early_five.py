#!/usr/bin/env python3
"""Write 5 missing early-season v5.1 JSON files."""
from __future__ import annotations

import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))

from scripts._early_acq_v51_common import base  # noqa: E402

APPROVED = ROOT / "data" / "approved"

META = {
    "links": {
        "apple_podcasts": "https://podcasts.apple.com/podcast/acquired/id1050462261",
        "spotify": "https://open.spotify.com/show/2HI3KdjtJnr3E8B4W8Y0Yx",
    }
}

def chrono(subject: str, events: list[tuple[str, str]]) -> dict:
    return {"subject": subject, "events": [{"date": d, "event": e} for d, e in events]}


EPISODES: dict[str, dict] = {
    "acq-episode-13-push-pop-press-facebook-instant-articles-with-todd-bishop": {
        "episode_rating": {"overall": 3},
        "keywords": ["Instant Articles", "Push Pop Press", "Publishing"],
        "conclusion": "Facebook's Push Pop Press acquisition (2016) — Apple veterans Mike Matas and Kimon Tsinteris — was a small people-and-technology pick-up that became product leadership for Instant Articles: publisher HTML hosted on Facebook, loading ~10x faster than mobile web (~8 seconds to under a second). Todd Bishop (GeekWire) explains the publisher trade: Facebook as largest referral driver versus Google AMP and Apple News; Instant Articles keep users in-app with Facebook-served ads (100% revenue if publisher sells, 70/30 if Facebook sells). Paper app was the Trojan horse; hosts grade people/tech acquisition that fixed Facebook's non-native mobile app era post-hoodie AllThingsD interview.",
        "background": "Guest Todd Bishop joins Ben and David on Push Pop Press — founded February 2010 by ex-Apple designers/engineers who built Camera, Photos, Maps, Settings on early iPhone. TED 2011 demo with Al Gore's Our Choice reimagined interactive book on iOS.\n\nFacebook acquired team; founders said they would not continue in book industry — technology applied to Instant Articles (David Carr scoop: Facebook as 'big dog in the park'). Episode compares AMP vs IA UX; Todd on GeekWire's ad sales and reader experience choices.",
        "important_facts": [
            "Push Pop Press founded Feb 2010; Mike Matas and Kimon Tsinteris ex-Apple (~4–5 years); TED 2011 Our Choice with Al Gore; never raised VC — acquisition price undisclosed, assumed small.",
            "Instant Articles load ~10x faster than mobile web; Facebook cites ~8 second average mobile article load vs instant in-app reader.",
            "Revenue split: publisher-sold ads keep 100%; Facebook-sold ads 70/30 to Facebook; content hosted on Facebook servers — aggregation tension for publishers.",
            "Facebook Paper app (2014) from Creative Labs showcased Push Pop Press animation sensibility; Paper later shut down — tech lived in Instant Articles.",
            "Episode guest Todd Bishop (GeekWire); category people + technology; Zuckerberg mobile pivot after infamous hoodie AllThingsD interview cited as context."
        ],
        "mental_model": {
            "name": "Host the Content, Own the Session",
            "components": "Instant Articles trade publisher page views for speed and Facebook ad infrastructure — classic aggregator move: improve UX, keep user in walled garden, capture ad dollars. Push Pop Press brought native iOS polish Facebook lacked when mobile web wrappers failed. Publishers face prisoner's dilemma: must be where readers are (Facebook feed) even if it commoditizes brand and ad sales.",
            "application": "Media and B2B content businesses should model platform-hosted formats as tax on direct relationships — negotiate revenue share and data rights upfront. Acquirers buying design teams should trace where IP lands (Paper → Instant Articles) not where press release says."
        },
        "competitive_advantage": "Facebook's advantage was distribution plus native rendering engine — not journalism.\n\nPush Pop Press team imported Apple-grade animation and layout to in-feed reading; Instant Articles reduced bounce from slow mobile web. Publishers gained speed; Facebook gained session time and ad inventory.\n\nVersus Google AMP (still feels like web overlay), hosts prefer Facebook native experience. Todd notes Google better monetization tools for some publishers; Facebook better traffic.\n\nWeakness: publisher fear of platform dependency; Paper standalone failed to scale; Instant Articles required giving content to Facebook CDN.",
        "key_insights": [
            {"view": "People acquisition with hidden product roadmap.", "question": "Why buy a book startup?", "answer": "Founders explicitly exited book business post-deal — Facebook wanted iOS talent for mobile feed formats, not publishing vertical. Matas led Instant Articles; Paper was design prototype."},
            {"view": "Speed is the consumer hook.", "question": "Why 10x load time matters?", "answer": "Ben cites 8-second mobile web bounce; Instant Articles pre-fetch on Facebook infrastructure — reduces friction for shared links, increases ad impressions per session."},
            {"view": "Publishers face aggregation tax.", "question": "Why Todd Bishop cares?", "answer": "GeekWire lives on referral traffic; hosting on Facebook vs owned site shifts ad economics and reader relationship — Todd discusses own ad sales vs platform 30% cut."},
            {"view": "Mobile panic drove M&A.", "question": "Facebook context?", "answer": "Post-IPO Facebook needed native mobile ad units; hoodie interview embarrassment accelerated Creative Labs acquisitions including Push Pop Press."},
            {"view": "AMP vs IA product philosophy.", "question": "Google comparison?", "answer": "Ben prefers IA native feel over AMP webpage overlay; Google may win publisher tooling — dual-platform publishing inevitable for mid-size outlets."}
        ],
        "top_investment_implications": [
            {"ticker": "META", "direction": "Watch", "confidence": "Low", "thesis": "Instant Articles era shows Facebook converting feed dominance into publisher ad share — relevant to Meta audience network and Reels monetization history."}
        ],
        "golden_quotes": [
            "\"Facebook is like a big dog in the park\" — David Carr on Instant Articles scoop, quoted by hosts.",
            "\"Cough. Publishing. Cough.\" — Ben when founders said they would not continue in books.",
            "\"10 times faster\" — Facebook Instant Articles performance claim vs mobile web."
        ],
        "chronology": chrono("Push Pop Press · Instant Articles", [
            ("Feb 2010", "Push Pop Press founded by ex-Apple Matas and Tsinteris"),
            ("Spring 2011", "TED demo — Our Choice interactive book with Al Gore"),
            ("2011–12", "Facebook mobile crisis; non-native apps"),
            ("2013", "Hoodie AllThingsD interview — Zuckerberg mobile pivot"),
            ("2014", "Facebook Paper app launches from Creative Labs"),
            ("2014", "David Carr scoops Instant Articles in development"),
            ("2015", "Instant Articles launch to publishers"),
            ("2016", "Facebook acquires Push Pop Press team"),
            ("2016", "Acquired episode with Todd Bishop records"),
            ("2017+", "Paper shut down; IA persists in main app"),
            ("2016+", "Publishers weigh AMP, Apple News, and IA simultaneously"),
        ]),
    },
    "acq-acquired-top-ten-the-best-acquisitions-of-all-time": {
        "episode_rating": {"overall": 4},
        "keywords": ["M&A Rankings", "Capital Allocation", "Instagram"],
        "conclusion": "Season 6 episode 3 ranks history's best acquisitions by absolute dollar value created for acquirer (market cap contribution minus price), with caveats: majority deals only, enough time elapsed, subjective attribution when product merges (NeXT inside iOS). Top honors go to Google's Motorola-era peer deals and Facebook Instagram (~$1B buy, ~$20B revenue line cited at recording). Honorable mentions include WhatsApp (too soon on revenue), VMware ($625M EMC → ~$9B revenue). Hosts emphasize business-line acquisitions dominate; make big bets (Facebook) vs build-in-house (Google X). Moment-in-time March 2020 data amid COVID volatility.",
        "background": "Meta-episode from blog post expanded to director's cut — Ben and David rank top 10 with honorable mentions (WhatsApp, VMware, Pixar near-miss). Methodology: absolute dollar return to acquirer, attribution discounts when product subsumed, majority purchases only.\n\nCoverage includes Instagram $1B→~$20B ads revenue on Facebook stack, DoubleClick ad tech rails, Android $50M→~$77B attributed return, NeXT $429M→Jobs+iOS lineage, Marvel, ESPN, PayPal-eBay, booking.com, YouTube, Google Maps suite. Playbook: platform owners should acquire when distribution advantage converts to revenue line.",
        "important_facts": [
            "Ranking metric: absolute dollar value added to acquirer market cap minus purchase price — not ROI multiple alone (Android 1555X ROI but #4 on absolute list).",
            "Instagram (2012 ~$1B): ~$20B annual ad revenue attributed at recording — roughly two-sevenths of Facebook revenue; hosts cite bidding war with Twitter.",
            "Android acquired 2005 for ~$50M; hosts attribute ~$13B annual revenue contribution (~$9B Play + search allocation) and ~$77B net market cap contribution estimate.",
            "DoubleClick (2008 ~$3.1B): Google Network ads largely DoubleClick+AdMob stack per episode research — initially underestimated by hosts.",
            "NeXT (~$429M, 1997): Apple $1.4T company 'would not exist' without Jobs return and NeXTSTEP→macOS/iOS; Pixar $7.4B Disney deal added ~$2.3B net incremental market cap per their math."
        ],
        "mental_model": {
            "name": "Absolute Dollar Alpha",
            "components": "Best acquisitions create new business lines with near-zero marginal distribution cost for the acquirer — Instagram reused Facebook ad sales force; DoubleClick owned ad-serving rails. ROI multiples flatter small bases (Android $50M); absolute dollars favor mega-platforms buying revenue engines. Content deals (Marvel, ESPN) rank lower than zero-marginal-cost tech lines unless repeatable franchises (Marvel beats Pixar on predictability).",
            "application": "Corporate dev should score deals on incremental profit dollars at scale, not multiple on revenue — and ask whether target must remain standalone business line to count. VCs use list to justify platform bets: Facebook's Instagram/WhatsApp/Oculus trifecta vs Google's build-first culture."
        },
        "competitive_advantage": "Winning acquirers share open-loop distribution: Google search/Android, Facebook social graph, Disney franchise IP.\n\nInstagram's moat post-acquisition: same ad buyer UI, zero content COGS, mobile-native engagement — $20B revenue from free creator content. DoubleClick became industry plumbing — switching costs for publishers and advertisers.\n\nAndroid secured mobile search default and Play billing toll booth. NeXT supplied OS kernel and executive who could rebuild Apple culture.\n\nWeaknesses in list: attribution squinting (NeXT, Android search revenue); time-lagged outcomes; missing Berkshire-scale deals by design scope.",
        "key_insights": [
            {"view": "Business lines beat feature buys at scale.", "question": "Category breakdown?", "answer": "David tags 7 of top 10 as business lines vs 2 products (Android, Maps suite) and 1 people+tech (NeXT) — standalone P&L potential drives absolute dollar outcomes."},
            {"view": "Instagram is the revenue miracle.", "question": "Why #3?", "answer": "~$20B ads through Facebook portal with minimal incremental sales cost; content free from creators — hosts prefer Instagram economics over YouTube bandwidth costs."},
            {"view": "Android wins ROI not rank.", "question": "Why #4 not #1?", "answer": "$50M → ~$77B absolute still loses to larger dollar creators; can't eat multiple — absolute return metric favors already-large platforms buying large lines."},
            {"view": "Make bets; don't only build.", "question": "Facebook vs Google?", "answer": "Facebook Instagram/WhatsApp/Oculus acquisition spree vs Google X build — hosts argue acquire when distribution converts; Google succeeded with YouTube/Android/DoubleClick buys too."},
            {"view": "Content is lumpy.", "question": "Why Pixar honorable mention?", "answer": "Pixar requires hit every year; Marvel/ESPN more predictable revenue — next-hit risk keeps Pixar out of top 10 despite cultural value."}
        ],
        "top_investment_implications": [
            {"ticker": "META", "direction": "Long", "confidence": "Medium", "thesis": "Episode cites Instagram as canonical proof of acquirer distribution multiplying acquired engagement product — framework for judging Meta's later bets."},
            {"ticker": "GOOGL", "direction": "Watch", "confidence": "Medium", "thesis": "Android+DoubleClick+YouTube trilogy on list supports platform M&A discipline; underweights moonshot build-only strategy."}
        ],
        "golden_quotes": [
            "\"You can't eat ROI multiple\" — David on Android 1555X vs absolute-dollar ranking.",
            "\"Two-sevenths of Facebook's revenue is Instagram\" — Ben at time of recording.",
            "\"Make these bets\" — David playbook takeaway from Facebook acquisition era."
        ],
        "chronology": chrono("Acquired Top 10 · methodology", [
            ("S6 E3", "Top 10 episode recorded — blog post director's cut"),
            ("Mar 2020", "Market caps compiled pre-COVID volatility caveat"),
            ("1997", "Apple acquires NeXT — Jobs returns"),
            ("2005", "Google acquires Android ~$50M"),
            ("2006", "Disney acquires Pixar ~$7.4B"),
            ("2008", "Google acquires DoubleClick ~$3.1B"),
            ("2008", "Google acquires YouTube ~$1.65B"),
            ("2012", "Facebook acquires Instagram ~$1B"),
            ("2014", "Facebook acquires WhatsApp ~$19B — honorable mention"),
            ("2010s", "Hosts rank Marvel, ESPN, PayPal, booking.com entries"),
            ("2020+", "Listeners invited to Slack/email with missing deals"),
        ]),
    },
    "acq-acquired-episode-17-waze": {
        "episode_rating": {"overall": 4},
        "keywords": ["Waze", "Google Maps", "Mobile Platform Wars"],
        "conclusion": "Google acquired Waze in June 2013 for ~$1.0–1.3 billion (mostly cash) after Apple Maps failure and a failed Facebook bid — team stayed in Israel, key sticking point versus Menlo Park relocation. Waze crowdsourced live traffic, police, and road data from ~7M users (Oct 2011 Series C at ~$200M valuation, $30M round) versus top-down Garmin/TomTom maps. Ben and David frame deal as defensive data asset and mobile platform war weapon: Apple rumored ~$500M talks post-Maps apology; Facebook ~$1B press cycle collapsed on geography. Hosts grade highly for Google — free turn-by-turn destroyed $50–100 paid nav apps while harvesting invaluable probe data.",
        "background": "Episode 17 covers Google/Waze with community spotlight on Nexcast. David traces Free Map Israel origin — Ehud Shabtai C&D from GPS hardware vendor led to crowdsourced maps. Apple iOS 6 Maps launch (2012), Tim Cook apology, Scott Forstall exit, and Waze listed as alternative in apology letter.\n\nBidding drama: Apple rumors, Facebook weeks-long 'done deal' press, Google wins with Israel HQ preserved. Tech themes: data asset upends business model (give nav free, monetize data), mobile winner-take-all 2012 mindset.",
        "important_facts": [
            "Google acquired Waze June 2013 for ~$1.0–1.3B (mostly cash); team remained in Israel — Facebook deal failed partly over moving HQ to Menlo Park.",
            "Waze Oct 2011 Series C: $30M at ~$200M valuation, 7M users; Dec 2010 had 2M users and 250M km logged.",
            "Apple iOS 6 (2012) replaced Google Maps; Tim Cook public apology — unprecedented; Scott Forstall refused to sign letter, later fired.",
            "Apple rumored ~$500M Waze talks post-Maps flop; Facebook ~$1B acquisition reported for weeks before Google won.",
            "Hosts compare ~$1B Waze to ~$1B GM Cruise — Waze delivered real-time data value to Google Maps quickly."
        ],
        "mental_model": {
            "name": "Free Product, Paid Data",
            "components": "When probe data has platform value, give consumer product away (turn-by-turn nav) to maximize sensor network — Waze users report police, accidents, traffic; Google Maps ingests probe fleet. Competitors selling $50–100 Garmin apps could not match price. M&A resolves mobile war externalities: Apple needed Waze after Maps miss; Google could not let Facebook own social+driving graph.",
            "application": "Evaluate mapping/logistics startups on probe density and refresh rate, not consumer subscription revenue. Strategists pricing defensive M&A should model counterfactual platform loss (iOS default search/maps) not DCF of Waze standalone P&L."
        },
        "competitive_advantage": "Waze moat was live crowdsourced incident layer on community-maintained basemap — not static tiles.\n\nSocial login and gamified reporting created faster police/traffic updates than pure passive Android probes early on. Israeli engineering hub preserved post-deal — talent retention clause mattered.\n\nGoogle integration fortified Maps real-time routing; denied Apple and Facebook ownership of driving attention during commute.\n\nWeakness at sale: small user base vs price; revenue modest; Facebook/Apple could have built alternatives with time — speed mattered in 2012 platform war.",
        "key_insights": [
            {"view": "Maps apology created M&A window.", "question": "Why Tim Cook letter matters?", "answer": "Public Maps failure + recommending Waze in apology signaled Apple desperation; rumored $500M talks; Google preempted with higher bid and Israel terms."},
            {"view": "Facebook lost on geography.", "question": "Why didn't Facebook close?", "answer": "Waze team insisted on staying in Israel; Facebook wanted Menlo Park integration — weeks of press assumed done deal until Google swooped."},
            {"view": "Data asset > nav revenue.", "question": "Why pay $1B?", "answer": "Ben argues valuation tied to strategic data for Maps/Android, not Waze P&L — free nav destroys paid app market while feeding probe network."},
            {"view": "Platform wars felt winner-take-all.", "question": "2012 context?", "answer": "iOS vs Android battle; Maps exclusivity on iPhone ended; both sides treated mapping as existential — feels archaic now but drove bidding."},
            {"view": "Forstall exit tied to Maps.", "question": "Apple org damage?", "answer": "Scott Forstall refused to sign Cook apology; protégé of Jobs; fired — Maps quality became executive casualty beyond product bug."}
        ],
        "top_investment_implications": [
            {"ticker": "GOOGL", "direction": "Watch", "confidence": "Medium", "thesis": "Waze illustrates Google paying billions for probe data and mobile defaults — relevant to Maps moat vs Apple Maps recovery."},
            {"ticker": "META", "direction": "Watch", "confidence": "Low", "thesis": "Failed Waze bid shows Facebook mapping/social location ambition blocked — precursor to location-based ad strategies."}
        ],
        "golden_quotes": [
            "\"You drive with friends\" — Ben on Waze social navigation tagline.",
            "\"This would never happen under Steve\" — on Tim Cook Maps apology letter.",
            "\"A billion dollars is not a talent acquisition\" — Ben on Waze price vs acqui-hire."
        ],
        "chronology": chrono("Waze · Google acquisition", [
            ("2006", "Ehud Shabtai starts Free Map Israel after GPS vendor C&D"),
            ("Dec 2010", "2M users; 250M km logged"),
            ("Oct 2011", "Series C $30M at ~$200M val; 7M users"),
            ("Jun 2012", "Apple announces iOS 6 Apple Maps at WWDC"),
            ("Sep 2012", "Apple Maps launch; widespread failures"),
            ("2012", "Tim Cook apology; Scott Forstall exit"),
            ("2012–13", "Apple ~$500M Waze rumors; Facebook ~$1B press cycle"),
            ("Jun 2013", "Google acquires Waze ~$1.0–1.3B"),
            ("2013+", "Waze team stays in Israel; data feeds Google Maps"),
            ("2016", "Acquired Episode 17 records deal history"),
            ("2014+", "Apple Maps gradual quality recovery cited by hosts"),
        ]),
    },
    "acq-acquired-episode-16-midroll-stitcher-acquired-by-scripps": {
        "episode_rating": {"overall": 3},
        "keywords": ["Podcast Advertising", "Midroll", "Stitcher"],
        "conclusion": "Scripps acquired Midroll (~$50M, ~$1.5–2M revenue) and Stitcher (~$4.5M, ~8M registered users) to vertically integrate podcast ads, hosting, and client — first splash consolidating creator/ad/client pillars when total U.S. podcast ad spend was only ~$35M/year (~2% YoY). Ben grades Midroll D on price, Stitcher B as cheap user acquisition (~$0.56/user) but doubts $54.5M total wins category vs Apple default client and ~$100 CPM niche. Power law: top 10 publishers ~40% listens. PSL explored podcast startup but shied from Apple platform risk and MVP heaviness.",
        "background": "Episode 16 on Scripps/Midroll/Stitcher trifecta — old media buying podcast stack. Midroll ad network (~30% take; handful of shows >$1M gross). Stitcher client with lapsed users. Industry fragmented: Squarespace RSS, Libsyn hosting, manual Midroll sales minimums.\n\nBen's PSL podcast ad dynamic insertion research; Apple owns directory but ignores monetization. Grades split Midroll vs Stitcher; skepticism on Netflix-of-podcasts Howl premium tier.",
        "important_facts": [
            "Total U.S. podcast ad spend ~$35M/year at recording (~2% YoY growth) — entire TAM smaller than one Midroll price.",
            "Scripps ~$50M for Midroll on ~$1.5–2M revenue; ~$4.5M for Stitcher (~8M registered users, ~$0.56/user).",
            "Midroll ~30% take rate; handful of podcasters gross >$1M/year on network.",
            "Podcast CPMs ~$25–100 cited vs ~$14 YouTube 2014 average — high-value audience but tiny spend pool.",
            "Top 10 podcast publishers account for ~40% of industry listens — power law distribution."
        ],
        "mental_model": {
            "name": "Platform Default Beats Vertical Stack",
            "components": "Podcasting value chain (hosting, ads, client, analytics) wants consolidation but Apple ships free client with OS — same as IE-on-Windows dynamic Ben cites. Without exclusive content or measurement, Stitcher cannot displace default. Midroll needs top publishers for inventory; Scripps lacks tech DNA to build client in-house.",
            "application": "Investors in audio/media should model Apple strategic indifference/risk as binary outcome. Startups must own exclusive content or superior dynamic ad measurement — not merely stitch existing RSS stack."
        },
        "competitive_advantage": "Midroll's edge was relationships with largest indie podcasts and spoken-word ad sales expertise — people business not tech.\n\nStitcher offered installed base for ad injection if product improved. Scripps cash deployed when broadcast cash flows declined.\n\nCombined thesis: Netflix-of-podcasts with Howl premium originals + ad-free archives.\n\nWeakness: TAM $35M cannot justify $50M Midroll; Apple platform risk; Stitcher engagement uncertain; Ben PSL passed for MVP scope and Apple switch risk.",
        "key_insights": [
            {"view": "TAM too small for price.", "question": "Why grade Midroll D?", "answer": "$50M on ~$2M revenue requires massive industry expansion Scripps may not catalyze — entire market only ~$35M spend."},
            {"view": "Stitcher cheap on users.", "question": "Why Stitcher B?", "answer": "~$0.56 per registered user cheap if engagement fixable; pointing Midroll ads into client plausible small business even if category winner unlikely."},
            {"view": "Apple is sleeping giant.", "question": "Platform risk?", "answer": "Apple created podcasting via iTunes directory, ships default app, ignores monetization — any API/reporting change could obsolete third-party stacks."},
            {"view": "Power law inventory.", "question": "Who matters?", "answer": "Top 10 publishers ~40% listens — ad network must represent NPR/This American Life tier or TAM irrelevant."},
            {"view": "Consolidation inevitable but winner unclear.", "question": "PSL lesson?", "answer": "Ben explored dynamic ad insertion startup — needs client-side measurement Apple won't provide; heavy MVP vs Facebook/Instagram lightweight launches."}
        ],
        "top_investment_implications": [
            {"ticker": "SSP", "direction": "Watch", "confidence": "Low", "thesis": "Scripps podcast bet early indicator of broadcasters buying audio stacks — episode skeptical on ROI; illustrative not core SSP thesis."}
        ],
        "golden_quotes": [
            "\"$50 million for something that makes 2 million a year?\" — Ben on Midroll price.",
            "\"Apple has just accidentally had this nascent, huge opportunity\" — Ben on podcasting and iTunes directory.",
            "\"Top 10 publishers are responsible for 40 percent of listeners\" — David on power law."
        ],
        "chronology": chrono("Midroll · Stitcher · Scripps", [
            ("2010", "Midroll founded; ad network model"),
            ("2012+", "Stitcher client grows registered base"),
            ("2014", "U.S. podcast ad spend ~$35M industry-wide"),
            ("2015–16", "Dynamic ad insertion startups (Acast, Megaphone) emerge"),
            ("2016", "Scripps acquires Midroll ~$50M"),
            ("2016", "Scripps acquires Stitcher ~$4.5M"),
            ("2016", "Midroll launches Howl premium originals tier"),
            ("2016", "Acquired Episode 16 records; Ben PSL podcast exploration"),
            ("2016+", "Facebook Paper shutdown noted in follow-ups"),
            ("2017+", "Spotify and others later enter podcast M&A wave"),
            ("2016", "Apple maintains default Podcasts app dominance"),
        ]),
    },
    "acq-acquired-episode-15-exacttarget-acquired-by-salesforce-with-scott-dorsey": {
        "episode_rating": {"overall": 4},
        "keywords": ["ExactTarget", "Salesforce", "Marketing Cloud"],
        "conclusion": "Salesforce acquired ExactTarget in June 2013 for $2.5 billion ($33.75/share, ~50% premium) — founder CEO Scott Dorsey (Ben's cousin) on show. ExactTarget grew from Indianapolis bootstrap ($200K friends/family, Dec 2000) through dry cleaners and pizza shops to enterprise email marketing; IPO March 2012 at $19/share. Marketing Cloud revenue ~$654M in Salesforce FY2016 vs ExactTarget standalone ~$294M in 2012 — more than 2x in under three years. Hosts grade A-: business-line acquisition giving Salesforce CMO channel via 'account control' gorilla sales force; Scott ran Marketing Cloud post-close.",
        "background": "Interview format with Scott Dorsey — founding during dot-com bust outside Silicon Valley, commission-only early sales DNA, international via channel partners, dead 2007–09 IPO filing pre-JOBS Act exposing financials to competitors.\n\nSEC acquisition proxy with Party A/B/C bidders; Scott on process stress. Category: business line — Salesforce selling to sales orgs needed CMO/marketing automation (Pardot bundled). Tech theme: SaaS outsourcing non-core functions; sub-$1000 credit-card bypass of CIO for land-and-expand.",
        "important_facts": [
            "ExactTarget founded Dec 2000 Indianapolis; ~$200K initial raise; Scott Dorsey co-founder with Chris Baggot and Peter McCormick.",
            "Acquisition June 2013: $2.5B, $33.75/share (~50% premium); IPO March 2012 at $19/share; trading ~$22 day before deal.",
            "ExactTarget 2012 revenue ~$294M; Salesforce Marketing Cloud FY2016 ~$654M — >2x growth in <3 years post-acquisition.",
            "Salesforce still reports Marketing Cloud as distinct business line; Scott Dorsey ran division after close.",
            "SEC proxy disclosed Party A, B, C competing bidders — public M&A playbook for public company sale."
        ],
        "mental_model": {
            "name": "Account Control Expansion",
            "components": "Enterprise giants (Microsoft, SAP, Oracle, Salesforce) win by owning CIO/CMO relationships then cross-sell modules — ExactTarget gave Salesforce marketing automation slot alongside Sales Cloud. Indianapolis bootstrapping + commission sales culture scaled to Microsoft as customer before IPO. Acquisitions work best when target is bought, not sold — ExactTarget accelerated growth pre-deal.",
            "application": "B2B investors should map suite completeness vs point solutions — Salesforce needed CMO wallet share to match Oracle Eloqua/Adobe. Founders outside SV can win via capital efficiency and enterprise stair-steps (SMB → franchise → enterprise)."
        },
        "competitive_advantage": "ExactTarget moat was enterprise email deliverability, cross-channel expansion (SMS, social CoTweet), and Midwestern enterprise sales discipline.\n\nSalesforce added gorilla distribution — same customers, new buyer persona (CMO). Marketing Cloud branding persists as P&L line.\n\nWeakness: marketing automation point products faced Oracle/Adobe roll-ups; standalone IPO path blocked by 2008 crisis; only Salesforce scale completed CMO story.",
        "key_insights": [
            {"view": "Business line, not feature.", "question": "Category?", "answer": "Full marketing hub suite (email, SMS, social) with channel to customers Salesforce lacked — still called Marketing Cloud in earnings."},
            {"view": "Bootstrap to $294M.", "question": "Indianapolis lesson?", "answer": "Scott built on $200K through SMB stair-step to Microsoft enterprise logo — commission-only early sales shaped org DNA."},
            {"view": "Buy vs sell timing.", "question": "Why sell at premium?", "answer": "Hosts quote 'great acquisitions happen when companies are bought not sold' — Q1 beat during process supported $2.5B price."},
            {"view": "Marketing roll-up era.", "question": "Could standalone giant emerge?", "answer": "ExactTarget, Eloqua, others swallowed by Oracle/Salesforce — Scott skeptical one independent marketing SaaS giant at scale."},
            {"view": "Credit-card land expand.", "question": "Tech theme?", "answer": "Sub-$1000 SaaS lets advocates buy without CIO — opens PSL/Pioneer Square Labs-style fast first customer landings."}
        ],
        "top_investment_implications": [
            {"ticker": "CRM", "direction": "Long", "confidence": "Medium", "thesis": "ExactTarget Marketing Cloud doubling revenue in 3 years exemplifies Salesforce suite cross-sell — template for Slack/MuleSoft later integrations."}
        ],
        "golden_quotes": [
            "\"Great acquisitions happen when companies are bought, not sold\" — hosts on ExactTarget timing.",
            "\"Over twice as much in less than 3 years\" — David on $294M to $654M Marketing Cloud revenue.",
            "\"Account control\" — David on Salesforce pushing products through enterprise relationships."
        ],
        "chronology": chrono("ExactTarget · Salesforce", [
            ("Dec 2000", "ExactTarget founded Indianapolis post-bust"),
            ("2004", "Inside VC $10.5M raise; ~$40M revenue trajectory"),
            ("Dec 2007", "First IPO filing — financials public pre-JOBS Act"),
            ("2008–09", "IPO withdrawn amid financial crisis"),
            ("2011", "Private raise exceeds eventual IPO proceeds cited"),
            ("Mar 2012", "IPO at $19/share"),
            ("Jun 2013", "Salesforce acquires for $2.5B"),
            ("2013–16", "Scott Dorsey runs Marketing Cloud"),
            ("FY2016", "Marketing Cloud ~$654M revenue"),
            ("2016", "Acquired interview episode with Scott Dorsey"),
            ("2013", "SEC proxy documents Party A/B/C bids"),
        ]),
    },
}


def main() -> None:
    for ep_id, body in EPISODES.items():
        data = base(ep_id, **body)
        path = APPROVED / f"{ep_id}.json"
        path.write_text(json.dumps(data, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
        print(f"wrote {path.name}")


if __name__ == "__main__":
    main()
