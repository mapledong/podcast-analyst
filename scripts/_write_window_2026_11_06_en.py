#!/usr/bin/env python3
"""ILTB 498, Founders 439, SV101 E257 — last two weeks as of 2026-11-06."""
from __future__ import annotations

import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))
from scripts._window_lib import dump, en_std, validate_file  # noqa: E402
from src.chinese_transcript import load_transcript_body, quote_supported_in_transcript, transcript_path  # noqa: E402

ILTB_APPLE = "https://podcasts.apple.com/podcast/invest-like-the-best-with-patrick-o-shaughnessy/id1154105909"
FND_APPLE = "https://podcasts.apple.com/podcast/founders/id1141877104"
SV_APPLE = "https://podcasts.apple.com/cn/podcast/id1498541229"


def check(eid, quotes):
    body = load_transcript_body(transcript_path(eid))
    for q in quotes:
        ok = quote_supported_in_transcript(q, body)
        print(eid, "OK" if ok else "FAIL", q)
        if not ok:
            raise SystemExit(q)


def ep498():
    eid = "ep498"
    meta = {
        "episode_number": 498,
        "title": "Martin Casado — Frontier Model Economics, the Slowdown, and the Cursor Deal",
        "guest": "Martin Casado",
        "guest_role": "General partner, a16z · infrastructure",
        "date": "2026-11-04",
        "duration_minutes": 65,
        "youtube_url": "https://www.youtube.com/watch?v=XZxDawMm4lU",
        "links": {
            "youtube": "https://www.youtube.com/watch?v=XZxDawMm4lU",
            "apple_podcasts": ILTB_APPLE,
        },
    }
    concl = (
        "Casado sorts venture into four mindsets: spreadsheet finance, productive assets, "
        "1960s frontier bets, and pure timing. He says the finance mindset is being applied "
        "too early. Defensibility is second-order while a market still grows. Frontier models "
        "have taken 80% or more of dollar-weighted spend for three years, at about 1% of "
        "enterprise budget. A model's commercial life is three to six months, so a six-month "
        "Anthropic slip can zero the last release. Saturated coding tasks do not imply a cheaper "
        "model; rivals still pay for the smartest. Cursor cleared on users, data, and compute, "
        "not an auction."
    )
    bg = (
        "EP498, Nov 4. Casado has spent about a decade and hundreds of deals on computer-science "
        "infrastructure only. He sold Nicira to VMware for $1.26 billion, later sat on the "
        "Tabular-to-Databricks sale, and now walks Cursor, World Labs, and Open Router as the "
        "recent strategic set. Patrick calls the frame productive investing."
    )
    facts = [
        (
            "Four mindsets, then the shape of a moat. Finance uses the market and the spreadsheet "
            "as a proxy for the whole business — SaaS metrics and TAM — and Casado now sees that "
            "habit in Series A rooms, which he calls discordant. Productive investors underwrite "
            "the asset: technical approach, adjacent budgets, speed, team, partial willingness to "
            "pay before COGS is known. Frontier investing is the 1960s version: do not second-guess "
            "the founder. Speculators time a market they do not know. Mix the four and any deal "
            "can be justified. Separate moat shape from mechanism. Superlinear means $5 million "
            "into the slightly larger network pulls away — LinkedIn, and maybe GitHub. Sublinear "
            "means the leader grows slower than a challenger spending the same dollar. Uber is "
            "funded scale, not a lock. True superlinear cases almost never happen, and "
            "defensibility is second-order while the market is still opening white space."
        ),
        (
            "Frontier models and the slowdown. For three years the best model has taken 80% or more "
            "of dollar-weighted spend, with pricing power for being a bit better and no demand "
            "problem. Penetration is still about 0.1% in the broad claim, or 3% of enterprises "
            "but 1% or less of budget. 'Never invest in a model' and 'neocloud revenue is bad' "
            "both missed value that accrued while the market grew. An Anthropic S-1 buyer still "
            "has to ask about defensibility if the thesis is no longer early penetration. Model "
            "life, from the app graphs he sees, is three to six months. Software used to have a "
            "long tail. A six-month Anthropic slip, or a three-month slip, can lose the market. "
            "Coding near a 95% task ceiling slows tokens inside code. It does not license a "
            "cheaper model: rivals still pay about 10 times for the smartest one. If use saturates, "
            "value can fall into open source. Networking was sleepy for 15 years; clusters are "
            "producing the first new companies since Arista, plus optical."
        ),
        (
            "Private markets, then Cursor. His dream book is 5% of every competitive round — he "
            "names Cognition and Cursor — because private markets look efficient and the deals "
            "that returned capital were the competitive ones. You cannot index them. The firm "
            "picks the top company in each real sector and takes the market price. Hunting "
            "non-consensus, he says, adds follow-on risk. He rejects the line that only about "
            "20 startups matter. Nicira to VMware was $1.26 billion, about a $1 billion option on "
            "a $40 billion market. Cursor is the largest of the recent strategic set in his "
            "account. A few-billion raise was nearly done when a model he prices at about $3 "
            "billion to train made compute the bottleneck. SpaceX had the compute. Cursor had "
            "the users and the data. He pairs Michael Truell with Elon. Open Router leaked. "
            "World Labs did not. Strategic M&A is trust, not a poker game."
        ),
    ]
    mental = {
        "name": "Four Mindsets × Moat Shape × Three-to-Six-Month Models",
        "components": (
            "Name the mindset before the price. Finance reads TAM too early. Productive investing "
            "maps a technical approach onto how infrastructure is bought. Frontier investing does "
            "not second-guess the founder. Speculation times a chart. Moat shape is superlinear, "
            "linear, or sublinear, separate from the mechanism. LinkedIn is the rare superlinear "
            "case. Uber is funded scale. While the market grows, defensibility is second-order. "
            "Frontier dollars at 80% or more for three years sit on about 1% budget penetration. "
            "Model life is three to six months. A coding ceiling slows tokens and still does not "
            "license a dumber model. Private markets are efficient enough that the job is the "
            "best company per sector. Extra capital enlarges the set. Strategic sales clear on "
            "trust and an option on a larger market."
        ),
        "application": (
            "Private:Anthropic is the S-1 the tape says a public buyer must underwrite for "
            "defensibility — 80% dollar share while growth holds, and a six-month slip that can "
            "zero the last model. Private:Cursor is the strategic-sale file: users and data "
            "against a compute owner, price set by a few-billion raise, trust instead of a leak. "
            "ANET is the last networking platform's public winner and the name he uses for "
            "'nothing new since,' while he also says an incumbent can add optical and cluster "
            "features. Do not treat a sponsor read as a holding. Do not short a lab because "
            "coding tasks look saturated."
        ),
    }
    insights = [
        {
            "view": "Name the mindset or any deal clears.",
            "question": "What are the four?",
            "answer": "Spreadsheet finance, productive assets, 1960s founder bets, and market timing. Finance is showing up at Series A. Mix them and bias writes the memo.",
        },
        {
            "view": "A smarter model still gets the dollar.",
            "question": "Does 95% coding saturation cheapen tokens?",
            "answer": "No. Token growth inside code can slow. Competitive equilibrium still pays about 10 times for the smartest model. Life of a model is three to six months; 80% or more of dollars have sat at the frontier for three years.",
        },
        {
            "view": "The Cursor sale was an option on compute.",
            "question": "What cleared it?",
            "answer": "A few-billion raise was setting price. A model he costs at about $3 billion needed compute SpaceX had. Cursor had users and data. Leaks killed the feel of Open Router; World Labs stayed quiet.",
        },
    ]
    invest = [
        {
            "ticker": "Private:Anthropic",
            "direction": "Long",
            "confidence": "Low",
            "thesis": "80%+ frontier dollar share while penetration is still ~1% of budget; a six-month slip can zero the prior model — low",
        },
        {
            "ticker": "Private:Cursor",
            "direction": "Long",
            "confidence": "Low",
            "thesis": "Users and data met a compute owner; a few-billion raise set the mark and the sale cleared on trust — low",
        },
        {
            "ticker": "ANET",
            "direction": "Long",
            "confidence": "Low",
            "thesis": "Last networking winner he names; cluster and optical work is the first new build since, and incumbents may add it — low",
        },
    ]
    quotes = [
        "talking about defensibility is kind of a second or third order thing if the market is growing",
        "the lifespan of a model is three to six months",
        "You would always pay 10 times more for the smartest model.",
    ]
    chrono = {
        "subject": "Casado · models · Cursor",
        "events": [
            {"date": "2012", "event": "Nicira to VMware, $1.26B; ~$1B option on a $40B market"},
            {"date": "2010s–20s", "event": "Tabular to Databricks beats that revenue multiple"},
            {"date": "2023–26", "event": "Frontier takes 80%+ of dollar-weighted model spend"},
            {"date": "2026", "event": "Cursor strategic sale; Open Router leaks; World Labs does not"},
            {"date": "2026", "event": "Anthropic S-1 is the public-buyer defensibility test on the tape"},
            {"date": "2026-11-04", "event": "EP498 publishes"},
        ],
    }
    en = en_std(
        eid, "Invest Like the Best", "Patrick O'Shaughnessy", meta, 3,
        ["Private:Anthropic", "Private:Cursor", "ANET"],
        concl, bg, facts, mental, insights, invest, quotes, chrono,
        "| v4.10 window ILTB EP498", "youtube-auto",
    )
    dump(ROOT / f"data/approved/{eid}.json", en)
    validate_file(ROOT / f"data/approved/{eid}.json")


def fnd439():
    eid = "fnd-439-how-eiichiro-oda-works"
    meta = {
        "episode_number": 439,
        "title": "#439 How Eiichiro Oda Works",
        "guest": "Eiichiro Oda",
        "guest_role": "Creator of One Piece · no biography, interview file",
        "date": "2026-11-04",
        "duration_minutes": 33,
        "youtube_url": "https://www.youtube.com/watch?v=WaxQXHi5Vuo",
        "links": {
            "youtube": "https://www.youtube.com/watch?v=WaxQXHi5Vuo",
            "apple_podcasts": FND_APPLE,
        },
    }
    concl = (
        "Senra builds Oda from interviews because there is no biography and almost no photographs. "
        "One Piece passed 600 million copies. Oda started it in July 1997 as a five-year story and "
        "is still in it approaching a 30th anniversary in 2027. The schedule is the method: a "
        "chapter every seven days, about three hours of sleep, every moving figure drawn by him. "
        "The only reader in his head is himself at 15. Netflix did not ship the live-action until "
        "he signed the scripts. He copied Disney's Little Mermaid frame by frame after an editor "
        "insulted his characters."
    )
    bg = (
        "Founders 439, Nov 4, about 33 minutes. Eric Glyman at Ramp kept texting Senra to do Oda. "
        "The mid-episode Ramp block — 5% average savings, a UK launch, ramp.com/invest — is a "
        "sponsor read, not the manga file. Senra spent a week in interviews. Oda is 51, started "
        "the life of a manga artist young, and will not be photographed."
    )
    facts = [
        (
            "Scale and the broken five-year plan. One Piece is the best-selling manga and comic "
            "series Senra cites, over 600 million copies, with a Guinness record for copies of "
            "one series by a single author. Serialization began in Weekly Shonen Jump in July "
            "1997. Oda expected the adventure to last about five years. In a 2022 interview he "
            "said he had badly underestimated it. The original plan now runs toward a 30th "
            "anniversary in 2027, and he has repeatedly underestimated how much story is left. "
            "He is 51 on this tape. Published wealth guesses run from $250 million to $500 "
            "million, with $20 million to $40 million a year from the work. For the 600 million "
            "copy mark he wrote the truth of the treasure and of Luffy, split the page, and sank "
            "the revealing half in a chest on the seabed, to be raised when the manga ends."
        ),
        (
            "The week and the sleep. A chapter has to move every seven days. Monday through "
            "Wednesday he writes story, dialogue, and rough boards. Thursday through Saturday he "
            "draws and finishes with assistants. Sunday is color, covers, and the rest. In a "
            "2016 interview he described bed at 2:00 a.m. and wake at 5:00 a.m., held for roughly "
            "15 years. An extra hour of sleep is an hour of work lost. Planning on four hours "
            "made him dread wasting that fourth hour. After a manuscript he allows one longer "
            "sleep. New ideas, "
            "he says, arrive only when he is tired and has skipped sleep and food, because that "
            "is when a person hits a limit. Assistants paint backgrounds. He draws people, "
            "animals, crowds, smoke, clouds, and the ocean himself, because another hand changes "
            "the moving line. He once stayed on the phone with an editor for 12 hours; the editor "
            "fell asleep. If the idea is not his, he does not "
            "want to draw it. They may criticize. They may not invent."
        ),
        (
            "One reader, then the guard dog. The audience in his head is himself at 15. He does "
            "not know how other people feel, so awesome means what that boy would love. An early "
            "editor said the women were not attractive. Oda could not sleep, practiced all night, "
            "and advanced through hand-drawn Disney — The Little Mermaid — frame by frame. On the "
            "Netflix live-action he refused a handoff. Netflix agreed not to release until he "
            "called it satisfactory. He read scripts, gave notes, and called himself a guard dog."
        ),
    ]
    mental = {
        "name": "Fifteen-Year-Old Reader × Three-Hour Nights × Guard-Dog IP",
        "components": (
            "No biography, so the file is interviews. 600 million copies, Jump since July 1997, "
            "a five-year plan that became a 30th anniversary in 2027. The week is fixed: write "
            "Mon–Wed, draw Thu–Sat, color Sunday. Sleep is three hours, 2:00 a.m. to 5:00 a.m., "
            "for about 15 years; four hours already feels like waste; youth was two hours per "
            "48, in 15-minute naps. He draws every moving mark. Editors criticize and do not "
            "invent. The only reader is Oda at 15, which Senra hears as Jobs on taste. Netflix "
            "waited for his signature. Disney's Little Mermaid was the frame-by-frame school "
            "after an insult. A chest on the seabed holds the ending until the manga ends. "
            "Wealth on the tape is $250–500 million and $20–40 million a year, displayed on "
            "purpose so younger artists see the prize."
        ),
        "application": (
            "NFLX is the adapter that could not ship until the author signed. DIS is the "
            "animation school he copied, not the owner of One Piece. AAPL is Senra's explicit "
            "taste compare — Jobs to Moritz — not a manga multiple. Do not underwrite the Ramp "
            "sponsor read (5% savings, UK launch) as Oda's business. The operating fact is "
            "one person still drawing the moving line in year 28."
        ),
    }
    insights = [
        {
            "view": "The five-year story is in year 28.",
            "question": "What did 1997 assume?",
            "answer": "July 1997 in Jump, done in about five years. By 2022 he said he had underestimated it. 600 million copies, and a 30th anniversary due in 2027.",
        },
        {
            "view": "Sleep is the scarce input he withholds.",
            "question": "What is the night?",
            "answer": "2:00 a.m. to 5:00 a.m. for about 15 years. A fourth hour feels like waste. Ideas show up at the limit, without sleep or food. He still draws every moving figure.",
        },
        {
            "view": "The live-action waited on one signature.",
            "question": "What did Netflix agree?",
            "answer": "No release until he was satisfied. He read scripts and acted as guard dog. Editors may criticize. They may not invent the plot.",
        },
    ]
    invest = [
        {
            "ticker": "NFLX",
            "direction": "Long",
            "confidence": "Low",
            "thesis": "Live-action shipped only after Oda signed the scripts; the author is still the guard dog — low",
        },
        {
            "ticker": "DIS",
            "direction": "Long",
            "confidence": "Low",
            "thesis": "Little Mermaid was the frame-by-frame school after an editor insulted the characters, not the One Piece owner — low",
        },
        {
            "ticker": "AAPL",
            "direction": "Long",
            "confidence": "Low",
            "thesis": "Senra's Jobs/Moritz compare: taste starts with the product test, not the commercial brief — low",
        },
    ]
    quotes = [
        "Would the 15-year-old version of me think this is awesome?",
        "Netflix agreed that they wouldn't go out with the show until I agreed it was satisfactory.",
        "humans can only come up with truly new ideas when they reach their limit",
    ]
    chrono = {
        "subject": "Oda · One Piece · schedule",
        "events": [
            {"date": "1997-07", "event": "One Piece begins in Weekly Shonen Jump; five-year plan"},
            {"date": "~2001–16", "event": "2:00 a.m.–5:00 a.m. sleep held ~15 years by the 2016 interview"},
            {"date": "2015", "event": "Published week: write Mon–Wed, draw Thu–Sat, color Sunday"},
            {"date": "2022", "event": "Admits the five-year plan was badly short"},
            {"date": "2020s", "event": "600 million copies; ending page sunk in a seabed chest"},
            {"date": "2020s", "event": "Netflix live-action waits on his script sign-off"},
            {"date": "2027", "event": "Series approaches its 30th anniversary, still unfinished"},
            {"date": "2026-11-04", "event": "Founders 439 publishes"},
        ],
    }
    en = en_std(
        eid, "Founders", "David Senra", meta, 3,
        ["NFLX", "DIS", "AAPL"],
        concl, bg, facts, mental, insights, invest, quotes, chrono,
        "| v4.10 window Founders 439", "youtube-auto",
    )
    dump(ROOT / f"data/approved/{eid}.json", en)
    validate_file(ROOT / f"data/approved/{eid}.json")


def sv257():
    eid = "sv101-ep257"
    quotes = [
        "safety安全这个词一共出现了248次",
        "掌握一般表决事项50.1%的投票权",
        "最终让机构兑现了大约5亿美元",
    ]
    check(eid, quotes)
    meta = {
        "episode_number": 257,
        "title": "Vitalik on AI Safety, Effective Altruism, and d/acc",
        "guest": "Vitalik Buterin · Afra",
        "guest_role": "Ethereum co-founder · writer and tech journalist",
        "date": "2026-10-28",
        "duration_minutes": 113,
        "youtube_url": "https://www.youtube.com/watch?v=XcastAK9pDM",
        "links": {
            "youtube": "https://www.youtube.com/watch?v=XcastAK9pDM",
            "apple_podcasts": SV_APPLE,
            "fireside": "https://sv101.fireside.fm/271",
            "xiaoyuzhou": "https://www.xiaoyuzhoufm.com/podcast/5e5c52c9418a84a04625e6cc",
        },
    }
    concl = (
        "Yiwen opens on Anthropic's S-1: nearly 100 pages of risk factors, the word safety 248 "
        "times and AI safety 36 times, seven founders keeping 50.1% of ordinary votes, and a "
        "long-term benefit trust that can elect a board majority. The secret successor list is "
        "the public's problem if the warnings are real. The hour maps effective altruism from "
        "MacAskill and 80,000 Hours through SBF and Dario Amodei's exit from OpenAI. Vitalik's "
        "2021 crypto gift to the Future of Life Institute later cashed out near $500 million. His "
        "alternative is d/acc. OpenAI gave up openness for safety, then safety for speed."
    )
    bg = (
        "E257, Oct 28, about 113 minutes, two sittings. Yiwen frames the S-1 and the camps. "
        "Hongjun and Yiwen then talk with Vitalik and Afra about his donations and his break "
        "with parts of EA; a second sitting is Afra alone on MacAskill and Yudkowsky. The "
        "Economist put EA on the cover this month. The US Defense Department's line on the "
        "tape is Americanism, not effective altruism. Captions are the Chinese manual file."
    )
    facts = [
        (
            "The S-1 is the cold open, not a footnote. Anthropic filed this week. Yiwen counts "
            "nearly 100 pages of risk factors, including catastrophic and existential risk from "
            "frontier AI, plus a line that the company cannot promise its safety measures will "
            "work. Ctrl-F: safety 248 times, AI safety 36 times. After listing, seven co-founders "
            "keep 50.1% of votes on ordinary matters through a special share class. A long-term "
            "benefit trust may elect a majority of the board, so commercial goals are supposed "
            "to sit next to humanity's long-run interest. Founders may pre-name who inherits "
            "their votes if they cannot serve. Those names need internal approval and stay "
            "secret. Yiwen's second worry is governance: if the warning is real, the public "
            "still does not know who might speak for humanity. That stack is why the episode "
            "treats AI safety as a corporate fact about Anthropic, not only a philosophy seminar. "
            "Holden Karnofsky, married to Daniela Amodei, co-founded GiveWell and Open Philanthropy."
        ),
        (
            "How EA got to the labs. MacAskill, an Oxford philosopher, asks how limited money "
            "and time can help more people, and co-founded 80,000 Hours — a career is about "
            "that many hours. SBF made 'earn to give' famous; the FTX collapse brought the "
            "criticism, and did not end the movement. Yudkowsky is the rationalist who asked "
            "how a smarter-than-human machine stays aimed at human interests. Dario Amodei left "
            "OpenAI with colleagues to start Anthropic over safety and direction. Vitalik funded "
            "global health and, in 2021, sent crypto to the Future of Life Institute. He later "
            "recalled that gift realizing about $500 million, and he has moved away from some of "
            "that circle's methods. The camps "
            "Afra draws are no longer one EA: EA close to Anthropic, EA far from Anthropic, "
            "Pause AI (more populist, willing to say rationalism and AI are bad), and e/acc "
            "— Andreessen Horowitz and Jeff Bezos — which wants acceleration. Rationalists "
            "sit nearby but, in Vitalik's split, they are motivated by curiosity; EA is "
            "solemn, a rescue mission that does not get to play."
        ),
        (
            "d/acc against the OpenAI sequence. Vitalik's label is defensive, decentralized "
            "or democratizing, and acceleration. Technology should keep moving. More of the "
            "budget should go to protection: cybersecurity against AI hacking, and antiviral "
            "work before models make dangerous biology easier. The third leg refuses "
            "concentrated power — open source and tools that empower ordinary people, with "
            "a Switzerland-and-mountains picture of small independent units rather than one "
            "capital. Defensive and democratizing reinforce each other. Afra's short history "
            "of OpenAI is the foil: they sacrificed openness for safety (GPT-3 too dangerous "
            "to open-source, around 2020, plus safety pledges), then sacrificed safety for "
            "acceleration when the pledges, including ones to government bodies, became "
            "inconvenient. Altman pushed out and brought back is, on this tape, one more "
            "round of e/acc versus EA inside the same company. Vitalik offers d/acc as "
            "acceleration that does not hand the vote to a secret list. The named firms are "
            "Anthropic, OpenAI, and a16z."
        ),
    ]
    mental = {
        "name": "S-1 Safety Count × Four Camps × d/acc",
        "components": (
            "Read the filing before the philosophy. Safety appears 248 times, AI safety 36, "
            "across nearly 100 pages of risks the company will not guarantee it can manage. "
            "Seven founders keep 50.1% of ordinary votes. A long-term benefit trust can elect "
            "the board majority. Successor voters are pre-named and secret. EA reached that "
            "clause through MacAskill, 80,000 Hours, SBF's collapse, Yudkowsky, Bostrom, and "
            "Dario's exit from OpenAI. Vitalik's 2021 FLI crypto gift later cashed near $500 "
            "million, and he now dissents from parts of the circle. Camps: Anthropic-near EA, "
            "Anthropic-far EA, Pause AI, and e/acc (a16z and Bezos), with rationalists as "
            "the curious neighbors. d/acc keeps acceleration, spends on cyber and antivirals, "
            "and refuses a single capital. OpenAI's audible sequence is openness given up for "
            "safety, then safety given up for acceleration."
        ),
        "application": (
            "Private:Anthropic is the S-1 governance file — safety language plus 50.1% and "
            "the trust — not a settled answer to who speaks for humanity. Private:OpenAI is "
            "the acceleration sequence on the tape, including Altman out and back. Private:a16z "
            "is the named e/acc firm, not a lab. Do not mark AMZN off Bezos's personal camp, "
            "or GOOGL off a campus meetup. The tradable question is not in this hour."
        ),
    }
    insights = [
        {
            "view": "The safety words are a filing fact.",
            "question": "What did Yiwen count?",
            "answer": "Safety 248 times, AI safety 36, in nearly 100 pages of risks Anthropic will not promise to contain. Seven founders keep 50.1% of ordinary votes. A trust can elect the board majority. Successors stay secret.",
        },
        {
            "view": "EA did not end with FTX.",
            "question": "How did it reach the labs?",
            "answer": "MacAskill and 80,000 Hours, then SBF, then Dario leaving OpenAI. Vitalik's 2021 gift to FLI later cashed near $500 million. He has since broken with parts of that practice.",
        },
        {
            "view": "d/acc is acceleration with a brake and a split vote.",
            "question": "What are the three legs?",
            "answer": "Keep building. Spend on cyber defense and antivirals. Do not concentrate power. OpenAI, on this tape, dropped openness for safety and then safety for speed.",
        },
    ]
    invest = [
        {
            "ticker": "Private:Anthropic",
            "direction": "Long",
            "confidence": "Low",
            "thesis": "S-1 puts safety 248 times in the risk factors and leaves 50.1% plus a board trust with the founders' circle — low",
        },
        {
            "ticker": "Private:OpenAI",
            "direction": "Long",
            "confidence": "Low",
            "thesis": "Tape's sequence is openness traded for safety, then safety traded for acceleration, Altman out and back — low",
        },
        {
            "ticker": "Private:a16z",
            "direction": "Long",
            "confidence": "Low",
            "thesis": "Named home of e/acc on this tape, the camp opposite Pause AI and Anthropic-near EA — low",
        },
    ]
    chrono = {
        "subject": "EA · Anthropic S-1 · d/acc",
        "events": [
            {"date": "2010s", "event": "MacAskill, 80,000 Hours; Yudkowsky; Bostrom Superintelligence"},
            {"date": "~2020", "event": "OpenAI withholds GPT-3; safety pledges"},
            {"date": "2021", "event": "Dario leaves OpenAI for Anthropic; Vitalik's FLI gift later ~$500M"},
            {"date": "2022", "event": "FTX collapse; EA criticism, movement continues"},
            {"date": "2023", "event": "Altman removed and returned — e/acc vs EA inside OpenAI"},
            {"date": "2026-10", "event": "Economist EA cover; DoD line against EA"},
            {"date": "2026-10", "event": "Anthropic S-1: safety 248 / AI safety 36; 50.1% votes"},
            {"date": "2026-10-28", "event": "E257 publishes"},
        ],
    }
    en = en_std(
        eid, "Silicon Valley 101", "Hongjun", meta, 3,
        ["Private:Anthropic", "Private:OpenAI", "Private:a16z"],
        concl, bg, facts, mental, insights, invest, quotes, chrono,
        "| v4.10 window SV101 E257", "youtube-manual",
    )
    zh_meta = dict(meta)
    zh_meta.update(
        title="E257｜对话Vitalik：AI安全背后的哲学思想，有效利他主义如何影响硅谷？",
        guest="Vitalik Buterin · Afra",
        guest_role="以太坊联合创始人 · 写作者 / 科技记者",
    )
    zh = dict(en)
    zh.update({
        "podcast": "硅谷101",
        "host": "泓君",
        "metadata": zh_meta,
        "conclusion": (
            "Yiwen用Anthropic招股书开场：风险因素将近100页，safety出现248次、AI安全36次，"
            "七位联合创始人靠特殊股掌握一般表决50.1%，长期利益信托可以选举董事会多数。"
            "如果警告是真的，继任投票人名单仍对公众保密。后面把有效利他主义从MacAskill和八万小时，"
            "接到SBF、Yudkowsky，以及Dario离开OpenAI创立Anthropic。Vitalik 2021年给未来生命研究所的"
            "加密捐赠后来兑现大约5亿美元，他已经和这个圈子的一部分做法拉开距离。他的替代方案是d/acc："
            "加速，但要防御，并且不要把权力集中。Afra对OpenAI的短史是：先为安全放弃开放，再为加速放弃安全。"
        ),
        "background": (
            "E257，10月28日，大约113分钟，分两次录。Yiwen先讲招股书和阵营。泓君、Yiwen再与Vitalik、Afra"
            "谈捐赠和他与EA部分做法的分歧；第二场是Afra单独讲MacAskill和尤德考斯基。"
            "《经济学人》这个月把EA放上封面。美国国防部在带子上的口号是美国主义，而不是有效利他主义。"
            "字幕是中文人工稿。"
        ),
        "important_facts": [
            (
                "招股书是开场，不是脚注。Anthropic本周递表。Yiwen数到将近100页风险因素，包括前沿AI的"
                "灾难性甚至生存风险，以及公司不能保证安全措施有效。Ctrl-F：safety 248次，AI安全36次。"
                "上市后七位联合创始人通过特殊股份掌握一般事项50.1%的投票权。长期利益信托可以选举董事会多数，"
                "让商业目标旁边坐着人类长远利益。创始人可以预先指定失能后的投票继承人，名单要内部批准且保密。"
                "Yiwen的第二问是治理：如果警告为真，公众仍不知道谁可能代表人类发言。所以这期把AI安全写成"
                "Anthropic的公司事实，不只是哲学讨论。Daniela Amodei的丈夫Holden Karnofsky联合创办了"
                "GiveWell和Open Philanthropy，慈善图和实验室图是同一间屋子。"
            ),
            (
                "EA怎样走到实验室。牛津哲学家MacAskill问有限的钱和时间怎样帮到更多人，并共同创办八万小时——"
                "职业生涯大约就是这么多小时。SBF把「赚钱为了捐钱」做成招牌；FTX崩塌带来批评，运动没有结束。"
                "Yudkowsky追问比人更聪明的机器如何对准人类利益。Bostrom《超级智能》是Yiwen点的书；"
                "Sam Altman公开推荐过，也写过自己的担忧。Dario Amodei早年贴近有效慈善，后来和同事离开OpenAI"
                "创立Anthropic，分歧就在安全和方向。一部分有效利他主义者把灭绝风险当成下一美元的最高用途。"
                "Vitalik资助全球健康，2021年向未来生命研究所捐了一批加密货币，他后来回忆这笔捐赠兑现了大约"
                "5亿美元。这期带子上他已经离开那个圈子的一些做法。Afra画的阵营不再是一个EA：贴近Anthropic的EA、"
                "远离Anthropic的EA、更民粹的Pause AI，以及e/acc——a16z和Jeff Bezos——要加速。"
                "理性主义者在旁边。Vitalik的分法是：理性主义者出于好奇，EA是严肃的拯救任务，不能玩。"
                "他举的好玩文本是Yudkowsky的HPMOR和Scott Alexander的Unsong。"
            ),
            (
                "d/acc对着OpenAI的序列。Vitalik的标签是防御、去中心或民主化、以及加速。技术要继续走。"
                "更多预算要给保护：对付AI黑客的网络安全，以及在模型让危险生物更容易出现之前做抗病毒。"
                "第三条拒绝集中权力——开源，以及让普通人更有能力的工具。他用瑞士和山里的小城，而不是一个首都。"
                "防御和民主化互相加强。Afra的OpenAI短史是对照：大约2020年，GPT-3太危险不能开源，他们为安全"
                "牺牲开放，并做过安全承诺；后来承诺（包括对一些政府组织的）妨碍发展，他们又为加速牺牲安全。"
                "Altman被请走又回来，在这期带子上是同一家公司里e/acc和EA的又一轮。谷歌园区的e/acc聚会是这个"
                "阵营的现场版。Vitalik不是说Anthropic的信托已经解决董事会问题。他给的是一条加速但不把票交给"
                "秘密名单的路。可交易的对照很薄。点名的机构是Anthropic、OpenAI和a16z。"
            ),
        ],
        "mental_model": {
            "name": "招股书安全计数 × 四个阵营 × d/acc",
            "components": (
                "先读文件再读哲学。safety出现248次，AI安全36次，将近100页风险，公司不保证自己管得住。"
                "七位创始人掌握一般表决50.1%。长期利益信托可以选董事会多数。继任投票人预先指定且保密。"
                "EA走到这一条，经过MacAskill、八万小时、SBF崩塌、Yudkowsky、Bostrom，以及Dario离开OpenAI。"
                "Vitalik 2021年给FLI的加密捐赠后来兑现近5亿美元，他现在反对这个圈子的一部分做法。"
                "阵营：贴近Anthropic的EA、远离的EA、Pause AI，以及e/acc（a16z和Bezos），理性主义者是好奇的邻居。"
                "d/acc保持加速，把钱花在网络安全和抗病毒上，并拒绝一个首都。OpenAI在带子上的序列是："
                "为安全放弃开放，再为加速放弃安全。"
            ),
            "application": (
                "Private:Anthropic是招股书治理档案——安全用语加上50.1%和信托——不是「谁代表人类」的定论。"
                "Private:OpenAI是带子上的加速序列，包括Altman出去又回来。Private:a16z是点名的e/acc机构，不是实验室。"
                "不要因为Bezos个人站队去标AMZN，也不要因为一次园区聚会去标GOOGL。这小时里没有干净的上市股票论点。"
            ),
        },
        "key_insights": [
            {
                "view": "安全这两个字是文件事实。",
                "question": "Yiwen数了什么？",
                "answer": "safety 248次，AI安全36次，将近100页风险，Anthropic不承诺能兜住。七位创始人掌握一般表决50.1%。信托可以选董事会多数。继任者保密。",
            },
            {
                "view": "EA没有停在FTX。",
                "question": "它怎样进了实验室？",
                "answer": "MacAskill和八万小时，然后SBF，然后Dario离开OpenAI。Vitalik 2021年给FLI的捐赠后来兑现近5亿美元。他已经和其中一部分做法分手。",
            },
            {
                "view": "d/acc是带着刹车、拆开投票权的加速。",
                "question": "三条腿是什么？",
                "answer": "继续造。把钱花在网络防御和抗病毒上。不要集中权力。OpenAI在这期带子上先为安全放弃开放，再为速度放弃安全。",
            },
        ],
        "golden_quotes": quotes,
        "review_notes": "| v4.10 window 硅谷101 E257",
    })
    dump(ROOT / f"data/approved/{eid}.json", en)
    dump(ROOT / f"data/approved/zh/{eid}.json", zh)
    validate_file(ROOT / f"data/approved/{eid}.json")


def main():
    ep498()
    fnd439()
    sv257()


if __name__ == "__main__":
    main()
