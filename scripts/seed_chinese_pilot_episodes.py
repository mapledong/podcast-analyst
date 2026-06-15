#!/usr/bin/env python3
"""Seed bilingual approved JSON for Chinese podcast pilot episodes."""

from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
ZH = ROOT / "data" / "approved" / "zh"
EN = ROOT / "data" / "approved"

EPISODES = {
    "zj-ep140": {
        "zh": {
            "episode_id": "zj-ep140",
            "podcast": "张小珺商业访谈录",
            "host": "张小珺",
            "metadata": {
                "episode_number": 140,
                "title": "请允许我小疯一下：在 Anthropic 与 Gemini 训模型、英雄主义已过去",
                "guest": "姚顺宇",
                "guest_role": "Google DeepMind 研究员（前 Anthropic）",
                "date": "2026-05-11",
                "duration_minutes": 228,
                "youtube_url": "https://www.youtube.com/watch?v=ttkd0t5qTD4",
                "links": {
                    "youtube": "https://www.youtube.com/watch?v=ttkd0t5qTD4",
                    "apple_podcasts": "https://podcasts.apple.com/cn/podcast/id1634356920",
                    "xiaoyuzhou": "https://www.xiaoyuzhoufm.com/podcast/626b46ea9cbbf0451cf5a962",
                },
            },
            "episode_rating": {"overall": 5},
            "keywords": ["GOOGL", "AI 前沿实验室", "模型训练"],
            "conclusion": "姚顺宇的核心判断：前沿模型能力正在拉平，OpenAI、Anthropic、Google 三家不再担心「追不上」，真正的难题是「赌什么」——产品定义与执行靠谱度比英雄主义叙事更重要。对个人投资者：算力与分发仍向头部集中，但应用层机会来自把模型嵌进真实工作流；中国侧豆包等产品在语音等场景已出现差异化。",
            "background": "张小珺对话刚从 Anthropic 转至 Google DeepMind 的姚顺宇（顺宇），从 2025–2026 年模型发布潮谈起。顺宇参与过 Claude 与 Gemini 训练，见证「推理」能力跃迁后行业心态从「能不能做到」转向「要做什么」。他描述硅谷模型圈像冲浪——大家乘同一浪，关键是谁更细、更靠谱。",
            "important_facts": [
                "顺宇称 2025 年前后前沿三家（OpenAI、Anthropic、Google）在基准能力上差距缩小；一年前 Anthropic 还担心追不上 OpenAI 的 reasoning，如今更焦虑的是任务定义与产品 bet。",
                "他举例豆包语音生成体验在中国日常场景中强于 Gemini/Claude，但美国用户更在意 coding 与深度推理——产品优化路径因用户群而异。",
                "顺宇求职时同时接触 Anthropic、OpenAI 与 Google DeepMind；最终因面试节奏选择 Anthropic，后转 GDM。他提到 Dario 曾公开点名多家公司「蒸馏」Anthropic 模型，侧面反映头部实验室对 IP 与数据闭环的防御心态。",
            ],
            "mental_model": {
                "name": "能力拉平 × 产品 bet × 靠谱执行",
                "components": "当模型基准差距收窄，竞争从「有没有智力」转向「为谁解决什么问题」。Startup 可以 top-down 下赌注（Anthropic 的 coding bet 是案例）；大公司更难统一方向。行业核心特质是靠谱：做事细、对结果负责，而非个人英雄叙事。",
                "application": "投资映射：① 头部实验室（GOOGL/私有 OpenAI/Anthropic）仍吃训练与推理规模；② 区域产品（字节豆包等）在语音、低延迟等场景拿份额；③ 应用层看工作流嵌入深度，而非模型榜单分数。顺宇提醒普通用户对模型能力感知很弱——多数人不碰 o 系列，产品体验与留存才是商业化胜负手。",
            },
            "key_insights": [
                {
                    "view": "AI 进入「担心事情是否被良好定义」的阶段，而非担心做不到。",
                    "question": "能力拉平后，差异化来自哪里？",
                    "answer": "来自产品 bet 与 insight：Anthropic 用 Claude Code 吃 coding 增量；Google 用 Nano Banana 等拉量再靠 Gemini 3 留人。模型智商差 5 个点用户未必感知，但「快、好用、便宜」感知极强。",
                },
                {
                    "view": "OpenAI 市占高到模型失误的边际影响变小，但 Google 必须靠产品把量打回来。",
                    "question": "为什么 Gemini 的「拉量」动作很关键？",
                    "answer": "顺宇认为 ChatGPT 心智仍强，Gemini 需要消费级爆款（如图像/轻量功能）把人留住，再用旗舰模型承接。对投资者：搜索+安卓分发是 Google 独有杠杆，但转化需要连续产品命中。",
                },
                {
                    "view": "「英雄主义已过去」——行业不再需要天才叙事，需要长期靠谱交付。",
                    "question": "这对团队与资本意味着什么？",
                    "answer": "训练与对齐变成工程与组织战：数据、评测、产品闭环比单点论文重要。顺宇称 AI「不太需要脑子、需要靠谱」，意指投机式押注窗口收窄，能持续交付商业结果的团队溢价上升。",
                },
            ],
            "top_investment_implications": [
                {
                    "ticker": "GOOGL",
                    "direction": "Long",
                    "confidence": "Medium",
                    "thesis": "Gemini 3 与消费级功能若持续拉量，搜索与安卓分发可放大模型变现；顺宇视角下 Google 正处于「把量打回来」的关键战役",
                },
                {
                    "ticker": "Private:Anthropic",
                    "direction": "Watch",
                    "confidence": "Medium",
                    "thesis": "Coding/agent 工作流 bet 领先，但面临蒸馏与开源压力；能力拉平后需证明 ARR 与 enterprise 锁定的可持续性",
                },
            ],
            "golden_quotes": [
                "每个人都是冲浪的人，本质上是一个浪，而不是你那个冲浪的人。",
                "现在大家都不那么担心 AI 能不能做到，而是担心这件事是不是被良好定义。",
                "这个行业最重要的特质就是靠谱，就是做事细，然后对自己做的事负责任。",
            ],
            "chronology": {
                "subject": "姚顺宇 · 前沿模型训练",
                "events": [
                    {"date": "GPT-3 时代", "event": "顺宇入行，见证 Tom Brown 等主导的 scaling 叙事"},
                    {"date": "2023–2024", "event": "行业焦点转向 reasoning；Anthropic 担心追赶 OpenAI"},
                    {"date": "2025 中", "event": "Claude Code 等产品触发 coding 商业化拐点"},
                    {"date": "2025–2026", "event": "顺宇在 Anthropic 参与训练，后转 Google DeepMind"},
                    {"date": "2026", "event": "三家前沿能力感知拉平，竞争重心转向产品定义与执行"},
                ],
            },
        },
        "en": {
            "episode_id": "zj-ep140",
            "podcast": "Zhang Xiaojun Podcast",
            "host": "Zhang Xiaojun",
            "metadata": {
                "episode_number": 140,
                "title": "Let Me Go a Little Crazy: Training at Anthropic & Gemini, Heroism Is Over",
                "guest": "Yao Shunyu",
                "guest_role": "Google DeepMind Researcher (formerly Anthropic)",
                "date": "2026-05-11",
                "duration_minutes": 228,
                "youtube_url": "https://www.youtube.com/watch?v=ttkd0t5qTD4",
                "links": {
                    "youtube": "https://www.youtube.com/watch?v=ttkd0t5qTD4",
                    "apple_podcasts": "https://podcasts.apple.com/cn/podcast/id1634356920",
                    "xiaoyuzhou": "https://www.xiaoyuzhoufm.com/podcast/626b46ea9cbbf0451cf5a962",
                },
            },
            "episode_rating": {"overall": 5},
            "keywords": ["GOOGL", "AI Labs", "Model Training"],
            "conclusion": "Yao's bottom line: frontier model capability is converging — OpenAI, Anthropic, and Google worry less about catching up and more about what to bet on. Reliability and product definition beat hero narratives. For investors: compute and distribution still accrue to leaders, but application-layer wins go to whoever embeds models in real workflows; China's Doubao already differentiates on voice UX.",
            "background": "Zhang Xiaojun interviews Yao Shunyu after his move from Anthropic to Google DeepMind. He helped train Claude and Gemini through the 2025–26 model wave and watched the industry's anxiety shift from 'can AI do it?' to 'what should we build?' He describes frontier labs as surfers on the same wave — execution and taste matter more than myth-making.",
            "important_facts": [
                "Yao says by 2025–26 the top three labs looked much closer on benchmarks; a year earlier Anthropic still feared OpenAI's reasoning lead — now the harder problem is choosing the right product bet.",
                "He notes Doubao's voice generation feels best for everyday Chinese users, while US users weight coding and deep reasoning — optimization paths diverge by audience.",
                "When job-hunting he talked to Anthropic, OpenAI, and DeepMind; picked Anthropic on pace, later joined GDM. He references Dario Amodei publicly calling out distillers — a sign top labs are defending data and IP loops.",
            ],
            "mental_model": {
                "name": "Capability Convergence × Product Bet × Reliable Execution",
                "components": "As benchmark gaps shrink, competition moves from raw intelligence to 'for whom, solving what.' Startups can make top-down bets (Anthropic on coding); big companies struggle to align. The scarcest trait is reliability — detail orientation and ownership — not lone-genius stories.",
                "application": "Investing lens: (1) leaders (GOOGL / private OpenAI / Anthropic) still capture training and inference scale; (2) regional products (ByteDance Doubao, etc.) win on voice, latency, and local UX; (3) at the app layer, judge workflow lock-in, not leaderboard scores. Most users barely perceive model IQ gaps — speed, usefulness, and price drive retention.",
            },
            "key_insights": [
                {
                    "view": "AI has entered a phase of worrying whether problems are well-defined, not whether models can solve them.",
                    "question": "Where does differentiation come from after convergence?",
                    "answer": "Product bets and taste: Anthropic leaned into Claude Code; Google needs consumer hits (e.g., Nano Banana) to pull volume back before flagship models retain users. A five-point benchmark gap often goes unnoticed; 'fast, useful, cheap' does not.",
                },
                {
                    "view": "OpenAI's share is so high that model stumbles hurt less at the margin; Google must win the volume game.",
                    "question": "Why does Gemini's consumer push matter?",
                    "answer": "ChatGPT still owns mindshare. Gemini needs breakout consumer features to feed the funnel, then flagship models to hold users. For investors, search + Android distribution are Google's unique levers — but only if product hits chain together.",
                },
                {
                    "view": "The heroism era is over — the industry needs steady delivery, not genius mythology.",
                    "question": "What does that mean for teams and capital?",
                    "answer": "Training becomes an engineering and org game: data, evals, and product loops beat one-off papers. Yao quips AI 'doesn't need brains, it needs reliability' — speculative punts narrow; teams that ship commercial results command a premium.",
                },
            ],
            "top_investment_implications": [
                {
                    "ticker": "GOOGL",
                    "direction": "Long",
                    "confidence": "Medium",
                    "thesis": "If Gemini 3 plus consumer features keep pulling volume, search and Android distribution amplify monetization — Yao frames Google as fighting to win the volume war back",
                },
                {
                    "ticker": "Private:Anthropic",
                    "direction": "Watch",
                    "confidence": "Medium",
                    "thesis": "Coding/agent workflow bet is ahead, but distillation and open-source pressure rise as capabilities converge — must prove durable ARR and enterprise lock-in",
                },
            ],
            "golden_quotes": [
                "Everyone is a surfer on the same wave — it's the wave, not the surfer, that matters.",
                "People worry less about whether AI can do it, and more about whether the problem is well defined.",
                "This industry's most important trait is reliability — doing careful work and owning the outcome.",
            ],
            "chronology": {
                "subject": "Yao Shunyu · Frontier Model Training",
                "events": [
                    {"date": "GPT-3 era", "event": "Yao enters field during Tom Brown–era scaling narrative"},
                    {"date": "2023–24", "event": "Industry pivots to reasoning; Anthropic fears OpenAI lead"},
                    {"date": "Mid-2025", "event": "Claude Code catalyzes coding commercialization"},
                    {"date": "2025–26", "event": "Yao trains at Anthropic, then joins Google DeepMind"},
                    {"date": "2026", "event": "Top-three capability perceived as converging; product definition becomes the battleground"},
                ],
            },
        },
    },
    "zj-ep143": {
        "zh": {
            "episode_id": "zj-ep143",
            "podcast": "张小珺商业访谈录",
            "host": "张小珺",
            "metadata": {
                "episode_number": 143,
                "title": "何小鹏：停掉旧机器人、押注人形 IRON 与物理世界 AI",
                "guest": "何小鹏",
                "guest_role": "小鹏汽车董事长兼 CEO",
                "date": "2026-05-28",
                "duration_minutes": 86,
                "youtube_url": "https://www.youtube.com/watch?v=rUjaLPE3mME",
                "links": {
                    "youtube": "https://www.youtube.com/watch?v=rUjaLPE3mME",
                    "apple_podcasts": "https://podcasts.apple.com/cn/podcast/id1634356920",
                    "xiaoyuzhou": "https://www.xiaoyuzhoufm.com/podcast/626b46ea9cbbf0451cf5a962",
                },
            },
            "episode_rating": {"overall": 4},
            "keywords": ["XPEV", "人形机器人", "自动驾驶", "物理世界 AI"],
            "conclusion": "何小鹏的核心判断：旧机器人技术栈已耗费数百亿且方向错误，必须果断止损；人形机器人 IRON 是低胜率（约 20%）但高赔率 bet，成败取决于物理世界数据闭环。物理世界 AI 数据采集成本每年可能超 10 亿人民币——这是比模型本身更硬的壁垒。L4 纯视觉捷径已证伪，GX 车型 pivot 反映产品定义比技术炫技更重要。对投资者：XPEV 估值需同时计入汽车基本盘、AI 投入 burn 与机器人期权，不宜用单一 PE 框架。",
            "background": "张小珺对话小鹏汽车何小鹏，从 2025–2026 年机器人与智驾战略大调整谈起。小鹏曾投入大量资源于上一代机器人方案，最终选择「停掉旧栈、all-in 人形」。他坦承 IRON 项目胜率不高，但若成功将重新定义公司边界。话题延伸至 L4 自动驾驶路线反思、GX 产品 pivot，以及「物理世界 AI」为何比 LLM 更烧钱。",
            "important_facts": [
                "何小鹏称旧机器人技术路线累计投入达数百亿人民币量级，团队与供应链绑定深，止损决策痛苦但必要——继续投入是「沉没成本陷阱」。",
                "人形机器人 IRON 被他定性为约 20% 胜率的高赔率 bet：硬件、运动控制、场景数据三环缺一不可，小鹏试图用汽车智驾积累迁移，但人形与车载场景差异仍大。",
                "物理世界 AI 的数据采集与标注成本极高——他估算年投入可能超 10 亿人民币，远超纯软件 AI；这解释了为何机器人赛道最终只剩少数玩家。",
                "L4 纯视觉/端到端「捷径」在小鹏实践中未达预期，GX 车型 pivot 是产品与市场匹配调整，而非单纯技术失败。",
            ],
            "mental_model": {
                "name": "止损旧栈 × 低胜率期权 × 物理世界数据壁垒",
                "components": "当技术路线被证伪，沉没成本不应绑架未来 capital allocation。人形机器人是典型「20% 胜率、10x 回报」期权——需独立预算与 KPI，不能与主业务 P&L 混算。物理世界 AI 的竞争本质是数据闭环：谁能在真实场景持续采集、标注、迭代，谁才有训练优势；这比模型架构更难复制。",
                "application": "投资映射：① XPEV 汽车销量与毛利仍是估值锚，机器人/AI 投入是减项或期权 depending on 执行；② 对比 TSLA Optimus、Figure 等，小鹏有制造与供应链但缺场景密度；③ L4 赛道整体降温，投资者应下调「纯软件定义汽车」溢价，重视硬件迭代与监管节奏。",
            },
            "key_insights": [
                {
                    "view": "旧机器人栈的数百亿投入是「买教训」，继续投是理性但错误的选择。",
                    "question": "为何大厂难以在技术路线错误时及时止损？",
                    "answer": "组织惯性、人才绑定与叙事压力使止损像「承认失败」。何小鹏强调 CEO 必须能承担短期舆论代价，把 capital 转投胜率更高的方向——IRON 虽仅 20% 胜率，但成功回报远超继续修补旧栈。",
                },
                {
                    "view": "物理世界 AI 的数据成本可能是被低估的「隐形 moat」。",
                    "question": "为何机器人 AI 比 LLM 更烧钱？",
                    "answer": "文本数据近乎免费，物理场景数据需真实设备、安全合规、长尾场景覆盖——年成本 10 亿+ 不夸张。这意味着机器人赛道天然 oligopoly：只有能持续 burn 且有多场景入口的玩家能玩。",
                },
                {
                    "view": "L4 捷径思维在小鹏侧已修正，GX pivot 是产品诚实。",
                    "question": "对智驾投资意味着什么？",
                    "answer": "纯视觉端到端并非万能钥匙；监管、地图、安全冗余仍约束落地节奏。投资者应降低对「202X 年 L4 大规模商用」的线性预期，更关注 L2+ 渗透率与 ASP 提升对 near-term 收入的贡献。",
                },
            ],
            "top_investment_implications": [
                {
                    "ticker": "XPEV",
                    "direction": "Watch",
                    "confidence": "Medium",
                    "thesis": "汽车基本盘与机器人/AI burn 并存；IRON 是低胜率期权，需跟踪 quarterly 现金流与 GX 交付数据，不宜仅用传统 auto PE 定价",
                },
                {
                    "ticker": "TSLA",
                    "direction": "Watch",
                    "confidence": "Low",
                    "thesis": "Optimus 与人形赛道直接对标；何小鹏的 20% 胜率框架暗示行业普遍高失败率，Tesla 机器人叙事溢价需 scenario 分析",
                },
                {
                    "ticker": "NVDA",
                    "direction": "Long",
                    "confidence": "Medium",
                    "thesis": "物理世界 AI 与机器人训练推高 edge 算力需求；无论哪家 OEM 胜出，芯片层受益",
                },
            ],
            "golden_quotes": [
                "旧机器人那条路，我们花了太多钱，必须停——不停才是最大的浪费。",
                "IRON 这个项目，我自己评估胜率大概两成，但成了就是另一家公司。",
                "物理世界的 AI，数据才是真的贵，一年十亿可能都不够。",
            ],
            "chronology": {
                "subject": "何小鹏 · 机器人与智驾 pivot",
                "events": [
                    {"date": "2020–2023", "event": "小鹏投入上一代机器人与 L4 智驾，累计资本开支达数百亿量级"},
                    {"date": "2024–2025", "event": "旧机器人栈被判定方向错误，启动止损与组织调整"},
                    {"date": "2025–2026", "event": "All-in 人形机器人 IRON；物理世界 AI 数据体系独立预算"},
                    {"date": "2026", "event": "GX 车型 pivot 落地；L4 纯视觉捷径被内部证伪"},
                ],
            },
        },
        "en": {
            "episode_id": "zj-ep143",
            "podcast": "Zhang Xiaojun Podcast",
            "host": "Zhang Xiaojun",
            "metadata": {
                "episode_number": 143,
                "title": "He Xiaopeng: Killing the Old Robot Stack, Betting on IRON Humanoids & Physical-World AI",
                "guest": "He Xiaopeng",
                "guest_role": "Chairman & CEO, XPeng",
                "date": "2026-05-28",
                "duration_minutes": 86,
                "youtube_url": "https://www.youtube.com/watch?v=rUjaLPE3mME",
                "links": {
                    "youtube": "https://www.youtube.com/watch?v=rUjaLPE3mME",
                    "apple_podcasts": "https://podcasts.apple.com/cn/podcast/id1634356920",
                    "xiaoyuzhou": "https://www.xiaoyuzhoufm.com/podcast/626b46ea9cbbf0451cf5a962",
                },
            },
            "episode_rating": {"overall": 4},
            "keywords": ["XPEV", "Humanoid Robotics", "Autonomous Driving", "Physical-World AI"],
            "conclusion": "He's bottom line: the legacy robot stack burned billions on the wrong architecture — stopping was rational, not failure. IRON humanoids are a ~20% probability, high-payoff bet hinging on physical-world data loops. Data capture alone may exceed RMB 1B/year — a harder moat than model weights. The L4 vision-only shortcut failed internally; the GX pivot shows product-market fit beats tech bragging rights. For investors: XPEV needs a sum-of-the-parts lens — auto core, AI burn, and robotics optionality — not a single auto PE multiple.",
            "background": "Zhang Xiaojun interviews XPeng's He Xiaopeng on the 2025–26 reset in robotics and autonomy. XPeng walked away from a prior robot program after sunk costs in the tens of billions of RMB, going all-in on humanoid IRON. He frames it as low win-rate, massive upside. The conversation covers L4 autonomy regrets, the GX product pivot, and why physical-world AI is more capital-intensive than LLMs.",
            "important_facts": [
                "He says the old robot route consumed on the order of tens of billions of RMB; unwinding it was painful but necessary — throwing good money after bad was the real risk.",
                "IRON is tagged at ~20% win probability: hardware, locomotion, and scenario data must click together; auto-driving experience helps but humanoid use cases differ materially.",
                "Physical-world AI data may cost RMB 1B+ annually — far above pure software AI — explaining why robotics consolidates to a handful of well-funded players.",
                "The L4 vision-only shortcut underperformed expectations; the GX pivot reflects honest product repositioning, not just a tech miss.",
            ],
            "mental_model": {
                "name": "Kill the Old Stack × Low-Probability Option × Physical-Data Moat",
                "components": "When a tech path is disproved, sunk cost must not dictate capital allocation. Humanoids are classic 20%-win / 10x-payoff options — budget and KPIs should be separate from core auto P&L. Physical-world AI competition is a data flywheel: whoever captures, labels, and iterates in real scenes wins training advantage — harder to copy than architecture.",
                "application": "Investing lens: (1) XPEV auto volume and gross margin remain the valuation anchor; robotics/AI spend is either drag or option value; (2) vs. TSLA Optimus and Figure, XPeng has manufacturing but lacks scenario density; (3) L4 hype should cool — weight L2+ penetration and ASP uplift for near-term revenue over linear L4 timelines.",
            },
            "key_insights": [
                {
                    "view": "Billions on the old robot stack bought lessons — continuing would have been the irrational choice.",
                    "question": "Why do big companies struggle to kill bad tech bets?",
                    "answer": "Org inertia, talent lock-in, and narrative pressure make stops feel like confession. He argues CEOs must absorb short-term criticism and redeploy capital — IRON's ~20% odds still beat patching a disproved stack.",
                },
                {
                    "view": "Physical-world AI data cost is an underappreciated moat.",
                    "question": "Why is robot AI more expensive than LLMs?",
                    "answer": "Text is nearly free; physical scenes need real hardware, safety compliance, and long-tail coverage — RMB 1B+/year is plausible. Robotics naturally oligopolizes: only players with burn capacity and multi-scenario entry points survive.",
                },
                {
                    "view": "The L4 shortcut mindset is corrected internally; GX pivot is product honesty.",
                    "question": "What does this mean for autonomy investing?",
                    "answer": "End-to-end vision isn't a skeleton key; regulation, mapping, and redundancy still gate deployment. Investors should discount linear 'L4 by 202X' narratives and focus on L2+ adoption and near-term ASP contribution.",
                },
            ],
            "top_investment_implications": [
                {
                    "ticker": "XPEV",
                    "direction": "Watch",
                    "confidence": "Medium",
                    "thesis": "Auto core coexists with robotics/AI burn; IRON is a low-probability option — track quarterly cash flow and GX deliveries; traditional auto PE alone misprices the story",
                },
                {
                    "ticker": "TSLA",
                    "direction": "Watch",
                    "confidence": "Low",
                    "thesis": "Optimus is a direct comp; He's ~20% win-rate framing implies industry-wide high failure rates — Tesla robot narrative premium needs scenario analysis",
                },
                {
                    "ticker": "NVDA",
                    "direction": "Long",
                    "confidence": "Medium",
                    "thesis": "Physical-world AI and robot training lift edge compute demand; chip layer benefits regardless of which OEM wins",
                },
            ],
            "golden_quotes": [
                "We spent too much on the old robot path — stopping is the real savings.",
                "I put IRON's win probability at roughly twenty percent — but if it works, we're a different company.",
                "In physical-world AI, data is what's truly expensive — a billion a year may not be enough.",
            ],
            "chronology": {
                "subject": "He Xiaopeng · Robotics & Autonomy Pivot",
                "events": [
                    {"date": "2020–23", "event": "XPeng invests heavily in prior robot stack and L4 autonomy — cumulative spend in tens of billions RMB"},
                    {"date": "2024–25", "event": "Legacy robot direction judged wrong; stop-loss and org reset begin"},
                    {"date": "2025–26", "event": "All-in on IRON humanoid; physical-world AI data budget ring-fenced"},
                    {"date": "2026", "event": "GX product pivot ships; L4 vision-only shortcut disproved internally"},
                ],
            },
        },
    },
    "zj-ep144": {
        "zh": {
            "episode_id": "zj-ep144",
            "podcast": "张小珺商业访谈录",
            "host": "张小珺",
            "metadata": {
                "episode_number": 144,
                "title": "阳萌：安克创新的浅海战略、AI 组织与用十亿 token 理解一家公司",
                "guest": "阳萌",
                "guest_role": "安克创新创始人兼 CEO",
                "date": "2026-06-08",
                "duration_minutes": 218,
                "youtube_url": "https://www.youtube.com/watch?v=kBsqirnWTpI",
                "links": {
                    "youtube": "https://www.youtube.com/watch?v=kBsqirnWTpI",
                    "apple_podcasts": "https://podcasts.apple.com/cn/podcast/id1634356920",
                    "xiaoyuzhou": "https://www.xiaoyuzhoufm.com/podcast/626b46ea9cbbf0451cf5a962",
                },
            },
            "episode_rating": {"overall": 5},
            "keywords": ["300866.SZ", "Anker", "浅海战略", "AI 组织"],
            "conclusion": "阳萌的核心框架：安克 (~600 亿+ 人民币市值) 坚持「浅海 vs 深海」——优先进入 TAM <500 亿美元、可建立品类领导力的细分赛道，而非红海肉搏。AI 正在重塑组织：context length 扩展到十亿 token 级，理论上可「读完」一家公司的全部文档，改变 research 与决策方式。历史上毛利率每年提升 1.1–1.5 个百分点是复利引擎。对投资者：300866.SZ 是品类扩张 + 品牌溢价 + 运营效率的故事，需跟踪新品类成功率与 Amazon 渠道依赖。",
            "background": "三小时对话中，阳萌复盘安克从充电配件到多品类消费电子品牌的成长路径。他解释「浅海战略」如何避开与巨头正面冲突，以及 2025–2026 年 AI 如何渗透产品定义、供应链与内部知识管理。张小珺与他探讨：当 AI 能 ingest 十亿 token 的公司资料，投资研究与管理决策会被如何改写。",
            "important_facts": [
                "安克市值已达 600 亿人民币以上；阳萌强调品类选择比规模更重要——目标市场常限定在 500 亿美元 TAM 以下，以便快速成为 category leader。",
                "「浅海」= 竞争尚未固化、用户痛点清晰、可凭产品与设计建立心智；「深海」= 巨头林立的红海，安克主动回避。",
                "阳萌描述 AI 组织革命：内部知识、用户反馈、竞品情报可被 LLM 整合；context window 向十亿 token 演进，意味着「理解一家公司」的成本骤降。",
                "安克历史上毛利率每年约提升 1.1–1.5 个百分点，来自品牌溢价、供应链优化与 SKU 结构升级——这是长期 compounder 的核心财务特征。",
            ],
            "mental_model": {
                "name": "浅海品类 × 毛利率复利 × 十亿 token 研究",
                "components": "选市场：TAM 适中、竞争格局未封死、可凭产品力拿第一。做组织：AI 把分散文档变成可查询 context，缩短从 insight 到 action 的链路。看财务：毛利率年化 +1–1.5pt 比收入增速更能证明 brand moat。",
                "application": "投资映射：① 300866.SZ 估值应 tied to 新品类 ROIC 与毛利率 trajectory，而非单一充电配件周期；② 浅海逻辑可对标 DTC 品牌 vs 平台依赖 —— 跟踪 Amazon 占比与自有渠道；③ AI 工具若真提升决策效率，应体现在 faster SKU 迭代与更低 SG&A ratio。",
            },
            "key_insights": [
                {
                    "view": "多数好生意藏在「不够大」的市场里——500 亿美元 TAM 是 mental ceiling。",
                    "question": "为何不直接打手机、笔记本等超级大盘？",
                    "answer": "大盘吸引巨头全资源投入，初创/中型玩家难建心智。浅海允许安克用 2–3 年成为品类第一，再 adjacent expansion——这与 Christensen 式颠覆逻辑一致，但执行更偏品牌与产品而非纯低价。",
                },
                {
                    "view": "十亿 token context 可能改变「理解公司」的 economics。",
                    "question": "对投资者意味着什么？",
                    "answer": "若模型可 ingest 财报、供应链、用户评论、专利全集，research 边际成本下降，但 alpha 转向「问对问题」与 judgment。阳萌暗示安克已在内部试验——领先应用 AI 的消费品牌可能获得决策速度优势。",
                },
                {
                    "view": "毛利率 +1.1–1.5pt/年 是安克最应被 respect 的指标。",
                    "question": "如何验证浅海战略有效？",
                    "answer": "收入增速会波动，但 sustained gross margin expansion 说明定价权与成本结构在改善。投资者应警惕毛利率 flatten 或 SG&A 飙升 —— 可能是浅海红利耗尽或品类扩张失焦的信号。",
                },
            ],
            "top_investment_implications": [
                {
                    "ticker": "300866.SZ",
                    "direction": "Long",
                    "confidence": "Medium",
                    "thesis": "Category expansion + brand premium + ~1.1–1.5pt annual gross margin lift; track new category hit rate and Amazon channel concentration",
                },
                {
                    "ticker": "AAPL",
                    "direction": "Watch",
                    "confidence": "Low",
                    "thesis": "Anker's accessory adjacency competes at ecosystem edges; Apple's pricing and retail power cap upside in overlapping SKUs",
                },
                {
                    "ticker": "AMZN",
                    "direction": "Watch",
                    "confidence": "Medium",
                    "thesis": "Anker remains Amazon-native; platform policy, ads cost, and private-label competition directly affect 300866 margins",
                },
            ],
            "golden_quotes": [
                "我们喜欢的市场，往往不到五百亿美元——够大能养出第一，不够大引不来全部巨头。",
                "AI 之后，理解一家公司可能需要十亿 token 的 context，这会改变所有管理决策。",
                "毛利率每年涨一个多点，看起来不多，复利十年就是完全不同的公司。",
            ],
            "chronology": {
                "subject": "阳萌 · 安克创新与浅海战略",
                "events": [
                    {"date": "2011", "event": "阳萌创立 Anker，从充电配件切入 Amazon 渠道"},
                    {"date": "2016–2020", "event": "多品类扩张（音频、智能家居等），浅海战略成型"},
                    {"date": "2020", "event": "安克创新深交所上市 (300866.SZ)"},
                    {"date": "2025–2026", "event": "市值突破 600 亿 RMB；AI 组织变革与十亿 token 研究框架提出"},
                ],
            },
        },
        "en": {
            "episode_id": "zj-ep144",
            "podcast": "Zhang Xiaojun Podcast",
            "host": "Zhang Xiaojun",
            "metadata": {
                "episode_number": 144,
                "title": "Yang Meng: Anker's Shallow-Sea Strategy, AI Org Revolution & Billion-Token Company Understanding",
                "guest": "Yang Meng",
                "guest_role": "Founder & CEO, Anker Innovations",
                "date": "2026-06-08",
                "duration_minutes": 218,
                "youtube_url": "https://www.youtube.com/watch?v=kBsqirnWTpI",
                "links": {
                    "youtube": "https://www.youtube.com/watch?v=kBsqirnWTpI",
                    "apple_podcasts": "https://podcasts.apple.com/cn/podcast/id1634356920",
                    "xiaoyuzhou": "https://www.xiaoyuzhoufm.com/podcast/626b46ea9cbbf0451cf5a962",
                },
            },
            "episode_rating": {"overall": 5},
            "keywords": ["300866.SZ", "Anker", "Shallow-Sea Strategy", "AI Organization"],
            "conclusion": "Yang's framework: Anker (~RMB 60B+ market cap) plays 'shallow sea vs. deep sea' — target categories under ~$500B TAM where category leadership is achievable, avoiding bloody red oceans. AI is reshaping the org: billion-token context could let you 'read' an entire company's corpus, changing research and decisions. Historically, +1.1–1.5pt gross margin per year is the compounding engine. For investors: 300866.SZ is category expansion + brand premium + operational efficiency — watch new-category hit rates and Amazon dependence.",
            "background": "In a three-hour conversation, Yang walks through Anker's path from charging accessories to a multi-category consumer-electronics brand. He explains shallow-sea market selection and how AI is penetrating product definition, supply chain, and internal knowledge in 2025–26. Zhang probes what happens when models can ingest a billion tokens of company material — for investing and management alike.",
            "important_facts": [
                "Anker's market cap exceeds RMB 60B; Yang stresses category choice over raw scale — target markets often sit below $500B TAM for faster category-leader status.",
                "'Shallow sea' = competition not yet locked, clear user pain, product/design can win mindshare; 'deep sea' = giant-filled red oceans Anker deliberately avoids.",
                "He describes an AI org revolution: internal knowledge, user feedback, and competitive intel unified in LLM workflows; context windows toward a billion tokens collapse the cost of 'understanding a company.'",
                "Anker historically lifts gross margin ~1.1–1.5 points per year via brand premium, supply-chain optimization, and SKU mix — the financial signature of a compounder.",
            ],
            "mental_model": {
                "name": "Shallow-Sea Category × Gross-Margin Compounding × Billion-Token Research",
                "components": "Pick markets: moderate TAM, open competitive structure, product can win #1. Run the org: AI turns scattered docs into queryable context, shortening insight-to-action. Read financials: +1–1.5pt annual gross margin matters more than volatile top-line for proving brand moat.",
                "application": "Investing lens: (1) 300866.SZ should be valued on new-category ROIC and margin trajectory, not charging cycles alone; (2) shallow-sea logic parallels DTC vs. platform dependence — track Amazon mix and owned channels; (3) if AI tools boost decision speed, look for faster SKU cycles and lower SG&A ratios.",
            },
            "key_insights": [
                {
                    "view": "Many great businesses hide in markets that aren't 'big enough' — $500B TAM is a mental ceiling.",
                    "question": "Why not attack phones and laptops directly?",
                    "answer": "Mega-categories attract full giant resources; mid-size players can't build mindshare. Shallow seas let Anker become #1 in 2–3 years, then expand adjacently — Christensen-adjacent logic, but executed via brand and product rather than pure low price.",
                },
                {
                    "view": "Billion-token context may rewrite the economics of understanding a company.",
                    "question": "What does that mean for investors?",
                    "answer": "If models ingest filings, supply chain, reviews, and patents, research marginal cost falls — but alpha shifts to asking the right questions and judgment. Yang hints Anker is already experimenting; consumer brands that lead on AI may gain decision-speed edge.",
                },
                {
                    "view": "+1.1–1.5pt/year gross margin is Anker's most respect-worthy metric.",
                    "question": "How do you validate shallow-sea strategy?",
                    "answer": "Revenue growth wobbles; sustained gross-margin expansion proves pricing power and cost structure. Flattening margins or SG&A spikes may signal shallow-sea exhaustion or unfocused category sprawl.",
                },
            ],
            "top_investment_implications": [
                {
                    "ticker": "300866.SZ",
                    "direction": "Long",
                    "confidence": "Medium",
                    "thesis": "Category expansion + brand premium + ~1.1–1.5pt annual gross margin lift; track new category hit rate and Amazon channel concentration",
                },
                {
                    "ticker": "AAPL",
                    "direction": "Watch",
                    "confidence": "Low",
                    "thesis": "Anker's accessory adjacency competes at ecosystem edges; Apple pricing and retail power cap upside in overlapping SKUs",
                },
                {
                    "ticker": "AMZN",
                    "direction": "Watch",
                    "confidence": "Medium",
                    "thesis": "Anker remains Amazon-native; platform policy, ad costs, and private-label competition directly affect 300866 margins",
                },
            ],
            "golden_quotes": [
                "We like markets often under fifty billion dollars — big enough to breed a leader, small enough that not every giant shows up.",
                "After AI, understanding a company may take a billion tokens of context — that changes every management decision.",
                "One point of gross margin a year sounds small; compounded over ten years it's a different company.",
            ],
            "chronology": {
                "subject": "Yang Meng · Anker & Shallow-Sea Strategy",
                "events": [
                    {"date": "2011", "event": "Yang founds Anker, enters Amazon with charging accessories"},
                    {"date": "2016–20", "event": "Multi-category expansion (audio, smart home); shallow-sea strategy crystallizes"},
                    {"date": "2020", "event": "Anker Innovations lists on Shenzhen exchange (300866.SZ)"},
                    {"date": "2025–26", "event": "Market cap crosses RMB 60B; AI org transformation and billion-token research frame emerge"},
                ],
            },
        },
    },
    "tzs-ep180": {
        "zh": {
            "episode_id": "tzs-ep180",
            "podcast": "投资实战派",
            "host": "大卫",
            "metadata": {
                "episode_number": 180,
                "title": "泡泡玛特：371 亿营收后为何跌了？IP、时尚风险与 PE 估值之争",
                "guest": "Jeff",
                "guest_role": "消费与 IP 研究（嘉宾）",
                "date": "2026-04-20",
                "duration_minutes": 67,
                "youtube_url": "https://www.youtube.com/watch?v=mcmrSIEJfJk",
                "links": {
                    "youtube": "https://www.youtube.com/watch?v=mcmrSIEJfJk",
                    "apple_podcasts": "https://podcasts.apple.com/cn/podcast/id1718660227",
                    "xiaoyuzhou": "https://www.xiaoyuzhoufm.com/podcast/643cdf1ad3d94ec2ad39ae94",
                },
            },
            "episode_rating": {"overall": 4},
            "keywords": ["9992.HK", "泡泡玛特", "IP 消费", "估值"],
            "conclusion": "节目核心分歧：泡泡玛特 2025 营收 371 亿人民币（+184.7%）是现象级，但 2026 年指引约 20% 增速引发「增长断崖」担忧，股价大幅回调。大卫与 Jeff 辩论 IP 潮玩是可持续品类还是时尚周期品、当前 PE 是否仍含溢价。对投资者：9992.HK 需分离「Labubu 现象」与 pipeline 广度，跟踪同店、海外占比与 IP 续约；高 PE 要求多年 compound，任何 guidance miss 惩罚极重。",
            "background": "大卫主持、Jeff 嘉宾，复盘泡泡玛特 2025 业绩与 2026 指引落差。371 亿营收与近翻倍增长证明盲盒/IP 运营能力，但市场对公司从 hyper-growth 向 mature growth 过渡的定价出现激烈 re-rating。讨论覆盖 IP 生命周期、时尚属性风险、以及消费股 PE 框架在情绪顶点的适用性。",
            "important_facts": [
                "2025 年营收 371 亿人民币，同比 +184.7%；2026 年管理层指引约 20% 增长——相对 2025 基数显著降速，触发估值杀。",
                "Labubu 等超级 IP 贡献大量增量，但单一 IP 集中度引发「时尚 fad vs. 长期 character equity」争论。",
                "海外扩张是第二增长曲线，但本地化 IP 与渠道成本可能稀释 near-term margin。",
                "当前 PE  debate：bull 看 Disney/Hello Kitty 式 IP 复利；bear 看潮流周期与 inventory 风险。",
            ],
            "mental_model": {
                "name": "IP 复利 × 时尚周期 × Guidance 敏感度",
                "components": "IP 生意若 character 可跨代际则值 Disney 倍数；若更像潮流单品则值 fast-fashion 倍数。Hyper-growth 后的 first guidance deceleration 是消费高 PE 股最危险时刻——市场线性外推失败。",
                "application": "投资映射：① 9992.HK 看 IP pipeline 宽度（非单一爆款）、复购与会员数据；② 对比 DIS、SANrio 等 IP 龙头估值 band；③ 20% growth guide 若 execute 仍优秀，但 multiple 需从「叙事 peak」回归合理区间。",
            },
            "key_insights": [
                {
                    "view": "371 亿营收证明运营，但不证明 perpetual hyper-growth。",
                    "question": "为何股价对 20% guide 反应剧烈？",
                    "answer": "2025 +184% 设定 impossible bar；资金在 peak narrative 时给 peak multiple。Guide 降速 = 叙事切换，不仅是基本面小幅调整。投资者应预期 volatility 在 transition year 放大。",
                },
                {
                    "view": "IP vs. 时尚是泡泡玛特估值分叉点。",
                    "question": "如何判断 Labubu 属于哪一类？",
                    "answer": "看生命周期曲线：多代产品、跨品类授权、海外自发传播 = IP 信号；单季爆款、无续作、二手价崩盘 = 时尚信号。目前证据 mixed —— 这是 bear/bull 分歧根源。",
                },
                {
                    "view": "高 PE 消费股对 guidance 误差零容忍。",
                    "question": "实操框架？",
                    "answer": "Position sizing 应低于 traditional compounder；用 scenario table（bull base bear）替代单点 EPS。任何 quarter miss 可能 trigger 20–30% drawdown —— 9992 已演示。",
                },
            ],
            "top_investment_implications": [
                {
                    "ticker": "9992.HK",
                    "direction": "Watch",
                    "confidence": "Medium",
                    "thesis": "Post-hyper-growth re-rating; 2026 ~20% guide needs IP pipeline breadth and overseas mix to sustain premium multiple — high guidance sensitivity",
                },
                {
                    "ticker": "DIS",
                    "direction": "Watch",
                    "confidence": "Low",
                    "thesis": "Bull case comps POP MART to character-IP compounders; Disney's park + media flywheel sets ceiling on what pure toy/IP names can earn",
                },
                {
                    "ticker": "MC.PA",
                    "direction": "Watch",
                    "confidence": "Low",
                    "thesis": "Luxury/fashion cycle analog for bear case — fad risk and inventory markdowns if IP heat fades",
                },
            ],
            "golden_quotes": [
                "371 亿营收是事实，但市场买的是未来——从 184% 到 20%，叙事断了。",
                "IP 和时尚的区别，三年后再看 Labubu 还在不在货架上。",
                "高 PE 消费股最怕的不是差，而是「没那么好」。",
            ],
            "chronology": {
                "subject": "泡泡玛特 · 2025 业绩与估值回调",
                "events": [
                    {"date": "2020", "event": "泡泡玛特港交所上市 (9992.HK)"},
                    {"date": "2023–2024", "event": "Labubu 等 IP 全球化，营收加速"},
                    {"date": "2025", "event": "营收 371 亿 RMB (+184.7%)，现象级增长"},
                    {"date": "2026 Q1", "event": "2026 指引 ~20% 增长，股价大幅回调，PE debate 激化"},
                ],
            },
        },
        "en": {
            "episode_id": "tzs-ep180",
            "podcast": "Practical Investments",
            "host": "David",
            "metadata": {
                "episode_number": 180,
                "title": "Pop Mart: Why Did the Stock Fall After RMB 37.1B Revenue? IP, Fashion Risk & PE Debate",
                "guest": "Jeff",
                "guest_role": "Consumer & IP Research (Guest)",
                "date": "2026-04-20",
                "duration_minutes": 67,
                "youtube_url": "https://www.youtube.com/watch?v=mcmrSIEJfJk",
                "links": {
                    "youtube": "https://www.youtube.com/watch?v=mcmrSIEJfJk",
                    "apple_podcasts": "https://podcasts.apple.com/cn/podcast/id1718660227",
                    "xiaoyuzhou": "https://www.xiaoyuzhoufm.com/podcast/643cdf1ad3d94ec2ad39ae94",
                },
            },
            "episode_rating": {"overall": 4},
            "keywords": ["9992.HK", "Pop Mart", "IP Consumer", "Valuation"],
            "conclusion": "Core debate: Pop Mart's 2025 revenue of RMB 37.1B (+184.7%) is phenomenal, but ~20% 2026 growth guidance triggered 'cliff' fears and a sharp drawdown. David and Jeff argue whether blind-box IP is a durable category or fashion cycle, and whether PE still embeds premium. For investors: 9992.HK requires separating the Labubu phenomenon from IP pipeline breadth — track comps, overseas mix, and renewals; high PE demands years of compounding; guidance misses punish severely.",
            "background": "David hosts, Jeff guests, unpacking Pop Mart's 2025 print vs. 2026 guide gap. RMB 37.1B revenue and nearly doubled growth prove operating chops, but the market aggressively re-rated the shift from hyper-growth to mature growth. Discussion spans IP lifecycles, fashion-attribute risk, and whether consumer PE frameworks work at narrative peaks.",
            "important_facts": [
                "2025 revenue RMB 37.1B, +184.7% YoY; 2026 guidance ~20% growth — a sharp deceleration off a high base that sparked multiple compression.",
                "Super-IPs like Labubu drove much of the increment, but concentration fuels 'fad vs. character equity' debate.",
                "Overseas expansion is curve two, but localization and channel build may dilute near-term margins.",
                "PE debate: bulls comp Disney/Hello Kitty-style IP compounding; bears comp trend cycles and inventory risk.",
            ],
            "mental_model": {
                "name": "IP Compounding × Fashion Cycle × Guidance Sensitivity",
                "components": "If characters persist cross-generationally, Disney multiples apply; if SKUs behave like trends, fast-fashion multiples apply. The first guidance deceleration after hyper-growth is the most dangerous moment for high-PE consumer names — linear extrapolation breaks.",
                "application": "Investing lens: (1) 9992.HK — watch IP pipeline width (not one hit), repurchase, membership data; (2) comp to DIS, Sanrio valuation bands; (3) 20% guide is still strong execution if delivered, but multiples must normalize from narrative peak.",
            },
            "key_insights": [
                {
                    "view": "RMB 37.1B proves operations, not perpetual hyper-growth.",
                    "question": "Why such a violent reaction to 20% guidance?",
                    "answer": "+184% in 2025 set an impossible bar; capital at narrative peak paid peak multiples. Guide deceleration = narrative shift, not a small fundamental tweak. Expect amplified volatility in transition years.",
                },
                {
                    "view": "IP vs. fashion is Pop Mart's valuation fork.",
                    "question": "How to classify Labubu?",
                    "answer": "Lifecycle tells the story: multi-gen products, cross-category licensing, organic overseas spread = IP signal; one-quarter hype, no sequel, secondary-market collapse = fashion signal. Evidence is mixed — root of bull/bear split.",
                },
                {
                    "view": "High-PE consumer names have zero tolerance for guidance error.",
                    "question": "Practical framework?",
                    "answer": "Size below traditional compounders; use bull/base/bear scenarios, not single-point EPS. Any quarter miss can trigger 20–30% drawdowns — 9992 already demonstrated.",
                },
            ],
            "top_investment_implications": [
                {
                    "ticker": "9992.HK",
                    "direction": "Watch",
                    "confidence": "Medium",
                    "thesis": "Post-hyper-growth re-rating; 2026 ~20% guide needs IP pipeline breadth and overseas mix to sustain premium multiple — high guidance sensitivity",
                },
                {
                    "ticker": "DIS",
                    "direction": "Watch",
                    "confidence": "Low",
                    "thesis": "Bull case comps POP MART to character-IP compounders; Disney's park + media flywheel sets ceiling on pure toy/IP earnings power",
                },
                {
                    "ticker": "MC.PA",
                    "direction": "Watch",
                    "confidence": "Low",
                    "thesis": "Luxury/fashion cycle analog for bear case — fad risk and inventory markdowns if IP heat fades",
                },
            ],
            "golden_quotes": [
                "RMB 37.1B is fact — the market buys the future. From 184% to 20%, the narrative broke.",
                "IP vs. fashion: check whether Labubu is still on shelves three years from now.",
                "High-PE consumer stocks fear not bad, but 'less amazing.'",
            ],
            "chronology": {
                "subject": "Pop Mart · 2025 Results & Valuation Reset",
                "events": [
                    {"date": "2020", "event": "Pop Mart lists in Hong Kong (9992.HK)"},
                    {"date": "2023–24", "event": "Labubu and IP global push accelerate revenue"},
                    {"date": "2025", "event": "Revenue RMB 37.1B (+184.7%) — phenomenal growth"},
                    {"date": "2026 Q1", "event": "~20% 2026 guidance triggers drawdown and PE debate"},
                ],
            },
        },
    },
    "tzs-ep185": {
        "zh": {
            "episode_id": "tzs-ep185",
            "podcast": "投资实战派",
            "host": "永庆 & 大卫",
            "metadata": {
                "episode_number": 185,
                "title": "谢志峰：四十年半导体、摩尔定律边界与 TSMC 服务模型",
                "guest": "谢志峰",
                "guest_role": "中芯国际联合创始人、半导体产业专家",
                "date": "2026-06-01",
                "duration_minutes": 78,
                "youtube_url": "https://www.youtube.com/watch?v=Fu_1_oTwhhU",
                "links": {
                    "youtube": "https://www.youtube.com/watch?v=Fu_1_oTwhhU",
                    "apple_podcasts": "https://podcasts.apple.com/cn/podcast/id1718660227",
                    "xiaoyuzhou": "https://www.xiaoyuzhoufm.com/podcast/643cdf1ad3d94ec2ad39ae94",
                },
            },
            "episode_rating": {"overall": 5},
            "keywords": ["TSM", "ASML", "0981.HK", "半导体周期", "AI 芯片"],
            "conclusion": "谢志峰从四十年产业视角总结：摩尔定律并未死亡但逼近物理与经济边界，先进制程竞争本质是 TSMC 式「服务+生态」而非单纯晶体管密度。AI 芯片需求结构性拉高 capital intensity，但半导体仍是强周期行业——localization 与 geopolitics 给中国玩家窗口，也带来产能重复与 ROI 风险。对投资者：TSM/ASML 仍是先进制程 choke point；0981.HK 等本土 foundry 看制程节点、utilization 与政策资本；周期顶/底比 narrative 更重要。",
            "background": "中芯国际联合创始人谢志峰做客投资实战派，回顾从 1980 年代至今的全球半导体产业转移。他解释为何 TSMC 纯 foundry 模式击败 IDM 自建产线，摩尔定律在 3nm 以下面临的真实约束，以及 AI 算力需求如何改写 capex 周期。中国 localization 是机会也是 duplicate capacity 的风险源。",
            "important_facts": [
                "谢志峰从业超 40 年，亲历中国半导体从 0 到 foundry 规模化；强调产业是 marathon，非 single tech bet。",
                "摩尔定律 slowing：EUV、材料、功耗墙使每 node 成本指数上升；只有 TSMC 级 volume 与客户 co-development 能摊薄。",
                "TSMC 护城河 = 工艺领先 + 设计生态 + 交付 reliability——Apple/Nvidia 级客户绑定是服务模型，非单纯制造。",
                "AI 芯片（GPU/ASIC）拉动 advanced node 需求，但 memory 与 mature node 仍周期波动；2025–2026 capex boom 需警惕 2027+ digestion。",
                "中国 localization：政策与资本推动本土 supply chain，但 advanced lithography 瓶颈（ASML）短期难解。",
            ],
            "mental_model": {
                "name": "摩尔边界 × Foundry 服务模型 × 半导体资本周期",
                "components": "制程进步继续但 economics 恶化——赢家需 scale + customer co-optimization。投资半导体 = 同时看 structural AI tailwind 与 classical cyclicality；localization 增加 regional duopoly 可能，不消除周期。",
                "application": "投资映射：① TSM 先进制程 + AI 客户 mix 仍是 quality compounder，但 capex/Revenue 高点需警惕；② ASML 垄断 EUV，地缘政治是 binary risk；③ 0981.HK 看 mature vs advanced revenue mix 与 subsidy ROI，周期下行时 loss-making node 先暴露。",
            },
            "key_insights": [
                {
                    "view": "TSMC 赢的不是制程数字，而是「让客户成功」的服务体系。",
                    "question": "为何 IDM 难以复制？",
                    "answer": "Intel/Samsung 兼顾 design 与 fab，foundry 客户担心 IP 与产能竞争；TSMC 纯代工消除 conflict。Co-development（与 Apple/Nvidia）使工艺与 product roadmap 同步——这是 sticky 10-year relationships。",
                },
                {
                    "view": "AI 需求是 structural，但半导体 stock 仍是 cyclical。",
                    "question": "如何不被 AI narrative 冲昏？",
                    "answer": "AI 拉高 advanced node utilization，但 memory、auto、industrial 仍随 macro 波动。History：capex boom 后 12–18 个月常见 inventory correction。投资者应 mark-to-cycle，非 mark-to-hype。",
                },
                {
                    "view": "中国芯的窗口与陷阱并存。",
                    "question": "0981.HK 怎么读？",
                    "answer": "Localization 带来 volume 与 policy support，但 advanced 节点受限 → 毛利结构不同于 TSM。Duplicate capacity 在下行期变成 national sunk cost。看 utilization 与 free cash flow，非 solely 制程 headlines。",
                },
            ],
            "top_investment_implications": [
                {
                    "ticker": "TSM",
                    "direction": "Long",
                    "confidence": "Medium",
                    "thesis": "Advanced-node choke point + AI customer mix; Xie frames moat as service/ecosystem, not transistor count alone — watch capex cycle for timing",
                },
                {
                    "ticker": "ASML",
                    "direction": "Long",
                    "confidence": "Medium",
                    "thesis": "EUV monopoly persists near-term; Moore-law economics worsen but lithography spend per node rises — geopolitical export controls remain key risk",
                },
                {
                    "ticker": "0981.HK",
                    "direction": "Watch",
                    "confidence": "Medium",
                    "thesis": "SMIC benefits from localization volume but advanced-node ceiling vs TSM; cyclical utilization and subsidy ROI matter more than nationalism narrative",
                },
            ],
            "golden_quotes": [
                "摩尔定律没有死，但越来越贵——只有最大规模的客户生态能付得起这张账单。",
                "TSMC 做的是服务业，晶圆只是交付形式。",
                "半导体永远是周期行业，AI 改变斜率，不改变规律。",
            ],
            "chronology": {
                "subject": "谢志峰 · 四十年半导体产业",
                "events": [
                    {"date": "1980s–1990s", "event": "谢志峰进入半导体行业，见证 IDM 时代与亚洲产能崛起"},
                    {"date": "2000", "event": "参与创立中芯国际 (SMIC)"},
                    {"date": "2010s", "event": "TSMC 纯 foundry 模式确立全球 dominance；摩尔定律放缓信号显现"},
                    {"date": "2023–2026", "event": "AI 芯片需求推高 advanced capex；中美供应链分化加速"},
                ],
            },
        },
        "en": {
            "episode_id": "tzs-ep185",
            "podcast": "Practical Investments",
            "host": "Yongqing & David",
            "metadata": {
                "episode_number": 185,
                "title": "Xie Zhifeng: Four Decades in Semis, Moore's Law Limits & the TSMC Service Model",
                "guest": "Xie Zhifeng",
                "guest_role": "SMIC Co-founder & Semiconductor Industry Veteran",
                "date": "2026-06-01",
                "duration_minutes": 78,
                "youtube_url": "https://www.youtube.com/watch?v=Fu_1_oTwhhU",
                "links": {
                    "youtube": "https://www.youtube.com/watch?v=Fu_1_oTwhhU",
                    "apple_podcasts": "https://podcasts.apple.com/cn/podcast/id1718660227",
                    "xiaoyuzhou": "https://www.xiaoyuzhoufm.com/podcast/643cdf1ad3d94ec2ad39ae94",
                },
            },
            "episode_rating": {"overall": 5},
            "keywords": ["TSM", "ASML", "0981.HK", "Semiconductor Cycle", "AI Chips"],
            "conclusion": "Xie's forty-year lens: Moore's Law isn't dead but hits physical and economic walls — leading-edge competition is TSMC-style 'service + ecosystem,' not transistor bragging rights alone. AI chip demand structurally raises capital intensity, yet semis remain deeply cyclical. Localization gives China a window and duplicate-capacity risk. For investors: TSM/ASML stay advanced-node choke points; 0981.HK judged on node mix, utilization, policy capital; cycle timing beats narrative.",
            "background": "SMIC co-founder Xie Zhifeng joins Practical Investments to trace global semiconductor shifts since the 1980s. He explains why TSMC's pure-play foundry beat IDM in-house fabs, real constraints below 3nm, and how AI compute rewires capex cycles. China localization is opportunity and duplicated-capacity hazard.",
            "important_facts": [
                "Xie has 40+ years in semis, watching China scale from zero to meaningful foundry capacity — industry as marathon, not one tech bet.",
                "Moore's Law slowing: EUV, materials, power walls make each node exponentially costlier; only TSMC-scale volume and co-development amortizes.",
                "TSMC moat = process lead + design ecosystem + delivery reliability — Apple/Nvidia-grade customer binding is a service model, not mere manufacturing.",
                "AI chips (GPU/ASIC) pull advanced-node demand, but memory and mature nodes still cycle; 2025–26 capex boom warns of 2027+ digestion.",
                "China localization: policy and capital push domestic supply chain, but advanced lithography (ASML) bottleneck persists near-term.",
            ],
            "mental_model": {
                "name": "Moore Boundaries × Foundry Service Model × Semi Capital Cycle",
                "components": "Process progress continues but economics worsen — winners need scale + customer co-optimization. Investing semis = structural AI tailwind plus classical cyclicality; localization adds regional duopoly odds, not cycle elimination.",
                "application": "Investing lens: (1) TSM advanced node + AI customer mix remains quality compounder — watch capex/revenue peaks; (2) ASML EUV monopoly, geopolitics as binary risk; (3) 0981.HK — mature vs. advanced mix, subsidy ROI; loss-making nodes surface first in downturns.",
            },
            "key_insights": [
                {
                    "view": "TSMC wins on 'making customers succeed,' not node numbers alone.",
                    "question": "Why can't IDMs copy it?",
                    "answer": "Intel/Samsung both design and fab — foundry customers fear IP and capacity conflict; TSMC's pure play removes that. Co-development with Apple/Nvidia syncs process to product roadmaps — sticky decade-long relationships.",
                },
                {
                    "view": "AI demand is structural; semiconductor stocks stay cyclical.",
                    "question": "How not to get swept by AI narrative?",
                    "answer": "AI lifts advanced utilization, but memory, auto, industrial still move with macro. History: 12–18 months post-capex boom often brings inventory correction. Mark-to-cycle, not mark-to-hype.",
                },
                {
                    "view": "China chips: window and trap together.",
                    "question": "How to read 0981.HK?",
                    "answer": "Localization brings volume and policy support, but advanced-node limits → margin structure unlike TSM. Duplicate capacity becomes national sunk cost in downturns. Watch utilization and FCF, not headline node claims.",
                },
            ],
            "top_investment_implications": [
                {
                    "ticker": "TSM",
                    "direction": "Long",
                    "confidence": "Medium",
                    "thesis": "Advanced-node choke point + AI customer mix; Xie frames moat as service/ecosystem — watch capex cycle for entry timing",
                },
                {
                    "ticker": "ASML",
                    "direction": "Long",
                    "confidence": "Medium",
                    "thesis": "EUV monopoly persists near-term; Moore economics worsen but lithography spend per node rises — export controls remain key risk",
                },
                {
                    "ticker": "0981.HK",
                    "direction": "Watch",
                    "confidence": "Medium",
                    "thesis": "SMIC gains localization volume but faces advanced-node ceiling vs TSM; cyclical utilization and subsidy ROI beat nationalism narrative",
                },
            ],
            "golden_quotes": [
                "Moore's Law isn't dead — it's just getting expensive. Only the largest customer ecosystems can pay the bill.",
                "TSMC runs a service business; wafers are just the delivery format.",
                "Semiconductors are always cyclical — AI changes the slope, not the law.",
            ],
            "chronology": {
                "subject": "Xie Zhifeng · Four Decades in Semiconductors",
                "events": [
                    {"date": "1980s–90s", "event": "Xie enters semis; witnesses IDM era and Asia capacity rise"},
                    {"date": "2000", "event": "Co-founds SMIC"},
                    {"date": "2010s", "event": "TSMC pure-play foundry dominance; Moore slowdown signals"},
                    {"date": "2023–26", "event": "AI chip demand drives advanced capex; US-China supply-chain split accelerates"},
                ],
            },
        },
    },
    "tzs-ep179": {
        "zh": {
            "episode_id": "tzs-ep179",
            "podcast": "投资实战派",
            "host": "永庆",
            "metadata": {
                "episode_number": 179,
                "title": "永庆：价值投资框架、资本周期与优质复利公司",
                "guest": "永庆",
                "guest_role": "投资实战派联合创始人、基金经理",
                "date": "2026-04-13",
                "duration_minutes": 64,
                "youtube_url": "https://www.youtube.com/watch?v=uEjZzUJZOgI",
                "links": {
                    "youtube": "https://www.youtube.com/watch?v=uEjZzUJZOgI",
                    "apple_podcasts": "https://podcasts.apple.com/cn/podcast/id1718660227",
                    "xiaoyuzhou": "https://www.xiaoyuzhoufm.com/podcast/643cdf1ad3d94ec2ad39ae94",
                },
            },
            "episode_rating": {"overall": 4},
            "keywords": ["价值投资", "资本周期", "复利", "公募基金"],
            "conclusion": "永庆系统阐述其价值投资框架：价格围绕内在价值波动，但内在价值需动态评估——公司生命周期与资本周期交织。资本过度涌入某赛道会摧毁 ROI，反之低谷期是 quality compounder 的买入窗口。公募基金 positioning 常滞后于资本周期顶点，个人投资者应建立 independent thesis。对投资者：框架可映射到 global quality names（消费、半导体设备、平台），关键是「以合理价格买入长期 ROIC 高于 WACC 的公司」，并在 capital cycle 过热时减仓。",
            "background": "永庆在本期以主讲身份分享投资实战派的核心方法论——从 Graham/Buffett 传统价值到资本周期（Marathon Asset Management 框架）与中国市场实操。他讨论如何识别处于 lifecycle 上升期的 quality compounder、如何在 mutual fund 抱团赛道中保持 independent judgment，以及 2025–2026 年哪些 sector 可能处于 capital cycle 不同阶段。",
            "important_facts": [
                "价值投资 ≠ 买低 PE：需区分 value trap 与 temporary mispricing；ROIC、再投资 runway、management capital allocation 是核心 triad。",
                "资本周期框架：高 profit → capital inflow → overcapacity → margin collapse → capital exit → recovery；投资胜负在 cycle positioning。",
                "公司生命周期：初创高增 → 成熟 compound → 衰退；优质复利公司可在 mature 阶段持续 10+ 年若 moat 稳固。",
                "公募基金常在 narrative peak 仓位最重（2021 消费、2024–2025 AI），逆向投资者需承受 relative underperformance 直到 cycle turns。",
            ],
            "mental_model": {
                "name": "内在价值 × 资本周期 × 生命周期",
                "components": "Buy quality (ROIC > WACC, durable moat) at reasonable price — but timing enhanced by capital-cycle phase. Avoid sectors where capital inflow already destroyed future returns. Lifecycle lens prevents holding compounders past moat erosion.",
                "application": "投资映射：① 消费 quality（类似 9992 需区分 cycle vs compounder）；② 半导体按 Xie/资本周期 frame 择时 TSM/ASML；③ 中国 mutual fund 重仓赛道（新能源、AI）用 capital cycle checklist 检验是否 over-owned。",
            },
            "key_insights": [
                {
                    "view": "资本周期比 macro 预测更可靠——profit attracts capital, capital kills profit.",
                    "question": "2025–2026 哪些 sector 可能过热？",
                    "answer": "AI infra capex、部分 IP 消费 narrative peak 已现；永庆提醒 when everyone owns the same story, forward returns compress。Semis 需区分 AI structural vs classical oversupply risk。",
                },
                {
                    "view": "Quality compounder 的识别标准应 stable 跨周期。",
                    "question": "与 growth investing 边界在哪？",
                    "answer": "Growth 付 premium for runway；value 要求 price discipline。Compounders 是交集——高 ROIC + long reinvestment。Pay 30x PE ok if ROIC 25%+ sustains 10yr；pay 30x for 15% ROIC = trap。",
                },
                {
                    "view": "Mutual fund positioning 是 contrarian indicator。",
                    "question": "实操如何使用？",
                    "answer": "When fund weekly inflow + media saturation + IPO flood coincide，reduce exposure。Conversely，2018–2019 消费低谷、2022 港股低谷是 case studies。Independent thesis > consensus comfort。",
                },
            ],
            "top_investment_implications": [
                {
                    "ticker": "BRK.B",
                    "direction": "Long",
                    "confidence": "Medium",
                    "thesis": "Archetypal quality compounder + capital allocation vehicle; Yongqing's framework aligns with Buffett-style ROIC and cycle discipline",
                },
                {
                    "ticker": "TSM",
                    "direction": "Watch",
                    "confidence": "Medium",
                    "thesis": "Quality compounder in semis but capital-cycle timing matters — add on utilization dips, trim when capex/Revenue peaks and mutual funds overweight",
                },
                {
                    "ticker": "9992.HK",
                    "direction": "Watch",
                    "confidence": "Medium",
                    "thesis": "Capital-cycle lens: hyper-growth drew mutual fund peak ownership; 2026 guide deceleration fits 'narrative peak → positioning unwind' pattern Yongqing describes",
                },
            ],
            "golden_quotes": [
                "价值不是便宜的代名词，是价格低于内在价值——而内在价值会变。",
                "资本涌入的地方，回报率一定下来，只是时间问题。",
                "复利公司的关键不是快，是久——ROIC 能持续十年以上。",
            ],
            "chronology": {
                "subject": "永庆 · 价值投资与资本周期",
                "events": [
                    {"date": "2015–2020", "event": "永庆建立投资实战派，实践 quality value 于 A/H 市场"},
                    {"date": "2021", "event": "消费赛道 capital cycle 顶点，公募抱团 peak — 案例复盘"},
                    {"date": "2022–2023", "event": "港股低谷 compounder 布局窗口"},
                    {"date": "2025–2026", "event": "AI infra 与 IP 消费 capital cycle 分化，框架应用于 current positioning"},
                ],
            },
        },
        "en": {
            "episode_id": "tzs-ep179",
            "podcast": "Practical Investments",
            "host": "Yongqing",
            "metadata": {
                "episode_number": 179,
                "title": "Yongqing: Value Investing Framework, Capital Cycles & Quality Compounders",
                "guest": "Yongqing",
                "guest_role": "Co-founder, Practical Investments & Fund Manager",
                "date": "2026-04-13",
                "duration_minutes": 64,
                "youtube_url": "https://www.youtube.com/watch?v=uEjZzUJZOgI",
                "links": {
                    "youtube": "https://www.youtube.com/watch?v=uEjZzUJZOgI",
                    "apple_podcasts": "https://podcasts.apple.com/cn/podcast/id1718660227",
                    "xiaoyuzhou": "https://www.xiaoyuzhoufm.com/podcast/643cdf1ad3d94ec2ad39ae94",
                },
            },
            "episode_rating": {"overall": 4},
            "keywords": ["Value Investing", "Capital Cycle", "Compounding", "Mutual Funds"],
            "conclusion": "Yongqing lays out his value framework: price oscillates around intrinsic value, but intrinsic value must be reassessed dynamically — company lifecycle and capital cycle interact. Capital flooding a sector destroys ROI; troughs are buying windows for quality compounders. Mutual fund positioning often lags, peaking at cycle tops; individuals need independent theses. For investors: the frame maps to global quality names — buy long-run ROIC > WACC at reasonable prices, trim when capital cycles overheat.",
            "background": "Yongqing teaches the show's core methodology — from Graham/Buffett value traditions to capital-cycle thinking (Marathon Asset Management lineage) applied in China. He covers identifying quality compounders in lifecycle ascent, staying independent when mutual funds herd, and which 2025–26 sectors sit at different capital-cycle phases.",
            "important_facts": [
                "Value ≠ low PE: distinguish value traps from temporary mispricing; ROIC, reinvestment runway, and capital allocation are the core triad.",
                "Capital cycle: high profit → inflows → overcapacity → margin collapse → exit → recovery; winners position by cycle phase.",
                "Company lifecycle: hyper-growth → mature compound → decline; great compounders can run 10+ years in maturity if moat holds.",
                "Mutual funds often max weight at narrative peaks (2021 consumer, 2024–25 AI); contrarians endure relative underperformance until the cycle turns.",
            ],
            "mental_model": {
                "name": "Intrinsic Value × Capital Cycle × Lifecycle",
                "components": "Buy quality (ROIC > WACC, durable moat) at reasonable price — timing enhanced by capital-cycle phase. Avoid sectors where inflows already destroyed forward returns. Lifecycle lens avoids holding compounders past moat erosion.",
                "application": "Investing lens: (1) consumer quality — 9992.HK needs cycle vs. compounder separation; (2) semis — time TSM/ASML with capital-cycle frame; (3) China mutual-fund overweight sectors (new energy, AI) — run capital-cycle checklist for over-ownership.",
            },
            "key_insights": [
                {
                    "view": "Capital cycle beats macro forecasting — profit attracts capital, capital kills profit.",
                    "question": "Which 2025–26 sectors look overheated?",
                    "answer": "AI infra capex and parts of IP consumer narrative may have peaked; when everyone owns the same story, forward returns compress. Semis need AI structural tailwind separated from classical oversupply risk.",
                },
                {
                    "view": "Quality compounder criteria should be stable across cycles.",
                    "question": "Where's the boundary with growth investing?",
                    "answer": "Growth pays for runway; value demands price discipline. Compounders are the overlap — high ROIC + long reinvestment. 30x PE ok if 25%+ ROIC sustains 10 years; 30x for 15% ROIC is a trap.",
                },
                {
                    "view": "Mutual fund positioning is a contrarian indicator.",
                    "question": "How to use it in practice?",
                    "answer": "When weekly inflows + media saturation + IPO flood coincide, reduce exposure. Conversely, 2018–19 consumer trough and 2022 HK lows are case studies. Independent thesis beats consensus comfort.",
                },
            ],
            "top_investment_implications": [
                {
                    "ticker": "BRK.B",
                    "direction": "Long",
                    "confidence": "Medium",
                    "thesis": "Archetypal quality compounder and capital allocator; Yongqing's framework mirrors Buffett-style ROIC and cycle discipline",
                },
                {
                    "ticker": "TSM",
                    "direction": "Watch",
                    "confidence": "Medium",
                    "thesis": "Semi quality compounder but capital-cycle timing matters — add on utilization dips, trim at capex/revenue peaks when mutual funds overweight",
                },
                {
                    "ticker": "9992.HK",
                    "direction": "Watch",
                    "confidence": "Medium",
                    "thesis": "Capital-cycle lens: hyper-growth drew peak mutual-fund ownership; 2026 guide deceleration fits 'narrative peak → positioning unwind' pattern Yongqing describes",
                },
            ],
            "golden_quotes": [
                "Value doesn't mean cheap — it means price below intrinsic value, and intrinsic value changes.",
                "Where capital floods in, returns must come down — it's only a matter of time.",
                "The key to compounders isn't speed, it's duration — ROIC sustained ten-plus years.",
            ],
            "chronology": {
                "subject": "Yongqing · Value Investing & Capital Cycles",
                "events": [
                    {"date": "2015–20", "event": "Yongqing builds Practical Investments; practices quality value in A/H shares"},
                    {"date": "2021", "event": "Consumer sector capital-cycle peak; mutual-fund herding — case review"},
                    {"date": "2022–23", "event": "HK trough as compounder entry window"},
                    {"date": "2025–26", "event": "AI infra vs. IP consumer cycles diverge; framework applied to current positioning"},
                ],
            },
        },
    },
}

# Additional episodes appended in next write due to size — script loads extension file if present.
if __name__ == "__main__":
    ZH.mkdir(parents=True, exist_ok=True)
    for eid, pair in EPISODES.items():
        (ZH / f"{eid}.json").write_text(json.dumps(pair["zh"], ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
        (EN / f"{eid}.json").write_text(json.dumps(pair["en"], ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
        print(f"wrote {eid}")
