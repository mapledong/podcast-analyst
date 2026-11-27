#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""ILTB 502 and SV101 E259–E261."""
from __future__ import annotations

import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))
from scripts._window_lib import dump, en_std, validate_file  # noqa: E402
from src.chinese_transcript import load_transcript_body, quote_supported_in_transcript, transcript_path  # noqa: E402

ILTB = "https://podcasts.apple.com/podcast/invest-like-the-best-with-patrick-o-shaughnessy/id1154105909"
SV = "https://podcasts.apple.com/cn/podcast/id1498541229"
SV_XYZ = "https://www.xiaoyuzhoufm.com/podcast/5e5c52c9418a84a04625e6cc"


def check(eid, quotes):
    body = load_transcript_body(transcript_path(eid))
    for q in quotes:
        ok = quote_supported_in_transcript(q, body)
        print(eid, "OK" if ok else "FAIL", q)
        if not ok:
            raise SystemExit(q)


def save_en(eid, meta, kws, concl, bg, facts, mental, insights, invest, quotes, chrono, notes):
    en = en_std(eid, "Invest Like the Best", "Patrick O'Shaughnessy", meta, 3, kws, concl, bg, facts, mental, insights, invest, quotes, chrono, notes, "youtube-auto")
    dump(ROOT / f"data/approved/{eid}.json", en)
    validate_file(ROOT / f"data/approved/{eid}.json")


def save_sv(eid, meta, kws, concl, bg, facts, mental, insights, invest, quotes, chrono, zh):
    check(eid, quotes)
    en = en_std(eid, "Silicon Valley 101", "Hongjun", meta, 3, kws, concl, bg, facts, mental, insights, invest, quotes, chrono, f"| v4.10 window {eid}", "youtube-zh")
    zh_meta = dict(meta)
    zh_meta.update(zh["meta"])
    z = dict(en)
    z.update({
        "podcast": "硅谷101", "host": "泓君", "metadata": zh_meta,
        "conclusion": zh["conclusion"], "background": zh["background"],
        "important_facts": zh["facts"], "mental_model": zh["mental"],
        "key_insights": zh["insights"], "golden_quotes": quotes,
        "review_notes": f"| v4.10 window 硅谷101 {eid}",
    })
    dump(ROOT / f"data/approved/{eid}.json", en)
    dump(ROOT / f"data/approved/zh/{eid}.json", z)
    validate_file(ROOT / f"data/approved/{eid}.json")


def ep502():
    save_en(
        "ep502",
        {
            "episode_number": 502,
            "title": "Scott Wu — Cybersecurity, Compute, and the Future of Engineering",
            "guest": "Scott Wu",
            "guest_role": "CEO, Cognition",
            "date": "2026-11-24",
            "duration_minutes": 64,
            "youtube_url": "https://www.youtube.com/watch?v=efoZj_7oVJs",
            "links": {"youtube": "https://www.youtube.com/watch?v=efoZj_7oVJs", "apple_podcasts": ILTB},
        },
        ["Private:Cognition", "C", "DDOG"],
        (
            "Wu says the next 6 to 12 months bring major breaches at Fortune 50 and "
            "Fortune 100 firms and at governments, because attackers will use agent "
            "swarms on 30-year-old software before defenders do. Cognition went from "
            "a first dollar on September 20, 2024 to a billion-dollar revenue run rate "
            "on September 16, 2026. It is inside more than 100 of the Fortune 500, "
            "with about 500 employees. Customers measure about 8 to 15 times ROI. "
            "Citi is rolling Devin out to about 14,000 of 80,000 technical staff. "
            "The defense he wants is the same swarm on your own attack surface."
        ),
        (
            "EP502, Nov 24, about 64 minutes. Patrick asks for a Cognition snapshot "
            "before the security product Wu released the morning of the taping. A year "
            "ago the team was still small. They once had about 70 people in one house. "
            "Adoption he names includes Datadog, Harvey, and OpenRouter. Devin started "
            "on routine migrations and is now used across the board."
        ),
        [
            (
                "The business print. First revenue dollar September 20, 2024. A billion-dollar "
                "run rate on September 16, 2026, just under two years. More than 100 of the "
                "Fortune 500. About 500 employees. The early house ended crowded, about 70 "
                "people. The work shifted to enterprise. Use spread from routine migrations "
                "to everything, including at Datadog, Harvey, and OpenRouter. ROI, when "
                "customers measure it themselves, is about 8 to 15 times per dollar. One "
                "hour of Devin is about 8 hours of engineer-equivalent output. Citi has "
                "started a rollout to about 14,000 engineers. The firm has about 80,000 "
                "technical staff who build and maintain software, so Wu calls that a long "
                "way to go. Jane Fraser, on the earnings call the week before, said Citi "
                "expects about $1.5 billion of savings in 2026 just from bringing projects "
                "in house that used to go to consultants. That figure is before the new "
                "things those teams will build."
            ),
            (
                "Why security is the capability test. Wu released a security product the "
                "day of the tape. Attackers can train capable models of their own. The "
                "urgent gap is that defenders are not using agents at the same depth. A "
                "swarm has to walk every attack surface of the product and the site, keep "
                "it current, and watch logs and entry points. A lot of the code is about "
                "30 years old and has to be brought forward. On the current path, the next "
                "6 to 12 months produce many major breaches. Not small firms. Fortune 50, "
                "Fortune 100, and government institutions. He treats that as close to "
                "inevitable unless the defense swarm is deployed at the same intensity as "
                "the attack. The product is the same agent used to write software, pointed "
                "at the holes in that software."
            ),
            (
                "Compute and the engineering job. The title frame is cybersecurity, compute, "
                "and what engineering becomes when an agent hour replaces most of a human "
                "hour. The Citi number is the tell: 14,000 of 80,000 is the start, and the "
                "$1.5 billion is consultant work pulled inside, not a claim that headcount "
                "goes to zero. Wu still describes a long rollout. The ROI range of 8 to 15 "
                "times is what customers calculate, not a Cognition slide he asks you to "
                "trust without their own measurement. Fortune 500 penetration above 100 "
                "logos is the distribution. The breach forecast is the reason the security "
                "product exists in the same quarter as the billion-dollar run rate."
            ),
        ],
        {
            "name": "Billion in Two Years × 8 to 15 Times × Defense Swarm",
            "components": (
                "September 20, 2024 to September 16, 2026 is the zero-to-a-billion clock. "
                "More than 100 Fortune 500s. About 500 employees. Customer-measured ROI is "
                "8 to 15 times, and one Devin hour is about 8 engineer hours. Citi is at "
                "about 14,000 of 80,000 technical staff, with about $1.5 billion of 2026 "
                "insourcing savings named by Jane Fraser. The next 6 to 12 months are the "
                "breach window for Fortune 50 and Fortune 100 names if defenders do not "
                "run the same swarm against 30-year-old code."
            ),
            "application": (
                "Private:Cognition is the agent company on this print. C is the customer "
                "with the rollout and the $1.5 billion line. DDOG is one of the tech "
                "adopters he names, not a security multiple. Do not treat the breach "
                "forecast as a short on every Fortune 100. It is the case for pointing "
                "the same agents at your own surface."
            ),
        },
        [
            {"view": "A billion in just under two years is the business.", "question": "What is the clock?", "answer": "First dollar September 20, 2024. Billion-dollar run rate September 16, 2026. More than 100 Fortune 500s. About 500 people. Customers measure 8 to 15 times ROI."},
            {"view": "Citi is the rollout, not the whole staff.", "question": "How far has Devin gone there?", "answer": "About 14,000 engineers of 80,000 technical staff. Jane Fraser put about $1.5 billion of 2026 savings on bringing consultant projects inside. Wu says there is a long way left."},
            {"view": "The breach window is 6 to 12 months.", "question": "Who gets hit if defense lags?", "answer": "Fortune 50, Fortune 100, and governments, on 30-year-old software. The defense he wants is an agent swarm on your own attack surface, logs, and entry points."},
        ],
        [
            {"ticker": "Private:Cognition", "direction": "Long", "confidence": "Medium", "thesis": "Zero to a billion-dollar run rate in just under two years, 8 to 15 times customer ROI, security product in the same quarter — medium"},
            {"ticker": "C", "direction": "Long", "confidence": "Low", "thesis": "About 14,000 engineers on Devin and about $1.5 billion of 2026 insourcing savings named by the CEO — low"},
            {"ticker": "DDOG", "direction": "Long", "confidence": "Low", "thesis": "Named among Silicon Valley teams that have moved Devin past routine migrations — low"},
        ],
        [
            "we went from zero to a billion just under two years",
            "they're getting something in the range of 8 to 15 X ROI",
            "over the next 6 to 12 months, there will be a lot of major breaches",
        ],
        {"subject": "Cognition · Devin · the breach window", "events": [
            {"date": "2024-09-20", "event": "First dollar of Cognition revenue"},
            {"date": "2026-09-16", "event": "Billion-dollar revenue run rate"},
            {"date": "2026", "event": "Inside more than 100 Fortune 500s; about 500 employees"},
            {"date": "2026", "event": "Citi rollout to about 14,000 of 80,000 technical staff"},
            {"date": "2026-11", "event": "Jane Fraser: about $1.5 billion 2026 insourcing savings"},
            {"date": "2026-11-24", "event": "EP502; security product released that morning"},
        ]},
        "| v4.10 window ILTB EP502",
    )


def ep259():
    quotes = ["人均薪酬高达268万美元", "190亿美元", "24万亿美元"]
    meta = {
        "episode_number": 259,
        "title": "Quant Giants, Anti-Human Strategy, and the AI Compute Bet",
        "guest": "XTX Markets researcher and a former DRW researcher",
        "guest_role": "Quant researchers",
        "date": "2026-11-22",
        "duration_minutes": 150,
        "youtube_url": "https://www.youtube.com/watch?v=yvV2svDKAEA",
        "links": {"youtube": "https://www.youtube.com/watch?v=yvV2svDKAEA", "apple_podcasts": SV, "xiaoyuzhou": SV_XYZ, "fireside": "https://sv101.fireside.fm/273"},
    }
    save_sv(
        "sv101-ep259", meta,
        ["Private:Jane Street", "Private:XTX", "GS"],
        (
            "Jane Street pays about $2.68 million a person. Goldman, one street over, pays "
            "about $400,000. Banks left this spread after Volcker. Jane Street signed about "
            "$19 billion of compute this year. ETFs went from about $70 billion to about "
            "$24 trillion. XTX had about 25,000 GPUs at roughly 200 people by December 2024. "
            "The hiring test is losing your own money so you will not override the model."
        ),
        (
            "E259, Nov 22, about 150 minutes. Two guests from a closed industry: one at "
            "XTX Markets in London, one formerly at DRW, which started in rates and was "
            "present when Lehman fell in 2008. Alex Gerko built XTX from foreign exchange "
            "and has been among Britain's largest taxpayers. Citadel Securities and Hudson "
            "River Trading are in the same spread group. High-Flyer is the Chinese firm "
            "from that window. Manual Chinese captions."
        ),
        [
            (
                "The spread business the banks dropped. Hongjun's picture is an airport "
                "exchange desk: a bid, an offer, a thin gap. Market maker and high-frequency "
                "shop are the same people, machines and models. Goldman and Jane Street sit "
                "one street apart in Manhattan. Goldman pay is about $400,000 a person. Jane "
                "Street pay, from the Bloomberg report she cites, is about $2.68 million. "
                "Banks once ignored electronic market making because the profit looked too "
                "thin. After 2008 the Volcker rule limited proprietary trading with the "
                "bank's own money. Electronics did the rest. Twenty years later these firms "
                "are the new whales. Jane Street's edge was ETFs. That market was about $70 "
                "billion when it entered and about $24 trillion now. This year Jane Street "
                "signed about $19 billion of multi-year compute. XTX is also spending heavily "
                "on compute. Several of these firms were early investors in frontier model labs."
            ),
            (
                "XTX, High-Flyer, and the anti-human rule. XTX was founded around the same "
                "time as OpenAI and bet early on deep learning. It was an early investor in "
                "Anthropic. It once shared a campus with DeepMind. A Financial Times report "
                "from about two years ago, dated December 2024 on the tape, put the firm at "
                "a bit over 200 people and about 25,000 GPUs. Last year three UK operating "
                "entities had about £3.93 billion of net revenue. Public filings imply nearly "
                "$20 million of revenue per employee, which Hongjun calls the highest among "
                "quant shops. Founder Alex Gerko came from FX. The hiring joke is the point: "
                "a researcher who steadily loses a few thousand of his own money, and more in "
                "a bad year, is hired because he will not override the model with a personal "
                "view. His boss says that personal judgment is nothing. High-Flyer, cofounded "
                "by DeepSeek's Liang Wenfeng, is the Chinese firm from the same era. DRW, "
                "the other guest's old shop, started in interest-rate derivatives and was "
                "in the market when Lehman failed in 2008."
            ),
            (
                "Why the strategy is called anti-human. The product is not a star trader. "
                "It is a model that must not be talked out of a print by someone who is sure "
                "this time is different. The compensation gap, $400,000 versus $2.68 million, "
                "is what that model is worth to the people who keep it running. The compute "
                "bills, $19 billion at Jane Street and a large GPU pile at XTX, are the same "
                "bet the labs are making, funded by a spread instead of a subscription. "
                "ETFs supplied Jane Street's volume. Deep learning supplied XTX's. The "
                "regulatory gift was Volcker. None of these firms is a public stock on this "
                "tape except the bank that no longer owns the book. Goldman is the before "
                "picture, one street away and much cheaper per person."
            ),
        ],
        {
            "name": "Thin Spread × No Human Override × Compute Like a Lab",
            "components": (
                "Bid, offer, a small gap, machines. Banks left because the margin looked "
                "thin and Volcker closed proprietary trading. Jane Street pay is about "
                "$2.68 million versus Goldman at about $400,000. ETFs went from about $70 "
                "billion to about $24 trillion. Jane Street signed about $19 billion of "
                "compute this year. XTX, about 200 people and 25,000 GPUs in December 2024, "
                "early Anthropic, about £3.93 billion net revenue and near $20 million per "
                "person. Hire the person who loses his own money so he will not touch the model. That rule is the product."
            ),
            "application": (
                "Private:Jane Street and Private:XTX are the two compute-heavy books. GS is "
                "the firm one street away that no longer owns this spread. Do not buy a "
                "bank because the whale used to sit there. The public tell is the compute "
                "contract and the pay, not a ticker on the tape."
            ),
        },
        [
            {"view": "The spread the banks skipped became the whale.", "question": "What is the pay gap?", "answer": "Goldman about $400,000 a person. Jane Street about $2.68 million, one street over. Volcker plus electronic markets moved the book. ETFs went from about $70 billion to about $24 trillion."},
            {"view": "These firms buy compute like labs.", "question": "How large is the bill?", "answer": "Jane Street about $19 billion of multi-year compute this year. XTX had about 25,000 GPUs at roughly 200 people by December 2024, and was an early Anthropic investor."},
            {"view": "A losing personal account is the hiring test.", "question": "Why not a star trader?", "answer": "XTX wants someone who knows his own judgment is nothing, so he will not override the model. Three UK entities did about £3.93 billion of net revenue, near $20 million a person."},
        ],
        [
            {"ticker": "Private:Jane Street", "direction": "Long", "confidence": "Low", "thesis": "ETF spread book, about $2.68 million pay per person, about $19 billion of compute this year — low"},
            {"ticker": "Private:XTX", "direction": "Long", "confidence": "Low", "thesis": "About 25,000 GPUs, early Anthropic, about £3.93 billion UK net revenue, hire people who will not override the model — low"},
            {"ticker": "GS", "direction": "Long", "confidence": "Low", "thesis": "The Manhattan neighbor at about $400,000 a person, the firm that no longer owns this spread — low"},
        ],
        quotes,
        {"subject": "Jane Street · XTX · the spread banks left", "events": [
            {"date": "2008", "event": "Volcker era begins; DRW is in rates when Lehman fails"},
            {"date": "2010s", "event": "Jane Street rides ETFs from about $70 billion toward $24 trillion"},
            {"date": "2015", "event": "XTX founded near OpenAI; later an early Anthropic investor"},
            {"date": "2024-12", "event": "XTX about 200 people and 25,000 GPUs, per the FT figure on the tape"},
            {"date": "2025", "event": "Three UK entities about £3.93 billion net revenue"},
            {"date": "2026", "event": "Jane Street signs about $19 billion of multi-year compute"},
            {"date": "2026-11-22", "event": "E259 publishes"},
        ]},
        {
            "meta": {"title": "E259｜机械神教与反人性策略：华尔街量化巨头的AI之路", "guest": "XTX Markets 研究员 · 前 DRW 研究员", "guest_role": "量化研究员"},
            "conclusion": "泓君把Jane Street、XTX、Citadel Securities和Hudson River Trading写成股票和ETF交易对面的人，赚的是机场换汇柜台那种薄价差。高盛人均大约40万美元。隔一条街的Jane Street，她引用彭博，人均大约268万美元。银行觉得太薄，沃尔克规则又限制了自营，这块生意让了出去。Jane Street今年签了大约190亿美元的多年算力合同。ETF从它进入时的大约700亿美元到现在大约24万亿美元。XTX和OpenAI差不多同时成立，是Anthropic的早期投资人，2024年12月大约200人和25000张GPU，去年三家英国实体净营收大约39.3亿英镑，人均接近2000万美元。幻方是梁文锋的中国对照。招聘测验是你自己的账户会稳定亏钱，这样你就不会用个人判断去改模型。",
            "background": "E259，11月22日，大约150分钟。两位来自封闭行业的嘉宾：一位在伦敦XTX Markets，一位曾在DRW，利率衍生品起家，2008年雷曼倒下时在场。Alex Gerko从外汇做出XTX，做过英国纳税最多的人之一。中文人工字幕。",
            "facts": [
                "银行丢掉的价差。泓君的图是机场换汇柜台：买价、卖价、中间很薄。做市商和高频说的是同一批人，机器和模型。曼哈顿高盛和Jane Street隔一条街。高盛人均大约40万美元。Jane Street人均，她引用的彭博报道，大约268万美元。银行曾经看不上电子做市，因为利润看起来太薄。2008年之后沃尔克规则限制银行用自己的钱做自营。电子化做了剩下的事。二十年后这些公司是新的巨鲸。Jane Street的优势是ETF。它进入时这个市场大约700亿美元，现在大约24万亿美元。今年Jane Street签了大约190亿美元的多年算力合同。XTX也在重金押算力。其中几家还是前沿模型实验室的早期投资人。",
                "XTX、幻方，以及反人性。XTX和OpenAI差不多同时成立，很早押深度学习，也是Anthropic的早期投资人，曾经和DeepMind在同一个园区。大约两年前的《金融时报》，带子上写的是2024年12月，公司200多人、大约25000张GPU。去年三家英国运营实体净营收大约39.3亿英镑。按公开备案估算，人均接近2000万美元，泓君称为量化公司里最高的一档。创始人Alex Gerko从外汇来，做过英国纳税最多的人。招聘笑话就是论点：一个研究员自己的账户每年稳定亏几千，差的年份亏更多，才会被留下，因为他不会用个人判断去改模型。老板说个人判断什么都不是。幻方由DeepSeek的梁文锋联合创办，是同一时期的中国公司。另一位嘉宾的旧东家DRW从利率衍生品起家，雷曼2008年倒下时在场。",
                "为什么叫反人性。产品不是明星交易员，是一个不能被「这次不一样」说动的模型。40万美元对268万美元的薪酬差，是这个模型对维护它的人值多少钱。算力账单，Jane Street大约190亿美元，XTX一大堆GPU，是和实验室同一笔赌注，资金来自价差而不是订阅。ETF给了Jane Street成交量。深度学习给了XTX。监管送的礼是沃尔克。这期带子上除了已经不再拥有这块账本的银行，这些公司都不是上市股票。高盛是「之前」的画面，隔一条街，每个人便宜得多。",
            ],
            "mental": {
                "name": "薄价差 × 不许人改模型 × 像实验室一样买算力",
                "components": "买价、卖价、一条小缝、机器。银行离开是因为利润看起来薄，沃尔克关掉了自营。Jane Street人均大约268万美元，高盛大约40万。ETF从大约700亿美元到大约24万亿美元。Jane Street今年大约190亿美元算力。XTX在2024年12月大约200人和25000张GPU，早期投了Anthropic，净营收大约39.3亿英镑，人均近2000万美元。雇那个会把自己的钱亏掉的人，这样他不会去碰模型。",
                "application": "Private:Jane Street和Private:XTX是两本重算力的账。GS是隔街那家不再拥有这个价差的公司。不要因为巨鲸以前坐在银行里就去买银行。公开的信号是算力合同和薪酬，不是带子上的一个交易代码。",
            },
            "insights": [
                {"view": "银行跳过的价差变成了巨鲸。", "question": "薪酬差多少？", "answer": "高盛大约每人40万美元。Jane Street大约268万美元，隔一条街。沃尔克加上电子市场把账本搬走了。ETF从大约700亿美元到大约24万亿美元。"},
                {"view": "这些公司和实验室一样买算力。", "question": "账单有多大？", "answer": "Jane Street今年大约190亿美元的多年合同。XTX到2024年12月大约200人、25000张GPU，并且是Anthropic的早期投资人。"},
                {"view": "自己的账户会亏，才是招聘测验。", "question": "为什么不是明星交易员？", "answer": "XTX要一个知道自己的判断什么都不是的人，这样他不会改模型。三家英国实体净营收大约39.3亿英镑，人均接近2000万美元。"},
            ],
        },
    )


def ep260():
    quotes = ["英伟达的股价开盘上涨30%", "黄仁勋和CFO Colette Kress", "超过20%的股价飙升"]
    meta = {
        "episode_number": 260,
        "title": "Nvidia, CoreWeave, and the Compute Credit Market",
        "guest": "Maggie Wang and Ethan Xu",
        "guest_role": "Founder, Anoris Capital · data-center and energy strategist",
        "date": "2026-11-24",
        "duration_minutes": 86,
        "youtube_url": "https://www.youtube.com/watch?v=aZlaPfp_2-U",
        "links": {"youtube": "https://www.youtube.com/watch?v=aZlaPfp_2-U", "apple_podcasts": SV, "xiaoyuzhou": SV_XYZ, "fireside": "https://sv101.fireside.fm/274"},
    }
    save_sv(
        "sv101-ep260", meta,
        ["NVDA", "CRWV", "MSFT"],
        (
            "The episode was taped November 17, the night of Nvidia's third-quarter "
            "print, while the board was still saying Jensen Huang would not return. "
            "The published open is November 23: he is CEO again, the stock opens up "
            "about 30%, and CoreWeave jumps more than 20%. Huang and CFO Colette Kress "
            "disagreed on neo-cloud guarantees. A guarantee starts when a project can be "
            "turned on. Microsoft and CoreWeave do not borrow on the same terms."
        ),
        (
            "E260, Nov 24, about 86 minutes. Yiwen hosts with Hongjun. Maggie Wang runs "
            "Anoris Capital and studies credit. Ethan Xu works on data-center planning "
            "and energy. They say the management discussion is what they knew on "
            "November 17, and that the market has been moving in hundreds of billions "
            "on Nvidia-linked headlines. Manual Chinese captions."
        ),
        [
            (
                "The week the tape is about. Recorded November 17, earnings night. The "
                "board was still insisting Huang would not be asked back. The open the "
                "show publishes is November 23: Nvidia reappoints him, he says he made "
                "a serious mistake and is returning, the stock opens about 30% higher, "
                "and the neo-clouds tied to Nvidia, CoreWeave, Nebius, and IREN, rise "
                "more than 20%. Maggie reads the print as demand that is not in doubt. "
                "Agent workflows show up as data-center orders for hyperscalers and "
                "neo-clouds. The interim CEO, who had been the CFO, also said vendor "
                "financing would be reviewed more carefully, and that guarantees begin "
                "when a project can be put into service, not while it is stuck. That "
                "is the line the market still has to digest. A week of Nvidia headlines "
                "moved on the order of hundreds of billions across the AI complex."
            ),
            (
                "Two strategies inside one guarantee. Ethan and Maggie both treat Nvidia "
                "as the company whose words move the build, maybe the single most "
                "important firm in the AI industry. A month or two earlier, high interest "
                "on AI borrowers had already hit the stocks. Huang told the market the "
                "operators were fine and that Nvidia did not even need to step in. "
                "Confidence in the neo-clouds returned. The worry on November 17 is "
                "that Huang and Colette Kress had disagreed on guarantees and financing "
                "for these clouds. If he is not CEO, implicit promises may not be kept "
                "when a partner's cash is about to break. The question is whether Nvidia "
                "still supplies emergency money and a guarantee in a crunch, for the "
                "industry rather than for one credit. They say that has to be watched, "
                "not assumed from the old habit."
            ),
            (
                "Who borrows, and who eats a delay. The show's earlier video was on how "
                "large clouds use capital markets and leverage for capex. This hour goes "
                "from debt and power, with Nvidia as the start. CoreWeave's stock is the "
                "roller coaster of the year, including a move of more than 20% on November 23. Microsoft, Meta, and CoreWeave are all "
                "building data centers and do not borrow at the same cost or on the same "
                "conditions. If a project slips, someone has to carry the financial risk. "
                "The guarantee that starts only when the site can be turned on leaves "
                "the construction period with the borrower. Power is Ethan's half: "
                "planning a data center is an energy-transition problem, not only a chip "
                "order. Demand is the part Maggie calls affirmed. The credit terms are "
                "the part that still depends on who is CEO and how far the CFO will sign."
            ),
        ],
        {
            "name": "Chip Seller × Guarantee × Unequal Borrowers",
            "components": (
                "November 17 tape, November 23 open: Huang back, stock about 30% up, "
                "CoreWeave, Nebius, and IREN more than 20%. Nvidia sells the chip, "
                "funds customers, buys compute, and has guaranteed financing. Huang "
                "and Colette Kress split on how far neo-cloud guarantees go. A "
                "guarantee that starts at switch-on leaves the delay with the borrower. "
                "Microsoft, Meta, and CoreWeave do not pay the same rate. Agent demand "
                "is not the questioned half. Hundreds of billions move on his sentences."
            ),
            "application": (
                "NVDA is the firm whose CEO and CFO disagree on the rescue. CRWV is the "
                "roller-coaster borrower, not Microsoft's credit. MSFT is the cheap "
                "borrower in the same build. Do not treat a 30% open as the underwriting. "
                "Underwrite who signs if the site is late."
            ),
        },
        [
            {"view": "The open and the taping are six days apart.", "question": "What changed by November 23?", "answer": "Taped November 17, board still refusing a return. The published open is Huang back as CEO, the stock up about 30%, and CoreWeave, Nebius, and IREN up more than 20%."},
            {"view": "Demand is not the argument. The signature is.", "question": "Where did Huang and the CFO split?", "answer": "On guarantees and financing for neo-clouds. The print says support continues but vendor financing gets a harder look, and the guarantee starts when the project can be turned on."},
            {"view": "Three builders, three borrowing costs.", "question": "Who eats a delay?", "answer": "Microsoft, Meta, and CoreWeave do not borrow on the same terms. CoreWeave is the year's roller coaster. A late site sits with the borrower until the guarantee begins."},
        ],
        [
            {"ticker": "NVDA", "direction": "Long", "confidence": "Medium", "thesis": "The firm whose CEO return, on this tape, opens the stock about 30% and moves neo-clouds with it — medium"},
            {"ticker": "CRWV", "direction": "Long", "confidence": "Low", "thesis": "The neo-cloud roller coaster, up more than 20% with the return, borrowing on worse terms than Microsoft — low"},
            {"ticker": "MSFT", "direction": "Long", "confidence": "Low", "thesis": "Same data-center build, cheaper and cleaner borrowing than CoreWeave when a project slips — low"},
        ],
        quotes,
        {"subject": "Nvidia · CoreWeave · who signs the guarantee", "events": [
            {"date": "2026-09", "event": "High interest on AI borrowers hits neo-cloud stocks; Huang says they are fine"},
            {"date": "2026-11-17", "event": "Taping, Q3 night; board still says Huang will not return"},
            {"date": "2026-11-17", "event": "Print: demand affirmed; guarantees start when a project can be used"},
            {"date": "2026-11-23", "event": "Published open: Huang back, stock about 30% higher"},
            {"date": "2026-11-23", "event": "CoreWeave, Nebius, IREN up more than 20%"},
            {"date": "2026-11-24", "event": "E260 publishes"},
        ]},
        {
            "meta": {"title": "E260｜黄仁勋归来之际，深聊英伟达、CoreWeave和算力信用市场", "guest": "Maggie Wang · Ethan Xu", "guest_role": "Anoris Capital 创始人 · 数据中心与能源策略"},
            "conclusion": "这期录于11月17日，英伟达三季报当晚，董事会当时仍说不会请黄仁勋回来。节目发布时的开头是11月23日：他重新担任CEO，股价开盘大约涨30%，CoreWeave、Nebius和IREN涨超过20%。Anoris Capital的Maggie Wang和做数据中心与电力的Ethan Xu把英伟达写成卖芯片、投资客户、采购算力，并且为融资做担保的公司。黄仁勋和CFO Colette Kress在新云担保做到多远上有过分歧。如果他不是CEO，现金要断时那些隐性承诺未必兑现。财报上的担保从项目能够投入使用才开始。微软、Meta和CoreWeave借钱的条件不一样。智能体需求不是问题。延期了谁付钱才是问题。",
            "background": "E260，11月24日，大约86分钟。Yiwen和泓君一起主持。Maggie Wang做信用。Ethan Xu做数据中心规划和能源。他们说管理层讨论停留在11月17日已知的信息，英伟达相关头条可以带动上千亿的市值波动。中文人工字幕。",
            "facts": [
                "这一周。11月17日财报夜录的。董事会当时仍坚持不会请黄仁勋回来。节目给出的开头是11月23日：英伟达重新任命他，他说自己犯了很严重的错误、即将回来，股价开盘大约高30%，和英伟达绑在一起的新云CoreWeave、Nebius、IREN涨超过20%。Maggie把财报读成需求没有问题。智能体工作流变成超大规模云和新云的数据中心订单。临时CEO，也就是原来的CFO，同时说会更严格地评估供应商融资，担保从项目可以投入使用时才开始，而不是卡在建设里的时候。这是市场还要消化的一句。一周的英伟达头条，在整个AI复合体上是上千亿的波动。",
                "同一份担保里的两种策略。Ethan和Maggie都把英伟达当成话语能推动建设的公司，也许是AI行业里最重要的那一家。一两个月前，AI借款人的高利息已经打过这些股票。黄仁勋当时告诉市场运营商没问题，英伟达甚至不必亲自下场。新云的信心回来了。11月17日的担心是，黄仁勋和Colette Kress在给这些云做担保和融资上有过较大分歧。如果他不是CEO，伙伴的现金要断时，隐性承诺未必还会兑。问题是危急时英伟达还会不会为了行业、而不只是为了一笔信用，提供紧急资金和担保。他们说这件事要看，不能用旧习惯直接假定。",
                "谁在借，延期谁承担。节目更早的视频讲大型云怎么用资本市场和杠杆支撑资本开支。这一小时从债务和电力讲，英伟达是起点。CoreWeave的股价是今年的过山车。微软、Meta和CoreWeave都在建数据中心，借钱的成本和条件不一样。项目延期，得有人承担金融风险。担保要到场地能够开机才开始，建设期就留在借款人身上。电力是Ethan的一半：规划数据中心是能源转型问题，不只是芯片订单。需求是Maggie称为已经被肯定的那一半。信用条款仍取决于谁是CEO，以及CFO愿意签多远。",
            ],
            "mental": {
                "name": "卖芯片的人 × 担保 × 不平等的借款人",
                "components": "11月17日的录音，11月23日的开头：黄仁勋回来，股价大约涨30%，CoreWeave、Nebius、IREN超过20%。英伟达卖芯片、给客户钱、买算力，并且做过融资担保。黄仁勋和Colette Kress在新云担保做到多远上有分裂。开机才生效的担保，把延期留在借款人身上。微软、Meta和CoreWeave不是同一个利率。智能体需求不是被质疑的那一半。他的句子可以带动上千亿。",
                "application": "NVDA是CEO和CFO在救援上有分歧的那家公司。CRWV是过山车借款人，不是微软的信用。MSFT是同一场建设里更便宜的借款人。不要把30%的开盘当成尽调。要尽调的是场地晚了谁签字。",
            },
            "insights": [
                {"view": "开头和录音隔了六天。", "question": "11月23日变了什么？", "answer": "11月17日录的，董事会仍拒绝回归。发布的开头是黄仁勋回到CEO，股价大约涨30%，CoreWeave、Nebius和IREN涨超过20%。"},
                {"view": "需求不是争论点。签名才是。", "question": "黄仁勋和CFO分在哪？", "answer": "分在给新云的担保和融资。财报说支持还在，但供应商融资会看得更严，担保从项目能够投入使用才开始。"},
                {"view": "三个建设者，三种借钱成本。", "question": "延期谁承担？", "answer": "微软、Meta和CoreWeave的借款条件不同。CoreWeave是今年的过山车。场地晚了，在担保开始之前停在借款人身上。"},
            ],
        },
    )


def ep261():
    quotes = ["仅次于法国的", "近1/4的美国家庭", "同比增长了380%"]
    meta = {
        "episode_number": 261,
        "title": "How Korean Beauty Took the US Shelf",
        "guest": "Kelly Peng and Han Xiao",
        "guest_role": "US-based business writer · editor, Beauty Insider",
        "date": "2026-11-26",
        "duration_minutes": 90,
        "youtube_url": "https://www.youtube.com/watch?v=7uXtzRAf4PM",
        "links": {"youtube": "https://www.youtube.com/watch?v=7uXtzRAf4PM", "apple_podcasts": SV, "xiaoyuzhou": SV_XYZ, "fireside": "https://sv101.fireside.fm/275"},
    }
    save_sv(
        "sv101-ep261", meta,
        ["EL", "LRLCY", "Private:Silicon2"],
        (
            "Mahua, Kelly Peng, and Han Xiao of Beauty Insider treat Korean beauty as "
            "an export policy, not a cheap cream. Korea has passed the US to become "
            "the second-largest beauty exporter after France. Global sales more than "
            "doubled in two years. Nearly a quarter of American households have used a "
            "Korean product. APR's European revenue was up about 380% in the second "
            "quarter. Silicon2 switched from chips in 2012 and now lists more than 430 "
            "brands, with US warehouses."
        ),
        (
            "E261, Nov 26, about 90 minutes. A joint episode of Silicon Valley 101 and "
            "its consumer show, hosted by contributing researcher Mahua. Kelly Peng "
            "writes from the Bay Area. Han Xiao edits Beauty Insider, a trade title. "
            "Manual Chinese captions. The claim is culture plus a group supply chain, "
            "not a low price alone. Amorepacific, founded in 1945, and LG Household and "
            "Health still own old labels and buy new ones. Olive Young, Sephora, and "
            "Costco are shelves, not the exporters. A product at $10 to $50 is the "
            "price that surprises people and is not the cause."
        ),
        [
            (
                "The export numbers. Across third-party counts, Korean beauty sales "
                "more than doubled globally in two years. The US is now the largest "
                "export destination. Nearly one in four American households has used "
                "a Korean product. Western Europe is growing faster than North America. "
                "Exports to the UK rose about 1.8 times in the first three quarters. "
                "APR, a newer group, grew European revenue about 380% in the second "
                "quarter. Korea has passed the US and sits second only to France as a "
                "beauty exporter. The price that surprises people is low: about 100 "
                "to 200 yuan, or $10 to $50, for products that sound technical. Kelly "
                "and Han Xiao say the heat is not the price. It is the control of a "
                "marketing concept, a state policy that sends culture out to carry "
                "the product, and a supply chain that leaves as a group rather than "
                "as one brand."
            ),
            (
                "Old groups and new labels. The 1.0 brands and the 2.0 brands are "
                "partly the same companies. Amorepacific, founded in 1945, still has "
                "Sulwhasoo, Laneige, and Innisfree, and the 2.0 snail line COSRX, and "
                "it has been buying newer names such as Aestura. LG Household and "
                "Health is the other old giant that is still here. The new fortunes "
                "are often one group with a long list of small brands, each brand "
                "built around one hero product. Medicube is the example they use. "
                "Centralized media made Estee Lauder, L'Oreal, and Helena Rubinstein, "
                "and also Chinese names such as Proya. That broadcast is hard to "
                "repeat, outside elevator ads people hate. The new Korean labels "
                "spread through circles, then through US shelves at Sephora and "
                "Costco and through Olive Young at home. Local American influencers, "
                "not only Korean celebrities, now carry the product. Kendall Jenner "
                "is one of the endorsements they mention."
            ),
            (
                "The distributor that used to sell chips. Silicon2 is the firm Mahua "
                "found organizing the overseas shelf, especially in Europe and, in "
                "the conversation, the US network. It was founded in 2002 as a "
                "semiconductor trader. In 2012, as Korean beauty was growing, it "
                "switched to cosmetics distribution. It is now one of the larger "
                "Korean beauty distributors. US warehouses mean the box does not have "
                "to come through Hong Kong, which changes time and cost versus peers "
                "that only store in Hong Kong. It works with more than 430 Korean "
                "brands. That is the group exit: culture, a pile of hero SKUs, and a "
                "distributor that already knows how to move physical goods across a "
                "border because it used to move chips. The Western incumbents on the "
                "tape are the brands of the broadcast era. They are not the ones "
                "opening the US warehouse."
            ),
        ],
        {
            "name": "Culture First × Hero SKU × A Chip Trader's Warehouse",
            "components": (
                "Second-largest beauty exporter after France, ahead of the US. Sales "
                "more than doubled in two years. US is the top destination. Nearly a "
                "quarter of American homes have used a Korean product. UK exports "
                "about 1.8 times in three quarters. APR Europe about 380% in one "
                "quarter. Price $10 to $50 is not the cause. Amorepacific, since 1945, "
                "buys the new labels. Silicon2, chips from 2002, cosmetics from 2012, "
                "more than 430 brands, US warehouses. Estee and L'Oreal are the old "
                "broadcast brands. The warehouse, not the $10 bottle, is the operating asset."
            ),
            "application": (
                "EL and LRLCY are the incumbents this wave is routing around, not the "
                "exporters. Private:Silicon2 is the distributor that makes the US shelf "
                "possible. Do not underwrite a salmon essence. Underwrite who owns the "
                "warehouse and how many hero SKUs sit behind one group."
            ),
        },
        [
            {"view": "Korea is now the number two beauty exporter.", "question": "What are the figures?", "answer": "Past the US, second to France. Global sales more than doubled in two years. The US is the top destination. Nearly one in four American households has used a product. APR's Europe was up about 380% in the second quarter."},
            {"view": "The old groups are buying the new labels.", "question": "Is Amorepacific finished?", "answer": "Founded in 1945, still Sulwhasoo and Laneige, plus COSRX, and it bought Aestura. LG Household and Health is the other old giant. New money is often one group and many small brands, Medicube among them."},
            {"view": "A chip trader now holds the US warehouse.", "question": "What is Silicon2?", "answer": "Founded in 2002 in semiconductor trade, switched to cosmetics in 2012, more than 430 Korean brands, warehouses in the US so the box does not wait in Hong Kong."},
        ],
        [
            {"ticker": "EL", "direction": "Long", "confidence": "Low", "thesis": "Named as a centralized-media brand this Korean wave is not using to open the US shelf — low"},
            {"ticker": "LRLCY", "direction": "Long", "confidence": "Low", "thesis": "The other broadcast-era incumbent on the tape, beside Estee, not the exporter — low"},
            {"ticker": "Private:Silicon2", "direction": "Long", "confidence": "Low", "thesis": "Semiconductor trader from 2002, cosmetics since 2012, 430-plus brands and US warehouses — low"},
        ],
        quotes,
        {"subject": "Korean beauty · Silicon2 · Amorepacific", "events": [
            {"date": "1945", "event": "Amorepacific founded"},
            {"date": "2002", "event": "Silicon2 founded in semiconductor trade"},
            {"date": "2012", "event": "Silicon2 switches to cosmetics distribution"},
            {"date": "2024-26", "event": "Global Korean beauty sales more than double; US becomes top destination"},
            {"date": "2026", "event": "APR Europe about 380% in Q2; UK exports about 1.8x in three quarters"},
            {"date": "2026-11-26", "event": "E261 publishes"},
        ]},
        {
            "meta": {"title": "E261｜表演有效、组团出海，韩国美妆如何抢占美国市场？", "guest": "Kelly Peng · 寒笑", "guest_role": "美国商业博主 · 《美妆内行人》主编"},
            "conclusion": "麻花、Kelly Peng和《美妆内行人》的寒笑把韩妆写成出口政策，不是便宜的面霜。韩国已经超过美国，成为仅次于法国的第二大美妆出口国。全球销售额两年里增长一倍多。美国是最大出口目的地，近四分之一的美国家庭用过韩妆。西欧增速快过北美。前三季度对英国出口大约增长1.8倍。APR第二季度欧洲营收大约增长380%。单品可以是10到50美元。1945年的爱茉莉太平洋和LG生活健康在买新牌子，而不只是守着雪花秀和兰芝。Silicon2于2002年做半导体贸易，2012年改做化妆品分销，现在超过430个韩国品牌，美国有仓。雅诗兰黛和欧莱雅是这波浪潮不是的那种集中媒体品牌。",
            "background": "E261，11月26日，大约90分钟。《硅谷101》和消费子栏目的串台，特约研究员麻花主持。Kelly Peng在湾区写商业。寒笑主编行业媒体《美妆内行人》。中文人工字幕。论点是文化加上成组的供应链，不只是低价。",
            "facts": [
                "出口数字。综合第三方统计，韩妆全球销售额两年里增长一倍多。美国现在是最大出口目的地。近四分之一的美国家庭用过韩妆。西欧增速快过北美。前三季度对英国出口大约增长1.8倍。较新的集团APR，第二季度欧洲营收大约增长380%。韩国已经超过美国，美妆出口仅次于法国。让人惊讶的价格其实不高：大约一百到两百人民币，或10到50美元，听起来却很技术。Kelly和寒笑说热度不是价格。是营销概念控得住，国家用文化出海带产品，以及供应链成组离开，而不是一个牌子单飞。",
                "老集团和新牌子。1.0和2.0背后有一部分是同一批公司。爱茉莉太平洋1945年成立，仍有雪花秀、兰芝、悦诗风吟，也有2.0的蜗牛线COSRX，并且在买更新的名字，比如Aestura。LG生活健康是另一家还在的老巨头。新的造富经常是一个集团、一长串小品牌，每个牌子打一个英雄单品。Medicube是他们用的例子。集中媒体时代造出了雅诗兰黛、欧莱雅、赫莲娜，也有中国的珀莱雅。那种广播很难再做，除了人们讨厌的电梯广告。新的韩国牌子走圈层，再走丝芙兰、Costco的美国货架，以及国内的Olive Young。现在带货的不只有韩国明星，还有美国本地网红。Kendall Jenner是他们提到的代言之一。",
                "以前卖芯片的分销商。Silicon2是麻花找到的、在组织海外货架的公司，尤其在欧洲，对话里也有美国网络。2002年成立时做半导体贸易。2012年韩国美妆在长，它改做化妆品分销。现在是较大的韩国美妆分销商之一。美国有仓，箱子不必经香港，时间和成本都跟只有香港仓的同行不同。合作品牌超过430个。这就是组团出海：文化、一堆英雄SKU，以及一个本来就会把实物运过边境的分销商，因为它以前运的是芯片。带子上的西方在位者是广播时代的品牌。开美国仓的不是它们。",
            ],
            "mental": {
                "name": "文化先行 × 英雄单品 × 芯片商人的仓库",
                "components": "美妆出口国里仅次于法国，超过美国。销售额两年里一倍多。美国是最大目的地。近四分之一的美国家庭用过韩妆。英国三个季度大约1.8倍。APR欧洲一个季度大约380%。10到50美元不是原因。爱茉莉太平洋从1945年买新牌子。Silicon2，2002年的芯片，2012年的化妆品，430多个品牌，美国有仓。雅诗兰黛和欧莱雅是旧的广播品牌。",
                "application": "EL和LRLCY是这波在绕开的在位者，不是出口方。Private:Silicon2是让美国货架成为可能的分销商。不要去尽调一瓶三文鱼精华。要尽调仓库在谁手里，一个集团后面有多少英雄单品。",
            },
            "insights": [
                {"view": "韩国现在是第二大美妆出口国。", "question": "数字是什么？", "answer": "超过美国，仅次于法国。全球销售两年里一倍多。美国是最大目的地。近四分之一的美国家庭用过。APR欧洲第二季度大约增长380%。"},
                {"view": "老集团在买新牌子。", "question": "爱茉莉太平洋结束了吗？", "answer": "1945年成立，仍有雪花秀和兰芝，加上COSRX，还买了Aestura。LG生活健康是另一家老巨头。新钱常常是一个集团、很多小品牌，Medicube是其中之一。"},
                {"view": "一个芯片商人现在握着美国的仓。", "question": "Silicon2是什么？", "answer": "2002年做半导体贸易，2012年改化妆品，430多个韩国品牌，美国有仓，箱子不必在香港等。"},
            ],
        },
    )


if __name__ == "__main__":
    ep502()
    ep259()
    ep260()
    ep261()
