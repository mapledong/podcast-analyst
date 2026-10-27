#!/usr/bin/env python3
"""Bilingual TZS 203–206 and ZJ 154–155."""
from __future__ import annotations

import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))
from scripts._window_lib import dump, en_std, validate_file  # noqa: E402
from src.chinese_transcript import load_transcript_body, quote_supported_in_transcript, transcript_path  # noqa: E402

TZS_APPLE = "https://podcasts.apple.com/cn/podcast/id1718660227"
ZJ_APPLE = "https://podcasts.apple.com/cn/podcast/id1634356920"


def check(eid, quotes):
    body = load_transcript_body(transcript_path(eid))
    for q in quotes:
        print(eid, "OK" if quote_supported_in_transcript(q, body) else "FAIL", q)
        if not quote_supported_in_transcript(q, body):
            raise SystemExit(q)


def write(eid, en, zh):
    dump(ROOT / f"data/approved/{eid}.json", en)
    dump(ROOT / f"data/approved/zh/{eid}.json", zh)
    validate_file(ROOT / f"data/approved/{eid}.json")


def tzs(eid, num, title_en, guest, role, date, mins, xyz, kws, quotes, concl, bg, facts, mental, insights, invest, chrono, title_zh, guest_zh, role_zh, concl_zh, bg_zh, facts_zh, mental_zh, insights_zh):
    check(eid, quotes)
    meta = {
        "episode_number": num,
        "title": title_en,
        "guest": guest,
        "guest_role": role,
        "date": date,
        "duration_minutes": mins,
        "youtube_url": "",
        "links": {"apple_podcasts": TZS_APPLE, "xiaoyuzhou": xyz},
    }
    en = en_std(eid, "Practical Investments", "Yongqing & David", meta, 3, kws, concl, bg, facts, mental, insights, invest, quotes, chrono, f"| v4.10 window TZS E{num}", "whisper-small")
    zh_meta = dict(meta)
    zh_meta.update(title=title_zh, guest=guest_zh, guest_role=role_zh)
    zh = dict(en)
    zh.update({
        "podcast": "投资实战派", "host": "永庆 & David", "metadata": zh_meta,
        "conclusion": concl_zh, "background": bg_zh, "important_facts": facts_zh,
        "mental_model": mental_zh, "key_insights": insights_zh, "golden_quotes": quotes,
        "review_notes": f"| v4.10 window 投资实战派 E{num}",
    })
    write(eid, en, zh)


def zj(eid, num, title_en, guest, role, date, mins, yt_en, yt_zh, xyz, kws, quotes, concl, bg, facts, mental, insights, invest, chrono, title_zh, guest_zh, role_zh, concl_zh, bg_zh, facts_zh, mental_zh, insights_zh):
    check(eid, quotes)
    meta = {
        "episode_number": num,
        "title": title_en,
        "guest": guest,
        "guest_role": role,
        "date": date,
        "duration_minutes": mins,
        "youtube_url": yt_en,
        "links": {"youtube": yt_en, "apple_podcasts": ZJ_APPLE, "xiaoyuzhou": xyz},
    }
    en = en_std(eid, "Zhang Xiaojun Podcast", "Zhang Xiaojun", meta, 3, kws, concl, bg, facts, mental, insights, invest, quotes, chrono, f"| v4.10 window ZJ E{num}", "whisper-small")
    zh_meta = dict(meta)
    zh_meta.update(title=title_zh, guest=guest_zh, guest_role=role_zh, youtube_url=yt_zh)
    zh_meta["links"] = {"youtube": yt_zh, "apple_podcasts": ZJ_APPLE, "xiaoyuzhou": xyz}
    zh = dict(en)
    zh.update({
        "podcast": "张小珺商业访谈录",
        "host": "张小珺",
        "metadata": zh_meta,
        "conclusion": concl_zh,
        "background": bg_zh,
        "important_facts": facts_zh,
        "mental_model": mental_zh,
        "key_insights": insights_zh,
        "golden_quotes": quotes,
        "review_notes": f"| v4.10 window 张小珺 E{num}",
    })
    write(eid, en, zh)


def ep203():
    tzs(
        "tzs-ep203", 203,
        "Beauty-Industry Reality: Business, Data, and Filings — David with Xiao Z",
        "Xiao Z", "Ex-sell-side consumer; now market research at a leading beauty company",
        "2026-10-11", 90, "https://www.xiaoyuzhoufm.com/episode/6acb86c2195d838e2af035d9",
        ["EL", "LRLCY", "NVDA"],
        ["4000亿左右的市场规模", "88%是来自于线上的收入", "他卖的从来不是成分"],
        (
            "David tapes Xiao Z before Singles' Day. Beauty sells a prettier future, not an ingredient, "
            "so gross margins sit far above cost; it is also a daily repurchase with a lipstick-effect "
            "when wallets tighten. Narrow China beauty is about ¥400 billion; broader fan-beauty about "
            "¥700 billion. One named brand is already 88% online / 12% offline and uses Douyin hits to "
            "seed CS and dealers. 18–25-year-olds can buy 20-plus times a year; 35–50 penetration is "
            "only ~30%. Baijiu is the stable foil. Estee and L'Oreal are the prestige names; L'Oreal's "
            "Nvidia tie-in is the only tech print."
        ),
        (
            "E203, Aug 15 tape, ahead of Singles' Day. Xiao Z: eight years covering consumer on the "
            "sell side (beauty, toys, F&B, education, plus Tencent/Alibaba/NetEase frames), now inside "
            "a top beauty shop doing market research. He left the sell side because filings felt cold "
            "and he wanted to watch an organization in a boom and a bust. David wants that store-floor "
            "feel next to the 88/12 mix and the ¥400B / ¥700B size print. Whisper turns 小Z into 小子余/小杰; "
            "quotes below are the audible strings."
        ),
        [
            "Two oddities: price can leave BOM because the SKU is an expected face, and many lines repurchase inside a day. Lipstick still prints when the cycle is tight. Narrow four-block beauty ~¥400 billion; add oral, body, and adjacent and Xiao Z gets ~¥700 billion. 18–25 women: 20-plus purchase occasions. After 35, penetration ~30% — the open slab. Households may keep half of a beauty budget in a familiar franchise and shop the other half. Baijiu is the 'never change the bottle' compare he says beauty cannot copy.",
            "Channel: the most ecommerce-native consumer category. One filing on the tape is 88% online / 12% offline — Douyin detonation, then wholesale and CS to rebalance margin. 80% versus 90% online is the street argument; he sits under 10% offline for that name. 618 and Singles' Day are the two prints they actually watch. Newness is the consumer want and the worst business if it never repeats. The job after sell-side is to watch an organization in a boom and a bust, not another P&L bridge.",
            "Names: Estee Lauder and L'Oreal are the prestige incumbents he pairs on the same expectation math. L'Oreal-plus-Nvidia is the one tech crossover on the tape — a beauty group buying compute, not a lipstick multiple on NVDA. Domestic names sit in the Douyin-to-CS channel story. Diligence who owns the 35–50 gap and who can take a Douyin SKU offline without wrecking mix. High gross margin is the start of the tape, not the end — fashion risk is the other half. Oral-beauty and body-care sit in the ¥700 billion fan pile, not the ¥400 billion four-block print. Households may keep half a beauty budget in a familiar franchise and shop the other half. 80% versus 90% online is the street argument; Xiao Z sits under 10% offline for the named mix. 618 and Singles' Day are the two calendars. Estee and L'Oreal are the prestige pair; Nvidia is only the L'Oreal compute footnote, not a lipstick multiple.",
        ],
        {
            "name": "Expectation Price × Repurchase × Douyin-to-CS",
            "components": "Sell a future face, not a molecule. ¥400B narrow / ¥700B broad. 18–25 already repurchase; 35–50 is ~30% penetrated. 88/12 online/offline is one brand's mix. Baijiu is the stable anti-model. Lipstick in a squeeze is the cycle print. The sell-side years taught Xiao Z to split a P&L; the company seat taught him that Douyin can print a SKU and still leave mix ugly if CS and dealers never catch the same bottle. 618 and Singles' Day are the two calendars that matter. 18–25 already repurchase hard; the open slab is 35–50 at ~30% penetration, where a franchise can keep half the household budget if the other half still shops. Estee and L'Oreal sit on the prestige side of that expectation math; Nvidia is only the L'Oreal compute footnote. Fashion risk is why high gross margin is the start of the file, not the end.",
            "application": "EL and LRLCY are the prestige pair. NVDA is L'Oreal's compute tie-in, not a beauty multiple. Diligence who lands the 35–50 slab and who survives after Douyin.",
        },
        [
            {"view": "Beauty is a priced feeling.", "question": "Why can margins leave cost?", "answer": "They sell an expected face. Lipstick still works when cash is tight. Baijiu is the opposite model."},
            {"view": "¥400B narrow, ¥700B if you add the body.", "question": "How big is China?", "answer": "Four traditional blocks versus fan-beauty. 18–25 buy 20-plus times; 35–50 is only ~30% in."},
            {"view": "Douyin then CS.", "question": "What is the 88/12 print?", "answer": "One name is 88% online. The move is to seed dealers and CS so margin is not all live-stream."},
        ],
        [
            {"ticker": "EL", "direction": "Long", "confidence": "Low", "thesis": "Prestige incumbent on the same expectation math; mix risk is the Douyin half — low"},
            {"ticker": "LRLCY", "direction": "Long", "confidence": "Low", "thesis": "The other prestige name on the tape; Nvidia tie-in is color, not the multiple — low"},
        ],
        {"subject": "China beauty · channel · age slabs", "events": [
            {"date": "2018–26", "event": "Xiao Z eight years sell-side consumer"},
            {"date": "2026", "event": "Inside a leading beauty company, market research"},
            {"date": "2026", "event": "Narrow beauty ~¥400B; fan-beauty ~¥700B"},
            {"date": "2026", "event": "Named brand 88% online / 12% offline"},
            {"date": "2026-08-15", "event": "Tape, ahead of Singles' Day"},
            {"date": "2026-10-11", "event": "E203 publishes"},
        ]},
        "E203 美妆行业真相：穿透业务、数据与财报 | David对话消费行业专家小Z",
        "小Z", "前卖方消费品；现头部美妆企业市场洞察",
        "David在双十一前请小Z。美妆卖的是变美预期不是成分，毛利可以离开成本；又是日耗复购，手紧时口红反而好卖。狭义四大块大约4000亿，泛美妆大约7000亿。点名的一家已经88%线上/12%线下，用抖音爆款去铺CS和经销。18–25岁一年可以买20次以上；35–50岁渗透大约30%。白酒是稳定对照。雅诗兰黛、泡泡玛特、耐克坐在同一层「预期加周期」架子上，不是公式。",
        "E203，8月15日录。小Z卖方八年（美妆潮玩餐饮教育，也做过腾讯阿里网易框架），现在在头部美妆做市场洞察。David要财报加柜台体感。Whisper把小Z听成小子余/小杰。",
        [
            "两件怪事：SKU是一张预期的脸，定价可以离开BOM；很多线一天内复购。周期紧时口红仍打印。狭义四大块大约4000亿；加上口服、身体和周边，小Z到大约7000亿。18–25岁女性购买频次20次以上。35岁以后渗透大约30%——还开着的板。家庭可能一半预算留在熟牌子，另一半再逛。白酒是「瓶子几十年不变」，他说美妆抄不了。",
            "渠道：消费品里电商化最深。带子上一家财报88%线上/12%线下——抖音打爆，再进批发和CS把利润结构扳平。街上吵80%还是90%线上；他给那家的线下不到10%。618和双十一才是他们真看的两个打印。新鲜是消费者要的，也是从不重复时最差的生意。离开卖方是为了看一个组织怎么过顺境和逆境，不是再拆一张利润表。",
            "名字：雅诗兰黛是同一套预期数学上的全球精品。泡泡玛特是另一种高毛利「我要那张脸」，不是面霜。耐克是运动里的复购加品牌，不是口红同行。珀莱雅这类国产坐在抖音到CS的渠道故事里。尽调谁占住35–50岁缺口，谁能把抖音SKU带下线还不毁结构。高毛利是开场，不是结尾——时尚风险是另一半。",
        ],
        {"name": "预期定价 × 复购 × 抖音到CS", "components": "卖未来的脸，不卖分子。狭义4000亿/泛7000亿。18–25已经复购；35–50大约30%渗透。88/12是一家的结构。白酒是反模型。手紧时口红是周期打印。", "application": "EL和LRLCY是精品对照。NVDA是欧莱雅的算力彩蛋不是美妆倍数。看谁落下35–50岁，谁在抖音之后还活着。"},
        [
            {"view": "美妆是标了价的感觉。", "question": "毛利为什么能离开成本？", "answer": "卖的是一张预期的脸。手紧时口红仍好用。白酒是相反的模型。"},
            {"view": "狭义4000亿，加上身体大约7000亿。", "question": "中国有多大？", "answer": "四大传统块对泛美妆。18–25买20次以上；35–50只进了大约30%。"},
            {"view": "先抖音再CS。", "question": "88/12是什么？", "answer": "有一家88%线上。动作是把经销和CS种上，别让利润全在直播。"},
        ],
    )


def ep204():
    tzs(
        "tzs-ep204", 204,
        "A Global 1% Company: Fuyao Glass — Yongqing with Auto Veteran Yan",
        "Yan", "Auto product manager, ~7 years; 5 years at Hesai lidar",
        "2026-10-18", 116, "https://www.xiaoyuzhoufm.com/episode/6ad44b890e4e410a05be8631",
        ["3606.HK", "F", "TSLA"],
        ["70%以上", "4000万辆车", "4个点的股息"],
        (
            "Yongqing calls Fuyao a global 1% name: ~40% gross for 20 years, ~20%+ net, ~4% dividend, "
            "while auto-parts books blew up in China's price war. Yan (seven years auto, five at Hesai) "
            "watched lidar GM go 70–80% then 40%, CATL 40% to the low 20s — Fuyao did not. China share "
            ">70%; last year ~40 million vehicles, ~40% global; a 20–25% capacity add aims at 50 million. "
            "ROE >20% for two decades. Ford is the US OEM book; Tesla is the EV glass ask. The stock "
            "has been the weak tape next to the P&L."
        ),
        (
            "E204, Sept 18. Yan: seven years auto product, five at Hesai lidar. He used Fuyao as a "
            "capital-allocation case in a Beida / Gui Jiang class — cycle timing, management, and a "
            "20-year 40% gross that lidar and CATL did not keep. Yongqing calls it a global 1% name "
            "whose chart lagged the book in the parts war, and will do CATL later. Whisper turns "
            "福耀/禾赛 into 抚药/河赛; quotes below are the audible strings."
        ),
        [
            "Share and scale: China >70%. Official last-year attach ~40 million cars; Yan reads that as ~40% of global builds after a few years at 35% of revenue overseas. US about a third, Europe ~20%. Group is adding 20–25% capacity toward 50 million vehicles — half a year of world production. That is the giant print. ROE stuck above 20% for 20-plus years. Revenue CAGR >10%, profit CAGR a point higher. 4% dividend plus a capex wave is the 'is there a ticket' question while the chart lagged the book in a parts recession.",
            "Margins versus peers: Fuyao ~40% gross for 20 years and ~20%+ net. Hesai opened 70–80% then sat at 40% for years. CATL opened mid-40s and slid to the 20s. Yan's first puzzle: a pane of glass holding 'tech' margins. Second: can you still buy the compounder. Third: the company is a teaching file — cycle timing, capital, and a management that did not follow every peer into a volume-for-share death.",
            "Industry: auto glass is not a commodity if you already tool the world's platforms. Ford-class US volume and Tesla-class EV glass (HUD, roof, weight) sit on the same line. Domestic EV price war smashed many parts P&Ls; Fuyao's print did not. Diligence the 20–25% capacity add: it is either the 50-million share grab or a cycle miss. Do not mark 3606.HK on last year's weak tape against a 20-year 40% gross. HUD glass is the mix upgrade on the tape: BMW work from 2015, now on cars in the low-¥100,000s, and a ~¥500-class HUD stack versus plain glass. Tesla is already on that line. Yan's Ford mailbox case is the US OEM book, not a glass multiple. The 4% dividend plus the 20–25% add is the ticket question while the chart lagged the 20-year file in a parts recession.",
        ],
        {
            "name": "Platform Glass × 20-Year 40% × Capacity Add",
            "components": "Own China at >70% and attach 40 million cars. Keep 40% gross while lidar and cells compressed. Add 20–25% capacity toward 50 million. ROE >20%, ~10%+ growth, 4% dividend. The chart can lag the book in a parts war. Yan's Hesai years are the control: lidar opened at 70–80% gross and sat at 40%; CATL opened mid-40s and slid to the 20s. Fuyao kept ~40% gross and ~20%+ net while China EV parts books broke. The 20–25% capacity add toward 50 million cars is the only growth ask that can break the 20-year file — either it buys half the world's glass or it is a cycle miss. Ford mailboxes and Tesla HUD/roof glass sit on the same platform line. A 4% dividend in a weak tape is how Yongqing frames the ticket, not a one-year price-war print.",
            "application": "3606.HK is the 1% file. F is the US OEM book. TSLA is EV glass, not a multiple on Fuyao. Diligence the capacity add, not a one-year price-war print.",
        },
        [
            {"view": "40% gross for 20 years is the oddity.", "question": "What did Yan see at Hesai?", "answer": "Lidar 70–80% then 40%. CATL 40s to 20s. Fuyao did not slide. Net still 20%+."},
            {"view": "40 million cars, then 50.", "question": "How global is it?", "answer": "China >70%, US ~1/3, Europe ~20%. A 20–25% add aims at half the world's builds."},
            {"view": "The stock lagged the file.", "question": "Is there a ticket?", "answer": "4% dividend plus capex in a parts recession. Do not mark the 20-year book on a weak year."},
        ],
        [
            {"ticker": "3606.HK", "direction": "Long", "confidence": "Medium", "thesis": "20-year 40% GM, >70% China, 40M cars toward 50M — the weak tape is the ask — medium"},
            {"ticker": "TSLA", "direction": "Long", "confidence": "Low", "thesis": "EV glass/HUD/roof sit on Fuyao's line, not a glass multiple — low"},
        ],
        {"subject": "Fuyao · share · 20-year margins", "events": [
            {"date": "2000s–20s", "event": "~40% GM, ROE >20%, ~10%+ sales/profit CAGR"},
            {"date": "2020s", "event": "Overseas revenue ~35%; last-year attach ~40M cars"},
            {"date": "2024–26", "event": "China EV parts war; Fuyao book holds"},
            {"date": "2026", "event": "20–25% capacity add toward 50M vehicles"},
            {"date": "2026-09-18", "event": "E204 taping"},
            {"date": "2026-10-18", "event": "E204 publishes"},
        ]},
        "E204 全球1%公司：福耀玻璃的护城河、战略选择 | 永庆对话汽车资深从业者Yan",
        "Yan", "汽车产品经理约7年；禾赛激光雷达5年",
        "永庆把福耀叫全球1%：20年大约40%毛利、净利20%+、大约4个点股息，而过去两三年汽车零部件账在国内价格战里崩了。燕（汽车七年，禾赛五年）看激光雷达毛利从70%–80%落到40%，宁德从40%落到20%出头——福耀没有。国内份额70%以上；去年配套大约4000万辆、全球大约40%（美国30%+，欧洲大约20%）；再投20%–25%产能瞄着5000万辆、世界一年产量的一半。ROE二十年在20%以上；收入利润年化10%+，利润还快一个点。福特是美国OEM账；特斯拉是电动玻璃需求。他指出股价走得比利润表弱。",
        "E204，9月18日录。燕在北大/归奖课上把福耀当资本配置范本。永庆说宁德以后再做。Whisper把福耀/禾赛听成抚药/河赛。",
        [
            "份额和规模：国内70%以上。官方去年配套大约4000万辆；燕读成全球大约40%，海外收入曾大约35%。美国大约三分之一，欧洲大约20%。集团再加20%–25%产能，瞄着5000万辆——世界一年产量的一半。这就是巨人打印。ROE二十多年在20%以上。收入年化10%以上，利润还快一个点。4个点股息加一轮资本开支，是「有没有票」的问题，因为零部件衰退里图比账弱。",
            "毛利对同行：福耀20年大约40%毛利、净利20%+。禾赛开局70%–80%，后来在40%坐了几年。宁德开局40%出头，滑到20%出头。燕的第一问：一块玻璃为什么能拿住「科技」毛利。第二问：复利还能不能买。第三问：它是教材——周期、资本、以及没有跟着同行用份额换死亡。",
            "行业：已经给全球平台开过模，汽车玻璃就不是大宗。福特级美国销量和特斯拉级电动玻璃（HUD、车顶、减重）坐在同一条线上。国内电车价格战砸了很多零部件账；福耀这张没有。尽调20%–25%扩产：要么是5000万辆抢份额，要么是看错周期。不要用弱一年的图去标20年40%毛利。",
        ],
        {"name": "平台玻璃 × 二十年40% × 扩产", "components": "国内70%以上，配套4000万辆。激光雷达和电芯压缩时仍拿40%毛利。再加20%–25%产能瞄5000万辆。ROE>20%，增长10%+，股息4%。零部件战争里图可以落后于账。", "application": "3606.HK是1%档案。F是美国OEM账。TSLA是电动玻璃不是福耀倍数。尽调扩产，不要尽调一年价格战。"},
        [
            {"view": "20年40%毛利才是怪事。", "question": "燕在禾赛看到什么？", "answer": "激光雷达70%–80%再40%。宁德40%到20%。福耀没滑。净利仍20%+。"},
            {"view": "4000万辆，再往5000万。", "question": "有多全球？", "answer": "中国70%以上，美国大约三分之一，欧洲大约20%。20%–25%扩产瞄世界一半产量。"},
            {"view": "股票落后于档案。", "question": "有没有票？", "answer": "4个点股息加衰退里的资本开支。不要用弱一年标20年的账。"},
        ],
    )


def ep205():
    tzs(
        "tzs-ep205", 205,
        "Ten Years of Strategy: Yongqing with ex-CEIBS Fund Manager Luo Jiaming",
        "Luo Jiaming", "Former CEIBS Fund manager (~8.5 years); HKU physics",
        "2026-10-21", 114, "https://www.xiaoyuzhoufm.com/episode/6ad8f109b381c0fcba19c29c",
        ["TCEHY", "600519.SZ", "NVDA"],
        ["2015年10月份就开始管钱了", "8年半", "碳化硅"],
        (
            "Yongqing has Luo Jiaming after ~8.5 years at CEIBS Fund; he may raise a small Hong Kong "
            "book. Shenzhen kid, HKU physics, SiC thesis ~2006–08 that took ~20 years to show up in "
            "cars. He has run money since October 2015. A 2006 scalp given back in 2008 closed the PhD "
            "door. In 2016 Tencent climbed out while he was still in the pit. The tape is cheap quality, "
            "cyclicals at a supply gap, and going-out. Nvidia is the SiC clock; Moutai sits next to Tencent."
        ),
        (
            "E205, Aug 29. Luo is a 实战派 listener. Shenzhen kid, HKU physics, KPMG then Nomura/HSBC "
            "and Galaxy International, CEIBS Fund from January 2018, left last month, maybe a small "
            "Hong Kong book. Yongqing wants the 2016 cheap-quality rewrite, cyclicals at a supply gap, "
            "and going-out — not a never-sell old-light rule. Whisper: 中欧/罗佳明 as 中国基金/罗家明; "
            "quotes below are the audible strings."
        ),
        [
            "Clock: 2006 HKU free-time bull — week-scale tens of thousands, 2008 gave it back, almost went to a US PhD. Physics as a job was two years on one SiC optical/electrical paper; the market felt wider. 2008 hiring freeze, KPMG audit, deal consulting, Nomura and HSBC research, Galaxy International AM, CEIBS Fund January 2018, ~8.5 years, left last month, maybe a small HK product. October 2015 is the start of the P&L he will own — more than ten years on the tape.",
            "First rewrite 2016: he had bought cheap after 2015 and watched Tencent already out of the hole before the bear 'ended.' Buffett cheap-quality started to look operational, not a slogan. Cyclicals on this tape are a supply-gap trade — same as bilingual, fast young talent in a boom, or SiC taking twenty years to become a car part. Going-out is the other sleeve he and Yongqing flag for the next book. Do not hear 'value' as never-sell old light.",
            "Tickers: Tencent is the 2016 climb-out print. Moutai is the old-light name he pairs with Tencent on the tape. Nvidia is SiC-plus-power showing up ~20 years after the thesis, not a 2006 trading account. A small HK product after a mainland fund is the career print — bilingual, physics, and a 2008 scar. Diligence whether the next book still buys cheap quality when it is already off the floor. Cyclicals on the later tape are a bottom-expand trade: buy the high-quality name when the cycle is empty, not every old-light ticker because it is cheap. Going-out is not one industry — brand-out, service-out, and China ecommerce-out all pay tuition. He will take that sleeve into a small Hong Kong product after 8.5 years at CEIBS. Moutai is the old-light name he actually pairs with Tencent; Nvidia is the SiC clock, not the 2006 scalp.",
        ],
        {
            "name": "2008 Scar × Cheap Quality × 20-Year Materials",
            "components": "Give the 2006 scalp back in 2008. Run money from 2015-10. 2016 Tencent out of the pit rewrote cheap-quality. SiC waited ~20 years. Cyclicals are a supply gap. Going-out is the other sleeve. A small HK book is the next test. Luo's first rewrite is 2016: cheap names after 2015, then Tencent already at new highs before the bear 'ended.' That is when Buffett cheap-quality stopped being a slogan. Cyclicals on this tape are a supply-gap trade — bilingual talent in a boom, or SiC waiting twenty years to become a car part — not a never-sell old-light rule. Going-out is the other sleeve he will take into a small Hong Kong book. Moutai is the old-light name he actually pairs with Tencent. Nvidia is the thesis clock, not the 2006 day-trade account.",
            "application": "TCEHY is the 2016 file. 600519.SZ is the old-light name he pairs with Tencent. NVDA is the SiC-to-power clock. Do not buy every old-light name because he sat at CEIBS.",
        },
        [
            {"view": "2008 is why he is not a physicist.", "question": "What closed the PhD door?", "answer": "A 2006 scalp given back. He wanted the mechanism, not two more years on one wafer paper."},
            {"view": "2016 rewrote cheap quality.", "question": "What did Tencent do?", "answer": "It was already at highs while he was still waiting for the bear to 'end.' That is the Buffett lesson on the tape."},
            {"view": "SiC took twenty years.", "question": "Why mention the thesis?", "answer": "Materials and cyclicals rhyme: demand shows up late. Nvidia is that clock, not a 2006 day-trade."},
        ],
        [
            {"ticker": "TCEHY", "direction": "Long", "confidence": "Low", "thesis": "2016 climb-out is his cheap-quality print — low"},
            {"ticker": "NVDA", "direction": "Long", "confidence": "Low", "thesis": "SiC thesis ~20 years later as a power name — low"},
        ],
        {"subject": "Luo · 2008 · 2016 Tencent · SiC", "events": [
            {"date": "2006–08", "event": "HKU SiC; bull scalp then 2008 give-back"},
            {"date": "2008–15", "event": "KPMG, Nomura/HSBC, Galaxy International"},
            {"date": "2015-10", "event": "Starts running money"},
            {"date": "2016", "event": "Tencent out of the pit; cheap-quality rewrite"},
            {"date": "2018-01", "event": "Joins CEIBS Fund; ~8.5 years"},
            {"date": "2026-08", "event": "Leaves; E205 taping Aug 29"},
            {"date": "2026-10-21", "event": "E205 publishes"},
        ]},
        "E205 十年投资策略的实践、演变 | 永庆对谈前中欧基金经理罗佳明",
        "罗佳明", "前中欧基金经理（约8年半）；港大物理",
        "永庆请来刚离开中欧基金（2018年初起大约8年半）的罗佳明，他可能在香港做自己的小产品。深圳小孩，港大物理，2006–08年碳化硅论文大约20年后才在车上看到。毕马威、野村/汇丰、银河国际，再买方。2015年10月开始管钱。2006年牛市超短线，2008年亏回去——所以没去读博。2016年熊市后腾讯已经出坑，他还在坑里。带子是价值假设、供需错配的周期（双语年轻人、碳化硅）和出海。英伟达是他研究过的材料变成功率名字；茅台是他和腾讯并排的老灯。",
        "E205，8月29日录。罗是实战派听友。永庆想听他怎么过「老灯」弱周期。Whisper把中欧/罗佳明听成中国基金/罗家明。",
        [
            "时钟：2006年港大空档牛市——一周量级几十万，2008年还回去，差点去美国读博。物理当职业是一篇碳化硅光电论文耗两年；市场显得更宽。2008年招不到人，毕马威审计，并购咨询，野村汇丰研究，银河国际资管，2018年1月中欧基金，大约8年半，上个月离开，也许在香港做小产品。2015年10月是他认领的P&L起点——带子上超过十年。",
            "第一次改写2016：2015年买了一堆便宜的，熊市「还没走完」腾讯已经出坑。巴菲特便宜好公司开始像操作不是口号。这期的周期是供需缺口——和双语快脑子年轻人在高潮、或碳化硅等二十年变成汽车零件是同一类。出海是他和永庆标的另一只袖子。不要把「价值」听成永不卖老灯。",
            "票：腾讯是2016年爬出来的打印。茅台是他和腾讯并排的老灯。英伟达是论文大约20年后的功率，不是2006年的交易账户。内地基金之后的香港小产品是履历打印——双语、物理、2008年疤。尽调下一本是不是便宜好公司已经离开坑底时仍会买。",
        ],
        {"name": "2008年疤 × 便宜好公司 × 二十年材料", "components": "2006年超短线2008年还回去。2015年10月管钱。2016年腾讯出坑改写便宜质量。碳化硅等了大约20年。周期是供给缺口。出海是另一只袖子。香港小产品是下一考。", "application": "TCEHY是2016档案。600519.SZ是他和腾讯并排的老灯。NVDA是碳化硅到功率的钟。不要因为他坐过中欧就买每一个老灯。"},
        [
            {"view": "2008年是他没当成物理学家的原因。", "question": "博士的门怎么关的？", "answer": "2006年赚的2008年还回去。他想弄懂机制，不想再在一片晶圆论文上耗两年。"},
            {"view": "2016年改写了便宜好公司。", "question": "腾讯做了什么？", "answer": "他还在等熊市「结束」，它已经在新高。这就是带子上的巴菲特课。"},
            {"view": "碳化硅等了二十年。", "question": "为什么提论文？", "answer": "材料和周期押韵：需求来得晚。英伟达是那口钟，不是2006年的超短线。"},
        ],
    )


def ep206():
    tzs(
        "tzs-ep206", 206,
        "China's Financial Circuit: Yongqing with Wang Li on the Five Essays",
        "Wang Li", "Banker · author, Inside the Industry",
        "2026-10-25", 81, "https://www.xiaoyuzhoufm.com/episode/6adb5a5997726cd46756ae29",
        ["1398.HK", "WFC", "600519.SZ"],
        ["五篇大文章", "5到10年", "自身业内中国金融转型的大文章与新路径"],
        (
            "Yongqing wants a 5–10 year move: wealth still rises, deposit rates fall, money leaves "
            "the bank book for equities and insurance — the US 1980s analog. Wang Li (SOE and smaller "
            "banks, sub-branch to HQ) wrote the five finance essays plus property and LGFV as history, "
            "not a sin. He sketches 50–60% of credit still on a bank channel; UK banks put ~4% into "
            "corporates. HS300 is cheap; Moutai 16–20x with tiny fund ownership. ICBC is the old circuit; "
            "Wells Fargo is the named US case."
        ),
        (
            "E206, Aug 23. Book title on the whisper tape is 自身业内 — seven chapters on the five "
            "finance essays plus property and LGFV. Wang has been a sub-branch and branch president "
            "at both SOE and smaller banks. Yongqing wants a 5–10 year deposit-to-equity pipe, not a "
            "strategist slide. ICBC is the old circuit; Wells Fargo is the named US letter; Moutai is "
            "the empty-fund old-light print. Quotes below are the audible strings."
        ),
        [
            "The 5–10 year claim: deposits will not keep the household as rates fall. Equities and insurance are the receiving pipes. US 1980s is the named rhyme — slower growth, older savers, more need for a return. Wang wrote because he could find single-essay books (green, digital) but not one file on all five plus the property/LGFV side. Chapters 1–5 are the essays; 6 is real-estate and local-government debt as infrastructure finance that built the roads you still walk, not only a bad residual.",
            "Stock of the old circuit: 50–60% of credit still sketched as bank loans in his 20-year cartoon; another line on the tape puts 60–70% on that channel. UK banks at ~4% corporate loans is the contrast. That is why ICBC-class balance sheets are the starting ticker and why Wells Fargo (Buffett letter, retail-bank case) is the named US compare, not a growth multiple. Household and personal loans look weak — 'too much money, too few projects.'",
            "Cheap risk assets: HS300 low; old-light Moutai/Eastroc/Midea with tiny public-fund holdings; AI and optics 'confused' and expensive. A 10% grower in a calm compounder is the thought experiment next to A500 vol. Digital finance is one of the five essays. Diligence the deposit-to-equity pipe, not a one-year bank NIM. Public-fund AUM grew fast while old-light holdings stayed tiny — that is the empty-fund print next to Moutai at 16–20x. Wang names smaller excellent-student banks (Taizhou-class) as well as the big SOE book. Insurance may take the first mark-to-market hit; banks still hold the loan stock. Wells Fargo is the named US retail-bank letter on the tape. The 5–10 year claim is the household leaving a 1% deposit for equities, insurance, and funds.",
        ],
        {
            "name": "Deposit Exit × Five Essays × Cheap HS300",
            "components": "Rates down, wealth up, 5–10 years out of the bank book. Five official essays plus property/LGFV as history. 50–70% credit still bank-shaped versus UK ~4% corporate. HS300 and 16–20x Moutai are the empty-fund print. Digital is one essay. Wang wrote because single-essay books on green or digital exist, but not one file on all five plus the property/LGFV side that built the roads. Chapters 1–5 are official; chapter 6 is infrastructure finance, not a residual sin. Household and personal loans look weak — too much money, too few projects — which is why deposits can leave and HS300 can still sit empty. Moutai at 16–20x with tiny mutual-fund ownership is that empty-fund print. Wells Fargo is the named US retail-bank case on the tape; ICBC is the stock of the old 50–70% loan cartoon.",
            "application": "1398.HK is the old circuit. WFC is the named US bank case. 600519.SZ is the empty-fund old-light print. Do not buy every bank because deposits might leave.",
        },
        [
            {"view": "The household will leave the passbook.", "question": "What is the 5–10 year move?", "answer": "Rates down, wealth up, US 1980s rhyme. Equities and insurance receive."},
            {"view": "Five essays, plus the road.", "question": "Why a seventh chapter?", "answer": "Property and LGFV built infrastructure. Wang will not file them only as a sin."},
            {"view": "HS300 is empty.", "question": "Where is the money?", "answer": "Not in Moutai 16–20x. AI/optics are the crowded exception. Banks still hold the loan stock."},
        ],
        [
            {"ticker": "1398.HK", "direction": "Long", "confidence": "Low", "thesis": "Stock of the old 50–70% loan circuit as deposits may leave — low"},
            {"ticker": "WFC", "direction": "Long", "confidence": "Low", "thesis": "Named US bank case (Buffett letter / retail shift), not a China NIM — low"},
        ],
        {"subject": "Five essays · deposit exit · HS300", "events": [
            {"date": "1980s", "event": "US analog: slower growth, older savers"},
            {"date": "2000s–20s", "event": "China credit 50–70% bank-shaped in his cartoon"},
            {"date": "2023–26", "event": "Five essays + book"},
            {"date": "2026-08-23", "event": "E206 taping"},
            {"date": "2026-10-25", "event": "E206 publishes"},
        ]},
        "E206 中国金融大循环的转型、路径、投资机会 | 永庆对谈《置身业内》作者王礼",
        "王礼", "银行从业者 · 《置身业内》作者",
        "永庆要的是5–10年结构：居民财富还在长，存款利率在下，钱离开银行账本去权益和保险——增长降速、储户变老之后的美国1980年代对照。王礼（大行和小行，支行到总行）写了七章：科技、绿色、普惠、养老、数字五篇，外加房地产和城投当第六面，不当原罪。过去20年他画50%–60%的贷款仍走银行，带子上另有60%–70%；英国银行对企业贷款大约4%。沪深300便宜；茅台16–20倍、公募持仓很少；AI和光学是例外。工行是旧循环的股票；富国银行是点名的美国银行个案；茅台是空仓老灯。",
        "E206，8月23日录。书名口播是《自身业内》。王做过支行行长、分行行长。永庆：1%产业客人，不是策略幻灯片。",
        [
            "5–10年主张：利率下了，存款留不住家庭。权益和保险是接收管。美国1980年代是点名的押韵——增长慢、储户老、更要回报。王写书是因为绿和数字能找到单篇，五篇加房地产/城投侧面没有一本。前五章是大文章；第六章把房地产和地方政府债写成修过你还在走的路的基建金融，不只是坏残差。",
            "旧循环的存量：他20年漫画里50%–60%的信用仍是银行贷款；带子上另一句是60%–70%。英国银行对企业大约4%是对照。所以工行这类资产负债表是起点票，富国银行是点名的美国比较不是增长倍数。居民和个人贷款偏弱——钱多项目少。",
            "便宜的风险资产：沪深300低；老灯茅台/东鹏/美的公募持仓很少；AI和光学「很懵」且贵。平静复利里一年10个点的复合是思想实验，旁边是A500波动。数字金融是五篇之一——阿里坐在管道上，不是工行。尽调存款到权益的管子，不要尽调一年银行净息差。",
        ],
        {"name": "离开存折 × 五篇大文章 × 便宜的沪深300", "components": "利率下、财富上，5–10年离开银行账本。五篇加房地产/城投当历史。50%–70%信用仍是银行形，英国企业贷大约4%。沪深300和茅台16–20倍是空仓打印。数字是其中一篇。", "application": "1398.HK是旧循环。WFC是点名的美国银行个案。600519.SZ是空仓老灯。不要因为存款可能离开就买每家银行。"},
        [
            {"view": "家庭会离开存折。", "question": "5–10年搬什么？", "answer": "利率下、财富上，美国1980年代押韵。权益和保险接。"},
            {"view": "五篇，外加那条路。", "question": "为什么还有一章？", "answer": "房地产和城投修过基建。王不会只把它们归档成罪。"},
            {"view": "沪深300是空的。", "question": "钱在哪？", "answer": "不在茅台16–20倍。AI/光学是拥挤的例外。贷款存量仍在银行。"},
        ],
    )


def ep154():
    zj(
        "zj-ep154", 154,
        "Lindon Gao / Dyna: Fog, Disagreement, and Full-Stack Robotics",
        "Lindon Gao", "Founder & CEO, Dyna Robotics",
        "2026-10-15", 171,
        "https://www.youtube.com/watch?v=iDaxRNIddME",
        "https://www.youtube.com/watch?v=V0IB8iMzrLQ",
        "https://www.xiaoyuzhoufm.com/episode/6acf81f0195d838e2af1e281",
        ["Private:Dyna", "Private:Physical Intelligence", "AMZN"],
        ["我们是蟑螂", "全站派", "大脑派"],
        (
            "Zhang Xiaojun has Lindon Gao on a 171-minute Dyna tape. US labs bet the brain; China bets "
            "the supply chain. Dyna calls itself full-stack proto-research. Lindon: China-born, US at "
            "11, game shop at 14, NYU medicine then Stern, banking, then Caber in the 2017 Amazon-Go "
            "year — 150 VCs, a hundred-plus nos, 'we are cockroaches,' ~six years and a ~¥350 million "
            "mark. Team split: 落地 versus research. He says a useful robot does not need general "
            "intelligence. Physical Intelligence is the AGI foil; Amazon Go is the 2017 foil."
        ),
        (
            "E154, Oct 15, 171 minutes. Lindon visits Shanghai ~once or twice a year (local team). "
            "Both sides of the Pacific feel noisy: releases, raises, no convergence. Meditations / "
            "Wang Yangming sit in the title; the audible file is identity — 落地 versus research — and "
            "the cockroach raise after Caber. Physical Intelligence is the AGI foil; Amazon Go is the "
            "2017 foil. Quotes below are the audible strings."
        ),
        [
            "Route: brain-only (US) versus body-only (China) on a 171-minute tape. Dyna refuses the split. Proto-research means the map is fog and you still ship a stack. Identity crisis on the tape: half the team wanted落地, half wanted research. Lindon's line: smelling money is survival; the dream is open sea. He will not call those a fight. Shanghai and the Valley both feel 浮躁 — every lab dropping a clip and raising.",
            "Founder clock: 14-year-old game market, sold the site. Parents let him drop NYU medicine after two years for Stern, then IB because everyone wanted IB (~2 years), then Caber — unmanned retail in 2017 when Amazon Go made fifty-plus clones. He says they were among the few left. 150 meetings that year; later 60-plus investors; a hundred-plus nos; ~six years; ~¥10 million-class checks and a 3.5亿 figure on the tape. Cockroach is the internal name. 2021 is when the next turn becomes visible on the file.",
            "Product: most people equate a general robot with Physical Intelligence being 'solved.' Lindon: product definition — a robot can be useful before intelligence is general. Diligence Dyna as a long fog, not a 2026 humanoid print. PI is the foil, not a customer. Do not mark AMZN on one Shanghai visit. He was 14 on the first game-account shop, two years in NYU medicine, then Stern and about two years of banking before Caber. Amazon Go in 2017 spawned fifty-plus clones; he says they were among the few left. Later 60-plus investors and a 千万-class check sit next to the 3.5亿 mark. 2021 is when the next turn becomes visible. Shanghai once or twice a year is the local-team cadence, not a China-pivot.",
        ],
        {
            "name": "Full-Stack Fog × Cockroach Raise × Useful Before AGI",
            "components": "Refuse US-brain / China-body. Keep research and落地 in one identity. Survive a hundred nos (2017 retail → Dyna). Useful beats general. Tesla and PI are the two compares: one stack, one brain-max. The identity fight is the long part of the 171 minutes: half the team wanted落地, half wanted research, and Lindon will not call money-scent and star-sea a split. Both Shanghai and the Valley feel noisy — clips and raises, no convergence. Caber in 2017 was the Amazon-Go copycat year with 150 meetings and a hundred-plus nos; cockroach is the internal name that survived ~six years and a 3.5亿-class mark. Product definition is the punchline: a robot can be useful before intelligence is general. Physical Intelligence is the foil that waits for AGI in the body; Amazon Go is the foil that already shipped a store.",
            "application": "Private:Dyna is a fog-route private. PI is the general-intelligence foil. AMZN is the 2017 Go / Caber foil. Do not buy a 2026 robot week.",
        },
        [
            {"view": "Full-stack is the third party.", "question": "Brain or body?", "answer": "US waits on the body; China waits on the brain. Dyna wants both. That split is the identity fight."},
            {"view": "Cockroaches take a hundred nos.", "question": "What did Caber teach?", "answer": "2017 Amazon-Go clones. 150 VCs. Six years. ¥350 million-class mark. Same refusal muscle."},
            {"view": "Useful before general.", "question": "What about Physical Intelligence?", "answer": "He will not wait for AGI in the body. Tesla is the other stack that agrees."},
        ],
        [
            {"ticker": "Private:Dyna", "direction": "Long", "confidence": "Low", "thesis": "Full-stack fog after a hundred-nos retail life; not a 2026 humanoid print — low"},
            {"ticker": "AMZN", "direction": "Long", "confidence": "Low", "thesis": "Amazon Go year is the Caber foil on this tape, not a robot multiple — low"},
        ],
        {"subject": "Dyna · Caber · brain vs body", "events": [
            {"date": "age 11–14", "event": "US; first game-account shop"},
            {"date": "2010s", "event": "NYU medicine → Stern → ~2 years IB"},
            {"date": "2017", "event": "Caber / Amazon Go year; 150 VCs"},
            {"date": "2017–23", "event": "~six years, 100+ nos, cockroach line"},
            {"date": "2021", "event": "Next-turn visibility on the tape"},
            {"date": "2026-10-15", "event": "E154 publishes"},
        ]},
        "154. 对Dyna创始人Lindon的3小时访谈：机器人世界的迷雾、分歧与抉择",
        "Lindon Gao", "Dyna Robotics 创始人兼CEO",
        "张小珺用171分钟问Lindon。美国赌大脑等身体，中国赌供应链等大脑。Dyna自称全站——原型研究，不是演示周。Lindon：中国出生，11岁去美国，14岁卖游戏账号，纽大医学两年再Stern，投行大约两年，2017年Caber无人零售（Amazon Go仿品年，见150个VC，后来60多个，被拒一百多次，「我们是蟑螂」），大约六年、口播3.5亿量级。团队裂过：落地对研究。闻得到钱和星辰大海是一条路。Physical Intelligence是「身体里的通用智能」对照——他说好用的机器人不必先通用。亚马逊Go是2017年Caber对照。",
        "E154，10月15日。Lindon一年回上海一两次（有本地团队）。太平洋两边都吵：发布、融资、不收敛。标题里的《沉思录》/阳明在可听文件里变成身份和路线。",
        [
            "路线：只赌大脑（美国）对只赌身体（中国）。Dyna不选边。原型研究是地图有雾仍交出一栈。带子上的身份危机：一半要落地，一半要研究。Lindon：闻钱是活；梦想是海。他不把这两句当打架。上海和谷都浮躁——每家丢片段、都在融。",
            "创始人钟：14岁游戏市场，网站卖掉。父母由他从纽大医学两年转到Stern，再因人人都去投行去了大约两年，然后Caber——2017年Amazon Go带出五十多家仿品。他说他们是少有的还活着的。那年150个会面；后来60多个投资人；一百多次不；大约六年；千万级支票和口播3.5亿。蟑螂是队内名字。2021年是档案上下一转看得见的年份。",
            "产品：多数人把通用机器人写成Physical Intelligence已经「解决」。Lindon：产品定义——智能未通用也可以好用。亚马逊Go是2017年Caber对照。把Dyna当长雾尽调，不当2026人形打印。PI是对照不是客户。不要用一次上海访问去标AMZN。",
        ],
        {"name": "全站迷雾 × 蟑螂融资 × 好用先于通用", "components": "拒绝美国大脑/中国身体。研究和落地放在一个身份里。活过一百次不（2017零售→Dyna）。好用压过通用。亚马逊Go和PI是两个比较：零售雾，一脑。", "application": "Private:Dyna是雾路私募。PI是通用智能对照。AMZN是2017年Caber对照。不要买2026机器人周。"},
        [
            {"view": "全站是第三方。", "question": "大脑还是身体？", "answer": "美国等身体；中国等大脑。Dyna两个都要。这个分裂就是身份架。"},
            {"view": "蟑螂吃得下一百次不。", "question": "Caber教了什么？", "answer": "2017年Amazon Go仿品。150个VC。六年。3.5亿量级。同一块拒绝肌。"},
            {"view": "好用先于通用。", "question": "Physical Intelligence呢？", "answer": "他不等身体里的AGI。特斯拉是另一个同意的栈。"},
        ],
    )


def ep155():
    zj(
        "zj-ep155", 155,
        "Qian Cheng / Ecovacs: Father, Son, and a Farming-Civilization Robot Shop",
        "Qian Cheng (David)", "CEO, Ecovacs; second generation",
        "2026-10-21", 120,
        "https://www.youtube.com/watch?v=86wFCPat2GY",
        "https://www.youtube.com/watch?v=vhKLKoKhI0s",
        "https://www.xiaoyuzhoufm.com/episode/6ad4dacd641ef406308d86e5",
        ["603486.SH", "Private:Dyna", "TSLA"],
        ["农耕文明", "最年轻", "1990年"],
        (
            "Zhang Xiaojun sits with Ecovacs CEO Qian Cheng — born 1990 in Shenzhen, once the youngest "
            "A-share CEO, second generation. Eleven years Shenzhen, eleven Canada, back at 22 in 2012 "
            "when the shop already sold robot vacs and his father texted teens-to-twenties of units a "
            "day. He calls it a farming civilization: plant, wait — not a nomad bite. Tesla Model S / "
            "FSD is his caution on features that do not land. Dyna is last week's fog guest, not this "
            "P&L. He will not date a clean 'I came back to take over.'"
        ),
        (
            "E155, Oct 21, 120 minutes. Father: Nanjing University, Shantou teaching, Hainan, Shenzhen "
            "SOE then trade, Suzhou factory (T1K/TED-K). Xiaojun wants the succession mix of father/son "
            "and boss/report — not a clean founder myth. Qian is David to the staff, oat-bowl, red-eye "
            "dog avatar. Tesla Model S / FSD is his caution on features that do not land; Dyna is last "
            "week's fog guest. Whisper: 钱程/科沃斯 as 前程/科物资; quotes below are the audible strings."
        ),
        [
            "Clock: 1990 Shenzhen, 11 to Canada, 08–12 university, 2012 into the company already selling robot vacs. Father's SMS: a dozen or twenty units a day, province by province. He had summer looks at the floor and no App-startup conversion in the mobile-internet boom. Succession is 'hard to say I came back in order to take over' — walk, then the chair. Youngest A-share CEO is the press line; the tape is a man who found the job an epic mis-set of 'peak life.'",
            "Culture: farming not nomad. Plant, wait for grain; do not bite a huge category because it is huge. That is how he splits from 90s founders who own the baby. Desire had to be lit by the environment — he had enough, so he did not need to kill. Red-eye dog and oat bowl are the personal props. Internal, he still talks like an operator, not a capital-market second gen.",
            "Compares: Tesla is the other home-robot / household machine. Dyna (E154) is research-fog, not a listed vac P&L. Diligence 603486.SH as a planted-field compounder that already had a selling robot in 2012, not as a humanoid week. The father-to-son file is the reason Xiaojun booked the hour — mix of filial and line-manager, not a clean founder myth. University was 2008–12, mobile-internet peak, and he still did not start an app shop. Canada began with ten dictionary words a day. Tesla Model S with FSD on a ten-year-old car is his caution: a feature can be sold for a decade and still not land in daily use — China robotaxi talk gets the same shrug. T1K/TED-K is the pre-listing name. Oat bowl and the red-eye dog are the personal props for wolfishness he says he lacked.",
        ],
        {
            "name": "Farming Shop × Unchosen Chair × Already-Selling 2012",
            "components": "Eleven-year thirds: Shenzhen, Canada, Suzhou. 2012 vacs already on the SMS. Farming versus nomad. Desire borrowed from the room. Youngest-CEO headline versus 'I did not plan the takeover.' Tesla and Dyna are two other robot files, not this P&L. Qian will not date the takeover. 2012 he walked into a company already texting teens-to-twenties of vacs a day; youngest A-share CEO was the press line, not a 20-year plan. Farming versus nomad is how he splits from 90s founders who own the baby — Wang Xinxin / JK is 'their kid, my brother.' Desire had to be lit by the room; he had enough, so he did not need to kill. Tesla Model S with FSD on a ten-year-old car is his caution that a feature can be sold and still not land. Dyna is last week's research fog, not this listed vac P&L.",
            "application": "603486.SH is the planted A-share. Dyna is last week's private fog. TSLA is household machines, not Ecovacs. Diligence the 2012 selling floor, not a 90s founder myth.",
        },
        [
            {"view": "The chair was not a 20-year plan.", "question": "When did he decide to take over?", "answer": "He will not date it. 2012 he walked into a company already selling vacs. Youngest CEO was the press, not the plan."},
            {"view": "Farming, not a bite of the category.", "question": "How is he not Wang Xinxin?", "answer": "Founders own the baby. He calls this a brother. Plant and wait."},
            {"view": "2012 already had a robot SKU.", "question": "What did the father text?", "answer": "Teens to twenties of units a day. That is the compounder, not a 2026 humanoid."},
        ],
        [
            {"ticker": "603486.SH", "direction": "Long", "confidence": "Low", "thesis": "2012 already selling vacs; farming-civilization operator, not a humanoid week — low"},
            {"ticker": "TSLA", "direction": "Long", "confidence": "Low", "thesis": "The other household-machine file on a succession tape — low"},
        ],
        {"subject": "Ecovacs · succession · 2012 vacs", "events": [
            {"date": "1990", "event": "Born Shenzhen"},
            {"date": "2001", "event": "Canada at 11"},
            {"date": "2008–12", "event": "University; father already selling robot vacs"},
            {"date": "2012", "event": "Joins; SMS of teens–twenties units/day"},
            {"date": "2010s", "event": "Youngest A-share CEO line"},
            {"date": "2026-10-21", "event": "E155 publishes"},
        ]},
        "155. 和科沃斯钱程聊，父与子、企二代接班的样本与肌理、机器人",
        "钱程", "科沃斯 CEO / 企二代",
        "张小珺采访科沃斯CEO钱程——1990年深圳生，一度最年轻的A股CEO，二代。深圳11年、加拿大11年（父亲让他每天从字典背十个词），22岁2012年回来，公司已经在卖扫地机器人，父亲短信里一天十几二十台。上市前叫T1K/TED-K。他把店写成农耕文明：埋种子等粮，不是游牧咬一口。燕麦碗，狗头像眼睛改成发光红提醒狼性——他说自己原来没有。王欣欣/JK是创始人能量对照：「那是他们的孩子，这是我兄弟。」特斯拉是另一个家庭机器人故事；Dyna是上周雾路客人，不是同一张利润表。他不会给「回来就是为了接班」一个干净日期。",
        "E155，10月21日。父亲：南大、汕头教书、海南、深圳国企再贸易、苏州办厂。小珺要的是父子加上下级混在一起的交接。Whisper把钱程/科沃斯听成前程/科物资。",
        [
            "时钟：1990深圳，11岁加拿大，08–12大学，2012年进已经在卖扫地机的公司。父亲短信：一天十几或二十台，一省一省报。他暑假看过车间，移动互联网风口没做成App创业。接班是「很难说回来就是为了接」——先走，再坐椅子。最年轻A股CEO是新闻稿；带子是一个发现当CEO绝不是人生巅峰的人。",
            "文化：农耕不是游牧。种下去等粮；不因为品类大就咬一口。这是他和拥有孩子的90后创始人的分法。欲望要靠环境点燃——他拥有的已经多，所以不必去杀。红眼狗和燕麦碗是个人道具。对内他仍像经营者，不像资本市场二代。",
            "比较：特斯拉是另一个家里的机器。Dyna（E154）是研究雾，不是上市扫地机利润表。把603486.SH当2012年已经在卖的田，不当人形周。父到子档案才是小珺约这小时的原因——孝和直线经理混在一起，不是干净创始人神话。",
        ],
        {"name": "农耕店 × 不是自己选的椅子 × 2012年已经在卖", "components": "三等分：深圳、加拿大、苏州。2012年短信里已经有扫地机。农耕对游牧。欲望从房间里借。最年轻CEO标题对上「我没规划接班」。特斯拉和Dyna是另外两份机器人档案，不是这张利润表。", "application": "603486.SH是种下的A股。Dyna是上周私募雾。TSLA是家庭机器不是科沃斯。尽调2012年的销售车间，不要尽调90后创始神话。"},
        [
            {"view": "椅子不是20年计划。", "question": "他什么时候决定接？", "answer": "他不会给日期。2012年走进已经在卖机的公司。最年轻CEO是新闻不是计划。"},
            {"view": "农耕，不是咬一口品类。", "question": "和王欣欣有何不同？", "answer": "创始人拥有孩子。他叫这兄弟。种了等。"},
            {"view": "2012年已经有机器人SKU。", "question": "父亲短信写什么？", "answer": "一天十几到二十台。那才是复利，不是2026人形。"},
        ],
    )


def main():
    ep203()
    ep204()
    ep205()
    ep206()
    ep154()
    ep155()


if __name__ == "__main__":
    main()
