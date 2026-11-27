#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Bilingual ZJ E158. 202 minutes, over_180 tier."""
from __future__ import annotations

import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))
from scripts._window_lib import dump, en_std, validate_file  # noqa: E402
from src.chinese_transcript import load_transcript_body, quote_supported_in_transcript, transcript_path  # noqa: E402

APPLE = "https://podcasts.apple.com/cn/podcast/id1634356920"
XYZ = "https://www.xiaoyuzhoufm.com/episode/6b05746801b0ab432eddab62"


def main():
    eid = "zj-ep158"
    quotes = [
        "我觉得最近两周的硅谷的氛围其实是挺悲观的",
        "我觉得XI最大的问题就是它没有自己稳定的站位方向",
        "每年依然能够有上百亿的收入",
    ]
    body = load_transcript_body(transcript_path(eid))
    for q in quotes:
        ok = quote_supported_in_transcript(q, body)
        print(eid, "OK" if ok else "FAIL", q)
        if not ok:
            raise SystemExit(q)
    meta = {
        "episode_number": 158,
        "title": "2026 Recap with Shen Yikang — xAI, RSI, and a White-Box Pretrain",
        "guest": "Shen Yikang",
        "guest_role": "Founder-CEO, Learning Machine; former xAI pretraining",
        "date": "2026-11-24",
        "duration_minutes": 202,
        "youtube_url": "",
        "links": {"apple_podcasts": APPLE, "xiaoyuzhou": XYZ},
    }
    concl = (
        "Shen Yikang recaps 2026 from inside the training stack. The week of this "
        "taping, Silicon Valley felt pessimistic: Anthropic listing talk had moved "
        "from about 2 trillion to about 1.3 trillion, and Jensen Huang was, on that "
        "tape, out. xAI can stand up a few hundred thousand GB-class GPUs in months "
        "and, he says, can clear more than 10 billion a year as a cloud even if the "
        "model is not first. The failure is direction. RSI today is a linear 10 to "
        "20 percent. A new "
        "capability is the unsolved half. Learning Machine is the continual-learning bet."
    )
    bg = (
        "E158, Nov 24, about 202 minutes. Zhang Xiaojun with Shen Yikang, founder-CEO "
        "of Learning Machine and a former xAI pretraining researcher who joined in "
        "early 2025. Before that he led a pretraining team at a lab Whisper renders "
        "as APPM and does not expand. A Montreal PhD from 2016, architectures from "
        "LSTM to the transformer, and a tape credit for an ICLR 2019 best paper. "
        "Whisper hears Shen Yikang as Shen Yikang-variant, Grok as Glock, Muon as "
        "Mewang, and DeltaNet as Dark Knight. The hour was taped the week the show "
        "was treating Jensen Huang as out. The day before publish he was said to be "
        "back, and they kept the earlier tape. That sequence is the episode account. "
        "At IBM he worked with MIT on gated linear attention and DeltaNet. He says a "
        "recent Kimi model combines those two. The papers he ranks are the transformer, "
        "GPT-style in-context learning and scaling, RLHF or SFT, and chain-of-thought. "
        "He calls language the key to intelligence."
    )
    facts = [
        (
            "The week felt like a bubble argument. Shen calls the Silicon Valley mood "
            "pessimistic. Anthropic, he says, went from listing talk near 2 trillion "
            "to about 1.4 trillion and then about 1.3 trillion. New labs were still "
            "raising at hundreds of millions and at tens of billions, series A or "
            "series C, which he sets next to the hottest stretch of the internet "
            "bubble. His own round is money already sitting with VCs, so a short shock "
            "does not pull it. He puts the cleanup from year-end into next year, and "
            "possibly one to two years, while the technology itself still looks to him "
            "like it is moving. The complaint he hears about Huang is the GPU price, "
            "which he treats as demand. He puts the next stretch at about 50 percent "
            "either way, and says the shock has not yet changed how the industry works. "
            "He wants the chip supply, and the financing around it, not to break."
        ),
        (
            "xAI was not short of money or people. Grok 1, Grok 2, and Grok 3 scaled "
            "up. The cluster moved from H100 to GB200 to large GB300 deployments. A "
            "few hundred thousand cards can be stood up in months. He calls the lab "
            "one of the largest buyers of the GB series, with a large share of that "
            "capacity. Even if the model is not the winner, xAI or SpaceX as a cloud "
            "vendor can still clear more than 10 billion a year. The tape does not "
            "name the currency. The failure is the digit in front. Engineering speed "
            "and talent density are the zeros. Without one stable direction, each area "
            "ends a step behind the first tier, and the early spend is hard to justify. "
            "A rocket wreck can be collected and read. A model is right or wrong only "
            "after users show up. The leftover path, if you are not the frontier, is "
            "to distill behavior off a frontier model."
        ),
        (
            "RSI, as he defines it, is GPT-4 training GPT-5 with no person in the loop. "
            "A 10 percent faster kernel, a 10 percent better optimizer, cleaner data, "
            "and new synthetic data add up to a 10 to 20 percent gain from one "
            "generation to the next. That linear gain is what exists now, including a "
            "coding score moving from 50 to 70. Inventing a capability the last model "
            "did not have, such as chain-of-thought, is the unsolved half. Infra moved "
            "first because token throughput is one number. A small pretrain can iterate "
            "in minutes to an hour. Post-training is slower because the benchmarks do "
            "not agree. A startup that runs the loop on Claude may be improving Claude. "
            "Continual learning is related and is not a subset. After deployment, task "
            "A is slow, B is faster, C is direct, and D falls from a slow pass to a "
            "fast one. Frontier RSI shops are not, on what he has seen, slower than "
            "the new labs. That comparison still needs a test."
        ),
    ]
    mental = {
        "name": "One direction × linear RSI × a private front door",
        "components": (
            "Separate the cluster from the research bet. A few hundred thousand GB "
            "cards in months, and a cloud that can clear more than 10 billion a year, "
            "are a survival plan even when the model is not first. They do not pick "
            "the next capability. User data is slower than the 2023 story. It does not "
            "open a gap in one release. It tells a lab which problem to train for, "
            "repo-level work versus a single change, and that hint is why a coding "
            "share matters. RSI that only climbs an existing score, 10 percent on a "
            "kernel or 20 points on a coding test, is a tool the frontier labs already "
            "run. A new idea, a training trick the last model could not express, is "
            "the bar he does not think anyone has cleared. Continual learning sits "
            "beside that bar. The model keeps the domain after it is shipped, so the "
            "fourth task in a family no longer needs a long search. A white box, in "
            "this telling, is the shape of the update, not a caption on every neuron. "
            "Muon pulls large destructive steps down and small patterns up, which also "
            "covers a data mix that was never balanced. The product picture is a "
            "personal agent as the front door and a specialist model inside each firm. "
            "The legal file goes out as a packet. The private history stays put. "
            "Anthropic, once it found coding and held most of that market, is his "
            "example of a lab that can see the next training choice instead of guessing. "
            "A small lab does not get a free pass on RSI just by being new. What it "
            "can own is the memory after shipping, because that asks for a different "
            "pretrain and post-train design from the first day."
        ),
        "application": (
            "NVDA is the supply he does not want broken, and the price is the complaint "
            "he will live with. Private:xAI is the cluster and the cloud cash, under "
            "a direction that has not stayed still. Private:Anthropic is the coding "
            "loop that actually collects users, while the listing number on this tape "
            "fell from about 2 trillion toward about 1.3. Learning Machine is the "
            "continual-learning company, not a mark on those three."
        ),
    }
    insights = [
        {
            "view": "The zeros do not save a missing one.",
            "question": "Why did a rich xAI pretrain still miss the first tier?",
            "answer": (
                "People, speed, and GPUs were there. Grok moved from the first model "
                "to the third. Cards moved from H100 to GB200 to GB300, and a few "
                "hundred thousand can arrive in months. He still says each area finished "
                "a step behind, because the lab did not stay on one direction long "
                "enough for the spend to compound. A rocket team can read a wreck. A "
                "model team learns from users it does not have unless it is already "
                "in front. Distilling a frontier model is what remains. More than 10 billion "
                "a year of cloud revenue, currency unnamed, can keep the firm alive and "
                "still leave every research area a step behind. Standing the cards up is a few "
                "months of work. Choosing what those cards should learn, and staying with "
                "that choice, is the part the lab did not bank. He is explicit about the gap."
            ),
        },
        {
            "view": "Linear RSI is not a new capability.",
            "question": "What would count as RSI actually working?",
            "answer": (
                "Using GPT-4 to train GPT-5 with no person in the loop, for a 10 percent "
                "faster kernel or a cleaner dataset, is the linear version, and a 10 "
                "to 20 percent generation gain is the result he says labs already get. "
                "A coding score from 50 to 70 is the same kind of climb. The flag he "
                "wants is a capability the previous model did not have, found by the "
                "agent rather than specified by a researcher. Infra got there first "
                "because throughput is one score. Post-training has too many scores. "
                "A loop that calls Claude may be teaching Claude."
            ),
        },
        {
            "view": "The agent should be a door, not the whole building.",
            "question": "What does decentralized AI mean on this tape?",
            "answer": (
                "Each person holds a model that knows them and does not leak. Each "
                "firm holds a model with its own files. The personal agent routes a "
                "job, the way a search box routes a query to a site it does not own. "
                "A legal packet goes to a legal model and comes back done. Phone chips "
                "and a laptop that is not always open are limits, so this is not a "
                "promise that the model lives on the device. The white-box claim is "
                "narrower too. He can describe the update, including a Muon step that "
                "evens lengths across directions. He does not claim a name for every "
                "neuron. Learning rate driven all the way to zero is also not the "
                "checkpoint he trusts, because the last steps overfit."
            ),
        },
    ]
    invest = [
        {
            "ticker": "NVDA",
            "company": "Nvidia",
            "direction": "Long",
            "confidence": "Low",
            "thesis": "Chip supply he does not want broken; the complaint is price — low",
            "rationale": (
                "Everyone still needs the GPUs. The gripe he hears is that they got "
                "expensive, which he reads as demand. The resignation week is the "
                "episode account, and he hopes the supply and the financing around it hold."
            ),
        },
        {
            "ticker": "Private:xAI",
            "company": "xAI",
            "direction": "Long",
            "confidence": "Low",
            "thesis": "A GB cluster and cloud cash above 10 billion, if one direction holds — low",
            "rationale": (
                "Hundreds of thousands of cards in months, a large share of GB supply, "
                "and a cloud that can clear more than 10 billion a year even if the "
                "model is not first. The research bet fails when the direction moves."
            ),
        },
        {
            "ticker": "Private:Anthropic",
            "company": "Anthropic",
            "direction": "Long",
            "confidence": "Low",
            "thesis": "Coding share that collects a real user loop, as the listing talk fell — low",
            "rationale": (
                "Finding coding and keeping most of that market is how a lab gets the "
                "feedback a model needs. On this tape the listing talk moved from about "
                "2 trillion to about 1.3 trillion. He treats that as caution, not a break "
                "in the technical case."
            ),
        },
    ]
    chrono = {
        "subject": "Shen Yikang · xAI pretrain · Learning Machine",
        "events": [
            {"date": "2016", "event": "Starts architecture research in a Montreal PhD"},
            {"date": "2019", "event": "Tape credits an ICLR best paper"},
            {"date": "2025-01", "event": "Joins xAI pretraining, architecture and scaling"},
            {"date": "2026", "event": "Founder-CEO of Learning Machine, on continual learning"},
            {"date": "2026-11", "event": "Taping, the week the show treats Jensen Huang as out"},
            {"date": "2026-11-23", "event": "Day before publish, the show says he is back; the tape stays"},
            {"date": "2026-11-24", "event": "E158 publishes"},
        ],
    }
    en = en_std(
        eid, "Zhang Xiaojun Podcast", "Zhang Xiaojun", meta, 3,
        ["Private:xAI", "NVDA", "Private:Anthropic"],
        concl, bg, facts, mental, insights, invest, quotes, chrono,
        "| v4.10 window ZJ E158", "whisper-small",
    )
    zh_meta = dict(meta)
    zh_meta.update(
        title="E158 2026年复盘：和沈驿康聊黄仁勋、xAI、RSI、持续学习与预训练白盒",
        guest="沈驿康",
        guest_role="Learning Machine 创始人兼 CEO · 前 xAI 预训练",
    )
    zh = dict(en)
    zh.update({
        "podcast": "张小珺商业访谈录",
        "host": "张小珺",
        "metadata": zh_meta,
        "conclusion": (
            "沈驿康从训练栈里面复盘2026。这期录制的那一周，硅谷情绪悲观："
            "Anthropic上市说法从大约2万亿说到大约1.3万亿，节目里的黄仁勋当时是离开的。"
            "xAI可以在几个月里拉起几十万张GB卡。他说就算模型不是第一，做成云一年也能有上百亿收入。"
            "失败在方向。前面的1如果一直换，后面的0没有用。"
            "现在的RSI是线性的10%到20%。新能力还没人做出来。Learning Machine押的是持续学习。"
        ),
        "background": (
            "E158，11月24日，大约202分钟。张小珺对谈沈驿康，Learning Machine创始人兼CEO，"
            "2025年初加入xAI预训练，之前在一家Whisper听成APPM、没有展开的实验室负责整个预训练团队。"
            "2016年起在蒙特利尔读博做架构，从LSTM到transformer，节目里提到ICLR 2019的最佳论文。"
            "Whisper把沈驿康听成沈亿康，把Grok听成Glock，把Muon听成Mewang，把DeltaNet听成Dark Knight。"
            "节目录于节目所说黄仁勋离开后的一周。发布前一天他又回来了，他们把原来的录音留着。"
            "这是节目自己的时间线。"
        ),
        "important_facts": [
            "那一周像一场泡沫辩论。他说硅谷氛围挺悲观。Anthropic的上市说法从大约2万亿变成大约1.4万亿，再到大约1.3万亿。新实验室仍在以几亿到几十亿估值融A轮或C轮，他拿来和互联网泡沫最热的一段比。他自己要融的钱是已经在VC手里的资金，短震不会把它抽走。清理期他放到今年年底到明年，也可能一到两年，技术本身他仍然觉得在变快。对黄仁勋听到的抱怨是GPU越来越贵，他认为这是需求。他希望芯片供应和周围的融资环境不要断。",
            "xAI不缺钱，也不缺人。Grok从1到2到3，规模在涨。集群从H100到GB200，再到大规模GB300。几十万张卡可以在几个月里建起来。他说他们是GB系列最大的买家之一，很大一部分产能在这边。就算模型不成功，xAI或SpaceX做成云，一年仍可以有上百亿收入。带子没有说币种。问题是前面的那个1。工程速度和人才密度是后面的0。方向不稳定，每个领域都会差第一梯队一截，早期投入就很难解释。火箭炸了可以把碎片收回来读。模型对不对，要等用户用了才知道。不是frontier，剩下的路就是去蒸馏frontier模型的行为。",
            "他把RSI定义成用GPT-4训练GPT-5，人不再介入。内核快10%，优化器好10%，清掉脏数据，再自动造一批新方向的数据，加起来一代提升10%到20%。这是现在有的线性版本，包括coding从50分到70分。上一代没有的能力，比如在没有思维链的模型上做出思维链，是还没解决的那一半。Infra最先动，因为token吞吐量是一个数。小预训练几分钟到一小时就能迭代。后训练更慢，因为benchmark对不齐。用Claude把循环跑起来的创业公司，可能是在训练Claude。持续学习相关，但不是子集。部署之后，任务A很慢，B更快，C可以直接做，D从慢思考变成快反应。这是Learning Machine要做的。他看到的frontier实验室做RSI并不比新公司慢。这个比较还需要验证。",
        ],
        "mental_model": {
            "name": "一个方向 × 线性RSI × 私人前门",
            "components": "把集群和研究赌注分开。几个月几十万张GB卡，以及一年上百亿的云收入，是模型不是第一时的生存方案。它们不决定下一种能力。用户数据比2023年的故事慢。它不会在一个版本里拉开鸿沟。它告诉实验室下一步该练什么，是整个仓库还是一个改动。这就是coding份额有用的原因。只爬现有分数的RSI，内核快10%或者coding高20分，frontier实验室已经在跑。新想法，上一代模型表达不了的训练技巧，是他认为还没有人跨过的线。持续学习在这条线旁边。模型出货之后还留着这个领域的经验，所以同一族的第四个任务不必再长搜索。白盒在这里是更新的形状，不是给每个神经元起名字。Muon把破坏性的大步压下去，把小的模式提上来，也补一块本来就不平衡的数据配比。产品图景是个人agent当大门，每家公司里有专家模型。法律文件打包送出去。私人历史留在原地。",
            "application": "NVDA是他不希望断掉的供应，价格是他可以接受的抱怨。Private:xAI是集群和云的现金，方向还没有站稳。Private:Anthropic是真能收到用户的coding循环，这期带子上的上市数字从大约2万亿落到大约1.3万亿。Learning Machine是持续学习公司，不是这三家里的一个标的。",
        },
        "key_insights": [
            {"view": "后面的0救不了前面缺失的1。", "question": "资源很多的xAI为什么还是没进第一梯队？", "answer": "人、速度和GPU都在。Grok从第一代走到第三代。卡从H100到GB200再到GB300，几十万张可以在几个月里到位。他仍然说每个领域都差一截，因为实验室没有在一个方向上停留到投入可以复利。火箭队能读残骸。模型队要有用户才学得会，除非它已经在前面。剩下的路是蒸馏frontier模型。"},
            {"view": "线性的RSI不是一种新能力。", "question": "怎样才算RSI真的做成了？", "answer": "用GPT-4训练GPT-5、人不进循环，内核快10%或数据更干净，这是线性版本。一代10%到20%是他说实验室已经拿到的结果。coding从50分到70分是同一种爬升。他要的旗子是上一代没有的能力，由agent找出来，而不是研究员写进规格。Infra先到，因为吞吐量是一个分数。后训练的分数太多。调用Claude的循环，可能是在教Claude。"},
            {"view": "Agent应该是门，不是整栋楼。", "question": "这期说的去中心化是什么？", "answer": "每个人有一个了解自己、又不外泄的模型。每家公司有一个装着自己文件的模型。个人agent把活分出去，像搜索框把查询送到它并不拥有的网站。法律材料打包给法律模型，办完送回。手机算力和不会一直开着的笔记本是限制，所以这不是承诺模型住在设备上。白盒也比较窄。他能描述更新，包括Muon把各个方向的步长拉平。他不声称能给每个神经元起名。学习率一路收到零也不是他信任的检查点，因为最后几步会过拟合。"},
        ],
        "golden_quotes": quotes,
        "review_notes": "| v4.10 window 张小珺 E158",
    })
    dump(ROOT / f"data/approved/{eid}.json", en)
    dump(ROOT / f"data/approved/zh/{eid}.json", zh)
    validate_file(ROOT / f"data/approved/{eid}.json")


if __name__ == "__main__":
    main()
