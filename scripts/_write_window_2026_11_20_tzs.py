#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Bilingual TZS E209 and E211."""
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


def pair(eid, en, zh):
    dump(ROOT / f"data/approved/{eid}.json", en)
    dump(ROOT / f"data/approved/zh/{eid}.json", zh)
    validate_file(ROOT / f"data/approved/{eid}.json")


def ep209():
    eid = "tzs-ep209"
    quotes = ["成立于1931年", "2000万美元左右", "1.5万亿美元"]
    check(eid, quotes)
    meta = {
        "episode_number": 209,
        "title": "How to Recognize a Good Investment Firm — Capital Group with Fan Enjie",
        "guest": "Fan Enjie",
        "guest_role": "Founder, Smart Investor · translator, The Long Game",
        "date": "2026-11-08",
        "duration_minutes": 115,
        "youtube_url": "",
        "links": {
            "apple_podcasts": APPLE,
            "xiaoyuzhou": "https://www.xiaoyuzhoufm.com/episode/6af034beb4a4e20202f686d8",
        },
    }
    concl = (
        "Fan Enjie spent five years as a fund reporter from 2002, nine years inside a "
        "mutual fund through 2015, then built Smart Investor. In 2018 he interviewed "
        "70 to 80 people for the industry's twenty-year book. Capital Group, founded "
        "in 1931, stayed near $20 million for about twenty years and was a $1.5 trillion "
        "growth complex by 2015. Own money can hold Moutai as a deposit substitute. An "
        "institution that needs 10-15% cannot copy Duan Yongping's Moutai. One manager "
        "went to cash at Sputnik. Jon Lovelace answered with multiple managers, and in "
        "1974 they still sold stocks."
    )
    # I'll trim if over 100 after the run. Keep a shorter one if needed.
    bg = (
        "E209, published Nov 8, taped Sept 17, about 115 minutes. The book is the "
        "ninety-year Capital Group history he translated, set next to his China fund "
        "reporting. Whisper hears 长线自胜 and 公务基金. Not a product recommendation."
    )
    facts = [
        (
            "The observer. Fan started in 2002 as a securities and fund reporter and stayed "
            "five years. He then spent nine years at a mutual-fund company and left at the "
            "end of 2015 to start Smart Investor, a content shop with a public account, an "
            "app, and a site. In 2018, the twentieth year of the formal public-fund industry, "
            "the securities association asked for a book. He interviewed about 70 to 80 people: "
            "regulators, founding partners, famous public managers, and people who had already "
            "gone private. He calls that book a stereo history of policy, behavior, and the "
            "market. The Capital Group translation is the foreign file next to that domestic "
            "reporting. He had already followed the firm for more than twenty years. A "
            "colleague in 2015 told him the growth complex was about $1.5 trillion, and that "
            "the firm founded in 1931 had been only about $20 million for nearly twenty years. "
            "Ninety years is the point of the book. The details are a textbook because the "
            "market changes and the management problem does not."
        ),
        (
            "Own money versus other people's money. A professional with his own capital and "
            "no leverage can actually be long-term. Duan Yongping playing golf is hard to "
            "copy. Duan can hold Moutai as a substitute for bank interest. An institution "
            "that needs 10-15%, sometimes said as 20%, on the whole portfolio cannot use "
            "that asset in that role. The manager is dancing in shackles. The client may "
            "not accept three or four rough years on the way to the target. So the "
            "institution has to underwrite the liability, the holding period, and the "
            "path, not only the asset. A personal account that puts 5% into something "
            "Duan would size as a core holding is not the same decision. Pop Mart is the "
            "same lesson: personal money can hold a view the fund's clients will not fund "
            "through the drawdown."
        ),
        (
            "Why one manager is not an institution. A polite senior who lets everyone talk "
            "and then splits the difference produced mediocre results, because nobody really "
            "believed the compromise. A single-manager shop failed the other way. Around "
            "Sputnik, the growth portfolio, Hall on the tape, went to cash. Lovelace stayed "
            "with Eisenhower and stayed in stocks, so the growth fund became the conservative "
            "one and the conservative fund became the aggressive one. One person will be "
            "wrong across a long career. A firm that wants to last cannot bet that one "
            "person stays right. The third path was multiple managers. The idea was Jon "
            "Lovelace, the founder's son and the second-generation head, not the founder. "
            "In the 1970s they faced another client-first test. Peers launched money-market "
            "funds. By 1974 the stock market was already crushed, and a sales team would "
            "have loved a cash product. Jon said pushing cash was wrong. If they were "
            "active stock investors, they should be selling stocks. That is the "
            "institutional tell Fan wants: the product follows the belief, not the easy "
            "channel, and no single temperament owns the whole book."
        ),
    ]
    mental = {
        "name": "Liability First × Multiple Managers × Ninety Years",
        "components": (
            "Personal capital can be a deposit substitute. Institutional capital has a "
            "10-15% portfolio target and clients who will not sit through three or four "
            "bad years. A committee that only compromises is mediocre. One manager will "
            "invert his own style in a panic, as the growth book did at Sputnik. Multiple "
            "managers, Jon Lovelace's design, stop one error from being the firm. In "
            "1973-74 they would not hide in money-market funds. The firm itself was about "
            "$20 million for twenty years after 1931 and about $1.5 trillion in the growth "
            "complex by 2015. Fan followed them for more than twenty years before the "
            "translation. That gap is the tell. Time is the asset of the institution, not a star year."
        ),
        "application": (
            "Private:Capital Group is the case, not a tradable stock. 600519.SZ is the "
            "deposit-substitute holding an institution with a 10-15% target should not "
            "pretend to copy. 9992.HK is the personal-money position the same way. "
            "Judge a firm by whether one temperament can sink the book, and by what it "
            "sold in 1974, not by whether the manager looks busy."
        ),
    }
    insights = [
        {"view": "Twenty years at $20 million is the start of the story.", "question": "What was Capital Group in 1931?", "answer": "Founded that year, still about $20 million two decades later. The growth complex he was shown in 2015 was about $1.5 trillion."},
        {"view": "Other people's money cannot copy a personal account.", "question": "Why is Duan's Moutai hard to learn?", "answer": "For him it replaces bank interest. A fund that needs 10-15% on the portfolio, with clients who hate a three or four year drawdown, is dancing in shackles."},
        {"view": "One manager will be wrong. The firm should not be.", "question": "What did Sputnik teach them?", "answer": "The growth book went to cash and the conservative book stayed in. Jon Lovelace, the son, built multiple managers so one panic is not the firm. In 1974 they still sold stocks, not money funds."},
    ]
    invest = [
        {"ticker": "Private:Capital Group", "direction": "Long", "confidence": "Low", "thesis": "1931 start, about $20 million for twenty years, $1.5 trillion growth complex by 2015, multiple managers after Sputnik — low"},
        {"ticker": "600519.SZ", "direction": "Long", "confidence": "Low", "thesis": "A deposit substitute for personal capital, not a 10-15% institutional hurdle — low"},
        {"ticker": "9992.HK", "direction": "Long", "confidence": "Low", "thesis": "A personal-money position clients of a fund will not finance through the drawdown — low"},
    ]
    chrono = {"subject": "Fan Enjie · Capital Group · multiple managers", "events": [
        {"date": "1931", "event": "Capital Group founded; about $20 million for nearly 20 years"},
        {"date": "1957", "event": "Sputnik: growth book to cash, Lovelace stays in stocks"},
        {"date": "1973-74", "event": "Jon Lovelace refuses the money-market push and sells stocks"},
        {"date": "2002-15", "event": "Fan: five years reporting, nine years at a fund, leaves end-2015"},
        {"date": "2015", "event": "Growth complex cited near $1.5 trillion"},
        {"date": "2018", "event": "70-80 interviews for the twenty-year public-fund book"},
        {"date": "2026-09-17", "event": "Taping"},
        {"date": "2026-11-08", "event": "E209 publishes"},
    ]}
    en = en_std(eid, "Practical Investments", "Yongqing & David", meta, 3,
                ["Private:Capital Group", "600519.SZ", "9992.HK"],
                concl, bg, facts, mental, insights, invest, quotes, chrono,
                "| v4.10 window TZS E209", "whisper-small")
    zh_meta = dict(meta)
    zh_meta.update(
        title="E209 如何识别好的投资机构？美国资本集团百年实践｜永庆对话《长线制胜》译者范恩洁",
        guest="范恩洁",
        guest_role="聪明投资者创始人 · 《长线制胜》译者",
    )
    zh = dict(en)
    zh.update({
        "podcast": "投资实战派", "host": "永庆 & David", "metadata": zh_meta,
        "conclusion": "范恩洁2002年起做了五年基金报道，又在公募待了九年，2015年底出来做聪明投资者。2018年为基金业二十年书写过大约70到80个人。资本集团1931年成立，大约二十年规模还在2000万美元附近，2015年他听到的成长组合大约1.5万亿美元。自己的钱可以把茅台当存款替代。机构要组合10%到15%，持有人受不了三四年颠簸，就学不了段永平。只做妥协的委员会结果平庸。卫星上天时一个经理换成现金，另一个留在股票里，风格对调。乔恩·洛夫莱斯的答案是多基金经理。1973到1974年他们拒绝推货币基金，继续卖股票。",
        "background": "E209，11月8日发布，9月17日录，大约115分钟。一本是他翻译的资本集团九十年，一本是他对中国基金业的采访。Whisper把《长线制胜》听成长线自胜，把公募听成公务。不是产品推荐。",
        "important_facts": [
            "观察者。范2002年做证券基金报道，五年。然后在一家公募待了九年，2015年底离开，创办聪明投资者，有公众号、App和官网。2018年公募规范成立二十年，协会要写一本书。他采访了大约70到80人：监管、创始元老、著名基金经理，以及已经去私募的人。他说那本书把政策、行为和市场叠成立体史。资本集团的译本是旁边的海外档案。他跟踪这家机构已经二十多年。2015年有人告诉他，成长组合大约1.5万亿美元，而1931年成立的公司有将近二十年规模只有大约2000万美元。九十年是这本书的重点。市场会变，管人的问题不变。",
            "自己的钱和别人的钱。有能力圈、不加杠杆的个人可以真的长期。段永平打高尔夫很难学。他可以把茅台当成银行存款利息的替代。机构如果整体组合要10%到15%，有时说到20%，就不能把这个资产放在那个角色里。管理人是带着镣铐跳舞。持有人往往受不了三四年的颠簸。所以机构要看负债、持有期和路径，不只看资产。个人账户买5%，和段永平当成核心持仓，不是同一个决定。泡泡玛特是同一课：个人的钱可以拿一个观点，基金的客户不会为回撤付钱。",
            "为什么一个经理不是一家机构。一位脾气好的老人让所有人发言，再取中间，结果平庸，因为没有人真的相信那个妥协。单一经理是另一种失败。卫星上天前后，带子上的成长组合经理霍尔换成了现金。老洛夫莱斯站在艾森豪威尔一边，股票仓位很高。成长基金变保守，稳健基金变激进。一个人的职业生涯一定会错。想活很久的组织不能押一个人持续正确。第三条路是多基金经理。这个设计来自创始人的儿子、第二代掌门乔恩·洛夫莱斯，不是创始人本人。1970年代还有一次从客户出发的考试。同行推货币基金。1974年股市已经跌狠了，销售会喜欢现金产品。乔恩说推货币是错的。如果他们是主动的股票投资者，就应该卖股票。范要的机构标志是：产品跟着信仰，不跟着好卖的渠道，而且没有一种脾气拥有整本书。",
        ],
        "mental_model": {
            "name": "先看负债 × 多基金经理 × 九十年",
            "components": "个人资本可以是存款替代。机构资本要10%到15%，客户受不了三四年差年份。只做妥协的委员会是平庸。一个经理会在恐慌里把自己的风格反过来，卫星上天时成长组合就是这样。多基金经理是乔恩·洛夫莱斯的设计，让一次错误不等于这家公司。1973到1974年他们不躲进货币基金。公司1931年后大约二十年只有2000万美元，2015年成长组合大约1.5万亿美元。时间是机构的资产，不是一个明星年份。",
            "application": "Private:Capital Group是这个案例，不是上市股票。600519.SZ是存款替代，要10%到15%的机构不该假装在抄。9992.HK同样是个人的钱。判断一家机构，看一种脾气能不能毁掉整本书，以及1974年它在卖什么，不要看经理忙不忙。",
        },
        "key_insights": [
            {"view": "两千万美元的二十年才是开头。", "question": "1931年的资本集团是什么？", "answer": "那年成立，大约二十年后仍在2000万美元附近。2015年他看到的成长组合大约1.5万亿美元。"},
            {"view": "别人的钱抄不了个人账户。", "question": "段永平的茅台为什么难学？", "answer": "对他来说这是存款利息的替代。基金要组合10%到15%，客户又受不了三四年回撤，就是带着镣铐跳舞。"},
            {"view": "一个人会错。机构不该跟着错。", "question": "卫星教了他们什么？", "answer": "成长组合换成现金，稳健组合留在股票里。乔恩·洛夫莱斯做成多基金经理。1974年他们卖的仍是股票，不是货币基金。"},
        ],
        "golden_quotes": quotes,
        "review_notes": "| v4.10 window 投资实战派 E209",
    })
    pair(eid, en, zh)


def ep211():
    eid = "tzs-ep211"
    quotes = ["只有有竞争优势的公司才能够去做预判", "从格雷厄姆到巴菲特", "被讨厌的勇气"]
    check(eid, quotes)
    meta = {
        "episode_number": 211,
        "title": "A Bad Tape Is for Reading — Yongqing's Value-Investing Shelf, with Sam",
        "guest": "Yongqing",
        "guest_role": "Host, on the books, with Sam as stand-in",
        "date": "2026-11-18",
        "duration_minutes": 78,
        "youtube_url": "",
        "links": {
            "apple_podcasts": APPLE,
            "xiaoyuzhou": "https://www.xiaoyuzhoufm.com/episode/6afda919a4a79edf137b529b",
        },
    }
    concl = (
        "Sam hosts after a Shanghai podcast-festival book panel. Yongqing's shared shelf, "
        "if he may name only three, is three Columbia value courses. Greenwald's "
        "Competition Demystified is the business test: without an advantage you cannot "
        "forecast, because the company cannot forecast itself. Value Investing from "
        "Graham to Buffett is the valuation test: assets, earnings, and growth. The "
        "analyst's advanced guide is how you write the case for a boss, a client, or "
            "yourself. Value meant quality in 2019, PDD and Li Auto in 2021, and dividends "
            "now. Courage to Be Disliked covers wanting 12 times and printing 10."
    )
    bg = (
        "E211, published Nov 18, taped Oct 26, about 78 minutes. Yongqing is the guest "
        "and Sam is the stand-in host. The prompt was a book session the day before, "
        "and a weak tape that is a better time to read than to trade. He started in PE "
        "in 2016, minority stakes, then a Hong Kong hedge fund."
    )
    facts = [
        (
            "Three books, one course. If a beginner and a professional have to share a "
                "shelf, Yongqing names 3 books by Columbia value teachers. First, Bruce "
            "Greenwald, Competition Demystified, the red-covered Chinese edition "
            "translated by Lin Anji and Fan Shuai. He has already recorded with Fan on "
            "this show. The book is how you tell whether a company has an advantage. "
            "Only then can you forecast. Without an advantage, the people inside the "
            "company cannot forecast either, because the world is too mixed. Second, "
            "Value Investing from Graham to Buffett, now in a second Chinese edition. "
            "It is the valuation shelf: asset, earnings, and growth. Third, the "
            "advanced guide for the securities analyst, retitled in Chinese. It is how "
            "you lay out the case for a boss, a client, or yourself, including the "
                "market and the multiple. Together they are business, value, and the memo. "
                "A good source points at a better source."
        ),
        (
            "What value meant in each year. He graduated in 2016 into private equity, "
            "domestic deals, placements and negotiated transfers, aiming to be an active "
            "holder around 10% and not a silent minor shareholder. Then a Hong Kong "
            "hedge fund. Himalaya Capital's Chang Jing lectured on value. From 2016 to "
            "2019 the rooms were offline, then online, and in 2023 he moved to Shanghai "
            "for family. In 2024 he sat in on Gui Jiang's value course and did it again "
            "in 2026. Early practice was growth, with large swings. He came out wanting "
            "high-quality companies. The label moved without anyone drawing the map. In "
            "2019, value meant quality. In 2021 it meant hyper-growth: Pinduoduo, the "
            "EV names including Li Auto, and new energy. Now the same words mean "
            "dividends, certainty, and a high payout. Ten years of practice is what "
            "made the split visible. The idea is easy. The strategy the market is "
            "discussing is not stable."
        ),
        (
            "Nerve, and other people's memos. After a drop he wants readers to be "
            "careful people, not louder people. Two books. The Courage to Be Disliked "
            "is the one whose title makes you quit, and the one he has kept for years. "
            "The investor trap is: I know this company, it should be 12 times, it is "
            "10 times, the market is stupid. The book separates what you can do from "
            "the outside causes you cannot. That matches an inside scorecard. Liking "
            "a company does not obligate the price to agree. The second book is Li "
            "Guofei, Jobs, Zen, and Value Investing. Years ago it felt vague. Now he "
            "reads the psychology as the engine: resentment, invention, and actually "
            "wanting the problem solved are why someone spends the hours. He also "
            "says stock picking is not a place for novelty. If he wants an oil stock "
            "he rereads how Buffett bought PetroChina and Occidental. If he wants a "
                "cycle he stacks how the known buyers, including Deng Xiaofeng in gold, "
                "did that asset. The file is sorted memos from other investors, not a new theory."
        ),
    ]
    mental = {
        "name": "Three Columbia Books × A Moving Word × An Inside Scorecard",
        "components": (
            "Advantage first, or there is nothing to forecast. Then three ways to value: "
            "assets, earnings, growth. Then a memo a boss or a client can use. The word "
            "value meant quality in 2019, PDD and Li Auto in 2021, and dividends now. "
            "A 12 times business at 10 times is not a stupid market. The Courage to Be "
            "Disliked is the separation of what you control. Li Guofei is the claim that "
            "psychology is the engine. Oil and cycles are studied by rereading Buffett "
            "and Deng, not by inventing a method."
        ),
        "application": (
            "PDD and LI are the 2021 meaning of value on this tape, not a current buy. "
            "OXY is the Occidental file he would reread before buying an oil stock. "
            "Do not treat a course list as a portfolio. The work is to have read the "
            "3 Columbia books and to know which year of that definition you are using."
        ),
    }
    insights = [
        {"view": "No advantage, no forecast.", "question": "Why is Greenwald first?", "answer": "Only a company with an advantage can be forecast, because otherwise the people inside it cannot forecast either. The book is the business test."},
        {"view": "Value is a word that changed jobs.", "question": "What did the market mean?", "answer": "2019 was quality. 2021 was Pinduoduo, Li Auto, and new energy. Now it is dividends and certainty. The idea did not move. The strategy being discussed did."},
        {"view": "Ten times is not an insult.", "question": "What is the nerve book for?", "answer": "The Courage to Be Disliked. Knowing a company and wanting 12 times when it prints 10 is the trap. You do not control the outside cause."},
    ]
    invest = [
        {"ticker": "PDD", "direction": "Long", "confidence": "Low", "thesis": "The 2021 meaning of value on this tape, hyper-growth, not the dividend definition he hears now — low"},
        {"ticker": "LI", "direction": "Long", "confidence": "Low", "thesis": "Named with Pinduoduo as the EV growth the market called value in 2021 — low"},
        {"ticker": "OXY", "direction": "Long", "confidence": "Low", "thesis": "The Occidental file he would reread, next to PetroChina, before buying an oil stock — low"},
    ]
    chrono = {"subject": "Yongqing · three books · what value meant", "events": [
        {"date": "2016", "event": "PE after the master's, active minority stakes around 10%"},
        {"date": "2016-19", "event": "Chang Jing and offline value rooms; then growth-stock swings"},
        {"date": "2019", "event": "Value, in the market's mouth, means quality"},
        {"date": "2021", "event": "The same word means PDD, Li Auto, new energy"},
        {"date": "2024-26", "event": "Gui Jiang's course; dividends are the new default"},
        {"date": "2026-10-26", "event": "Taping, the day after the Shanghai book panel"},
        {"date": "2026-11-18", "event": "E211 publishes"},
    ]}
    en = en_std(eid, "Practical Investments", "Yongqing & David", meta, 3,
                ["PDD", "LI", "OXY"],
                concl, bg, facts, mental, insights, invest, quotes, chrono,
                "| v4.10 window TZS E211", "whisper-small")
    zh_meta = dict(meta)
    zh_meta.update(
        title="E211 行情不好多读书，投资精选书单推荐 | 永庆与 Sam 聊读书",
        guest="永庆",
        guest_role="主播，Sam 代班主持",
    )
    zh = dict(en)
    zh.update({
        "podcast": "投资实战派", "host": "永庆 & David", "metadata": zh_meta,
        "conclusion": "播客节书单的第二天，Sam代班，永庆来讲书。如果只能留三本，都是哥大价值投资课老师写的。格林沃尔德《竞争优势》是业务考试：没有优势就不能预判，因为公司自己也无法预判。第二本《价值投资：从格雷厄姆到巴菲特》是估值：资产、利润、成长。第三本《证券分析师进阶指南》是怎么给老板、客户或自己写出要点。市场嘴里的价值在换工作：2019年是高质量，2021年是拼多多、理想和新能源，现在是红利。心力两本是《被讨厌的勇气》和李国飞讲乔布斯与价值投资。公司该12倍、现在10倍，不是市场傻。",
        "background": "E211，11月18日发布，10月26日录，大约78分钟。永庆是嘉宾，Sam代班主持。前一天是上海播客节的书单场，行情不好，更适合读书。他2016年进PE做少数股权，后来去香港对冲基金。",
        "important_facts": [
            "三本书，一门课。小白和业内要共用一个架子，永庆点三本哥大价值课老师的书。第一本格林沃尔德《竞争优势》，红色封面，林安霁和樊帅译。他跟樊帅在实战派录过。这本书是判断公司有没有优势。有了才能预判。没有优势，公司里的人也无法预判，因为世界太混。第二本《价值投资：从格雷厄姆到巴菲特》，中文第二版。估值分三类：资产、利润、成长。第三本中文名叫《证券分析师进阶指南》，原名被改过。它讲怎么给老板、客户或自己理出框架，包括市场和倍数。三本合起来是业务、估值和备忘录。他说很多推荐书单其实没人读完。好的信息源会指向更好的信息源。耶鲁之类的课单是找下一本书的办法，不是奖杯。",
            "价值这个词每年换工作。他2016年硕士毕业进PE，做国内定增和协议转让，想做大约10%以内的积极股东，而不是沉默小股东。然后去香港对冲基金。喜马拉雅资本常劲讲过价值。2016到2019年线下，后来线上。2023年因家庭到上海。2024年旁听归江的价值课，2026年又听。早期实践是成长股，波动很大，后来要高质量公司。没有人把地图画清楚。2019年价值默认是高质量。2021年默认是超级成长：拼多多、理想汽车和其他新能源。现在同样两个字的意思是红利、确定性和高股息。十年实践才看见这个分裂。理念好懂。市场正在讨论的策略不稳定。",
            "心力和别人的备忘录。跌完之后他希望读者成为有心力的人，不是更大声的人。两本书。《被讨厌的勇气》书名让人想放弃，他几年前看过，一直留着。投资者的陷阱是：我了解这家公司，它该12倍，现在10倍，市场傻。书把你能做的事和你控制不了的外因分开。这和内部记分卡是一回事。你喜欢一家公司，价格没有义务同意。第二本是李国飞《乔布斯禅与价值投资》。几年前觉得虚。现在他把心理读成发动机：怨、创新、以及真的想解决问题，才是一个人肯花时间的原因。他还说选股不是创新的地方。想买石油股，就重读巴菲特怎么买中石油和西方石油。想买周期，就把邓晓峰买黄金这类已知买方的框架叠起来。档案是别人的备忘录，整理过，不是一套新理论。",
        ],
        "mental_model": {
            "name": "三本哥大书 × 一个在搬家的词 × 内部记分卡",
            "components": "先看优势，否则没有东西可预判。然后三种估值：资产、利润、成长。然后一份老板或客户能用的备忘录。价值在2019年指质量，2021年指拼多多和理想，现在指红利。12倍的公司印在10倍，不是市场傻。《被讨厌的勇气》是把你能控制的分开。李国飞的书是说心理才是发动机。石油和周期靠重读巴菲特和邓晓峰，不靠发明方法。",
            "application": "PDD和LI是这期带子上2021年价值的意思，不是现在的买入。OXY是买石油股之前要重读的西方石油档案。不要把课单当成组合。工作是读完那三本哥大书，并且知道你用的是哪一年的定义。",
        },
        "key_insights": [
            {"view": "没有优势，就没有预判。", "question": "为什么格林沃尔德排第一？", "answer": "只有有竞争优势的公司才能预判，否则公司里的人也无法预判。这本书是业务考试。"},
            {"view": "价值是一个换过工作的词。", "question": "市场当时指什么？", "answer": "2019年是质量。2021年是拼多多、理想和新能源。现在是红利和确定性。理念没动。被讨论的策略动了。"},
            {"view": "十倍不是侮辱。", "question": "心力那本书做什么？", "answer": "《被讨厌的勇气》。你了解公司，想要12倍，它印在10倍，这就是陷阱。外因不由你控制。"},
        ],
        "golden_quotes": quotes,
        "review_notes": "| v4.10 window 投资实战派 E211",
    })
    pair(eid, en, zh)


if __name__ == "__main__":
    ep209()
    ep211()
