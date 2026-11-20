#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Bilingual SV101 E258."""
from __future__ import annotations

import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))
from scripts._window_lib import dump, en_std, validate_file  # noqa: E402
from src.chinese_transcript import load_transcript_body, quote_supported_in_transcript, transcript_path  # noqa: E402

EID = "sv101-ep258"
QUOTES = ["每期招收10家企业一年三期", "100万美元的支票", "在模型的价格上加5%"]


def main():
    body = load_transcript_body(transcript_path(EID))
    for q in QUOTES:
        print(EID, "OK" if quote_supported_in_transcript(q, body) else "FAIL", q)
        if not quote_supported_in_transcript(q, body):
            raise SystemExit(q)
    meta = {
        "episode_number": 258,
        "title": "HF0 and the Early OpenRouter Story",
        "guest": "Guo Jing (Joe)",
        "guest_role": "Founder and CEO, ACE Studio",
        "date": "2026-11-09",
        "duration_minutes": 54,
        "youtube_url": "https://www.youtube.com/watch?v=3K7IWJAnOE8",
        "links": {
            "youtube": "https://www.youtube.com/watch?v=3K7IWJAnOE8",
            "apple_podcasts": "https://podcasts.apple.com/cn/podcast/id1498541229",
            "fireside": "https://sv101.fireside.fm/272",
            "xiaoyuzhou": "https://www.xiaoyuzhoufm.com/podcast/5e5c52c9418a84a04625e6cc",
        },
    }
    concl = (
        "Hongjun asks why founders would take HF0 over Y Combinator. Joe, who runs "
        "ACE Studio, a voice model for working musicians, was in the fall 2024 batch. "
        "HF0 takes 10 companies, three times a year, and has them live together for "
        "three months. His batch was $1 million for 5%. YC, as he hears it, is a "
        "couple hundred teams and a spray. OpenRouter, a year earlier, was four people. "
        "It adds 5% to the model price and became the door for trying a new model. "
        "ACE roughly did a 10x by treating growth as a product, not a trick."
    )
    bg = (
        "E258, Nov 9, about 54 minutes. Hongjun opens on the San Francisco house where "
        "founders eat and live together. The guest is Joe of ACE Studio. Users he names "
        "include Hans Zimmer and Teddy Riley. Whisper turns HF0 into HFZero and the "
        "host into 红军. YouTube captions were off, so this is a small-model transcript."
    )
    facts = [
        (
            "The house versus the spray. HF0 admits 10 companies a batch and runs 3 "
            "batches a year. They prefer repeat founders. Hongjun's compare is YC at "
            "about 200 companies a batch and 4 batches a year. Joe has not been to YC. "
            "He still says a founder holding both offers picks HF0 without hesitating. "
            "YC is a brand and, in his joke, spray and pray: water everyone and hope "
            "someone grows. HF0 is selective, the acceptance rate is far below YC, and "
            "the work is living and working in one place for 3 months. The term moved "
            "as the program got hotter. Early checks were $250,000 for 2.5%. The batch "
            "before ACE was $625,000 for 3%. ACE's fall 2024 batch was $1 million for "
            "5%. Investors had told Hongjun that clever people in one house for 3 months "
            "produce new ideas, and that some companies 10x inside those months."
        ),
        (
            "OpenRouter, one year ahead. Joe places OpenRouter in the fall 2023 batch, "
            "12 months before ACE. Two cofounders then. Hongjun's other figure is 4 "
            "people, 2 of them part-time, when it entered. The host had heard a "
            "multi-billion-dollar sale. On the tape the guest's next line is that the "
            "recent story is not a Stripe acquisition. What they do describe is the "
            "product. OpenRouter wanted to be the router across models: faster, more "
            "stable, more models. The first-mover spot became the place global "
            "developers test a new model, and the call-count chart became an authority. "
            "Labs then asked to be listed, instead of OpenRouter begging them. They did "
            "not push commercialization or a fundraise once that slot was clear. The "
            "price is the model price plus 5%. They do not run the China-style spread "
            "of buying at 30% and selling at 50%. New model releases are their growth, "
            "not a weekly influencer trick. Joe says that is a different growth from ACE."
        ),
        (
            "Growth as a product, not a trick. ACE makes a voice model for working "
            "musicians. Joe names Hans Zimmer, Teddy Riley, and other Grammy-level "
            "users. Inside the house the question every week is the growth number. Some "
            "weeks he had to stand up and say there was no growth while everyone else "
            "had some. A 10% week and a 50% week both showed up. Small tricks, including "
            "influencer growth that other teams were famous for, do not hold a stable "
            "curve. He came in ignorant of growth and left with other people asking ACE "
            "to teach it. The line he keeps is to build growth the way you build a "
            "product, or the way you build an algorithm. Hongjun had wanted the "
            "management lesson for AI companies: which HF0 habits travel after the "
            "batch. Joe's answer is the weekly number, the refusal to blame everything "
            "on growth, and the 10x the batch actually printed for them. OpenRouter is "
            "the exception he sets aside, because a router can grow when a new model "
            "ships even if the team does little that week."
        ),
    ]
    mental = {
        "name": "Ten-Company House × 5% Check × Growth as a Product",
        "components": (
            "10 companies, 3 batches a year, 3 months in one house. YC is the spray: "
            "about 200 a batch. The check went from $250,000 for 2.5% to $625,000 for "
            "3% to $1 million for 5%. OpenRouter, fall 2023, four people, takes 5% on "
            "the token price and became the test door for new models. ACE, fall 2024, "
            "treats weekly growth as a product. Tricks do not hold. A week of zero is "
            "part of the room. A sale rumor from the host is not the operating fact on the tape. That is the tell."
        ),
        "application": (
            "Private:HF0 is the program, not a stock. Private:OpenRouter is the router "
            "that charges 5% and does not discount its way in. Private:ACE Studio is "
            "the music-voice company that 10x'd inside the house. Do not underwrite a "
            "Stripe price. Underwrite whether the growth survives the week the trick stops."
        ),
    }
    insights = [
        {"view": "Founders pick the small house.", "question": "Why HF0 over YC?", "answer": "Joe says they do not hesitate. YC is a brand and a spray of about 200 teams. HF0 is 10 teams living together, and the acceptance rate is far lower."},
        {"view": "The check got more expensive as the program worked.", "question": "What did ACE give up?", "answer": "Early batches were $250,000 for 2.5%, then $625,000 for 3%. His fall 2024 batch was $1 million for 5%."},
        {"view": "OpenRouter grows when a model ships. ACE had to build the week.", "question": "What is the 5%?", "answer": "OpenRouter adds 5% to the model price and does not run a discount spread. It became the first door for testing a new model. The ACE 10x was the house, not that router math."},
    ]
    invest = [
        {"ticker": "Private:OpenRouter", "direction": "Long", "confidence": "Low", "thesis": "5% on the token price, first test door for new models, fall 2023 HF0 batch at four people — low"},
        {"ticker": "Private:HF0", "direction": "Long", "confidence": "Low", "thesis": "10 companies, 3 months, $1 million for 5% on the latest batch, founders take it over YC — low"},
        {"ticker": "Private:ACE Studio", "direction": "Long", "confidence": "Low", "thesis": "Voice model for working musicians, about a 10x inside the fall 2024 house — low"},
    ]
    quotes = QUOTES
    chrono = {"subject": "HF0 · OpenRouter · ACE Studio", "events": [
        {"date": "early", "event": "HF0 checks at $250,000 for 2.5%"},
        {"date": "2023-fall", "event": "OpenRouter batch, about four people, two part-time"},
        {"date": "2024", "event": "Prior batch at $625,000 for 3%"},
        {"date": "2024-fall", "event": "ACE Studio batch, $1 million for 5%, about a 10x"},
        {"date": "2026", "event": "Host hears a large sale rumor; guest says it is not Stripe"},
        {"date": "2026-11-09", "event": "E258 publishes"},
    ]}
    en = en_std(EID, "Silicon Valley 101", "Hongjun", meta, 3,
                ["Private:HF0", "Private:OpenRouter", "Private:ACE Studio"],
                concl, bg, facts, mental, insights, invest, quotes, chrono,
                "| v4.10 window SV101 E258", "whisper-small")
    zh_meta = dict(meta)
    zh_meta.update(
        title="E258｜聊聊硅谷创业“修道院”HF0与OpenRouter早期故事",
        guest="郭靖（Joe）",
        guest_role="ACE Studio 创始人兼 CEO",
    )
    zh = dict(en)
    zh.update({
        "podcast": "硅谷101", "host": "泓君", "metadata": zh_meta,
        "conclusion": "泓君问创始人为什么宁可去HF0也不去YC。ACE Studio的Joe做音乐人用的声音模型，2024年秋批次。HF0一期10家，一年三期，一起住三个月。他那期的支票是100万美元换5%。更早是25万美元换2.5%，上一期是62.5万美元换3%。他听到的YC是一两百家、洒水再祈祷。OpenRouter早一整年，2023年秋，进去时大约四个人、两个兼职。它在模型价格上加5%，成了开发者试新模型的第一扇门。增长小技巧留不住ACE。把增长当成产品才留下。他说这个批次大概让他们涨了10倍。",
        "background": "E258，11月9日，大约54分钟。泓君从旧金山那栋一起吃住的房子讲起。嘉宾是ACE Studio的Joe。他点名的用户包括汉斯·季默和Teddy Riley。Whisper把HF0听成HFZero，把泓君听成红军。YouTube没有字幕，这是小模型转写。",
        "important_facts": [
            "小房子对洒水。HF0一期收10家，一年3期，偏连续创业者。泓君的对照是YC一期大约200家、一年4期。Joe没去过YC。他还是说两张offer都在的时候，创始人会毫不犹豫选HF0。YC是品牌，他开玩笑叫spray and pray：全都洒上，祈祷有人成。HF0更挑，入选率远低于YC，工作是在一个地方住三个月、一起做。条款随着项目变热在涨。早期25万美元换2.5%。ACE的上一期是62.5万美元换3%。2024年秋ACE这期是100万美元换5%。投资人跟泓君说过，聪明人住在一起三个月会冒出新想法，也有公司在这三个月里涨10倍。",
            "OpenRouter早一年。Joe把它放在2023年秋，比ACE早12个月。当时两个联合创始人。泓君的另一个数字是进去时4个人，其中2个兼职。主持人听到过一笔几十亿美元的出售传闻。带子上嘉宾紧接着的一句是，最近并不是Stripe收购。他们讲清楚的是产品。OpenRouter要做跨模型的路由器：更快、更稳、更多模型。先发位置变成全球开发者试新模型的第一入口，调用次数的榜有了权威。后来是实验室求着上，不是他们求实验室。这个卡位清楚之后，他们没有猛推商业化，也没有猛融资。价格是模型价再加5%。他们不做中国这边常见的三折进、五折出的差价。新模型发布才是他们的增长，不是每周的网红技巧。Joe说这和ACE的增长不是同一种。",
            "增长是产品，不是技巧。ACE做给在职音乐人的声音模型。Joe点名汉斯·季默、Teddy Riley和其他格莱美级别用户。房子里每周的问题是增长数字。有的星期他要站起来说没增长，别人都有。10%的一周和50%的一周都出现过。小技巧，包括别的队很出名的网红增长，撑不住一条稳定曲线。他进去时不懂增长，出来后有人请ACE去讲。他留下的一句是：像做产品一样做增长，或者像做算法一样做增长。泓君想要的是AI公司能带走的管理习惯。Joe的答案是每周那个数字，不要把所有问题都算成增长，以及这个批次给他们打下的大约10倍。OpenRouter被他拿开，因为新模型一发，路由器即使那周没做什么也会涨。",
        ],
        "mental_model": {
            "name": "十家的房子 × 5%的支票 × 把增长当产品",
            "components": "一期10家，一年3期，同住3个月。YC是洒水：一期大约200家。支票从25万美元换2.5%，到62.5万美元换3%，再到100万美元换5%。OpenRouter是2023年秋，大约四个人，在token价格上加5%，成了新模型的测试门。ACE是2024年秋，把每周增长当成产品。技巧留不住。零增长的一周也是房间的一部分。主持人的出售传闻不是带子上的经营事实。",
            "application": "Private:HF0是项目，不是股票。Private:OpenRouter是收5%、不靠打折挤进去的路由器。Private:ACE Studio是在房子里大约涨了10倍的音乐声音公司。不要去标一个Stripe的价格。要看技巧停了以后增长还在不在。",
        },
        "key_insights": [
            {"view": "创始人选小房子。", "question": "为什么是HF0不是YC？", "answer": "Joe说他们不会犹豫。YC是品牌，一期大约200个队的洒水。HF0是10个队住在一起，入选率低得多。"},
            {"view": "项目越有效，支票越贵。", "question": "ACE让出了什么？", "answer": "早期25万美元换2.5%，然后62.5万美元换3%。他2024年秋那期是100万美元换5%。"},
            {"view": "OpenRouter靠新模型涨。ACE得把那一周做出来。", "question": "5%是什么？", "answer": "OpenRouter在模型价格上加5%，不打价格战。它成了试新模型的第一扇门。ACE的10倍是这栋房子，不是那套路由器数学。"},
        ],
        "golden_quotes": QUOTES,
        "review_notes": "| v4.10 window 硅谷101 E258",
    })
    dump(ROOT / f"data/approved/{EID}.json", en)
    dump(ROOT / f"data/approved/zh/{EID}.json", zh)
    validate_file(ROOT / f"data/approved/{EID}.json")


if __name__ == "__main__":
    main()
