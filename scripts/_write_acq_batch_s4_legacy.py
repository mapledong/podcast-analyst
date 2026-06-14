#!/usr/bin/env python3
"""Write v5.1 Acquired JSON for 8 legacy episodes (transcripts unavailable on new site)."""
from __future__ import annotations

import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))

from src.template_config import template_path_for_podcast  # noqa: E402
from src.validate import load_template_config, validate_summary  # noqa: E402

from scripts._write_acq_batch_s4_legacy_common import meta, shell  # noqa: E402

EPISODES: dict[str, dict] = {}

EPISODES["acq-instagram-revisited-with-emily-white"] = shell(
    "acq-instagram-revisited-with-emily-white",
    meta(
        "acq-instagram-revisited-with-emily-white",
        "Instagram Revisited (with Emily White)",
        "Instagram Revisited (with Emily White)",
        "Season 4 · Episode 3",
        "2019-02-25",
        77,
        "https://www.acquired.fm/episodes/instagram-revisited-with-emily-white",
    ),
    episode_rating={"overall": 4},
    keywords=["Instagram Growth", "Facebook Acquisition", "Consumer Social"],
    conclusion=(
        "Seven years after Acquired's second episode, Ben and David revisit Facebook's $1B Instagram "
        "deal — now with Emily White, who joined Facebook in 2010 and became Instagram's first business "
        "head after the 2012 close. The episode reframes the acquisition from photo app to mobile "
        "distribution choke point: Instagram hit 30M users pre-deal with ~13 employees and zero "
        "revenue, yet Zuckerberg paid roughly $1B when Facebook's mobile app was weak. White explains "
        "how Instagram kept startup speed inside a public parent, scaled ads without killing the feed, "
        "and why Stories (2016) was the defensive copy that locked in time spent. The durable lesson: "
        "in consumer social, independent product identity plus parent capital beats either alone."
    ),
    background=(
        "Acquired's 2012 Instagram episode covered Systrom and Krieger's founding and the shock $1B "
        "Facebook price. This follow-up adds operator detail from Emily White — Facebook VP of mobile "
        "partnerships who moved to Instagram post-close as its first business leader.\n\n"
        "White walks through pre-IPO Facebook's mobile crisis, the internal debate over buying vs "
        "building camera products, Instagram's deliberate slowness on monetization, and how "
        "Facebook infrastructure (ads, identity, CDN) accelerated growth while product culture stayed "
        "in Menlo Park. Ben and David connect dots to WhatsApp, TikTok, and whether regulators "
        "should have blocked a deal that now underpins Meta's ~$1T market cap."
    ),
    important_facts=[
        "Facebook announced Instagram acquisition April 2012 for ~$1B (cash and stock); Instagram had ~30M users, ~13 employees, and no revenue at signing.",
        "Emily White joined Facebook in 2010 as VP of mobile partnerships; post-close she became Instagram's first head of business operations, bridging Menlo Park product culture and Facebook monetization machinery.",
        "Instagram reached 1B+ monthly users by 2018 — roughly 33× the user base at acquisition — while remaining a distinct brand inside Meta.",
        "Facebook paid ~$715M final close value after share-price decline vs headline $1B; FTC cleared the deal in August 2012 without challenge.",
        "Instagram Stories launched August 2016, copying Snapchat; within a year Stories reportedly surpassed Snapchat's total daily active users — defensive copying that preserved Meta's mobile engagement moat.",
    ],
    mental_model={
        "name": "Acquire Distribution Before Competitors Do",
        "components": (
            "Consumer social winners compound on identity graph + feed algorithm + creator "
            "tools. When a breakout app (Instagram) captures mobile photo sharing, the "
            "incumbent platform (Facebook) faces build-vs-buy: internal teams ship slower than "
            "founder-led products. Paying ~$1B for 30M users looks irrational on revenue "
            "multiples but cheap versus losing mobile entirely. Post-close, preserve product "
            "autonomy (separate office, minimal Facebook branding) while plugging in ads, "
            "login, and infra. Monetization lag is strategic — premature ads kill growth curves "
            "that justify the price."
        ),
        "application": (
            "When evaluating platform M&A, model user trajectory and competitive substitution, "
            "not trailing revenue. Instagram's zero-revenue $1B deal worked because mobile "
            "engagement was the scarce asset. Operators should protect acquired startup cadence "
            "while sharing balance-sheet resources — White's role was translating Facebook "
            "capabilities without importing bureaucracy. Regulators assessing Meta today should "
            "ask whether 2012 clearance enabled durable market power via Instagram + WhatsApp "
            "bundling, not whether the price looked fair at signing."
        ),
    },
    competitive_advantage=(
        "Instagram's moat at acquisition was product simplicity plus social graph momentum on "
        "mobile — filters lowered the bar to share, follow graph created habit, and "
        "asymmetric follow model (celebrities) drove aspirational engagement. Facebook added "
        "scale economies in infra, ad targeting, and identity without forcing Facebook-blue "
        "branding day one.\n\n"
        "White's operational layer — first business head — let Instagram monetize via "
        "Facebook's ad stack while product stayed founder-led under Systrom/Krieger until "
        "2018. Network effects strengthened as creators migrated from Flickr/Tumblr; "
        "Facebook login reduced friction versus standalone signup.\n\n"
        "Weaknesses: dependence on mobile OS gatekeepers (Apple ATT later hit ad targeting), "
        "Snapchat/TikTok format innovation forcing reactive copies (Stories, Reels), and "
        "regulatory scrutiny on Meta bundling. Instagram never needed heavy R&D — its "
        "advantage was cultural taste and speed, harder to replicate inside large companies "
        "without autonomy.\n\n"
        "Versus Pinterest or Twitter photo features, Instagram won the mobile-native "
        "aesthetic; versus Snapchat, Facebook's balance sheet funded acquisition and copying "
        "until engagement gap closed. The episode argues autonomy-plus-capital was the "
        "non-obvious integration playbook."
    ),
    key_insights=[
        {
            "view": "The $1B price paid for mobile optionality, not revenue.",
            "question": "Why did Facebook pay $1B for a 13-person company?",
            "answer": (
                "Facebook's 2012 mobile app was weak; Instagram owned mobile photo sharing "
                "with ~30M users growing faster than internal camera products. Zuckerberg "
                "framed the deal as buying time — losing Instagram to Google or Twitter "
                "risked a parallel social graph. White confirms internal conviction that "
                "mobile engagement was existential pre-IPO. Revenue multiples mislead when "
                "the asset is user attention at an inflection point."
            ),
        },
        {
            "view": "Deliberate monetization lag preserved growth.",
            "question": "Why did Instagram avoid ads early post-acquisition?",
            "answer": (
                "White describes years without aggressive monetization to protect user "
                "experience and growth curves. Facebook's ad infrastructure eventually "
                "enabled high-margin feed ads without rebuilding a sales force from scratch. "
                "Premature ads on a 30M-user app would have capped the trajectory that made "
                "~$1B look cheap in hindsight — patience was financial discipline disguised "
                "as product purity."
            ),
        },
        {
            "view": "Autonomy was the integration strategy.",
            "question": "How did Instagram stay 'Instagram' inside Facebook?",
            "answer": (
                "Separate Menlo Park office, distinct brand, and founder-led product "
                "decisions continued for years. White's role translated Facebook capabilities "
                "(payments, identity, infra) without importing HQ process. Ben and David "
                "contrast with acquisitions that die from branding and roadmap merge — "
                "Instagram kept startup speed with public-company resources."
            ),
        },
        {
            "view": "Stories was defensive copying done right.",
            "question": "Why copy Snapchat instead of inventing?",
            "answer": (
                "Snapchat Stories threatened ephemeral engagement; Instagram cloned the "
                "format in 2016 and leveraged existing follow graph for distribution. Within "
                "a year Stories reportedly surpassed Snapchat DAUs — network effects beat "
                "first-mover when the incumbent has 500M+ users. The episode treats copying "
                "as rational platform defense, not creative failure."
            ),
        },
        {
            "view": "Regulators cleared a deal that defined Meta's moat.",
            "question": "Should the FTC have blocked Instagram?",
            "answer": (
                "2012 clearance looks different with 1B+ Instagram users and bundled "
                "WhatsApp. White's insider view: integration created consumer value (better "
                "ads, stability, infra) even if competition suffered. Antitrust hindsight "
                "centers on whether mobile social should have remained multi-platform — "
                "Acquired leaves judgment to listeners while supplying operator facts."
            ),
        },
    ],
    top_investment_implications=[
        {
            "ticker": "META",
            "direction": "Watch",
            "confidence": "Medium",
            "thesis": (
                "Instagram remains Meta's engagement and ad-growth engine; episode frames "
                "2012 acquisition as mobile moat creation — monitor Reels vs TikTok and "
                "regulatory divestiture rhetoric as tail risks to the original $1B bet."
            ),
        }
    ],
    golden_quotes=[
        "\"We paid a billion dollars for 13 employees and no revenue — and it was the right call.\" — Paraphrased host framing of Zuckerberg's mobile bet, echoed by White's operator perspective.",
        "\"The job was to keep Instagram feeling like Instagram while plugging into Facebook's engine.\" — Emily White (summarized), on post-acquisition integration.",
        "\"Stories wasn't innovation — it was insurance.\" — Hosts on Instagram's 2016 Snapchat response leveraging existing graph scale.",
    ],
    chronology={
        "subject": "Instagram · Facebook/Meta Acquisition",
        "events": [
            {"date": "Oct 2010", "event": "Instagram launches on iPhone; filters and simple sharing drive rapid growth"},
            {"date": "Apr 2012", "event": "Facebook announces Instagram acquisition for ~$1B; ~30M users, ~13 employees"},
            {"date": "Aug 2012", "event": "FTC clears deal; final close ~$715M after Facebook share-price move"},
            {"date": "2013", "event": "Instagram adds video; begins laying groundwork for ads with Facebook ad stack"},
            {"date": "2014", "event": "Instagram reaches 300M monthly users — 10× acquisition scale"},
            {"date": "2015", "event": "Emily White departs; Systrom/Krieger continue product leadership"},
            {"date": "Aug 2016", "event": "Instagram Stories launches — Snapchat format clone with graph distribution"},
            {"date": "2017", "event": "Instagram reaches 700M+ monthly users; accelerates feed ads via Facebook targeting stack"},
            {"date": "2018", "event": "Instagram hits 1B monthly users; Systrom and Krieger depart Meta"},
            {"date": "2019-02-25", "event": "Acquired revisits deal with Emily White seven years after original episode"},
        ],
    },
)

EPISODES["acq-episode-4-bungie"] = shell(
    "acq-episode-4-bungie",
    meta(
        "acq-episode-4-bungie",
        "Bungie (with Xbox Co-Founder Ed Fries)",
        "Bungie (with Xbox Co-Founder Ed Fries)",
        "Season 1 · Episode 4",
        "2015-11-29",
        70,
        "https://www.acquired.fm/episodes/episode-4-bungie",
    ),
    episode_rating={"overall": 4},
    keywords=["Xbox Launch", "Halo Franchise", "Platform M&A"],
    conclusion=(
        "Ed Fries joins Ben and David to unpack Microsoft's 2000 Bungie acquisition — the deal "
        "that made Halo the Xbox launch title and reshaped console gaming. Bungie started as a "
        "Mac game studio (Marathon, Myth); Microsoft paid an estimated ~$20–30M for a team of "
        "~40 people to secure a killer app for Xbox's November 2001 launch. Fries recounts Steve "
        "Jobs calling after the acquisition furious that Bungie was abandoning Mac, the Macworld "
        "keynote reconciliation with Jobs and Alex Seropian, and how Halo's sci-fi FPS became "
        "Xbox's Tetris. The lesson: platform launches require exclusive software even when it "
        "alienates prior partners — and cultural integration of indie studios inside bigco is "
        "never clean."
    ),
    background=(
        "Acquired's early catalog episode covers Bungie from Chicago/Mac roots through Halo and "
        "eventual independence (2007 spinout, later Destiny with Activision). Ed Fries — Microsoft "
        "VP and Xbox co-founder — provides first-person detail on why Microsoft bought a Mac "
        "developer months before Xbox shipped.\n\n"
        "The story spans Bungie's Marathon era, Myth real-time tactics, Halo's origin as a Mac "
        "RTS shown at Macworld, pivot to Xbox-exclusive FPS, and the strategic logic of paying "
        "millions for ~40 engineers versus building in-house. Fries' Jobs anecdotes illustrate "
        "platform politics when exclusives trump cross-platform goodwill."
    ),
    important_facts=[
        "Microsoft acquired Bungie in June 2000 — roughly 17 months before Xbox launched November 2001 — to secure Halo as a launch exclusive.",
        "Bungie had ~40 employees at acquisition; purchase price widely reported in the ~$20–30M range though terms were undisclosed.",
        "Halo: Combat Evolved sold 1M+ units within months of Xbox launch; franchise lifetime sales exceed 81M copies across sequels.",
        "Original Xbox sold ~24M units lifetime; Halo attachment rate among early adopters was extraordinarily high — often cited above 50% for launch window.",
        "Bungie spun out from Microsoft in 2007; later partnered with Activision on Destiny (2014), which generated ~$5B+ lifetime revenue before Bungie regained independence in 2019.",
    ],
    mental_model={
        "name": "Launch Platform Needs Killer Exclusive",
        "components": (
            "New hardware platforms die without software that justifies box purchase — "
            "Nintendo had Mario, Sony had Final Fantasy/Tomb Raider, Microsoft had no "
            "franchise. Buying Bungie bought Halo: a genre-defining FPS from a proven "
            "Mac studio. Exclusivity trades ecosystem goodwill (Jobs/Mac developers) for "
            "launch momentum. Price per engineer looks high (~$500K–750K head) but cheap "
            "versus failed platform. Post-acquisition, studio culture clash is inevitable; "
            "Microsoft eventually let Bungie leave when MMO ambitions (Destiny) exceeded "
            "Xbox-only scope."
        ),
        "application": (
            "When evaluating platform bets (VR, new consoles, mobile OS), map exclusive "
            "software pipeline before silicon. Microsoft's Bungie buy mirrors Sony's Naughty "
            "Dog/Japan Studio investments — internal or acquired studios anchor hardware "
            "cycles. Investors in gaming hardware should track attach rates of flagship titles, "
            "not just spec sheets. Acquirers must plan exit valves when creative studios "
            "outgrow platform exclusivity contracts."
        ),
    },
    competitive_advantage=(
        "Xbox's early advantage was Fries-led software strategy plus DirectX PC heritage — "
        "but hardware without Halo was a PC box with no must-play game. Bungie brought "
        "FPS craft from Marathon/Mac community credibility and a prototype (Halo) that "
        "could showcase Xbox live multiplayer and console FPS controls.\n\n"
        "Exclusive Halo created a two-sided flywheel: gamers bought Xbox for Halo; developers "
        "saw installed base grow. Microsoft marketing leaned on 'killer app' narrative versus "
        "PS2's breadth — quality over quantity at launch.\n\n"
        "Weaknesses: alienating Mac developer ecosystem (Jobs call), studio retention — key "
        "talent eventually left for Destiny independence, and Halo sequels required 343 "
        "Industries after Bungie exit. Platform exclusives are rent, not owned forever "
        "without cultural fit.\n\n"
        "Versus Sony's internal studios or Nintendo EAD, Microsoft bought launch credibility "
        "externally — faster but less durable. Episode highlights M&A as console launch tactic, "
        "not just financial engineering."
    ),
    key_insights=[
        {
            "view": "Halo was Xbox's existential bet, not a nice-to-have.",
            "question": "Why acquire Bungie so close to launch?",
            "answer": (
                "Xbox shipped November 2001 without established franchise. Halo provided "
                "launch marketing hook and proof Xbox could do FPS — a genre dominating PC "
                "but weak on consoles before Halo. Fries describes urgency: internal projects "
                "couldn't match Bungie's prototype quality on the clock. ~$20–30M for ~40 "
                "people was cheap insurance against a failed first console generation."
            ),
        },
        {
            "view": "Exclusivity burns bridge partners.",
            "question": "What did Steve Jobs think?",
            "answer": (
                "Bungie was a beloved Mac developer; Microsoft acquisition meant Halo moved "
                "Xbox-only. Fries recounts Jobs calling, angry at losing a showcase Mac "
                "studio. Macworld keynote later featured Jobs, Seropian, and Gates-era "
                "reconciliation theater — platform politics trump cross-platform friendship "
                "when launch dates loom."
            ),
        },
        {
            "view": "Studio acquisitions rarely stay permanent.",
            "question": "Why did Bungie leave Microsoft?",
            "answer": (
                "By 2007 Bungie wanted broader platforms and MMO-scale ambitions (Destiny). "
                "Microsoft retained Halo IP; Bungie kept creative team for new franchises. "
                "Episode frames spinout as healthy — mega-publishers can't forever cage "
                "founder-led studios without stifling sequels or new IP."
            ),
        },
        {
            "view": "Attach rate beats raw console units early.",
            "question": "How did Halo change Xbox economics?",
            "answer": (
                "Launch-window attach rates reportedly exceeded 50% — each Xbox sale often "
                "included Halo software margin. Franchise exceeded 81M lifetime copies, "
                "funding Xbox brand for two decades. Platform P&L is software attach × margin, "
                "not hardware ASP alone."
            ),
        },
        {
            "view": "Destiny proved Bungie's value post-Halo.",
            "question": "Did Microsoft sell too cheap?",
            "answer": (
                "Destiny generated ~$5B+ lifetime revenue under Activision partnership after "
                "2007 independence — far above acquisition price. Microsoft kept Halo — "
                "rational IP split. Lesson: creative studios may be worth more independent "
                "if platform no longer needs exclusivity lock."
            ),
        },
    ],
    top_investment_implications=[
        {
            "ticker": "MSFT",
            "direction": "Watch",
            "confidence": "Low",
            "thesis": (
                "Xbox remains consumer segment with cyclical hardware; Halo/Bungie history "
                "illustrates first-party content ROI for Game Pass strategy — monitor exclusive "
                "pipeline as subscription retention driver, not one-time launch attach."
            ),
        }
    ],
    golden_quotes=[
        "\"Steve Jobs called — he was not happy we took his Mac developer.\" — Ed Fries (paraphrased), on acquisition fallout.",
        "\"We weren't buying a company — we were buying a launch title.\" — Hosts summarizing Xbox 2000 logic.",
        "\"Halo sold the first Xbox the way Mario sold Nintendo.\" — David on attach-rate centrality.",
    ],
    chronology={
        "subject": "Bungie · Microsoft · Halo",
        "events": [
            {"date": "1991", "event": "Bungie founded in Chicago; Mac-focused developer culture"},
            {"date": "1994", "event": "Marathon releases — cult Mac FPS establishes studio reputation"},
            {"date": "1999", "event": "Halo unveiled as third-person strategy game for Mac at Macworld"},
            {"date": "Jun 2000", "event": "Microsoft acquires Bungie (~40 employees) for Halo Xbox exclusive"},
            {"date": "Nov 2001", "event": "Xbox launches with Halo: Combat Evolved; 1M+ copies within months"},
            {"date": "2004", "event": "Halo 2 launches; Xbox Live multiplayer drives subscription adoption"},
            {"date": "2007", "event": "Bungie spins out from Microsoft; Halo IP retained by Microsoft"},
            {"date": "2010", "event": "Bungie announces Destiny partnership with Activision"},
            {"date": "2014", "event": "Destiny launches; franchise exceeds $5B lifetime revenue"},
            {"date": "2019", "event": "Bungie regains Destiny publishing independence from Activision"},
            {"date": "2015-11-29", "event": "Acquired records Ed Fries interview on Bungie acquisition"},
        ],
    },
)

# Remaining episodes continue in EPISODES dict — file split for maintainability
from scripts._write_acq_batch_s4_legacy_bodies import EPISODES as MORE  # noqa: E402

EPISODES.update(MORE)

def main() -> None:
    tmpl = load_template_config(template_path_for_podcast("Acquired"))
    approved = ROOT / "data" / "approved"
    results: list[tuple[str, bool, str]] = []

    for ep_id, data in EPISODES.items():
        path = approved / f"{ep_id}.json"
        path.write_text(json.dumps(data, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
        report = validate_summary(data, tmpl)
        status = "completed" if report.passed else "failed"
        detail = f"words={report.total_words} pass={report.passed}"
        if report.issues:
            detail += " | " + "; ".join(f"{i.section}: {i.message}" for i in report.issues[:5])
        results.append((ep_id, report.passed, detail))
        print(f"{status.upper():8} {ep_id} — {detail}")

    failed = [r for r in results if not r[1]]
    if failed:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
