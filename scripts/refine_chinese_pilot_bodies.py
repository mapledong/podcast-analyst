"""Clean body content for refine_chinese_pilot.py (no metadata/episode_rating)."""

from __future__ import annotations

from typing import Any

from refine_new_episodes_bodies import NEW_EPISODES

_REFINED_BASE: dict[str, dict[str, dict[str, Any]]] = {
    "zj-ep140": {
        "en": {
            "keywords": ['GOOGL', 'AI Frontier Labs', 'Model Training'],
            "conclusion": "After training at Anthropic and joining Google's Gemini team in late 2025, Yao Shunyu argues frontier labs no longer fear falling behind on raw capability — they fear picking the wrong product bet. Benchmark gaps among OpenAI, Anthropic, and Google have narrowed; retention now turns on workflow lock-in, distribution, and reliability, not hero narratives. He puts Gemini consumer share at roughly twenty percent and cites Doubao's voice UX as proof regional product fit can win without global IQ leadership. Investors should underwrite commercial paths — coding agents, search/Android funnels, enterprise attach — rather than leaderboard deltas.",
            "background": "In a 228-minute interview Zhang Xiaojun speaks with Yao Shunyu, who trained models at Anthropic before joining Google DeepMind's Gemini team in late 2025. He lived through the 2025–26 release wave — reasoning jumps, coding agents, image tools — and watched anxiety flip from 'can we build it?' to 'what should we bet on?' He compares frontier labs to surfers on one wave: the wave is shared; taste, speed, and reliability separate winners. OpenAI still owns mindshare, but benchmark gaps among OpenAI, Anthropic, and Google have narrowed enough that product definition matters more than another five IQ points. ChatGPT still sets consumer defaults even when public benchmarks converge. Yao stresses reliability over heroism when frontier labs converge on capability. Most users do not perceive five-point benchmark IQ differences. Hero narratives help hiring but do not justify billion-dollar training capex alone. Investors should track ARR paths for coding enterprise and consumer segments. Dario Amodei publicly named distillers defending Anthropic model IP. Wall-street diligence should weight Gemini retention cohorts and enterprise attach over single benchmark releases.",
            "important_facts": [
                "By 2025–26 Yao says OpenAI, Anthropic, and Google look much closer on public benchmarks than a year earlier, when Anthropic still feared OpenAI's reasoning lead. The harder problem now is choosing the right product bet — coding agents, consumer hits, enterprise workflows — not raw capability. Most users barely perceive small IQ gaps; speed, price, and usefulness drive retention. Training is increasingly an engineering-organization problem: data pipelines, eval discipline, and product loops beat one-off research wins. Startups can make top-down workflow bets faster than multi-product giants can align incentives. He joined Gemini in late 2025 after Anthropic training experience. Speed usefulness and price drive consumer AI adoption more than leaderboard rank. 2026 is a year of bet clarification not capability miracles for frontier labs. Search and Android distribution are unique GOOGL advantages if retention follows. OpenAI mindshare still dominates even as benchmark gaps narrow. Frontier labs now compete on eval transparency and product ownership culture as much as on pre-training scale.",
                "Regional optimization diverges. Doubao's voice generation feels best for everyday Chinese scenarios — low latency, local data, conversational UX — while US users weight coding and deep reasoning. Yao joined Gemini after interviewing Anthropic, OpenAI, and DeepMind; he picked Anthropic first on interview pace, then moved to Google when volume and distribution became the battleground. He guesses Gemini consumer share is roughly twenty percent today — a working estimate, not a bull case — and stresses Google must chain consumer hits before flagship models retain users. Claude Code validates Anthropic's coding and agent commercialization path in the US. He guesses Gemini holds roughly twenty percent consumer share today. Product bet clarity matters more than raw model intelligence now. Investors treating any one lab as permanent winner misread a convergence cycle where distribution and workflow lock-in decide economics.",
                'Dario Amodei publicly named companies distilling Anthropic models, signaling top labs defend IP and data loops as capabilities flatten. Yao argues the heroism era is over: the scarcest trait is reliability — detail orientation, eval transparency, ownership of outcomes. Distillation disputes may become recurring legal and partnership friction. 2026 diligence should track commercial recurring revenue paths and retention cohorts for coding, enterprise, and consumer segments — not parameter counts or leaderboard rank alone. Doubao voice UX leads daily Chinese scenarios versus Gemini and Claude. Startups can make top-down workflow bets faster than aligned big companies. Legal friction around distillation and data rights may become a recurring line item as model differentiation compresses.',
            ],
            "mental_model": {
                "name": 'Capability Convergence × Product Bet × Reliable Execution',
                "components": "As benchmark gaps compress, edge shifts from raw intelligence to 'for whom, solving what.' Convergence plus a reliability filter: underwrite go-to-market and retention, not leaderboard deltas. Late-2025 Gemini hiring marks Google's volume war; a ~20% share guess frames upside if consumer hits chain and downside if retention stalls. Doubao proves regional UX can win local share without global IQ leadership; Claude Code proves workflow lock-in monetizes before the next model drop. Product bet clarity matters more than raw intelligence when gaps under five points go unnoticed by mainstream users. Claude Code validates Anthropic's coding and agent workflow commercial bet. Training is increasingly an engineering organization and eval discipline problem.",
                "application": 'Sizing: Alphabet (GOOGL) as distribution compounder with AI optionality — search plus Android are unique levers if Gemini retention follows. Anthropic as a coding and agent pure play; avoid treating any single lab as permanent winner. Monitor distillation disputes and enterprise churn. China voice UX leaders may capture share without winning global benchmarks. Barbell portfolio: Alphabet distribution option, private lab workflow bets, China scene winners by UX not IQ. 2026 checklist: product bet clarity, eval transparency, commercial ARR paths — not capability miracles. Data pipelines and product loops beat one-off research paper wins. Watch quarterly commercial recurring revenue in coding and consumer segments as the falsifiable test of product bets.',
            },
            "key_insights": [
                {
                    "view": 'AI has entered a phase of worrying whether problems are well-defined, not whether models can solve them.',
                    "question": 'Where does differentiation come from after convergence?',
                    "answer": "Product bets and taste, not five-point benchmark gaps. Anthropic leaned into Claude Code for coding and agent workflows; Google needs consumer hits to pull volume, then flagship Gemini models to hold it. Users feel 'fast, useful, cheap' far more than leaderboard rank. Track Gemini app retention, enterprise attach, and search integration quarterly — not parameter releases alone. Regional optimization can win local share without global IQ leadership. Workflow-embedded products monetize before the next capability jump — Claude Code is the clearest US example today.",
                },
                {
                    "view": "OpenAI's share is so high that stumbles hurt less at the margin; Google must win the volume game.",
                    "question": "Why does Yao's ~20% Gemini share guess matter for investors?",
                    "answer": "ChatGPT still owns mindshare, so Google's fight is distribution conversion, not lab prestige. Yao joined Gemini in late 2025 precisely when pulling consumer volume back became existential. Search and Android are GOOGL's unique levers — but only if product hits chain and retention cohorts hold. Treat ~20% as a working estimate to stress-test upside and stall scenarios without treating it as a bull case. Alphabet's search and Android funnel remains worthless without consecutive consumer hits that feed flagship retention.",
                },
                {
                    "view": 'The heroism era is over — steady delivery beats genius mythology.',
                    "question": 'What does that mean for teams and capital?',
                    "answer": "Training becomes an engineering and organization war: data, evals, and product loops matter more than lone-researcher narratives. Yao quips the industry 'doesn't need brains, it needs reliability' — speculative punts narrow, teams that ship commercial results command a premium. 2026 is a bet-clarification year for frontier labs, not a capability-miracle year — hero narratives help recruiting but do not justify billion-dollar training spend alone. Capital should prefer teams with eval discipline and shipping records over hero-founder narratives at scale.",
                },
            ],
            "top_investment_implications": [
                {
                    "ticker": 'GOOGL',
                    "direction": 'Long',
                    "confidence": 'Medium',
                    "thesis": "Alphabet (GOOGL): Gemini consumer push plus search and Android distribution — Yao frames late-2025 hiring as Google's volume war; ~20% share guess implies room if retention chains",
                },
                {
                    "ticker": 'Private:Anthropic',
                    "direction": 'Watch',
                    "confidence": 'Medium',
                    "thesis": 'Coding and agent workflow bet leads via Claude Code, but distillation pressure rises as capabilities converge — must prove durable enterprise ARR and lock-in, not benchmark wins',
                },
                {
                    "ticker": 'NVDA',
                    "direction": 'Long',
                    "confidence": 'Low',
                    "thesis": 'Nvidia (NVDA): multi-frontier training capex persists as model alpha compresses — chip layer benefits regardless of which product bet wins',
                },
            ],
            "golden_quotes": ["Everyone is a surfer on the same wave — it's the wave, not the surfer, that matters.", 'People worry less about whether AI can do it, and more about whether the problem is well defined.', "This industry's most important trait is reliability — doing careful work and owning the outcome."],
            "chronology": {
                "subject": 'Yao Shunyu · Frontier Model Training',
                "events": [
                    {'date': 'GPT-3 era', 'event': 'Yao enters field during scaling narrative'},
                    {'date': '2023–24', 'event': 'Industry pivots to reasoning; Anthropic fears OpenAI lead'},
                    {'date': 'Mid-2025', 'event': 'Claude Code catalyzes coding commercialization'},
                    {'date': 'Late 2025', 'event': 'Yao leaves Anthropic for Google DeepMind Gemini team'},
                    {'date': '2026', 'event': 'Top-three capability converging; product definition is the battleground'},
                ],
            },
        },
        "zh": {
            "keywords": ['GOOGL', 'AI 前沿实验室', '模型训练'],
            "conclusion": '姚顺宇在 Anthropic 参与训练、2025 年末加入 Google Gemini 团队后判断：前沿实验室的焦虑已从「模型够不够强」转为「该押哪条产品路线」。OpenAI、Anthropic、Google 在公开基准上差距收窄，差异化转向工作流锁定、分发渠道与执行纪律——他称之为「靠谱」，而非英雄叙事。顺宇估计 Gemini 消费端市占约两成（工作假设），并以豆包语音体验说明区域产品适配可赢而不必全球智能第一。对投资者：应跟踪编程智能体、搜索与安卓漏斗、企业端绑定的商业化路径，而非榜单分差本身。',
            "background": '228 分钟对话中，张小珺对话姚顺宇——他先在 Anthropic 训练模型，2025 年末加入 Google DeepMind Gemini 团队。亲历 2025–2026 年发布潮：推理跃迁、编程智能体、图像工具，行业心态从「能不能做到」转向「该做什么」。他把前沿实验室比作同浪冲浪者：浪是共享的，品味、速度与靠谱度决定胜负。OpenAI 心智仍强，但 OpenAI、Anthropic、Google 三家基准差距收窄，产品定义比再涨五个智能点更重要。即便公开基准收敛，ChatGPT 仍定消费默认选项。顺宇强调前沿能力收敛时靠谱胜过英雄主义；多数用户感知不到五个点的模型智能差距。买方尽职调查应更重 Gemini 留存用户群组与企业端绑定，而非单次基准发布。',
            "important_facts": [
                '顺宇称 2025–2026 年 OpenAI、Anthropic、Google 在公开基准上比一年前更接近；此前 Anthropic 还担心 OpenAI 的推理领先。更难的问题是选对产品赌注——编程智能体、消费爆款、企业工作流——而非原始能力。多数用户感知不到小幅智能差距；速度、价格、好用度决定留存。训练日益是工程与组织问题：数据管线、评测纪律、产品闭环胜过单点论文胜利。创业公司比多产品线巨头更能快速做自上而下工作流赌注。他 2025 年末加入 Gemini，此前在 Anthropic 参与训练。速度、好用、便宜比榜单排名更驱动消费级人工智能采用。前沿实验室现在在评测透明度与产品负责文化上的竞争，不亚于预训练规模竞争。',
                '区域优化路径分化。豆包语音生成在中国日常场景中体验领先——低延迟、本地数据、对话交互——美国用户更看重编程与深度推理。顺宇求职时接触 Anthropic、OpenAI、DeepMind；先因面试节奏选 Anthropic，后在拉量与分发成主战场时转 Gemini。他猜测 Gemini 消费端市占约两成——工作假设而非乐观情景——并强调 Google 须先用消费命中留人，再用旗舰模型承接。Claude Code 验证 Anthropic 在美国编程与智能体商业化路径。产品赌注清晰度比原始智力更关键；将任一实验室视为永久赢家，误读了收敛周期——分发与工作流锁定才决定经济学。',
                'Dario Amodei 公开点名多家公司「蒸馏」Anthropic 模型，说明能力拉平时头部实验室在防御知识产权与数据闭环。顺宇认为英雄主义时代已过去：最稀缺特质是靠谱——做事细、评测透明、对结果负责。蒸馏争议或成持续法律与合作摩擦源。2026 年尽职调查应跟踪编程、企业与消费三线商业经常性收入与留存用户群组——非参数量或榜单排名本身。豆包语音在中国日常场景领先 Gemini 与 Claude。创业公司比大公司更能快速做自上而下工作流赌注。模型差异化压缩后，蒸馏与数据权利的法律摩擦或成经常性科目。',
            ],
            "mental_model": {
                "name": '能力收敛 × 产品赌注 × 靠谱执行',
                "components": '基准差距压缩后，竞争从原始智力转向「为谁、解决什么」。收敛加靠谱筛选：押注上市路径与留存，非榜单分差。2025 年末加入 Gemini 是 Google 拉量战的时间标记；市占约两成框定上行（消费命中连锁）与下行（留存停滞）。豆包证明区域用户体验可拿本地份额而不必全球智能第一；Claude Code 证明工作流锁定可在下一代模型前变现。差距五个点以内时，产品赌注清晰度比原始智力更关键。训练日益是工程、组织与评测纪律问题。',
                "application": '配置：Alphabet（GOOGL）为分发复利型公司加人工智能期权——搜索加安卓是独有杠杆，前提是 Gemini 留存跟上。Anthropic 为编程与智能体纯方向赌注；勿将单一实验室视为永久赢家。跟踪蒸馏争议与企业客户流失。中国语音体验领先者可拿份额而不必赢全球基准。哑铃组合：Alphabet 分发期权、私有实验室工作流赌注、中国场景体验赢家。2026 清单：产品赌注清晰度、评测透明度、商业年度经常性收入路径——非能力奇迹。季度跟踪编程与消费细分商业经常性收入，是产品赌注的可证伪测试。',
            },
            "key_insights": [
                {
                    "view": 'AI 进入「担心事情是否被良好定义」的阶段，而非担心做不到。',
                    "question": '能力拉平后，差异化来自哪里？',
                    "answer": '来自产品赌注与洞察，非五个点的基准分差。Anthropic 押 Claude Code 做编程与智能体工作流；Google 需消费爆款拉量，再用旗舰 Gemini 承接。用户感知「快、好用、便宜」远强于榜单排名。季度跟踪 Gemini 应用留存、企业端绑定与搜索整合——非参数量发布本身。ChatGPT 心智仍强，即便榜单差距缩小。区域优化可拿本地份额而不必全球智能第一。嵌入工作流的产品能在下一轮能力跃迁前变现——Claude Code 是今日最清晰的美国案例。',
                },
                {
                    "view": 'OpenAI 市占高到失误边际影响变小，Google 必须把量打回来。',
                    "question": '顺宇猜测 Gemini 市占约两成，对投资者意味着什么？',
                    "answer": 'ChatGPT 心智仍强，Google 打的是分发转化战，非实验室声望战。顺宇 2025 年末加入 Gemini，正因把消费端量拉回来已成生存问题。搜索加安卓是 GOOGL 独有杠杆——但须产品命中连锁且留存用户群组稳住。将「约两成」作工作假设压力测试上行与停滞，勿当作乐观情景。Alphabet 搜索与安卓漏斗若无连续消费命中承接旗舰留存，则分发优势为空。',
                },
                {
                    "view": '「英雄主义已过去」——行业需要长期靠谱交付，非天才叙事。',
                    "question": '这对团队与资本意味着什么？',
                    "answer": '训练与对齐变成工程与组织战：数据、评测、产品闭环比孤胆研究者叙事重要。顺宇说人工智能「不太需要脑子、需要靠谱」——投机式押注窗口收窄，能持续交付商业结果的团队溢价上升。2026 对前沿实验室是赌注澄清之年，非能力奇迹之年——英雄叙事助招聘但不足以单独支撑巨额训练资本开支。资本应偏好有评测纪律与交付记录的团队，而非规模化英雄式创始人叙事。',
                },
            ],
            "top_investment_implications": [
                {
                    "ticker": 'GOOGL',
                    "direction": 'Long',
                    "confidence": 'Medium',
                    "thesis": 'Alphabet（GOOGL）：Gemini 消费拉量加搜索与安卓分发——顺宇将 2025 年末入职框为 Google 拉量战；市占约两成意味着留存连锁兑现仍有空间',
                },
                {
                    "ticker": 'Private:Anthropic',
                    "direction": 'Watch',
                    "confidence": 'Medium',
                    "thesis": 'Anthropic：Claude Code 领先编程与智能体工作流赌注，但能力收敛后蒸馏压力上升——须证明企业年度经常性收入与锁定可持续，非榜单胜利',
                },
                {
                    "ticker": 'NVDA',
                    "direction": 'Long',
                    "confidence": 'Low',
                    "thesis": '英伟达（NVDA）：多前沿实验室训练资本开支持续——模型超额收益压缩不减算力需求，无论哪条产品赌注胜出芯片层受益',
                },
            ],
            "golden_quotes": ['每个人都是冲浪的人，本质上是一个浪，而不是你那个冲浪的人。', '现在大家都不那么担心 AI 能不能做到，而是担心这件事是不是被良好定义。', '这个行业最重要的特质就是靠谱，就是做事细，然后对自己做的事负责任。'],
            "chronology": {
                "subject": '姚顺宇 · 前沿模型训练',
                "events": [
                    {'date': 'GPT-3 时代', 'event': '顺宇入行，见证规模扩张叙事'},
                    {'date': '2023–2024', 'event': '行业焦点转向推理；Anthropic 担心追赶 OpenAI'},
                    {'date': '2025 中', 'event': 'Claude Code 触发编程商业化拐点'},
                    {'date': '2025 末', 'event': '顺宇离开 Anthropic，加入 Google DeepMind Gemini'},
                    {'date': '2026', 'event': '三家前沿能力感知拉平；产品定义成主战场'},
                ],
            },
        },
    },
    "zj-ep143": {
        "en": {
            "keywords": ['XPEV', 'Humanoid Robotics', 'Physical-World AI'],
            "conclusion": "He Xiaopeng's message is a capital-allocation reset: XPeng shut down a legacy robot stack that consumed a few tens of billions RMB (not hundreds) because it could not generalize, then concentrated bets on humanoid IRON — roughly twenty percent probability but company-changing upside. Broad AI across autonomy and robotics runs fifteen to twenty percent of the firm; physical-world data alone costs close to RMB ten billion per year, a rigid line item text models do not share. The episode demands valuing XPeng as auto core cash flow plus a costly option and a data moat only multi-scenario survivors can fund.",
            "background": "In an 86-minute interview He Xiaopeng walks through XPeng's robotics and autonomy pivot. The prior robot program consumed a few tens of billions RMB cumulatively — he corrects the 'hundreds of billions' narrative — and was shut down around 2025 because robots could not generalize across unfamiliar venues. Capital now concentrates on humanoid IRON, which he rates at roughly twenty percent probability but transformative payoff. Broad AI spend spans smart driving and robotics at fifteen to twenty percent of company resources. Physical-world data collection alone approaches RMB 1B+ per year as a rigid cost — harder than model weights. The L4 vision-only shortcut underperformed; the GX product pivot reflects honest repositioning. He separates auto core cash flow from robotics optionality — investors must model them independently.",
            "important_facts": [
                'The old robot route burned a few tens of billions RMB — not hundreds — before He stopped it around 2025. The stack could not generalize robots in unfamiliar venues; continuing would have been a sunk-cost trap despite organizational pain. Each physical-world training cycle runs tens to hundreds of terabytes; workflow decisions at scale can cost tens of millions RMB per iteration. Humanoid success would redefine XPeng beyond traditional auto original equipment manufacturer narrative.',
                'IRON is framed as roughly a twenty percent win-rate bet: hardware, locomotion, and scenario data must click together. Auto-driving experience helps but humanoid use cases differ materially. Broad AI — smart driving plus robotics — consumes fifteen to twenty percent of company resources, requiring separate budgeting from core auto profit and loss. Each physical-world workflow decision at scale can cost tens of millions RMB per iteration.',
                'Physical-world AI data is a rigid RMB 1B+/year cost — close to ten billion RMB annually — far above pure software AI. Text data is nearly free; physical scenes need real hardware, safety compliance, and long-tail coverage, naturally oligopolizing the field. The L4 shortcut failed internally; GX pivot adjusts product-market fit rather than chasing tech bragging rights. He stopped the legacy robot stack that cost a few tens of billions of RMB.',
            ],
            "mental_model": {
                "name": 'Kill the Old Stack × Low-Probability Option × Physical-Data Moat',
                "components": "When a tech path is disproved, sunk cost must not dictate capital allocation — the old stack's few tens of billions RMB bought lessons, not optionality. Humanoids are classic twenty-percent-win, ten-times-payoff options with separate key performance indicators from auto core. Physical-world AI competition is a data flywheel: capture, label, and iterate in real scenes — harder to copy than architecture. Broad AI at fifteen to twenty percent of the company must be funded only if auto cash flow covers the burn.",
                "application": 'Model XPeng (XPEV) as auto core plus fifteen to twenty percent broad AI burn and roughly twenty percent IRON option value. Physical-data RMB 1B+/year is a hard constraint — sustainable only if vehicle gross margin and volume fund it. Nvidia (NVDA) benefits from training spend regardless of which humanoid OEM wins. Downgrade linear L4 timelines; weight L2+ penetration and average selling price uplift for near-term revenue. Compare scenario density versus Tesla Optimus and Figure — manufacturing helps but scenes matter more. IRON humanoid is roughly a twenty percent probability bet with massive upside.',
            },
            "key_insights": [
                {
                    "view": 'A few tens of billions on the old stack bought lessons — stopping was the rational choice.',
                    "question": 'Why is stopping so hard for large auto OEMs?',
                    "answer": "Org inertia, talent lock-in, and narrative pressure make stops feel like public failure. He argues CEOs must absorb short-term criticism and redeploy capital — IRON's ~20% odds still beat patching a disproved architecture that already consumed a few tens of billions RMB. Only fund broad AI burn if vehicle gross margin and volume cover the rigid data line item. Physical-world AI data rigid costs approach one billion RMB per year or more.",
                },
                {
                    "view": 'Physical-world data cost is an underappreciated moat — RMB 1B+/year rigid.',
                    "question": 'Why is robot AI more capital-intensive than large language models?',
                    "answer": 'Text is abundant; physical scenes require devices, safety compliance, and long-tail coverage. He puts annual rigid spend close to ten billion RMB — a line item investors must model explicitly. Only players with multi-scenario entry points and sustained burn capacity survive.',
                },
                {
                    "view": 'The L4 shortcut mindset is corrected; GX pivot is product honesty.',
                    "question": 'What does this mean for autonomy investing?',
                    "answer": "End-to-end vision is not a skeleton key — regulation, mapping, and redundancy still gate deployment. Investors should discount linear 'L4 by 202X' narratives and focus on L2+ adoption, delivery data, and near-term average selling price contribution from GX and successors.",
                },
            ],
            "top_investment_implications": [
                {
                    "ticker": 'XPEV',
                    "direction": 'Long',
                    "confidence": 'Medium',
                    "thesis": 'XPeng (XPEV): auto core plus 15–20% broad AI burn and ~20% IRON option — track quarterly cash flow and GX deliveries; traditional auto price-to-earnings alone misprices the story',
                },
                {
                    "ticker": 'NVDA',
                    "direction": 'Long',
                    "confidence": 'Medium',
                    "thesis": 'Nvidia (NVDA): physical-world AI and robot training lift edge compute demand — chip layer benefits regardless of which OEM wins the humanoid race',
                },
            ],
            "golden_quotes": ['We spent a few tens of billions on the old robot path — stopping is the real savings.', "I put IRON's win probability at roughly twenty percent — but if it works, we're a different company.", "In physical-world AI, data is what's truly expensive — close to ten billion a year."],
            "chronology": {
                "subject": 'He Xiaopeng · Robotics & Autonomy Pivot',
                "events": [
                    {'date': '2020–23', 'event': 'Prior robot stack and L4 — few tens of billions RMB cumulative'},
                    {'date': '~2025', 'event': 'Old stack stopped — failed to generalize across venues'},
                    {'date': '2025–26', 'event': 'All-in IRON; broad AI 15–20% of company resources'},
                    {'date': '2025–26', 'event': 'Physical-world data budget rigid at RMB 1B+/year'},
                    {'date': '2026', 'event': 'GX pivot; L4 vision-only shortcut disproved internally'},
                ],
            },
        },
        "zh": {
            "keywords": ['XPEV', '人形机器人', '物理世界 AI'],
            "conclusion": '何小鹏传达的是资本配置重置：旧机器人栈累计「小几十个亿」（非数百亿）因无法泛化而停掉，资本集中到自评胜率约两成、但成功将重写公司边界的人形 IRON。泛人工智能含智驾与机器人，占公司 15%–20%；物理世界数据采集年刚性成本接近 10 亿以上，是大语言模型经济学不具备的硬开支。节目不是把人形机器人当确定趋势——而是要求投资者把小鹏汽车拆成汽车基本盘现金流、昂贵的期权与只有少数玩家能长期承受的物理数据壁垒来估值。',
            "background": '86 分钟对话中，何小鹏复盘小鹏机器人与智驾大转向。上一代机器人累计投入「小几十个亿」——他纠正「数百亿」误传——约 2025 年因机器人无法在陌生场馆泛化而关停。资本集中押注人形 IRON，自评胜率约两成但回报极高。泛人工智能覆盖智驾与机器人，占公司资源 15%–20%。物理世界数据采集单独一项年刚性成本接近 10 亿以上——比模型权重更硬的壁垒。L4 纯视觉捷径内部未达预期；GX 车型转向是产品与市场匹配的诚实调整。他将汽车基本盘现金流与机器人期权分开——投资者须独立建模。',
            "important_facts": [
                '旧机器人路线累计「小几十个亿」（非数百亿），约 2025 年因无法泛化停掉——继续投入是沉没成本陷阱，尽管组织止损痛苦。单次物理世界训练数据量达数十到数百 TB；规模化下每项数据工作流决策可耗数千万人民币。人形成功将重新定义小鹏，超越传统车企整车厂叙事。',
                '人形 IRON 被框定为约两成胜率的赌注：硬件、运动控制、场景数据须同时成立。智驾经验可迁移但人形场景差异大。泛人工智能含智驾与机器人，占公司 15%–20%，须与汽车基本盘损益分开预算与考核。规模化下每项物理世界工作流决策可耗数千万人民币。',
                '物理世界人工智能数据是年刚性成本 10 亿以上——远高于纯软件人工智能。文本数据近乎免费；物理场景需真实设备、安全合规、长尾覆盖，赛道天然寡头化。L4 捷径内部证伪；GX 转向调整产品匹配，非追逐技术炫技。',
            ],
            "mental_model": {
                "name": '止损旧栈 × 低胜率期权 × 物理世界数据壁垒',
                "components": '技术路线被证伪时，沉没成本不应绑架资本配置——旧栈「小几十个亿」买的是教训，非期权。人形是典型的两成胜率、十倍回报期权，关键绩效指标须与汽车核心分开。物理世界人工智能竞争本质是数据飞轮：真实场景采集、标注、迭代——比架构更难复制。泛人工智能占公司 15%–20%，仅当汽车现金流覆盖现金消耗才可持续。',
                "application": '小鹏汽车（XPEV）建模：汽车核心加 15%–20% 泛人工智能现金消耗与约两成 IRON 期权。物理数据年 10 亿以上是硬约束——须靠整车毛利率与销量支撑。英伟达（NVDA）受益于训练支出，与人形赢家无关。下调 L4 线性落地预期；重视 L2+ 渗透率与 GX 交付对近端收入的贡献。对比 Tesla Optimus 与 Figure 的场景密度——制造优势不等于场景优势。',
            },
            "key_insights": [
                {
                    "view": '旧栈「小几十个亿」是买教训——停掉才是理性选择。',
                    "question": '为何大型车企难以及时止损？',
                    "answer": '组织惯性、人才绑定与叙事压力使止损像公开失败。何小鹏强调 CEO 须承担短期舆论代价并重配资本——IRON 约两成胜率仍优于继续修补已证伪、已耗「小几十个亿」的旧架构。仅当整车毛利率与销量覆盖刚性数据成本时，才可持续 15%–20% 泛人工智能现金消耗。',
                },
                {
                    "view": '物理世界数据成本是被低估的壁垒——年刚性 10 亿以上。',
                    "question": '为何机器人人工智能比大语言模型更烧钱？',
                    "answer": '文本数据充裕；物理场景需设备、合规、长尾覆盖。他将年度刚性投入定在接近 10 亿以上——投资者须单列建模。只有多场景入口且能持续现金消耗的玩家能留在牌桌。',
                },
                {
                    "view": 'L4 捷径思维已修正；GX 转向是产品诚实。',
                    "question": '对智驾投资意味着什么？',
                    "answer": '端到端视觉非万能钥匙——监管、地图、安全冗余仍约束落地节奏。投资者应降低「20XX 年 L4 大规模商用」线性预期，更关注 L2+ 采用率、GX 交付数据与近端平均售价贡献。',
                },
            ],
            "top_investment_implications": [
                {
                    "ticker": 'XPEV',
                    "direction": 'Long',
                    "confidence": 'Medium',
                    "thesis": '小鹏汽车（XPEV）：汽车基本盘与 15%–20% 泛人工智能现金消耗、约两成 IRON 期权并存——跟踪季度现金流与 GX 交付；传统汽车市盈率单独使用会误定价',
                },
                {
                    "ticker": 'NVDA',
                    "direction": 'Long',
                    "confidence": 'Medium',
                    "thesis": '英伟达（NVDA）：物理世界人工智能与机器人训练推高边缘算力需求——无论哪家整车厂赢人形机器人竞赛，芯片层受益',
                },
            ],
            "golden_quotes": ['旧机器人那条路花了小几十个亿，必须停——不停才是最大的浪费。', 'IRON 这个项目，我自己评估胜率大概两成，但成了就是另一家公司。', '物理世界的 AI，数据才是真的贵，一年接近十个亿以上。'],
            "chronology": {
                "subject": '何小鹏 · 机器人与智驾转向',
                "events": [
                    {'date': '2020–2023', 'event': '投入上一代机器人与 L4，累计「小几十个亿」'},
                    {'date': '约 2025', 'event': '旧栈因无法泛化停掉'},
                    {'date': '2025–2026', 'event': '全力押注 IRON；泛人工智能占公司 15%–20%'},
                    {'date': '2025–2026', 'event': '物理世界数据年刚性成本 10 亿以上'},
                    {'date': '2026', 'event': 'GX 转向；L4 纯视觉捷径内部证伪'},
                ],
            },
        },
    },
    "zj-ep144": {
        "en": {
            "keywords": ['300866.SZ', 'Shallow-Sea Strategy', 'AI Organization'],
            "conclusion": "Yang Meng defends disciplined category selection at scale: Anker Innovations stays in shallow-sea markets — large enough to build a number-one brand, small enough that Apple-scale rivals do not deploy full war chests — and compounds through roughly 1.1–1.5 points of annual gross margin lift rather than revenue spikes. At RMB 60B+ market cap the test is whether adjacent categories repeat return-on-capital discipline. Heavy Amazon reliance remains the main overhang: rising marketplace ads, policy shifts, and private-label competition can erode third-party margins even when Anker wins category leadership — underwrite margin path and channel mix together.",
            "background": 'In a 218-minute conversation Yang retraces Anker from 2011 founding — Google Founders Award — to RMB 60B+ market capitalization. Shallow-sea strategy targets categories under about $500B total addressable market: power banks near $5B, earphones $200–300B — big enough to breed a leader, small enough that not every giant enters. Deep sea like phones near $500B and PCs near $200B is deliberately avoided. Gross margin historically lifts 1.1–1.5 points annually via brand, supply chain, and stock keeping unit mix. By 2025–26 artificial intelligence penetrates product definition and internal knowledge work; context windows toward a billion tokens could ingest filings, supply chain reviews, patents, and user feedback to understand a firm at marginal cost near zero. Yang stresses that at RMB 60B+ cap shallow-sea discipline must repeat — investors score adjacents on time-to-leader, not hype. Power bank TAM is about five billion dollars; earphones two hundred to three hundred billion. Margin expansion proves pricing power better than volatile revenue growth. Track new category ROIC and time-to-category-leader for adjacent expansion. Deep sea phones are five hundred billion dollars; PCs two hundred billion. Anker avoids deep sea red oceans with full giant resource deployment. Institutional holders should monitor adjacent category return on invested capital and Amazon revenue concentration each quarter.',
            "important_facts": [
                'Market cap exceeds RMB 60B; Yang founded Anker in 2011 and won a Google Founders Award early on. Category choice beats raw scale: shallow-sea targets sit below roughly $500B total addressable market — power banks about $5B, earphones $200–300B — large enough for category leadership, small enough that Apple and Samsung do not deploy full resources. At RMB 60B+ scale shallow-sea discipline must repeat in each adjacent category — score new launches on time-to-category-leader and gross-margin contribution. Deep-sea avoidance is strategic capital allocation preventing wars with Apple and PC OEMs. Gross margin rises roughly one point one to one point five per year historically. AI lowers cost of understanding a company but raises judgment premium. Shallow sea strategy must repeat discipline at RMB sixty billion plus scale.',
                'Deep sea means phones near $500B and PCs near $200B red oceans Anker avoids by design — strategic capital allocation preventing head-on wars while earphones and power banks offer leader economics. Shallow sea equals open competition, clear pain points, product and design winning number one. Gross margin lifts roughly 1.1–1.5 points per year — the falsifiable test of shallow-sea execution at scale, proving pricing power better than volatile revenue growth. Billion-token research lowers internal diligence cost if it shows up in SKU velocity and SG&A ratio. Amazon channel concentration remains a structural margin risk factor. SG&A efficiency and SKU velocity should reflect AI org experiments.',
                'Yang describes AI organization change: internal knowledge, user feedback, and competitive intelligence unified in large language model workflows. Context toward a billion tokens collapses research marginal cost — alpha shifts to asking better questions and judgment. Anker experiments internally; leading AI adopters in consumer brands should show faster stock keeping unit velocity, lower selling general and administrative ratio, and sustained margin lifts within two to three years, not slide decks alone. Amazon channel concentration remains structural margin risk despite category leadership wins. Billion-token context can ingest filings supply chain reviews and patents. Investors respect sustained margin trajectory over single-quarter revenue spikes. Yang argues that at RMB 60B+ capitalization the next chapter is not proving the model but repeating shallow-sea discipline in every adjacent launch — investors should score new categories on time-to-number-one and gross-margin contribution, not headline revenue spikes. Artificial intelligence organization experiments must show up in faster stock keeping unit cycles and selling general and administrative efficiency within two to three years, or the billion-token research narrative remains slide-deck optionality rather than operating leverage.',
            ],
            "mental_model": {
                "name": 'Shallow-Sea Category × Gross-Margin Compounding × Billion-Token Research',
                "components": 'Pick markets: moderate total addressable market under about $500B, open structure, product can win number one. Shallow sea is repeatable if return on invested capital per category stays high; deep sea is a deliberate no-fly zone. Run organization: billion-token context turns scattered documents into queryable knowledge, shortening insight to action. Read financials: 1.1–1.5 point annual gross margin expansion proves brand moat more than revenue spikes. Google Founders Award lineage underscores product-led DNA, not commodity scaling. Category size ceiling near $500B total addressable market keeps giants partially absent — core to reinvestment runway.',
                "application": 'Anker Innovations (300866.SZ): overweight margin trajectory and category return on invested capital; underweight single-channel revenue spikes. Heavy Amazon reliance caps upside if marketplace ad load and private-label competition erode gross margin despite category wins. Artificial intelligence organization gains must evidence in operating metrics within two to three years, not slide decks alone. At RMB 60B+ cap execution is proven — next chapter is adjacent category hit rate and whether faster internal decisions translate into sustained roughly 1.1–1.5 point annual gross-margin expansion and lower selling general and administrative ratios.',
            },
            "key_insights": [
                {
                    "view": 'Great businesses hide in markets that are not mega-sized — about $500B total addressable market is a mental ceiling.',
                    "question": 'Why not attack phones and personal computers directly?',
                    "answer": 'Phones near $500B and PCs near $200B deep sea attract full giant resources — Apple-scale capital deployment. Power banks near $5B and earphones $200–300B shallow seas allow number one in two to three years then adjacent expansion. Execution favors brand and product design, not pure low price — category size ceiling keeps partial giant absence, core to reinvestment runway. Adjacent expansion should be judged on return on invested capital per category, not revenue spikes alone.',
                },
                {
                    "view": 'Billion-token context may rewrite company-understanding economics.',
                    "question": 'What does that mean for investors?',
                    "answer": 'If models ingest filings, supply chain reviews, patents, and user comments, research marginal cost falls — alpha shifts to judgment and question quality. Yang hints Anker experiments internally; margin trajectory and stock keeping unit cycles should reflect AI-led decision speed within two to three years. Artificial intelligence lowers cost of understanding a company but raises the premium on asking the right question. Ask whether faster internal decisions show up in sustained 1.1–1.5 point margin lifts.',
                },
                {
                    "view": 'Roughly 1.1–1.5 points per year gross margin is the metric to respect.',
                    "question": 'How do you validate shallow-sea strategy?',
                    "answer": 'Revenue wobbles quarter to quarter; sustained gross-margin expansion proves pricing power. Flattening margins or selling general and administrative spikes may signal shallow-sea exhaustion or category sprawl. At RMB 60B+ market cap margin path beats single-quarter revenue — the 1.1–1.5 point annual lift is the falsifiable execution test investors should monitor. Watch selling general and administrative efficiency alongside gross margin trajectory at scale.',
                },
            ],
            "top_investment_implications": [
                {
                    "ticker": '300866.SZ',
                    "direction": 'Long',
                    "confidence": 'Medium',
                    "thesis": 'Anker Innovations (300866.SZ): shallow-sea category leadership compounds through ~1.1–1.5pt annual gross margin at RMB 60B+ cap — track adjacent category ROIC, margin path, and Amazon revenue mix alongside platform fee and ad inflation',
                },
            ],
            "golden_quotes": ['We like markets often under fifty billion dollars — big enough to breed a leader, small enough that not every giant shows up.', 'After AI, understanding a company may take a billion tokens of context — that changes every management decision.', "One point of gross margin a year sounds small; compounded over ten years it's a different company."],
            "chronology": {
                "subject": 'Yang Meng · Anker & Shallow-Sea Strategy',
                "events": [
                    {'date': '2011', 'event': 'Yang founds Anker; Google Founders Award'},
                    {'date': '2016–20', 'event': 'Multi-category expansion; shallow-sea strategy crystallizes'},
                    {'date': '2020', 'event': 'Anker Innovations lists on Shenzhen exchange (300866.SZ)'},
                    {'date': '2021–25', 'event': 'Gross margin +1.1–1.5pt/year; market cap crosses RMB 60B'},
                    {'date': '2025–26', 'event': 'AI org transformation and billion-token research frame emerge'},
                ],
            },
        },
        "zh": {
            "keywords": ['300866.SZ', '浅海战略', '人工智能组织'],
            "conclusion": '阳萌对话的核心是：在 600 亿+ 市值上继续用「浅海」纪律选品——够大能养出品类第一、又不够大引不来巨头全资源——并用每年 1.1–1.5 个百分点的毛利率复利，而非追逐收入尖峰。下一章看相邻品类能否复制投入资本回报率。高度依赖亚马逊渠道仍是主要悬而未决的风险：平台广告、政策与自有品牌竞争可能在品类领先的情况下仍挤压第三方毛利，持安克创新应把毛利率走势与渠道结构一并纳入判断。',
            "background": '218 分钟对话中，阳萌复盘安克从 2011 年创立到市值 600 亿+ 人民币的路径。浅海战略：优先目标市场规模约 500 亿美元以下、可建品类领导的赛道——充电宝约 50 亿美元，耳机约 2000–3000 亿美元；够大能养出第一，不够大引不来全部巨头。深海如手机约 5000 亿、个人电脑约 2000 亿，安克主动回避。历史上毛利率每年约提升 1.1–1.5 个百分点。2025–2026 年人工智能渗透产品定义与内部知识管理；上下文向十亿词元演进，理论上可消化财报、供应链、专利与用户反馈全集，边际成本趋近于零。600 亿+ 市值后浅海纪律须在每个相邻品类复制——投资者按成为品类第一的速度评分，而非炒作叙事。',
            "important_facts": [
                '安克市值已达 600 亿人民币以上；阳萌 2011 年创立，早期获 Google 创始人奖。品类选择比规模更重要：浅海目标常限定目标市场规模约 500 亿美元以下——充电宝约 50 亿美元、耳机约 2000–3000 亿美元——够大能养出第一，不够大引不来 Apple、Samsung 全资源投入。600 亿+ 规模下浅海纪律须在相邻品类复制——按成为品类第一速度与毛利贡献评分新品类。回避深海是战略资本配置，避免与 Apple、个人电脑整车厂正面战争。',
                '「深海」指手机（约 5000 亿美元）、个人电脑（约 2000 亿美元）等红海，安克战略性回避正面冲突。浅海等于竞争未固化、用户痛点清晰、凭产品与设计拿品类第一。历史上毛利率每年约提升 1.1–1.5 个百分点——规模化浅海执行的可证伪测试，比波动收入更能证明定价权。十亿词元研究若有效，应体现在库存单位周转速度与销售管理费用率改善。',
                '阳萌描述人工智能组织变革：内部知识、用户反馈、竞品情报可被大语言模型整合；上下文向十亿词元演进，理解一家公司的研究边际成本骤降，超额收益转向问对问题与判断力。安克已在内部试验——领先应用人工智能的消费品牌应在 2–3 年内体现在库存单位速度、销售管理费用率与持续毛利率提升，而非仅演示文稿。',
            ],
            "mental_model": {
                "name": '浅海品类 × 毛利率复利 × 十亿词元研究',
                "components": '选市场：目标市场规模适中（约 500 亿美元以下）、竞争未封死、产品力可拿第一。浅海可重复若各品类投入资本回报率高；深海是刻意禁飞区。做组织：十亿词元上下文把分散文档变成可查询知识，缩短洞察到行动。看财务：毛利率年化提升 1.1–1.5 个百分点比收入增速更能证明品牌护城河。约 500 亿美元目标市场规模天花板使巨头部分缺席——再投资跑道核心。',
                "application": '安克创新（300866.SZ）：超配毛利率走势与品类投入资本回报率；低配单渠道收入尖峰。亚马逊渠道集中若叠加广告成本与自有品牌竞争，可能在浅海品类胜利下仍侵蚀毛利。人工智能组织收益须在 2–3 年内体现在经营指标，而非仅演示文稿。600 亿+ 市值意味着执行已验证，下一章看相邻品类命中率与更快内部决策是否转化为持续 1.1–1.5 个百分点毛利率提升及销售管理费用率改善。',
            },
            "key_insights": [
                {
                    "view": '好生意常在「不够大」的市场——约 500 亿美元目标市场规模是心理上限。',
                    "question": '为何不直接打手机、笔记本等超级大盘？',
                    "answer": '手机约 5000 亿、个人电脑约 2000 亿深海吸引巨头全资源；充电宝约 50 亿、耳机 2000–3000 亿浅海允许 2–3 年成品类第一再相邻扩张。执行偏品牌与产品而非纯低价——品类规模天花板使巨头部分缺席，是再投资跑道核心。相邻扩张应按品类投入资本回报率评判，非单看收入尖峰。',
                },
                {
                    "view": '十亿词元上下文可能改写理解公司的经济学。',
                    "question": '对投资者意味着什么？',
                    "answer": '若模型消化财报、供应链、评论、专利全集，研究边际成本下降，超额收益转向问对问题与判断力。阳萌暗示安克内部已试验；消费品牌若领先人工智能应用，2–3 年内应体现在毛利率与库存单位周期。更快内部决策是否体现为持续 1.1–1.5 个百分点毛利率提升，是可证伪测试。',
                },
                {
                    "view": '毛利率每年提升 1.1–1.5 个百分点是最应重视的指标。',
                    "question": '如何验证浅海战略？',
                    "answer": '收入增速会波动，但持续毛利率扩张说明定价权改善。投资者警惕毛利率走平或销售管理费用飙升——可能是浅海红利耗尽或品类扩张失焦。600 亿+ 市值下毛利率走势比单季收入更重要——1.1–1.5 个百分点年化是可证伪测试。Amazon 渠道集中度仍是结构性毛利风险。',
                },
            ],
            "top_investment_implications": [
                {
                    "ticker": '300866.SZ',
                    "direction": 'Long',
                    "confidence": 'Medium',
                    "thesis": '安克创新（300866.SZ）：浅海品类领导地位通过约 1.1–1.5 个百分点年化毛利率在 600 亿+ 市值上复利——跟踪相邻品类投入资本回报率、毛利率走势与亚马逊收入占比及平台费/广告变化',
                },
            ],
            "golden_quotes": ['我们喜欢的市场，往往不到五百亿美元——够大能养出第一，不够大引不来全部巨头。', '人工智能之后，理解一家公司可能需要十亿词元的上下文，这会改变所有管理决策。', '毛利率每年涨一个多点，看起来不多，复利十年就是完全不同的公司。'],
            "chronology": {
                "subject": '阳萌 · 安克创新与浅海战略',
                "events": [
                    {'date': '2011', 'event': '阳萌创立 Anker；获 Google 创始人奖'},
                    {'date': '2016–2020', 'event': '多品类扩张，浅海战略成型'},
                    {'date': '2020', 'event': '安克创新深交所上市（300866.SZ）'},
                    {'date': '2021–2025', 'event': '毛利率年化提升 1.1–1.5 个百分点；市值突破 600 亿人民币'},
                    {'date': '2025–2026', 'event': '人工智能组织变革与十亿词元研究框架提出'},
                ],
            },
        },
    },
    "tzs-ep180": {
        "en": {
            "keywords": ['9992.HK', 'IP Consumer', 'Valuation'],
            "conclusion": "Recorded March 31, 2026, David and Jeff walk through Pop Mart's narrative break: 2025 revenue RMB 37.1B (+184.7%) but net profit RMB 13B rose only 29.3%, and roughly twenty percent 2026 growth guidance felt like a hard brake — shares fell about thirty percent in two days to near 142–143 HKD, market cap below HKD 200B. The question is whether Labubu is durable IP or a fashion cycle, with Disney near fourteen times price-to-earnings as the comp. Until pipeline breadth proves out, position below traditional compounders and use scenarios, not single-point earnings.",
            "background": "In a 67-minute cross-podcast episode recorded March 31, 2026, David and Jeff unpack Pop Mart's 2025 print versus 2026 guidance gap. Revenue reached RMB 37.1B, up 184.7% year on year; net profit RMB 13B rose 29.3% — profit growth far below revenue, hinting at margin and operating expense pressure. Management guided roughly twenty percent growth for 2026 — a sharp deceleration off an impossible base — and shares fell about thirty percent over roughly two trading days. Stock traded near 142–143 Hong Kong dollars with market cap below HKD 200B. Debate spans intellectual property durability versus fashion cycle; Disney near fourteen times price-to-earnings frames the valuation fork. Labubu and overseas expansion drove much of the 2025 revenue increment — concentration remains the debate. Shares fell about thirty percent over roughly two trading days after the guide. IP durability versus fashion cycle is the core bull bear valuation fork.",
            "important_facts": [
                '2025 revenue RMB 37.1B, +184.7% year on year; net profit RMB 13B, +29.3% year on year. 2026 guidance near twenty percent revenue growth — described as a hard brake — sparked about thirty percent share decline over roughly two trading days. Moving from +184.7% to ~20% is a narrative break, not a small tweak; high price-to-earnings consumer names punish guidance errors severely. Intellectual property durability versus fashion cycle is the core bull-bear valuation fork for 9992.HK.',
                'Shares traded near 142–143 HKD; market cap fell below HKD 200B. Labubu and overseas expansion drove much of the 2025 increment but single-intellectual-property concentration fuels fad versus character-equity debate. Overseas curve two brings localization and channel costs that may dilute near-term gross margin even if top-line growth continues.',
                'Bulls compare Disney and Hello Kitty intellectual property compounding; the episode cites Disney near fourteen times price-to-earnings as valuation anchor. Bears compare trend cycles and inventory risk. Intellectual property durability versus fashion cycle is the core bull-bear fork — evidence mixed on whether Labubu sustains shelf presence three years forward. Pop Mart 2025 revenue was RMB 37.1 billion up 184.7 percent year on year. Stock traded near 142 to 143 Hong Kong dollars with market cap below 200 billion HKD. High price to earnings consumer names punish guidance misses severely.',
            ],
            "mental_model": {
                "name": 'IP Compounding × Fashion Cycle × Guidance Sensitivity',
                "components": 'Cross-generational characters earn Disney-style multiples; trend stock keeping units earn fast-fashion multiples. First guidance deceleration after hyper-growth is the danger zone — RMB 37.1B revenue at +184.7% set an impossible bar; net profit +29.3% shows margin pressure. High price-to-earnings consumer franchises have zero tolerance for guidance misses.',
                "application": 'Pop Mart (9992.HK): track intellectual property pipeline width, repurchase, and membership — not Labubu alone. At 142–143 HKD and market cap below HKD 200B, multiples normalize from narrative peak. Disney (DIS) near fourteen times price-to-earnings is the episode anchor; bull-bear fork on IP durability sets premium room. Roughly twenty percent 2026 guide still strong if delivered; size below traditional compounders and use scenario tables not single-point earnings. Position sizing should stay below traditional compounders until pipeline breadth proves character equity. Net profit was RMB 13 billion up 29.3 percent far below revenue growth. Disney price to earnings near fourteen times was used as a valuation anchor.',
            },
            "key_insights": [
                {
                    "view": 'RMB 37.1B revenue proves operations; RMB 13B net profit does not prove perpetual hyper-growth.',
                    "question": 'Why such a violent reaction to roughly twenty percent guidance?',
                    "answer": '+184.7% in 2025 set an impossible bar; about thirty percent two-day drop shows narrative fracture. Capital at peak paid peak multiples — guide deceleration shifts the story investors underwrote. Use bull, base, and bear scenarios; expect amplified volatility in transition years after hyper-growth. Separate Labubu phenomenon from intellectual property pipeline when building bull scenarios. 2026 guidance near twenty percent growth was described as a hard brake.',
                },
                {
                    "view": 'Intellectual property versus fashion is the valuation fork; Disney ~14x price-to-earnings is the reference.',
                    "question": 'How to classify Labubu?',
                    "answer": 'Multi-generation products, licensing, organic overseas spread signal intellectual property; one-quarter hype and secondary-market collapse signal fashion. Evidence remains mixed — episode contrasts Pop Mart premium to Disney near fourteen times price-to-earnings, debating whether character equity supports a higher multiple than the anchor. Labubu and overseas expansion drove much of the 2025 revenue increment.',
                },
                {
                    "view": 'Below HKD 200B market cap at 142–143 HKD, high price-to-earnings has zero tolerance for misses.',
                    "question": 'Practical framework?',
                    "answer": 'Position size below traditional compounders; scenario tables beat single-point earnings estimates. Quarter misses can trigger twenty to thirty percent drawdowns — 9992.HK already demonstrated. Track comparable store sales, overseas mix, intellectual property renewals; separate Labubu phenomenon from pipeline breadth.',
                },
            ],
            "top_investment_implications": [
                {
                    "ticker": '9992.HK',
                    "direction": 'Long',
                    "confidence": 'Medium',
                    "thesis": 'Pop Mart (9992.HK): post-guide shock at ~142–143 HKD, market cap below HKD 200B after ~30% two-day drop — ~20% 2026 growth still respectable if IP pipeline breadth sustains premium vs Disney ~14x',
                },
                {
                    "ticker": 'DIS',
                    "direction": 'Long',
                    "confidence": 'Low',
                    "thesis": 'Disney (DIS): episode comps Pop Mart to character-IP compounders at ~14x price-to-earnings — park plus media flywheel sets ceiling on pure toy and IP earnings power',
                },
            ],
            "golden_quotes": ['RMB 37.1B revenue is fact, RMB 13B profit — the market buys the future. From 184% to 20%, the narrative broke.', "A thirty percent drop in two days — high price-to-earnings consumer stocks fear 'less amazing.'", 'IP versus fashion: check whether Labubu is still on shelves three years from now.'],
            "chronology": {
                "subject": 'Pop Mart · 2025 Results & Valuation Reset',
                "events": [
                    {'date': '2020', 'event': 'Pop Mart lists in Hong Kong (9992.HK)'},
                    {'date': '2023–24', 'event': 'Labubu and IP global push accelerate revenue'},
                    {'date': '2025', 'event': 'Revenue RMB 37.1B (+184.7%); net profit RMB 13B (+29.3%)'},
                    {'date': '2026-03-31', 'event': 'David and Jeff record episode on results and valuation'},
                    {'date': '2026 Q1', 'event': '~20% 2026 guide; ~30% two-day drop; stock ~142–143 HKD'},
                ],
            },
        },
        "zh": {
            "keywords": ['9992.HK', '知识产权消费', '估值'],
            "conclusion": '2026 年 3 月 31 日录制的节目中，大卫与 Jeff 复盘泡泡玛特的叙事断裂：2025 年营收 371 亿人民币（+184.7%），净利润 130 亿仅增 29.3%，管理层 2026 年约 20% 增长指引在高基数下像「急刹车」，两日股价跌约 30% 至 142–143 港元，市值低于 2000 亿港币。投资分歧不在运营能力，而在 Labubu 是可持续的角色资产还是时尚周期——节目以迪士尼约 14 倍市盈率作参照。在产品管线证明广度之前，仓位宜低于传统复利型公司，用情景分析表而非单点盈利预测。',
            "background": '67 分钟跨播客节目，2026 年 3 月 31 日录制，讨论泡泡玛特 2025 业绩与 2026 指引落差。营收 371 亿人民币同比 +184.7%，净利润 130 亿人民币同比 +29.3%——利润增速远低于收入，暗示毛利率与费用结构压力。管理层 2026 年指引约 20% 增长，相对 2025 高基数急刹车，市场两日股价跌约 30%。股价约 142–143 港元，市值跌破 2000 亿港币。嘉宾辩论知识产权潮玩与时尚周期，并以 Disney 约 14 倍市盈率作估值参照。Labubu 与海外扩张贡献 2025 年大部分增量——集中度仍是辩论焦点。',
            "important_facts": [
                '2025 年营收 371 亿人民币，同比 +184.7%；净利润 130 亿人民币，同比 +29.3%。2026 年管理层指引约 20% 收入增长——相对 2025 高基数「急刹车」，公告后约两个交易日股价跌约 30%。从 +184% 到约 20%，叙事切换大于基本面微调；高市盈率消费股对业绩指引不及预期惩罚极重。知识产权耐久性与时尚周期是泡泡玛特（9992.HK）估值分歧核心。',
                '股价约 142–143 港元，市值低于 2000 亿港币。Labubu 等超级知识产权贡献大量增量，但单一知识产权集中度引发风潮与角色资产之争。海外扩张是第二曲线，本地化与渠道成本可能稀释短期毛利率。',
                '多头看 Disney/Hello Kitty 式知识产权复利；节目引用 Disney 约 14 倍市盈率作参照，空头看潮流周期与库存风险。Labubu 三年后是否仍在货架上，证据仍分化——这是多空估值分歧根源。',
            ],
            "mental_model": {
                "name": '知识产权复利 × 时尚周期 × 业绩指引敏感度',
                "components": '角色跨代际则值 Disney 倍数；潮流单品则值快时尚倍数。超高速增长后首次业绩指引降速是消费高市盈率最危险时刻——371 亿营收 +184.7% 设下不可能的高标杆。净利润 +29.3% 低于收入增速提示毛利率与费用结构压力。',
                "application": '泡泡玛特（9992.HK）：看知识产权产品管线宽度、复购与会员——非 Labubu 单独一项。股价 142–143 港元、市值低于 2000 亿港币后，市盈率从叙事峰值回归。Disney 约 14 倍市盈率是节目锚点，多空对知识产权持久性分歧决定溢价空间。2026 约 20% 指引若兑现仍优秀，但仓位宜低于传统复利型公司，用情景分析表而非单点每股收益。在产品管线宽度证明角色资产前，仓位宜低于传统复利型公司。',
            },
            "key_insights": [
                {
                    "view": '371 亿营收证明运营，净利润 +29.3% 不证明永续超高速增长。',
                    "question": '为何股价对约 20% 指引反应剧烈？',
                    "answer": '2025 +184.7% 设定不可能的高标杆；两日跌约 30% 显示叙事断裂。资金在峰值时给峰值市盈率。指引降速等于叙事切换——投资者应预期过渡年波动放大，用乐观/基准/悲观情景表。构建乐观情景时须分离 Labubu 现象与知识产权产品管线。',
                },
                {
                    "view": '知识产权与时尚是估值分叉点；Disney 约 14 倍市盈率是节目参照。',
                    "question": '如何判断 Labubu 属于哪一类？',
                    "answer": '多代产品、跨品类授权、海外自发传播是知识产权信号；单季爆款、二手价崩盘是时尚信号。证据分化是多空分歧根源。节目以 Disney 约 14 倍市盈率对比泡泡玛特当时溢价，争论知识产权是否支撑更高倍数。',
                },
                {
                    "view": '市值跌破 2000 亿港币、股价 142–143 港元后，高市盈率对不及预期零容忍。',
                    "question": '实操框架？',
                    "answer": '仓位配置低于传统复利型公司；用乐观/基准/悲观情景表。任何季度不及预期可触发 20–30% 回撤——9992.HK 已演示。跟踪同店、海外占比、知识产权续约；分离 Labubu 现象与产品管线广度。',
                },
            ],
            "top_investment_implications": [
                {
                    "ticker": '9992.HK',
                    "direction": 'Long',
                    "confidence": 'Medium',
                    "thesis": '泡泡玛特（9992.HK）：业绩指引冲击后股价约 142–143 港元、市值低于 2000 亿港币、两日跌约 30%——2026 约 20% 增速若兑现仍优，但须知识产权产品管线宽度支撑相对 Disney 约 14 倍市盈率溢价',
                },
                {
                    "ticker": 'DIS',
                    "direction": 'Long',
                    "confidence": 'Low',
                    "thesis": '迪士尼（DIS）：节目以约 14 倍市盈率将泡泡玛特与角色知识产权复利型公司对比——乐园加媒体飞轮设定纯潮玩知识产权盈利能力的估值天花板',
                },
            ],
            "golden_quotes": ['371 亿营收是事实，净利润 130 亿——但市场买的是未来，从 184% 到 20%，叙事断了。', '两天跌三成，说明高市盈率消费股最怕「没那么好」。', '知识产权和时尚的区别，三年后再看 Labubu 还在不在货架上。'],
            "chronology": {
                "subject": '泡泡玛特 · 2025 业绩与估值回调',
                "events": [
                    {'date': '2020', 'event': '泡泡玛特港交所上市（9992.HK）'},
                    {'date': '2023–2024', 'event': 'Labubu 等知识产权全球化，营收加速'},
                    {'date': '2025', 'event': '营收 371 亿人民币（+184.7%）；净利润 130 亿（+29.3%）'},
                    {'date': '2026-03-31', 'event': '大卫与 Jeff 录制节目，讨论业绩与估值'},
                    {'date': '2026 年一季度', 'event': '2026 指引约 20%；两日股价跌约 30%；股价约 142–143 港元'},
                ],
            },
        },
    },
    "tzs-ep185": {
        "en": {
            "keywords": ['TSM', 'ASML', '0981.HK', 'Semiconductor Cycle'],
            "conclusion": "Across forty years — Intel's highest technology award in 1990, co-founding SMIC around 2000 — Xie Zhifeng argues Moore's Law is slowing, not dead, and that TSMC's moat is a service and ecosystem model, not node bragging rights alone. Semiconductors still obey roughly five-year cycles even with an AI tailwind; SMIC ranks second pure-play foundry globally but faces utilization and subsidy-return constraints unlike TSMC. For investors the episode reinforces a cycle-aware stance: TSMC and ASML are advanced choke points worth owning with timing discipline; SMIC demands proof on utilization and ROI, not headline node milestones.",
            "background": "In a 78-minute episode SMIC co-founder Xie Zhifeng traces roughly forty years in semiconductors: Intel highest technology achievement award in 1990, co-founded Semiconductor Manufacturing International around 2000. He explains TSMC's pure-play foundry service model beating conflicted integrated device manufacturer fabs, Moore's Law economic walls as extreme ultraviolet lithography costs rise, and artificial intelligence rewiring capital expenditure. Semiconductors historically run about five-year cycles though AI may flatten downturns; SMIC ranks second in pure foundry globally behind TSMC in the episode framing. China localization adds volume but duplicate capacity risks return on investment when cycles turn down. AI chips pull advanced node demand but memory and mature nodes still cycle. SMIC ranks second in pure foundry behind TSMC in the episode framing. ASML EUV remains a near-term lithography choke point with export controls. China localization adds volume but duplicate capacity risks ROI in downturns. Investors should mark to cycle not to AI hype alone in semi names. Cycle-aware investors mark semiconductor names to utilization and free cash flow, not headline node announcements alone.",
            "important_facts": [
                'Xie has roughly forty years in semiconductors: Intel highest technology award 1990, co-founded SMIC (0981.HK) around 2000. He watched China scale from zero to meaningful foundry capacity — the industry is a marathon, not a single technology bet. Localization brings volume but duplicate capacity risks return on investment in downturns. Artificial intelligence chips pull advanced node demand but memory and mature nodes still cycle with macro.',
                "Moore's Law slowing: extreme ultraviolet lithography, materials, and power walls raise cost per node exponentially — only TSMC-scale volume and customer co-development amortizes spend. TSMC moat equals process lead plus design ecosystem plus delivery reliability; Apple and Nvidia binding reflects a service model, not just wafer output. ASML extreme ultraviolet remains a near-term lithography choke point with export controls.",
                'Semiconductor history shows roughly five-year cycles; AI chips pull advanced node demand but memory and mature nodes still cycle with macro. SMIC ranks second global pure-play foundry behind TSMC; advanced nodes remain capped while mature mix drives utilization economics. Investors should mark to cycle, not artificial intelligence hype alone. Xie reminds investors that artificial intelligence lifts advanced-node utilization but memory, automotive, and industrial segments still follow macro cycles — twelve to eighteen months after capital-expenditure booms often bring inventory corrections. Marking semiconductor holdings to cycle phase rather than artificial intelligence headlines alone avoids paying peak multiples into classical oversupply.',
            ],
            "mental_model": {
                "name": 'Moore Boundaries × Foundry Service Model × Five-Year Semi Cycle',
                "components": 'Process progress continues but economics worsen — winners need scale plus customer co-optimization. TSMC wins on making customers succeed; wafers are delivery format, not the product. About five-year historical cycles plus AI structural tailwind; SMIC second pure foundry behind TSMC. Intel award 1990 and SMIC founding 2000 bracket the shift from integrated device manufacturers to foundry services.',
                "application": 'Taiwan Semiconductor (TSM): advanced node plus AI customer mix quality compounder — watch capital expenditure peaks and roughly five-year cycle for entry timing. ASML: extreme ultraviolet monopoly as Moore economics worsen; export controls remain binary risk. SMIC (0981.HK): mature versus advanced mix, utilization, subsidy return on investment — loss-making nodes surface first in downturns. Mark to cycle not hype — Moore slowdown makes each node costlier, amplifying swing amplitude.',
            },
            "key_insights": [
                {
                    "view": 'TSMC wins on customer success, not node numbers alone.',
                    "question": "Why can't integrated device manufacturers copy the model?",
                    "answer": 'Intel and Samsung design and fab — customers fear intellectual property and capacity conflict; TSMC pure play removes it. Co-development with Apple and Nvidia syncs roadmaps — decade-long stickiness Xie witnessed from 1990 Intel research through 2000 SMIC founding. Twelve to eighteen months post-capex boom often brings inventory correction even with AI tailwind.',
                },
                {
                    "view": 'AI demand is structural; semiconductor stocks stay cyclical — about five-year cycles.',
                    "question": 'How not to get swept by AI narrative alone?',
                    "answer": 'AI lifts advanced utilization; memory, automotive, and industrial still follow macro. Twelve to eighteen months post-capital-expenditure boom often brings inventory correction. Mark to cycle, not hype — Moore slowdown makes each node costlier, amplifying swing amplitude.',
                },
                {
                    "view": 'SMIC second pure foundry — window and trap together.',
                    "question": 'How to read SMIC (0981.HK)?',
                    "answer": 'Localization brings volume and policy support but advanced limits yield margin structure unlike TSMC. Duplicate capacity becomes national sunk cost in downturns. Watch utilization and free cash flow, not headline node announcements alone.',
                },
            ],
            "top_investment_implications": [
                {
                    "ticker": 'TSM',
                    "direction": 'Long',
                    "confidence": 'Medium',
                    "thesis": 'Taiwan Semiconductor (TSM): advanced-node choke point plus AI customer mix — Xie frames moat as service and ecosystem; watch ~5-year semi cycle for entry timing',
                },
                {
                    "ticker": 'ASML',
                    "direction": 'Long',
                    "confidence": 'Medium',
                    "thesis": 'ASML: extreme ultraviolet monopoly as Moore economics worsen — lithography spend per node rises; export controls remain key risk',
                },
                {
                    "ticker": '0981.HK',
                    "direction": 'Watch',
                    "confidence": 'Low',
                    "thesis": 'SMIC (0981.HK): second pure foundry with localization tailwind — utilization and subsidy ROI matter more than advanced node headlines',
                },
            ],
            "golden_quotes": ["Moore's Law isn't dead — it's just getting expensive. Only the largest ecosystems can pay.", 'TSMC runs a service business; wafers are just the delivery format.', 'Semiconductors are always cyclical — AI changes the slope, not the law.'],
            "chronology": {
                "subject": 'Xie Zhifeng · Four Decades in Semiconductors',
                "events": [
                    {'date': '1990', 'event': 'Xie wins Intel highest technology award'},
                    {'date': '1980s–90s', 'event': 'Witnesses integrated device manufacturer era and Asia capacity rise'},
                    {'date': '2000', 'event': 'Co-founds SMIC (0981.HK)'},
                    {'date': '2010s', 'event': 'TSMC pure-play dominance; Moore slowdown signals'},
                    {'date': '2023–26', 'event': 'AI capital expenditure boom; SMIC #2 pure foundry globally'},
                ],
            },
        },
        "zh": {
            "keywords": ['TSM', 'ASML', '0981.HK', '半导体周期'],
            "conclusion": '谢志峰以约 40 年产业经历（1990 年 Intel 最高技术奖、2000 年联合创立中芯国际）说明：摩尔定律放缓但未死，台积电的护城河是服务与生态，而非单纯制程数字。半导体仍遵循约 5 年周期，人工智能只是改变斜率；中芯纯代工全球第二，但产能利用率与政策补贴回报约束不同于台积电。对投资者：台积电与 ASML 是先进制程关键瓶颈，宜周期择时持有；中芯须看利用率与投入资本回报率，而非节点宣传本身。',
            "background": '78 分钟节目中，中芯国际联合创始人谢志峰回顾约 40 年半导体生涯：1990 年获 Intel 最高技术奖，2000 年联合创立中芯国际。他解释台积电纯代工服务模型如何击败垂直整合制造商自建产线，摩尔定律在先进节点面临的经济与物理边界，以及人工智能算力如何改写资本开支。半导体历史上典型约 5 年周期；中芯在纯代工领域全球排名第二，仅次于台积电。中国本土化带来出货量，但周期下行时重复产能带来投入资本回报率风险。摩尔定律延续但每节点成本随极紫外光刻等壁垒指数上升。人工智能芯片拉动先进制程，但存储与成熟节点仍周期波动。',
            "important_facts": [
                '谢志峰从业约 40 年：1990 年获 Intel 最高技术奖，2000 年联合创立中芯国际（0981.HK）。亲历中国半导体从零到晶圆代工规模化，强调产业是马拉松而非单一技术赌注。本土化带来出货量但重复产能在下行期带来投入资本回报率风险。人工智能芯片拉动先进制程，但存储与成熟节点仍随宏观周期波动。',
                '摩尔定律放缓：极紫外光刻、材料、功耗墙使每制程节点成本指数上升；只有台积电级出货量与客户联合研发能摊薄。台积电护城河等于工艺领先加设计生态加交付可靠性——Apple/Nvidia 级客户绑定是服务模型。ASML 极紫外光刻仍是近端光刻瓶颈，受出口管制影响。',
                '半导体历史上约 5 年周期；人工智能芯片拉高先进制程需求，但存储与成熟制程仍波动。中芯纯代工全球排名第二，仅次于台积电；先进制程节点受限而成熟制程组合驱动产能利用率经济学。投资半导体应按周期定价，非仅人工智能叙事。',
            ],
            "mental_model": {
                "name": '摩尔边界 × 代工服务模型 × 5 年半导体周期',
                "components": '制程进步继续但经济学恶化——赢家需规模加客户联合优化。台积电赢的是「让客户成功」的服务体系，晶圆是交付形式。约 5 年历史周期叠加人工智能结构性顺风；中芯纯代工全球第二，仅次于台积电。1990 年 Intel 奖与 2000 年中芯创立框定垂直整合制造商向代工服务转移。',
                "application": '台积电（TSM）：先进制程加人工智能客户组合仍是优质复利型公司，警惕资本开支峰值与约 5 年周期择时。ASML：极紫外光刻垄断，地缘政治二元风险。中芯国际（0981.HK）：成熟制程与先进制程组合、产能利用率、补贴投入资本回报率——周期下行亏损制程节点先暴露。按周期定价而非炒作——摩尔放缓使每节点更贵，放大波动振幅。',
            },
            "key_insights": [
                {
                    "view": '台积电赢的不是制程数字，而是让客户成功的服务体系。',
                    "question": '为何垂直整合制造商难以复制？',
                    "answer": 'Intel/Samsung 兼顾设计与产线，晶圆代工客户担心知识产权与产能冲突；台积电纯代工消除冲突。联合研发与 Apple/Nvidia 同步工艺与产品路线图——粘性十年关系。谢志峰 1990 年 Intel 奖、2000 年中芯创立见证产业重心转移。资本开支繁荣后 12–18 个月常见库存修正，即便有人工智能顺风。',
                },
                {
                    "view": '人工智能需求结构性，但半导体股票仍周期性（约 5 年周期）。',
                    "question": '如何不被人工智能叙事冲昏？',
                    "answer": '人工智能拉高先进制程产能利用率，但存储、汽车、工业仍随宏观波动。资本开支繁荣后 12–18 个月常见库存修正。按周期定价，非按叙事定价；摩尔放缓使每制程节点更贵，放大周期振幅。',
                },
                {
                    "view": '中芯全球纯代工第二，窗口与陷阱并存。',
                    "question": '中芯国际（0981.HK）怎么读？',
                    "answer": '本土化带来出货量与政策支持，但先进制程节点受限，毛利结构不同于台积电。重复产能在下行期成国家级沉没成本。看产能利用率与自由现金流，非仅制程头条。',
                },
            ],
            "top_investment_implications": [
                {
                    "ticker": 'TSM',
                    "direction": 'Long',
                    "confidence": 'Medium',
                    "thesis": '台积电（TSM）：先进制程关键瓶颈加人工智能客户组合——谢志峰将护城河框为服务与生态；约 5 年半导体周期决定入场时机',
                },
                {
                    "ticker": 'ASML',
                    "direction": 'Long',
                    "confidence": 'Medium',
                    "thesis": 'ASML：摩尔经济学恶化下极紫外光刻垄断——每节点光刻支出上升；出口管制仍是关键风险',
                },
                {
                    "ticker": '0981.HK',
                    "direction": 'Watch',
                    "confidence": 'Low',
                    "thesis": '中芯国际（0981.HK）：纯代工全球第二、本土化顺风——产能利用率与补贴投入资本回报率比先进制程头条更重要',
                },
            ],
            "golden_quotes": ['摩尔定律没有死，但越来越贵——只有最大规模的客户生态能付得起这张账单。', '台积电做的是服务业，晶圆只是交付形式。', '半导体永远是周期行业，人工智能改变斜率，不改变规律。'],
            "chronology": {
                "subject": '谢志峰 · 四十年半导体产业',
                "events": [
                    {'date': '1990', 'event': '谢志峰获 Intel 最高技术奖'},
                    {'date': '1980s–1990s', 'event': '见证垂直整合制造商时代与亚洲产能崛起'},
                    {'date': '2000', 'event': '联合创立中芯国际（0981.HK）'},
                    {'date': '2010s', 'event': '台积电纯代工主导地位；摩尔放缓信号'},
                    {'date': '2023–2026', 'event': '人工智能推高先进资本开支；中芯纯代工全球第二'},
                ],
            },
        },
    },
    "tzs-ep179": {
        "en": {
            "keywords": ['Value Investing', 'Capital Cycle', 'Compounding'],
            "conclusion": "Yongqing's Practical Investments framework ties Graham-era price-to-book thinking to today's quality compounders: intrinsic value moves with lifecycle, and capital cycles — not macro headlines — tell you when crowded trades will compress forward returns. Mutual funds peak weight at narrative tops and de-risk on drawdowns, which contrarians can use as timing signals if they tolerate relative underperformance. The actionable rule is buy durable return-on-invested-capital above cost of capital at reasonable prices, and trim when capital floods into a sector; thirty times price-to-earnings only works if roughly twenty-five percent ROIC sustains ten years.",
            "background": "In a 64-minute episode Yongqing teaches Practical Investments methodology — Graham and Buffett value through capital-cycle thinking in China A-shares and Hong Kong. Value does not equal low price-to-earnings: separate traps from temporary mispricing. Graham era emphasized price-to-book; today's quality compounders sustain return on invested capital ten-plus years if moats hold. Mutual funds peak weight at narrative tops and de-risk on drawdowns — 2021 consumer herding and 2024 artificial intelligence peaks are case studies. 2025–26 artificial intelligence infrastructure versus intellectual property consumer cycles diverge; the framework guides current positioning without macro forecasting. Scenario tables beat single-point earnings estimates in transition years — Yongqing applies this to cycle peaks. Independent thesis beats consensus comfort when cycles turn. Quality compounders are friends of time with sustained ROIC above cost of capital. Thirty times PE needs roughly twenty five percent ROIC sustained ten years. 2021 consumer herding and 2024 AI peaks are mutual fund contrarian signals. Company lifecycle lens avoids holding compounders past moat erosion. Scenario tables beat single point earnings estimates in transition years. Yongqing applies scenario tables in transition years when mutual-fund positioning and media saturation peak together.",
            "important_facts": [
                'Value triad: return on invested capital, reinvestment runway, management capital allocation. Price below intrinsic value defines value; intrinsic value shifts with lifecycle — not static low price-to-earnings. Graham-era price-to-book frameworks need upgrading for mature compounders trading at premium multiples justified by sustained returns. Thirty times price-to-earnings needs roughly twenty-five percent return on invested capital sustained ten years to be reasonable.',
                "Capital cycle: high profit attracts capital inflow, overcapacity follows, margins collapse, capital exits, recovery begins — positioning beats macro calls. Where capital floods, returns must fall; only a matter of time. 2021 consumer peak and 2022–23 Hong Kong trough are Yongqing's replay cases.",
                'Quality compounders — friends of time — combine high return on invested capital with long reinvestment runways, sustaining ten-plus years in maturity if moats hold. Mutual funds max weight at narrative peaks and de-risk on drawdowns due to risk controls, not fundamentals alone; contrarians need independent theses and must tolerate relative underperformance until cycles turn. Yongqing stresses that contrarian investors must tolerate relative underperformance while mutual funds de-risk on drawdowns — weekly inflows, media saturation, and initial public offering floods often coincide with cycle tops. Independent thesis beats consensus comfort; 2018–2019 consumer troughs and 2022 Hong Kong lows remain his entry case studies.',
            ],
            "mental_model": {
                "name": 'Intrinsic Value × Capital Cycle × Lifecycle',
                "components": 'Buy quality — return on invested capital above weighted average cost of capital, durable moat — at reasonable price; timing via capital-cycle phase. Avoid sectors where inflows destroyed forward returns. Lifecycle lens prevents holding compounders past moat erosion. Mutual fund de-risking on drawdowns is a contrarian indicator, not a fundamental verdict.',
                "application": 'Consumer quality — Pop Mart (9992.HK) requires separating cycle from compounder thesis. Semiconductors: time Taiwan Semiconductor (TSM) and ASML with capital cycle, adding on utilization dips, trimming at capital expenditure peaks when funds overweight. Thirty times price-to-earnings acceptable if twenty-five percent plus return on invested capital sustains ten years; thirty times for fifteen percent return on invested capital is a trap. Mutual-fund overweight sectors — new energy, artificial intelligence — need capital-cycle checklist before adding. Apply capital-cycle checklists before adding to mutual-fund overweight themes such as new energy or artificial intelligence infrastructure — when inflows and media saturation peak together, forward returns compress.',
            },
            "key_insights": [
                {
                    "view": 'Capital cycle beats macro forecasting — profit attracts capital, capital kills profit.',
                    "question": 'Which 2025–26 sectors look overheated?',
                    "answer": 'Artificial intelligence infrastructure capital expenditure and parts of intellectual property consumer narrative may have peaked; when everyone owns the same story, forward returns compress. Separate AI structural tailwind from classical semiconductor oversupply — mark to cycle phase. Company lifecycle lens avoids holding compounders past moat erosion even if multiples look cheap.',
                },
                {
                    "view": 'Quality compounders are friends of time — criteria stable across cycles.',
                    "question": 'Boundary with growth investing?',
                    "answer": 'Growth pays premium for runway; value demands price discipline. Compounders overlap — high return on invested capital plus long reinvestment. Pay thirty times price-to-earnings only if twenty-five percent plus return on invested capital sustains ten years; otherwise value trap.',
                },
                {
                    "view": 'Mutual fund positioning and drawdown de-risking are contrarian indicators.',
                    "question": 'How to use in practice?',
                    "answer": 'When weekly inflows, media saturation, and initial public offering floods coincide, reduce exposure. 2018–19 consumer trough and 2022 Hong Kong lows are entry case studies. Independent thesis beats consensus comfort — fund de-risking often deepens troughs rather than signaling fundamental collapse.',
                },
            ],
            "top_investment_implications": [
                {
                    "ticker": 'BRK.B',
                    "direction": 'Long',
                    "confidence": 'Medium',
                    "thesis": "Berkshire Hathaway (BRK.B): archetypal quality compounder and capital allocator — Yongqing's return-on-invested-capital and capital-cycle discipline align with Buffett framework",
                },
                {
                    "ticker": 'TSM',
                    "direction": 'Long',
                    "confidence": 'Medium',
                    "thesis": 'Taiwan Semiconductor (TSM): semi quality compounder but capital-cycle timing matters — add on utilization dips, trim when capital expenditure to revenue peaks and funds overweight',
                },
            ],
            "golden_quotes": ["Value doesn't mean cheap — it means price below intrinsic value, and intrinsic value changes.", "Where capital floods in, returns must come down — it's only a matter of time.", "Compounders aren't about speed, they're about duration — return on invested capital sustained ten-plus years, friends of time."],
            "chronology": {
                "subject": 'Yongqing · Value Investing & Capital Cycles',
                "events": [
                    {'date': 'Graham era', 'event': 'Price-to-book-weighted value investing origins'},
                    {'date': '2015–20', 'event': 'Yongqing builds Practical Investments; quality value in A/H shares'},
                    {'date': '2021', 'event': 'Consumer capital-cycle peak; mutual-fund herding'},
                    {'date': '2022–23', 'event': 'Hong Kong trough entries; mutual funds de-risk on drawdowns'},
                    {'date': '2025–26', 'event': 'AI infra vs IP consumer cycles diverge; framework applied'},
                ],
            },
        },
        "zh": {
            "keywords": ['价值投资', '资本周期', '复利'],
            "conclusion": '永庆在投资实战派中把格雷厄姆时代的市净率思维延伸到今日优质复利公司：内在价值随生命周期变化，资本周期——而非宏观标题——才告诉你拥挤交易何时压缩远期回报。公募基金在叙事峰值重仓、回撤时减仓，逆向投资者若承受相对落后，可将其当作择时信号。可执行规则：以合理价格买入投入资本回报率持续高于资本成本的优质公司，资本大量涌入的板块应减仓；30 倍市盈率仅当约 25% 投入资本回报率能持续十年才合理。',
            "background": '64 分钟节目中，永庆分享投资实战派方法论：从格雷厄姆/巴菲特传统价值到资本周期框架与中国市场实操。价值投资不等于低市盈率——须区分价值陷阱与暂时错价。格雷厄姆时代更重市净率；今日优质复利公司若护城河稳固，投入资本回报率可持续十年以上。公募基金在回撤时常降低风险敞口，2021 年消费抱团、2024–2025 年人工智能热潮是案例。2025–2026 年人工智能基础设施与潮玩消费资本周期分化，框架用于指导当前仓位而非宏观预测。',
            "important_facts": [
                '价值投资核心三角：投入资本回报率、再投资空间、管理层资本配置。价格低于内在价值才是价值投资，内在价值随生命周期变化——非静态低市盈率。格雷厄姆时代市净率框架在成熟复利公司上须升级——溢价倍数须用持续回报支撑。30 倍市盈率需约 25% 投入资本回报率持续十年才合理。',
                '资本周期：高利润吸引资本流入→产能过剩→毛利率坍塌→资本退出→复苏；胜负在周期仓位。资本涌入之处回报率必然下行，只是时间问题。2021 年消费赛道顶点、2022–2023 年港股低谷是永庆复盘案例。',
                '优质复利公司（时间的朋友）：高投入资本回报率加长再投资跑道，护城河稳固时可在成熟阶段持续十年以上。公募基金在叙事峰值仓位最重，回撤时降低风险敞口；逆向投资者须独立投资论点，容忍相对落后直至周期转折。周度资金流入、媒体饱和度与新股密集发行常重合周期顶点；2018–2019 年消费低谷与 2022 年港股低谷仍是其入场案例。',
            ],
            "mental_model": {
                "name": '内在价值 × 资本周期 × 生命周期',
                "components": '以合理价格买入优质公司（投入资本回报率高于加权平均资本成本、护城河持久），择时靠资本周期相位。回避资金流入已摧毁远期回报的板块。生命周期视角防止持有复利股超过护城河侵蚀点。公募基金回撤减仓是逆向指标，非基本面判决。',
                "application": '消费优质标的——泡泡玛特（9992.HK）须区分周期波动与复利逻辑。半导体按资本周期择时台积电（TSM）/ ASML——产能利用率低谷加仓、资本开支占营收峰值且公募超配时减仓。30 倍市盈率若投入资本回报率 25% 以上可持续十年则合理；30 倍市盈率配 15% 投入资本回报率则是陷阱。公募重仓赛道（新能源、人工智能）加仓前须过资本周期检查清单。',
            },
            "key_insights": [
                {
                    "view": '资本周期比宏观预测更可靠——利润吸引资本，资本最终压低回报。',
                    "question": '2025–2026 年哪些板块可能过热？',
                    "answer": '人工智能基础设施资本开支、部分潮玩消费叙事或已见顶；当所有人持有同一故事，远期回报被压缩。半导体须区分人工智能结构性需求与经典供给过剩——按周期相位定价。生命周期视角避免在护城河侵蚀后仍持有复利股，即便市盈率看似便宜。',
                },
                {
                    "view": '优质复利公司是「时间的朋友」，识别标准应跨周期稳定。',
                    "question": '与成长投资边界何在？',
                    "answer": '成长投资为跑道付溢价；价值投资要求价格纪律。复利型公司是交集——高投入资本回报率加长再投资跑道。仅当投入资本回报率 25% 以上可持续十年，才值得付 30 倍市盈率；否则是价值陷阱。',
                },
                {
                    "view": '公募基金仓位与回撤减仓是逆向指标。',
                    "question": '实操如何使用？',
                    "answer": '周度资金流入、媒体饱和度与新股密集发行重合时降低敞口。2018–2019 年消费低谷、2022 年港股低谷是入场案例。独立投资论点胜过共识舒适区；回撤时公募减仓常加剧低点而非预示基本面崩塌。',
                },
            ],
            "top_investment_implications": [
                {
                    "ticker": 'BRK.B',
                    "direction": 'Long',
                    "confidence": 'Medium',
                    "thesis": '伯克希尔哈撒韦（BRK.B）：典型优质复利型公司与资本配置者——永庆的投入资本回报率与资本周期纪律与巴菲特框架一致',
                },
                {
                    "ticker": 'TSM',
                    "direction": 'Long',
                    "confidence": 'Medium',
                    "thesis": '台积电（TSM）：半导体优质复利型公司，但资本周期择时重要——产能利用率低谷加仓、资本开支占营收峰值且公募超配时减仓',
                },
            ],
            "golden_quotes": ['价值不是便宜的代名词，是价格低于内在价值——而内在价值会变。', '资本涌入的地方，回报率一定下来，只是时间问题。', '复利公司的关键不是快，是久——投入资本回报率能持续十年以上，才是时间的朋友。'],
            "chronology": {
                "subject": '永庆 · 价值投资与资本周期',
                "events": [
                    {'date': '格雷厄姆时代', 'event': '市净率框架主导的价值投资起源'},
                    {'date': '2015–2020', 'event': '永庆建立投资实战派，实践优质价值投资'},
                    {'date': '2021', 'event': '消费赛道资本周期顶点，公募抱团'},
                    {'date': '2022–2023', 'event': '港股低谷布局复利股；公募降低风险敞口'},
                    {'date': '2025–2026', 'event': '人工智能基础设施与潮玩消费周期分化，框架应用于仓位'},
                ],
            },
        },
    },
}

REFINED = {**_REFINED_BASE, **NEW_EPISODES}
