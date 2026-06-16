#!/usr/bin/env python3
"""Expand batch-11 Founders summaries to meet v4.10 word targets."""
from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
APPROVED = ROOT / "data" / "approved"

PATCHES: dict[str, dict[str, str]] = {
    "fnd-415-how-elon-thinks": {
        "background_append": "\n\nMusk reads encyclopedias as a kid and treats engineering as magic — Clarke's sufficiently advanced technology line. He separates design from manufacturing physically so stove-hot mistakes pull designers immediately. Recruiting filters attitude over skill; acronyms banned as communication tax. SR-71 speed-as-defense and burn-rate triage frame daily priority — $100k/day at Tesla means half-hour delays cost eight figures.",
        "fact0_append": " Musk cites Sun Tzu and military history: engineering wins wars; discontinuities like lasers from space beat maneuvering at Caesar-era pace.",
        "mm_application_append": " Gigafactory five-step reversals — automate-then-delete mistakes tore out robots. Attack-the-constraint on Tesla casting: six suppliers said die-cast impossible; Musk asked if physics forbids it.",
    },
    "fnd-417-arnold-schwarzenegger": {
        "background_append": "\n\nSenra ties Arnold's 1977 book to young Elon sketching SpaceX and Bernard Arnault laying LVMH plans in his 40s — early blueprints ridiculed then vindicated. Gladiator forest squats: 250 reps, thighs like balloons. Todd Graves Raising Cane's mirrors fanatical routine — lived in apartment above first store, bedspread unchanged decades later.",
        "fact1_append": " Reg Park Hercules photo fixed ideal; Arnold pasted magazine photos on walls, trained below-zero without heat as teenager.",
        "insight1_answer_append": " Carl Jung psychology with training partner: your body cannot change overnight — clear goals and someone behind you saying one more rep.",
    },
    "fnd-413-how-to-run-down-a-dream": {
        "background_append": "\n\nGurley profiles Knight's 902 wins and Pete Newell clinic stack — 74 plays diagrammed on hotel floor. Meyer burned savings to $25k negative net worth studying 14 barbecue pork variations across North Carolina. Dylan hitchhiked 1,200 miles on $10; sold 100 million records after studying every folk album nine months.",
        "fact2_append": " Hinkie 76ers tenure media-covered; post-exit teaches Stanford with two ears one mouth rule; 87 Capital backs dreamers stopped learning.",
        "mm_application_append": " Zero excuse for ignorance — Gurley: news is free, collect information peers swipe from bedrock. Surround yourself with people you want to find; Bezos hiring bar single most important element.",
    },
    "fnd-412-how-roger-federer-works": {
        "background_append": "\n\nFederer skipped formal schooling at 16 for pro tour; dentist switched for positivity. Lucille Ball mentored Arnold parallel — say yes, act accordingly. Larry Ellison loved winning but corrected: 'No, I love to fight.' Nadal pre-match sprints versus Federer coffee-shop calm — same respect, different combustion.",
        "fact1_append": " Carter cerebral coaching from Australian journeyman at Basel; stagnation equals regression per team belief.",
        "fact2_append": " Burnout avoided via minimum practice, protected nights, therapy with Paul Annacone; Rick Rubin Creative Act cited for decompression.",
        "insight0_answer_append": " Roller coaster truth: natural to doubt after loss — force smile, move on, become master at overcoming hard moments.",
    },
    "fnd-411-tortured-into-greatness-the-life-of-andre-agassi": {
        "background_append": "\n\nOpen's shower self-talk — solitary confinement leads to audible orders. Jim Brown bet house on 8-year-old Andre; father Jim Brown story shows early hustle. JP pastor reframes God as angry voice in ear — Word says once. Mandela dinner: master fate, captain soul; rebuild at 27 after meth with Gilbert mantra.",
        "fact1_append": " 13th cortisone shot at 2006 Open — vacuum-packed spine; Gil surrogate father from Nick Bollettieri era forward.",
        "fact2_append": " Sampras 82 weeks No. 1; Agassi dating Brooke Shields, Nike stock, Frankie's restaurant tuition gift — bottom lip trembles at lasting value.",
        "mm_application_append": " Don Valentine storytelling collateral; Open written on walls narrowing pin prick — outside perspective via Gil prevents fragile mindset destruction.",
    },
    "fnd-410-excellent-advice-for-living": {
        "background_append": "\n\nKelly compresses lessons into tweetable seeds — Munger on hatred poisoning hater, Bezos on frugality except passions, Rubin redo secret. Rule of three in conversation; Kobe removed self-negotiation from training. Finite life shrinking — highest leverage is who you spend time with; courtesy costs nothing, consistency beats intensity.",
        "fact1_append": " Dell and Dyson infinite-game rulers; collecting displayed teaches like Buffett shareholder letters.",
        "mm_application_append": " Pros are pros at recovering from mistakes; assume busy on email, try twice. Greatness incompatible with optimizing short term — schedule Sabbaths and aimless walks.",
    },
    "fnd-409-the-creative-genius-of-rick-rubin": {
        "background_append": "\n\nRubin 78 areas echo Founders compounding — reread episodes three times for insight. Mackey Whole Foods origin: healthier grocery when none existed. Bezos ferocious on details; Jordan Oprah selfishness quote on craft protection. Iovine Defiant Ones: artists die overdosed when success unbearable.",
        "fact1_append": " Dyson noticed vacuum suction loss — ten words led to cyclonic empire; submerge in works calibrates meter.",
        "fact2_append": " Pompañcha mental chatter — Rubin normalizes self-doubt, separates from song doubt. Patience hangs like diary entry; impatience argues with reality.",
        "insight1_answer_append": " Kafka hermit silence; Warhol simultaneous TV/radio; Proust cork walls — environment broadcasts into work.",
    },
    "fnd-407-bruce-springsteen-repairs-the-hole-in-himself": {
        "background_append": "\n\nBorn to Run ~600 pages handwritten twice. Freehold kerosene stove, silent father thousand words unspoken in childhood. Steel Mill to E Street; skips graduation for gigs. Mike Appel 50/50 worst contract signed green; Columbia debut flop then 3,000-show lifeline. Depression repair via Patty Scialfa; Deliver Me Nowhere film with Iovine.",
        "fact1_append": " Motifs brothers Ray and Walter — Walter full-blooded animal attitude Bruce wanted. Landmarks on 1974 tour map; Time/Newsweek covers triggered impostor retreat.",
        "fact2_append": " John Landau instant chemical connection — educated homeboys fortifying drive. Democracy in band: names on dead, workload shared, muse freedom.",
        "mm_application_append": " Longevity over supernova — prioritize breathing days creating; addictive personalities need plan past five-minute brilliance.",
    },
    "fnd-406-christian-von-koenigsegg": {
        "background_append": "\n\nEk recommendation led Senra to dozen videos and hundred-idea note list. Post-Soviet pen trade; father sold retirement for bridge loan. Factory fire Saturday everyone working — tooling burned, airbase hangar with fighter-jet runway tests. Munger four ideas at dinner: human nature unchanged, troubles inescapable, don't whine, great businesses rare.",
        "fact1_append": " CC8S 1992–2002 void — truck driver neighbor, Volvo engineer from book; modeled without CAD until 1997.",
        "fact2_append": " Tesla IPO shares bought; Pagani differentiation parallel; Guinness 250+ records, 287 mph segment.",
        "insight2_answer_append": " Farm fire wind-as-blessing; government space after flames; jet-hangar runway beats public-road test limits.",
    },
    "fnd-397-jiro-ono-simplicity-is-the-ultimate-advantage": {
        "background_append": "\n\nSenra transcribed full documentary; Jiro dreams sushi ideas nightly. Shokunin moral duty serve society; kaizen daily train seat. MrBeast headquarters visit parallels obsessive thumbnails — one person one job. Todd Graves one-menu focus rhymes; Michelin inspectors astonished restroom outside premises.",
        "fact1_append": " Age nine homeless bridge; failure not option; three stars at 82 after decades unknown fame.",
        "fact2_append": " Rice dealer pressure cooker rivals cannot imitate; body-temperature serving; plate cleared in seconds.",
        "mm_application_append": " Arnold and Bernard Arnault detail spotting; Disney Main Street 50-foot congruity check — same detail religion across crafts.",
    },
}

ROUND2: dict[str, dict[str, str]] = {
    "fnd-411-tortured-into-greatness-the-life-of-andre-agassi": {
        "background_append": "\n\nAgassi beats Becker practice 52 times then loses $10,000 bet — father silent with trophy. Speed pills from Philly at nationals; boarding school psychology and visualization classes rebelled against with mohawk. 1999 French Open rain delay locker room — Gilbert screaming crosscourt plan; guns blazing opener.",
        "fact0_append": " Father kept axe handle and salt/pepper for street fights; yelled everything twice, sometimes ten times.",
        "insight2_answer_append": " Commercial villain brand moved Oakley product without asking — differentiation accidental but monetized rebellion.",
    },
    "fnd-407-bruce-springsteen-repairs-the-hole-in-himself": {
        "background_append": "\n\nGrandfather Sing Sing prison, Navy five wives — rock-star energy without arena. Cross-country trip at 32 critical mass; therapist Doc Meyers in LA suburb. Patty gauntlet stay-or-go; son born fills humility and terror circle. Broadway run and Deliver Me Nowhere documentary extend repair narrative.",
        "fact0_append": " 150M+ records; Howard Stern Rock Hall interview on breaking chains via children.",
        "mm_components_append": " Hole from father fuels music repair — hammer pain into righteous sword; no doover for history.",
        "conclusion_append": " SONY/catalog lens: authenticity and 3,000-show endurance beat flash supernova economics.",
    },
    "fnd-409-the-creative-genius-of-rick-rubin": {
        "fact0_append": " Wooden consecutive championships from sock habit; Rubin 400 Founders books compares uniqueness of 78-chapter form.",
        "insight0_answer_append": " Competition is yourself — rest is distraction; treat every word and action with skillful care.",
    },
    "fnd-397-jiro-ono-simplicity-is-the-ultimate-advantage": {
        "background_append": "\n\nYounger son two-star mirror restaurant; eldest apprenticing since 19. Zamuri award ceremony parallels — dedication to craft over social recognition. Octopus vendor picky customers only; anti-establishment rebel buys all or nothing.",
        "fact0_append": " 40–50 minute octopus massage; 200 rejected eggs; hot-towel burns before fish touch.",
    },
    "fnd-410-excellent-advice-for-living": {
        "background_append": "\n\nJohn Mackey 5,000th store age 75; Kelly on imagination potent force. Rule of seven research sources; experience overrated for hiring aptitude. Writing grateful possible therapy; calm contagious like panic.",
        "fact2_append": " Separate creating improving — editor killing creator same pass destroys originality per Catmull Ford maternity ward.",
    },
    "fnd-406-christian-von-koenigsegg": {
        "background_append": "\n\nSeed $200k, loans $300k, savings $2M; investors paid suppliers in stock. Koenigsegg bought Tesla IPO; compares weight to revenue like nut on scale.",
        "insight0_answer_append": " Age 22 start with truck-driver neighbor engineer — eight years to Paris 2002 CC8S reveal.",
    },
}


def apply_patch(data: dict, patch: dict) -> None:
    if "background_append" in patch:
        data["background"] += patch["background_append"]
    if "conclusion_append" in patch:
        data["conclusion"] += patch["conclusion_append"]
    facts = data["important_facts"]
    for key, idx in (("fact0_append", 0), ("fact1_append", 1), ("fact2_append", 2)):
        if key in patch and len(facts) > idx:
            facts[idx] += patch[key]
    mm = data.get("mental_model", {})
    if "mm_components_append" in patch:
        mm["components"] = mm.get("components", "") + patch["mm_components_append"]
    if "mm_application_append" in patch:
        mm["application"] = mm.get("application", "") + patch["mm_application_append"]
    insights = data.get("key_insights", [])
    for key, idx in (("insight0_answer_append", 0), ("insight1_answer_append", 1), ("insight2_answer_append", 2)):
        if key in patch and len(insights) > idx:
            insights[idx]["answer"] += patch[key]


def main() -> None:
    all_ids = set(PATCHES) | set(ROUND2)
    for ep_id in sorted(all_ids):
        path = APPROVED / f"{ep_id}.json"
        if not path.exists():
            continue
        data = json.loads(path.read_text(encoding="utf-8"))
        if ep_id in PATCHES:
            apply_patch(data, PATCHES[ep_id])
        if ep_id in ROUND2:
            apply_patch(data, ROUND2[ep_id])
        path.write_text(json.dumps(data, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
        print(f"patched {ep_id}")


if __name__ == "__main__":
    main()
