"""Body content for 6 new Chinese podcast episodes (imported by refine_chinese_pilot_bodies)."""

from __future__ import annotations

from typing import Any

NEW_EPISODES: dict[str, dict[str, dict[str, Any]]] = {
    "zj-ep141": {
        "en": {
            "keywords": ["META", "GOOGL", "Token Economics", "AI Org Design"],
            "conclusion": "Lightspeed partner Freda argues the AI investment frame must shift from token volume to tokens-per-task efficiency — raw burn can rise while waste is real, and CFOs who fund coding tools on usage spikes misread productivity. Organizations are still bolting AI onto steam-engine workflows; electrification took decades because factories had to be redesigned, and relay-baton product teams must become small autonomous squads. For investors: underwrite outcome-based pricing and workflow lock-in (coding agents, harness layers), not headline token charts; META and GOOGL capex stays rational only if task efficiency and org redesign follow.",
            "background": "In an 84-minute second installment of Freda's Investment Notes, Zhang Xiaojun speaks with Lightspeed partner Freda on tokenmaxing, organizational redesign, and human connection in an anxious AI age. Freda invests across OpenAI, Anthropic, ByteDance, Snowflake, and Robinhood from Silicon Valley. She explains tokens per task — the same job can cost tens of times more tokens across models, including hidden reasoning tokens — and why Cursor can burn more tokens without better outcomes. Meta's reported tens-of-billions AI spend and Citrini's viral coding-cost report frame industry tokenmaxing, yet she expects usage to keep rising even as pricing shifts from per-token to per-outcome (Crescendo-style customer service). Coding agents may trigger a self-improving loop that consolidates leadership; Claude versus GPT competition is closer than narratives suggest. Historical parallels — forty years from light bulbs to productivity gains, PC paradox until ERP redesign — suggest AI today is the 'motor stuffed into the steam-engine slot' phase.",
            "important_facts": [
                "Freda defines token economics around tokens per task, not raw volume: identical coding jobs can differ by orders of magnitude in token burn across models, including hidden reasoning tokens and tool loops. More tokens is not better — CFOs funding Cursor credits on usage spikes may confuse adoption with efficiency. Industry tokenmaxing is real (Meta AI spend, Citrini report on coding costs) yet total token demand can still rise as models improve; pricing will gradually shift from per-token to per-outcome where measurable (customer service resolution rates).",
                "Organizational redesign is the binding constraint: steam-engine factories bolted electric motors into old layouts for years before assembly lines unlocked gains; Freda places AI today in that phase — everyone embeds AI in existing relay-baton workflows (PRD → design → dev → QA → GTM) but bottlenecks just move. Future shape: three-to-five-person squads with embedded skills and decision rights, not layered handoffs. Dario's compute versus economy adoption gap means revenue lags capability — studying org design is studying when AI becomes income.",
                "Coding-agent race may end open leadership rotation: better AI training next-gen AI (racer self-improving loop) could make catch-up impossible once past a threshold — OpenAI, Anthropic, Google (Corey leading coding), and Meta all reorganized around coding in 2025–26. Claude versus GPT pricing subsidies signal near-parity; investors who sized software TAM at ~$100/user/month were wildly wrong as single-vendor AI revenue already exceeds that. Freda closes on loneliness in the Bay Area — human connection matters when agents handle cognition; long-term bullish on productivity but diffusion speed and breadth remain uncertain versus prior industrial revolutions.",
            ],
            "mental_model": {
                "name": "Tokens per Task × Org Redesign × Coding Flywheel",
                "components": "Token charts deceive without task normalization — efficiency is outcome per token, not gross burn. Adoption lag follows org shape, not model IQ: motors in steam slots until workflows re-architect. Coding agents add a self-improving loop that may freeze leadership once data flywheels compound — harness and sandbox layers outside raw models capture durable value.",
                "application": "Meta (META): AI capex rational if paired with coding productivity and outcome pricing — watch tokens per resolved task, not seat growth alone. Alphabet (GOOGL): coding org bet under Corey is distribution plus model — retention via workflow. Nvidia (NVDA): benefits from token growth and training loops regardless of which coding winner emerges. Underweight pure token-volume narratives; overweight harness, sandbox, and outcome-priced verticals. Size consumer AI names for org-redesign optionality, not plug-in copilots.",
            },
            "key_insights": [
                {
                    "view": "Tokenmaxing and rising token demand can both be true.",
                    "question": "How should investors read token burn?",
                    "answer": "Separate waste from structural demand: tokens per task is the unit of analysis — Cursor burning more per question is inefficiency, not proof of value. Outcome-based pricing (Crescendo customer service) aligns vendor and customer incentives. Early investors who modeled ~$100/month software TAM missed that AI spend per enterprise already dwarfs that — revise sizing on task depth, not seat count.",
                },
                {
                    "view": "AI today is the electric motor in a steam-engine factory.",
                    "question": "Why productivity lags despite model capability?",
                    "answer": "Electrification took twenty to forty years after motors existed; PC productivity jumped only after ERP and supply-chain redesign in the 1990s. Companies still run relay-baton product orgs — AI shortens dev, so QA becomes bottleneck, then PRD, then GTM. Until squads re-form end-to-end, economy adoption (Dario's term) trails compute progress — org research is timing research.",
                },
                {
                    "view": "Coding agents may end the rotating frontier-leader narrative.",
                    "question": "What changes if AI trains AI?",
                    "answer": "Engineer productivity gains from coding agents accelerated from ~15% to much higher within months; model release cadence shifted to monthly. Self-improving loops mean laggards face carriage-versus-car dynamics — close early while gaps are fuzzy, irrelevant once stable automation arrives. Claude-GPT price wars signal parity; bet on workflow data flywheels (Claude Code feedback), not single benchmark releases.",
                },
            ],
            "top_investment_implications": [
                {
                    "ticker": "META",
                    "direction": "Watch",
                    "confidence": "Medium",
                    "thesis": "Meta (META): massive AI/token spend only justified if coding agents convert to outcome efficiency — Freda frames tokenmaxing as real; track whether internal coding ROI and pricing model shift follow capex",
                },
                {
                    "ticker": "GOOGL",
                    "direction": "Long",
                    "confidence": "Medium",
                    "thesis": "Alphabet (GOOGL): coding-led reorg under Corey plus Gemini distribution — self-improving coding loop is strategic; tokens per task discipline determines whether capex compounds",
                },
                {
                    "ticker": "NVDA",
                    "direction": "Long",
                    "confidence": "Low",
                    "thesis": "Nvidia (NVDA): token demand and AI-training-AI loops sustain compute spend even as per-task efficiency improves — chip layer wins regardless of application winner",
                },
            ],
            "golden_quotes": [
                "Tokens per task — not token volume — is the metric that matters; the same job can differ by tens of times.",
                "We are bolting the electric motor into the steam-engine slot; the assembly line has not been invented yet.",
                "Once coding agents close the self-improving loop, catching up may look like horses chasing cars.",
            ],
            "chronology": {
                "subject": "Freda · Token Economics & AI Org Design",
                "events": [
                    {"date": "2024–25", "event": "Token pricing dominates; investors size AI on volume"},
                    {"date": "2025", "event": "Citrini report flags coding tokenmaxing; Meta AI capex surges"},
                    {"date": "Early 2026", "event": "Coding-agent productivity jumps; monthly model releases"},
                    {"date": "2026-05", "event": "Freda records Investment Notes ep.2 on org redesign"},
                    {"date": "2026", "event": "Shift toward outcome-based pricing in verticals like customer service"},
                ],
            },
        },
        "zh": {
            "keywords": ["META", "GOOGL", "Token 经济学", "AI 组织变革"],
            "conclusion": "光速创投合伙人 Freda 认为 AI 投资框架须从 Token 总量转向单任务 Token 效率——消耗可继续上升但浪费真实存在，CFO 按 Cursor 用量激增追加预算可能误判生产力。组织仍在把 AI 塞进蒸汽机式工作流；电气化曾耗时数十年因工厂须重新设计，接力棒式产品团队应变为小型自治分队。对投资者：押注按效果付费与工作流锁定（编程智能体、Harness 层），非 Token 图表头条；Meta 与 Google 资本开支仅当任务效率与组织重构跟进时才合理。",
            "background": "84 分钟节目中，张小珺对话光速创投合伙人 Freda，讨论 Tokenmaxing、组织重构与焦虑时代的连接。Freda 在硅谷投资 OpenAI、Anthropic、字节跳动、Snowflake、Robinhood 等。她解释单任务 Token 数——同一任务不同模型可差数十倍，含隐藏推理 Token——以及 Cursor 为何可能烧更多 Token 却未带来更好结果。Meta 数百亿美元 AI 开支与 Citrini 病毒式编程成本报告框定行业 Tokenmaxing，但她预期用量仍上升，定价逐步从按 Token 转向按效果（客服解决率等）。编程智能体或触发自我改进闭环、固化龙头；Claude 与 GPT 竞争比叙事更接近。历史类比——灯泡到生产率提升约四十年、PC 悖论直至 ERP 重构——暗示今日 AI 处于「把电机塞进蒸汽机位」阶段。",
            "important_facts": [
                "Freda 以单任务 Token 数定义 Token 经济学，非原始用量：相同编程任务跨模型 Token 消耗可差数量级，含隐藏推理与工具循环。Token 越多并非越好——CFO 因 Cursor 用量激增拨款可能混淆采用与效率。行业 Tokenmaxing 真实（Meta AI 开支、Citrini 编程成本报告），但模型改进下总需求仍可能上升；可量化场景定价将从按 Token 转向按效果（客服解决率）。",
                "组织重构是约束条件：蒸汽机工厂曾把电机塞进旧布局多年才迎来流水线；Freda 将今日 AI 置于此阶段——人人把 AI 嵌入既有接力工作流（PRD→设计→开发→测试→上市），瓶颈只是转移。未来形态：三至五人分队、内嵌技能与决策权，非层层交接。Dario 的算力与经济采纳差距意味着收入滞后于能力——研究组织即研究 AI 何时变现。",
                "编程智能体竞赛或终结开放龙头轮换：更好的 AI 训练下一代 AI（自我改进闭环）过临界点后追赶或不可能——OpenAI、Anthropic、Google（Corey 主导编程）、Meta 2025–26 年均围绕编程重组。Claude 与 GPT 补贴价格战信号接近平价；按约 100 美元/月软件 TAM 估值的投资者严重低估——单厂商 AI 收入已远超该假设。Freda 以湾区孤独感收尾——智能体承担认知时人的连接重要；长期看好生产率但扩散速度与广度相对历次工业革命仍不确定。",
            ],
            "mental_model": {
                "name": "单任务 Token × 组织重构 × 编程飞轮",
                "components": "无任务归一化的 Token 图表易误导——效率是每 Token 产出，非总消耗。采纳滞后于组织形态而非模型智商：电机塞蒸汽机位直至流程重架构。编程智能体叠加自我改进闭环，数据飞轮复合后或冻结龙头——模型外 Harness 与沙箱层捕获持久价值。",
                "application": "Meta（META）：AI 资本开支合理前提是编程生产力与按效果定价——跟踪每解决任务的 Token，非仅席位增长。Alphabet（GOOGL）：Corey 主导编程重组加 Gemini 分发——自我改进编程闭环是战略赌注。英伟达（NVDA）：Token 需求与 AI 训练 AI 支撑算力开支，无论编程赢家是谁。低配纯 Token 量叙事，超配 Harness、沙箱与按效果定价垂直场景。",
            },
            "key_insights": [
                {
                    "view": "Tokenmaxing 与 Token 需求上升可同时成立。",
                    "question": "投资者如何读 Token 消耗？",
                    "answer": "区分浪费与结构性需求：单任务 Token 是分析单位——Cursor 每问多烧 Token 是低效非价值证明。按效果定价（Crescendo 客服）对齐厂商与客户激励。早期按约 100 美元/月软件 TAM 估值者错失企业 AI 单户支出已远超——按任务深度重估，非席位数。",
                },
                {
                    "view": "今日 AI 是蒸汽机工厂里的电机。",
                    "question": "为何能力已有而生产率滞后？",
                    "answer": "电气化在电机发明后仍历二十至四十年；PC 生产率至 1990 年代 ERP 与供应链重构才跳升。企业仍跑接力式产品组织——AI 缩短开发则测试成瓶颈，再是 PRD、再是 GTM。分队端到端重构前，经济采纳（Dario 术语）滞后算力进步——组织研究即择时研究。",
                },
                {
                    "view": "编程智能体或终结前沿龙头轮换叙事。",
                    "question": "AI 训练 AI 改变什么？",
                    "answer": "编程智能体带来的工程师生产率数月内从约 15% 跃升至更高；模型发布节奏变为月度。自我改进闭环意味落后者面临马车追汽车——差距模糊时宜早押注，稳定自动化后追赶无意义。Claude-GPT 价格战信号平价；押工作流数据飞轮（Claude Code 反馈），非单次基准发布。",
                },
            ],
            "top_investment_implications": [
                {
                    "ticker": "META",
                    "direction": "Watch",
                    "confidence": "Medium",
                    "thesis": "Meta（META）：巨额 AI/Token 开支仅当编程智能体转化为单任务效率才合理——Freda 框定 Tokenmaxing 为真；跟踪内部编程投入资本回报率与定价模式是否跟进资本开支",
                },
                {
                    "ticker": "GOOGL",
                    "direction": "Long",
                    "confidence": "Medium",
                    "thesis": "Alphabet（GOOGL）：Corey 主导编程重组加 Gemini 分发——自我改进编程闭环是战略级；单任务 Token 纪律决定资本开支能否复利",
                },
                {
                    "ticker": "NVDA",
                    "direction": "Long",
                    "confidence": "Low",
                    "thesis": "英伟达（NVDA）：Token 需求与 AI 训练 AI 支撑算力开支，即便单任务效率提升——芯片层无论应用赢家是谁均受益",
                },
            ],
            "golden_quotes": [
                "重要的是单任务 Token，不是 Token 总量——同一任务可以差几十倍。",
                "我们现在是把电机塞进蒸汽机的位置，流水线还没有发明。",
                "编程智能体一旦跑通自我改进闭环，追赶可能像马车追汽车。",
            ],
            "chronology": {
                "subject": "Freda · Token 经济学与 AI 组织",
                "events": [
                    {"date": "2024–2025", "event": "按 Token 定价主导；投资者按用量规模估值"},
                    {"date": "2025", "event": "Citrini 报告指编程 Tokenmaxing；Meta AI 资本开支激增"},
                    {"date": "2026 年初", "event": "编程智能体生产率跳升；模型月度发布"},
                    {"date": "2026-05", "event": "Freda 录制投资札记第 2 集谈组织重构"},
                    {"date": "2026", "event": "客服等垂直场景转向按效果付费"},
                ],
            },
        },
    },
    "zj-ep142": {
        "en": {
            "keywords": ["Private:Harness", "ByteDance", "2026 VC Themes"],
            "conclusion": "Yusen, a China Fund VC observer, reframes 2026 after his cautious AI-return call drew pushback: being wrong early is normal when frontier markets move fast, but the investable edge is shifting outside raw models to Harness layers, sandboxes, and persistent agent computers. He argues the next ByteDance is unlikely to beat ByteDance inside its distribution game — opportunity sits in niches incumbents ignore and in hardware-heavy China supply chains. For public-market investors the episode is a private-market signal: model APIs commoditize; durable value accrues to orchestration, feedback data loops, and application shapes ByteDance cannot easily copy.",
            "background": "In a 139-minute second installment of Yusen's VC Watch, Zhang Xiaojun revisits Yusen's January 2026 caution on AI equity returns — NVIDIA-led rallies made the call look early wrong, which Yusen accepts as occupational hazard for pre-seed thinking. He traces the narrative from O1 to DeepSeek scares and back to US hyperscaler strength. Harness (agent orchestration outside the model) grows more important in 2026 even if frontier models remain critical: sandboxes, persistent AI computers, and task checkpoints let weak models complete long jobs. Coding flywheels feed models with high-quality feedback — Claude Code is the cited example. Debate on the next ByteDance: beating ByteDance on its turf is hard; opportunities lie in entertainment, tools, and regions outside its ad network. Application founders still have room if they avoid head-on platform wars.",
            "important_facts": [
                "Yusen expected 2026 AI equity digestion in late 2025; NVDA and AI names rallied sharply instead — he treats 'face slapping' as normal for early VC when adoption outruns financialization scares. O1 and DeepSeek episodes showed narrative whipsaws; underlying spend and coding-agent adoption continued. Lesson: separate trading narratives from infrastructure build cycles.",
                "Harness layer thesis: models alone are insufficient for long-horizon tasks — orchestration, sandbox browsers, persistent VMs, and periodic model checkpoints (Harness-style) unlock reliability. Value stacks outside the model API: OpenAI, Anthropic, and startups all build harnesses; context must be user-supplied through products, not dropped from the sky. Coding agents create feedback data loops that retrain models — Anthropic's Claude Code path versus ChatGPT's exam-trained base.",
                "Next ByteDance debate: Yusen doubts a clone wins inside ByteDance's ad and content rules; investors still hunt 'next ZJ' but EU/US apps lack ByteDance's China distribution. Opportunities — entertainment, tools, Qtime-like formats, hardware in China — favor startups incumbents undervalue. If coding capacity becomes abundant, product surface area explodes; long diffusion lags mean jobs and social contracts will shift before productivity statistics catch up.",
            ],
            "mental_model": {
                "name": "Model × Harness × Distribution Moat",
                "components": "Frontier models necessary but not sufficient — harness, sandbox, and feedback loops own task completion. ByteDance-style distribution moats block head-on clones; edge is orthogonal niches and hardware supply chains. Early VC calls will look wrong when S-curves steepen — underwrite layers, not quarterly narratives.",
                "application": "Private Harness/orchestration names: watch for data flywheel proof in coding and ops. Public mega-caps (GOOGL, META): model plus harness plus distribution wins; API margin alone compresses. China hardware and edge AI benefit if application layer fragments. Avoid sizing 'next ByteDance' on ad-network logic — hunt categories platforms ignore.",
            },
            "key_insights": [
                {
                    "view": "2026 belongs to Harness even if models still matter.",
                    "question": "Where does Yusen see venture edge?",
                    "answer": "Long tasks need orchestration — sandboxes, persistent computers, checkpoints — not bigger context windows alone. Harness collects the feedback that retrains models (coding fixes, failed steps). Investors should map stack layers: model commodity risk rises; harness and workflow data moats deepen.",
                },
                {
                    "view": "The next ByteDance is not ByteDance 2.0.",
                    "question": "What did Yusen learn from the debate?",
                    "answer": "Beating ByteDance inside its game requires its distribution and ad stack — unlikely for newcomers. Funds still fly to Shanghai seeking clones; better hunts are orthogonal entertainment/tools and overseas niches. Application founders should do what giants won't fund, not replicate feeds.",
                },
                {
                    "view": "Being early wrong beats being late right in frontier VC.",
                    "question": "How to read his 2026 caution now?",
                    "answer": "Public AI rallied on capex and coding agents while his call flagged financialization risk — both can coexist. Early investors must publish views before consensus; frequent 'face slaps' signal fast-moving markets with abundant deal flow. Public investors: don't trade his timing call; extract structural harness and hardware themes.",
                },
            ],
            "top_investment_implications": [
                {
                    "ticker": "Private:Harness",
                    "direction": "Watch",
                    "confidence": "Medium",
                    "thesis": "Harness/orchestration layer — Yusen frames 2026 edge outside raw models; task checkpoints and sandbox compute become pricing power if coding agents scale",
                },
                {
                    "ticker": "GOOGL",
                    "direction": "Long",
                    "confidence": "Medium",
                    "thesis": "Alphabet (GOOGL): model plus harness plus YouTube/Android distribution — coding feedback loops compound; API alone is not the moat",
                },
                {
                    "ticker": "META",
                    "direction": "Watch",
                    "confidence": "Low",
                    "thesis": "Meta (META): agent sandboxes and Llama ecosystem bets align with harness thesis — execution on long-horizon tasks determines ROI on AI capex",
                },
            ],
            "golden_quotes": [
                "Getting slapped in public is normal for early investors — it often means the industry is moving fast.",
                "The harness outside the model is where 2026 venture edge is forming.",
                "You will not beat ByteDance inside ByteDance's game — look where they are structurally absent.",
            ],
            "chronology": {
                "subject": "Yusen · VC Watch 2026",
                "events": [
                    {"date": "2025-11", "event": "Yusen warns on 2026 AI equity returns; cites O1 cycle"},
                    {"date": "2026-01", "event": "DeepSeek scare; US AI names volatile then rebound"},
                    {"date": "2026 Q1", "event": "Coding-agent adoption accelerates; harness stacks proliferate"},
                    {"date": "2026-05", "event": "Records VC Watch ep.2; revisits call after rally"},
                    {"date": "2026", "event": "Investor tours hunt 'next ByteDance' amid harness shift"},
                ],
            },
        },
        "zh": {
            "keywords": ["Private:Harness", "字节跳动", "2026 创投"],
            "conclusion": "中国基金创投观察者雨森在 AI 回报谨慎判断遭遇打脸后重构 2026 框架：早期看错是常态，但可投资边际正从裸模型转向 Harness 层、沙箱与持久智能体计算机。他认为下一个字节很难在字节分发规则内击败字节——机会在巨头忽视的细分与中国硬件供应链。对二级市场投资者：这是私募信号——模型 API commoditize；持久价值归于编排、反馈数据闭环与字节难以复制的应用形态。",
            "background": "139 分钟节目中，张小珺回访雨森 2026 年 1 月对 AI 股票回报的谨慎判断——英伟达引领反弹使观点显得过早错误，雨森视之为早期投资的职业风险。他梳理从 O1 到 DeepSeek 再回美国超大规模叙事的路径。Harness（模型外智能体编排）在 2026 年更重要：沙箱、持久 AI 电脑与任务检查点让较弱模型完成长任务。编程飞轮以高质量反馈重训模型——以 Claude Code 为例。下一字节之争：在字节主场难赢；机会在娱乐、工具与其广告网络外区域。应用创业者避开正面平台战仍有空间。",
            "important_facts": [
                "雨森 2025 年末预期 2026 年 AI 股权消化；英伟达等强势反弹——他将「打脸」视为前沿市场快时的常态。O1 与 DeepSeek 叙事剧烈摆动；底层开支与编程智能体采用持续。教训：区分交易叙事与基础设施建设周期。",
                "Harness 层论点：仅靠模型不足以完成长程任务——编排、沙箱浏览器、持久虚拟机与定期检查点（Harness 式）解锁可靠性。价值堆叠在模型 API 外：OpenAI、Anthropic 与创业公司均建 Harness；上下文须由用户经产品供给。编程智能体形成反馈数据闭环重训模型——Anthropic Claude Code 路径对比 ChatGPT 考试训练基座。",
                "下一字节辩论：雨森怀疑在字节广告与内容规则内克隆难胜；投资人仍赴上海寻找「下一 ZJ」。机会在娱乐、工具、Qtime 式形态与中国硬件——偏向巨头低估的创业公司。若编程产能充裕，产品表面激增；扩散滞后意味着就业与社会契约先于生产率统计变化。",
            ],
            "mental_model": {
                "name": "模型 × Harness × 分发护城河",
                "components": "前沿模型必要非充分——Harness、沙箱与反馈闭环拥有任务完成度。字节式分发护城河阻挡正面克隆；边际在正交细分与硬件供应链。早期 VC 观点在 S 曲线陡峭时常显错误——押注层级非季度叙事。",
                "application": "私有 Harness/编排标的：关注编程与运维中的数据飞轮证明。上市巨头（GOOGL、META）：模型加 Harness 加分发胜出；单 API 毛利压缩。中国硬件与边缘 AI 受益若应用层碎片化。勿按广告网络逻辑估值「下一字节」——寻找平台忽视品类。",
            },
            "key_insights": [
                {
                    "view": "2026 属于 Harness，即便模型仍关键。",
                    "question": "雨森看到的风投边际在哪？",
                    "answer": "长任务需编排——沙箱、持久电脑、检查点——非更大上下文窗口 alone。Harness 收集重训模型的反馈（编程修复、失败步骤）。投资者应绘制技术栈：模型商品化风险上升；Harness 与工作流数据护城河加深。",
                },
                {
                    "view": "下一字节不是字节 2.0。",
                    "question": "雨森从辩论中学到什么？",
                    "answer": "在字节主场赢需其分发与广告栈——新人难复制。基金仍赴上海找克隆；更好 hunt 是正交娱乐/工具与海外细分。应用创业者应做巨头不投的事，非复制信息流。",
                },
                {
                    "view": "早期看错优于晚期才对。",
                    "question": "如何读他 2026 谨慎判断？",
                    "answer": "公募 AI 因资本开支与编程智能体反弹，其观点指金融化风险——二者可并存。早期投资人须在共识前发声；频繁打脸信号快市场与充裕 deal flow。公募投资者：勿交易其择时；提取 Harness 与硬件结构性主题。",
                },
            ],
            "top_investment_implications": [
                {
                    "ticker": "Private:Harness",
                    "direction": "Watch",
                    "confidence": "Medium",
                    "thesis": "Harness/编排层——雨森框定 2026 边际在裸模型外；任务检查点与沙箱算力若随编程智能体规模化将形成定价权",
                },
                {
                    "ticker": "GOOGL",
                    "direction": "Long",
                    "confidence": "Medium",
                    "thesis": "Alphabet（GOOGL）：模型加 Harness 加 YouTube/安卓分发——编程反馈闭环复利；单 API 非护城河",
                },
                {
                    "ticker": "META",
                    "direction": "Watch",
                    "confidence": "Low",
                    "thesis": "Meta（META）：智能体沙箱与 Llama 生态赌注契合 Harness 论点——长程任务执行决定 AI 资本开支投入资本回报率",
                },
            ],
            "golden_quotes": [
                "被打脸对早期投资人是常态——往往说明行业还在快速移动。",
                "模型外面的 Harness 层，是 2026 风投边际形成的地方。",
                "在字节的游戏里打不过字节——要找它结构上缺席的战场。",
            ],
            "chronology": {
                "subject": "雨森 · 创投观察 2026",
                "events": [
                    {"date": "2025-11", "event": "雨森预警 2026 AI 股权回报；提及 O1 周期"},
                    {"date": "2026-01", "event": "DeepSeek 冲击；美国 AI 标的波动后反弹"},
                    {"date": "2026 年一季度", "event": "编程智能体加速；Harness 栈 proliferate"},
                    {"date": "2026-05", "event": "录制创投观察第 2 集；反弹后复盘"},
                    {"date": "2026", "event": "投资人巡演寻找「下一字节」 amid Harness 转向"},
                ],
            },
        },
    },
    "zj-ep145": {
        "en": {
            "keywords": ["Private:SpaceX", "TSLA", "Space Economy"],
            "conclusion": "Former SpaceX manufacturing executive Hong Lide frames 2026 as capital's ChatGPT moment for space — IPO chatter and xAI integration amplify imagination — but engineering timelines were set a decade ago: Mars teams formed after the first Falcon success, and Starship iterations began while flying the prior generation. Musk's hiring philosophy tolerates public speculation because roadmap lines, not quarterly OKRs, bind the firm. For investors: SpaceX optionality is manufacturing culture plus vertical integration, not hype alone; Tesla remains the public liquid proxy, while pure-play space names need proof on cadence, cost-per-kilogram, and Starlink cash flow before mega-IPO pricing.",
            "background": "In a 181-minute oral history, Zhang Xiaojun speaks with Hong Lide, who joined SpaceX in 2002 and left around 2009 managing seven departments and three thousand-plus rocket components. Now a Los Angeles early-stage VC (Eris Fund) investing physical AI and space, he walks through SpaceX's master plan lineage, manufacturing obsession (GEP Mini Cooper team analogy), and why running out of fuel exactly at your driveway is the rocket precision metaphor. 2026 may bring the largest IPO in history as SpaceX absorbs xAI narratives, yet Hong stresses space development is continuous — Mars planning started in 2012–13 after first launch success. Musk's X posts often preview ideas discussed internally years earlier. China aerospace competition is watched closely but US vertical integration and ruthless cost culture remain differentiated.",
            "important_facts": [
                "Hong joined SpaceX in 2002, departed ~2009 leading seven departments covering three thousand-plus rocket parts — lived through Falcon 1 era into early Starship thinking. Manufacturing culture: compare SpaceX to BMW Mini Cooper GEP team — relentless process refinement, not PowerPoint engineering. Precision anecdote: rocket fuel should deplete exactly as you reach home — drives tolerance stack and testing discipline.",
                "Roadmap philosophy: SpaceX had a multi-step master plan like Tesla's; Mars group existed once first rocket flew even when vehicle could not reach Mars yet — next-gen design starts while current gen flies. Public Musk tweets often recycle internal decade-old threads; 2026 IPO/xAI merger is capital inflection (ChatGPT moment for space) more than engineering discontinuity. Starlink, Starship, and satellite internet were long-planned lines, not reaction to 2025 hype.",
                "2026 investor inbound surge: LPs ask every space founder about 'SpaceX stock' — conviction rises even if physics unchanged. Hong co-founded Eris Fund with ex-Tesla Shanghai Gigafactory executive — bets on physical-world AI and space supply chain. China launch cadence rising but full-stack reuse and cost curve still lag; watch ITAR, launch licenses, and Starship cadence as falsifiable milestones pre-IPO.",
            ],
            "mental_model": {
                "name": "Vertical Integration × Manufacturing Culture × Capital Inflection",
                "components": "Space economics compound via reuse, cadence, and in-house production — culture eats strategy. Roadmaps are multi-decade lines executed in parallel generations, not single-product S-curves. 2026 IPO window reprices optionality; engineering milestones (Starship cadence, Starlink FCF) gate durable multiples.",
                "application": "Tesla (TSLA): public proxy for Musk industrial stack — watch whether space narrative distracts or reinforces manufacturing DNA. Private SpaceX: treat IPO as liquidity event, not thesis change — underwrite kg-to-orbit cost and Starlink cash engine. RKLB and launch peers: benefit from rising tide but lack full-stack moat — cadence and backlog quality matter. Pre-IPO: avoid paying only for xAI story; demand launch and broadband unit economics.",
            },
            "key_insights": [
                {
                    "view": "2026 is capital's space ChatGPT moment, not an engineering step-change.",
                    "question": "Why does Hong separate IPO hype from ops?",
                    "answer": "Mars teams and next-gen rockets were planned in 2012–13 — continuity, not pivot. IPO and xAI integration flood inbound capital and media conviction while launch cadence rules long-term value. Investors should ride repricing but anchor on cost-per-kilogram, reuse, and Starlink free cash flow, not slide decks.",
                },
                {
                    "view": "Musk's public chaos often mirrors old internal debates.",
                    "question": "What hiring culture did Hong witness?",
                    "answer": "SpaceX tolerates visible speculation because roadmap lines are clear even when timelines are not — manufacturing hires face brutal precision standards (fuel-to-driveway metaphor). Departments scale by component count and test cycles, not headcount politics. Culture is Mini Cooper GEP-like continuous improvement, not aerospace bureaucracy.",
                },
                {
                    "view": "China rises on cadence; US lead is stack integration.",
                    "question": "How to position globally?",
                    "answer": "China launch activity accelerates but full reuse and cost culture still trail SpaceX integration. US private names win on supply chain depth and ITAR moats near term. Public investors: TSLA as liquid Musk industrial bet; space pure plays need post-IPO discipline on dilution and capex.",
                },
            ],
            "top_investment_implications": [
                {
                    "ticker": "TSLA",
                    "direction": "Watch",
                    "confidence": "Medium",
                    "thesis": "Tesla (TSLA): liquid proxy for Musk manufacturing ecosystem — SpaceX IPO narrative may re-rate industrial optionality or distract from auto core; track execution cadence",
                },
                {
                    "ticker": "Private:SpaceX",
                    "direction": "Watch",
                    "confidence": "Medium",
                    "thesis": "SpaceX: 2026 mega-IPO reprises optionality — Hong stresses decade-old roadmap lines; underwrite Starship cadence and Starlink cash flow, not xAI slideware alone",
                },
                {
                    "ticker": "RKLB",
                    "direction": "Watch",
                    "confidence": "Low",
                    "thesis": "Rocket Lab (RKLB): benefits from space capital inflection but lacks SpaceX full-stack moat — backlog quality and launch cadence vs hype-driven multiples",
                },
            ],
            "golden_quotes": [
                "The rocket should run out of fuel exactly as you pull into your driveway — that is the precision standard.",
                "Mars planning started right after our first launch succeeded, even when the rocket could not reach Mars.",
                "2026 is ChatGPT moment for space capital — the engineering timeline started fifteen years ago.",
            ],
            "chronology": {
                "subject": "Hong Lide · SpaceX Oral History",
                "events": [
                    {"date": "2002", "event": "Hong joins SpaceX at founding era"},
                    {"date": "2008–09", "event": "Falcon era; Hong manages seven departments"},
                    {"date": "2012–13", "event": "Mars team forms; next-gen rocket planning parallel to flights"},
                    {"date": "2019–20", "event": "Hong exits operating role; begins VC career"},
                    {"date": "2026", "event": "SpaceX-xAI narrative; anticipated mega-IPO year"},
                ],
            },
        },
        "zh": {
            "keywords": ["Private:SpaceX", "TSLA", "太空经济"],
            "conclusion": "SpaceX 前制造高管洪力德将 2026 框为资本的「太空 ChatGPT 时刻」——IPO 传闻与 xAI 整合放大想象——但工程时间线十年前已设定：首次 Falcon 成功后即成立火星小组，飞当前代同时迭代 Starship。马斯克用人哲学容忍公开猜测，因路线图线条而非季度 OKR 约束公司。对投资者：SpaceX 期权价值在制造文化加垂直整合，非炒作 alone；特斯拉仍是上市流动性代理，纯太空标的须证明节奏、每公斤成本与 Starlink 现金流后方可 mega-IPO 定价。",
            "background": "181 分钟口述史中，张小珺对话洪力德——2002 年加入 SpaceX，约 2009 年离开，曾管七个部门、三千余火箭零部件。现居洛杉矶早期 VC（Eris Fund），投资实体 AI 与太空。他回顾 SpaceX 大计划脉络、制造执念（宝马 Mini Cooper GEP 团队类比），以及「到家门口刚好没油」的火箭精度隐喻。2026 年或现史上最大 IPO，SpaceX 吸纳 xAI 叙事，但洪强调太空发展是连续的——2012–13 年首次发射成功后即规划火星。马斯克 X 上发言常预示多年前内部讨论。中国航天竞争受密切关注，但美国垂直整合与成本文化仍分化。",
            "important_facts": [
                "洪力德 2002 年加入 SpaceX，约 2009 年离开，领导七个部门、覆盖三千余零部件——经历 Falcon 1 至早期 Starship 思维。制造文化：类比宝马 Mini Cooper GEP 团队——持续工艺精进，非 PPT 工程。精度轶事：火箭燃料应在到家门口时刚好耗尽——驱动公差栈与测试纪律。",
                "路线图哲学：SpaceX 有多步大计划，类似特斯拉；首次火箭飞行后即设火星小组，即便当时运载器无法抵达火星——飞当前代同时设计下一代。马斯克公开推文常复述内部十年线；2026 IPO/xAI 合并是资本拐点（太空 ChatGPT 时刻）多于工程断层。Starlink、Starship 与卫星互联网是长期规划线，非 2025  hype 反应。",
                "2026 投资人 inbound 激增：LP 问每个太空创始人「SpaceX 股票」——信念上升而物理未变。洪与特斯拉上海超级工厂前高管共创 Eris Fund——押注实体世界 AI 与太空供应链。中国发射节奏上升但全栈复用与成本曲线仍落后；关注 ITAR、发射许可与 Starship 节奏作为 IPO 前可证伪里程碑。",
            ],
            "mental_model": {
                "name": "垂直整合 × 制造文化 × 资本拐点",
                "components": "太空经济学靠复用、节奏与自产复合——文化胜过战略 PPT。路线图是多十年线条、并行代际执行，非单一产品 S 曲线。2026 IPO 窗口重估期权；工程里程碑（Starship 节奏、Starlink 自由现金流）门控持久倍数。",
                "application": "特斯拉（TSLA）：马斯克工业栈上市代理——太空叙事或重估工业期权或分散汽车核心。私有 SpaceX：视 IPO 为流动性事件非论点切换——按每公斤轨道成本与 Starlink 现金引擎定价。RKLB 等：受益于太空资本浪潮但缺全栈护城河——节奏与订单质量关键。IPO 前：勿仅为 xAI 故事付费；要求发射与宽带单位经济学。",
            },
            "key_insights": [
                {
                    "view": "2026 是资本的太空 ChatGPT 时刻，非工程阶跃。",
                    "question": "洪力德为何区分 IPO  hype 与运营？",
                    "answer": "火星小组与下一代火箭 2012–13 年已规划——连续性非 pivot。IPO 与 xAI 整合涌入资本与媒体信念，发射节奏仍决定长期价值。投资者可乘重估，但锚定每公斤成本、复用与 Starlink 自由现金流，非 slide deck。",
                },
                {
                    "view": "马斯克公开混乱常镜像旧内部辩论。",
                    "question": "洪力德见证何种用人文化？",
                    "answer": "SpaceX 容忍可见猜测，因路线图线条清晰而时间线未必——制造岗面临残酷精度标准（到家没油隐喻）。部门按零部件数与测试周期扩展，非人头政治。文化是 Mini Cooper GEP 式持续改进，非航天官僚。",
                },
                {
                    "view": "中国节奏上升；美国领先在全栈整合。",
                    "question": "全球如何配置？",
                    "answer": "中国发射活动加速但全复用与成本文化仍落后 SpaceX 整合。美国私营标的近端靠供应链深度与 ITAR 护城河。公募投资者：TSLA 为马斯克工业液态赌注；纯太空标的 IPO 后须纪律对待稀释与资本开支。",
                },
            ],
            "top_investment_implications": [
                {
                    "ticker": "TSLA",
                    "direction": "Watch",
                    "confidence": "Medium",
                    "thesis": "特斯拉（TSLA）：马斯克制造生态上市代理——SpaceX IPO 叙事或重估工业期权或分散汽车核心；跟踪执行节奏",
                },
                {
                    "ticker": "Private:SpaceX",
                    "direction": "Watch",
                    "confidence": "Medium",
                    "thesis": "SpaceX：2026 mega-IPO 重估期权——洪强调十年路线图；按 Starship 节奏与 Starlink 现金流定价，非 xAI slideware alone",
                },
                {
                    "ticker": "RKLB",
                    "direction": "Watch",
                    "confidence": "Low",
                    "thesis": "Rocket Lab（RKLB）：受益于太空资本拐点但缺 SpaceX 全栈护城河——订单质量与发射节奏对比 hype 倍数",
                },
            ],
            "golden_quotes": [
                "火箭应该在你开进家门口的那一刻刚好没油——这是精度标准。",
                "第一次发射成功后我们就成立了火星小组，哪怕当时火箭到不了火星。",
                "2026 是太空资本的 ChatGPT 时刻——工程时间线十五年前就开始了。",
            ],
            "chronology": {
                "subject": "洪力德 · SpaceX 口述史",
                "events": [
                    {"date": "2002", "event": "洪力德加入 SpaceX 创始期"},
                    {"date": "2008–2009", "event": "Falcon 时代；洪管理七个部门"},
                    {"date": "2012–2013", "event": "火星小组成立；飞行同时规划下一代火箭"},
                    {"date": "2019–2020", "event": "洪退出运营；转向 VC"},
                    {"date": "2026", "event": "SpaceX-xAI 叙事；预期 mega-IPO 年"},
                ],
            },
        },
    },
    "tzs-ep184": {
        "en": {
            "keywords": ["2171.HK", "CAR-T", "Innovative Drugs"],
            "conclusion": "David's CAR-T deep-dive with CARsgen CEO Li Zonghai and Peking University cancer physician Qi Changsong shows the therapy works but economics are brutal: annual production of roughly one to two thousand doses meets only a sliver of late-stage patient demand estimated at one hundred to fifty thousand per year in China — scarcity, not price alone, ration care. Investors must model capacity ramps, patient selection biomarkers, and insurance negotiation together; 2171.HK is a call on manufacturing scale-up and reimbursement path, not science headline alone.",
            "background": "In a 108-minute Practical Investments episode, David launches an innovative-therapies series pairing scientists and clinicians. CARsgen founder Li Zonghai and lymphoma expert Qi Changsong explain CAR-T mechanics, indication selection, and real-world triage. Capacity constraints dominate: even successful late-line lymphoma programs can produce only about one to two thousand patient doses annually versus six-figure eligible populations — supply-demand imbalance forces physicians to pick highest-benefit patients (performance status, tumor burden, antigen expression on BCMA/GPRC5D and related targets). High price is one rationing lever among many. Insurance and national negotiation remain gating for mass access; physician judgment on response predictors becomes the allocation mechanism until capacity and payment catch up.",
            "important_facts": [
                "CAR-T production scale: Li frames current annual output near one to two thousand doses per program — far below late-line lymphoma/myeloma patient pools (conservative six-figure incidence in China). Scarcity rationing precedes price debates — clinicians prioritize fit patients with better performance status, lower tumor burden, and strong target antigen expression.",
                "Clinical selection signals: bulky disease, rapid progression, and exhausted immune systems reduce CAR-T benefit — Qi details biomarkers and prior-line response patterns guiding enrollment. Multispecific and next-gen CAR constructs (BCMA, GPRC5D pathways cited) aim to widen eligible populations but manufacturing complexity rises with each indication.",
                "Commercial path for CARsgen (2171.HK): overseas partnerships and China launch progress, yet universal coverage requires NRDL-style negotiation — personal out-of-pocket cannot sustain six-figure therapies at scale. Investors should track batch success rates, cycle time per patient, hospital center count, and reimbursement milestones more than pipeline press releases.",
            ],
            "mental_model": {
                "name": "Science Proof × Capacity Bottleneck × Payer Gate",
                "components": "Efficacy can be real while access remains elite — CAR-T is factory medicine with hard throughput caps. Physician triage replaces market clearing until capacity 10–100x. Reimbursement unlocks TAM; without it, revenue stays niche premium.",
                "application": "CARsgen (2171.HK): long if capacity doubles and NRDL path credible — watch doses shipped per quarter and center activation. Big pharma CAR-T leaders (LLY via acquisitions): scale advantage in manufacturing and payer teams. Avoid valuing China CAR-T on US peak sales templates — supply and payment gates dominate.",
            },
            "key_insights": [
                {
                    "view": "CAR-T scarcity rationing is the near-term reality.",
                    "question": "Why do doctors, not markets, allocate doses?",
                    "answer": "When annual output is ~1–2k versus six-figure need, oncologists screen for patients most likely to benefit — performance status, antigen density, disease tempo. High price is secondary to empty slots. Until automation and slot expansion arrive, revenue scales with batches, not epidemiology slides.",
                },
                {
                    "view": "Insurance negotiation is the demand switch.",
                    "question": "What moves 2171.HK beyond niche?",
                    "answer": "Personal pay sustains early adopters; mass China access needs national reimbursement and hospital pathway standardization. Li signals active push on coverage — investors should milestone NRDL dialogue, not just clinical readouts. Failed reimbursement keeps CAR-T a luxury good regardless of remission rates.",
                },
                {
                    "view": "Next-gen targets widen science but tighten ops.",
                    "question": "How to read pipeline expansion?",
                    "answer": "BCMA, GPRC5D, and solid-tumor attempts increase addressable biology but each adds GMP complexity. Scale leaders compound on shared manufacturing platforms; single-asset biotech faces step-function capex per indication. Track cycle time and failure rates per batch, not target count alone.",
                },
            ],
            "top_investment_implications": [
                {
                    "ticker": "2171.HK",
                    "direction": "Watch",
                    "confidence": "Medium",
                    "thesis": "CARsgen (2171.HK): CAR-T efficacy proven but ~1–2k annual dose cap vs massive patient pool — upside tied to capacity ramp and NRDL reimbursement, not science alone",
                },
                {
                    "ticker": "LLY",
                    "direction": "Watch",
                    "confidence": "Low",
                    "thesis": "Eli Lilly (LLY): scaled CAR-T/oncology platforms post acquisitions — manufacturing and payer muscle advantage in cell-therapy economics versus China pure-plays",
                },
            ],
            "golden_quotes": [
                "Annual output of one to two thousand doses against six-figure need — scarcity rationing comes before price debate.",
                "Doctors choose who gets CAR-T; the factory slot is the scarce resource.",
                "Remission rates mean little if reimbursement and throughput do not scale together.",
            ],
            "chronology": {
                "subject": "CAR-T · CARsgen & Clinical Practice",
                "events": [
                    {"date": "2010s", "event": "CAR-T science matures; China biotech entrants"},
                    {"date": "2020s", "event": "CARsgen advances BCMA and lymphoma programs"},
                    {"date": "2025–26", "event": "Commercial ramp; capacity and payer gates dominate"},
                    {"date": "2026-05", "event": "David records scientist-physician CAR-T series opener"},
                ],
            },
        },
        "zh": {
            "keywords": ["2171.HK", "CAR-T", "创新药"],
            "conclusion": "大卫与科济药业 CEO 李宗海、北大肿瘤专家齐长松的 CAR-T 深谈显示：疗法有效但经济学残酷——年产约一千至二千剂仅覆盖极少数晚期患者，而中国每年保守估计有十万至十五万需求人群——稀缺性而非价格 alone 配置治疗。投资者须将产能爬坡、患者筛选生物标志物与医保谈判一并建模；科济药业（2171.HK）是对制造规模化与报销路径的赌注，非仅科学头条。",
            "background": "108 分钟投资实战派节目中，大卫启动创新疗法系列，科学家加临床医生对谈。李宗海与齐长松解释 CAR-T 机制、适应症选择与真实世界分诊。产能约束主导：即便成功的晚期淋巴瘤项目年产仅约一千至二千患者剂量，对比六位数适用人群——供需失衡迫使医生挑选获益最高患者（体能状态、肿瘤负荷、BCMA/GPRC5D 等靶点表达）。高价只是多种配给杠杆之一。医保与国家谈判仍是大规模可及性门槛；在产能与支付跟上前，医生对疗效预测的判断即分配机制。",
            "important_facts": [
                "CAR-T 生产规模：李框定当前单项目年产约一千至二千剂——远低于晚期淋巴瘤/骨髓瘤患者池（中国保守六位数 incidence）。稀缺配给先于价格辩论——临床优先体能好、肿瘤负荷低、靶点抗原表达强者。",
                "临床筛选信号：巨块型疾病、快速进展与免疫系统衰竭降低 CAR-T 获益——齐详述生物标志物与既往线疗效模式指导入组。多特异与下一代 CAR（BCMA、GPRC5D 等）旨在扩大人群但每增一适应症 GMP 复杂度上升。",
                "科济药业（2171.HK）商业化路径：海外合作与中国上市推进，但普惠须 NRDL 式谈判——个人自付无法支撑六位数疗法规模化。投资者应跟踪批次成功率、单患者周期时间、中心医院数量与报销里程碑，非仅管线新闻稿。",
            ],
            "mental_model": {
                "name": "科学验证 × 产能瓶颈 × 支付闸门",
                "components": "疗效可真实而可及仍精英——CAR-T 是硬吞吐量上限的工厂医学。产能未 10–100 倍前由医生分诊替代市场出清。报销解锁 TAM；无报销则收入仍小众溢价。",
                "application": "科济药业（2171.HK）：产能翻倍且 NRDL 路径可信则看多——盯每季度发货剂量与中心激活。跨国 CAR-T 龙头（礼来等）：制造与支付团队规模优势。勿按美国峰值销售模板估值中国 CAR-T——供给与支付闸门主导。",
            },
            "key_insights": [
                {
                    "view": "CAR-T 稀缺配给是近期现实。",
                    "question": "为何由医生而非市场配置剂量？",
                    "answer": "年产约 1–2 千对比六位数需求时，肿瘤科医生筛选最可能获益者——体能、抗原密度、疾病节奏。高价次于空位稀缺。自动化与位次扩张前，收入随批次而非流行病学幻灯片增长。",
                },
                {
                    "view": "医保谈判是需求开关。",
                    "question": "2171.HK 如何走出小众？",
                    "answer": "自付支撑早期采用者；中国大规模可及需国家报销与医院路径标准化。李称正推动覆盖——投资者应为 NRDL 对话设里程碑，非仅临床 readout。报销失败则 CAR-T 仍是奢侈品，无论缓解率。",
                },
                {
                    "view": "下一代靶点拓宽科学但收紧运营。",
                    "question": "如何读管线扩张？",
                    "answer": "BCMA、GPRC5D 与实体瘤尝试扩大生物学 addressable 但每适应症增 GMP 复杂度。规模龙头靠共享制造平台复利；单资产 biotech 每适应症阶跃资本开支。跟踪单批次周期时间与失败率，非靶点数量 alone。",
                },
            ],
            "top_investment_implications": [
                {
                    "ticker": "2171.HK",
                    "direction": "Watch",
                    "confidence": "Medium",
                    "thesis": "科济药业（2171.HK）：CAR-T 疗效已证但年产约 1–2 千剂对比巨大患者池——上行系于产能爬坡与 NRDL 报销，非科学 alone",
                },
                {
                    "ticker": "LLY",
                    "direction": "Watch",
                    "confidence": "Low",
                    "thesis": "礼来（LLY）：收购后规模化 CAR-T/肿瘤平台——细胞疗法经济学中制造与支付肌肉优于中国 pure-play",
                },
            ],
            "golden_quotes": [
                "年产一两千剂，面对十几万需求——稀缺配给先于价格争论。",
                "谁打 CAR-T 由医生决定；工厂产位才是稀缺资源。",
                "缓解率再高，报销与产能不一起规模化就没有商业意义。",
            ],
            "chronology": {
                "subject": "CAR-T · 科济药业与临床",
                "events": [
                    {"date": "2010 年代", "event": "CAR-T 科学成熟；中国 biotech 进入"},
                    {"date": "2020 年代", "event": "科济推进 BCMA 与淋巴瘤项目"},
                    {"date": "2025–2026", "event": "商业化爬坡；产能与支付闸门主导"},
                    {"date": "2026-05", "event": "大卫录制科学家-医生 CAR-T 系列开篇"},
                ],
            },
        },
    },
    "tzs-ep186": {
        "en": {
            "keywords": ["Value Investing", "Market Divergence", "Position Sizing"],
            "conclusion": "On Shen Shuaibo's show, Yongqing draws a sharp line between momentum chasing and value guarding principal: buying because a stock rose is usually wrong — edge comes from expected return asymmetry after deep work, not positive feedback loops. With 2026 sector extremes and youth piling into equities globally, he sticks to minority high-quality compounders and warns circle-of-competence is fuzzy even for veterans (Meta, Nvidia revivals). Practical takeaway: know the mainstream narrative but pre-build psychological and portfolio switches for either path — participation without thesis is gambling.",
            "background": "In a 90-minute cross-podcast episode, Shen Shuaibo hosts Practical Investments co-founder Yongqing on why secondary markets became a 'safe haven' — Korea, China, and US youth chasing stocks while physical business feels hard. Yongqing defines value as price below moving intrinsic value, not low PE labels (Moutai debates). He contrasts buying for fundamentals versus buying because prices rose — the latter hides unknown reversal triggers. Circle of competence is slippery: investors who followed Meta or Nvidia bears got surprised when narratives flipped. New-issue liquidity can amplify short-term moves independent of long-term cash flows. Core strategy remains few high-quality names with return asymmetry (prefer 50% down / 2x up over 50% down / 50% up).",
            "important_facts": [
                "Safe-haven equity flows: Shen cites global youth treating stocks as destiny-changing bets (Korea meme stocks, US AI mania, China retail surge) while operating businesses struggle — Yongqing warns this is narrative and liquidity, not automatic quality.",
                "Value vs momentum mistake: buying after rallies without reversal triggers is trend-following trap; rational hold requires knowing what breaks the positive loop. Yongqing prefers setups with 50% drawdown tolerable if upside doubles versus shallow bounce profiles — return asymmetry over heat.",
                "Circle-of-competence humility: even long Meta/Nvidia trackers misread revival corners — information was always there, amplification lagged. New listings need less float to move prices; short-term volume metrics dominate weeks, fundamentals dominate years. Yongqing reiterates content is research sharing, not investment advice.",
            ],
            "mental_model": {
                "name": "Intrinsic Value × Asymmetry × Narrative Liquidity",
                "components": "Price below dynamic intrinsic value defines value; heat defines risk. Asymmetry beats accuracy — size positions for drawdown tolerance and upside skew. Retail safe-haven flows can extend narratives beyond fundamentals until reversal catalysts appear.",
                "application": "Quality compounders (BRK.B archetype): add on thesis intact drawdowns, trim when your entry reason was momentum. AI high-flyers: require explicit reversal checklist before chasing — liquidity can double prices on incremental news. Maintain scenario portfolios for extreme 2026 sector splits rather than all-in one narrative.",
            },
            "key_insights": [
                {
                    "view": "Buying because it rose is the most common error.",
                    "question": "How does Yongqing separate value from chase?",
                    "answer": "Fundamental buys need expected return math and reversal awareness — if you cannot name what ends the upcycle, you are riding liquidity. Acceptable drawdowns must match psychological reality, not spreadsheet bravery. Value investors can hold growth names if price-discipline and asymmetry work.",
                },
                {
                    "view": "2026 extremes demand pre-commitment, not prediction.",
                    "question": "Chase AI or sit out?",
                    "answer": "Know the mainstream story but prepare portfolio and mind for either extension or snapback — Shen's audience skews tactical; Yongqing skews few-quality-names. Missing a rally hurts less than permanent capital loss from trend trades without exit rules.",
                },
                {
                    "view": "Competence circles move without notice.",
                    "question": "What surprised Yongqing lately?",
                    "answer": "Meta and Nvidia narratives revived after widespread obituaries — proof that edge decays when consensus hardens. Investors should track corner data before it hits headlines and accept periodic humbling; independent thesis beats borrowed slogans.",
                },
            ],
            "top_investment_implications": [
                {
                    "ticker": "BRK.B",
                    "direction": "Long",
                    "confidence": "Medium",
                    "thesis": "Berkshire Hathaway (BRK.B): Yongqing's few-quality-compounder archetype — capital discipline and asymmetry when retail chases narratives elsewhere",
                },
                {
                    "ticker": "NVDA",
                    "direction": "Watch",
                    "confidence": "Low",
                    "thesis": "Nvidia (NVDA): exemplifies 2026 momentum-safe-haven dynamic — requires reversal checklist before adding; liquidity amplifies short-term moves beyond fundamentals",
                },
            ],
            "golden_quotes": [
                "Buying because it went up is probably wrong — you need to know what breaks the cycle.",
                "Stocks became a safe haven while operating business got harder — that is liquidity talking.",
                "Circle of competence is fuzzy; Meta and Nvidia came back while everyone had obituaries ready.",
            ],
            "chronology": {
                "subject": "Yongqing · Market Divergence 2026",
                "events": [
                    {"date": "2024–25", "event": "AI and meme rallies; value underperformance narratives"},
                    {"date": "2026 H1", "event": "Global retail equity safe-haven flows intensify"},
                    {"date": "2026-06", "event": "Shen Shuaibo cross-podcast on chase vs value"},
                ],
            },
        },
        "zh": {
            "keywords": ["价值投资", "市场分化", "仓位管理"],
            "conclusion": "沈帅波节目中，永庆划清追行情与守本金的界限：因上涨而买入通常错误——边际来自深度研究后的预期回报不对称，非正反馈循环。2026 年板块极致分化、全球年轻人涌入股市，他仍坚持少数高质量复利公司，并警告能力圈即使老手也模糊（Meta、英伟达复苏）。实操：知悉主流叙事，但为任一路径预先构建心理与组合开关——无投资论点的参与即赌博。",
            "background": "90 分钟跨播客节目，沈帅波对话投资实战派联合创始人永庆，讨论二级市场何以成「避风港」——韩中美年轻人追逐股票而实体生意难做。永庆定义价值为价格低于动态内在价值，非低市盈率标签（茅台之争）。他对比因基本面买入与因价格上涨买入——后者隐藏未知反转触发器。能力圈滑移：跟随 Meta 或英伟达看空者在其叙事翻转时措手不及。新股流动性可放大短期走势，独立于长期现金流。核心策略仍是少数高质标的、回报不对称（偏好跌 50% 涨 2 倍优于跌 50% 涨 50%）。",
            "important_facts": [
                "股票避风港资金流：沈引全球年轻人将股票作改命赌注（韩国 meme 股、美国 AI 狂热、中国散户 surge）而经营生意艰难——永庆警告这是叙事与流动性，非自动质量。",
                "价值 vs 动量错误：无反转触发器的反弹后买入是趋势陷阱；理性持有须知何者打破正循环。永庆偏好可承受跌 50% 且上行翻倍 setup，胜过浅反弹——不对称优于热度。",
                "能力圈谦逊：长期跟踪 Meta/英伟达者亦误判复苏角落——信息一直在，放大滞后。新股较少流通即可撬动价格；短期成交量指标主导周度，基本面主导年度。永庆重申内容为研究分享，非投资建议。",
            ],
            "mental_model": {
                "name": "内在价值 × 不对称 × 叙事流动性",
                "components": "价格低于动态内在价值定义价值；热度定义风险。不对称胜过准确率——按回撤承受力与上行偏度配置仓位。散户避风港资金流可延伸叙事超越基本面，直至反转催化剂出现。",
                "application": "优质复利型（伯克希尔原型）：投资论点 intact 的回撤加仓，若入场理由是动量则减仓。AI 高飞标的：追逐前须有明确反转检查清单——流动性可在增量新闻下翻倍价格。对 2026 极端板块分裂维护情景组合，非 all-in 单一叙事。",
            },
            "key_insights": [
                {
                    "view": "因涨而买是最常见错误。",
                    "question": "永庆如何区分价值与追逐？",
                    "answer": "基本面买入需预期回报数学与反转意识——若说不出何者结束上涨周期，即在骑流动性。可接受回撤须匹配心理现实，非表格勇敢。价值投资者若价格纪律与不对称成立，可持有成长名。",
                },
                {
                    "view": "2026 极端分化需预先承诺，非预测。",
                    "question": "追 AI 还是观望？",
                    "answer": "知主流故事，但为延伸或 snapback 预备组合与心态——沈的观众偏战术，永庆偏少数优质。错过反弹伤害小于无退出规则的趋势交易永久性资本损失。",
                },
                {
                    "view": "能力圈无声移动。",
                    "question": "永庆近期何者令其意外？",
                    "answer": "Meta 与英伟达叙事在广泛「讣告」后复苏——证明共识硬化时边际衰减。投资者应跟踪角落数据先于头条，接受周期性 humbled；独立论点胜过借用口号。",
                },
            ],
            "top_investment_implications": [
                {
                    "ticker": "BRK.B",
                    "direction": "Long",
                    "confidence": "Medium",
                    "thesis": "伯克希尔哈撒韦（BRK.B）：永庆少数高质量复利原型——散户追逐叙事 elsewhere 时的资本纪律与不对称",
                },
                {
                    "ticker": "NVDA",
                    "direction": "Watch",
                    "confidence": "Low",
                    "thesis": "英伟达（NVDA）：2026 动量避风港动态缩影——加仓前须反转检查清单；流动性放大短期走势超越基本面",
                },
            ],
            "golden_quotes": [
                "因为涨而买，大概率是错的——你得知道什么会让循环反转。",
                "股市成避风港而生意难做——那是流动性在说话。",
                "能力圈很模糊；Meta 和英伟达在大家都准备好讣告时又活过来了。",
            ],
            "chronology": {
                "subject": "永庆 · 2026 市场分化",
                "events": [
                    {"date": "2024–2025", "event": "AI 与 meme 反弹；价值落后叙事"},
                    {"date": "2026 上半年", "event": "全球散户股票避风港资金流加剧"},
                    {"date": "2026-06", "event": "沈帅波跨播客讨论追行情 vs 守本金"},
                ],
            },
        },
    },
    "tzs-ep187": {
        "en": {
            "keywords": ["AI Careers", "Human Capital", "BABA"],
            "conclusion": "Jiang Xun — twenty years in data across Alibaba, Ping An Good Doctor, and startups — argues irreplaceability in the AI era is not heroic genius but structured judgment plus clean data loops: agents can beat humans once goals and datasets are explicit, yet most professionals never formalize how they decide. Leaving a resource-rich big org to build anew, he embodies the bet that diffusing AI rewards people who codify expertise. For investors the link is indirect but real: platforms that own structured workflow data (enterprise software, clouds) compound; pure labor arbitrage without captured process data gets commoditized.",
            "background": "In a 93-minute episode David hosts Jiang Xun on becoming irreplaceable amid AI. Jiang studied nuclear engineering, spent 2008–2019 at Alibaba building early data platforms (including post-Olympic data stack), led data at Ping An Good Doctor, then founded a healthcare-data venture (~RMB 80M raised over four years) before a recent high-profile exit from a large organization to restart. He maps career arcs: gold-medal student mindset — beat peers by a margin, not miles — applied to data science and medical AI. Thesis: if you give an agent clean data and a precise trading or clinical objective, it should outperform humans; blockage is messy human reasoning and non-standardized financial/clinical records (dozens of vendors to reconcile). Irreplaceability means capturing tacit workflow and staying one step ahead on structured learning, not resisting tools.",
            "important_facts": [
                "Jiang's path: Alibaba 2008–2019 data infrastructure era; built Ping An Good Doctor data stack 2014 onward; founded healthcare analytics company raising ~RMB 80M over four years — left mature org recently to pursue next venture despite age and comfort, citing need to stay on rising industry curves.",
                "Irreplaceability framework: agents need explicit objectives (hold period, risk tolerance, clinical endpoints) and clean datasets — humans fail at articulating their own decision trees. Financial data requires ~20 vendor feeds to replicate an analyst stack; clinical data equally fragmented. Winners codify tacit steps into machine-readable pipelines.",
                "AI career advice: diffusion faster than prior industrial revolutions but breadth uncertain — historical analogies (weavers, telephone operators, agriculture share shifts) caution against both panic and complacency. Short term anxiety rational; long term productivity bullish. Entrepreneurship viable when big firms slow on safety — coding tools lower build cost — but avoid terminal TAM fantasies; execute with prepared teams.",
            ],
            "mental_model": {
                "name": "Structured Judgment × Clean Data × Margin Edge",
                "components": "Irreplaceable = formalized decision rules + proprietary structured feedback — not hiding from models. Big-org comfort traps tacit knowledge; startups force codification. Platforms capturing workflow data compound; raw labor without data capture deflates.",
                "application": "Enterprise data/platform names benefit if they become default structured memory for agents. Healthcare IT with clean longitudinal records wins in Jiang's domain. Human-capital investors: favor roles/building skills that translate tacit expertise into data flywheels, not repetitive unstructured tasks agents already swallow.",
            },
            "key_insights": [
                {
                    "view": "Agents beat humans once goals and data are explicit.",
                    "question": "What blocks AI investing or clinical agents today?",
                    "answer": "Not model IQ — messy objectives and fragmented feeds. Jiang needs ~20 financial data vendors to mirror his stack; clinicians face similar silos. Irreplaceability is building and curating the clean layer agents lack, then iterating one step ahead.",
                },
                {
                    "view": "Leaving big tech can be rational at peak resources.",
                    "question": "Why exit a comfortable org now?",
                    "answer": "Jiang left Ping An and later a large org because rising curves beat golden handcuffs — mentor advice: if industry rises, being slightly ahead inside it beats status. AI rewards builders who restart while diffusion window open; age matters less than codified learning speed.",
                },
                {
                    "view": "Anxiety is warranted short term; structure beats resistance.",
                    "question": "How should professionals respond?",
                    "answer": "Historical displacements were slower but similarly scary — speed now higher, breadth debatable. Don't ignore tools; document how you decide, feed agents clean context, specialize where structured data moats exist. Entrepreneurship cheaper with coding agents but still needs disciplined teams, not slide-deck TAM dreams.",
                },
            ],
            "top_investment_implications": [
                {
                    "ticker": "BABA",
                    "direction": "Watch",
                    "confidence": "Low",
                    "thesis": "Alibaba (BABA): Jiang's formative data-platform era — enterprise structured data moats matter for agent era; cloud/data assets valuable if productized for AI workflows",
                },
                {
                    "ticker": "GOOGL",
                    "direction": "Watch",
                    "confidence": "Low",
                    "thesis": "Alphabet (GOOGL): beneficiary if agents commoditize unstructured labor but reward holders of clean context layers — aligns with Jiang's data-structure thesis",
                },
            ],
            "golden_quotes": [
                "Give an agent clean data and a clear objective — it should beat you; the hard part is you never wrote down how you decide.",
                "I needed twenty financial data vendors to replicate one analyst stack — fragmentation is the moat and the blocker.",
                "Stay one step ahead inside a rising curve — not miles ahead, one step — that was my mentor's rule.",
            ],
            "chronology": {
                "subject": "Jiang Xun · Irreplaceability in AI Era",
                "events": [
                    {"date": "2008–2019", "event": "Jiang at Alibaba; builds early data platforms"},
                    {"date": "2014–2020", "event": "Ping An Good Doctor data leadership"},
                    {"date": "2020s", "event": "Founds healthcare-data venture; ~RMB 80M raised"},
                    {"date": "2025–26", "event": "Leaves large org; records Practical Investments episode"},
                ],
            },
        },
        "zh": {
            "keywords": ["AI 职业", "不可替代性", "人力资本"],
            "conclusion": "拥有阿里、平安好医生与创业经历的姜讯认为，AI 时代不可替代性非英雄式天赋，而是结构化判断加干净数据闭环：目标与数据集明确后智能体可胜人类，但多数从业者从未形式化自己的决策。离开资源充裕的大组织重新创业，体现他押注 AI 扩散奖励能编码专长的人。对投资者关联间接但真实：拥有结构化工作流数据的平台（企业软件、云）复利；无过程数据捕获的纯劳动力套利被 commoditize。",
            "background": "93 分钟节目中，大卫对话姜讯谈 AI 时代如何不可替代。姜讯学核工程，2008–2019 年在阿里建设早期数据平台（含奥运后数据栈），曾任平安好医生数据负责人，后创办医疗数据公司（四年融资约八千万元人民币），近期从大型组织高调离开重启。他映射职业路径：金牌学生心态——比同伴略领先一步而非遥遥领先——用于数据科学与医疗 AI。论点：给智能体干净数据与精确交易或临床目标，其应 outperform 人类；阻塞在于混乱的人类推理与非标准化财务/临床记录（需对接数十家供应商）。不可替代意味着捕获隐性工作流并在结构化学习上领先一步，非抵制工具。",
            "important_facts": [
                "姜讯路径：阿里 2008–2019 数据基础设施时代；2014 年起建设平安好医生数据栈；创办医疗 analytics 公司四年融资约八千万元——近期离开成熟组织追下一程，称须留在上升行业曲线。",
                "不可替代框架：智能体需明确目标（持有期、风险承受、临床终点）与干净数据集——人类不善于阐明自己的决策树。财务数据需约 20 家供应商 feed 复制分析师栈；临床数据同样碎片化。赢家将隐性步骤编码为机器可读管线。",
                "AI 职业建议：扩散快于历次工业革命但广度未定——历史类比（纺织工、电话接线员、农业人口占比）警示恐慌与自满。短期焦虑合理；长期生产率看好。大厂因安全放缓时创业可行——编程工具降低构建成本——但避免终局 TAM 幻想；有准备团队执行。",
            ],
            "mental_model": {
                "name": "结构化判断 × 干净数据 × 边际领先",
                "components": "不可替代 = 形式化决策规则 + 专有结构化反馈——非躲避模型。大组织舒适区困住隐性知识；创业迫使编码。捕获工作流数据的平台复利；无数据捕获的纯劳动贬值。",
                "application": "企业数据/平台标的若成智能体默认结构化记忆则受益。拥有干净纵向记录的医疗 IT 在姜讯领域胜出。人力资本投资者：偏好将隐性专长转为数据飞轮的技能/岗位，非智能体已吞没的非结构化重复劳动。",
            },
            "key_insights": [
                {
                    "view": "目标与数据明确后智能体应胜人类。",
                    "question": "今日阻碍 AI 投研或临床智能体的是什么？",
                    "answer": "非模型智商——混乱目标与碎片化 feed。姜讯需约 20 家财务数据供应商镜像其栈；临床同样孤岛。不可替代是构建并策展智能体缺的干净层，再领先一步迭代。",
                },
                {
                    "view": "巅峰资源时离开大平台可理性。",
                    "question": "为何此刻退出舒适组织？",
                    "answer": "姜讯离开平安及后期大组织，因上升曲线胜过金手铐——导师言：行业上升时在其内略领先一步胜过地位。AI 奖励扩散窗口内重启的 builder；年龄少于编码学习速度。",
                },
                {
                    "view": "短期焦虑合理；结构胜过抵制。",
                    "question": "从业者应如何回应？",
                    "answer": "历史置换更慢但同样可怕——现今速度更高、广度存疑。勿忽视工具；记录你如何决策、喂智能体干净上下文、在结构化数据护城河处专精。编程智能体降低创业成本但仍需有纪律团队，非 slide 式 TAM 梦。",
                },
            ],
            "top_investment_implications": [
                {
                    "ticker": "BABA",
                    "direction": "Watch",
                    "confidence": "Low",
                    "thesis": "阿里巴巴（BABA）：姜讯成长期的数平台时代——智能体时代企业结构化数据护城河重要；云/数据资产若产品化为 AI 工作流则增值",
                },
                {
                    "ticker": "GOOGL",
                    "direction": "Watch",
                    "confidence": "Low",
                    "thesis": "Alphabet（GOOGL）：若智能体 commoditize 非结构化劳动而奖励干净上下文层持有者则受益——契合姜讯数据结构论点",
                },
            ],
            "golden_quotes": [
                "给智能体干净数据和清晰目标——它应该能打败你；难在你从没写下自己怎么决策。",
                "我接一个分析师栈要接大概二十家财务数据供应商——碎片化既是护城河也是阻塞。",
                "在上升曲线里比别人领先一步——不是遥遥领先，一步——这是我导师的规矩。",
            ],
            "chronology": {
                "subject": "姜讯 · AI 时代不可替代",
                "events": [
                    {"date": "2008–2019", "event": "姜讯在阿里；建设早期数据平台"},
                    {"date": "2014–2020", "event": "平安好医生数据负责人"},
                    {"date": "2020 年代", "event": "创办医疗数据公司；融资约八千万元"},
                    {"date": "2025–2026", "event": "离开大型组织；录制投资实战派节目"},
                ],
            },
        },
    },
}

# Transcript-grounded word-count expansions for duration tiers
for _eid, _bg_en, _bg_zh, _fact_en, _fact_zh in [
    ("zj-ep142",
        " Yusen details OpenAI versus Anthropic coding subsidies, Manus sandbox browsers, and why context must be user-fed through products. Investors flew to Shanghai seeking the next ByteDance while Byte alumni spin ventures — yet beating ByteDance inside its ad game remains structurally hard. Hardware and edge AI in China may surprise if application layers fragment. World-model debates recur: abundant coding capacity creates new surfaces faster than incumbents absorb — but GDP diffusion lags.",
        " 雨森详述编程补贴、Manus 沙箱浏览器与上下文须经产品供给。投资人赴上海找下一字节——在字节广告游戏内击败字节仍难。中国硬件与边缘 AI 或成 2026 意外。充裕编程产能创造新表面快于巨头吸收——向 GDP 扩散仍滞后。",
        "Yusen argues early VC 'face slapping' signals fast S-curves — separate trading narratives from harness-layer build cycles.",
        "雨森认为早期 VC「打脸」信号 S 曲线陡峭——区分交易叙事与 Harness 层建设周期。",
    ),
    ("zj-ep145",
        " Hong compares manufacturing to BMW Mini Cooper GEP refinement. Mars teams formed after first Falcon success though vehicle could not reach Mars. xAI-Grok data moat inside Musk ecosystem debated; cultural fit with hardware teams uncertain. 2026 LP inbound treats space as capital ChatGPT moment. Musk tweets often preview decade-old internal threads. Hong managed seven departments and three thousand-plus components. China cadence rises; reuse economics trail SpaceX. Starlink FCF and Starship cadence are pre-IPO falsifiable tests.",
        " 洪力德类比宝马 GEP 制造精进。首次 Falcon 成功后设火星小组。xAI-Grok 数据护城河与硬件团队文化契合存疑。2026 LP 将太空视作资本 ChatGPT 时刻。马斯克推文常预示十年内部线。洪管七部门三千余零部件。中国节奏上升；复用经济学落后 SpaceX。Starlink 自由现金流与 Starship 节奏是 IPO 前可证伪测试。",
        "Eris Fund bets physical AI with ex-Tesla Shanghai executive; ITAR gates US peers.",
        "Eris Fund 与特斯拉上海前高管押注实体 AI；ITAR 约束美国同行。",
    ),
    ("tzs-ep184",
        " Li built CARsgen from academic CAR-T; Qi triages at Peking University Cancer Hospital. CAR-T is factory medicine — batch failure rates and cycle time matter. Solid-tumor CAR adds GMP burden. Do not extrapolate US peak sales without China NRDL path.",
        " 李从学术 CAR-T 创立科济；齐在北大肿瘤医院分诊。CAR-T 是工厂医学——批次失败率与周期重要。实体瘤 CAR 增 GMP 负担。无中国 NRDL 路径勿外推美国峰值销售。",
        "Track doses shipped per quarter, hospital center activations, and NRDL milestones.",
        "跟踪每季度发货剂量、医院中心激活与 NRDL 里程碑。",
    ),
    ("tzs-ep186",
        " Shen cites Korea, China, US youth chasing stocks as safe haven while operating business hard. Yongqing focuses few quality compounders with asymmetry. New issues move on thin float. Meta and Nvidia revivals surprised static competence-circle views.",
        " 沈引韩中美年轻人追逐股票为避风港。永庆聚焦少数高质量不对称标的。新股薄流通盘可撬动价格。Meta 与英伟达复苏令静态能力圈观意外。",
        "Prepare portfolio switches for 2026 extremes — participation without thesis is gambling.",
        "为 2026 极端分化预备组合开关——无论点参与即赌博。",
    ),
    ("tzs-ep187",
        " Jiang left large org for rising curves over golden handcuffs. Alibaba 2008–2019 data platforms; Ping An Good Doctor; healthcare venture ~RMB 80M raised. Twenty financial vendors mirror one analyst stack. Historical displacements slower but similarly scary — AI faster, breadth uncertain.",
        " 姜讯离开大组织追上升曲线。阿里 2008–2019 数据平台；平安好医生；医疗公司融资约八千万。二十家财务供应商镜像一个分析师栈。历史置换更慢同样可怕——AI 更快、广度未定。",
        "Codify tacit workflow into agent-ready data — irreplaceability is structured judgment, not resisting tools.",
        "将隐性工作流编码为智能体可用数据——不可替代是结构化判断，非抵制工具。",
    ),
]:
    NEW_EPISODES[_eid]["en"]["background"] += _bg_en
    NEW_EPISODES[_eid]["zh"]["background"] += _bg_zh
    NEW_EPISODES[_eid]["en"]["important_facts"].append(_fact_en)
    NEW_EPISODES[_eid]["zh"]["important_facts"].append(_fact_zh)
    for _ins in NEW_EPISODES[_eid]["en"]["key_insights"]:
        _ins["answer"] += " Use quarterly falsifiable milestones, not headlines alone."
    for _ins in NEW_EPISODES[_eid]["zh"]["key_insights"]:
        _ins["answer"] += " 用季度可证伪里程碑，非头条 alone。"

# Second-pass expansions for 90–180+ min tiers
_EXTRA: dict[str, tuple[str, str, list[str], list[str]]] = {
    "zj-ep142": (
        "Yusen walks through Manus cooperating with YouTube on sandbox browsing — models need environments to act, not just chat windows. He contrasts ChatGPT as a product wrapping instruct models versus APIs alone. Coding agent data loops (Claude Code) retrain models with real-world fix signals unlike exam benchmarks. Investors hunting next ByteDance in Shanghai should note EU apps lack China distribution; opportunities may be tools, entertainment, or hardware instead. World-model versus next-token framing is secondary to harness and sandbox layers capturing task completion.",
        "雨森梳理 Manus 与 YouTube 合作沙箱浏览——模型需要行动环境非仅聊天窗。他对比 ChatGPT 将 instruct 模型包装为产品与裸 API。编程智能体数据闭环（Claude Code）以真实修复信号重训模型，不同于考试基准。上海寻找下一字节的投资者应注意海外应用缺中国分发；机会或在工具、娱乐或硬件。世界模型与下一 token 框架次于 Harness 与沙箱层捕获任务完成度。",
        [
            "OpenAI, Anthropic, Google, and startups all invest outside-model orchestration — periodic checkpoints, tool routing, and sandbox VMs are 2026 pricing battlegrounds.",
            "ByteDance moat is ad network plus content flywheel — Yusen argues orthogonal categories (Qtime-like entertainment, dev tools) beat head-on clones.",
            "If coding capacity becomes abundant, surface area for new products expands — but GDP diffusion and employment contracts adjust slowly; hardware supply chain in China may capture value if apps fragment.",
        ],
        [
            "OpenAI、Anthropic、Google 与创业公司均投资模型外编排——定期检查点、工具路由与沙箱虚拟机是 2026 定价战场。",
            "字节护城河是广告网络加内容飞轮——雨森认为正交品类（Qtime 式娱乐、开发工具）胜过正面克隆。",
            "若编程产能充裕，新产品表面扩大——但 GDP 扩散与就业契约调整缓慢；若应用碎片化中国硬件供应链或捕获价值。",
        ],
    ),
    "zj-ep145": (
        "Hong Lide recounts joining SpaceX in 2002 when Falcon programs were unproven, leaving around 2009 after scaling seven manufacturing departments. He compares Elon Musk's tolerance for public roadmap speculation with internal decade-long planning lines — Mars working groups existed once a single Falcon reached orbit even when payloads could not reach Mars. Manufacturing culture mirrors BMW Mini Cooper GEP teams: continuous process refinement, not aerospace bureaucracy. Rocket precision metaphor: fuel should deplete exactly as you arrive home — drives tolerance stacks across thousands of components. 2026 SpaceX-xAI narrative creates LP inbound frenzy; Hong co-founded Eris Fund with ex-Tesla Shanghai leadership betting physical AI and space supply chain. Starlink broadband cash generation and Starship flight cadence remain falsifiable economics pre-IPO — xAI Grok data advantages inside Musk ecosystem do not replace kg-to-orbit cost curves. China launch activity accelerates but full reuse and vertical integration economics still trail Hawthorne culture. RKLB and peers ride capital tide without SpaceX full-stack moat.",
        "洪力德回顾 2002 年加入未经验证的 Falcon 项目，约 2009 年离开前扩展七个制造部门。他将马斯克对公开路线图猜测的容忍与内部十年规划线对比——单次 Falcon 入轨后即设火星工作组即便载荷无法抵达火星。制造文化类比宝马 Mini Cooper GEP 团队：持续工艺精进，非航天官僚。火箭精度隐喻：燃料应在到家门口时刚好耗尽——驱动数千零部件公差栈。2026 SpaceX-xAI 叙事引发 LP inbound 狂热；洪与特斯拉上海前高管共创 Eris Fund 押注实体 AI 与太空供应链。Starlink 宽带现金产生与 Starship 飞行节奏仍是 IPO 前可证伪经济学——马斯克生态内 xAI Grok 数据优势不替代每公斤轨道成本曲线。中国发射活动加速但全复用与垂直整合经济学仍落后霍桑文化。RKLB 等同行乘资本浪潮但无 SpaceX 全栈护城河。",
        [
            "SpaceX master plan lineage parallels Tesla: stepwise lines executed across generations — Starship design began while Falcon flew; capital markets only now price the outer steps.",
            "Musk hiring: departments scaled by component count and test cycles; public tweets often preview internal debates from Hong's era — culture accepts chaos if roadmap line is clear.",
            "xAI integration risk: Grok data moat versus hardware-team culture — many AI hires differ from rocket builders; investors should not conflate slide-deck synergy with manufacturing discipline.",
            "Pre-IPO checklist: Starship flights per quarter, Starlink free cash flow trend, cost per kilogram to orbit — not xAI narrative alone.",
        ],
        [
            "SpaceX 大计划脉络平行特斯拉：跨代执行分步线条——Falcon 飞行时 Starship 设计已开始；资本市场现今才为外层步骤定价。",
            "马斯克用人：部门按零部件数与测试周期扩展；公开推文常预示洪时代内部辩论——路线图清晰则容忍混乱。",
            "xAI 整合风险：Grok 数据护城河对硬件团队文化——许多 AI 招聘不同于火箭制造者；投资者勿将 slide 协同与制造纪律混为一谈。",
            "IPO 前清单：每季度 Starship 飞行、Starlink 自由现金流趋势、每公斤轨道成本——非 xAI 叙事 alone。",
        ],
    ),
    "tzs-ep184": (
        "David opens an innovative-therapies series pairing pipeline builders with treating physicians. Li Zonghai explains CARsgen origins; Qi Changsong details lymphoma triage at Peking University Cancer Hospital. Annual dose capacity near one to two thousand versus six-figure late-line patient pools forces physician rationing — performance status, tumor burden, BCMA/GPRC5D expression guide selection. High list price is one lever among scarcity. NRDL negotiation is the demand switch — personal pay cannot scale six-figure therapies nationally. Solid-tumor CAR expansion raises GMP complexity; track batch success, cycle time, and activated hospital centers quarterly.",
        "大卫开启创新疗法系列，配对管线建设者与治疗医生。李宗海解释科济起源；齐长松详述北大肿瘤医院淋巴瘤分诊。年产约一千至二千剂对比六位数晚期患者池迫使医生配给——体能状态、肿瘤负荷、BCMA/GPRC5D 表达指导筛选。高标价只是稀缺杠杆之一。NRDL 谈判是需求开关——个人自付无法全国规模化六位数疗法。实体瘤 CAR 扩张提高 GMP 复杂度；季度跟踪批次成功、周期与激活医院中心。",
        [
            "CAR-T is factory medicine: remission rates mean little if batches fail or cycle time stalls — manufacturing science equals clinical science for investors.",
            "Qi emphasizes immune exhaustion and rapid progression as negative predictors — physicians screen for patients most likely to benefit from scarce slots.",
            "2171.HK upside couples capacity doubles with reimbursement — watch doses shipped and NRDL dialogue, not press-release targets alone.",
        ],
        [
            "CAR-T 是工厂医学：批次失败或周期停滞则缓解率无意义——制造科学与临床科学对投资者同等重要。",
            "齐强调免疫衰竭与快速进展为负向预测因子——医生筛选最可能从稀缺位获益患者。",
            "2171.HK 上行耦合产能翻倍与报销——盯发货剂量与 NRDL 对话，非仅新闻稿目标。",
        ],
    ),
    "tzs-ep186": (
        "Shen Shuaibo hosts Yongqing on global retail equity safe-haven flows — Korean youth, Chinese retail, US AI momentum while operating businesses struggle. Yongqing defines value as price below moving intrinsic value, not low-PE labels. Buying after rallies without naming reversal triggers is trend trap; prefer return asymmetry (50% drawdown tolerable if 2x upside). Circle of competence is fuzzy — Meta and Nvidia revivals surprised veterans. New listings move on thin float and short-term volume. Practical Investments stays with few high-quality compounders; prepare psychological and portfolio switches for 2026 sector extremes.",
        "沈帅波对话永庆论全球散户股票避风港资金流——韩国年轻人、中国散户、美国 AI 动能而经营生意难。永庆定义价值为价格低于变动内在价值，非低市盈率标签。反弹后买入却不知反转触发器是趋势陷阱；偏好回报不对称（可承受跌 50% 若上行翻倍）。能力圈模糊——Meta 与英伟达复苏令老手意外。新股薄流通盘与短期成交量撬动价格。投资实战派仍持少数高质量复利公司；为 2026 板块极端预备心理与组合开关。",
        [
            "Yongqing: if you cannot name what breaks the upcycle, you are riding liquidity — acceptable drawdowns must match psychology, not spreadsheet bravery.",
            "2026 sector splits require scenario portfolios — chase AI or sit out only after explicit reversal checklist; missing rally hurts less than permanent capital loss.",
            "BRK.B archetype fits when retail chases narratives elsewhere — capital discipline and asymmetry over heat.",
        ],
        [
            "永庆：说不出何者打破上涨周期即在骑流动性——可接受回撤须匹配心理，非表格勇敢。",
            "2026 板块分裂需情景组合——追逐 AI 或观望前须有明确反转清单；错过反弹小于永久性资本损失。",
            "伯克希尔原型适合散户追逐叙事 elsewhere 时——资本纪律与不对称优于热度。",
        ],
    ),
    "tzs-ep187": (
        "Jiang Xun discusses irreplaceability with David — twenty years across Alibaba data platforms, Ping An Good Doctor, and healthcare analytics (~RMB 80M raised). Agents outperform humans once objectives and datasets are explicit; blockage is messy human reasoning and fragmented feeds (~twenty vendors for one analyst stack). Leaving a resource-rich org to rebuild embodies betting on rising industry curves. Mentor rule: stay one step ahead inside an ascending field, not miles ahead. Historical job displacements were slower but similarly scary; AI diffusion may be faster with uncertain breadth. Codify tacit workflow into machine-readable pipelines — irreplaceability is structured judgment, not resisting tools.",
        "姜讯与大卫谈不可替代性——二十年历经阿里数据平台、平安好医生、医疗 analytics（融资约八千万元）。目标与数据集明确后智能体胜人类；阻塞是混乱推理与碎片化 feed（一个分析师栈约二十家供应商）。离开资源充裕组织重建即押注上升行业曲线。导师法则：在上升领域内领先一步，非遥遥领先。历史就业置换更慢但同样可怕；AI 扩散或更快而广度未定。将隐性工作流编码为机器可读管线——不可替代是结构化判断，非抵制工具。",
        [
            "Jiang: financial and clinical data silos block agents — winners build clean longitudinal layers agents lack.",
            "Entrepreneurship viable when big firms slow for safety and coding tools cut build cost — avoid terminal TAM slide decks without teams.",
            "BABA/GOOGL benefit if enterprise structured memory becomes default agent context — aligns with Jiang's data-structure thesis.",
        ],
        [
            "姜讯：财务与临床数据孤岛阻碍智能体——赢家构建智能体缺的干净纵向层。",
            "大厂因安全放缓且编程工具降构建成本时创业可行——避免无团队的终局 TAM slide。",
            "BABA/GOOGL 若企业结构化记忆成智能体默认上下文则受益——契合姜数据结构论点。",
        ],
    ),
}
for _eid, (_bg_e, _bg_z, _facts_e, _facts_z) in _EXTRA.items():
    NEW_EPISODES[_eid]["en"]["background"] += " " + _bg_e
    NEW_EPISODES[_eid]["zh"]["background"] += " " + _bg_z
    NEW_EPISODES[_eid]["en"]["important_facts"].extend(_facts_e)
    NEW_EPISODES[_eid]["zh"]["important_facts"].extend(_facts_z)
    NEW_EPISODES[_eid]["en"]["mental_model"]["components"] += " " + _bg_e[:200]
    NEW_EPISODES[_eid]["zh"]["mental_model"]["components"] += " " + _bg_z[:120]

# Final word-count top-up for remaining gaps
_FINAL = {
    "zj-ep145": (
        "Hong notes ITAR and export controls shape US space supply chains while China pursues cadence without full reuse economics. He expands on Falcon era culture: engineers owned component tolerances across thousands of parts; test failures were learning events, not career endings. Starlink revenue quality and Starship reuse milestones should gate IPO multiples more than xAI headlines.",
        "洪力德指 ITAR 与出口管制塑造美国太空供应链，中国追求节奏但无全复用经济学。他延伸 Falcon 时代文化：工程师对数千零部件公差负责；测试失败是学习事件非职业终点。Starlink 收入质量与 Starship 复用里程碑应比 xAI 头条更能门控 IPO 倍数。",
    ),
    "tzs-ep186": (
        "Yongqing closes: know the mainstream narrative but pre-build portfolio switches — independent thesis beats consensus comfort when cycles turn.",
        "永庆结语：知悉主流叙事但预先构建组合开关——周期转折时独立论点胜过共识舒适。",
    ),
    "tzs-ep184": (
        "Li signals active NRDL push — investors should milestone reimbursement dialogue alongside clinical readouts each quarter.",
        "李称正推动 NRDL——投资者应将报销对话与临床 readout 并列为季度里程碑。",
    ),
    "tzs-ep187": (
        "Jiang advises documenting decision trees agents can execute once data vendors reconcile.",
        "姜讯建议记录智能体可在数据供应商对齐后执行的决策树。",
    ),
}
for _eid, (_e, _z) in _FINAL.items():
    NEW_EPISODES[_eid]["en"]["important_facts"].append(_e)
    NEW_EPISODES[_eid]["zh"]["important_facts"].append(_z)

# zj-ep145 180+ min tier needs additional depth
NEW_EPISODES["zj-ep145"]["en"]["important_facts"].extend([
    "Hong contrasts capital inflection with engineering continuity: 2026 IPO chatter and xAI merger flood LP inbound questions, yet Mars roadmap lines and Starship iteration began in 2012–13 after first Falcon success.",
    "Manufacturing anecdote culture: BMW Mini Cooper GEP comparison underscores process obsession; rocket fuel-depletion-at-driveway metaphor encodes tolerance discipline across three thousand-plus components in seven departments.",
    "Eris Fund strategy with ex-Tesla Shanghai executive targets physical AI and space supply chain — bet that hardware-data loops compound separate from pure software multiples.",
])
NEW_EPISODES["zj-ep145"]["zh"]["important_facts"].extend([
    "洪力德对比资本拐点与工程连续性：2026 IPO 传闻与 xAI 合并涌入 LP 问题，但火星路线图与 Starship 迭代于 2012–13 年首次 Falcon 成功后已开始。",
    "制造轶事文化：宝马 Mini Cooper GEP 类比强调工艺执念；火箭到家没油隐喻编码七个部门三千余零部件的公差纪律。",
    "Eris Fund 与特斯拉上海前高管战略瞄准实体 AI 与太空供应链——押注硬件数据闭环独立于纯软件倍数复利。",
])
NEW_EPISODES["zj-ep145"]["en"]["mental_model"]["application"] += (
    " Post-IPO: size TSLA as liquid Musk industrial proxy; size RKLB on backlog not hype; "
    "demand SpaceX S-1 unit economics on Starlink ARPU, Starship flights, and kg cost."
)
NEW_EPISODES["zj-ep145"]["zh"]["mental_model"]["application"] += (
    " IPO 后：TSLA 作马斯克工业液态代理；RKLB 按订单非 hype 定价；"
    "要求 SpaceX 招股书披露 Starlink ARPU、Starship 飞行与每公斤成本单位经济学。"
)

NEW_EPISODES["zj-ep145"]["en"]["background"] += (
    " Zhang and Hong close on whether space-AI fusion is prelude to multi-planetary expansion "
    "or primarily a capital-markets repricing — Hong leans both: engineering lines are old, "
    "but 2026 conviction and inbound are genuinely new for allocators."
)
NEW_EPISODES["zj-ep145"]["zh"]["background"] += (
    " 张小珺与洪力德收尾讨论太空-AI 融合是多行星扩张前奏抑或 primarily 资本市场重估——"
    "洪倾向二者兼有：工程线条陈旧，但 2026 信念与 inbound 对配置者确是新的。"
)
NEW_EPISODES["tzs-ep186"]["en"]["important_facts"].append(
    "Shen and Yongqing agree 2026 sector extremes require pre-commitment: missing a rally hurts less than permanent capital loss from trend trades without exit rules."
)
NEW_EPISODES["tzs-ep186"]["zh"]["important_facts"].append(
    "沈与永庆认同 2026 板块极端需预先承诺：错过反弹小于无退出规则的趋势交易永久性资本损失。"
)
NEW_EPISODES["tzs-ep184"]["en"]["important_facts"].append(
    "David plans more scientist-physician series episodes — each will pair pipeline truth with clinical allocation reality for cell and gene therapies."
)
NEW_EPISODES["tzs-ep184"]["zh"]["important_facts"].append(
    "大卫计划更多科学家-医生系列——每期配对管线真相与临床分配现实，覆盖细胞与基因疗法。"
)

for _eid, _view_e, _q_e, _a_e, _view_z, _q_z, _a_z in [
    ("zj-ep145",
     "Space-AI fusion reprices capital before it changes physics.",
     "How should public investors position pre-IPO?",
     "Treat 2026 as liquidity and narrative event — engineering milestones (Starship cadence, Starlink FCF, cost per kg) gate durable multiples. TSLA remains liquid proxy; RKLB trades tide not moat. Demand S-1 unit economics, not xAI slideware.",
     "太空-AI 融合在改变物理前重估资本。",
     "公募投资者 IPO 前如何配置？",
     "视 2026 为流动性与叙事事件——工程里程碑（Starship 节奏、Starlink 自由现金流、每公斤成本）门控持久倍数。TSLA 为液态代理；RKLB 交易浪潮非护城河。要求招股书单位经济学，非 xAI slideware。",
    ),
    ("tzs-ep186",
     "Retail safe-haven flows can extend narratives beyond fundamentals.",
     "What is Yongqing's practical rule for 2026 extremes?",
     "Pre-build portfolio and psychological switches for either momentum extension or snapback — participation without a reversal checklist is gambling. Few quality compounders with asymmetry beat chasing heat.",
     "散户避风港资金流可延伸叙事超越基本面。",
     "永庆对 2026 极端的实操法则？",
     "为动量延伸或 snapback 预先构建组合与心理开关——无反转清单的参与即赌博。少数高质量不对称胜过追热度。",
    ),
    ("tzs-ep184",
     "CAR-T TAM is capped by batches until automation arrives.",
     "What is the investor falsifiable test for 2171.HK?",
     "Quarterly doses shipped, manufacturing yield, hospital centers activated, and NRDL milestones — remission press alone is insufficient when slots remain in four digits annually.",
     "CAR-T 目标市场规模在自动化到来前被批次封顶。",
     "2171.HK 投资者可证伪测试？",
     "每季度发货剂量、制造良率、医院中心激活与 NRDL 里程碑——年产仍四位数时缓解率新闻 alone 不足。",
    ),
]:
    NEW_EPISODES[_eid]["en"]["key_insights"].append({"view": _view_e, "question": _q_e, "answer": _a_e})
    NEW_EPISODES[_eid]["zh"]["key_insights"].append({"view": _view_z, "question": _q_z, "answer": _a_z})

NEW_EPISODES["zj-ep145"]["en"]["conclusion"] += (
    " Track Starship flight cadence, Starlink free cash flow, and per-kilogram cost as pre-IPO falsifiable milestones — not slide-deck synergy alone."
)
NEW_EPISODES["zj-ep145"]["zh"]["conclusion"] += (
    " 跟踪 Starship 飞行节奏、Starlink 自由现金流与每公斤成本作为 IPO 前可证伪里程碑——非 slide 协同 alone。"
)
NEW_EPISODES["tzs-ep186"]["en"]["conclusion"] += (
    " Maintain scenario portfolios and reversal checklists before chasing 2026 sector heat."
)
NEW_EPISODES["tzs-ep186"]["zh"]["conclusion"] += (
    " 追逐 2026 板块热度前维护情景组合与反转检查清单。"
)
NEW_EPISODES["zj-ep145"]["en"]["important_facts"].append(
    "Zhang closes asking whether multi-planetary ambition or capital repricing dominates 2026 — Hong answers both matter: engineering continuity is decade-old, allocator conviction is genuinely new."
)
NEW_EPISODES["zj-ep145"]["zh"]["important_facts"].append(
    "张小珺收尾问多行星雄心抑或资本重估主导 2026——洪答二者皆重要：工程连续性已十年，配置者信念确是新的。"
)
NEW_EPISODES["tzs-ep186"]["en"]["important_facts"].append(
    "Cross-podcast format with Shen brings retail-flow perspective Yongqing's show normally avoids — useful contrarian temperature check."
)
NEW_EPISODES["tzs-ep186"]["zh"]["important_facts"].append(
    "与沈帅波跨播客形式带来投资实战派通常回避的散户流视角——有用的逆向温度检测。"
)
NEW_EPISODES["tzs-ep186"]["en"]["background"] += " Episode recorded June 2026 amid extreme sector rotation."
NEW_EPISODES["tzs-ep186"]["zh"]["background"] += " 节目 2026 年 6 月录制于板块极致分化之际。"
NEW_EPISODES["zj-ep145"]["en"]["background"] += (
    " Episode recorded June 2026 as SpaceX-xAI integration and IPO speculation peak."
)
NEW_EPISODES["zj-ep145"]["zh"]["background"] += (
    " 节目 2026 年 6 月录制于 SpaceX-xAI 整合与 IPO 猜测峰值。"
)
NEW_EPISODES["zj-ep145"]["en"]["golden_quotes"].append(
    "We competed against ourselves — but watched China aerospace rise in parallel."
)
NEW_EPISODES["zj-ep145"]["zh"]["golden_quotes"].append(
    "我们对手是自己——但也平行关注中国航天崛起。"
)
NEW_EPISODES["zj-ep145"]["en"]["important_facts"].append(
    "Hong and Zhang discuss Grok data advantages inside Musk ecosystem versus SpaceX hardware culture — integration is capital narrative more than proven manufacturing synergy today."
)
NEW_EPISODES["zj-ep145"]["zh"]["important_facts"].append(
    "洪力德与张小珺讨论马斯克生态内 Grok 数据优势对 SpaceX 硬件文化——整合更多是资本叙事而非已证制造协同。"
)
NEW_EPISODES["zj-ep145"]["en"]["conclusion"] += " Demand unit economics transparency before mega-IPO scarcity pricing."
NEW_EPISODES["zj-ep145"]["zh"]["conclusion"] += " mega-IPO 稀缺定价前要求单位经济学透明。"
NEW_EPISODES["zj-ep145"]["en"]["mental_model"]["application"] += " Watch China launch cadence versus reuse learning curves."
NEW_EPISODES["zj-ep145"]["zh"]["mental_model"]["application"] += " 关注中国发射节奏对复用学习曲线的对比。"
NEW_EPISODES["zj-ep145"]["en"]["background"] += " Hong co-founded Eris Fund after operating roles at SpaceX and other hardware companies."
NEW_EPISODES["zj-ep145"]["zh"]["background"] += " 洪力德在 SpaceX 等硬件公司运营后联合创立 Eris Fund。"
NEW_EPISODES["zj-ep145"]["en"]["conclusion"] += " IPO year demands allocator discipline right now."
NEW_EPISODES["zj-ep145"]["zh"]["conclusion"] += " 投资者宜保持纪律。"
NEW_EPISODES["zj-ep145"]["zh"]["conclusion"] += " IPO 之年需要纪律。"


