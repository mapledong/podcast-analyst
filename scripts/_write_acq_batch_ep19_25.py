#!/usr/bin/env python3
"""Write Acquired v5.1 JSON for episodes 19–25 (early catalog batch)."""
from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))
APPROVED = ROOT / "data" / "approved"
DISCOVERED = json.loads((ROOT / "data" / "discovered" / "acquired_episodes.json").read_text())

LINKS_BASE = {
    "apple_podcasts": "https://podcasts.apple.com/podcast/acquired/id1050462261",
    "spotify": "https://open.spotify.com/show/2HI3KdjtJnr3E8B4W8Y0Yx",
}
META = {e["id"]: e for e in DISCOVERED["episodes"]}


def links(ep: dict) -> dict:
    return {
        "youtube": ep.get("youtube_url") or "",
        "acquired": ep["acquired_url"],
        **LINKS_BASE,
    }


def base(ep_id: str, **kwargs) -> dict:
    ep = META[ep_id]
    return {
        "episode_id": ep_id,
        "podcast": "Acquired",
        "host": "Ben Gilbert & David Rosenthal",
        "metadata": {
            "episode_number": ep["episode_number"],
            "title": ep["title"],
            "guest": ep["guest"],
            "guest_role": ep["guest_role"],
            "date": ep["date"],
            "duration_minutes": ep["duration_minutes"],
            "youtube_url": ep.get("youtube_url") or "",
            "links": links(ep),
        },
        "extraction_meta": {
            "model": "manual-gpt-agent-v5.1-acquired",
            "transcript_source": "acquired.fm",
            "status": "approved",
            "template_version": "5.1-acquired",
        },
        **kwargs,
    }


EPISODES: dict[str, dict] = {}

EPISODES["acq-episode-25-the-facebook-ipo"] = base(
    "acq-episode-25-the-facebook-ipo",
    episode_rating={"overall": 4},
    keywords=["Facebook IPO", "Mobile Monetization", "Sheryl Sandberg"],
    conclusion="Acquired's first IPO episode frames Facebook's May 2012 listing as a cultural touchstone that went wrong in the market but forced existential product fixes. Priced at $38 for a $104 billion market cap — third-largest U.S. IPO behind Visa and GM — Facebook was already printing money ($3.7 billion revenue, $1.7 billion operating income in 2011) yet disclosed mobile as a lethal S-1 risk with zero mobile ad revenue. The bungled NASDAQ open, Morgan Stanley's selective mobile guidance, and a 25% first-fortnight drawdown became Silicon Valley's cautionary tale about staying private. Zuckerberg and Sandberg responded by shipping a native iOS app and feed ads in one summer, taking mobile from 0% to 23% of ad revenue in Q4 2012 and eventually ~84% by 2016 — turning the 'fiasco' into the defining public-company pivot.",
    background="Ben and David pilot Acquired's IPO format with Facebook's May 2012 debut — the hottest technology listing ever, eight years after founding and after turning down Yahoo's $1 billion offer in 2006. Pre-IPO, SecondMarket and SharesPost traded employee shares, pushing Facebook toward the 500-shareholder rule; a Goldman special-purpose vehicle for wealthy clients backfired and killed Goldman's lead-left banker role.\n\nThe S-1 highlighted 3.2 billion daily likes and comments but flagged mobile as an uncapped risk — HTML5 apps lagged desktop engagement and carried no ads. During the roadshow Facebook bought Instagram for $1 billion (13 employees), amended filings amid mobile weakness, priced at $38, raised $16 billion, and watched bankers support a flat first-day close before a brutal selloff. The episode traces how crisis converted into native mobile ads and reset private-market IPO timing for a generation of unicorns.",
    important_facts=[
        "Facebook filed its S-1 February 1, 2012; priced May 17 at $38 per share for a $104 billion market cap — largest technology IPO and third-largest U.S. IPO at the time.",
        "2011 financials: $3.7 billion revenue and $1.7 billion operating income (~46% margin); Sheryl Sandberg built the ad platform from banner/Microsoft deals to scaled performance ads in roughly three years.",
        "S-1 risk factors cited 3.2 billion daily likes and comments (Q1 2012) but warned mobile usage without ads could hurt results; Zynga alone represented 15% of revenue.",
        "IPO sold 421 million shares, raising $16 billion; stock closed day one at $38.23, then lost ~25% of value within two weeks — roughly $25 billion of market cap erased.",
        "Q4 2012 mobile ads went from $0 to 23% of total ad revenue after a summer native-app push; by Q3 2016 mobile represented 84% of Facebook ad revenue.",
    ],
    mental_model={
        "name": "Crisis-Forced Platform Pivot",
        "components": "Public scrutiny converts disclosed 'risk factors' into operational mandates. Facebook's mobile gap was known internally but the IPO magnifying glass — flat pricing, lawsuits, and selective analyst briefings — made inaction impossible. Sandberg's ad infrastructure (built 2008–2011) gave monetization rails once product shipped; Instagram ($1 billion, April 2012) bought mobile-native engagement while the core app rebuilt.",
        "application": "When evaluating late-stage private companies, separate revenue scale from platform-transition risk. A profitable desktop franchise can mask zero mobile monetization until listing forces simultaneous product, disclosure, and banker-reputation crises — the fix may be faster post-IPO than pre-IPO because accountability spikes.",
    },
    competitive_advantage="Pre-IPO Facebook's moat was identity plus engagement density: billions of likes and comments on photos created a social graph competitors could not replicate quickly. Sheryl Sandberg imported Google's ad-stack discipline, turning low-quality banner inventory into a performance machine with 45%+ operating margins — rare for a private company at multi-billion revenue scale.\n\nWeaknesses were explicit in the S-1: HTML5 mobile strategy, fragmented feeds across devices, and Zynga platform concentration. The IPO process itself became a liability — Goldman SPV scrutiny, NASDAQ trading failures, and information asymmetry on mobile guidance damaged banker and exchange credibility.\n\nPost-crisis advantage compounded via native feed ads on mobile — a format competitors' banner-era products could not match. Instagram bolted photo-native behavior onto the graph. Lesson: network effects buy time, but monetization architecture must match the engagement surface; desktop ads do not port to mobile.",
    key_insights=[
        {
            "view": "The IPO flop forced the mobile fix that made Facebook.",
            "question": "Would a 'successful' pop have delayed mobile ads?",
            "answer": "Hosts argue a softer landing might have reduced urgency. The 25% drawdown and 'fiasco' press made mobile impossible to defer; Zuckerberg ran an all-summer native rebuild while bankers faced lawsuits. Counterfactual: lower pricing might have pleased day-one buyers but blunted the wakeup call that converted S-1 boilerplate into company-wide 'mobile is our future' propaganda.",
        },
        {
            "view": "SecondMarket trading created artificial IPO pressure.",
            "question": "Why couldn't Facebook stay private longer?",
            "answer": "Employee share sales on SecondMarket/SharesPost ballooned shareholder counts toward the 500-holder rule; illiquid secondary prints also anchored valuation expectations (Goldman round near $50 billion pre-IPO). JOBS Act passed during the roadshow — too late to relieve pressure. Lesson echoed in later unicorn secondary markets.",
        },
        {
            "view": "Instagram during the roadshow was mobile insurance.",
            "question": "Why pay $1 billion for 13 people mid-S-1?",
            "answer": "Photos drove core engagement; mobile shift threatened that wedge. Instagram was native-mobile and growing while Facebook's HTML5 app lagged. S-1 language promised standalone operation — unusual for a startup — underscoring regulatory sensitivity during registration.",
        },
        {
            "view": "Sandberg's COO hire was the revenue engine.",
            "question": "How did ads scale before IPO?",
            "answer": "Before March 2008 Facebook ran Microsoft banner deals with little in-house ad tech. Sandberg's charter: profitability via discrete ads, building targeting and auction mechanics akin to Google. Three years later: ~$4 billion revenue and ~$2 billion operating profit — the financial proof point that supported a $100 billion ask.",
        },
        {
            "view": "Facebook IPO reset private-market timelines.",
            "question": "What did founders learn — versus what Zuckerberg says?",
            "answer": "Industry absorbed 'don't go public'; Zuckerberg later argued listing forced maturity. Post-Facebook, Etsy (10 years), Shopify (11), Atlassian (13.5) stayed private longer while raising billions — Uber ~$11.5 billion pre-IPO cited. Paradox: disaster discouraged listings yet delayed accountability for mobile-era risks.",
        },
    ],
    top_investment_implications=[
        {
            "ticker": "META",
            "direction": "Watch",
            "confidence": "Medium",
            "thesis": "Episode documents origin of mobile feed ads and Instagram bolt-on — useful frame when judging whether new format shifts (Reels, AI recommendations) replicate 2012's platform transition under public scrutiny.",
        },
    ],
    golden_quotes=[
        "\"Betting on HTML5 over native in mobile\" — Zuckerberg at TechCrunch Disrupt 2012, cited as Facebook's biggest mistake.",
        "\"Mobile is our future\" — campus poster campaign during the post-IPO summer rebuild, per hosts.",
        "\"A cultural touchstone\" — Wikipedia's label for the Facebook IPO, quoted by Ben and David.",
    ],
    chronology={
        "subject": "Facebook · IPO & Mobile Pivot",
        "events": [
            {"date": "2004", "event": "Facebook founded at Harvard"},
            {"date": "2006", "event": "Yahoo $1 billion acquisition offer declined"},
            {"date": "2008-03", "event": "Sheryl Sandberg joins as COO; ad platform build begins"},
            {"date": "2010-11", "event": "SecondMarket/SharesPost employee share trading peaks"},
            {"date": "2012-02-01", "event": "S-1 filed; mobile risk and Zynga 15% revenue disclosed"},
            {"date": "2012-04-09", "event": "Instagram acquired for $1 billion during roadshow"},
            {"date": "2012-05-18", "event": "IPO prices at $38; NASDAQ trading failures; flat first-day close"},
            {"date": "2012-05", "event": "Stock loses ~25% in first two weeks; 'fiasco' narrative"},
            {"date": "2012-summer", "event": "Native iOS app and mobile feed ads developed"},
            {"date": "2012-Q4", "event": "Mobile ads reach 23% of ad revenue"},
            {"date": "2013", "event": "Zuckerberg disavows HTML5 mobile bet publicly"},
            {"date": "2016-Q3", "event": "Mobile ~84% of ad revenue per earnings cited on show"},
        ],
    },
    review_notes="Manual GPT Acquired batch ep19-25 — v5.1-acquired",
)

EPISODES["acq-episode-25-marvel"] = base(
    "acq-episode-25-marvel",
    episode_rating={"overall": 4},
    keywords=["Disney", "Marvel IP", "Franchise Flywheel"],
    conclusion="Disney's December 2009 $4.2 billion Marvel purchase completes the Pixar–Lucasfilm triumvirate and proves catalog IP can outperform Pixar's original content at the box office: first eight Marvel films post-deal grossed ~$6 billion versus ~$4.5 billion for Pixar's first eight, with higher theatrical profit (~$1.2 billion vs ~$600 million) though weaker home video. The episode traces Marvel from 1939 pulp origins through Perelman-era diversification, 1990s comic bubbles, Carl Icahn's bankruptcy, and Perlmutter-led studio bets that made the company acquirable. Disney gains 'action-hero' reach beyond princess animation while keeping Marvel creatively separate — a template Bob Iger used to convince Lucas and Jobs. Risk: sequel fatigue and superhero cycles may age like leisure suits; technology-enabled global distribution favors sure-thing tentpoles over originality.",
    background="Recorded remotely near Rogue One's release, Ben and David play Two Truths and a Lie (Icahn control and Fleer trading cards true; DC CEO owning Marvel false) before marching from Martin Goodman's 1939 Timely Publications and Marvel Comics #1 (~1 million copies) through Stan Lee's 1961 anti-hero tone, Ronald Perelman's 1989 $82.5 million buy, comic and baseball-card bubbles, 1996 bankruptcy, and Icahn's 'loan-to-own' control.\n\nFilm licensing accelerates in the 1990s–2000s; Marvel Studios' owned productions remake the asset. Disney pays ~$4.2 billion in 2009 — comparable to Lucasfilm's ~$4 billion — for 500+ characters (~50 mainstream). Hosts compare post-acquisition box office to Pixar, debate Disney's boy-demographic gap, and connect distribution-plus-content logic to Netflix, Facebook-Instagram, and Nintendo IP liberation.",
    important_facts=[
        "Marvel Comics #1 (October 1939) sold nearly 1 million copies; company renamed Marvel Comics in 1961 with Fantastic Four and edgier heroes versus DC.",
        "Ronald Perelman bought Marvel in 1989 for $82.5 million, took it public 1991, and expanded into Fleer trading cards and partial ToyBiz ownership before 1996 bankruptcy.",
        "Disney acquired Marvel in December 2009 for approximately $4.2 billion — completing a trilogy after Pixar (2006) and before Lucasfilm (2012, ~$4 billion).",
        "First eight Marvel films post-acquisition: ~$6 billion global box office and ~$1.2 billion theatrical profit; Pixar's first eight: ~$4.5 billion gross and ~$600 million profit.",
        "Marvel catalog held 500+ characters with roughly 50 recognizable to mainstream audiences at acquisition — far broader than Star Wars' concentrated franchise.",
    ],
    mental_model={
        "name": "Catalog IP × Distribution Flywheel",
        "components": "Decades-old characters become low-risk theatrical bets when global marketing and theme-park infrastructure amortize development costs. Disney buys latent IP, applies release-cadence discipline and consumer-products lift, and keeps creative labels separate to preserve edge (Marvel edgier than princess core). Perelman foreshadowed: Marvel as 'mini-Disney' in character marketing.",
        "application": "In media M&A, value scales with breadth of exploitable characters and control of sequel cadence — not just one franchise peak. Compare acquisition price to revenue per recognizable character and to downstream park/merchandise yield, not single-film ROI.",
    },
    competitive_advantage="Marvel's durable asset is serialized character IP with multi-decade nostalgia hooks — Spider-Man angst, Avengers ensemble economics — that survive publishing booms and busts. Post-bankruptcy, Perlmutter and Marvel Studios verticalized film production, capturing studio upside previously licensed away to Fox/Sony on key heroes.\n\nDisney added global marketing, ESPN/ABC cross-promotion, theme-park integration, and Bob Iger's reputation as steward (Lucas chose Disney; Jobs chose Pixar sale to Disney). Unlike Pixar, Marvel relies on third-party talent pools — more scalable but less artisanal.\n\nWeaknesses: theatrical bets cost hundreds of millions; flops like Tomorrowland hurt; superhero genre may be cyclical. Home video weakness vs Pixar ($400M vs $1.6B cited) shows theatrical skew. Tech leverage in film remains lower than software — 13-person Instagram vs Iron Man armies.",
    key_insights=[
        {
            "view": "Studios let Marvel accrue value by licensing away heroes.",
            "question": "Why wasn't Marvel acquired earlier?",
            "answer": "Fox and Sony enjoyed X-Men and Spider-Man economics without owning the corpus. Marvel Studios' owned-film strategy (post-2000s) internalized box office and made the parent company valuable. Disney moved when cadence + MCU planning proved repeatable.",
        },
        {
            "view": "Disney bought boys' attention, not just characters.",
            "question": "Why Marvel for princess-heavy Disney?",
            "answer": "Iger sought demographic balance — 'action heroes' versus princess animation. Marvel provided PG-13 tentpoles without contaminating core Disney brand; separate label preserved tone.",
        },
        {
            "view": "Breadth beat Star Wars on per-dollar film output.",
            "question": "Marvel vs Lucasfilm economics?",
            "answer": "~$4.2B vs ~$4B purchases but Marvel fields many parallel franchises (Iron Man, Thor, Cap) versus Star Wars' single saga. Hosts note Lucasfilm pushes spinoffs (Rogue One) to emulate Marvel seriality — harder with narrower canon.",
        },
        {
            "view": "Hollywood shifted from originals to sure-thing sequels.",
            "question": "Why fewer 1981-style original hits?",
            "answer": "1981 top-10: seven originals; today studios pour $200M into known IP because global instant distribution rewards lowest-variance bets. Creativity migrated to TV/YouTube; theaters are billion-dollar option exercises on nostalgia.",
        },
        {
            "view": "Technology raises stakes but not margins like software.",
            "question": "Can Marvel match tech leverage?",
            "answer": "Hosts contrast Facebook 45% operating margin expansion with ~23% film profit margins — technology companies compound with fewer heads; Marvel needs armies of creatives. IP flywheel is real but capital-intense.",
        },
    ],
    top_investment_implications=[
        {
            "ticker": "DIS",
            "direction": "Watch",
            "confidence": "Medium",
            "thesis": "Marvel remains core to Disney's theatrical and parks flywheel; monitor sequel-fatigue signals and box-office cadence versus streaming originals investment.",
        },
    ],
    golden_quotes=[
        "\"Marvel is a 'mini Disney' in terms of intellectual property\" — Ronald Perelman, 1989, quoted on the show.",
        "\"Carl Icahn is true, the Fleer thing is true\" — Two Truths and a Lie reveal on the cold open.",
        "\"You can't make Iron Man 3 with 13 people\" — Ben contrasting Marvel production scale with Instagram's value creation.",
    ],
    chronology={
        "subject": "Marvel · Disney Acquisition",
        "events": [
            {"date": "1939-10", "event": "Marvel Comics #1 published by Timely Publications"},
            {"date": "1941", "event": "Captain America debuts"},
            {"date": "1961", "event": "Fantastic Four; company renamed Marvel Comics"},
            {"date": "1986", "event": "Sold to New World Entertainment"},
            {"date": "1989", "event": "Ronald Perelman buys Marvel for $82.5 million"},
            {"date": "1991", "event": "Marvel goes public; expands into Fleer cards and ToyBiz"},
            {"date": "1996-12", "event": "Marvel files bankruptcy; Carl Icahn gains control"},
            {"date": "1997", "event": "Men in Black film — Marvel-licensed property hits mainstream"},
            {"date": "2000s", "event": "Marvel Studios produces owned films; MCU strategy forms"},
            {"date": "2009-12", "event": "Disney acquires Marvel for ~$4.2 billion"},
            {"date": "2012", "event": "Disney buys Lucasfilm for ~$4 billion — IP trilogy complete"},
        ],
    },
    review_notes="Manual GPT Acquired batch ep19-25 — v5.1-acquired",
)

EPISODES["acq-episode-24-skype"] = base(
    "acq-episode-24-skype",
    episode_rating={"overall": 4},
    keywords=["Skype", "VoIP", "Microsoft"],
    conclusion="Skype's journey — Kazaa founders, Estonian engineering, eBay's 2005 misfit purchase, Joltid licensing trap, Silver Lake's 2009 PE turnaround, and Microsoft's 2011 $8.5 billion acquisition — is Acquired's lesson in how great peer-to-peer technology can pass through multiple owners before strategic fit appears. Skype hit 10,000 downloads on day one (August 2003), 1 million users in month one, and ~20 million in year one with capital-efficient P2P architecture. eBay paid richly then kept core IP licensed from founders; the 2009 spinout at ~$2.75 billion and lawsuit settlement finally consolidated technology. Microsoft paid ~32× operating profit ($264 million on $860 million 2010 revenue) for 700 million users — rich, but hosts grade the saga as business-line and financial-engineering success despite narrative chaos.",
    background="Ben (ex-Microsoft, Talinn visitor) and David trace Skype from a 1999 Swedish Tele2 newspaper ad ($330/day) hiring Estonian PHP developers, through Kazaa's P2P dominance and legal scares, to 'Sky peer-to-peer' renamed Skype when Skyper.com was unavailable. Free VoIP around regulated telecom tariffs produced explosive growth; Bill Draper backed the Kazaa alumni on reputation alone.\n\neBay acquires Skype September 2005 hoping transaction verification synergies that never materialized; founders retain Joltid IP and license it back — repeating the Kazaa divestiture pattern. Culture clash (Estonia pool party on TV), 2007 write-down, 2009 PE consortium (Silver Lake, a16z) values Skype ~$2.75 billion; lawsuit yields 14% founder stake plus $85 million cash. Tony Bates modernizes mobile; Microsoft buys May 2011 for $8.5 billion — largest Microsoft deal until LinkedIn.",
    important_facts=[
        "Skype launched August 2003: 10,000 downloads day one, 1 million users in month one, 19.8 million users in year one — on peer-to-peer infrastructure with modest VC.",
        "eBay acquired Skype September 2005; founders kept core P2P technology in Joltid and licensed it to eBay — the same structure as the Kazaa sale.",
        "Q3 2009 Skype revenue $185 million; user base exceeded 500 million by spinout time while eBay faced Wall Street pressure to divest.",
        "2009 private-equity spinout valued Skype at ~$2.75 billion; settlement gave Zennström/Friis ~14% of Skype plus $85 million cash.",
        "Microsoft acquired Skype May 2011 for $8.5 billion; 2010 full-year $860 million revenue and $264 million operating profit (~700 million users) — ~32× operating profit.",
    ],
    mental_model={
        "name": "IP Ownership in Roll-up Acquisitions",
        "components": "Founders sell 'company' but retain core technology in a side entity, licensing back — creating renegotiation leverage at every subsequent transaction. Acquirers get brand and users, not full stack; spinouts and PE turns become litigation-heavy cleanup before strategic buyers (Microsoft) pay full price.",
        "application": "In tech M&A diligence, map legal ownership of protocols and patents separately from consumer brand. Assume founders of P2P/crypto/networking startups may replicate Kazaa/Skype/Joltid structures — price deals on owned IP only.",
    },
    competitive_advantage="Skype won on simplicity and economics: free/cheap international voice riding P2P supernodes, bypassing telecom minute pricing. Estonian engineering culture (Bill Draper bet on team) and Kazaa-era distributed systems know-how enabled scale without proportional data-center spend.\n\neBay and Microsoft phases added mobile push (iOS/Android) and enterprise distribution — Skype became a verb for video calls. PE interlude under Tony Bates integrated long-separated tech and prepared mobile roadmap.\n\nWeaknesses: text-first messaging rivals later dominated; eBay synergy fiction; repeated ownership fractures. Microsoft paid strategic premium vs cash flow — integration into Office/Lync ecosystem justified politically more than DCF.",
    key_insights=[
        {
            "view": "Licensing core tech is a time bomb.",
            "question": "Why did eBay 'succeed' financially anyway?",
            "answer": "Narrative focuses on misfit; eBay retained ~30% through spinout and recouped ~purchase price on Microsoft's sale. Skype was fast-growing and profitable throughout — wrong owner, not bad business.",
        },
        {
            "view": "PE turnaround was the value-creation leg.",
            "question": "Who deserves A+ credit?",
            "answer": "Silver Lake/a16z 2009–2011: settled Joltid suit, merged IP, mobile focus, hired Tony Bates — ~$6 billion value jump in under two years before Microsoft paid $8.5 billion.",
        },
        {
            "view": "P2P was capital-efficient growth.",
            "question": "How did 20M users need little VC?",
            "answer": "Peer bandwidth offset centralized CDN costs at 2003 scale; viral Kazaa alumni reputation unlocked Draper/Hartenbaum funding without business plan scrutiny.",
        },
        {
            "view": "Microsoft bought users, not eBay synergy.",
            "question": "Strategic rationale in 2011?",
            "answer": "700M users, enterprise comms overlap (Lync), Ballmer-era consumer reach; 32× operating profit rich but defensible vs building global VoIP graph from scratch.",
        },
        {
            "view": "Same founders, same playbook thrice.",
            "question": "Pattern across Kazaa, Skype, Rdio?",
            "answer": "Zennström/Friis: build P2P product, sell label not tech, reinvest proceeds, litigate when buyers need IP — then Joost/Rdio follow-ons. Acquirers must buy protocols outright early.",
        },
    ],
    top_investment_implications=[
        {
            "ticker": "MSFT",
            "direction": "Watch",
            "confidence": "Low",
            "thesis": "Skype DNA lives in Teams; episode helps judge whether comms assets are judged on user graph strategic value vs standalone profitability.",
        },
    ],
    golden_quotes=[
        "\"Dropped Skype's wiener\" — Ben on shortening Skyper to Skype when the domain was taken.",
        "\"What happens in Estonia stays in Estonia!\" — Niklas Zennström at the eBay management party, per press retelling.",
        "\"Third time is the charm for Skype\" — Ben on Microsoft finally buying the full cap table.",
    ],
    chronology={
        "subject": "Skype · Ownership Journey",
        "events": [
            {"date": "1999", "event": "Tele2 hires Estonian developers via newspaper ad"},
            {"date": "2000-09", "event": "Kazaa launches; becomes world's most popular app briefly"},
            {"date": "2002-03", "event": "Sky peer-to-peer / Skype alpha; protocol work begins"},
            {"date": "2003-08", "event": "Skype launches publicly; 10K day-one downloads"},
            {"date": "2005-06", "event": "Video calling added"},
            {"date": "2005-09", "event": "eBay acquires Skype; Joltid licenses core IP"},
            {"date": "2007-10", "event": "eBay writes down Skype value"},
            {"date": "2009", "event": "PE spinout at ~$2.75B; Joltid lawsuit settled"},
            {"date": "2010-10", "event": "Tony Bates named CEO"},
            {"date": "2011-05", "event": "Microsoft acquires Skype for $8.5 billion"},
        ],
    },
    review_notes="Manual GPT Acquired batch ep19-25 — v5.1-acquired",
)

EPISODES["acq-episode-23-next-live-show-at-the-geekwire-summit"] = base(
    "acq-episode-23-next-live-show-at-the-geekwire-summit",
    episode_rating={"overall": 5},
    keywords=["NeXT", "Apple", "Steve Jobs"],
    conclusion="Apple's 1996–97 $429 million NeXT acquisition — plus ~1.5 million Apple shares to Jobs — is the definitive people-plus-technology deal: Gil Amelio's slide deck literally listed 'Steve Jobs' as the rationale. NeXTSTEP brought Objective-C, networking, and GUI heritage Xerox PARC previewed; the World Wide Web was invented on a NeXT machine. Hardware failed (50,000 cubes at $10,000), but the 2001 ship of Mac OS X, then iPod, iPhone, and iPad on a shared Darwin kernel, traces to this purchase. Jobs returned as interim CEO within a year, fired 70% of product lines, and turned a $1B loss into profit. Hosts grade it the greatest acquisition of all time — trillions of downstream market cap from a modest exit that barely returned venture capital.",
    background="Recorded live at GeekWire Summit (Episode 23), Ben and David tell NeXT from Jobs's 1985 exile after the SuperMicro/BigMac workstation fight through Paul Rand's $100K logo, I. M. Pei offices, transparent salaries, and 1988 gala launch (violin duet with a $10K cube). NeXT pivots to software-only in 1993; WebObjects and Dell's e-commerce site show enterprise traction while Apple flails on Copland/Gershwin OS projects.\n\nDecember 1996: Apple buys NeXT for $429 million (BeOS was alternative but price failed). Acquisition closes February 1997; Jobs becomes advisor, ousts Amelio July 4 weekend, becomes interim CEO September 1997. OS X ships 2001 — five years post-deal. Live audience hears why Amelio expected OS integration in 1997 while Jobs preached focus and killing OpenDoc.",
    important_facts=[
        "NeXT sold roughly 50,000 workstations total at ~$10,000 each — hardware pivot to software-only followed in 1993.",
        "Tim Berners-Lee invented the World Wide Web in 1990 on a NeXT computer at CERN — enabled by object-oriented programming and networking on NeXTSTEP.",
        "Apple acquired NeXT December 1996 for $429 million cash plus stock grants including ~1.5 million Apple shares to Steve Jobs.",
        "Mac OS X shipped in 2001 — about five years after close; iPhone launched 2007 running a variant described as OS X on stage.",
        "Jobs became interim CEO September 1997; Apple had lost over $1 billion in the prior year before returning to profitability under his reset.",
    ],
    mental_model={
        "name": "Failed Startup as OS Insurance",
        "components": "When platform companies cannot ship next-gen OS internally (politics + technical debt), buying a small team with proven UNIX/OO foundation beats greenfield. NeXT's price was modest because hardware failed; Apple's urgency (Copland collapse) transferred option value to acquirer. Founder return multiplies integration speed.",
        "application": "Assess struggling platform owners for external OS/kernel acquisitions — value is time-to-ship and architect continuity, not target revenue. Jobs's slide at Macworld ('Steve Jobs') is the honest scoring rubric.",
    },
    competitive_advantage="NeXT's technical advantage was integrating three Xerox PARC insights Apple originally missed: GUI, object-oriented development (Objective-C), and networking — enabling rapid app ecosystems and web-era infrastructure (WebObjects, WWW origin). Vertical hardware failed on price and PMF, but software licensing to Dell and others proved portability.\n\nApple's post-acquisition advantage: single integrated stack from kernel to Interface Builder, decade-long developer continuity into iOS, and Jobs's focus discipline ('say no') clearing SKUs. BeOS alternative at $300M ask vs $125M Apple bid underscores NeXT's unique founder premium.\n\nWeakness during standalone era: extravagant burn (I. M. Pei offices, early announcements missing dates) — scars that shaped modern Apple's secrecy and supply-chain precision.",
    key_insights=[
        {
            "view": "People acquisition was the honest thesis.",
            "question": "Why NeXT over BeOS?",
            "answer": "Be wanted ~$300M vs Apple's ~$125M willingness; NeXT had Jobs, proven Obj-C toolchain, and enterprise ports. Amelio's public slide listed Steve as rationale — rare corporate candor.",
        },
        {
            "view": "OS timelines always slip — plan in years.",
            "question": "Why not ship OS X in 1997?",
            "answer": "Amelio promised 1997 integration; reality was 2001. Deep kernel swap plus Jobs's product massacre (OpenDoc killed at WWDC 1997) required half-decade bake — lesson for any 'just bolt on' platform M&A.",
        },
        {
            "view": "NeXT DNA persists in every Apple device.",
            "question": "What survived into iPhone?",
            "answer": "Darwin kernel, Objective-C heritage (Swift successor), Interface Builder lineage — Apple marketed iPhone as 'real OS X' to signal desktop-class ambitions BlackBerry dismissed.",
        },
        {
            "view": "Web was invented on the 'failed' machine.",
            "question": "Why does NeXT matter beyond Apple?",
            "answer": "Berners-Lee's WWW on NeXTSTEP validated OO + network stack for knowledge work — cultural proof that NeXT's ideas were right while retail hardware was wrong.",
        },
        {
            "view": "Greatest acquisition benchmark.",
            "question": "How do hosts grade versus Instagram?",
            "answer": "NeXT underpins trillion-dollar Apple market cap; Instagram is photo-mobile benchmark — hosts argue NeXT may be 'greatest of all time' on value created per dollar paid.",
        },
    ],
    top_investment_implications=[
        {
            "ticker": "AAPL",
            "direction": "Watch",
            "confidence": "Medium",
            "thesis": "NeXT explains Apple's integrated OS moat; relevant when judging whether visionOS and future platforms reuse the same kernel-and-tools consolidation playbook.",
        },
    ],
    golden_quotes=[
        "\"When I went to Xerox PARC in 1979… I was so blinded by the GUI I didn't find out about object-oriented programming and networking\" — Jobs, quoted on the show.",
        "\"A $2 billion company with 4,300 people couldn't compete with six people in blue jeans\" — Jobs Newsweek quote after leaving Apple.",
        "\"Reasons we acquired NeXT: Steve Jobs\" — Gil Amelio slide, cited live at GeekWire.",
    ],
    chronology={
        "subject": "NeXT · Apple Acquisition",
        "events": [
            {"date": "1984", "event": "Jobs leads SuperMicro division; BigMac workstation project"},
            {"date": "1985-09", "event": "Jobs resigns; founds NeXT two weeks later"},
            {"date": "1986-01", "event": "Settlement with Apple; NeXT cannot compete directly"},
            {"date": "1988", "event": "NeXT computer gala launch — $10,000 cube"},
            {"date": "1990", "event": "World Wide Web invented on NeXT at CERN"},
            {"date": "1993", "event": "NeXT exits hardware; focuses on NeXTSTEP software"},
            {"date": "1996-12", "event": "Apple agrees to buy NeXT for $429 million"},
            {"date": "1997-02", "event": "Deal closes; Jobs advisor"},
            {"date": "1997-07", "event": "Amelio ousted; Jobs interim CEO path begins"},
            {"date": "1997-09", "event": "Jobs named interim CEO"},
            {"date": "2001", "event": "Mac OS X ships"},
            {"date": "2007", "event": "iPhone launches — described as running OS X variant"},
        ],
    },
    review_notes="Manual GPT Acquired batch ep19-25 — v5.1-acquired; GeekWire live",
)

EPISODES["acq-episode-22-zillow-trulia-with-zillow-group-cfo-kathleen-philips"] = base(
    "acq-episode-22-zillow-trulia-with-zillow-group-cfo-kathleen-philips",
    episode_rating={"overall": 3},
    keywords=["Zillow", "Real Estate", "Aggregation"],
    conclusion="Zillow's 2015 stock-for-stock Trulia merger — negotiated from a 30% opening offer to ~33% of the combined company — doubled down on Premier Agent aggregation: more eyeballs on listings, more agents buying ads. CFO Kathleen Philips details three years of failed private/public valuation talks, shareholder NDAs, a $150 million breakup fee, dual FTC information requests, and ListHub cutting MLS feeds right before close. Hosts grade execution A+ but strategic outcome B/B+: traffic rose ~one-third for ~one-third of market cap — sensible, not Instagram. Rich Barton's 'information people crave' thesis (Zestimate obsession) and real-estate-as-entertainment explain why millennials 'live on Zillow' while most transactions remain offline.",
    background="Guest Kathleen Philips (CFO, ex-COO/GC, corp dev lead) walks through Zillow and Trulia's parallel origins, failed 2011–2012 merger talks (Catalyst advised Trulia pre-IPO), and 2014 shareholder soundings before Rich Barton emailed Trulia CEO Pete Flint. June–July 2015: offer at 30% Zillow stock, counter 37%, settled ~33% with $33 million Trulia management retention and no-go-shop tension.\n\nTrulia co-founder Sami Inkinen rowed the Pacific during negotiations. FTC took six months with two RFIs — rare negative signal. Post-approval, News Corp's ListHub cut data feeds, forcing direct MLS deals nationwide. Brands stay separate; Premier Agent ads unify backend. Ben/David cite Ben Thompson aggregation theory; Kathleen outlines bolt-on acquisitions (HotPads, Naked Apartments) for traffic and agent tools.",
    important_facts=[
        "Zillow IPO market cap was roughly $600–700 million — among first Seattle tech IPOs in years; Trulia IPO followed September 2012 after talks broke down twice.",
        "July 2015 merger terms converged near 33% Zillow stock for Trulia after opening at 30% and a 37% counter — announced July 28, 2015.",
        "Breakup fee: $150 million; Trulia management retention package: $33 million in equity.",
        "FTC review lasted ~6 months with 2 formal information requests — uncommon dual-RFI pattern spooked markets.",
        "Hosts estimate combined traffic boost ~one-third for ~one-third of combined market cap — execution strong, not a 10× outcome.",
    ],
    mental_model={
        "name": "Aggregation in Thin Online Penetration",
        "components": "Real estate transacts mostly offline; online portals aggregate demand (home shoppers) and sell access to supply-side agents (Premier Agent). Combining #1 and #2 increases ad surface without immediate product merge — classic horizontal roll-up when category TAM is huge but online share tiny.",
        "application": "In marketplace M&A, when offline share dominates, pay with stock near proportional traffic contribution and keep brands until agent products unify — antitrust and data-feed politics matter as much as price.",
    },
    competitive_advantage="Zillow's edge is Zestimate-driven habit loops — homeowners and renters refresh values weekly (Rich Barton 'mouse in lab' metaphor). Trulia brought overlapping audience and SEO strength. Combined entity pressures MLS data access and agent ad budgets; Premier Agent bundles impressions across properties (Zillow, Trulia, HotPads).\n\nPhilips's dual GC/corp-dev/people role enabled six-week close discipline. Weaknesses: ListHub dependency exposed; FTC scrutiny on duopoly; millennials browse but older cohorts still close offline — generation gap in transaction completion.",
    key_insights=[
        {
            "view": "Public stock unlocks merger math.",
            "question": "Why wait until both were public?",
            "answer": "Private mergers stall on valuation opacity; public comps and trading prices let 30–37% stock ranges converge quickly — Kathleen cites years of failed pre-IPO talks.",
        },
        {
            "view": "Brands stay separate by design.",
            "question": "Why not merge sites day one?",
            "answer": "Distinct consumer bases and SEO; integration on agent monetization first. Trulia leadership retention ($33M) assumes ongoing standalone operation.",
        },
        {
            "view": "Antitrust language in pitch decks matters.",
            "question": "Why two FTC RFIs?",
            "answer": "Defining 'market' as online listings made Zillow+Trulia look duopolistic; regulators subpoenaed history — startup bravado about 'taking over' can extend reviews.",
        },
        {
            "view": "Data supply is the real moat battle.",
            "question": "What was ListHub shock?",
            "answer": "News Corp's Move.com-owned ListHub cut feeds pre-close — forcing hundreds of direct MLS agreements. Distribution aggregation without listing data is fragile.",
        },
        {
            "view": "Real estate listings are media.",
            "question": "Why do non-buyers use Zillow?",
            "answer": "Aspirational browsing ('house porn') creates ad inventory against homes as content — same aggregation logic as Facebook/Google but monetized via agents.",
        },
    ],
    top_investment_implications=[
        {
            "ticker": "Z",
            "direction": "Watch",
            "confidence": "Medium",
            "thesis": "Episode frames Zillow as Premier Agent roll-up in low online penetration; useful when modeling iBuyer pivots against core ad marketplace economics.",
        },
        {
            "ticker": "RDFN",
            "direction": "Watch",
            "confidence": "Low",
            "thesis": "FTC market definition and MLS feed politics affect all portals — competitive dynamics post-Trulia inform Redfin's vertically integrated bet.",
        },
    ],
    golden_quotes=[
        "\"What piece of marketplace information do people crave and don't have?\" — Rich Barton, NYT interview, via David.",
        "\"Mr. Flint indicated that his near-term schedule would not accommodate a dinner\" — SEC filing tone on opening contact, read on air.",
        "\"Sami Inkinen was literally in a rowboat… across the Pacific\" — during the entire negotiation, per David.",
    ],
    chronology={
        "subject": "Zillow · Trulia Merger",
        "events": [
            {"date": "2011", "event": "Zillow IPO; first Trulia merger talks fail"},
            {"date": "2012-09", "event": "Trulia IPO after second failed Zillow talks"},
            {"date": "2014-spring", "event": "Zillow consults major shareholders under NDA"},
            {"date": "2015-06", "event": "Rich Barton emails Pete Flint; dinner deferred"},
            {"date": "2015-07-05", "event": "~33% stock ratio agreed"},
            {"date": "2015-07-28", "event": "Merger announced"},
            {"date": "2015", "event": "FTC issues two information requests"},
            {"date": "2015-07", "event": "No-go-shop and 33% ratio negotiations intensify"},
            {"date": "2016-02", "event": "FTC clears deal; close follows"},
            {"date": "2016", "event": "ListHub cuts feeds; direct MLS rebuild begins"},
            {"date": "2016+", "event": "Premier Agent portal unified across Zillow and Trulia brands"},
        ],
    },
    review_notes="Manual GPT Acquired batch ep19-25 — v5.1-acquired; guest episode",
)

EPISODES["acq-episode-21-inside-the-ma-press-with-bloombergs-alex-sherman"] = base(
    "acq-episode-21-inside-the-ma-press-with-bloombergs-alex-sherman",
    episode_rating={"overall": 3},
    keywords=["Bloomberg", "M&A Press", "Terminals"],
    conclusion="Acquired's meta-episode with Bloomberg's Alex Sherman explains why deal coverage looks the way it does: terminals (~$25,000/year) monetize speed and accuracy for traders, not pageviews — so 'people familiar with the matter' encodes sourcing discipline, redheaded headlines move markets in seconds, and retrospective 'did it work' stories rarely run because post-close analysis is not actionable. Sherman describes Bloomberg's Chinese-wall separation between terminals and newsroom, preference for both-sides sourcing on deals, and why splashy rumors (Apple–McLaren) get killed while verified Verizon–Yahoo threads publish. For founders, the playbook is relationships before you need them; for listeners, Acquired itself occupies the story-driven retrospective gap mainstream M&A press skips.",
    background="Episode 21 breaks Acquired's acquisition format to interview Alex Sherman (Bloomberg Deal of the Week; NY HQ since 2008 intern). David opens with Bloomberg LP history: 1981 founding, Merrill Lynch's 1983 $30 million for 30% (later repurchased 2008), terminal business as Wall Street's OS long before smartphones.\n\nConversation covers incentive alignment (truth over hype), coded bylines, algorithmic data feeds on red headlines, Friday 'take out the trash' dump timing, and why Instagram follow-ups (500K advertisers) still make news but post-merger grades do not. Hot takes include Disney–Twitter rumor (Sherman broke dual-side talks), Ford–Chariot vs GM–Cruise, and media business-model contrasts (WSJ paywall vs terminal subsidy).",
    important_facts=[
        "Bloomberg Terminal subscriptions cost on the order of ~$25,000 per year — core revenue engine subsidizing newsroom operations.",
        "Merrill Lynch invested $30 million for 30% of Bloomberg in 1983; Bloomberg repurchased the stake after Bank of America acquired Merrill in 2008.",
        "Instagram reported 500,000+ active advertisers — up from 200,000 in February — in follow-up segment citing recent announcement.",
        "Amazon share price referenced at ~$800 in follow-up (2016 recording) — Seattle economic spillover context.",
        "Ford acquired Chariot (San Francisco shuttle subscription ~$100/month) — contrasted with GM's Cruise autonomous bet.",
    ],
    mental_model={
        "name": "Terminal-Subsidized Truth",
        "components": "When customers pay five figures annually for milliseconds of advantage, newsroom incentives favor precision and dual confirmation — opposite of ad-CPM media chasing clicks. 'People familiar' signals sourcing tier; red headline triggers data feeds and trading algorithms instantly.",
        "application": "Read deal leaks through incentive lens: terminal-driven outlets underplay unverified splash; ad-driven outlets overplay. For corporate comms, Friday dumps and conflicting mega-deals hide smaller stories.",
    },
    competitive_advantage="Bloomberg's moat is terminal network effects — chat, trading, analytics on proprietary hardware — making journalism a retention feature rather than profit center. Breaking M&A moves terminal value in seconds (Sherman: 15 minutes is 'an eternity'). Chinese walls between news and terminals preserve credibility with paying users.\n\nWeakness vs creator ecosystems: individual journalists (Kara Swisher) lack redhead distribution unless bundled; social platforms resist paywalls because network effects break when sources leave. Acquired competes on narrative depth where Bloomberg optimizes timeliness.",
    key_insights=[
        {
            "view": "Post-close M&A analysis is a market failure.",
            "question": "Why no 'did it work' pieces?",
            "answer": "News dollars follow actionable moments — announce, break, close — not vegetables. Trade publications could fill gap; Acquired's listener base proves appetite for retrospective stories when drama exists (Snapchat spurned Facebook).",
        },
        {
            "view": "Coded language is insider API.",
            "question": "What does 'people familiar' mean?",
            "answer": "Signals sourced conversation, not document scrape; competitors parse bylines to infer which side leaked. Yahoo–Verizon coverage became case study.",
        },
        {
            "view": "Bloomberg kills wolf-cry rumors.",
            "question": "Why skip Apple–McLaren?",
            "answer": "Terminal brand punishes false positives; customers pay for accuracy. Incentive to downplay rivals' hype if own reporting stays conservative.",
        },
        {
            "view": "Friday is the rug-sweep day.",
            "question": "When to hide small M&A?",
            "answer": "Companies bury announcements ahead of mega-deals (Verizon week) — journalists know pattern; founders should expect lower scrutiny Fridays, not invisibility.",
        },
        {
            "view": "Stories beat news for podcasts.",
            "question": "Why Acquired's Snapchat episode endures?",
            "answer": "Drama and counterfactual narrative (Facebook owning Snapchat) attract non-M&A listeners; Sherman agrees anniversary features could work in text — validates Acquired's story-first format.",
        },
    ],
    top_investment_implications=[
        {
            "ticker": "MC",
            "direction": "Watch",
            "confidence": "Low",
            "thesis": "Terminal-model durability underpins Bloomberg LP; episode informs how private terminal peers might price news vs data bundles.",
        },
    ],
    golden_quotes=[
        "\"15 minutes is an eternity\" — David on algorithmic trading reaction time vs publishing speed.",
        "\"Your incentives are aligned with the truth\" — David summarizing terminal subscriber model.",
        "\"People, Ben. People. Not person.\" — Ben correcting dual-source Disney–Twitter reporting crediting Sherman.",
    ],
    chronology={
        "subject": "Bloomberg · Media & M&A Coverage",
        "events": [
            {"date": "1981", "event": "Michael Bloomberg founds Innovative Market Systems"},
            {"date": "1983", "event": "Merrill Lynch invests $30M for 30% stake"},
            {"date": "2008", "event": "Alex Sherman joins Bloomberg as intern"},
            {"date": "2008", "event": "Bloomberg buys Merrill's stake post-financial crisis"},
            {"date": "2012", "event": "Facebook IPO coverage era referenced"},
            {"date": "2016", "event": "Instagram 500K advertisers milestone cited"},
            {"date": "2016", "event": "Disney–Twitter talks reported by Sherman"},
            {"date": "2016", "event": "Ford buys Chariot; GM bought Cruise earlier"},
            {"date": "2016", "event": "Yahoo breach surfaces during Verizon deal scrutiny"},
            {"date": "2016", "event": "Acquired Android episode approaches Snapchat download popularity"},
        ],
    },
    review_notes="Manual GPT Acquired batch ep19-25 — v5.1-acquired; meta press episode",
)

EPISODES["acq-episode-20-android"] = base(
    "acq-episode-20-android",
    episode_rating={"overall": 5},
    keywords=["Android", "Google", "Mobile Platform"],
    conclusion="Google's 2005 ~$50 million Android acquisition — Andy Rubin's Danger/General Magic lineage, Steve Perlman's $10,000 cash infusion, no VC — became the defensive moat protecting Search from mobile distribution taxes. After January 2007 iPhone, Google scrapped the HTC non-touch prototype, launched Open Handset Alliance November 2007, and shipped the G1 in 2008. Oracle lawsuit disclosures cited ~$31 billion Android revenue and ~$22 billion profit; hosts estimate Android saves ~$4 billion yearly by avoiding ~34% traffic-share payments Apple extracts for default mobile search. Open-source AOSP plus Google Play/services bundle created 80% global share and fork pressure (Amazon, Xiaomi). David Lawee called it Google's best deal; hosts grade A+ alongside Instagram — defensive but existential.",
    background="Requested for months, Episode 20 unpacks Android pre-iPhone: Rubin leaves Danger 2003, builds Linux-based mobile OS; Larry/Sergey were Sidekick fans. Google buys 2005 before iPhone exists. January 2007 iPhone keynote forces full UI reset; November 2007 OHA announcement with $10M developer challenge; 2008 G1 (T-Mobile/HTC) trails iPhone but Verizon's 2009 Droid campaign (Lucasfilm 'droid' fee) ignites holy wars.\n\nEpisode links Motorola $12.5B patent buy (sold to Lenovo $2.9B), Oracle Java API suit revealing Apple–Google search rev-share (~34%), and Ben Thompson 'own the customer' theme. Eric Schmidt on Apple's board through 2007 — friendship to warfare in two years.",
    important_facts=[
        "Google acquired Android in 2005 for approximately $50 million; Andy Rubin had not raised VC — Steve Perlman once delivered $10,000 cash refusing equity.",
        "January 2007 iPhone launch triggered Android prototype scrap; Open Handset Alliance announced November 2007 with $10 million developer challenge.",
        "First Android phone (G1) shipped 2008 with HTC/T-Mobile; Verizon Droid campaign 2009 paid Lucasfilm for 'droid' trademark use.",
        "Oracle lawsuit cited ~$31 billion annual Android revenue and ~$22 billion profit; ~$15 billion mobile search revenue 2015 with Apple taking ~34% of iOS search.",
        "Hosts estimate Android's ~80% share avoids ~$4 billion per year in traffic-share payouts Google would owe if mobile search ran through others' browsers.",
    ],
    mental_model={
        "name": "Search Tax Avoidance via OS",
        "components": "Google monetizes attention on owned surfaces. Mobile inserted carriers/OEMs/browser defaults between users and AdWords; Apple extracts ~34% of iOS search revenue. Android gives Google default search on ~80% of phones — economic value is defensive rent capture, not Play Store margin alone.",
        "application": "Evaluate 'free' OS/product subsidies by quantifying avoided tolls on core cash engine. Android's ROI is tax saved plus Play 30% cut — compare to $50M entry vs building in-house without Rubin/OHA coalition.",
    },
    competitive_advantage="Android won via open coalition: free AOSP united OEMs/carriers against Apple exclusivity (AT&T/iPhone rocket). Developer reach argument pressured Apple to App Store in 2008. Samsung and others copied fast; Google controlled GMS bundle (Maps, Play, Gmail) on licensed builds.\n\nRubin's handset DNA (Danger Sidekick) and post-iPhone pivot speed mattered. Weaknesses: fragmentation, fork risk (Xiaomi, Fire OS), Motorola patent detour. Microsoft Windows Mobile lost because product sucked and coalition closed — lesson in UX-first plus open distribution.",
    key_insights=[
        {
            "view": "Android exists to protect AdWords.",
            "question": "Why give OS away free?",
            "answer": "Mobile reopened distribution tolls; Apple–Google revenue share (~$1B/year order-of-magnitude) shows cost of not owning front door. Chrome and Android share thesis — prevent taxing own users.",
        },
        {
            "view": "iPhone reset saved Android from irrelevance.",
            "question": "What if no iPhone?",
            "answer": "Pre-touch QWERTY prototypes would have lost slowly; iPhone forced parity chase and OHA narrative ('open vs closed') that recruited OEMs.",
        },
        {
            "view": "Eric Schmidt board seat was strategic intel.",
            "question": "Did Google know iPhone plans?",
            "answer": "Schmidt on Apple board until 2007; still, hosts argue exact smartphone war outcome unforeseeable — acquisition was talent/optionality bet that compounded.",
        },
        {
            "view": "Play Store is bonus revenue.",
            "question": "How else does Android pay?",
            "answer": "~30% Play cut on ~$10–15B of gross cited in lawsuit math — great on $50M purchase, but defensive search rent dominates.",
        },
        {
            "view": "A+ defensive can equal offensive Instagram.",
            "question": "Why grade as highly as Instagram?",
            "answer": "Ben: ensured Google customer access for decades; David wavers on '+' only because Instagram felt offensive — both existential to core business.",
        },
    ],
    top_investment_implications=[
        {
            "ticker": "GOOGL",
            "direction": "Long",
            "confidence": "Medium",
            "thesis": "Android economics explain mobile search margin structure; relevant when DOJ/remedy debates threaten default search bundles on Android OEMs.",
        },
    ],
    golden_quotes=[
        "\"If Google did not act, we faced a draconian future… one man, one company, one device\" — Vic Gundotra at Google I/O 2010, quoted by David.",
        "\"Google's best deal ever\" — David Lawee attribution on the acquisition.",
        "\"Droid Does\" — Verizon campaign paying Lucasfilm for every 'droid' mention.",
    ],
    chronology={
        "subject": "Android · Google Acquisition",
        "events": [
            {"date": "2003", "event": "Andy Rubin leaves Danger; starts Android"},
            {"date": "2005", "event": "Google acquires Android (~$50M)"},
            {"date": "2007-01", "event": "iPhone announced; Android prototypes scrapped"},
            {"date": "2007-11", "event": "Open Handset Alliance and Android announced"},
            {"date": "2008", "event": "G1 phone ships; Apple App Store walks back web-only apps"},
            {"date": "2009", "event": "Verizon Droid campaign vs iPhone"},
            {"date": "2011-08", "event": "Google buys Motorola Mobility for $12.5B (patents)"},
            {"date": "2014", "event": "Motorola sold to Lenovo for $2.9B"},
            {"date": "2010", "event": "Vic Gundotra frames Android as anti-monopoly hammer vs Apple"},
            {"date": "2011+", "event": "Oracle Java API lawsuit reveals mobile search economics"},
            {"date": "2016", "event": "Hosts grade Android A+ — 'Google's best deal ever' per Lawee"},
        ],
    },
    review_notes="Manual GPT Acquired batch ep19-25 — v5.1-acquired",
)

EPISODES["acq-episode-19-jet"] = base(
    "acq-episode-19-jet",
    episode_rating={"overall": 3},
    keywords=["Walmart", "Jet.com", "Marc Lore"],
    conclusion="Walmart's August 2016 $3.3 billion Jet.com deal ($3 billion cash, $300 million retention) bought Marc Lore's e-commerce playbook after his Quidsi/Diapers.com history — Amazon paid $545 million in 2010 after price-war coercion while Walmart had also bid. Jet raised $220 million pre-launch, dropped its $50/year Costco-style membership after three months, and touted 2 million customers and $90 million May 2016 revenue — growth without proven unit economics. Hosts categorize primarily people-plus-technology: urban millennials Jet attracted versus Walmart's Sears-like demographic, dynamic pricing cart incentives, and aggregation theory's winner-take-all online retail. Grade lands middling — bold Walmart defense against Amazon, but hard to imagine a durable #2 in U.S. e-commerce.",
    background="Episode 19 responds to listener demand on Walmart–Jet (record requests). David opens with Marc Lore's 2005 Quidsi/Diapers.com — Bezos school-picnic meeting, Amazon price war, defensive acquisition to block Walmart. Lore exits 2013 criticizing Amazon 'burnout culture,' launches Jet Hoboken 2014 with $80M seed (extraordinary trust) plus $140M pre-launch ($220M total).\n\nJuly 2015 launch: subway ads, 350K insider members, membership model killed October 2015. November 2015 $350M round; December 2M customers and $33M December revenue; May 2016 $90M monthly revenue. Fortune interview questions winner-take-all thesis. Walmart buys August 8, 2016; Lore to run Walmart.com. Tech themes: Ben Thompson aggregation, urban vs suburban retail, Amazon Seattle campus vs Walmart legacy.",
    important_facts=[
        "Amazon acquired Quidsi/Diapers.com in 2010 for $545 million after aggressive price competition; Walmart had also bid.",
        "Jet raised $80 million seed (2014) and $140 million more pre-launch — $220 million before selling a single item.",
        "Launch July 21, 2015 with ~$50/year membership (half of Prime); membership fee dropped October 2015 (~3 months later).",
        "December 2015: 2 million active customers and $33 million December revenue; May 2016: $90 million monthly revenue.",
        "Walmart acquisition August 8, 2016: $3.3 billion total ($3 billion cash, $300 million stock retention); Lore to lead Walmart.com.",
    ],
    mental_model={
        "name": "Get-Scale-or-Sell in E-commerce",
        "components": "Online retail aggregates to few winners when distribution is free (aggregation theory). Jet's dynamic cart discounts and membership flip-flop chased Amazon scale without matching fulfillment leverage; mega-retailers (Walmart) buy teams and tech when organic catch-up falters. Lore's track record made him the asset.",
        "application": "When modeling commerce challengers, separate GMV growth from margin structure — Walmart paid for CEO option value and millennial cohort access, not proven profits.",
    },
    competitive_advantage="Jet's innovation was gamified logistics pricing — bundle items from same fulfillment center, waive returns for discounts, pass half interchange back — technology-heavy but margin-thin against Amazon's scale and supplier terms. Lore's PR and fundraising credibility (post-Diapers) unlocked capital impossible for typical seed teams.\n\nWalmart brought balance sheet and store footprint; Jet brought urban brand and algorithmic pricing IP. Weakness: membership model abandoned; Amazon could underprice indefinitely; only ~5% U.S. retail online in 2012 baseline — battle is vast offline share, not just web traffic.",
    key_insights=[
        {
            "view": "People acquisition more than product.",
            "question": "Why $3.3B for one-year-old Jet?",
            "answer": "Marc Lore's second act, team, and pricing engine — Walmart explicitly put him in charge of Walmart.com; product fold likely temporary.",
        },
        {
            "view": "Amazon–Walmart chess repeats.",
            "question": "How did Diapers foreshadow Jet?",
            "answer": "Bezos blocked Walmart from Quidsi; Lore returns to compete, then sells to Walmart — same two players, decade apart.",
        },
        {
            "view": "Membership flip signaled model risk.",
            "question": "Why kill $50 fee after 3 months?",
            "answer": "Costco-style profit-from-fees thesis collapsed; shifted to 4–5% discounts vs Amazon — hosts skeptical on sustaining margins.",
        },
        {
            "view": "Winner-take-all makes #2 expensive.",
            "question": "Can two U.S. e-commerce giants coexist?",
            "answer": "Hosts struggle to name durable #2; category winners (apparel, etc.) fragment offline but online storefront is singular — Walmart buying optionality.",
        },
        {
            "view": "Urban millennial asset for Walmart.",
            "question": "What demographic gap closes?",
            "answer": "Jet's Hoboken/NYC subway brand vs Walmart's aging Sears comparison — acquisition buys cohort Amazon already owns.",
        },
    ],
    top_investment_implications=[
        {
            "ticker": "WMT",
            "direction": "Watch",
            "confidence": "Medium",
            "thesis": "Jet deal marks Walmart's Amazon defense via talent import; judge e-commerce ROI on omnichannel integration, not standalone Jet.com GMV.",
        },
        {
            "ticker": "AMZN",
            "direction": "Watch",
            "confidence": "Low",
            "thesis": "Aggregation dynamics in episode explain why incumbents struggle to dislodge Amazon scale — relevant to AWS-retail flywheel debates.",
        },
    ],
    golden_quotes=[
        "\"At Amazon, I saw it didn't matter how you treated people… very short-term thinking\" — Marc Lore, NYT, quoted by David.",
        "\"There's this huge middle class… willing to trade off convenience… for price\" — Lore starting Jet, per hosts.",
        "\"Walmart is this generation's Sears\" — Ben on demographic headwinds.",
    ],
    chronology={
        "subject": "Jet.com · Walmart Acquisition",
        "events": [
            {"date": "2005", "event": "Marc Lore founds Quidsi (Diapers.com)"},
            {"date": "2010", "event": "Amazon acquires Quidsi for $545 million"},
            {"date": "2013", "event": "Lore leaves Amazon"},
            {"date": "2014", "event": "Jet founded; $80M seed raised"},
            {"date": "2015-02", "event": "Additional $140M raised pre-launch"},
            {"date": "2015-07-21", "event": "Jet.com launches publicly"},
            {"date": "2015-10", "event": "Membership fee dropped"},
            {"date": "2015-11", "event": "$350 million funding round"},
            {"date": "2015-12", "event": "2M customers; $33M December revenue"},
            {"date": "2016-05", "event": "$90M monthly revenue announced"},
            {"date": "2016-08-08", "event": "Walmart acquires Jet for $3.3 billion"},
        ],
    },
    review_notes="Manual GPT Acquired batch ep19-25 — v5.1-acquired",
)

# Post-write expansions to meet v5.1 word minimum (~1600 words for 60+ min episodes)
EXPANSIONS: dict[str, dict[str, str]] = {
    "acq-episode-25-the-facebook-ipo": {
        "background": "\n\nHosts grade the IPO as defining for the public-company era: Morgan Stanley's $5 million Massachusetts settlement, NASDAQ's reputational damage, and lawsuits aside, the product outcome — native feed ads — became the industry template. They contrast Groupon's three-year path to IPO and Andrew Mason's 'never go public' Disrupt stage comment with Zuckerberg's later argument that listing improved discipline. General Motors' government re-IPO and Visa's larger deals provide scale context for why tech treated Facebook as the bellwether.",
        "competitive_advantage": "\n\nBanker dynamics mattered: lead-left prestige battle among Goldman, Morgan Stanley, and JP Morgan; selective downward revenue guidance to favored institutions created short-selling fuel. Facebook's dual-class control let Zuckerberg prioritize product over quarterly appeasement — critical when mobile rebuild required a full summer before monetization. Zynga platform concentration (15% of revenue) and GMV-style games revenue illustrated fragility of early social gaming layer; Facebook later diversified ad formats beyond desktop banners into performance direct-response units that travel to mobile.",
        "mental_model_components": " Secondary-market liquidity (SecondMarket) can force timing mistakes: when illiquid prints set $100 billion expectations, underwriters face pop-vs-discipline tradeoffs. JOBS Act arrived too late for Facebook but reshaped subsequent private-company windows.",
        "mental_model_application": " For IPO candidates today, stress-test mobile revenue disclosure early; treat S-1 risk factors as board-level OKRs once public. Instagram-sized bolt-ons during registration are regulatory-heavy but can hedge platform shifts.",
        "insight_suffix": "The episode ties each lesson to transcript numbers — S-1 filings, roadshow amendments, and quarterly mobile revenue splits — so investors can audit the narrative against primary sources rather than IPO folklore alone.",
        "conclusion_extra": "Hosts rate the episode a landmark IPO postmortem.",
    },
    "acq-episode-25-marvel": {
        "background": "\n\nHosts tie Marvel to Disney's Rogue One timing and compare Pixar (people/creative), Lucasfilm (single franchise cadence), and Marvel (third-party talent, ensemble scheduling). Men in Black (1997) surprises as Marvel IP; Star Wars comics licensing in the 1970s foreshadows the unified Disney shelf. Icahn 'loan-to-own' and Fleer baseball-card bubble mirror collectible manias; ToyBiz vertical integration previewed merchandise control Perlmutter later exploited.",
        "competitive_advantage": "\n\nPost-acquisition MCU cadence — multiple overlapping releases per year — amortizes marketing across franchises (Iron Man anchors lesser heroes). Theme-park rides and consumer products multiply theatrical ARPU versus standalone studios. Sony/Fox retained Spider-Man and X-Men rights for years, letting rivals fund character awareness while Marvel Studios captured bulk upstream value once films were owned.\n\nRisk factors hosts debate: superhero cycle fatigue (leisure-suit analogy), dependence on global China box office, and VFX cost inflation. Home-video decline versus Pixar hurts long-tail but streaming (Disney+) later provides new window — not covered in episode but implied successor to DVD flywheel.",
        "mental_model_components": " Perelman quote ('mini Disney') encodes that character libraries look like media utilities once distribution is bundled — similar to Facebook-Instagram ad stack pairing.",
        "mental_model_application": " When valuing content M&A, model characters as optionalities: each hero is a call option on theatrical, merchandise, and park revenue; breadth (Marvel) vs depth (Star Wars) changes variance of slate.",
        "insight_suffix": "Hosts benchmark against Pixar and Lucasfilm acquisitions in the same Disney trilogy, using box-office and home-video splits from post-acquisition slates and Two Truths cold-open facts.",
        "background_extra2": "\n\nTech themes span Sapiens-style shared-fiction IP (Harari book David cites), Hollywood's shift from 1981 originals to franchise bets, and whether superheroes face genre fatigue. Grading uses Instagram as benchmark; hosts land solid A territory on box-office ROI though home video trails Pixar. Carve-outs: Westworld, Overdrive library app, Marvel Symphonic Universe YouTube essay on absent memorable themes.",
        "competitive_extra2": "\n\nConsumer-products and parks flywheel (not fully modeled in episode financials) multiplies each theatrical dollar — Disney's integration advantage versus standalone Marvel in the 1990s. Perlmutter-era frugality on film budgets preserved downside; Iger-era marketing spend escalated upside. Comparison to Netflix/Amazon in-house content: Disney buys proven libraries; streamers must manufacture IP — different risk curves in the same attention economy.",
    },
    "acq-episode-24-skype": {
        "background": "\n\nBen's Talinn initiation (Millimallikas shot) and boardroom pool exemplify culture clash with eBay corporate governance. Rdio and Joost post-scripts show founders repeatedly recycling P2P tech; Microsoft integration under Ballmer made Tony Bates a CEO candidate before Satya Nadella. Hosts note Skype verb status for video calls even as text-first apps rose — strategic drift Microsoft accepted for Teams lineage.",
        "competitive_advantage": "\n\nRegulatory arbitrage on telecom pricing was Skype's wedge: bypassing international minute rates with P2P voice quality adequate for consumer calls. Supernode hybrid architecture balanced reliability with cost. Enterprise phase under Bates plus Microsoft Lync/Skype for Business overlap created upsell path eBay never pursued.\n\nFounder litigation strategy (Joltid) is a cautionary IP tale: sellers captured three liquidity events (Kazaa sale, eBay sale, spinout settlement) while buyers paid twice for the same protocol. Microsoft ultimately valued global real-time communications graph over standalone P/E.",
        "mental_model_components": " PE roll-ups (Silver Lake) excel when technology and cap table are broken — fixing IP title unlocks multiple expansion before strategic sale.",
        "mental_model_application": " Diligence checklist: confirm assignment of all protocol patents; model founder side-entities; assume culture integration cost if HQ is Tallinn and buyer is Bay Area enterprise.",
        "insight_suffix": "Ben's Microsoft and Talinn firsthand notes anchor the ownership chain from Kazaa through eBay, Silver Lake, and Microsoft with revenue and user counts from each transaction.",
        "background_extra2": "\n\nGrading disaggregates eBay (D), Silver Lake spinout (A+), Microsoft ($8.5B rich on 32× operating profit). Tech themes: P2P capital efficiency, founder litigation leverage, mobile transition under Tony Bates. Carve-outs include Shoe Dog and community spotlight Sentieo. Hosts note Skype text-chat as third feature while world moved to messaging-first.",
        "competitive_extra2": "\n\nMicrosoft Teams lineage and Lync merge gave enterprise upsell path; consumer Skype brand provided user trust during mobile VOIP transition. Estonia engineering culture and Kazaa-era reputation lowered recruiting friction for global protocol talent. Versus Zoom (later): Skype had head start but enterprise governance and Microsoft internal politics slowed standalone brand clarity — still, $8.5B valued real-time graph in 2011.",
    },
    "acq-episode-23-next-live-show-at-the-geekwire-summit": {
        "background": "\n\nLive GeekWire audience hears NeXT gala details: violin duet demo, no Apple attendees allowed, TextEdit/NeXT heritage jokes. BeOS alternative (Jean-Louis Gassée wanted $300M vs Apple's ~$125M) frames negotiation dynamics. Jobs sold all but one Apple share in 1986; Ross Perot and Canon invested ~$100–130M in NeXT — exit at $429M was modest for VCs but transformative for Apple.",
        "competitive_advantage": "\n\nNeXTSTEP's object-oriented toolchain let small teams ship complex apps (Doom, WWW) faster than procedural Mac OS toolchains of the era. Networking-first design anticipated internet-era collaboration; magnesium cube hardware failed on price but proved industrial design DNA that returned at Apple. WebObjects and Dell e-commerce deployment showed enterprise portability before consumer comeback.\n\nApple's acquisition bought time: Copland/Gershwin failures and Windows 95 pressure made internal next-gen OS non-credible. Jobs's interim CEO era killed SKUs (OpenDoc, printers) to focus on OS X path — organizational surgery only founder could execute.",
        "mental_model_components": " Platform emergencies justify founder-associated targets even at premium to standalone DCF; Gil Amelio slide honesty ('Steve Jobs') is rare corporate acknowledgment of people premium.",
        "mental_model_application": " When OS roadmaps slip multi-year, acquire proven UNIX/OO stack plus architects; expect 3–5 year integration and public leadership transition before revenue proof.",
        "insight_suffix": "GeekWire live format preserves primary quotes — Jobs on Xerox PARC, Amelio's slide, and Berners-Lee's WWW origin on NeXT hardware — for listeners tracing Apple's modern stack.",
        "background_extra2": "\n\nAcquisition category debate: people vs technology vs product — hosts land people-plus-technology with Gil's on-stage slide as evidence. What-would-have-happened: BeOS at $300M ask vs $125M Apple bid; internal Copland failure. Grade: greatest acquisition ever, NeXT vs Instagram benchmark. Carve-outs and hot takes include Spectacles launch and Hightower–VTS merger parallel.",
        "competitive_extra2": "\n\nObjective-C and Interface Builder continuity into iOS lowered developer switching costs for Apple ecosystem — decades-long API stability rare in platform M&A. NeXT's enterprise ports (Dell WebObjects) proved OS could run beyond cube hardware, de-risking software-only pivot Apple executed. Jobs's focus doctrine post-return removed printer/OpenDoc drag — organizational bandwidth mattered as much as kernel quality.",
    },
    "acq-episode-22-zillow-trulia-with-zillow-group-cfo-kathleen-philips": {
        "background": "\n\nKathleen's triple role (CFO, GC, people) explains six-week sprint from shareholder NDAs to July 28 announcement. Sami Inkinen Pacific row and proxy voting anecdote lighten deal lore. HotPads/Naked Apartments bolt-ons show Rich Barton playbook: buy traffic and agent tools without front-end merge. Disney-Twitter hot take in tail ties to media distribution thesis.",
        "competitive_advantage": "\n\nZestimate creates habitual traffic independent of transaction intent — reducing seasonality versus pure listings plays. Premier Agent auction dynamics let agents buy ZIP-level leads; Trulia doubled ad surface without killing SEO funnels. Combined firm negotiates MLS data aggressively after ListHub shock — vertical integration into data supply follows aggregation power laws.\n\nMillennial 'Zillow as entertainment' behavior (Ben, 27 at recording) signals future buyer cohort; older agents still close offline — two-speed market. Kathleen's FTC months in Washington show regulatory moat attempts by #1+#2 can clear if market defined broadly enough.",
        "mental_model_components": " Stock-for-stock at ~33% when traffic contribution ~one-third is fair arbitrage; $150M breakup fee prices distraction cost for both boards.",
        "mental_model_application": " In duopoly-prone marketplaces, pre-clear antitrust narrative and secure listing data contracts before announce; retention pools for rival management when brands stay separate.",
        "insight_suffix": "Kathleen Philips's SEC filing details and FTC timeline ground the merger story in corp-dev execution, not just consumer brand narrative or aggregation theory alone.",
        "background_extra2": "\n\nAcquisition category: business-line roll-up of same marketplace supply and demand; Kathleen outlines bolt-on strategy (HotPads, Naked Apartments). Tech themes: Rich Barton information-craving framework, real-estate-as-media, aggregation theory. Grade B/B+ from acquirer view — obvious but execution-heavy. Tail hot takes: Disney–Twitter, Snapchat Spectacles, MailChimp bootstrapped exit.",
        "competitive_extra2": "\n\nDual-brand SEO preserves organic acquisition while shared Premier Agent backend improves ARPU per agent lead — roll-up without front-end destruction. Kathleen's dual GC/corp-dev role compressed six-week timeline versus typical public-company merger cadence. Redfin vertical integration (not deep-dived) remains competitive contrast: Zillow chose aggregation breadth over brokerage margin capture at acquisition time.",
    },
    "acq-episode-21-inside-the-ma-press-with-bloombergs-alex-sherman": {
        "background": "\n\nEpisode abandons acquisition grading for press mechanics; David's WSJ stint informs paywall vs terminal contrast. Follow-ups cover Instagram advertiser growth, Amazon $800 share price, Yahoo breach material-adverse clause risk, and Kara Swisher/Recode without redhead distribution. Acquired listener base framed as trade-publication niche enjoying story-driven retrospectives Snapchat episode proved.",
        "competitive_advantage": "\n\nTerminal economics fund journalists who can refuse stories — negative selection against clickbait. Dual-source 'people familiar' norm reduces single-sided spin; competitors decode bylines for leak attribution (Yahoo–Verizon). Data feeds on red headlines monetize milliseconds — Sherman notes hedge funds pay $25K/year back in seconds on M&A alpha.\n\nWeakness: post-close analysis underproduced; podcast/longread formats (Acquired) capture drama without moving markets. Social platforms struggle to charge without killing network effects — Bloomberg model (expensive professional tier, free consumer site) is hard to replicate for Twitter/Facebook.",
        "mental_model_components": " Incentive alignment beats editorial policy: when customers punish false positives harder than missing a rumor, accuracy rises.",
        "mental_model_application": " Founders should cultivate reporters before fundraising peaks; bury small deals on heavy-news Fridays; read sourcing codes before trading on leaks.",
        "insight_suffix": "Sherman's terminal-subscriber lens explains why Bloomberg under-weights retrospective grades Acquired specializes in — and why founders misunderstand reporter incentives.",
        "background_extra2": "\n\nTech themes: messaging-as-OS in Asia vs U.S., Twitter paywall/network-effect paradox, Bloomberg dual-revenue model vs ad CPM press. Follow-ups: Instagram 500K advertisers, Amazon $800, Yahoo breach material-adverse risk, Ford Chariot vs GM Cruise. Carve-outs include Phil Knight Shoe Dog. Episode structure intentionally abandons acquisition grading rubric.",
        "competitive_extra2": "\n\nRecode/Vox acquisition cited as cautionary tale for star journalists without terminal infrastructure — distribution moat beats personal brand alone. Acquired occupies retrospective niche Sherman acknowledges: story quality without market-moving latency. For founders, relationship capital with beat reporters compounds; one-off pitch emails underperform when no trusted sourcing history exists.",
    },
    "acq-episode-20-android": {
        "background": "\n\nRubin lineage: Apple → General Magic (public, bankrupt) → WebTV → Danger Sidekick celebrity (Entourage) → Android without VC. January 2007 iPhone line-up story (Ben queued, no money for data plan). Eric Schmidt on Apple board through iPhone launch; Google Maps default on first iPhone. Motorola patent detour and Xiaomi fork cited as open-source second-order effects.",
        "competitive_advantage": "\n\nOpen Handset Alliance coordinated OEMs/carriers against Apple–AT&T exclusivity — economic enemy-of-my-enemy coalition. $10M developer challenge signaled openness; App Store pressure followed. GMS bundle (Play, Maps, Gmail) is real control point atop AOSP; Amazon Kindle Fire shows fork path without Google services. Samsung fast-follow copied iPhone features within months — acceptable to Google if Search default retained.\n\nOracle suit revealed Apple takes ~34% of iOS search revenue — quantifying Android's defensive ROI. Chrome parallel on desktop completes 'own the front door' strategy. Windows Mobile failed closed ecosystem; BlackBerry denied iPhone feasibility — incumbents misread UX revolution.",
        "mental_model_components": " Rubin + Sidekick fandom gave Google talent and timing; iPhone forced UI reset that synced launch with OHA marketing.",
        "mental_model_application": " When core revenue is traffic-mediated (ads), subsidize OS/browser to avoid tolls; measure success in avoided rev-share billions, not Play margin alone.",
        "insight_suffix": "Oracle litigation disclosures and Goldman mobile-search estimates give hard numbers to Android's defensive economics beyond market-share headlines and holy-war rhetoric.",
        "background_extra2": "\n\nAcquisition category: technology at purchase evolving to product, business line, and strategic asset. Motorola patent sidebar and Xiaomi/Amazon fork examples. Grade A+ vs Instagram — defensive but existential. Carve-outs and community Matt Morgante Patagonia book. Eric Schmidt board seat and Maps on first iPhone underline how fast alliances flipped.",
        "competitive_extra2": "\n\nGMS licensing bundle is the real control lever: OEMs get Play Store and Google apps only when default search/maps stay Google — AOSP forks without GMS (China, Fire OS) show ceiling of open-source alone. AT&T iPhone exclusivity 2007–2010 funded Apple's rise; Verizon Droid campaign bought Android credibility in U.S. carrier channel — coalition economics, not solo product superiority, won share.",
    },
    "acq-episode-19-jet": {
        "background": "\n\nCommunity spotlight: Chris Laurent Nowdue.ai; listener demand drove episode (10+ requests). Lore school-picnic Bezos meeting; Amazon left Diapers independent in Hoboken like Zappos model. Jet Insider Program ~350K pre-launch signups; subway ad blitz in NYC. Fortune July 2016 Lore interview on winner-take-all; hosts compare Walmart to fading Sears and Amazon biospheres vs suburban HQ legacy.",
        "competitive_advantage": "\n\nJet cart algorithms rewarded same-warehouse bundling, return waivers, and interchange givebacks — operational savings passed as consumer discounts if scale arrived. Lore's PR mastery sustained funding after killing membership fee — credibility from Diapers exit at $545M. Walmart gained urban millennial brand and Hoboken tech talent; stores offer pickup/last-mile options Amazon still builds.\n\nWeakness: Amazon could subsidize indefinitely; Jet's 10–15% undercut promise eroded when membership engine removed; December holiday $33M revenue impressive but May $90M still tiny vs Amazon. Aggregation theory suggests one online storefront per market — Walmart paid for time and talent, not proven #2 economics.",
        "mental_model_components": " Strategic buyers pay for proven founders when organic catch-up fails; retention stock ($300M) aligns multi-year integration.",
        "mental_model_application": " Model e-commerce challengers on GMV growth separately from contribution margin; ask whether buyer needs cohort, tech, or GMV — Jet was people+tech, not profitable product.",
        "insight_suffix": "Everything Store and Fortune interview quotes document Lore's Amazon exit motives and Walmart's second attempt after losing Diapers to Bezos in 2010.",
        "background_extra2": "\n\nAcquisition category spans people, technology, business line, and asset (urban millennial cohort). What-would-have-happened: Amazon price war playbook repeats. Tech themes: aggregation theory, e-commerce still ~5% of U.S. retail in 2012 baseline, Walmart as Sears generational analogy. Grade middling — bold defense, unproven #2. Hot takes: Disney–Twitter; carve-outs Shoe Dog, Marvel Symphonic Universe.",
        "competitive_extra2": "\n\nWalmart store footprint offers pickup and last-mile options Jet lacked — acquirer synergy more physical than digital. Lore's second successful exit premium justified $3.3B price for talent and playbook, not GAAP earnings. Costco membership metaphor failed quickly; dynamic cart remained differentiated tech asset if integrated into walmart.com pricing engine over multi-year horizon.",
    },
}


def apply_expansions(body: dict, ep_id: str) -> dict:
    exp = EXPANSIONS.get(ep_id)
    if not exp:
        return body
    if "background" in exp:
        body["background"] = body.get("background", "") + exp["background"]
    if "background_extra2" in exp:
        body["background"] = body.get("background", "") + exp["background_extra2"]
    if "competitive_advantage" in exp:
        body["competitive_advantage"] = body.get("competitive_advantage", "") + exp["competitive_advantage"]
    if "competitive_extra2" in exp:
        body["competitive_advantage"] = body.get("competitive_advantage", "") + exp["competitive_extra2"]
    mm = body.get("mental_model", {})
    if "mental_model_components" in exp:
        mm["components"] = mm.get("components", "") + exp["mental_model_components"]
    if "mental_model_application" in exp:
        mm["application"] = mm.get("application", "") + exp["mental_model_application"]
    body["mental_model"] = mm
    if "insight_suffix" in exp:
        for ki in body.get("key_insights", []):
            ki["answer"] = ki.get("answer", "") + " " + exp["insight_suffix"]
    if "conclusion_extra" in exp:
        body["conclusion"] = body.get("conclusion", "") + " " + exp["conclusion_extra"]
    return body


def main() -> None:
    APPROVED.mkdir(parents=True, exist_ok=True)
    results: dict[str, str] = {}
    for ep_id, body in EPISODES.items():
        body = apply_expansions(body, ep_id)
        path = APPROVED / f"{ep_id}.json"
        path.write_text(json.dumps(body, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
        proc = subprocess.run(
            [sys.executable, str(ROOT / "scripts" / "validate_one_acquired.py"), ep_id],
            capture_output=True,
            text=True,
            cwd=str(ROOT),
        )
        status = "completed" if proc.returncode == 0 else "failed"
        results[ep_id] = status
        print(f"{ep_id}: {status}")
        if proc.stdout:
            print(proc.stdout.strip())
        if proc.stderr:
            print(proc.stderr.strip(), file=sys.stderr)
    print("\n=== SUMMARY ===")
    for ep_id, status in results.items():
        print(f"{status}\t{ep_id}")


if __name__ == "__main__":
    main()
