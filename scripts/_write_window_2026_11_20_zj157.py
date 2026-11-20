#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Bilingual ZJ E157."""
from __future__ import annotations

import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))
from scripts._window_lib import dump, en_std, validate_file  # noqa: E402
from src.chinese_transcript import load_transcript_body, quote_supported_in_transcript, transcript_path  # noqa: E402

EID = "zj-ep157"
QUOTES = ["第二点是供给", "万亿级别和十万亿级别", "他也要发红包"]


def main():
    body = load_transcript_body(transcript_path(EID))
    for q in QUOTES:
        print(EID, "OK" if quote_supported_in_transcript(q, body) else "FAIL", q)
        if not quote_supported_in_transcript(q, body):
            raise SystemExit(q)
    meta = {
        "episode_number": 157,
        "title": "Personal Agents with Cai Wei of Ant Lingguang",
        "guest": "Cai Wei (David)",
        "guest_role": "Head of Ant Lingguang",
        "date": "2026-11-18",
        "duration_minutes": 163,
        "youtube_url": "https://www.youtube.com/watch?v=Ydn4NH_KQT8",
        "links": {
            "youtube": "https://www.youtube.com/watch?v=Ydn4NH_KQT8",
            "apple_podcasts": "https://podcasts.apple.com/cn/podcast/id1634356920",
            "xiaoyuzhou": "https://www.xiaoyuzhoufm.com/episode/6afd12c6a4a79edf137afd61",
        },
    }
    concl = (
        "Cai Wei runs Ant Lingguang and splits a personal agent into three jobs: "
        "intelligence, supply, and safety you can actually trust. He maps the product "
        "stages onto industries. Chat retrieved information, a hundred-billion-yuan "
        "market. Manus and Claude Code complete tasks, a trillion-yuan software market. "
        "A personal agent sells services, and in China that is a ten-trillion-yuan "
        "market. Ant starts with Alipay partners and still tunes each scene. His boss "
        "says that in this market even Sam Altman would hand out red packets."
    )
    bg = (
        "E157, Nov 18, about 163 minutes. Zhang Xiaojun with Cai Wei, who goes by David. "
        "Ten years in the US, computer vision at Google, back in 2019, two startups and "
        "some early-stage investing, then Ant in January 2024. Lingguang was scoped in "
        "March 2025, shown internally in July, and pushed out around October and November. "
        "YouTube captions were off. This is a small-model transcript. Whisper hears "
        "Calcode for Claude Code and Automite for Altman."
    )
    facts = [
        (
            "Three stages, three market sizes. After the models arrived, Cai walks the "
            "products as stages. Chatbots fetched information. Task tools, Manus and "
            "Claude Code on the tape, finish a job. A personal agent is the next stage, "
            "and it is a service, not a piece of software sitting on a desktop. Put that "
            "on China and he sizes them at about 100 billion yuan, 1 trillion yuan, and "
            "10 trillion yuan. Information, software, services. The three things a "
            "personal agent has to get right, in his summary, are intelligence, supply, "
            "and safety that is actually usable. Safety, privacy, and compliance are not "
            "a footnote. He says a large share of the work is still there, including "
            "authorization. Claude and Manus, in his telling, did not have to clear the "
            "same domestic permission stack. A personal agent that books, pays, and "
            "moves money does."
        ),
        (
            "Supply is the unglamorous half. A good model can know that a taxi request "
            "should call a taxi API and a meal request should call a delivery API. That "
            "is not the same as the ride feeling smooth. Each partner has a different "
            "interface. The product and engineering teams still tune the important "
            "scenes one by one. Ant's advantage is that many of those partners are "
            "already Alipay or Ant partners, so the conversation is cheaper than a cold "
            "start. 2025 they chose to connect the Alipay service graph first. He is clear "
            "they have not finished the permissions. Connectors, the same idea he sees "
            "in other personal-agent products, are how context gets in without asking "
            "a new user to invent the right question. Most people, especially in China, "
            "will not keep a long interview going with a model. A small group will. "
            "The rest need a low-cost way to hand context over. Personalized encyclopedia "
            "answers are not where that context pays. A personal agent that is supposed "
            "to surprise you only works if it knows you."
        ),
        (
            "The person and the subsidy question. Cai spent 10 years in the US and did "
            "computer vision at Google in the deep-learning years. He came back in 2019, "
            "started companies twice, looked at early investments, and joined Ant in "
            "January 2024 as the models were already up and Ant was turning toward AI. "
            "From late 2022 to 2024 in the Valley, and from 2024 to now in China, he "
            "calls the cultures different. The Valley pushes the ceiling of intelligence. "
            "Domestic companies ask what the same technique does in a product. Lingguang "
            "was scoped in March 2025. An internal version circulated in July. The "
            "external push was aimed at October and November, and he also describes the "
            "app as having launched in November, with 2.0 now out. Zhang asks whether "
            "this Spring Festival turns into a personal-agent subsidy war. Cai says his "
            "boss had a line for that market: in China's kind of competition, if Sam "
            "Altman showed up, he would be handing out red packets too. The agent that "
            "can spend is also the agent that can be subsidized."
        ),
    ]
    mental = {
        "name": "Intelligence × Supply × A Service Market",
        "components": (
            "Chat is information, about 100 billion yuan in his China sizing. Task "
            "tools are software, about 1 trillion. A personal agent is services, about "
            "10 trillion. Intelligence is necessary and not sufficient. Supply is a "
            "partner API tuned scene by scene, starting with Alipay. Safety and "
            "permission are a large share of the calendar once the agent can pay. "
            "Most users will not build the context in chat. Connectors have to. The "
            "Valley pushes the ceiling. China pushes the same model into a service "
            "graph, and the boss expects red packets if the category is real."
        ),
        "application": (
            "Private:Ant is Lingguang plus the Alipay graph, scoped March 2025 and out "
            "by November. Private:Manus is the task stage he places under the service "
            "stage, not the end state. Private:Anthropic is Claude Code on the same "
            "task shelf. Do not mark GOOGL off a ten-year vision job. Underwrite "
            "whether the taxi that the model knows how to call is a ride the user "
            "will finish."
        ),
    }
    insights = [
        {"view": "The big market is services, not another chatbot.", "question": "How does he size China?", "answer": "Information about 100 billion yuan, software about 1 trillion, personal-agent services about 10 trillion. Manus and Claude Code sit in the middle stage."},
        {"view": "Knowing the API is not the ride.", "question": "Why is supply the hard part?", "answer": "The model can call a taxi. Each partner interface is different, so the important scenes are still tuned one by one. Ant starts with partners it already has."},
        {"view": "A real category in China gets a red packet.", "question": "Will Spring Festival be a subsidy war?", "answer": "His boss said that in this market even Sam Altman would hand out red packets. The agent that can pay is also the agent that can be subsidized."},
    ]
    invest = [
        {"ticker": "Private:Ant", "direction": "Long", "confidence": "Low", "thesis": "Lingguang on the Alipay graph, scoped March 2025, the service layer he sizes near 10 trillion yuan — low"},
        {"ticker": "Private:Manus", "direction": "Long", "confidence": "Low", "thesis": "The task-completion stage under the personal agent, software rather than services — low"},
        {"ticker": "Private:Anthropic", "direction": "Long", "confidence": "Low", "thesis": "Claude Code is the other task tool on the tape, same shelf as Manus, not the service market — low"},
    ]
    chrono = {"subject": "Cai Wei · Lingguang · personal agents", "events": [
        {"date": "2009-19", "event": "About 10 years in the US, computer vision at Google"},
        {"date": "2019", "event": "Returns to China; two startups and early investing"},
        {"date": "2024-01", "event": "Joins Ant as the firm turns toward AI"},
        {"date": "2025-03", "event": "Lingguang project starts"},
        {"date": "2025-07", "event": "Internal release"},
        {"date": "2025-11", "event": "External push; 2.0 follows"},
        {"date": "2026-11-18", "event": "E157 publishes"},
    ]}
    en = en_std(EID, "Zhang Xiaojun Podcast", "Zhang Xiaojun", meta, 3,
                ["Private:Ant", "Private:Manus", "Private:Anthropic"],
                concl, bg, facts, mental, insights, invest, QUOTES, chrono,
                "| v4.10 window ZJ E157", "whisper-small")
    zh_meta = dict(meta)
    zh_meta.update(
        title="157. 复盘Personal Agent集体诞生背后：和蔡伟聊AI产品史、需求真伪、入口与未来想象",
        guest="蔡伟（David）",
        guest_role="蚂蚁灵光负责人",
    )
    zh = dict(en)
    zh.update({
        "podcast": "张小珺商业访谈录", "host": "张小珺", "metadata": zh_meta,
        "conclusion": "蔡伟负责蚂蚁灵光。他把个人代理拆成三件事：智能、供给，以及真正可信的安全。产品阶段对应行业。聊天获取信息，大约千亿。Manus和Claude Code完成任务，大约万亿的软件市场。个人代理卖的是服务，在中国他放到十万亿。模型知道该叫出租车，不代表这趟车顺。每一家的接口都要按场景调。蚂蚁先接支付宝，因为这些伙伴已经在网络里。多数用户不会自己把上下文问出来。老板对春晚补贴战的一句是：在这种竞争里，Sam Altman来了也要发红包。",
        "background": "E157，11月18日，大约163分钟。张小珺对蔡伟，英文名David。美国十年，在Google做计算机视觉，2019年回国，创过两次业，看过早期投资，2024年1月进蚂蚁。灵光2025年3月立项，7月内部，10月到11月往外推。YouTube没有字幕，这是小模型转写。Whisper把Claude Code听成Calcode，把Altman听成Automite。",
        "important_facts": [
            "三个阶段，三种规模。模型出来之后，蔡伟把产品分成阶段。聊天机器人获取信息。完成任务的工具，带子上是Manus和Claude Code。个人代理是下一阶段，它是服务，不是桌面上的一块软件。放到中国，他分别放到大约千亿、万亿和十万亿。信息、软件、服务。个人代理要搞好的三件事，他归纳为智能、供给，以及真正能用的安全。安全、隐私和合规不是脚注。他说相当一部分时间仍花在这里，包括授权。Claude和Manus在他的说法里不必过同一套国内许可。一个能订、能付、能转钱的代理必须过。",
            "供给是不好看的那一半。好模型知道打车请求该调打车接口，点餐该调外卖接口。这和这趟车顺不顺不是一回事。每个伙伴的接口不同。产品和工程仍在重要场景里一个一个调。蚂蚁的优势是很多伙伴本来就是支付宝或蚂蚁的伙伴，谈话成本低于冷启动。他们选择先接支付宝的服务图。他明确说授权还没接完，正在逐步接。连接器，他在别的个人代理产品里也看到的概念，是让新用户不必自己发明好问题，也能把上下文交进来。多数人，尤其国内用户，不会跟模型做一场长访谈。只有一小部分人会。其余的人需要低成本的交法。百科式的个性化回答不是上下文值钱的地方。一个应该给你惊喜的个人代理，前提是它了解你。",
            "这个人和补贴问题。蔡伟在美国待了大约10年，深度学习年代在Google做计算机视觉。2019年回国，创过两次业，看过早期项目，2024年1月加入蚂蚁。那时模型已经起来，蚂蚁在转向AI。2022年底到2024年在硅谷，2024年到现在在中国，他说两边文化不一样。硅谷更推智能的上限。国内公司更问同一项技术在产品里做什么。灵光2025年3月立项。7月有内部版本。对外原定10月到11月，他也把应用说成11月上线，现在有2.0。小珺问今年春晚会不会打成个人代理的补贴战。蔡伟说老板有一句：在中国这种充分竞争里，如果Sam Altman来，他也要发红包。能花钱的代理，也是能被补贴的代理。",
        ],
        "mental_model": {
            "name": "智能 × 供给 × 服务市场",
            "components": "聊天是信息，他给中国大约千亿。任务工具是软件，大约万亿。个人代理是服务，大约十万亿。智能必要，但不够。供给是按场景调过的伙伴接口，从支付宝开始。一旦代理能付款，安全和授权就占掉日历的一大块。多数用户不会在聊天里建起上下文。连接器必须做。硅谷推上限。中国把同一个模型推进服务图，老板预期这个品类如果是真的，就会有红包。",
            "application": "Private:Ant是灵光加上支付宝的图，2025年3月立项，11月往外。Private:Manus是他放在服务阶段下面的任务阶段，不是终点。Private:Anthropic的Claude Code在同一层任务架子上。不要因为一份十年的视觉工作去标GOOGL。要看模型知道该叫的那辆车，用户会不会坐完。",
        },
        "key_insights": [
            {"view": "大市场是服务，不是又一个聊天框。", "question": "他怎么给中国分规模？", "answer": "信息大约千亿，软件大约万亿，个人代理的服务大约十万亿。Manus和Claude Code坐在中间那一阶段。"},
            {"view": "知道接口，不等于这趟车顺。", "question": "为什么供给难？", "answer": "模型可以叫出租车。每个伙伴的接口不同，重要场景仍要一个一个调。蚂蚁从已经有的伙伴开始。"},
            {"view": "在中国，真品类会有红包。", "question": "春晚会打补贴战吗？", "answer": "老板说这种市场里Sam Altman来了也要发红包。能付钱的代理，也是能被补贴的代理。"},
        ],
        "golden_quotes": QUOTES,
        "review_notes": "| v4.10 window 张小珺 E157",
    })
    dump(ROOT / f"data/approved/{EID}.json", en)
    dump(ROOT / f"data/approved/zh/{EID}.json", zh)
    validate_file(ROOT / f"data/approved/{EID}.json")


if __name__ == "__main__":
    main()
