#!/usr/bin/env python3
"""Write, validate, and publish 8 ready-queue BB/Founders summaries (transcript-grounded)."""

from __future__ import annotations

import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))

from scripts.save_bb_founders_summary import enrich_metadata, save_and_publish

APPLE_BB = "https://podcasts.apple.com/podcast/business-breakdowns/id1559120677"
SPOTIFY_BB = "https://open.spotify.com/show/4zQbeLbLgqKEyn7e2sKzez"
APPLE_FND = "https://podcasts.apple.com/podcast/founders/id1141877104"
SPOTIFY_FND = "https://open.spotify.com/show/7txiovdzPARhjm18NwMUYj"

FND = {e["id"]: e for e in json.loads((ROOT / "data/discovered/founders_episodes.json").read_text())["episodes"]}
BB = {e["id"]: e for e in json.loads((ROOT / "data/discovered/business_breakdowns_episodes.json").read_text())["episodes"]}


def fnd(ep_id: str, rating: int, guest: str, guest_role: str, **body) -> dict:
    ep = FND[ep_id]
    num = ep["episode_number"]
    data = {
        "episode_id": ep_id,
        "podcast": "Founders",
        "host": "David Senra",
        "metadata": {
            "episode_number": num,
            "title": ep["title"],
            "guest": guest,
            "guest_role": guest_role,
            "date": ep["date"],
            "duration_minutes": ep["duration_minutes"],
            "youtube_url": ep.get("youtube_url", ""),
            "links": {
                "founders": f"https://www.founderspodcast.com/episodes/{num}",
                "apple_podcasts": APPLE_FND,
                "spotify": SPOTIFY_FND,
            },
        },
        "episode_rating": {"overall": rating},
        "review_notes": "Manual curated batch v4.10",
        "extraction_meta": {
            "model": "manual-curated",
            "transcript_source": "youtube/ytdlp-auto",
            "status": "approved",
            "template_version": "4.10",
        },
        **body,
    }
    yt = ep.get("youtube_url")
    if yt:
        data["metadata"]["links"]["youtube"] = yt
    enrich_metadata(data, ep)
    return data


def bb(ep_id: str, rating: int, guest: str, guest_role: str, **body) -> dict:
    ep = BB[ep_id]
    data = {
        "episode_id": ep_id,
        "podcast": "Business Breakdowns",
        "host": "Matt Reustle & Zack Fuss",
        "metadata": {
            "episode_number": ep["episode_number"],
            "title": ep["title"],
            "guest": guest,
            "guest_role": guest_role,
            "date": ep["date"],
            "duration_minutes": ep["duration_minutes"],
            "youtube_url": ep.get("youtube_url", ""),
            "links": {
                "colossus": ep.get("colossus_url", ""),
                "apple_podcasts": APPLE_BB,
                "spotify": SPOTIFY_BB,
            },
        },
        "episode_rating": {"overall": rating},
        "review_notes": "Manual curated batch v4.10",
        "extraction_meta": {
            "model": "manual-curated",
            "transcript_source": "whisper/base",
            "status": "approved",
            "template_version": "4.10",
        },
        **body,
    }
    enrich_metadata(data, ep)
    return data


SUMMARIES = [
    fnd(
        "fnd-405-how-rockefeller-worked",
        4,
        "John D. Rockefeller",
        "Biography · Standard Oil · Episode 405",
        keywords=["XOM", "Standard Oil", "Refining Scale"],
        conclusion="Senra distills David Freeman Hawke's 1980 Rockefeller biography into roughly 100 operating ideas Munger called the greatest company ever built: business as coded war, teenage ledger obsession, freight rebates as the first moat, and quiet consolidation until 25 refineries appeared in one partnership reveal. Rockefeller's lesson is relentless focus on unit economics — shipping by water at half rail cost, controlling barrels in-house, and outlasting loud partners with patient financing.",
        background="David Senra rereads John D.: The Founding Father of the Rockefellers by David Freeman Hawke (1980) and strips away biography to list how Standard Oil was actually assembled — the approach Charlie Munger praised as the greatest company ever created.\n\nThe monologue walks Rockefeller's Cleveland canvassing days (six days a week knocking on commission houses), his embrace of railroad and telegraph technology, refining-site genius on river plus rail, secret rebate negotiations, and the famous quiet takeover that backed 25 refineries while former partners thought they were winning an auction.",
        important_facts=[
            "Senra cites Hawke's concise Standard Oil narrative and a list of roughly 100 ideas Rockefeller used; Munger called Standard Oil the greatest company ever created. Rockefeller opened letters with battle language, used coded messages, and admitted later that secrecy was too extreme — comparing himself to a general who would never send a brass band ahead of an attack.",
            "As a teenager Rockefeller canvassed Cleveland firms six days a week with letters of introduction, revisiting every office until doors closed; he scrutinized every line item on bills before paying. He chose a refining site on both river and rail because shipping by water cost about 50% less than rail — Senra says location was the secret weapon when freight dominated unit economics.",
            "During a partner breakup Rockefeller quietly lined financing, let rivals bluff at auction, then won the bidding and weeks later newspapers announced a partnership backing 25 refineries worldwide — partners who had been loud and idle were shocked. Vanderbilt, 45 years older and then America's richest man, summoned young Rockefeller to Cleveland only to hear Rockefeller refuse advice because he had tracked every number since childhood."
        ],
        mental_model={
            "name": "Quiet Consolidation at the Margin",
            "components": "Rockefeller treated refining as war fought with ledgers: master posted freight rates through personal negotiation, borrow aggressively to control barrels in-house, and wear down competitors with methodical persistence rather than noise. He cultivated an unaggressive exterior — patient, gracious, never profane — while financing takeovers in secret. Technology edges (telegraph price signals, rail rebates, river shipping) compounded with obsessive cost inspection.",
            "application": "When commodity margins are thin, obsess over the largest cost line — freight and location before brand — and consolidate supply quietly while competitors perform in public auctions. Rockefeller's teenage bill auditing and refusal to be cheated on sloppy practices mirror how durable operators win roll-ups: finance first, confront second, and let newspapers announce the scale after the fact."
        },
        key_insights=[
            {
                "view": "Numbers are the true story.",
                "question": "Why did Rockefeller inspect every bill as a teenager?",
                "answer": "Hawke shows Rockefeller believed numbers reveal reality before narrative; he admonished partners who failed to verify totals and maintained that discipline from commission-house days through Standard Oil. Senra ties the habit to Munger's praise — the company's advantage was accounting-level precision applied to transportation rebates and refining throughput."
            },
            {
                "view": "Transportation is the first moat.",
                "question": "How did site selection compound?",
                "answer": "Rockefeller placed refineries where river and rail met, cutting shipping cost roughly in half versus rail-only rivals. Senra labels freight the largest expense of the era and says Rockefeller spent disproportionate time on routes, rebates, and boat captains — the same way modern operators obsess over the biggest COGS line before marketing."
            },
            {
                "view": "Charm masks consolidation.",
                "question": "What happened in the quiet auction?",
                "answer": "When partners tried to force him out, Rockefeller financed secretly, let them threaten and bluff, then won the asset auction and revealed backing for 25 refineries. Former loud partners had dismissed his empire as small-minded; the episode frames his gracious manner as a deliberate mask over relentless priority focus."
            }
        ],
        top_investment_implications=[
            {
                "ticker": "XOM",
                "direction": "Watch",
                "confidence": "Low",
                "thesis": "Standard Oil's breakup descendants inherited Rockefeller's scale-and-logistics DNA; the episode is historical operating craft (rebates, river routing, quiet roll-ups) rather than a direct ExxonMobil call, but it explains why integrated energy majors still treat transportation and refining coordination as core advantage."
            }
        ],
        golden_quotes=[
            "Rockefeller told Vanderbilt he needed no advice on transactions he had carried since childhood — extreme self-confidence at an age when Vanderbilt was already America's richest man.",
            "His father advised: never mind the crowd; tend your own business — Rockefeller followed that exclusionary focus for life.",
            "Partners thought they won the auction; weeks later newspapers announced Rockefeller's partnership backing 25 refineries worldwide."
        ],
        chronology={
            "subject": "John D. Rockefeller · Standard Oil",
            "events": [
                {"date": "1850s", "event": "Teenage Rockefeller canvasses Cleveland firms six days a week seeking commission-house work."},
                {"date": "1860s", "event": "Embraces telegraph and railroad technology in commodity trading before shifting to oil."},
                {"date": "1860s", "event": "Selects refining sites on river plus rail; pursues freight rebates as core advantage."},
                {"date": "1870s", "event": "Quiet financing and auction strategy consolidates refineries into Standard Oil scale."},
                {"date": "1870s", "event": "Newspapers announce partnership backing 25 refineries after partners underestimated him."},
                {"date": "1980", "event": "Senra sources Hawke biography John D.: The Founding Father of the Rockefellers."}
            ]
        },
    ),
    fnd(
        "fnd-400-the-stubborn-genius-of-james-dyson",
        4,
        "James Dyson",
        "Biography · Against the Odds · Episode 400",
        keywords=["Private:Dyson", "Stubbornness", "5126 Prototypes"],
        conclusion="Episode 400 marks nine years and 400 founder biographies for Senra; Dyson's second autobiography reframes vision as stubbornness — retain total control, prototype through 5,126 vacuum iterations, and sell half-finished products to learn from customers. Fry's lake-plank experiments and Brunel's impossible projects supply the mental model: expertise is optional when obsession and iteration compound.",
        background="David Senra celebrates episode 400 by rereading James Dyson's two autobiographies — Against the Odds first, a second written roughly 20 years later — and naming the episode for Dyson's line that vision might equally be stubbornness.\n\nSenra contrasts Dyson's anti-business-business philosophy (beautiful, useful objects) with Jeremy Fry mentorship at Bath: lake tests instead of hydrodynamics experts, ballbarrow departure from a stable job, 5,126 vacuum prototypes, and the principle of retaining control rather than licensing early.",
        important_facts=[
            "Senra took nine years to reach episode 400 and estimates 400 founder biographies read; Dyson's Against the Odds remains his top recommendation. Dyson writes that vision might equally be stubbornness and that his business philosophy is 'a book against business' filled with ugly, useless objects — difference and retention of total control summarize his approach.",
            "Mentor Jeremy Fry told young Dyson to tow a plank behind a Land Rover on the lake instead of hiring hydrodynamics experts; Dyson proceeded through preliminary sketches and prototypes until iterations worked extremely quickly. The bagless vacuum required 5,126 prototypes over years before success.",
            "Dyson left a high-paying job to pursue the ballbarrow (a wheel that does not sink in mud) despite partner pressure to stop wholesale selling; he argues entrepreneurs must tolerate excessive risk, sell finished-ish products for customer feedback, and keep control rather than license inventions early."
        ],
        mental_model={
            "name": "Stubborn Iteration With Control",
            "components": "Dyson pairs misfit contrarianism with Fry-style empirical testing — lake planks, workshop access, no expert committees — and refuses to release control at the moment an idea strikes. He studies invention history (Brunel, encyclopedias of great inventions) for perseverance fuel, runs daily stamina-building routines, and treats failure fear as competitive fuel through product cycles.",
            "application": "When experts say stop, prototype one more version and sell a rough product to real users if it carries learning value. Dyson's 5,126 vacuum iterations and ballbarrow leap show that retaining ownership of engineering and distribution matters more than early licensing revenue — stubbornness is a feature when paired with customer-facing iteration."
        },
        key_insights=[
            {
                "view": "Vision equals stubbornness.",
                "question": "Why does Dyson reject the arrogance label?",
                "answer": "He asks readers to celebrate stubbornness instead — claiming only virtues of a mule. Senra names the episode from that sentence because Dyson's career is persistence through ridicule: anti-expert testing, thousands of prototypes, and refusal to follow herd advice from shareholders or partners."
            },
            {
                "view": "Experts are optional.",
                "question": "What did Fry teach at the lake?",
                "answer": "When Dyson suggested hiring a hydrodynamics specialist, Fry pointed to the lake and a Land Rover — test the plank yourself. Senra says Dyson applied the same modus operandi for decades: enthusiasm plus intelligence beat credentialed committees for original products."
            },
            {
                "view": "Control beats early licensing.",
                "question": "What is Dyson's single-sentence strategy?",
                "answer": "Difference plus retention of total control — do not hand off the idea when it strikes. Licensing and partner-driven wholesale nearly killed early ventures; owning manufacturing and brand let Dyson compound industrial design into a global appliance company."
            }
        ],
        top_investment_implications=[
            {
                "ticker": "Private:Dyson",
                "direction": "Watch",
                "confidence": "Low",
                "thesis": "Private Dyson illustrates premium consumer hardware built by iterative R&D and brand control rather than outsourced manufacturing — relevant for investors tracking durable family-owned product companies, not a tradable equity thesis from this episode."
            }
        ],
        golden_quotes=[
            "Dyson: vision might equally well be stubbornness — celebrate stubbornness, not arrogance.",
            "Fry on hydrodynamics: the lake is there; take a plank and tow it behind the Land Rover.",
            "5,126 prototypes separated Dyson from the bagless vacuum that finally worked."
        ],
        chronology={
            "subject": "James Dyson · Against the Odds",
            "events": [
                {"date": "Youth", "event": "Father dies when Dyson is nine; Fry becomes engineering mentor at Bath."},
                {"date": "1970s", "event": "Ballbarrow project — leaves stable job; resists partner pressure to abandon wholesale."},
                {"date": "1970s-80s", "event": "5,126 vacuum prototypes before commercial bagless design succeeds."},
                {"date": "2000s", "event": "Second autobiography written ~20 years after Against the Odds."},
                {"date": "2025", "event": "Senra records episode 400 on Dyson's stubborn-genius philosophy."}
            ]
        },
    ),
    fnd(
        "fnd-159-andy-grove-intel",
        5,
        "Andy Grove",
        "Biography · Swimming Across · Episode 159",
        keywords=["INTC", "Swimming Across", "Only the Paranoid Survive"],
        conclusion="Swimming Across is Senra's pick for Grove's pre-Intel life: Budapest regime changes, a father who disappeared on the Russian front, 200,000 refugees after the 1956 revolution, and a professor who pointed him to San Francisco. Fairchild to Intel followed — Grove became CEO for 11 years and Time Man of the Year in 1997 — but the episode's core is endurance: immigrants swim across lakes with help, setbacks, and no resentment at success.",
        background="David Senra reads Andy Grove's autobiography Swimming Across after Walter Isaacson's Innovators rekindled interest. Grove opens by listing Hungarian fascism, Nazi occupation, Soviet siege, communist regimes, and the 1956 uprising crushed in 13 days — 200,000 Hungarians fled west; Grove was one.\n\nThe narrative covers his father disappearing with 90% mortality in Jewish labor battalions, childhood air raids in Budapest, escape to New York then Berkeley, Fairchild Semiconductor, Intel's founding, 11 years as CEO, U.S. citizenship, and book royalties donated to refugee aid.",
        important_facts=[
            "Grove was born in Budapest in 1936; by age 20 he had lived through fascist dictatorship, Nazi occupation, Soviet siege, and the 1956 revolution ended in 13 days with 200,000 Hungarians escaping west. His father was conscripted to the Russian front in Jewish labor battalions; Grove later learned roughly 90% did not return.",
            "After reaching New York Grove moved to UC Berkeley on scholarships, joined Fairchild Semiconductor, then co-founded Intel, rose to CEO for 11 years, and became a U.S. citizen. Time magazine named him Man of the Year in 1997; he notes no one resented his immigrant success as he progressed.",
            "Grove fell in love with the Bay Area driving through the Sierra Nevada — 'the words jumped out of the Karl May books' — and lived there ever since. Swimming Across royalties go to refugee support; he wrote the memoir after grandchildren arrived, framing life as swimming across a lake with setbacks and help from others."
        ],
        mental_model={
            "name": "Power to Endure",
            "components": "Extreme early instability — missing fathers, ghetto play reenactments, bombing raids — forged Grove's later management realism at Intel. He treats survival as continued swimming: scholarships, mentors, geographic reinvention (New York to California), and channeling fear into work rather than grievance. Endurance plus paranoia about industry transitions becomes the operating system.",
            "application": "Operators facing platform shifts can study Grove's biography as proof that personal catastrophe tolerance translates into corporate turnaround discipline — but the episode emphasizes immigration gratitude and mentor-enabled reinvention over tactical Intel management quotes."
        },
        key_insights=[
            {
                "view": "Endurance precedes paranoia.",
                "question": "Why does Senra call this a power-to-endure book?",
                "answer": "A New York Times review line frames Grove's early life — regime changes, father's disappearance, revolution escape — as commentary on enduring impossible environments before Fairchild and Intel. The management books make more sense once you understand centralized-economy survival skills."
            },
            {
                "view": "Mentors redirect geography.",
                "question": "How did Grove reach California?",
                "answer": "He loved America but hated New York weather; a professor described San Francisco, leading Grove to pile into an old car toward Berkeley after graduation. That single redirect placed him in Fairchild's orbit and the Intel founding circle."
            },
            {
                "view": "Success without resentment.",
                "question": "What surprised Grove about America?",
                "answer": "He writes that as he advanced through school and Intel, no one resented his immigrant success — scholarships opened doors, citizenship followed, and Time's 1997 honor capped a life he describes as still swimming with help from others."
            }
        ],
        top_investment_implications=[
            {
                "ticker": "INTC",
                "direction": "Watch",
                "confidence": "Low",
                "thesis": "Grove's Intel CEO era (11 years, semiconductor leadership) contextualizes INTC as a company built by immigrants who endured catastrophic personal risk — useful cultural background for turnaround investors, not a directional call from this autobiography-focused episode."
            }
        ],
        golden_quotes=[
            "Grove: by age 20 I had lived through Hungarian fascism, Nazi occupation, Soviet siege, and a revolution put down at gunpoint.",
            "His father disappeared at the Russian front; roughly 90% of Jewish labor battalion conscripts did not return.",
            "I managed to swim across the lake — not without effort, not without setbacks, and with a great deal of help."
        ],
        chronology={
            "subject": "Andy Grove · Swimming Across · Intel",
            "events": [
                {"date": "1936", "event": "Born in Budapest under right-wing dictatorship aligned with Nazi Germany."},
                {"date": "1942-43", "event": "Father conscripted; letters stop; official notice says he disappeared at the front."},
                {"date": "1944-45", "event": "Nazi occupation and Budapest bombing; Soviet army takes city April 1945."},
                {"date": "1956", "event": "Hungarian Revolution lasts 13 days; Grove escapes west with ~200,000 refugees."},
                {"date": "1960s", "event": "UC Berkeley graduate school; Fairchild Semiconductor job."},
                {"date": "1968+", "event": "Intel co-founder; CEO for 11 years; Time Man of the Year 1997."}
            ]
        },
    ),
    fnd(
        "fnd-132-edwin-land-steve-jobs-s-hero",
        4,
        "Edwin Land",
        "Biography · Polaroid · Episode 132",
        keywords=["Private:Polaroid", "SX-70", "Instant Photography"],
        conclusion="Senra opens a three-part Land series with The Instant Image: high technological drama as SX-70 burned millions without revenue, problems renamed opportunities, and Land treated Polaroid as experience not hardware. Jobs modeled himself on Land — no college degree, perfectionism, secrecy, shareholder letters as poetry — and Land's rule that anything worth doing is worth doing to excess explains both Polaroid's peaks and its later strain.",
        background="David Senra reads a 42-year-old copy of The Instant Image: Edwin Land and the Polaroid Experience, starting a three-part Land arc after listener Dustin mapped every Land biography. Fortune called SX-70 the biggest consumer gamble ever; Land reframed problems as opportunities while millions poured into manufacturing pain.\n\nThe episode ties Land to Steve Jobs — national treasure status, shrine-like meetings, instant camera secrecy paralleling iPhone development — and quotes Land's excess rule, group-originality skepticism, and ambition to make cameras as common as telephones.",
        important_facts=[
            "At SX-70's 1971 crisis Land called Polaroid's situation 'high technological drama' while the system had cost millions and not yet returned a dime; Fortune labeled it the biggest gamble on a consumer product. Land replaced the word problem with opportunity in his vocabulary during lean years after dazzling early success.",
            "Steve Jobs hailed Land as a national treasure and told reporters meeting him was like visiting a shrine; Jobs modeled careers after Land's perfectionism, marketing showmanship, and secrecy — Polaroid cameras developed in secret like later iPhones. Land was roughly 70 in the period covered yet still driving instant photography bets.",
            "Land's Harvard Business Review stance: no group originality — creativity is individual. He told a 1972 annual meeting his fantasy was cameras as widely used as telephones; Polaroid film carried roughly 60–80% margin in the Kodak comparison Senra cites from the book's competitive passages."
        ],
        mental_model={
            "name": "Experience Company, Not Product Company",
            "components": "Land sells technological drama and human connection — partners exploring a once-empty planet — not specifications. He ignores experts who judge only existing markets, believing ingenious products create new markets. Secrecy, superlative language, and doing worthy things to excess compound until manufacturing scale and consumer economics bite.",
            "application": "Founders chasing radical hardware should expect years of negative cash flow while renaming engineering crises as opportunities — and should study Land as both inspiration (Jobs) and caution (Polaroid unprepared for lean times after SX-70 scale-up)."
        },
        key_insights=[
            {
                "view": "Markets follow ingenious products.",
                "question": "Why did experts predict Polaroid failures?",
                "answer": "They judged new cameras against existing photography markets; Land believed sufficiently ingenious products create their own demand — instant imaging defined a category Kodak underestimated until film margins woke them up."
            },
            {
                "view": "Jobs's template is Land.",
                "question": "How did Jobs describe Land?",
                "answer": "Jobs called Land a national treasure and compared meetings to visiting a shrine; both lacked college degrees, demanded perfection, used secrecy for breakthrough launches, and treated shareholder communication as experience narrative, not metrics alone."
            },
            {
                "view": "Excess is strategy.",
                "question": "What rule did Land live by?",
                "answer": "If anything is worth doing, it's worth doing to excess — SX-70 spend, telephone-scale camera ambition, and refusal to use anything but superlatives in public statements show Land optimizing for breakthrough experience over incremental P&L calm."
            }
        ],
        top_investment_implications=[
            {
                "ticker": "Private:Polaroid",
                "direction": "Watch",
                "confidence": "Low",
                "thesis": "Polaroid's rise-and-strain arc is a case study in experience-led hardware with film-like recurring margins; no public Polaroid equity remains, but Land's SX-70 gamble informs how investors should underwrite long R&D ramps in consumer tech."
            }
        ],
        golden_quotes=[
            "Land on SX-70: high technological drama — millions spent, not yet a dime returned.",
            "If anything is worth doing, it's worth doing to excess.",
            "Jobs on Land: meeting him was like visiting a shrine."
        ],
        chronology={
            "subject": "Edwin Land · Polaroid · SX-70",
            "events": [
                {"date": "1930s-40s", "event": "Polarizing filter invention seeds Polaroid; Land ignores expert market sizing."},
                {"date": "1948+", "event": "Instant camera category established; dazzling growth precedes later lean years."},
                {"date": "1971", "event": "SX-70 crisis — manufacturing pains, negative cash flow, Land's drama framing."},
                {"date": "1972", "event": "Annual meeting: fantasy of cameras as ubiquitous as telephones."},
                {"date": "1980s", "event": "Senra's Instant Image source book published; Jobs parallels widely discussed."},
                {"date": "2020", "event": "Founders episode 132 opens three-part Land series."}
            ]
        },
    ),
    fnd(
        "fnd-38-the-space-barons-elon-musk-jeff-bezos-and-the-quest-to",
        4,
        "Elon Musk & Jeff Bezos",
        "Biography · The Space Barons · Episode 38",
        keywords=["AMZN", "TSLA", "Blue Origin"],
        conclusion="Davenport's Space Barons pairs Bezos the secretive tortoise with Musk the audacious hare: vertical rocket landings reignited space hope, while 2003 Blue Origin land hunts happened as Amazon passed a trillion-dollar market cap critics once mocked. Senra stresses criticism immunity (Amazon.bomb headlines), Bezos's 2003 analogy that the web was like electricity in 1908, and the closing thesis that rivalry — not consolation — is the best rocket fuel for Mars-scale ambitions.",
        background="David Senra reads Christian Davenport's The Space Barons, combining Musk and Bezos in one episode because the book contrasts their styles throughout. The intro celebrates two vertical rocket landings within a month after decades of disposable stages.\n\nCoverage includes 2003 Bezos helicopter near-crash while scouting Texas land for Blue Origin, Amazon get-big-fast discipline versus press mockery, Bezos defending NASA while funding reusable rockets, Musk plowing ahead publicly, and Kennedy-era competition as precedent for why billionaires need a rival at the shoulder.",
        important_facts=[
            "Davenport opens with two vertical rocket landings less than a month apart — first stages previously ditched in the ocean; Musk and Bezos treat that as waste akin to scrapping airliners after one flight. Bezos kept Blue Origin clandestine while Musk occupied center stage with SpaceX triumphs and failures.",
            "Around early 2003 Bezos scouted Texas property by helicopter nearly dying in a crash he later called a silly way to die; Amazon segments grew double digits while BusinessWeek and Barron's ran Amazon.toast and Amazon.bomb covers — Senra notes Amazon later exceeded a trillion-dollar market cap as Bezos became world's richest person.",
            "Bezos compared the 2003 web to electricity circa 1908 — sockets not yet standardized — arguing optimism if AWS-scale platforms were still ahead; Davenport interviewed four billionaires (Musk, Bezos, Branson, Allen) but Senra omits Branson and Allen. Closing thesis: Musk and Bezos need each other because rivalry is the best rocket fuel, echoing Kennedy's race after Gagarin."
        ],
        mental_model={
            "name": "Tortoise and Hare Rocket Fuel",
            "components": "Bezos builds secretively with Amazon-style long horizon; Musk publicizes bold timelines and forces industry reaction. Both recycle hardware to cut space access costs and chase multi-planetary or heavy-industry-off-Earth visions. External ridicule (Amazon.bomb) and internal near-death experiences (helicopter crash) do not derail capital allocation to passion projects.",
            "application": "When building category-defining infrastructure, expect mockery at inflection points and pair patience with visible competitive pressure — Bezos and Musk accelerate each other because neither wants to lose the second space race narrative."
        },
        key_insights=[
            {
                "view": "Critics lack predictive power.",
                "question": "Why cite Amazon.bomb today?",
                "answer": "Senra uses Bezos's 1990s magazine ridicule versus trillion-dollar market cap as weekly proof that founders must internalize criticism without obeying it — if Bezos faced it, operators should expect external doubt while investing in long-term platforms."
            },
            {
                "view": "Internet still early in 2003.",
                "question": "What was Bezos's electricity analogy?",
                "answer": "He argued the 2003 web resembled electricity in 1908 before standardized sockets — implying AWS and merchant platforms were nascent. That framing justified Blue Origin land buys and continued heavy reinvestment despite profitability debates."
            },
            {
                "view": "Rivals accelerate timelines.",
                "question": "Why combine Musk and Bezos in one episode?",
                "answer": "Davenport structures the book as comparison; legal skirmishes, landing milestones, and pad disputes feed motivation. Senra closes that consolation talk is false — competition drove Apollo after Sputnik and is the propellant for the next giant leap."
            }
        ],
        top_investment_implications=[
            {
                "ticker": "AMZN",
                "direction": "Long",
                "confidence": "Medium",
                "thesis": "Bezos's 2003 confidence — double-digit segment growth while funding Blue Origin — reinforces Amazon as a cash-flow engine that subsidizes optional long-horizon bets; episode supports enduring reinvestment culture more than near-term AWS multiples."
            },
            {
                "ticker": "TSLA",
                "direction": "Watch",
                "confidence": "Low",
                "thesis": "Musk's SpaceX narrative parallels Tesla's public-goal-driven strategy; episode is biography not an auto thesis, but illustrates how Musk uses visible rivals to marshal capital and talent toward physics-limited missions."
            }
        ],
        golden_quotes=[
            "Bezos after helicopter crash: what a silly way to die — while scouting Texas land for Blue Origin in 2003.",
            "Amazon.bomb magazine covers versus trillion-dollar market cap decades later.",
            "Rivalry, it turned out, was the best rocket fuel."
        ],
        chronology={
            "subject": "Musk · Bezos · Space Barons",
            "events": [
                {"date": "2003", "event": "Bezos scouts Texas; helicopter crash; Amazon posts double-digit segment growth."},
                {"date": "2003", "event": "Bezos compares web to electricity industry circa 1908; Blue Origin stays secret."},
                {"date": "2010s", "event": "SpaceX and Blue Origin achieve vertical landings weeks apart."},
                {"date": "2010s", "event": "Legal and Twitter skirmishes over landing significance and launch pads."},
                {"date": "2018", "event": "Senra records episode 38 on Davenport's comparative biography."}
            ]
        },
    ),
    fnd(
        "fnd-8-the-intel-trinity-how-robert-noyce-gordon-moore-and-and",
        4,
        "Robert Noyce",
        "Biography · Intel Trinity · Episode 8",
        keywords=["INTC", "Fairchild", "Moores Law"],
        conclusion="Senra focuses The Intel Trinity on Robert Noyce — Jobs's mentor and 'mayor of Silicon Valley' — rather than Gordon Moore or Andy Grove alone. Noyce co-founded Fairchild and Intel, charmed competitors on live TV, mentored Jobs through exile after Macintosh, and died June 1990 days after Sematech honored him; Apple's tribute called him the model every rebel entrepreneur wanted to become.",
        background="David Senra reads Michael Malone's The Intel Trinity but centers Robert Noyce after Isaacson's Jobs biography sparked interest. Intel was founded by Noyce and Moore; Grove operationalized later — yet 90% of Senra's notes cover Noyce's character.\n\nStories include Jobs camping at the Noyce home for mentorship without PC advice, Noyce as beloved Fairchild/Intel figure, Sematech government partnership against Japanese competition, chain-smoking stress, and sudden death after Sematech declared Bob Noyce Day June 1 1990.",
        important_facts=[
            "Steve Jobs sought Noyce as a father figure after exile from Apple — Next struggled and Jobs risked being forgotten in his 30s without another hit. Noyce let Jobs crash at events, fly in his CES plane (nearly flipping on landing), and absorb how to be successful and beloved unlike Jobs's abrasive early style.",
            "Noyce co-founded Fairchild Semiconductor and Intel with Gordon Moore; Malone frames Intel as inventing mass-produced complex chips at billion-unit scale with Moore's Law pace. Noyce was called mayor of Silicon Valley for being successful without Jobs-like cruelty — Apple later said he was the giant who provided the model for everything they wanted to become.",
            "Late career Noyce led Sematech with hundreds of millions in government support fighting Japanese semiconductor advantages; employees celebrated Bob Noyce Day June 1 1990 with T-shirts quoting a Mercury News pedestal line. He died Sunday June 3 1990 after swimming and lying down tired — Apple's comment called him the ultimate inventor, rebel, and entrepreneur."
        ],
        mental_model={
            "name": "Beloved Builder",
            "components": "Noyce combines Fairchild transistor lineage, Intel scaling culture, and personal warmth that attracts mentees and employees without intimidation. He competes publicly with confidence (TV challenges to top his demo) yet shares credit — contrasting Jobs's reality distortion without hostility. Government-industry coalitions appear when national supply chains threaten valley winners.",
            "application": "Leadership models in tech are plural: Noyce proves you can win semiconductor revolutions while being liked — useful for founders who want high performance without burning bridges required for decades-long mentor networks."
        },
        key_insights=[
            {
                "view": "Jobs needed a beloved model.",
                "question": "Why did Jobs pursue Noyce?",
                "answer": "After Apple exile Jobs wanted vision for living successfully in the valley without ridicule — Noyce had already founded two fundamental companies and was universally liked, something Jobs's early Apple behavior lacked."
            },
            {
                "view": "Moore's Law needs operators.",
                "question": "Where do Moore and Grove fit?",
                "answer": "Intel's founding pair is Noyce and Moore (Moore's Law namesake); Grove's operational intensity came later. Episode skews Noyce because Malone's anecdotes and Jobs mentorship supply the richest founder lessons."
            },
            {
                "view": "National industrial policy returns.",
                "question": "What was Sematech's role?",
                "answer": "Japanese government-backed competition threatened U.S. fabs; Noyce led a coalition with hundreds of millions in government funds — showing that even valley icons sometimes need public-private defense when supply chains shift."
            }
        ],
        top_investment_implications=[
            {
                "ticker": "INTC",
                "direction": "Watch",
                "confidence": "Low",
                "thesis": "Intel's cultural origin — Noyce's fairchild lineage and Moore's Law cadence — frames INTC as a national champion grown from mentor-network silicon; historical context for investors tracking fab politics, not a 2025 earnings call."
            }
        ],
        golden_quotes=[
            "Jobs on Noyce: he was the soul of Intel — I wanted to smell that wonderful second era of the valley.",
            "Noyce on TV after a demo: now let's see if you can top that one — friendly competitive confidence.",
            "Apple after his death: he was the ultimate inventor, rebel, and entrepreneur — the model for everything we wanted to become."
        ],
        chronology={
            "subject": "Robert Noyce · Intel · Fairchild",
            "events": [
                {"date": "1950s-60s", "event": "Fairchild Semiconductor era; Noyce transistor and planar process fame."},
                {"date": "1968", "event": "Intel founded by Noyce and Gordon Moore."},
                {"date": "1984", "event": "Jobs exiled from Apple; begins seeking Noyce mentorship."},
                {"date": "1988-90", "event": "Noyce leads Sematech coalition vs Japanese semiconductor rise."},
                {"date": "1990-06-01", "event": "Sematech declares Bob Noyce Day; celebration with employee T-shirts."},
                {"date": "1990-06-03", "event": "Noyce dies after swimming at home Sunday afternoon."}
            ]
        },
    ),
    bb(
        "bb-intuitive-surgical-robotic-precision",
        4,
        "Joe Thomas",
        "Analyst · 91 Capital",
        keywords=["ISRG", "Da Vinci", "Robotic Surgery"],
        conclusion="Joe Thomas of 91 Capital frames Intuitive Surgical at roughly $140 billion market cap as the robotic soft-tissue winner: ~100% share in approved procedures, 8,500 Da Vinci systems globally, and $7 billion revenue split 60% instruments / 25% systems. With 2.3 million procedures in 2023 and 14 million lifetime cases feeding algorithms, the moat is data plus surgeon trust — yet penetration is only ~10% of a 7-million-procedure addressable market.",
        background="Matt Reustle breaks down Intuitive Surgical with Joe Thomas, analyst at investment manager 91. Thomas explains Da Vinci robots for minimally invasive abdominal surgery, the evolution from open to laparoscopic to robotic, and why the fulcrum effect made manual lap tools unintuitive.\n\nThey size global surgery (~200–300 million procedures, ~7 million addressable soft-tissue), Intuitive's 2.3 million 2023 procedures, $1.4–1.5 million system ASP, leasing plus upgrade clauses derisking hospital purchases, Ion lung-biopsy platform growth, and ~70% gross margins with R&D near 14% of sales.",
        important_facts=[
            "At recording Intuitive traded near a $140 billion market cap at all-time highs; Thomas cites ~100% share in robotic soft-tissue surgery with 8,500 Da Vinci systems installed globally and system ASP around $1.4–1.5 million. 2023 placements approached 1,400 systems generating about $1.6 billion system revenue.",
            "Worldwide there are roughly 200–300 million surgical procedures annually; about 7 million are addressable soft-tissue cases where robotics is approved and economical. Intuitive performed 2.3 million Da Vinci procedures in 2023; instruments tied to those cases generated over $4 billion revenue — total company revenue about $7 billion (60% instruments, 25% systems, remainder service).",
            "Thomas notes ~70% gross margins, R&D near 14% of sales, SG&A near 26%, and 14 million cumulative Da Vinci procedures feeding product development. Ion bronchoscopy grew from near zero in 2019 to 54,000 procedures last year (~10x in three years) while core robotics penetration remains roughly 10% of addressable procedures."
        ],
        mental_model={
            "name": "Procedure Volume Compounder",
            "components": "Intuitive earns razor-blade economics after selling million-dollar consoles: each procedure pulls proprietary instruments and service contracts with high switching costs once surgeons trust staplers and sealers. Leasing and contractual upgrade paths smooth hospital capex scares. Competitors entered late while Intuitive filled tool gaps (stapling, energy) and accumulated impossible-to-replicate case data.",
            "application": "Medtech investors can map Intuitive as a installed-base annuity — growth equals penetration times procedures per system times instrument intensity — with Ion as a second platform option in lung cancer diagnostics where J&J shares flexible bronchoscopy share."
        },
        key_insights=[
            {
                "view": "Data moat scales with cases.",
                "question": "Why does 14 million procedures matter?",
                "answer": "Thomas argues competitors lack Intuitive's historical case database feeding algorithms and training; trust in stapling and vessel sealers took years because surgeons fear re-admissions from failed staples — first-mover data and reliability reinforce ~100% share."
            },
            {
                "view": "Penetration still low.",
                "question": "Is the market saturated?",
                "answer": "Despite dominance, robotics is only ~10% penetrated in a 7-million-procedure addressable pool growing from open and lap conversion — headroom remains even at $140 billion valuation."
            },
            {
                "view": "Leasing derisks upgrades.",
                "question": "How did Intuitive smooth capex cycles?",
                "answer": "Leasing and upgrade clauses reduce hospital fear of buying a system right before a new generation launches — smoothing placements after earlier volatile upgrade spikes between Da Vinci generations."
            }
        ],
        top_investment_implications=[
            {
                "ticker": "ISRG",
                "direction": "Long",
                "confidence": "Medium",
                "thesis": "Thomas's breakdown supports ISRG as a procedure-volume compounder with 70% gross margins, instrument-heavy revenue mix, and decade-long data moat — tempered by premium valuation at all-time highs and Ion competition from J&J in bronchoscopy."
            }
        ],
        golden_quotes=[
            "Thomas: Da Vinci holds essentially 100% share in robotic soft-tissue surgery — yet only ~10% of addressable procedures use robotics.",
            "14 million cumulative Da Vinci procedures feed development — competitors cannot replicate that history quickly.",
            "Fulcrum effect: laparoscopic tools reverse rotation through keyholes — the unintuitive problem Da Vinci was named to solve."
        ],
        chronology={
            "subject": "Intuitive Surgical · Da Vinci",
            "events": [
                {"date": "1910+", "event": "Laparoscopic surgery emerges; fulcrum effect challenges precision."},
                {"date": "1990s", "event": "Robotic surgery development; Intuitive founded around Da Vinci platform."},
                {"date": "2010s", "event": "Stapling and energy tools close hybrid-procedure gaps; competitors slow to respond."},
                {"date": "2019-23", "event": "Ion bronchoscopy scales from near zero to 54,000 procedures (~10x in three years)."},
                {"date": "2023", "event": "2.3 million Da Vinci procedures; ~$7 billion total revenue."},
                {"date": "2024", "event": "Business Breakdowns episode at ~$140 billion market cap."}
            ]
        },
    ),
    bb(
        "bb-amazon-aggregators-buying-third-party-sellers",
        3,
        "Ali Ahmed",
        "Partner · CoVenture",
        keywords=["AMZN", "FBA Roll-Up", "Third-Party Sellers"],
        conclusion="CoVenture's Ali Ahmed sizes Amazon third-party sellers at roughly $300 billion revenue growing faster than Amazon itself — ~$60 billion EBITDA at ~20% margins — while only ~$8 billion of aggregator funding chases the space at 4–6x EBITDA. Aggregators buy FBA storefronts (ASINs, reviews, inventory) and add Amazon-native playbooks: international review porting, DSP ads, and supply-chain redundancy rather than cost synergies.",
        background="Jesse Pooji hosts Ali Ahmed of CoVenture to explain Amazon aggregators — roll-ups of FBA businesses since Thrasio's 2018 founding. Ahmed contrasts reseller, vendor, and FBA models, emphasizing that ~40% of a seller's revenue often flows to Amazon for fulfillment and fees while Amazon earns higher margins on third-party than first-party sales.\n\nThey discuss $300 billion third-party GMV, 15–25% net margins, debt capacity potentially in the hundreds of billions at conservative leverage, pod-based org charts, and why Amazon avoids competing on tiny category share gains that aggregators pursue.",
        important_facts=[
            "Ahmed cites roughly $300 billion annual revenue from Amazon third-party sellers growing 30–50% year over year — faster than Amazon overall — with typical 15–25% net margins (~20% midpoint) implying about $60 billion addressable EBITDA. Only around $8 billion of funding has entered aggregators versus that EBITDA pool, with acquisitions often at 4–6x EBITDA.",
            "FBA sellers design products, manufacture abroad, store in Amazon warehouses, and sell via storefronts aggregators buy — acquiring ASINs, SKUs, inventory, and reviews. Ahmed notes about 40% of seller revenue can go to Amazon fees and services while Amazon reports higher margins on third-party than first-party retail.",
            "Value creation is revenue-side, not cost synergies: international expansion (porting 50,000 U.S. reviews to France or Japan), sophisticated PPC and DSP access, and supply-chain redundancy. Ahmed's firm backs multiple aggregators (Wonder Brands, Aqico, Benitago, D1) and stresses operators need 15% core growth to stay interesting to capital."
        ],
        mental_model={
            "name": "Amazon-Native Roll-Up",
            "components": "Aggregators arbitrage solo founders who hit scale limits on marketing language, international expansion, and ad tooling. Capital markets underfund the EBITDA pool relative to franchising analogies; leverage runs high on stable FBA cash flows (80–90% advance rates on 4x purchase multiples). Amazon's strategic indifference to small category share lets roll-ups improve listings without triggering first-party competition.",
            "application": "Investors treat the space as buy-and-build on marketplace cash flows — diligence is Googleable because $300 billion GMV is visible — but winner-take-most dynamics favor operators with 100-step playbooks and Amazon-specific ad stack expertise, not generic PE cost cutting."
        },
        key_insights=[
            {
                "view": "Funding gap versus EBITDA.",
                "question": "Why is capital still early?",
                "answer": "Ahmed contrasts ~$8 billion raised against ~$60 billion EBITDA today and potential trillion-dollar enterprise value at scale — multiples stay low because direct lenders and BDCs only recently underwrite FBA cash flows at high advance rates."
            },
            {
                "view": "Amazon likes third-party.",
                "question": "Does Amazon compete with sellers?",
                "answer": "Amazon Basics fills gaps, but Ahmed argues Amazon earns better margins as third-party infrastructure (warehousing, payments, shipping) without inventory risk — reducing incentive to crush successful FBA brands except when categories are strategic."
            },
            {
                "view": "Revenue playbook beats cost cuts.",
                "question": "Where do aggregators add value?",
                "answer": "Not procurement synergies — most lifts come from international review porting, DSP campaigns, stock-out prevention, and 150-step operational playbooks individual founders cannot staff."
            }
        ],
        top_investment_implications=[
            {
                "ticker": "AMZN",
                "direction": "Long",
                "confidence": "Medium",
                "thesis": "Aggregator growth validates Amazon's third-party flywheel — higher-margin fee revenue without inventory risk — supporting AMZN marketplace take rate durability as FBA GMV compounds toward Ahmed's half-trillion to trillion-dollar market-value scenario."
            }
        ],
        golden_quotes=[
            "Ahmed: ~$300 billion third-party seller revenue — only ~$8 billion of aggregator funding chasing ~$60 billion of EBITDA.",
            "Port 50,000 U.S. reviews to Japan and you can be number one overnight — obvious at scale, impossible for bootstrapped sellers.",
            "Amazon makes higher margins on third-party sales than on many first-party items — about 40% of seller revenue flows to Amazon."
        ],
        chronology={
            "subject": "Amazon FBA · Aggregators",
            "events": [
                {"date": "1990s-2000s", "event": "Amazon opens to third-party sellers; evolves FBA fulfillment model."},
                {"date": "2018", "event": "Thrasio founded — aggregator category begins."},
                {"date": "2020s", "event": "Dozens of roll-ups raise equity and debt; 4–6x EBITDA acquisitions common."},
                {"date": "2021", "event": "Business Breakdowns records aggregator category episode with CoVenture."},
                {"date": "2020s", "event": "Ahmed cites $300B GMV, 30–50% growth, and massive underfunding versus EBITDA."}
            ]
        },
    ),
]


def main() -> None:
    for data in SUMMARIES:
        save_and_publish(data, publish=True)
    print("Done:", len(SUMMARIES), "episodes")


if __name__ == "__main__":
    main()
