#!/usr/bin/env python3
"""Remove transcript meta-junk and rewrite Founders conclusions."""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
APPROVED = ROOT / "data" / "approved"

# Regex replacements applied to all string values in summary JSON
REGEX_FIXES = [
    (re.compile(r' In the transcript, he quantifies scale directly: "[^"]*"'), ""),
    (re.compile(r" In the transcript, Patel notes:.*$", re.MULTILINE), ""),
    (re.compile(r" He adds a concrete marker in the episode:.*$", re.MULTILINE), ""),
    (
        re.compile(
            r" This fact matters in the transcript because it is used to compare what looked normal in earlier cycles against today's operating environment, and to show how capital, competition, and execution demands have shifted\."
        ),
        "",
    ),
    (
        re.compile(
            r" The transcript's reasoning is that execution quality becomes more visible as conditions normalize, so teams that combine clear operating metrics with patient decision-making are more likely to sustain performance\. That is why the conversation repeatedly links strategy to measurable outcomes, not only to thematic narratives\."
        ),
        "",
    ),
    (re.compile(r" in the episode's framing"), ""),
    (re.compile(r" in the episode is therefore"), " is therefore"),
    (re.compile(r"The neoprime thesis in the episode is therefore"), "The neoprime thesis is therefore"),
    (re.compile(r"~10–20% gross in the framing\)"), "~10–20% gross)"),
    (re.compile(r"Long-term thesis in the episode:"), "Long-term thesis:"),
    (re.compile(r"the episode treats as"), "the analysis treats as"),
    (re.compile(r"The hosts cite "), ""),
    (re.compile(r"Tom and the hosts conclude "), "Tom Alberg concludes "),
    (re.compile(r"Smart-speaker market share data cited in the episode:"), "Smart-speaker market share data:"),
    (re.compile(r" in the episode's comparison"), ""),
    (re.compile(r" in the episode is product desirability"), " is product desirability"),
    (re.compile(r" The episode presents this as"), " This reflects"),
    (re.compile(r" a rare marketplace decision the episode treats as"), " a rare marketplace decision treated as"),
    (re.compile(r" Additional He also describes operating speed in explicit terms:.*$", re.MULTILINE), ""),
    (re.compile(r" He frames the operating constraint with concrete scale markers in the discussion, including:.*$", re.MULTILINE), ""),
    (re.compile(r" Applied practically, he points to manager decisions under rapid change windows such as:.*$", re.MULTILINE), ""),
    (
        re.compile(
            r"In this episode, the model is applied through recurring themes: Flexible mandate only works if the culture shares information\.; Capital architecture should prevent forced style drift\.; The best deals are whiteboarded with management, not pulled off a shelf\.\. The practical move is to make decisions that still work when conditions tighten: preserve strategic flexibility, keep operating discipline high, and focus on actions that improve long-duration compounding rather than short-term appearance metrics\."
        ),
        "Apply the model by sharing risk units across platforms, sizing each fund to its deal flow while TAL handles oversized checks, and whiteboarding bespoke structures with management rather than pulling products off the shelf.",
    ),
    (re.compile(r"Senra notes "), ""),
    (re.compile(r"Senra says "), ""),
    (re.compile(r"Senra treats "), ""),
    (re.compile(r"Senra's read supports"), "supports"),
    (re.compile(r"Senra's read "), ""),
    (re.compile(r"Senra frames "), ""),
    (re.compile(r"Senra emphasizes that "), ""),
    (re.compile(r"Senra highlights "), ""),
    (re.compile(r"Senra describes "), ""),
    (re.compile(r"Senra uses "), ""),
    (re.compile(r"Senra ties "), ""),
    (re.compile(r"Senra cites "), ""),
    (re.compile(r"Senra's lesson:"), "The lesson:"),
    (re.compile(r"Senra's lesson "), "The lesson "),
    (re.compile(r"Senra's favorite"), "A favorite"),
    (re.compile(r"Senra's emblem of"), "An emblem of"),
    (re.compile(r"Senra's reread suggests"), "The biography suggests"),
    (re.compile(r"Senra's fourth reread suggests"), "The memoir suggests"),
    (re.compile(r"Senra's contrast between"), "The contrast between"),
    (re.compile(r"Senra's Bowerman-vs-convention frame reminds"), "Bowerman's product obsession versus convention reminds"),
    (re.compile(r"Senra pairs this with"), "This pairs with"),
    (re.compile(r"Senra on scarcity"), "On scarcity"),
    (re.compile(r"Senra uses this to explain"), "This explains"),
    (re.compile(r", cited by Senra:"), ":"),
    (re.compile(r" — Senra's read supports"), " — supports"),
    (re.compile(r"; Senra's read supports"), "; supports"),
    (re.compile(r" not a direct thesis from Senra alone\."), " not a direct thesis from this episode alone."),
    (re.compile(r" in Senra's framing"), ""),
    (re.compile(r"Senra's lesson: maximal vision"), "Maximal vision"),
    (re.compile(r" milestones Senra ties to"), " milestones tied to"),
]

CONCLUSIONS = {
    "fnd-404-larry-ellison": (
        "Ellison's core idea is contrarian clarity under existential stakes: when analysts called databases mature, "
        "he burned the boats on client-server and bet Oracle entirely on internet architecture — then picked fights "
        "with Microsoft and IBM to force comparison with category leaders. Phantom revenue from misaligned sales "
        "incentives, not strategy alone, nearly killed the company in 1991 when the stock fell more than 80%; "
        "cost austerity and Safra Catz's execution discipline were the recovery playbook."
    ),
    "fnd-421-jony-ive": (
        "Ive's design method starts with the product story — what should this object feel like on first touch — "
        "and only then tackles engineering constraints. Jobs proved the payoff: cut 40 products to four, reversed "
        "engineer-first culture so industrial design drove specs, and turned iMac, iPod, and iPhone into proof "
        "that a 16-person A-team practicing ruthless simplification beats consensus committees and thousand-person armies."
    ),
    "fnd-416-demis-hassabis": (
        "Hassabis is a missionary founder pursuing AGI when the idea was ridiculed: chess prodigy turned neuroscientist "
        "who refused a £500,000 Bullfrog check, climbed a pragmatic ladder from Atari games to AlphaGo and AlphaFold, "
        "and sold DeepMind to Google for $650 million not for peak valuation but to escape fundraising and buy compute "
        "for a problem that outran venture timelines."
    ),
    "fnd-418-phil-knight": (
        "Knight's core idea is conviction under cash stress: Nike survived seven bank refusals because authentic belief "
        "in the product transmitted through community — track-meet trunk sales, Bowerman's kitchen-lab obsession, and "
        "a jogging book that expanded the market before the swoosh did. Authentic conviction beats scripted selling "
        "when capital is scarce and the founder still feels like an impostor."
    ),
    "fnd-355-rare-bernard-arnault-interview": (
        "Arnault saw atomized European luxury as an industry before peers did: roll up crown-jewel brands, keep creative "
        "autonomy while sharing back-office scale, and own the real estate so rivals pay rent on your storefronts. "
        "Handbags at roughly 10× manufacturing cost and Dior's arc from 3 stores and 90 million euros to 439 stores "
        "and 9.5 billion euros make luxury a software-margin business run through obsessive Saturday store inspections."
    ),
    "ep422": (
        "Focus for decades on work you love is the blunt lesson from 400+ founder biographies: the greatest operators "
        "— Graves, Dyson, Jobs, Walton, Munger, Schulz — looked boring or stubborn for years before they looked "
        "inevitable. Money is often a proxy for meaning; the best founders do not work their whole lives to earn "
        "the right to stop doing the work they love."
    ),
}

IMPORTANT_FACTS_FIXES = {
    "ep474": [
        (
            "Farber says that at recording time the Strait of Hormuz was effectively closed in practice and that Iranian military capability had been degraded. He adds that even if 85-90% of Iranians want regime change, outcomes depend on whether there is a credible alternative force structure rather than public sentiment alone. He also contrasts adversaries that can centralize decisions quickly with democracies that must earn legitimacy repeatedly, arguing that this legitimacy is still a strategic strength if institutions can translate it into timely procurement.",
            "At recording time the Strait of Hormuz was effectively closed in practice and Iranian military capability had been degraded. Even if 85-90% of Iranians want regime change, outcomes depend on whether there is a credible alternative force structure rather than public sentiment alone. Adversaries that centralize decisions quickly hold an operational edge, but democratic legitimacy remains a strategic strength when institutions can translate it into timely procurement.",
        ),
    ],
    "ep473": [
        (
            "On hardware reality, he cites Blackwell rack specs around 3,000 pounds, roughly 8 feet high by 4 feet deep by 3 feet wide, and about 100 kW power draw. He adds that SpaceX controls roughly 98-99% of satellites in orbit and notes Starlink V3 around 20 kW, then argues Nvidia could sell $2T-$3T of GPUs in 2026-27 under unconstrained TSMC capacity.",
            "Blackwell racks weigh about 3,000 pounds — roughly 8 feet high by 4 feet deep by 3 feet wide — and draw about 100 kW. SpaceX controls roughly 98-99% of satellites in orbit; Starlink V3 runs around 20 kW. Under unconstrained TSMC capacity, Nvidia GPU sales could reach $2T-$3T in 2026-27.",
        ),
    ],
    "fnd-404-larry-ellison": [
        (
            "Ellison founded Oracle (originally Software Development Laboratories) in 1976 at age 34 with a modest goal of roughly $10 million revenue and 50 employees. The first relational database shipped as Oracle version two because 'no one buys version one from five guys in California'; early customers included the CIA and U.S. intelligence agencies. Senra notes Ellison annotated Matthew Symonds' Softwar with footnotes after 40 hours of reading.",
            "Ellison founded Oracle (originally Software Development Laboratories) in 1976 at age 34 with a modest goal of roughly $10 million revenue and 50 employees. The first relational database shipped as Oracle version two because 'no one buys version one from five guys in California'; early customers included the CIA and U.S. intelligence agencies. Ellison annotated Matthew Symonds' Softwar with footnotes — the book pairs Symonds' portrait with Ellison's own corrections.",
        ),
        (
            "Ellison abandoned client-server engineering to bet entirely on internet applications when peers called it crazy. He repositioned Oracle against Microsoft and IBM — not Sybase or Informix — and cut global pricing staff from about 200 people to fewer than 10 after finding feudal duplication. Senra says Network Computing Architecture got no traction until renamed Internet Computing Architecture.",
            "Ellison abandoned client-server engineering to bet entirely on internet applications when peers called it crazy. He repositioned Oracle against Microsoft and IBM — not Sybase or Informix — and cut global pricing staff from about 200 people to fewer than 10 after finding feudal duplication. Network Computing Architecture got no traction until renamed Internet Computing Architecture.",
        ),
    ],
    "fnd-416-demis-hassabis": [
        (
            "Hassabis co-founded DeepMind in 2010 to build AGI when scientists and investors largely dismissed human-like AI; Founders Fund's $2.3 million in December 2010 bought just under half the company when almost no other capital was available. Senra cites 80% of conference attendees rolling their eyes at early AGI pitches; Peter Thiel backed Hassabis as a missionary, not a mercenary.",
            "Hassabis co-founded DeepMind in 2010 to build AGI when scientists and investors largely dismissed human-like AI; Founders Fund's $2.3 million in December 2010 bought just under half the company when almost no other capital was available. Roughly 80% of conference attendees rolled their eyes at early AGI pitches; Peter Thiel backed Hassabis as a missionary, not a mercenary.",
        ),
        (
            "DeepMind's AlphaGo beat Lee Sedol in 2016 using strategies humans had not conceived; AlphaFold's protein-structure breakthrough earned Hassabis and John Jumper the 2024 Nobel Prize in chemistry — milestones Senra ties to Hassabis's 2010 vision of AI as a meta-solution to scientific problems. Bill Gates's deck line cited a true ML breakthrough as worth ten Microsofts.",
            "DeepMind's AlphaGo beat Lee Sedol in 2016 using strategies humans had not conceived; AlphaFold's protein-structure breakthrough earned Hassabis and John Jumper the 2024 Nobel Prize in chemistry — milestones tied to Hassabis's 2010 vision of AI as a meta-solution to scientific problems. Bill Gates's deck line cited a true ML breakthrough as worth ten Microsofts.",
        ),
    ],
    "fnd-355-rare-bernard-arnault-interview": [
        (
            "Arnault is 75 with roughly $200 billion net worth; his workdays run 8 a.m. to 8:30 p.m. and Saturday store checks draw on a mental database built from an estimated 10,000 store visits. LVMH spans 75 luxury houses with 200,000 employees; Senra notes Arnault texts bullet-point critiques on chairs, landscaping, and salespeople's shoes.",
            "Arnault is 75 with roughly $200 billion net worth; his workdays run 8 a.m. to 8:30 p.m. and Saturday store checks draw on a mental database built from an estimated 10,000 store visits. LVMH spans 75 luxury houses with 200,000 employees; he texts bullet-point critiques on chairs, landscaping, and salespeople's shoes.",
        ),
        (
            "When Arnault bought Dior from bankrupt Boussac in 1984, the brand had 3 stores and about 90 million euros in annual sales; Senra cites 439 stores and 9.5 billion euros in sales last year. Arnault's early-40s ten-year objective — fewer global brands, LVMH among them — reads almost unchanged 35 years later; ready-to-wear generates only 10% of Louis Vuitton sales.",
            "When Arnault bought Dior from bankrupt Boussac in 1984, the brand had 3 stores and about 90 million euros in annual sales; Dior now has 439 stores and 9.5 billion euros in annual sales. Arnault's early-40s ten-year objective — fewer global brands, LVMH among them — reads almost unchanged 35 years later; ready-to-wear generates only 10% of Louis Vuitton sales.",
        ),
    ],
}

KEY_INSIGHTS_FIXES = {
    "fnd-404-larry-ellison": [
        (
            "Ellison wanted Oracle compared to IBM and Microsoft, not smaller database vendors. The media framed billionaire-versus-billionaire battles; Oracle's products rode along. Senra treats the fight as brand positioning — measure against top heavyweights so association lifts perceived survival, enterprise trust, and press coverage.",
            "Ellison wanted Oracle compared to IBM and Microsoft, not smaller database vendors. The media framed billionaire-versus-billionaire battles; Oracle's products rode along. Measuring against top heavyweights lifts perceived survival, enterprise trust, and press coverage.",
        ),
    ],
    "fnd-421-jony-ive": [
        (
            "Sculley's PDA label was too slippery; Ive asked what story the product tells in daily life and redesigned the lid as the first special interaction. Senra notes Ive repeats this story-first frame from Newton through iPod ('simplify, remove, reduce') and supplier negotiations where he works backward from an ideal sketch with no artificial limits.",
            "Sculley's PDA label was too slippery; Ive asked what story the product tells in daily life and redesigned the lid as the first special interaction. The same story-first frame runs from Newton through iPod ('simplify, remove, reduce') and supplier negotiations where he works backward from an ideal sketch with no artificial limits.",
        ),
        (
            "Senra cites 16 Apple industrial designers in one studio versus Samsung's 1,000 designers in 34 centers, echoing Jobs's line that eight A-players run circles around a giant team of B and C players. Ive protected the team, took blame for weak details personally, and accepted Jobs's critique that caring about team feelings over the work was vanity.",
            "Apple runs 16 industrial designers in one studio versus Samsung's 1,000 designers in 34 centers — echoing Jobs's line that eight A-players run circles around a giant team of B and C players. Ive protected the team, took blame for weak details personally, and accepted Jobs's critique that caring about team feelings over the work was vanity.",
        ),
    ],
    "fnd-416-demis-hassabis": [
        (
            "Thiel saw Hassabis as a missionary who would work around the clock for the problem itself, not a mercenary chasing a hot app. Senra emphasizes that in 2010 AGI sounded laughable, yet Hassabis scraped together believers while 80% of conference attendees literally rolled their eyes and walked away.",
            "Thiel saw Hassabis as a missionary who would work around the clock for the problem itself, not a mercenary chasing a hot app. In 2010 AGI sounded laughable, yet Hassabis scraped together believers while 80% of conference attendees literally rolled their eyes and walked away.",
        ),
        (
            "At Elixir, Hassabis inspired engineers into an impossible game and nobody gave real feedback. At DeepMind he let researchers tinker on 1970s Atari titles — affordable, scored, multi-game proof of general agents — before AlphaGo and AlphaFold. Senra's lesson: maximal vision plus the next rung, not a single leap.",
            "At Elixir, Hassabis inspired engineers into an impossible game and nobody gave real feedback. At DeepMind he let researchers tinker on 1970s Atari titles — affordable, scored, multi-game proof of general agents — before AlphaGo and AlphaFold. Maximal vision requires the next rung, not a single leap.",
        ),
        (
            "Hassabis was exhausted justifying widgets to investors while pursuing intelligence. Larry Page argued building another Google would consume his career; Google offered servers and freedom from fundraising. Senra quotes Hassabis: how many billions would you trade for five more years to finish the mission?",
            "Hassabis was exhausted justifying widgets to investors while pursuing intelligence. Larry Page argued building another Google would consume his career; Google offered servers and freedom from fundraising. Hassabis's trade: how many billions would you exchange for five more years to finish the mission?",
        ),
    ],
    "fnd-418-phil-knight": [
        (
            "Senra highlights Knight's belief that customers sense when a founder genuinely believes in the work. Shoe Dog shows Nike's early wins came from conviction transmitted through community — running books, track-meet trunk sales, Bowerman's product obsession — not polished pitches. Knight often felt like an impostor as CEO yet kept selling because the product story was true.",
            "Customers sense when a founder genuinely believes in the work. Nike's early wins came from conviction transmitted through community — running books, track-meet trunk sales, Bowerman's product obsession — not polished pitches. Knight often felt like an impostor as CEO yet kept selling because the product story was true.",
        ),
        (
            "Knight's accountant father pushed conventional success while Bowerman modeled obsessive craft and experimentation. Senra uses the Founders maxim that the father's story is embedded in the son: one path offered safety, the other offered the mission that became Nike.",
            "Knight's accountant father pushed conventional success while Bowerman modeled obsessive craft and experimentation. One path offered safety; the other offered the mission that became Nike.",
        ),
        (
            "When drivers threw things at joggers, Bowerman's Jogging book sold millions and normalized running. Knight stocked books and comfortable chairs in his first store. Senra's lesson: celebrate the activity, build community around the sport, and let shoe demand follow.",
            "When drivers threw things at joggers, Bowerman's Jogging book sold millions and normalized running. Knight stocked books and comfortable chairs in his first store. Celebrate the activity, build community around the sport, and let shoe demand follow.",
        ),
    ],
    "fnd-355-rare-bernard-arnault-interview": [
        (
            "Senra ties Arnault's Tokyo counter memory and Dubai chair critiques to the Founders theme that quantity compounds: tens of thousands of store visits build a database like Sam Walton's retail tours or Jay Paul Getty's plant walk-throughs. Once you've seen enough examples, incongruities jump out immediately.",
            "Arnault's Tokyo counter memory and Dubai chair critiques reflect quantity compounding: tens of thousands of store visits build a database like Sam Walton's retail tours or Jay Paul Getty's plant walk-throughs. Once you've seen enough examples, incongruities jump out immediately.",
        ),
        (
            "In Taste of Luxury he called luxury the only area with true luxury profit margins — software margins on physical goods. Senra highlights handbags at about 10 times manufacturing cost and Arnault's bet that grouped brands reinforce weaker names while sharing ad buying and retail location advantages.",
            "In Taste of Luxury he called luxury the only area with true luxury profit margins — software margins on physical goods. Handbags run at about 10 times manufacturing cost; grouped brands reinforce weaker names while sharing ad buying and retail location advantages.",
        ),
        (
            "Senra describes Arnault earning from his own stores, leasing to rivals, and appreciating premium real estate — pulling Louis Vuitton out of Bal Harbour to build Miami Design District. Competitors need his storefronts or lose the best locations; complaints draw his reply that efficient rivals do not need excuses.",
            "Arnault earns from his own stores, leases to rivals, and appreciates premium real estate — pulling Louis Vuitton out of Bal Harbour to build Miami Design District. Competitors need his storefronts or lose the best locations; complaints draw his reply that efficient rivals do not need excuses.",
        ),
    ],
    "ep474": [
        (
            "Farber says opposition sentiment is insufficient when coercive institutions remain intact. In his Iran framing, even an 85-90% desire for change does not produce transition unless military, financial, and organizational structures can realign. That is why he treats regime analysis as a force-structure problem, not a polling problem.",
            "Opposition sentiment is insufficient when coercive institutions remain intact. Even an 85-90% desire for change in Iran does not produce transition unless military, financial, and organizational structures can realign. Regime analysis is a force-structure problem, not a polling problem.",
        ),
    ],
}

OTHER_STRING_FIXES = {
    "fnd-404-larry-ellison": {
        "top_investment_implications[0].thesis": (
            "Ellison's playbook — database lock-in, repeated platform reinventions, and enterprise marketing — explains Oracle's survival through the 1991 near-death and internet pivot; durable enterprise software economics persist even as AI reshapes the next architecture cycle."
        ),
        "golden_quotes[2]": (
            "Forty hours with Softwar compressed into one dense hour — evidence of the density Ellison packs into contrarian stories about complexity, incentives, and long-term survival."
        ),
    },
    "fnd-421-jony-ive": {
        "mental_model.application": (
            "Ive's 100 foam Newton prototypes and 50 home-button iterations pair with Graham Duncan's 'trace of fear' hiring test and Jobs's 'design is how it works' mantra. When engineers cited 38 reasons against the iMac handle, Jobs overruled as CEO; Ive told suppliers to imagine a bucket of money and pull what they needed. The durable lesson: simplify, remove, reduce — but only after defining the story users can grasp on first touch."
        ),
        "top_investment_implications[0].thesis": (
            "Kahney's biography reinforces Apple's moat as design-driven culture institutionalized by the Jobs–Ive partnership — 2×2 product focus, engineer reversal, and manufacturing obsession that produced iMac, iPod, iPhone, and iPad category wins. The operational playbook ages better than spec-sheet PC competition even as hardware cycles mature."
        ),
        "golden_quotes[0]": (
            "Jobs told Apple employees on return: 'Our goal is not just to make money, but to make great products' — that line alone kept Ive from quitting back to England."
        ),
        "golden_quotes[1]": (
            "Ive on differentiation: 'It's very easy to be different, but very difficult to be better' — 50 home-button prototypes show fanatical care beyond obvious specs."
        ),
        "golden_quotes[2]": (
            "When engineers offered 38 reasons against the iMac handle, Jobs said: 'No, no, we're doing this… because I'm the CEO and I think it can be done' — the no-compromise partnership that replaced skin-on-enclosure design."
        ),
    },
    "fnd-416-demis-hassabis": {
        "mental_model.application": (
            "Founders pursuing hard tech should sequence ambition — Elixir failure versus DeepMind ladder — and sell to align resources with mission timing, not peak valuation. Hassabis chose Google for servers and five more years on the problem; Alphabet's bet bought AGI optionality, London research culture, and missionary founder retention through AlphaFold and Gemini lineage."
        ),
        "top_investment_implications[0].thesis": (
            "Alphabet's 2014 DeepMind bet bought AGI optionality and compute scale — AlphaFold, Gemini lineage, and London research culture — suggesting Google's AI moat partly reflects missionary founder retention and massive sustained R&D spend post-acquisition."
        ),
        "top_investment_implications[1].thesis": (
            "OpenAI's 2015 launch reacted to Google-DeepMind concentration of AGI talent — a structural competitive dynamic where Microsoft's later OpenAI partnership becomes one answer to Hassabis's 2014 sale."
        ),
        "golden_quotes[1]": (
            "Hassabis on losing: 'It's like my soul on fire' — this explains why he refused Bullfrog's £500,000 check and later chose mission over fundraising comfort."
        ),
    },
    "fnd-418-phil-knight": {
        "mental_model.components": (
            "Knight built Nike by pairing a contrarian import thesis with a product-obsessed partner, surviving bank refusals because believers — financiers, employees, and eventually runners — sensed authentic conviction rather than a sales script. Customers sense when a founder genuinely believes in the work; early wins came through community — running books, track-meet trunk sales, Bowerman's product obsession — not polished pitches. Two father figures shaped the drive: an accountant father pushing convention and Bowerman modeling obsessive craft."
        ),
        "top_investment_implications[0].thesis": (
            "Shoe Dog reinforces Nike's origin as a conviction-and-community brand built through cash crises and loyal early backers — a durable halo narrative even as the public company faces cyclical inventory and margin pressure unrelated to Knight's founding playbook. The memoir's operator lessons age better than quarterly sneaker hype cycles."
        ),
        "top_investment_implications[1].thesis": (
            "Bowerman's product obsession versus convention reminds investors that athletic-footwear leaders win by product obsession and market creation, not discounting alone — relevant when comparing Nike's community-origin story to Adidas turnaround narratives."
        ),
        "golden_quotes[0]": (
            "Shoe Dog is a nearly perfect entrepreneurial autobiography that still delivers new energy on every reread — rare for a memoir read three or four times."
        ),
        "golden_quotes[2]": (
            "Woodell lent his family's entire $8,000 life savings with no paperwork; six years later at the IPO Knight converted that trust into stock worth about $1.6 million — a loyalty-compounding story."
        ),
    },
    "fnd-355-rare-bernard-arnault-interview": {
        "top_investment_implications[1].thesis": (
            "The contrast between LVMH's integrated real estate and rival complaints about landlord power frames Tapestry and other multi-brand luxury names as structurally disadvantaged without flagship ownership and back-office scale."
        ),
        "golden_quotes[0]": (
            "The only English Arnault biography is over 30 years old and sells for $1,500 to over $5,000 — which is why Bloomberg's House of Arnault piece deserved three reads."
        ),
    },
}


def apply_regex(text: str) -> str:
    for pattern, repl in REGEX_FIXES:
        text = pattern.sub(repl, text)
    return text


def walk(obj):
    if isinstance(obj, str):
        return apply_regex(obj)
    if isinstance(obj, list):
        return [walk(x) for x in obj]
    if isinstance(obj, dict):
        return {k: walk(v) for k, v in obj.items()}
    return obj


def replace_in_list(items: list, old: str, new: str) -> None:
    for i, item in enumerate(items):
        if item == old:
            items[i] = new
            return
        if isinstance(item, dict):
            for k, v in item.items():
                if isinstance(v, str) and v == old:
                    item[k] = new
                    return


def main() -> int:
    changed: list[str] = []
    for path in sorted(APPROVED.glob("*.json")):
        if path.stem == "batch_state":
            continue
        raw = path.read_text(encoding="utf-8")
        data = json.loads(raw)
        eid = data.get("episode_id", path.stem)

        updated = walk(data)

        if eid in CONCLUSIONS:
            updated["conclusion"] = CONCLUSIONS[eid]

        for old, new in IMPORTANT_FACTS_FIXES.get(eid, []):
            replace_in_list(updated.get("important_facts", []), old, new)

        for old, new in KEY_INSIGHTS_FIXES.get(eid, []):
            replace_in_list(updated.get("key_insights", []), old, new)

        for key, value in OTHER_STRING_FIXES.get(eid, {}).items():
            if key.startswith("top_investment_implications"):
                idx = int(key.split("[")[1].split("]")[0])
                field = key.split(".")[-1]
                updated["top_investment_implications"][idx][field] = value
            elif key.startswith("golden_quotes"):
                idx = int(key.split("[")[1].split("]")[0])
                updated["golden_quotes"][idx] = value
            elif key == "mental_model.application":
                updated["mental_model"]["application"] = value
            elif key == "mental_model.components":
                updated["mental_model"]["components"] = value

        new_raw = json.dumps(updated, indent=2, ensure_ascii=False) + "\n"
        if new_raw != raw:
            path.write_text(new_raw, encoding="utf-8")
            changed.append(path.stem)
            print(f"updated: {path.stem}")

    print(f"\nTotal changed: {len(changed)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
