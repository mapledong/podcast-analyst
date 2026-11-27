#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Bilingual TZS E212."""
from __future__ import annotations

import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))
from scripts._window_lib import dump, en_std, validate_file  # noqa: E402
from src.chinese_transcript import load_transcript_body, quote_supported_in_transcript, transcript_path  # noqa: E402

APPLE = "https://podcasts.apple.com/cn/podcast/id1718660227"
XYZ = "https://www.xiaoyuzhoufm.com/episode/6b0424fe4ecad672d4105bb9"


def check(eid, quotes):
    body = load_transcript_body(transcript_path(eid))
    for q in quotes:
        ok = quote_supported_in_transcript(q, body)
        print(eid, "OK" if ok else "FAIL", q)
        if not ok:
            raise SystemExit(q)


def main():
    eid = "tzs-ep212"
    quotes = ["现在大概不到14倍", "最大的价值陷阱有万科", "我是科技信仰者"]
    check(eid, quotes)
    meta = {
        "episode_number": 212,
        "title": "Steady Is Fast — Liang Yufeng on Allocation After the Drawdown",
        "guest": "Liang Yufeng",
        "guest_role": "Author, Steady Is Fast",
        "date": "2026-11-23",
        "duration_minutes": 77,
        "youtube_url": "",
        "links": {"apple_podcasts": APPLE, "xiaoyuzhou": XYZ},
    }
    concl = (
        "After the October drawdown, Liang Yufeng walks through Steady Is Fast. "
        "CSI 300 is under 14 times, an earnings yield near 7.5 percent, and ROE "
        "near 11 to 12 percent on a 1.4 price to book. Deposits are about 1 percent. "
        "Credit bonds are about 2 to 3 percent. He wants a pyramid: more equity when "
        "cheap, less if Shanghai reaches 5,000 or 6,000. Vanke in late 2020 was his "
        "largest value trap. A 30 percent optical-module margin without a deep moat "
        "is a profit he expects rivals to attack."
    )
    bg = (
        "E212, published Nov 23, taped Oct 20, about 77 minutes. David hosts Liang "
        "Yufeng, in securities since 1998, more than ten years running research at "
        "Orient Securities, and out on his own in 2014. The new book has a preface "
        "from Liu Jipeng. Whisper hears the title as a jumble and the name as Liang "
        "Yunfen. Six steadies: allocation, name, action, portfolio, risk, temperament. "
        "Not a product pitch. A signed-copy giveaway closes the open."
    )
    facts = [
        (
            "The equity case is an earnings yield. CSI 300 is under 14 times, so the "
            "inverse is about 7.5 percent. He sets aside this year growth, which he "
            "puts near 20 percent, and still gets a 7 to 8 percent potential return. "
            "ROE is about 11 to 12 percent, down from about 20 percent at the peak, "
            "when it sat near the S&P 500. Bank ROE went from about 20 percent to "
            "about 10 percent. Price to book is about 1.4, and 11 to 12 divided by "
            "1.4 is again 7 to 8 percent. Deposits are about 1 percent. Government "
            "bonds are about 1.6 to 1.7 percent. Credit bonds are about 2 to 3 percent. "
            "Shanghai rental yield is 1 to 2 points. The old 10-point property capital "
            "gain is what buyers no longer expect. A 60 percent equity and 40 percent "
            "bond mix, he says, beat many complicated models in one paper he read."
        ),
        (
            "A cheap name can still destroy value. His largest value trap was Vanke, "
            "looked at in late 2020 or early 2021, while the bubble was still intact "
            "and both quality and the multiple looked fine. From 2022 the industry "
            "destroyed value. He keeps the miss small: Vanke was about 3 to 5 percent "
            "of the book. Banks are the contrast. If in 2021 someone said sales area "
            "would fall 70 to 80 percent and prices 30 to 40 percent, he says 99 percent "
            "of people would not believe it, and would conclude the economy and the "
            "banks were finished. Five or six years later the drop happened. Big banks "
            "have earnings pressure, not a liquidity break. Exposure was smaller than "
            "imagined because policy had already kept banks off developer credit, which "
            "is why shadow banking grew. From the June 30 high, some public funds he "
            "watches are down more than 40 percent. His simulated balanced books are "
            "down under 10 points."
        ),
        (
            "A 30 percent margin in a shallow moat is an invitation. Optical modules "
            "sit between strong suppliers and strong customers. Shortage lets that "
            "link earn about 30 percent, while 10 percent is already a good Chinese "
            "manufacturing margin and many plants earn 4 or 5. Luxshare at 4 to 5 "
            "percent is the bitter business he prefers, because few owners copy a hard "
            "life for a thin margin, and many will copy 30 percent. Moutai is the deep "
            "moat: baijiu is weak and Moutai still holds the shelf price while other "
            "labels trade inverted. He believes in technology and not in technology "
            "stocks. On AI hardware spend, a 1 trillion bill can fall to 300 or 400 "
            "billion in two years, the way photovoltaic equipment orders fell about "
            "90 percent over two or three years. Optimistic optical demand of 200 to "
            "300 billion and a pessimistic peak of 70 to 80 billion are a variance he "
            "will not underwrite. Beer is the small-variance cousin: margins went from "
            "about 3 points twenty years ago to about 15."
        ),
    ]
    mental = {
        "name": "Pyramid allocation × small mistakes × bitter margin",
        "components": (
            "Price the asset class by earnings yield before you pick a story. Under "
            "14 times on CSI 300 is about 7.5 percent, against deposits near 1 percent. "
            "Add equity when the multiple is low. Cut it if Shanghai is at 5,000 or "
            "6,000. The inverted pyramid, empty at 3,000 and full plus leverage at "
            "4,500, is how ordinary accounts lose. A wrong name is allowed if it is "
            "3 to 5 percent. A 40 percent drawdown in a hot fund versus under 10 points "
            "in a balanced book is the same lesson. Prefer a moat that holds price, or "
            "a bitter 4 to 5 percent margin. Do not underwrite a 30 percent margin that "
            "a crowd can enter. Most technology-stock profits are not his to take."
        ),
        "application": (
            "600519.SZ is the moat example, a shelf price that other baijiu labels no "
            "longer hold. 002475.SZ is the bitter industrial margin, not a new buy "
            "order. 000002.SZ is the trap already lived, sized small on purpose. The "
            "action is the pyramid, not a call on optical modules."
        ),
    }
    insights = [
        {
            "view": "Seven to eight percent is the scarce yield.",
            "question": "Why is equity the attractive asset now?",
            "answer": (
                "CSI 300 under 14 times and ROE of 11 to 12 percent on 1.4 times book "
                "both land near 7 to 8 percent. Deposits are about 1 percent and credit "
                "bonds about 2 to 3."
            ),
        },
        {
            "view": "The miss has to stay small.",
            "question": "What did Vanke teach him?",
            "answer": (
                "Late 2020 it looked cheap and high quality. From 2022 it destroyed "
                "value. It was 3 to 5 percent of the book, so the error was survivable."
            ),
        },
        {
            "view": "A fat margin without a moat gets copied.",
            "question": "Why avoid the 30 percent optical profit?",
            "answer": (
                "Luxshare earns 4 to 5 percent in a hard business few will copy. "
                "Thirty percent in a shallow moat is the profit a crowd will chase."
            ),
        },
    ]
    invest = [
        {
            "ticker": "600519.SZ",
            "company": "Kweichow Moutai",
            "direction": "Long",
            "confidence": "Low",
            "thesis": "The baijiu moat that still holds a shelf price — low",
            "rationale": (
                "Baijiu is weak and Moutai still holds the only shelf price that is "
                "not inverted. He uses it as the deep moat, not as a fresh price target."
            ),
        },
        {
            "ticker": "002475.SZ",
            "company": "Luxshare Precision",
            "direction": "Long",
            "confidence": "Low",
            "thesis": "A bitter 4 to 5 percent margin over a 30 percent optical profit — low",
            "rationale": (
                "A 4 to 5 percent margin in a bitter business is the industrial pattern "
                "he prefers to a 30 percent optical margin that rivals can enter."
            ),
        },
        {
            "ticker": "000002.SZ",
            "company": "China Vanke",
            "direction": "Long",
            "confidence": "Low",
            "rationale": (
                "His largest value trap, bought when quality and the multiple both "
                "looked fine, and kept to 3 to 5 percent so the error stayed small. "
                "Not a new long. The lesson is size."
            ),
        },
    ]
    # Direction must be Long or Short. A trap he already owns is not a short call.
    # Drop Vanke from the position list; keep it as a keyword via the prose.
    invest = invest[:2]
    chrono = {"subject": "Liang Yufeng · Steady Is Fast · six steadies", "events": [
        {"date": "1998", "event": "Enters the securities industry"},
        {"date": "2000s", "event": "Runs research at Orient Securities for more than ten years"},
        {"date": "2014", "event": "Leaves to build his own research practice"},
        {"date": "2020-12", "event": "Looks at Vanke before the property break"},
        {"date": "2022", "event": "Property downturn turns that holding into a value trap"},
        {"date": "2026-06-30", "event": "Hot public funds he watches later fall more than 40 percent"},
        {"date": "2026-10-20", "event": "Taping, after the October growth-stock drawdown"},
        {"date": "2026-11-23", "event": "E212 publishes"},
    ]}
    en = en_std(
        eid, "Practical Investments", "David", meta, 3,
        ["600519.SZ", "002475.SZ", "000002.SZ"],
        concl, bg, facts, mental, insights, invest, quotes, chrono,
        "| v4.10 window TZS E212", "whisper-small",
    )
    zh_meta = dict(meta)
    zh_meta.update(
        title="E212 《稳就是快》的理念与实践｜David对话梁宇峰",
        guest="梁宇峰",
        guest_role="《稳就是快》作者",
    )
    zh = dict(en)
    zh.update({
        "podcast": "投资实战派",
        "host": "David",
        "metadata": zh_meta,
        "conclusion": (
            "10月回调之后，梁宇峰用《稳就是快》讲A股怎么落地。沪深300不到14倍，"
            "盈利收益率大约7.5%，ROE大约11%到12%，市净率大约1.4倍，两条都指向7%到8%。"
            "存款大约1%，信用债大约2%到3%。配置要金字塔：便宜时多配权益，上证到5000或6000再降。"
            "2020年底看中的万科，是他最大的价值陷阱。光模块30%的净利率如果没有深护城河，"
            "就是别人会来抢的利润。他信科技，不信科技股。"
        ),
        "background": (
            "E212，11月23日发布，10月20日录，大约77分钟。David请梁宇峰。"
            "他1998年入行，在东方证券管了十多年研究，2014年出来自己做。"
            "新书由刘纪鹏作序。Whisper把书名听成稳救书块，把梁宇峰听成梁云芬。"
            "六稳是配置、标的、操作、组合、风控、心态。开场有五本签名书抽奖。不是荐股。"
        ),
        "important_facts": [
            "权益的吸引力是盈利收益率。沪深300不到14倍，倒数大约7.5%。今年业绩增长他放到大约20%，不算进去，潜在回报仍是7%到8%。ROE大约11%到12%，高峰时大约20%，当时和标普500差不多。银行ROE从大约20%降到大约10%。市净率大约1.4倍，11%到12%除以1.4还是7%到8%。存款大约1%，国债大约1.6%到1.7%，信用债大约2%到3%。上海租金回报1到2个点，以前房价每年大约10个点的资本利得，现在这个预期没了。60%权益、40%债券这种简单方案，他读过的一篇文章里打赢了很多复杂模型。",
            "便宜也会毁灭价值。他最大的价值陷阱是万科，2020年底或2021年初看的时候泡沫还没破，质地和估值都好看。2022年行业变成价值毁灭。仓位他压得很小，大约3到5个点。银行是对照。如果2021年有人说销售面积要跌70%到80%、房价跌30%到40%，他说99%的人不会信，还会觉得经济和银行都完了。五六年后这件事发生了，大行有盈利压力，没有流动性断裂。暴露比想象小，因为监管早就把银行和房企融资隔开，影子银行才起来。6月30日高点之后，他关注的一些公募回撤超过40%，自己的模拟均衡组合不到10个点。",
            "没有深护城河的30%净利率是请人来抢。光模块夹在强上游和强下游中间，短缺时这个环节能到大约30%，而中国制造业10%已经很好，很多只有4到5个点。立讯大约4到5个点，是他喜欢的苦生意：很少有人愿意为这点利润去复制那么苦的活，30%则会有一堆人来分。茅台是深护城河，白酒差的时候只有它还能稳住一批价，别的已经倒挂。他是科技信仰者，不是科技股信仰者。AI硬件资本开支，1万亿可能两年掉到3000到4000亿，像光伏设备两三年订单掉大约90%，不是从1万亿慢慢掉到9000亿。乐观看到2000到3000亿、悲观700到800亿见顶，这种方差他不认。啤酒是方差小的对照，净利率二十年前大约3个点，现在大约15个点。",
        ],
        "mental_model": {
            "name": "金字塔配置 × 错误要小 × 苦利润",
            "components": "先用盈利收益率给大类资产定价，再讲故事。沪深300不到14倍，大约7.5%，存款大约1%。便宜时把权益配重，上证到5000或6000再降下来。倒金字塔是3000点空仓、4500点加杠杆，这是普通账户亏钱的路径。看错一个名字可以，只要它只占3到5个点。热门基金回撤超过40%，均衡组合不到10个点，是同一件事。要价格还能站住的护城河，或者4到5个点的苦生意。不要为一个人群能进来的30%利润签字。科技股里大部分钱，不是他能挣的。",
            "application": "600519.SZ是护城河例子，一批价还在，别的白酒倒挂。002475.SZ是苦的工业利润，不是新的买入指令。000002.SZ是已经吃过的陷阱，仓位故意很小。要做的是金字塔，不是给光模块定价。",
        },
        "key_insights": [
            {"view": "7%到8%是现在稀缺的收益率。", "question": "为什么权益最有吸引力？", "answer": "沪深300不到14倍，ROE大约11%到12%除以1.4倍市净率，都落在7%到8%。存款大约1%，信用债大约2%到3%。"},
            {"view": "看错可以，仓位不行。", "question": "万科教了什么？", "answer": "2020年底质地和估值都好看。2022年变成价值毁灭。它只占组合3到5个点，所以错误还能活。"},
            {"view": "没有护城河的厚利润会被复制。", "question": "为什么躲开光模块的30%？", "answer": "立讯4到5个点的苦生意很少有人复制。30%的浅护城河会招来一堆竞争者。"},
        ],
        "golden_quotes": quotes,
        "review_notes": "| v4.10 window 投资实战派 E212",
    })
    dump(ROOT / f"data/approved/{eid}.json", en)
    dump(ROOT / f"data/approved/zh/{eid}.json", zh)
    validate_file(ROOT / f"data/approved/{eid}.json")


if __name__ == "__main__":
    main()
