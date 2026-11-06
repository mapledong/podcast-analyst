#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Bilingual TZS E207–E208."""
from __future__ import annotations

import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))
from scripts._window_lib import dump, en_std, validate_file  # noqa: E402
from src.chinese_transcript import load_transcript_body, quote_supported_in_transcript, transcript_path  # noqa: E402

APPLE = "https://podcasts.apple.com/cn/podcast/id1718660227"


def check(eid, quotes):
    body = load_transcript_body(transcript_path(eid))
    for q in quotes:
        ok = quote_supported_in_transcript(q, body)
        print(eid, "OK" if ok else "FAIL", q)
        if not ok:
            raise SystemExit(q)


def write_pair(eid, en, zh):
    dump(ROOT / f"data/approved/{eid}.json", en)
    dump(ROOT / f"data/approved/zh/{eid}.json", zh)
    validate_file(ROOT / f"data/approved/{eid}.json")


def ep207():
    eid = "tzs-ep207"
    quotes = ["全網只有3000本", "買了茅台跌了10個點", "紫金漲了10倍"]
    check(eid, quotes)
    meta = {
        "episode_number": 207,
        "title": "Yongqing on Practical Stock Investing, and the US–China Financial Circuit",
        "guest": "Yongqing",
        "guest_role": "Host · author, Practical Stock Investing",
        "date": "2026-10-28",
        "duration_minutes": 97,
        "youtube_url": "",
        "links": {
            "apple_podcasts": APPLE,
            "xiaoyuzhou": "https://www.xiaoyuzhoufm.com/episode/6ae1f123c96c8942ec13c18e",
        },
    }
    concl = (
        "Yongqing walks his book, finished around September 2024 and delayed after the "
        "September 24 policy rally. About 3,000 copies at 40 yuan, royalty near 10,000 yuan. "
        "ChatGPT said the method is fine and the hole is the "
        "portfolio and the trade. Outside money will not sit through Moutai down 10 points "
        "while AI is up 50. Zijin is the split: 10 times since 2019, profit about 4 times, "
        "and 60–70% of the stock move was the metal price. US listings fell from about 7,000 "
        "to 5,000 while China still lists to fund the shift."
    )
    bg = (
        "E207, Oct 28, about 97 minutes. Yongqing solo on the book and a US–China circuit "
        "compare. The book is frameworks, methods, and cases, not a worldview. He says the "
        "share itself is about 75 minutes. Whisper is traditional-character small. A disclaimer "
        "on the tape: not a recommendation, history is not the future."
    )
    facts = [
        (
            "The book is a thinking tool with a tiny print. He finished it around September 2024. "
            "After the September 24, 2024 policy turn, stock books got crowded and this one slipped "
            "a year or two. About 3,000 copies, cover near 40 yuan, author share 15–20%, so roughly "
            "10,000 yuan. A paid community at 1,000 yuan a head can clear 100,000 yuan faster. He "
            "wrote it anyway, by hand in early 2024 before chat tools were good, because a book "
            "forces a system: financials, valuation, business model. He later sent the file to "
            "ChatGPT. The model said the method is fine and the hole is portfolio construction and "
            "when to buy or sell — the eye stays on the single name and misses the book. That is "
            "the supplement he wants this hour to add."
        ),
        (
            "Agency, then two case files. Own money can wait three flat years. Other people's money "
            "gets two months. From April to June they ask why he did not own more AI. In August "
            "they ask why he did not sell. He bought AI-up-50% as the benchmark and Moutai down "
            "10 points as the holding that makes him look stupid. Zijin, in his Deng Xiaofeng "
            "review: bought around 2019, stock up 10 times since, profit up about 4 times. About "
            "60–70% of the 10 times is the commodity price. About 40% is profit. Strip the price "
            "and a bad six-year hold is still about 2 to 2.5 times from profit growth. Apple is "
            "the multiple file: bought when growth was soft and the balance sheet was net cash, "
            "earnings he puts near $50 billion a year, the multiple from the teens to the thirties. "
            "Price, profit, and multiple are three different checks. A 60,000-yuan unit profit that "
            "becomes 8,000 under auction pricing breaks the model; a cost-plus price that steps up "
            "is the comfortable path."
        ),
        (
            "Two circuits. US listed names fell from about 7,000 to about 5,000. After the 1990s "
            "the bar rose: a few hundred delistings a year, fewer IPOs than exits, a market that "
            "feels like it is there to make money. China, in his telling, lists companies to fund "
            "a technology shift, so supply keeps coming and the index experience is worse. US "
            "market cap sits in the first two or three hundred names. A-shares will not allow that "
            "concentration, and the small-cap tail matters. S&P 100 ROE and ROIC rose from 2011 "
            "to 2023. China's went down. A Goldman note he cites puts local state holdco ROIC "
            "under 1. US mix is consumption, health, and tech, plus buybacks. Chinese listed "
            "companies hoard cash the way households do. Leverage: "
            "Chinese households and firms borrow. The US borrower is the federal government. "
            "Pensions there are a standing bid for equities. Here, "
            "equities are small next to banks, retail is a large share of both assets and turnover, "
            "there is no real short, and the sales loop is product push. There, stocks are the "
            "core asset, institutions hold them, and the client pays the manager."
        ),
    ]
    mental = {
        "name": "Single-Name Method × Price versus Profit × Two Circuits",
        "components": (
            "The book is the single-name method. ChatGPT's hole is the portfolio and the trade. "
            "Own capital can wait. Outside capital benchmarks you against AI up 50 and Moutai "
            "down 10. Split a 10-times Zijin into price (about 60–70%) and profit (about 4 times, "
            "or 2–2.5 times with the price stripped). Apple is the multiple moving from the teens "
            "to the thirties on about $50 billion of earnings. The US circuit delists, concentrates, "
            "raises ROE, and has pensions as a bid. The China circuit lists to fund a shift, "
            "hoards cash, borrows at the household and the firm, and sells funds to retail. A "
            "3,000-copy book at 40 yuan is the system. It is not the P&L."
        ),
        "application": (
            "2899.HK is the 2019-to-now file: 10 times, with most of it the metal price and a "
            "still-positive profit residual. AAPL is the multiple expansion he walks, from a soft "
            "growth year and net cash to the thirties. 600519.SZ is the agency pain, down 10 points "
            "while AI ran, not a broken-product short. Do not buy the index because the US delists "
            "more. Underwrite which of the three checks — price, profit, multiple — you are being paid."
        ),
    }
    insights = [
        {
            "view": "The book pays worse than a community and that is fine.",
            "question": "Why write it?",
            "answer": "About 3,000 copies, 40 yuan, 15–20% royalty, roughly 10,000 yuan. A 1,000-yuan community clears more. The book forces the system ChatGPT can then critique.",
        },
        {
            "view": "Split the 10 times.",
            "question": "What did Zijin actually pay?",
            "answer": "Stock 10 times since 2019. Profit about 4 times. About 60–70% of the stock move is the price. A bad six years on profit alone is still about 2–2.5 times.",
        },
        {
            "view": "The US market shrinks its share count. China uses listings as policy.",
            "question": "What is the circuit gap?",
            "answer": "About 7,000 US names to 5,000, a few hundred delistings a year. S&P 100 ROE rose from 2011 to 2023. China ROE fell. Pensions bid there. Retail and cash hoards sit here.",
        },
    ]
    invest = [
        {"ticker": "2899.HK", "direction": "Long", "confidence": "Low", "thesis": "10 times since 2019, about 60–70% of it the metal price, profit growth still about 2–2.5 times in a bad six-year case — low"},
        {"ticker": "AAPL", "direction": "Long", "confidence": "Low", "thesis": "Multiple from the teens to the thirties on roughly $50 billion of earnings, bought when growth was soft — low"},
        {"ticker": "600519.SZ", "direction": "Long", "confidence": "Low", "thesis": "The down-10-points holding next to AI up 50; the pain is agency, not a vanished product — low"},
    ]
    chrono = {
        "subject": "Book · Zijin · US vs China listings",
        "events": [
            {"date": "2011–23", "event": "S&P 100 ROE/ROIC up; China shareholder returns down"},
            {"date": "2019", "event": "Zijin hold he reviews; stock later 10x, profit ~4x"},
            {"date": "2024-09", "event": "Book finished; Sept 24 policy delays the print"},
            {"date": "2024–26", "event": "About 3,000 copies, ~40 yuan, royalty ~10,000 yuan"},
            {"date": "2026", "event": "US listings ~7,000 to ~5,000 in his count"},
            {"date": "2026-10-28", "event": "E207 publishes"},
        ],
    }
    en = en_std(
        eid, "Practical Investments", "Yongqing & David", meta, 3,
        ["2899.HK", "AAPL", "600519.SZ"],
        concl, bg, facts, mental, insights, invest, quotes, chrono,
        "| v4.10 window TZS E207", "whisper-small",
    )
    zh_meta = dict(meta)
    zh_meta.update(
        title="E207 永庆分享《股票投资实战派》、中美金融大循环对比",
        guest="永庆",
        guest_role="主播 · 《股票投资实战派》作者",
    )
    zh = dict(en)
    zh.update({
        "podcast": "投资实战派",
        "host": "永庆 & David",
        "metadata": zh_meta,
        "conclusion": (
            "永庆讲自己的书。大约2024年9月写完，9月24日政策之后股票书变挤，这本拖了一两年。"
            "大约3000本、40块，版税大约1万。写书是为了逼出系统，不是为了稿费。"
            "他把文件发给ChatGPT，模型说方法可以，缺的是组合和买卖。"
            "管别人的钱扛不住茅台跌10个点、AI涨50%。紫金是干净的拆法：2019年以来10倍，利润大约4倍，"
            "10倍里大约60%–70%是金属价格。美股上市公司从大约7000家减到5000家，中国仍用上市给转型融资。"
        ),
        "background": (
            "E207，10月28日，大约97分钟。永庆一个人讲书，再比中美金融循环。书是框架、方法和案例，不是世界观。"
            "他说这次分享大约75分钟。Whisper是繁体小模型。带子上的声明：不是推荐，历史不是未来。"
        ),
        "important_facts": [
            "书写完大约是2024年9月。9月24日政策之后，股票书热闹起来，这本非名作者的稿又拖了一两年。全网大约3000本，定价大约40元，版税15%–20%，大约1万元。知识星球一头1000元，更容易到10万。他仍然写，因为2024年上半年聊天工具还不强，手写能逼出财务、估值和商业模式。后来把文件发给ChatGPT。模型说方法论可以，没讲组合管理和买卖，眼睛停在个股，没看到组合。这小时要补的就是这个洞。",
            "自己的钱可以熬三年不涨。别人的钱两个月就问。4月到6月问为什么不多配AI。8月问为什么不卖。他用的对照是AI涨了50%，茅台跌了10个点，持有的人显得很蠢。紫金是他复盘邓晓峰的案子：大约2019年买，到现在股价10倍，利润大约4倍。10倍里大约60%–70%是价格，大约40%是利润。去掉价格，差的六年持有仍然大约2到2.5倍，来自利润。苹果是倍数档案：增长偏软、账上净现金时买，一年利润他放到大约500亿美元，倍数从十几倍到三十几倍。价格、利润、倍数是三次不同的检查。单位利润从6万变成拍卖定价下的8千，模型就坏了。成本定价再一步步提价，才是舒服的路径。",
            "两个循环。美股上市公司从大约7000家减到大约5000家。90年代以后门槛提高，一年退市三五百家，上市少于退出，市场像是来赚钱的。中国在他的说法里用上市给科技转型出钱，供给一直来，指数体验更差。美股市值坐在前面两三百家。A股不允许那样集中，小公司尾巴仍然重要。标普100的ROE和ROIC在2011年到2023年往上。中国往下。他引用的高盛笔记里，地方国有控股平台的ROIC不到1。制造和出口要资本开支，还有过剩产能。美国结构是消费、医疗和科技，加上回购。中国上市公司像居民一样囤现金。国企不能随便分。地方财政差、公司有钱时，最好是持续分红；差一档是钱进财务公司；再差是被要求收当地资产。央企他觉得干净些，因为钱是财政部的。杠杆：中国是居民和企业在借。美国借钱的是联邦政府，地方政府看起来还好。那边养老金是股票的持续买盘。这边权益相对银行很小，散户占资产和交易都高，没有真正的做空，销售循环是卖产品。那边股票是核心资产，机构拿着，客户付钱给管理人。",
        ],
        "mental_model": {
            "name": "个股方法 × 价格对利润 × 两个循环",
            "components": "书是个股方法。ChatGPT指出的洞是组合和交易。自己的钱能等。外面的钱用AI涨50%、茅台跌10%来考你。把紫金的10倍拆成价格（大约60%–70%）和利润（大约4倍，去掉价格仍有2到2.5倍）。苹果是倍数从十几到三十几，利润大约500亿美元。美国循环在退市、集中、ROE上升，养老金是买盘。中国循环用上市给转型融资，囤现金，居民和企业加杠杆，向散户卖产品。3000本、40元的书是系统，不是利润表。",
            "application": "2899.HK是2019年到现在的档案：10倍，大部分是金属价格，利润残差仍是正的。AAPL是他走的倍数扩张，从增长偏软和净现金到三十几倍。600519.SZ是代理痛苦，跌10个点而AI在涨，不是产品消失的做空。不要因为美国退市更多就去买指数。先问你拿到的是价格、利润，还是倍数。",
        },
        "key_insights": [
            {"view": "这本书比社群赚得少，这没关系。", "question": "为什么写？", "answer": "大约3000本、40元、版税15%–20%，大约1万元。1000元的社群更赚。书逼出系统，ChatGPT才能批评它。"},
            {"view": "把10倍拆开。", "question": "紫金付的是什么？", "answer": "2019年以来股价10倍。利润大约4倍。股价里大约60%–70%是价格。差的六年只看利润，仍大约2到2.5倍。"},
            {"view": "美国在减少上市公司。中国用上市做政策。", "question": "循环差在哪？", "answer": "美股大约7000家减到5000家，一年退市三五百家。标普100的ROE从2011年到2023年上升。中国下降。那边有养老金买盘。这边是散户和现金囤积。"},
        ],
        "golden_quotes": quotes,
        "review_notes": "| v4.10 window 投资实战派 E207",
    })
    write_pair(eid, en, zh)


def ep208():
    eid = "tzs-ep208"
    quotes = ["应该是小于20的", "没腰斩大概也有40的这样的幅度", "茅台的股票跌一半"]
    check(eid, quotes)
    meta = {
        "episode_number": 208,
        "title": "A-Share Swings and the Practice of Value Investing — Yongqing and David with Zhang Jun",
        "guest": "Zhang Jun",
        "guest_role": "Hongshang Asset",
        "date": "2026-11-03",
        "duration_minutes": 88,
        "youtube_url": "",
        "links": {
            "apple_podcasts": APPLE,
            "xiaoyuzhou": "https://www.xiaoyuzhoufm.com/episode/6ae9ac11c96c8942ec16b0af",
        },
    }
    concl = (
        "Third sitting with Zhang Jun of Hongshang Asset, taped October 16. His cumulative "
        "drawdown this year is a personal record, while Shanghai's amplitude looks under 20, "
        "about 4,200 to about 3,600. ChiNext and STAR are about 40% off the late-June high. "
        "Photonics is more than 50% off the peak. Baijiu's worst drop is about 30%. Dividend "
        "low-vol fell about 10 points in a hot June and bounced in July. The 2001 engine, "
        "property plus trade, broke by about 2018. Moutai has halved over five years. Xiaomi "
        "tripled, then placed a huge deal. Nvidia gave back a large rally."
    )
    bg = (
        "E208, published Nov 3, taped Oct 16, about 88 minutes. First tape with Zhang was "
        "Sept 13, 2024, then a fall 2025 sitting. David is in the room. Whisper hears 张郡 and "
        "红上. The show title is 弘尚资产张骏. Not a product recommendation."
    )
    facts = [
        (
            "Index calm, sleeve violence. Zhang's cumulative giveback this year is a record for "
            "him, even if the absolute number is still controlled. The cold fact: Shanghai "
            "Composite amplitude, as he remembers it, is under 20, from a high around 4,200 to "
            "a low around 3,600. ChiNext and STAR are about 40% off the late-June high, not quite "
            "a halving. A photonics sleeve is more than 50% off the peak. Semiconductors swung "
            "hard. The baijiu index's worst drop this year is about 30%. Dividend low-vol, the "
            "index that is supposed to be quiet, had a teens drawdown on the year, fell about 10 "
            "points in June while tech was frantic, and bounced in July as the market fell. He "
            "calls that dividend low-vol turned into dividend high-vol. The push is short-duration "
            "money. This week's drop gets blamed on insurers and fixed-income books hitting "
            "stop-losses. US AI and tech names, on the same tape, kept making highs. The noise "
            "there looks ordinary. A-share old-light names kept falling. Good manufacturers "
            "round-tripped whether or not they were tied to AI."
        ),
        (
            "Do not grant a long duration. His break was 2023. Looking back, the stable stretch "
            "started around 2001: better trade terms outside, a property upcycle inside, household "
            "income and wealth rising, and Western value models imported into that weather. He "
            "dates the break around 2018, when property topped and the US-China relationship "
            "turned. Exports can still be fine. There is no agreed new domestic engine. Households "
            "save because the future is unclear. Firms with access raise money. Firms without it "
            "cut investment and fight on price. A classic value model that assumes a long calm "
            "does not fit a world that will not hand you the duration. Dividend stocks at 6–7% "
            "look fine until earnings drop and the dividend itself is the question. He would add "
            "some dividend weight. He does not treat 6–7% as a promise."
        ),
        (
            "Purchasing power, then the round trip. Over five years Moutai's stock has halved. "
            "The index is still above 3,000. Shanghai housing is better. Edge districts can be "
            "down by half. High-end prices, including liquor, fell. A drinker who did nothing "
            "doubled purchasing power in Moutai. Restaurant purchasing power is up maybe 20–30%. "
            "Daily goods barely rose. The thing that hurts can be the thing that later pays, and "
            "the reverse. Nvidia and Xiaomi are his paired example of a rally that does not "
            "change the market's character: Xiaomi's stock tripled and then came a very large "
            "placement. Nvidia ran up and then gave back a large piece. US AI, he notes, had "
            "already recovered and was breaking highs again. A-shares stay short-bull, long-bear. "
            "He had hoped an AI industrial shift would change that. It has not, much. Li Guofei's "
            "old posts name Ping An, Tencent, and Apple and carry the stamp of that era. Zhang "
            "says some of his own views rhyme with that blog."
        ),
    ]
    mental = {
        "name": "Quiet Index × Short-Duration Money × No New Engine",
        "components": (
            "Shanghai can move less than 20 points from about 4,200 to about 3,600 and still "
            "destroy a concentrated book. STAR and ChiNext about 40% off the June high. Photonics "
            "more than 50%. Baijiu about 30%. Dividend low-vol down about 10 in the hot June and "
            "up in the weak July. Insurers and bond books are the short-duration sellers. The "
            "2001–2018 engine was trade plus property. After that, households save and firms "
            "either raise or shrink. A 6–7% dividend is not a duration. Moutai halved and the "
            "drinker's purchasing power doubled. Xiaomi's triple ended in a huge placement. "
            "Nvidia's rally gave a large piece back and the US tape was at highs again. A-share "
            "AI labels did not turn the bull short and the bear long."
        ),
        "application": (
            "600519.SZ is the five-year halving that raised a drinker's purchasing power. NVDA is "
            "the US AI name that gave back and then made highs again. 1810.HK is the triple plus "
            "a huge placement, the A-share version of a rally that finances itself. Do not read a "
            "sub-20 Shanghai amplitude as a quiet book. Underwrite sleeve drawdowns and how short "
            "the money is."
        ),
    }
    insights = [
        {
            "view": "The index got quieter. The sleeves did not.",
            "question": "What is the cold fact?",
            "answer": "Shanghai amplitude under 20, about 4,200 to about 3,600. ChiNext and STAR about 40% off the late-June high. Photonics more than 50%. Baijiu about 30%. Dividend low-vol fell about 10 points in June.",
        },
        {
            "view": "The long calm ended around 2018.",
            "question": "What was the engine?",
            "answer": "From about 2001, trade terms plus a property upcycle. Property topped and the US-China relationship turned. No replacement engine, so households save and firms raise or cut.",
        },
        {
            "view": "A halving can be a purchasing-power gain.",
            "question": "What happened to Moutai?",
            "answer": "The stock halved over five years. A regular drinker doubled purchasing power. Xiaomi tripled and placed stock. Nvidia gave back a large rally and US AI was at highs again.",
        },
    ]
    invest = [
        {"ticker": "600519.SZ", "direction": "Long", "confidence": "Low", "thesis": "Stock halved over five years while a regular drinker doubled purchasing power — low"},
        {"ticker": "NVDA", "direction": "Long", "confidence": "Low", "thesis": "Large giveback after the rally, then US AI names back at highs — the contrast to A-share round trips — low"},
        {"ticker": "1810.HK", "direction": "Long", "confidence": "Low", "thesis": "Tripled, then a very large placement; the A-share rally that finances itself — low"},
    ]
    chrono = {
        "subject": "Zhang Jun · A-share amplitude · 2018 break",
        "events": [
            {"date": "2001", "event": "Trade-terms plus property upcycle begins, in his dating"},
            {"date": "~2018", "event": "Property tops; US-China relationship turns; long duration ends"},
            {"date": "2023", "event": "Personal investment break; the reflection starts"},
            {"date": "2024-09-13", "event": "First sitting with Yongqing"},
            {"date": "2025-09", "event": "Second sitting"},
            {"date": "2026-06", "event": "STAR/ChiNext high; later ~40% drawdown; dividend low-vol -10 in the hot month"},
            {"date": "2026-10-16", "event": "Third sitting, Shanghai ~4200 to ~3600 on the year"},
            {"date": "2026-11-03", "event": "E208 publishes"},
        ],
    }
    en = en_std(
        eid, "Practical Investments", "Yongqing & David", meta, 3,
        ["600519.SZ", "NVDA", "1810.HK"],
        concl, bg, facts, mental, insights, invest, quotes, chrono,
        "| v4.10 window TZS E208", "whisper-small",
    )
    zh_meta = dict(meta)
    zh_meta.update(
        title="E208 A股又是大震荡，价值投资的实践、挑战和思考 | 永庆、David 对谈弘尚资产张骏",
        guest="张骏",
        guest_role="弘尚资产",
    )
    zh = dict(en)
    zh.update({
        "podcast": "投资实战派",
        "host": "永庆 & David",
        "metadata": zh_meta,
        "conclusion": (
            "弘尚资产张骏第三次来，10月16日录。他今年的累计回撤是个人纪录，同时记得上证振幅不到20，"
            "大约从4200点到3600点。狠的是切片：创业板和科创板从6月底高点下来大约40%，光模块一类从顶点超过50%，"
            "白酒指数最差大约30%。红利低波在6月科技最热时单月跌大约10个点，7月市场跌时又弹回去。"
            "钱的久期很短。2001年开始的引擎是贸易加地产，大约2018年停了。茅台股价五年跌一半，喝酒的人购买力翻倍。"
            "小米涨了三倍然后有一笔超大定增。英伟达涨上去又回吐一大块。美股AI当时已经回到新高。"
        ),
        "background": (
            "E208，11月3日发布，10月16日录，大约88分钟。第一次是2024年9月13日，2025年秋天又坐过一次。David在场。"
            "Whisper听成张郡、红上。节目标题是弘尚资产张骏。不是产品推荐。"
        ),
        "important_facts": [
            "指数安静，板块很狠。张骏说今年累计回撤是自己的纪录，绝对数仍然控得住。冷知识：他印象里上证振幅小于20，高点大约4200，低点大约3600。创业板和科创板从6月底高点下来大约40%，没到腰斩。光模块一类从顶点超过50%。半导体波动也大。白酒指数今年最大跌幅大约30%出头。红利低波本该安静，年内最大回撤有十几，6月科技疯狂时单月跌大约10个点，7月市场跌时又弹回去。他把这叫红利低波做成了红利高波。推动力是短久期的钱。这一周的下跌被归到保险和固收止损。同一条带子上，美股AI和科技还在创新高，扰动看起来普通。A股老灯还在跌。好的制造业公司涨完又跌，跟不跟AI关系不大。",
            "不要再给长久期。他的坎在2023年。回头看，稳定段大约从2001年开始：外面贸易条件变好，里面地产向上，居民收入和财富往上，西方价值模型是在那种天气里套进来的。断点他放在大约2018年，地产到头，中美关系转向。出口还可以。国内没有公认的新引擎。居民因为不确定而存钱。有资源的企业去融资。没有资源的就收缩投资、打价格。经典价值模型假设一段长的平静，而这世界不再给你久期。红利股6到7个点看起来不错，业绩掉下去，股息本身就成了问题。他愿意加一点红利权重。他不把6%–7%当成承诺。",
            "购买力，然后是来回。五年里茅台股价跌一半。指数还在3000点以上。上海房子好一些。边缘可以跌一半。高端价格包括酒在跌。什么都没做、平时喝茅台的人，购买力翻倍。下馆子的购买力也许提高20%–30%。日用品基本没涨。让你难受的东西以后可能让你赚钱，反过来也一样。英伟达和小米是他配的一对：涨完并不改变市场性格。小米股价涨了三倍，然后一笔超大定增。英伟达涨上去，又回吐一大块。美股AI他指出已经收回来并突破新高。A股仍是牛短熊长。他曾希望AI产业革命改掉这一点。改动不大。李国飞旧文里的平安、腾讯、苹果带着那个时代的印。张骏说自己有些看法和那博客同韵。",
        ],
        "mental_model": {
            "name": "安静的指数 × 短久期的钱 × 没有新引擎",
            "components": "上证可以从大约4200到3600、振幅不到20，仍然毁掉一个集中的组合。科创和创业板离6月高点大约40%。光模块超过50%。白酒大约30%。红利低波在热的6月跌大约10个点，在弱的7月上涨。保险和债券盘是短久期的卖方。2001到2018的引擎是贸易加地产。之后居民存钱，企业要么融资要么收缩。6%–7%的股息不是久期。茅台跌一半，喝酒的人购买力翻倍。小米的三倍结束于超大定增。英伟达的上涨回吐一大块，美股又在高点。A股的AI标签没有把牛短熊长反过来。",
            "application": "600519.SZ是五年跌半、喝酒的人购买力上升。NVDA是回吐之后美股AI又创新高的对照。1810.HK是三倍加超大定增，A股版的上涨给自己融资。不要把上证振幅不到20读成组合也安静。先看切片回撤，以及钱有多短。",
        },
        "key_insights": [
            {"view": "指数更安静了。切片没有。", "question": "冷知识是什么？", "answer": "上证振幅不到20，大约4200到3600。创业板和科创板离6月底高点大约40%。光模块超过50%。白酒大约30%。红利低波在6月跌了大约10个点。"},
            {"view": "长的平静大约在2018年结束。", "question": "引擎是什么？", "answer": "大约从2001年起，贸易条件加地产向上。地产到头，中美关系转向。没有替代引擎，所以居民存钱，企业融资或收缩。"},
            {"view": "跌一半可以是购买力上升。", "question": "茅台发生了什么？", "answer": "股价五年跌一半。常喝的人购买力翻倍。小米涨三倍然后定增。英伟达把一大段涨幅回吐，美股AI又在新高。"},
        ],
        "golden_quotes": quotes,
        "review_notes": "| v4.10 window 投资实战派 E208",
    })
    write_pair(eid, en, zh)


def main():
    ep207()
    ep208()


if __name__ == "__main__":
    main()
