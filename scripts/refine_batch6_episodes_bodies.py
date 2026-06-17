"""Body content for 20 batch-6 Chinese podcast episodes (imported by refine_chinese_pilot_bodies)."""

from __future__ import annotations

from typing import Any

BATCH6_EPISODES: dict[str, dict[str, dict[str, Any]]] = {
    "zj-ep115": {
        "en": {
            "keywords": ["GOOGL", "Private:OpenAI", "Agent", "RL"],
            "conclusion": "Yao Shunyu's three-hour OpenAI agent retrospective frames the second half of AI as systems that act in environments — not bigger chat models. Six years of RL and tool-use research converge on super-app orchestration and bounded autonomy; most upside stays in private OpenAI while public investors tax the feast via Alphabet (GOOGL). Investors should Watch GOOGL on Gemini agent distribution and Private:OpenAI on product cadence as the benchmark for agent economics.",
            "background": "Zhang Xiaojun's Apr 19, 2025 interview with Yao Shunyu (OpenAI researcher at time of recording) walks six years of agent research — from academic RL to ChatGPT tools and computer-use agents. Yao argues the first half of AI was language and perception; the second half is humans plus systems: agents that plan, call APIs, and inhabit product surfaces. He discusses swallowing boundaries between apps (super-app thesis), unipolar model labs versus plural deployment, and why environment design matters more than raw parameter count. Episode is technical philosophy for investors sizing agent capex versus application revenue.",
            "important_facts": [
                "Six-year agent arc: Yao Shunyu traces agent work from RL foundations through tool use and multi-step planning — OpenAI's trajectory mirrors research-first productization. Second-half AI means systems that change state in the world, not autocomplete; super-app metaphors describe one orchestrator calling many services.",
                "Humans and systems: Yao stresses co-design of human intent and system affordances — agents fail when environments are ambiguous. Unipolar labs (OpenAI) versus plural ecosystems (many agents on GOOGL/Android) shapes who captures margin; most agent upside remains private-market asymmetric.",
                "Investable frame: Alphabet (GOOGL) Watch — Gemini plus Android distribution is public agent landlord; Private:OpenAI Watch — operator and research cadence set consumer willingness-to-pay for action. Underweight pure chat wrappers without environment or payment loop.",
            ],
            "mental_model": {
                "name": "Second-Half AI × Environment Design × Super-App Orchestration",
                "components": "First half: language and perception. Second half: agents acting in environments. Super-app wins by orchestration, not one omniscient model. Private labs own research optionality; hyperscalers own distribution rent.",
                "application": "Alphabet (GOOGL): Watch agent features in Search, Workspace, and Android — landlord thesis if action-layer monetizes. Private:OpenAI: Watch product releases as private asymmetry benchmark; public investors rarely get same entry.",
            },
            "key_insights": [
                {
                    "view": "Second half of AI is action in environments.",
                    "question": "What shifts after the chat era?",
                    "answer": "Yao Shunyu says scaling language solved information; the next wave is agents that plan, use tools, and persist state — RL and environment design dominate. Investors should track willingness-to-pay for completed tasks, not token volume alone.",
                },
                {
                    "view": "Super-app swallows single-purpose apps.",
                    "question": "How do agents reshape distribution?",
                    "answer": "One orchestrator calling travel, commerce, and productivity APIs compresses app silos — similar to WeChat super-app logic applied globally. Winners own the orchestration layer or become paid tools behind it; losers are thin UI wrappers.",
                },
                {
                    "view": "Unipolar research, plural deployment.",
                    "question": "Why pair OpenAI private with GOOGL public?",
                    "answer": "OpenAI concentrates frontier agent research; GOOGL and others deploy across billions of devices. Public markets access distribution landlords and miss most private AGI optionality — Yao's arc explains why agent narratives split feast (infra) from bubble (wrappers).",
                },
            ],
            "top_investment_implications": [
                {
                    "ticker": "GOOGL",
                    "direction": "Watch",
                    "confidence": "Medium",
                    "thesis": "Alphabet (GOOGL): Yao Shunyu agent second-half frame — Watch Gemini agent distribution and Android orchestration as public landlord play",
                },
                {
                    "ticker": "Private:OpenAI",
                    "direction": "Watch",
                    "confidence": "Medium",
                    "thesis": "Private:OpenAI: Six-year agent research benchmark — Watch operator and tool-use cadence as private asymmetry public markets cannot replicate",
                },
            ],
            "golden_quotes": [
                "The second half of AI is not about bigger language models — it is about systems that act in environments.",
                "A super-app does not need one god model; it needs an orchestrator that swallows boundaries between services.",
                "Six years of agent research taught me environment design beats parameter count for real utility.",
            ],
            "chronology": {
                "subject": "Yao Shunyu · OpenAI Agent Research",
                "events": [
                    {"date": "2019–2023", "event": "Yao Shunyu agent and RL research arc"},
                    {"date": "2023–2024", "event": "ChatGPT tools and multi-step agent prototypes"},
                    {"date": "2025", "event": "Super-app and second-half AI thesis matures"},
                    {"date": "2025-04-19", "event": "Three-hour Zhang Xiaojun interview recorded"},
                    {"date": "2025–2026", "event": "Computer-use and operator agents ship"},
                    {"date": "2026+", "event": "Agent economics test willingness-to-pay"},
                ],
            },
        },
        "zh": {
            "keywords": ["GOOGL", "Private:OpenAI", "Agent", "RL"],
            "conclusion": "姚顺雨三小时 OpenAI Agent 回顾将 AI 下半场框为在环境中行动的系统——非更大聊天模型。六年 RL 与工具调用研究汇聚于超级应用编排与有界自主；多数上行留于私募 OpenAI，公开投资者经 Alphabet（GOOGL）向盛宴收税。投资者应观望 GOOGL 的 Gemini Agent 分发与 Private:OpenAI 的产品节奏作 Agent 经济学基准。",
            "background": "张小珺 2025 年 4 月 19 日访谈姚顺雨（录制时为 OpenAI 研究员）梳理六年 Agent 研究——从学术 RL 到 ChatGPT 工具与电脑操作 Agent。姚顺雨称 AI 上半场是语言与感知；下半场是人与系统：规划、调 API、栖居产品面的 Agent。他讨论吞噬应用边界的超级应用论、单极模型实验室对多元部署，以及环境设计重于参数量。节目为投资者衡量 Agent 资本开支对应用收入的技术哲学。",
            "important_facts": [
                "六年 Agent 弧：姚顺雨从 RL 基础经工具调用与多步规划追溯——OpenAI 轨迹镜像研究优先产品化。下半场 AI 指改变世界状态的系统非自动补全；超级应用隐喻是一个编排器调用多服务。",
                "人与系统：姚顺雨强调人类意图与系统 affordance 协同设计——环境模糊则 Agent 失败。单极实验室（OpenAI）对多元生态（GOOGL/Android 上多 Agent）决定谁捕获毛利；多数 Agent 上行仍是私募非对称。",
                "可投资框架：Alphabet（GOOGL）观望——Gemini 加 Android 分发是公开 Agent 房东；Private:OpenAI 观望——Operator 与研究节奏定消费端为行动付费意愿。无环境或付费环的纯聊天套壳低配。",
            ],
            "mental_model": {
                "name": "AI 下半场 × 环境设计 × 超级应用编排",
                "components": "上半场：语言与感知。下半场：环境中行动的 Agent。超级应用靠编排胜非全知单模型。私募实验室握研究期权；hyperscaler 握分发租金。",
                "application": "Alphabet（GOOGL）：观望搜索、Workspace、Android 的 Agent 功能——行动层变现则房东论点成立。Private:OpenAI：观望产品发布作私募非对称基准；公开投资者难获同等入场。",
            },
            "key_insights": [
                {
                    "view": "AI 下半场是环境中行动。",
                    "question": "聊天时代后何变？",
                    "answer": "姚顺雨称扩展语言解决信息；下一波是规划、用工具、持久状态的 Agent——RL 与环境设计主导。投资者应跟完成任务付费意愿非仅 token 量。",
                },
                {
                    "view": "超级应用吞噬单用途 App。",
                    "question": "Agent 如何重塑分发？",
                    "answer": "一个编排器调旅行、电商、生产力 API 压缩应用孤岛——类微信超级应用逻辑全球化。赢家握编排层或成其后的付费工具；输家是薄 UI 套壳。",
                },
                {
                    "view": "单极研究、多元部署。",
                    "question": "为何并列 OpenAI 私募与 GOOGL 公开？",
                    "answer": "OpenAI 集中前沿 Agent 研究；GOOGL 等经数十亿设备部署。公开市场得分发房东、失多数私募 AGI 期权——姚顺雨弧解释 Agent 叙事如何分裂盛宴（infra）与泡沫（套壳）。",
                },
            ],
            "top_investment_implications": [
                {
                    "ticker": "GOOGL",
                    "direction": "Watch",
                    "confidence": "Medium",
                    "thesis": "Alphabet（GOOGL）：姚顺雨 Agent 下半场框架——观望 Gemini Agent 分发与 Android 编排作公开房东玩法",
                },
                {
                    "ticker": "Private:OpenAI",
                    "direction": "Watch",
                    "confidence": "Medium",
                    "thesis": "Private:OpenAI：六年 Agent 研究基准——观望 Operator 与工具调用节奏作公开市场无法复制的私募非对称",
                },
            ],
            "golden_quotes": ["占位一", "占位二", "占位三"],
            "chronology": {
                "subject": "姚顺雨 · OpenAI Agent 研究",
                "events": [
                    {"date": "2019–2023", "event": "姚顺雨 Agent 与 RL 研究弧"},
                    {"date": "2023–2024", "event": "ChatGPT 工具与多步 Agent 原型"},
                    {"date": "2025", "event": "超级应用与 AI 下半场论点成熟"},
                    {"date": "2025-04-19", "event": "张小珺三小时访谈录制"},
                    {"date": "2025–2026", "event": "电脑操作与 Operator Agent 交付"},
                    {"date": "2026+", "event": "Agent 经济学考验付费意愿"},
                ],
            },
        },
    },
    "zj-ep70": {
        "en": {
            "keywords": ["XPEV", "TSLA", "NVDA", "FSD"],
            "conclusion": "He Xiaopeng frames China's EV war as swimming in a sea of blood — FSD is survival, not feature marketing. XPeng bets end-to-end autonomy and NVIDIA compute while benchmarking Tesla (TSLA); heroes versus cowards separate in chaos. Investors should Watch XPeng (XPEV) on FSD rollout miles and margin through price war, and NVDA on China AD chip demand as OEMs race autonomy.",
            "background": "Zhang Xiaojun's Jul 15, 2024 interview with He Xiaopeng (XPeng chairman and CEO) covers FSD strategy, industry blood-bath competition, and leadership under chaos. He argues intelligent driving is the next moat after electrification — without it OEMs become commodity assemblers. He cites swimming in blood sea: hundreds of brands collapsing to few survivors; cowards exit, heroes invest through downturn. Tesla remains benchmark; XPeng pursues city NOA and end-to-end stacks with heavy NVIDIA training spend.",
            "important_facts": [
                "Blood sea thesis: He Xiaopeng says China EV entered kill phase — price war plus tech race; FSD separates survivors from OEMs who only assemble batteries. XPeng (XPEV) must prove autonomy miles and software revenue path while gross margin compresses.",
                "FSD as moat: Without full-scene assisted driving, brands lack differentiation — He benchmarks Tesla (TSLA) FSD data flywheel. XPeng invests end-to-end perception-planning; NVIDIA (NVDA) GPUs train models — compute intensity rises as competition intensifies.",
                "Heroes and cowards: In chaos, cutting R&D is cowardice; He vows XPeng continues autonomy spend even when market panics. Investors Watch XPEV delivery cadence plus FSD subscription attach; underweight if autonomy lags while burning cash in price war.",
            ],
            "mental_model": {
                "name": "Blood Sea Survival × FSD Moat × Tesla Benchmark",
                "components": "EV commoditization pushes margin to software and autonomy. Blood sea kills weak brands; FSD is differentiation or death. NVIDIA trains; Tesla sets miles bar.",
                "application": "XPeng (XPEV): Watch city NOA coverage and FSD monetization — Long only if autonomy narrows Tesla gap while deliveries hold. NVIDIA (NVDA): Watch China AD training demand as blood sea forces compute spend.",
            },
            "key_insights": [
                {
                    "view": "Swimming in blood sea is the new normal.",
                    "question": "Why does He use such harsh framing?",
                    "answer": "Hundreds of EV startups and legacy OEMs fight for share with collapsing ASP — He says only tech and brand survivors remain. Investors must price XPEV for years of margin pain, not quarterly delivery beats alone.",
                },
                {
                    "view": "FSD is moat, not optional feature.",
                    "question": "What happens without autonomy leadership?",
                    "answer": "He Xiaopeng argues assembly-only OEMs become Foxconn for cars — Tesla and leaders with data flywheels win. XPeng's bet is end-to-end stack plus China localization; failure mode is lagging TSLA while burning on discounts.",
                },
                {
                    "view": "Chaos separates heroes from cowards.",
                    "question": "How should management act in downturn?",
                    "answer": "He refuses to cut autonomy R&D when peers retreat — heroes invest through blood sea. Cowards preserve short-term margin and lose next war; XPEV thesis requires believing He's execution on FSD despite volatility.",
                },
            ],
            "top_investment_implications": [
                {
                    "ticker": "XPEV",
                    "direction": "Watch",
                    "confidence": "Medium",
                    "thesis": "XPeng (XPEV): He Xiaopeng blood-sea and FSD moat — Watch autonomy rollout and margin through EV price war",
                },
                {
                    "ticker": "TSLA",
                    "direction": "Watch",
                    "confidence": "Medium",
                    "thesis": "Tesla (TSLA): He Xiaopeng benchmark — Watch FSD miles and data flywheel as ceiling Chinese OEMs chase",
                },
                {
                    "ticker": "NVDA",
                    "direction": "Watch",
                    "confidence": "Medium",
                    "thesis": "NVIDIA (NVDA): China AD blood sea — Watch training GPU demand as OEMs race end-to-end FSD",
                },
            ],
            "golden_quotes": [
                "We are swimming in a sea of blood — only intelligence and courage survive.",
                "FSD is not a feature slide; it is whether you become a car company or a contract manufacturer.",
                "In chaos, cutting autonomous driving R&D is what cowards do.",
            ],
            "chronology": {
                "subject": "He Xiaopeng · XPeng FSD",
                "events": [
                    {"date": "2023–2024", "event": "China EV price war intensifies"},
                    {"date": "2024", "event": "XPeng city NOA and end-to-end push"},
                    {"date": "2024", "event": "He frames industry as blood sea"},
                    {"date": "2024-07-15", "event": "Zhang Xiaojun interview recorded"},
                    {"date": "2024–2025", "event": "FSD miles race versus Tesla benchmark"},
                    {"date": "2026+", "event": "Survivor consolidation in China EV"},
                ],
            },
        },
        "zh": {
            "keywords": ["XPEV", "TSLA", "NVDA", "FSD"],
            "conclusion": "何小鹏将中国 EV 战框为在血海中游泳——FSD 是生存非功能营销。小鹏押注端到端智驾与英伟达算力并以特斯拉（TSLA）为标杆；乱世中英雄与狗熊分流。投资者应观望小鹏（XPEV）FSD 里程落地与价格战中的毛利，以及 NVDA 在中国智驾算力需求随 OEM 竞速。",
            "background": "张小珺 2024 年 7 月 15 日访谈何小鹏（小鹏董事长兼 CEO）涵盖 FSD 战略、行业血战竞争与乱世领导力。何称智驾是电动化后的下一护城河——无则 OEM 沦为代工组装。他引血海游泳：数百品牌坍缩至少数幸存者；狗熊退出、英雄在低谷投资。特斯拉仍是基准；小鹏以重英伟达训练投入追城市 NOA 与端到端栈。",
            "important_facts": [
                "血海论点：何小鹏称中国 EV 进入淘汰赛——价格战加技术赛；FSD 区分幸存者与只组装电池的 OEM。小鹏（XPEV）须证智驾里程与软件收入路径，同时毛利压缩。",
                "FSD 即护城河：无全场景辅助驾驶则品牌无差异化——何以特斯拉（TSLA）FSD 数据飞轮为标杆。小鹏投端到端感知规划；英伟达（NVDA）GPU 训模型——竞争加剧则算力强度升。",
                "英雄与狗熊：乱世砍研发是狗熊；何誓小鹏继续智驾投入即使市场恐慌。投资者观望 XPEV 交付节奏加 FSD 订阅 attach；智驾落后且价格战烧钱则低配。",
            ],
            "mental_model": {
                "name": "血海生存 × FSD 护城河 × 特斯拉基准",
                "components": "EV 商品化把毛利推向软件与智驾。血海淘汰弱品牌；FSD 是差异化或死亡。英伟达训练；特斯拉定里程标杆。",
                "application": "小鹏（XPEV）：观望城市 NOA 覆盖与 FSD 变现——仅当智驾缩小特斯拉差距且交付稳住时看多。英伟达（NVDA）：观望中国智驾训练需求随血海迫算力开支。",
            },
            "key_insights": [
                {
                    "view": "血海游泳是新常态。",
                    "question": "何小鹏为何用如此狠框架？",
                    "answer": "数百 EV 创业与 legacy OEM 抢份额、ASP 坍缩——何称仅技术与品牌幸存者留。投资者须按数年毛利痛苦给 XPEV 定价，非仅季度交付超预期。",
                },
                {
                    "view": "FSD 是护城河非可选功能。",
                    "question": "无智驾领先会怎样？",
                    "answer": "何小鹏称仅组装 OEM 成汽车富士康——特斯拉与有数据飞轮者胜。小鹏赌注端到端栈加中国本地化；失败模式是追 TSLA 落后且折扣烧钱。",
                },
                {
                    "view": "乱世分英雄与狗熊。",
                    "question": "下行期管理层该如何？",
                    "answer": "何拒绝同行撤退时砍智驾研发——英雄在血海投资。狗熊保短期毛利失下一场战争；XPEV 论点须信何小鹏在波动中执行 FSD。",
                },
            ],
            "top_investment_implications": [
                {
                    "ticker": "XPEV",
                    "direction": "Watch",
                    "confidence": "Medium",
                    "thesis": "小鹏（XPEV）：何小鹏血海与 FSD 护城河——观望智驾落地与 EV 价格战毛利",
                },
                {
                    "ticker": "TSLA",
                    "direction": "Watch",
                    "confidence": "Medium",
                    "thesis": "特斯拉（TSLA）：何小鹏标杆——观望 FSD 里程与数据飞轮作中国 OEM 追赶天花板",
                },
                {
                    "ticker": "NVDA",
                    "direction": "Watch",
                    "confidence": "Medium",
                    "thesis": "英伟达（NVDA）：中国智驾血海——观望端到端 FSD 竞速带来的训练 GPU 需求",
                },
            ],
            "golden_quotes": ["占位一", "占位二", "占位三"],
            "chronology": {
                "subject": "何小鹏 · 小鹏 FSD",
                "events": [
                    {"date": "2023–2024", "event": "中国 EV 价格战加剧"},
                    {"date": "2024", "event": "小鹏城市 NOA 与端到端推进"},
                    {"date": "2024", "event": "何框定行业为血海"},
                    {"date": "2024-07-15", "event": "张小珺访谈录制"},
                    {"date": "2024–2025", "event": "FSD 里程赛对特斯拉基准"},
                    {"date": "2026+", "event": "中国 EV 幸存者整合"},
                ],
            },
        },
    },
    "zj-ep87": {
        "en": {
            "keywords": ["LI", "AI", "MEGA", "Agent OS"],
            "conclusion": "Li Xiang's podcast cut (Jan 2025) reveals the otaku-founder lens on AI, MEGA's painful lesson, family as entropy reduction, and games as training for product ladders. Li Auto bets Agent OS and domain models over universal agents; MEGA BEV stumble tests second-act execution. Investors should Watch Li Auto (LI) on AI productization and BEV recovery after MEGA reset — founder clarity remains moat until price war erodes margin.",
            "background": "Zhang Xiaojun's three-hour podcast edition with Li Xiang (Jan 2, 2025) differs from the video AI Talk — more personal: otaku youth, game ladder metaphors, family philosophy, and candid MEGA postmortem. Li links gaming rank grind to product iteration discipline and argues AI must become production tools users pay for. MEGA launch taught hubris on timing and positioning; Li doubles down on focused SKUs plus software. Episode humanizes the LI thesis: execution premium with visible failure modes.",
            "important_facts": [
                "Otaku to CEO ladder: Li Xiang maps game ranking systems to product tiers — patience and feedback loops from gaming inform Li Auto SKU strategy. AI section previews Agent OS thesis: orchestration over god-model; cars need domain VLA not generic chat.",
                "MEGA lesson: Pure-electric flagship miss on positioning and timing — Li admits overreach; investors should Watch LI BEV pipeline recovery without assuming every SKU hits. Failure sharpens capital discipline Li credits for L-series success.",
                "Family and AI philosophy: Li frames family as entropy reduction for founders — long horizon decisions versus quarterly panic. Li Auto (LI) Watch ties to whether AI spend converts to paid production tools and AD transparency, not demo copilots alone.",
            ],
            "mental_model": {
                "name": "Game Ladder Discipline × MEGA Reset × Production-Tool AI",
                "components": "Founder psychology shapes product cadence. Painful SKU miss is data, not doom, if learning compounds. AI wins on paid action, not chat novelty.",
                "application": "Li Auto (LI): Watch post-MEGA BEV orders and Agent OS monetization signals — Long requires second-hit product plus software attach. Trim if AI spend lacks revenue path while ASP collapses.",
            },
            "key_insights": [
                {
                    "view": "Games train product ladder thinking.",
                    "question": "Why does Li lean on gaming metaphors?",
                    "answer": "Ranked progression teaches iteration under feedback — Li applies to vehicle tiers and AI roadmap. Investors reading LI should track SKU hit rate and learning speed after MEGA, not founder charisma alone.",
                },
                {
                    "view": "MEGA was necessary failure.",
                    "question": "How should markets price the MEGA miss?",
                    "answer": "Li Xiang treats MEGA as timing and positioning error, not strategic retreat from BEV — Watch whether next BEV SKUs show repositioning. Coward would abandon electric; hero adjusts ladder.",
                },
                {
                    "view": "AI must be production tool.",
                    "question": "What AI thesis repeats from full AI Talk?",
                    "answer": "Information and assistive AI do not cut work hours — production tools with payment prove value. LI investment case needs software revenue mix, aligning with Li's Agent OS and VLA bets.",
                },
            ],
            "top_investment_implications": [
                {
                    "ticker": "LI",
                    "direction": "Watch",
                    "confidence": "Medium",
                    "thesis": "Li Auto (LI): Li Xiang podcast cut — Watch MEGA reset, BEV second act, and Agent OS monetization as execution proof",
                },
            ],
            "golden_quotes": [
                "Product iteration is like climbing a game ladder — you cannot skip ranks without paying tuition.",
                "MEGA taught us humility on timing; the BEV war is still the second war we must win.",
                "AI becomes real when users pay for completed work, not when demos go viral.",
            ],
            "chronology": {
                "subject": "Li Xiang · Podcast Cut",
                "events": [
                    {"date": "2024", "event": "MEGA launch and market reception debate"},
                    {"date": "2025-01", "event": "Post-DeepSeek AI strategy acceleration"},
                    {"date": "2025-01-02", "event": "Three-hour podcast cut published"},
                    {"date": "2025", "event": "Agent OS and VLA roadmap refinement"},
                    {"date": "2025–2026", "event": "BEV SKU repositioning after MEGA"},
                    {"date": "2026+", "event": "Production-tool AI monetization tests"},
                ],
            },
        },
        "zh": {
            "keywords": ["LI", "AI", "MEGA", "Agent OS"],
            "conclusion": "李想播客版（2025 年 1 月）呈现宅男创始人视角：AI、MEGA 惨痛课、家庭作减熵、游戏作产品天梯训练。理想押 Agent OS 与领域模型胜通用 Agent；MEGA 纯电挫折考验第二幕执行。投资者应观望理想（LI）AI 产品化与 MEGA 调整后的纯电复苏——创始人清晰仍是护城河直至价格战侵蚀毛利。",
            "background": "张小珺与李想三小时播客版（2025 年 1 月 2 日）异于视频 AI Talk——更个人：宅男青春、游戏天梯隐喻、家庭哲学与坦诚 MEGA 复盘。李想把游戏排位磨练与产品迭代纪律相连，称 AI 须成用户愿付费的生产工具。MEGA 发布教训是时机与定位傲慢；李想加码聚焦 SKU 加软件。节目人性化 LI 论点：有可见失败模式的执行溢价。",
            "important_facts": [
                "宅男到 CEO 天梯：李想将游戏段位映射产品梯队——游戏耐心与反馈环滋养理想 SKU 战略。AI 部分预告 Agent OS：编排胜上帝模型；车需领域 VLA 非通用聊天。",
                "MEGA 课：纯电旗舰在定位与时机失手——李想承认过度；投资者应观望 LI 纯电管线复苏勿假设每款 SKU 命中。失败若转化为学习则 sharpen 李想归功于 L 系列的资本纪律。",
                "家庭与 AI 哲学：李想框家庭为创始人减熵——长周期决策对季度恐慌。理想（LI）观望系 AI 投入能否转为付费生产工具与智驾透明，非仅 demo Copilot。",
            ],
            "mental_model": {
                "name": "游戏天梯纪律 × MEGA 重置 × 生产工具 AI",
                "components": "创始人心理塑造产品节奏。痛苦 SKU 失误是数据非末日，若学习复利。AI 赢在付费行动非聊天新奇。",
                "application": "理想（LI）：观望 MEGA 后纯电订单与 Agent OS 变现信号——看多需第二款爆款加软件 attach。AI 投入无收入路径且 ASP 崩则减仓。",
            },
            "key_insights": [
                {
                    "view": "游戏训练产品天梯思维。",
                    "question": "李想为何倚重游戏隐喻？",
                    "answer": "排位进步教反馈下迭代——李想用于车型梯队与 AI 路线图。读 LI 应跟 SKU 命中率与 MEGA 后学习速度，非仅创始人魅力。",
                },
                {
                    "view": "MEGA 是必要失败。",
                    "question": "市场如何给 MEGA 失手定价？",
                    "answer": "李想视 MEGA 为时机定位错误非战略放弃纯电——观望下一款纯电 SKU 是否显示 reposition。狗熊会弃电；英雄调天梯。",
                },
                {
                    "view": "AI 须是生产工具。",
                    "question": "相对完整 AI Talk 重复何 AI 论点？",
                    "answer": "信息与辅助 AI 不减工作时长——有付费的生产工具证价值。LI 投资案需软件收入 mix，对齐李想 Agent OS 与 VLA 赌注。",
                },
            ],
            "top_investment_implications": [
                {
                    "ticker": "LI",
                    "direction": "Watch",
                    "confidence": "Medium",
                    "thesis": "理想（LI）：李想播客版——观望 MEGA 调整、纯电第二幕与 Agent OS 变现作执行验证",
                },
            ],
            "golden_quotes": ["占位一", "占位二", "占位三"],
            "chronology": {
                "subject": "李想 · 播客版",
                "events": [
                    {"date": "2024", "event": "MEGA 发布与市场反响争论"},
                    {"date": "2025-01", "event": "DeepSeek 后 AI 战略加速"},
                    {"date": "2025-01-02", "event": "三小时播客版发布"},
                    {"date": "2025", "event": "Agent OS 与 VLA 路线图精炼"},
                    {"date": "2025–2026", "event": "MEGA 后纯电 SKU 重新定位"},
                    {"date": "2026+", "event": "生产工具 AI 变现考验"},
                ],
            },
        },
    },
    "zj-ep79": {
        "en": {
            "keywords": ["TSLA", "UBER", "Robotaxi", "FSD"],
            "conclusion": "Meng Xing's Robotaxi event debrief explains why Tesla (TSLA) fell while Uber (UBER) rose — markets priced execution risk on autonomy while rewarding near-term mobility network optionality. Cybercab timeline, regulatory gaps, and fleet economics dominate; Uber benefits as partner narrative without capex burden. Investors should Watch TSLA on FSD miles and Robotaxi regulatory path, and UBER on autonomous partnership revenue mix.",
            "background": "Zhang Xiaojun and Meng Xing (autonomous driving founder, podcast host) dissect Tesla's Oct 2024 Robotaxi event (Oct 13, 2024 episode). Meng contrasts market reaction: TSLA sold on vague timelines and missing details; UBER rallied on partnership subtext and asset-light exposure to autonomy upside. Episode covers Cybercab design, unsupervised FSD claims, charging infrastructure, and why network operators may capture value before OEMs prove robot fleets.",
            "important_facts": [
                "Market split: Meng Xing notes TSLA drop reflected disappointment on concrete Robotaxi deployment — dates, geography, and unit economics thin. UBER rise framed as autonomy optionality without owning fleet capex — partnership lens wins when Tesla proof lags.",
                "Robotaxi economics: Unsupervised FSD is necessary but insufficient — fleet utilization, regulation, and remote assist costs determine ROI. Tesla (TSLA) must show miles between intervention trending down; Uber (UBER) benefits if multiple OEMs compete for network access.",
                "Investable Watch: TSLA — regulatory approvals and FSD subscription or per-mile monetization; UBER — autonomous trip mix and take-rate on partner fleets. Underweight TSLA Robotaxi premium without intervention metrics; overweight UBER only if partnership revenue materializes.",
            ],
            "mental_model": {
                "name": "Execution Gap × Network Optionality × Fleet Capex",
                "components": "Autonomy hype prices before deployment proof. Asset-light networks tax robot fleets via partnerships. Regulatory and utilization gates dominate OEM valuation swings.",
                "application": "Tesla (TSLA): Watch FSD intervention trends and Robotaxi city permits — Long autonomy thesis needs miles proof. Uber (UBER): Watch AV partnership revenue — network landlord if OEMs commoditize hardware.",
            },
            "key_insights": [
                {
                    "view": "Tesla sold the dream too thin.",
                    "question": "Why did TSLA fall post-event?",
                    "answer": "Meng Xing says investors wanted deployment specifics — cities, fleet size, unsupervised metrics — and got concept cars. Gap between keynote and SOP timeline widened risk premium.",
                },
                {
                    "view": "Uber owns network, not robot risk.",
                    "question": "Why did UBER rise?",
                    "answer": "Markets treat Uber as mobility OS that can integrate any AV supplier — autonomy success lifts take rate without Cybercab capex. Partnership narrative beats owning unproven fleet.",
                },
                {
                    "view": "Robotaxi is regulation plus utilization.",
                    "question": "What blocks TSLA re-rating?",
                    "answer": "Unsupervised FSD must clear regulators and achieve taxi-grade utilization — charging, maintenance, and edge cases. Meng warns event marketing runs ahead of intervention statistics investors should track.",
                },
            ],
            "top_investment_implications": [
                {
                    "ticker": "TSLA",
                    "direction": "Watch",
                    "confidence": "Medium",
                    "thesis": "Tesla (TSLA): Meng Xing Robotaxi debrief — Watch FSD intervention metrics and regulatory path versus event hype",
                },
                {
                    "ticker": "UBER",
                    "direction": "Watch",
                    "confidence": "Medium",
                    "thesis": "Uber (UBER): Robotaxi event read-through — Watch autonomous partnership revenue as asset-light autonomy optionality",
                },
            ],
            "golden_quotes": [
                "Tesla sold the Robotaxi dream; the market wanted deployment spreadsheets.",
                "Uber rises when autonomy is optionality on the network, not capex on the balance sheet.",
                "Unsupervised FSD is the ticket — utilization and regulation are the show.",
            ],
            "chronology": {
                "subject": "Meng Xing · Robotaxi Debrief",
                "events": [
                    {"date": "2024-10", "event": "Tesla Robotaxi / Cybercab event"},
                    {"date": "2024-10", "event": "TSLA falls, UBER rises on market read"},
                    {"date": "2024-10-13", "event": "Zhang Xiaojun debrief with Meng Xing"},
                    {"date": "2024–2025", "event": "FSD v12/v13 miles and intervention tracking"},
                    {"date": "2025+", "event": "City-level Robotaxi permit race"},
                    {"date": "2026+", "event": "Network-OEM partnership economics clarify"},
                ],
            },
        },
        "zh": {
            "keywords": ["TSLA", "UBER", "Robotaxi", "FSD"],
            "conclusion": "孟醒 Robotaxi 大会复盘解释为何特斯拉（TSLA）跌而 Uber（UBER）涨——市场给自主执行风险定价，同时奖励近端出行网络期权。Cybercab 时间表、监管缺口与车队经济学主导；Uber 以合作叙事受益而无重资产负担。投资者应观望 TSLA 的 FSD 里程与 Robotaxi 监管路径，以及 UBER 的自动驾驶合作收入 mix。",
            "background": "张小珺与孟醒（自动驾驶创业者、播客主播）拆解特斯拉 2024 年 10 月 Robotaxi 大会（2024 年 10 月 13 日节目）。孟醒对比市场反应：TSLA 因时间表模糊与细节缺失遭抛售；UBER 因合作潜台词与轻资产享自主上行而上涨。节目涵盖 Cybercab 设计、无人 FSD 宣称、充电基建，以及网络运营方何以在 OEM 证机器人车队前捕获价值。",
            "important_facts": [
                "市场分裂：孟醒指 TSLA 下跌反映对具体 Robotaxi 部署失望——日期、地域、单位经济学稀薄。UBER 上涨框为无车队 capex 的自主期权——特斯拉验证滞后时合作透镜胜。",
                "Robotaxi 经济学：无人 FSD 必要不充分——车队利用率、监管与远程协助成本定 ROI。特斯拉（TSLA）须示干预间隔里程下行；Uber（UBER）若多 OEM 争网络接入则受益。",
                "可投资观望：TSLA——监管批准与 FSD 订阅或按里程变现；UBER——自动行程 mix 与合作伙伴车队抽佣。无干预指标勿超重 TSLA Robotaxi 溢价；仅合作收入落地才超配 UBER。",
            ],
            "mental_model": {
                "name": "执行缺口 × 网络期权 × 车队 Capex",
                "components": "自主 hype 先于部署验证定价。轻资产网络经合作向机器人车队收税。监管与利用率门控 OEM 估值波动。",
                "application": "特斯拉（TSLA）：观望 FSD 干预趋势与 Robotaxi 城市许可——看多自主须里程验证。Uber（UBER）：观望 AV 合作收入——OEM 硬件商品化则网络房东胜。",
            },
            "key_insights": [
                {
                    "view": "特斯拉梦卖得太薄。",
                    "question": "会后 TSLA 为何跌？",
                    "answer": "孟醒称投资者要部署细节——城市、车队规模、无人指标——只得概念车。 keynote 与 SOP 时间表缺口拉宽风险溢价。",
                },
                {
                    "view": "Uber 握网络非机器人风险。",
                    "question": "UBER 为何涨？",
                    "answer": "市场将 Uber 作可集成任一 AV 供应商的出行 OS——自主成功抬抽佣而无 Cybercab capex。合作叙事胜持有未证车队。",
                },
                {
                    "view": "Robotaxi 是监管加利用率。",
                    "question": "何阻 TSLA 重估？",
                    "answer": "无人 FSD 须过监管并达出租车级利用率——充电、维保与边缘案例。孟醒示警活动营销跑在投资者应跟的干预统计前。",
                },
            ],
            "top_investment_implications": [
                {
                    "ticker": "TSLA",
                    "direction": "Watch",
                    "confidence": "Medium",
                    "thesis": "特斯拉（TSLA）：孟醒 Robotaxi 复盘——观望 FSD 干预指标与监管路径对活动 hype",
                },
                {
                    "ticker": "UBER",
                    "direction": "Watch",
                    "confidence": "Medium",
                    "thesis": "Uber（UBER）：Robotaxi 大会读穿——观望自动驾驶合作收入作轻资产自主期权",
                },
            ],
            "golden_quotes": ["占位一", "占位二", "占位三"],
            "chronology": {
                "subject": "孟醒 · Robotaxi 复盘",
                "events": [
                    {"date": "2024-10", "event": "特斯拉 Robotaxi/Cybercab 大会"},
                    {"date": "2024-10", "event": "TSLA 跌、UBER 涨的市场解读"},
                    {"date": "2024-10-13", "event": "张小珺与孟醒复盘节目"},
                    {"date": "2024–2025", "event": "FSD v12/v13 里程与干预跟踪"},
                    {"date": "2025+", "event": "城市级 Robotaxi 许可竞赛"},
                    {"date": "2026+", "event": "网络-OEM 合作经济学明朗"},
                ],
            },
        },
    },
    "zj-ep72": {
        "en": {
            "keywords": ["TSLA", "FSD", "End-to-End", "Autonomous Driving"],
            "conclusion": "Meng Xing's Tesla FSD evolution history (Steam Engine to Self-Driving ep.3) traces rule-based stacks through neural networks to end-to-end vision — Tesla called each transition earliest. FSD v12's unified network replaced modular pipelines; data flywheel and custom silicon remain moat. Investors should Watch Tesla (TSLA) on intervention miles and FSD revenue recognition as the industry copies architecture without matching fleet scale.",
            "background": "Zhang Xiaojun's Aug 18, 2024 episode with Meng Xing continues the autonomy history series — focused on Tesla FSD lineage. Meng walks Occupancy Networks, BEV fusion, shadow mode, and the shift to end-to-end driving policies trained on fleet video. Tesla's willingness to delete hand-engineered modules when neural nets suffice is the recurring lesson; Chinese OEMs now mimic but lag on data volume and iteration speed.",
            "important_facts": [
                "Modular to end-to-end: Meng Xing explains Tesla retired perception-planning stacks for single-network FSD v12 — architecture simplification cuts error compounding. TSLA Watch on miles between critical interventions as proof, not release notes.",
                "Data flywheel mechanics: Fleet shadow mode and auto-labeling convert driving video to training data — competitors lack global miles at Tesla scale. Custom FSD chips follow algorithm hunger; NVDA trains cloud but Tesla optimizes inference.",
                "History lesson for investors: Each AV era (rules, CNN perception, BEV, end-to-end) Tesla moved first — Meng warns copying slides without data discipline fails. TSLA benchmark sets valuation ceiling for XPEV, LI, and AD suppliers.",
            ],
            "mental_model": {
                "name": "Architecture Simplification × Fleet Data × First-Mover Transitions",
                "components": "End-to-end removes stitch-point failures. Shadow mode turns miles into labels. First correct transition beats incremental patches on dead stacks.",
                "application": "Tesla (TSLA): Watch FSD v12+ intervention trends and subscription attach — autonomy optionality prices on data scale. Underweight OEMs claiming end-to-end without transparent miles.",
            },
            "key_insights": [
                {
                    "view": "FSD v12 deleted the pipeline.",
                    "question": "What changed in Tesla's latest stack?",
                    "answer": "Meng Xing says unified network replaces modular perception-planning handoffs — fewer stitch hallucinations. Industry copycats ship demos; Tesla ships fleet-wide OTA when metrics clear.",
                },
                {
                    "view": "Shadow mode is the secret factory.",
                    "question": "How does Tesla scale labels?",
                    "answer": "Fleet drives in shadow comparing human versus policy — disagreements become training signal. Data volume moat is harder to clone than open-source model weights.",
                },
                {
                    "view": "Steam engine to self-driving is transition discipline.",
                    "question": "Why a history series for investors?",
                    "answer": "Each paradigm shift kills sunk-cost incumbents — Meng's arc shows Tesla abandons modules when metrics win. Investors should fund data flywheels, not lidar-map nostalgia.",
                },
            ],
            "top_investment_implications": [
                {
                    "ticker": "TSLA",
                    "direction": "Watch",
                    "confidence": "Medium",
                    "thesis": "Tesla (TSLA): Meng Xing FSD evolution — Watch end-to-end intervention miles and FSD monetization as global AD benchmark",
                },
            ],
            "golden_quotes": [
                "FSD v12 did not patch the pipeline — it deleted the pipeline.",
                "Shadow mode turns every customer mile into a labeling factory.",
                "Tesla wins transitions by abandoning sunk modules when the network is ready.",
            ],
            "chronology": {
                "subject": "Meng Xing · Tesla FSD History",
                "events": [
                    {"date": "2016–2019", "event": "Tesla FSD chip and neural net perception era"},
                    {"date": "2020–2022", "event": "Occupancy Networks and BEV fusion adoption"},
                    {"date": "2023", "event": "FSD v12 end-to-end unified network rollout"},
                    {"date": "2024-08-18", "event": "Steam Engine to Self-Driving ep.3 recorded"},
                    {"date": "2024–2025", "event": "v12/v13 fleet OTA and intervention tracking"},
                    {"date": "2026+", "event": "Unsupervised FSD and Robotaxi economics"},
                ],
            },
        },
        "zh": {
            "keywords": ["TSLA", "FSD", "端到端", "自动驾驶"],
            "conclusion": "孟醒特斯拉 FSD 进化史（蒸汽机到无人驾驶第 3 集）梳理规则栈经神经网络到端到端视觉——特斯拉每次转型最早喊出。FSD v12 统一网络取代模块化管线；数据飞轮与自研硅仍是护城河。投资者应观望特斯拉（TSLA）干预里程与 FSD 收入确认，行业抄架构难匹车队规模。",
            "background": "张小珺 2024 年 8 月 18 日与孟醒续自动驾驶史系列——聚焦特斯拉 FSD 脉络。孟醒走过 Occupancy Network、BEV 融合、影子模式与向端端驾驶策略（车队视频训练）转变。特斯拉在神经网络足够时删除手工模块的意愿是反复出现的课；中国 OEM 现模仿但数据量与迭代速度落后。",
            "important_facts": [
                "模块化到端到端：孟醒解释特斯拉以单一网络 FSD v12 退役感知-规划栈——架构简化降错误复合。TSLA 观望关键干预间里程为证非 release note。",
                "数据飞轮机制：车队影子模式与自动标注将驾驶视频转训练数据——对手缺特斯拉规模全球里程。自研 FSD 芯片跟随算法饥渴；英伟达训云但特斯拉优化推理。",
                "投资者历史课：每代 AV（规则、CNN 感知、BEV、端到端）特斯拉最先动——孟醒示警抄幻灯片无数据纪律则败。TSLA 基准定 XPEV、LI 与智驾供应商估值天花板。",
            ],
            "mental_model": {
                "name": "架构简化 × 车队数据 × 转型先发",
                "components": "端到端去除拼接点失败。影子模式把里程变标签。最先正确转型胜死栈上 incremental 补丁。",
                "application": "特斯拉（TSLA）：观望 FSD v12+ 干预趋势与订阅 attach——自主期权按数据规模定价。宣称端到端却无透明里程的 OEM 低配。",
            },
            "key_insights": [
                {
                    "view": "FSD v12 删除管线。",
                    "question": "特斯拉最新栈何变？",
                    "answer": "孟醒称统一网络取代模块化感知-规划交接——少拼接幻觉。行业抄袭者交 demo；特斯拉指标清则车队 OTA。",
                },
                {
                    "view": "影子模式是秘密工厂。",
                    "question": "特斯拉如何规模化标注？",
                    "answer": "车队影子驾驶比较人与策略——分歧变训练信号。数据量护城河比开源权重难克隆。",
                },
                {
                    "view": "蒸汽机到自驾是转型纪律。",
                    "question": "为何给投资者讲历史系列？",
                    "answer": "每次范式转换杀死沉没成本 incumbent——孟醒弧显示特斯拉指标赢则弃模块。投资者应资助数据飞轮非激光雷达地图怀旧。",
                },
            ],
            "top_investment_implications": [
                {
                    "ticker": "TSLA",
                    "direction": "Watch",
                    "confidence": "Medium",
                    "thesis": "特斯拉（TSLA）：孟醒 FSD 进化——观望端到端干预里程与 FSD 变现作全球智驾基准",
                },
            ],
            "golden_quotes": ["占位一", "占位二", "占位三"],
            "chronology": {
                "subject": "孟醒 · 特斯拉 FSD 史",
                "events": [
                    {"date": "2016–2019", "event": "特斯拉 FSD 芯片与神经网络感知时代"},
                    {"date": "2020–2022", "event": "Occupancy Network 与 BEV 融合采纳"},
                    {"date": "2023", "event": "FSD v12 端到端统一网络 rollout"},
                    {"date": "2024-08-18", "event": "蒸汽机到无人驾驶第 3 集录制"},
                    {"date": "2024–2025", "event": "v12/v13 车队 OTA 与干预跟踪"},
                    {"date": "2026+", "event": "无人 FSD 与 Robotaxi 经济学"},
                ],
            },
        },
    },
    "zj-ep94": {
        "en": {
            "keywords": ["NVDA", "DeepSeek", "Kimi", "MiniMax"],
            "conclusion": "Guangmi's paper walkthrough of DeepSeek, Kimi, and MiniMax attention innovations frames Chinese labs as hardware brute-force aesthetes — MLA, sparse attention, and MoE routing squeeze more tokens per watt on NVIDIA (NVDA) clusters. Efficiency gains compress inference cost curves but raise GPU demand for training scale. Investors should Watch NVDA on China cluster buildout and lab efficiency races as open-weight models pressure hyperscaler margins.",
            "background": "Zhang Xiaojun's Mar 2, 2025 episode with Guangmi (AI researcher, LLM quarterly host) line-by-lines new attention papers from DeepSeek, Moonshot Kimi, and MiniMax. Theme: 'brute-force aesthetics on hardware' — algorithm co-designed for H100/H800 memory bandwidth and MFU. Guangmi explains Multi-head Latent Attention, lightning attention variants, and why Chinese labs publish engineering breakthroughs Western labs hide in infra.",
            "important_facts": [
                "Attention engineering wave: DeepSeek V3/R1 MLA reduces KV cache memory — more context per GPU; Kimi and MiniMax push sparse and linear attention hybrids. NVDA benefits from training scale even when inference per token falls — Jevons paradox on compute.",
                "Open-weight pressure: Chinese labs release papers and weights — commoditizes base model rent for GOOGL/META while spurring hardware demand. Guangmi says prettiest algorithms are cleanest — investors track MFU and $/token, not parameter bragging.",
                "Investable NVDA: China lab capex cycles tie to attention breakthroughs — clusters upgrade when new arch ships. Watch NVDA data center revenue from Chinese hyperscaler and startup training; risk is export controls cap H800 supply.",
            ],
            "mental_model": {
                "name": "Attention MFU × Open-Weight Commoditization × Jevons Compute",
                "components": "Efficiency lowers $/token but raises total tokens served. Chinese labs co-design for NVIDIA memory topology. Open weights compress model rent, expand hardware feast.",
                "application": "NVIDIA (NVDA): Watch China training cluster demand post-DeepSeek/Kimi papers — efficiency gains increase aggregate compute. Underweight if export policy permanently caps China MFU growth.",
            },
            "key_insights": [
                {
                    "view": "Brute-force aesthetics means hardware co-design.",
                    "question": "What is Guangmi's thesis on Chinese papers?",
                    "answer": "DeepSeek MLA and peers optimize for real cluster topology — memory bandwidth and MFU, not academic novelty alone. Investors should read papers as capex signals for GPU generations.",
                },
                {
                    "view": "Clean algorithms win economically.",
                    "question": "Why praise 'prettiest and cleanest' math?",
                    "answer": "Simpler attention variants deploy faster and debug easier — lowers engineering drag per flop. Labs that ship clean arch plus open weights force Western incumbents to match efficiency or burn margin.",
                },
                {
                    "view": "Efficiency can increase GPU demand.",
                    "question": "Does MLA hurt NVDA?",
                    "answer": "Guangmi implies Jevons effect — cheaper inference spawns more agents and longer context, training races continue. NVDA wins on aggregate tokens times training frontier, not per-token rent alone.",
                },
            ],
            "top_investment_implications": [
                {
                    "ticker": "NVDA",
                    "direction": "Watch",
                    "confidence": "Medium",
                    "thesis": "NVIDIA (NVDA): Guangmi DeepSeek/Kimi/MiniMax attention papers — Watch China cluster demand as efficiency races expand aggregate compute",
                },
            ],
            "golden_quotes": [
                "The prettiest attention algorithms are the cleanest — and the cleanest are built for real GPU memory.",
                "Chinese labs practice brute-force aesthetics: co-design math with H100 topology.",
                "Efficiency does not kill GPU demand — it feeds more tokens and more agents.",
            ],
            "chronology": {
                "subject": "Guangmi · Attention Papers",
                "events": [
                    {"date": "2024", "event": "DeepSeek V2/V3 MLA attention breakthroughs"},
                    {"date": "2025-01", "event": "Kimi K1.5 and reasoning model attention variants"},
                    {"date": "2025-02", "event": "MiniMax and peer sparse attention papers"},
                    {"date": "2025-03-02", "event": "Guangmi paper walkthrough recorded"},
                    {"date": "2025", "event": "China lab cluster upgrades on new arch"},
                    {"date": "2026+", "event": "Inference cost curves and agent token demand"},
                ],
            },
        },
        "zh": {
            "keywords": ["NVDA", "DeepSeek", "Kimi", "MiniMax"],
            "conclusion": "广密逐篇讲解 DeepSeek、Kimi、MiniMax 注意力创新，将中国实验室框为硬件上的暴力美学——MLA、稀疏注意力与 MoE 路由在英伟达（NVDA）集群上榨更多 token/瓦。效率增益压缩推理成本曲线但抬高训练规模 GPU 需求。投资者应观望 NVDA 的中国集群建设与实验室效率赛，开源模型压 hyperscaler 毛利。",
            "background": "张小珺 2025 年 3 月 2 日与广密（AI 研究员、大模型季报主播）逐句精读 DeepSeek、月之暗面 Kimi、MiniMax 新注意力论文。主题「硬件上的暴力美学」——算法与 H100/H800 内存带宽及 MFU 协同设计。广密解释多头潜注意力、闪电注意力变体及中国实验室为何发表西方藏在 infra 里的工程突破。",
            "important_facts": [
                "注意力工程浪潮：DeepSeek V3/R1 MLA 降 KV cache 内存——每 GPU 更多上下文；Kimi 与 MiniMax 推稀疏与线性注意力混合。即使每 token 推理降，训练规模仍利 NVDA——算力杰文斯悖论。",
                "开源权重压力：中国实验室发论文与权重——商品化 GOOGL/META 基础模型租金同时刺激硬件需求。广密称最美算法最干净——投资者跟 MFU 与 $/token 非参数量吹嘘。",
                "可投资 NVDA：中国实验室 capex 周期绑注意力突破——新架构交付则集群升级。观望 NVDA 数据中心收入来自中国 hyperscaler 与创业训练；风险是出口管制 cap H800 供给。",
            ],
            "mental_model": {
                "name": "注意力 MFU × 开源商品化 × 杰文斯算力",
                "components": "效率降 $/token 但抬总服务 token。中国实验室为英伟达内存拓扑协同设计。开源权重压缩模型租金、扩大硬件盛宴。",
                "application": "英伟达（NVDA）：观望 DeepSeek/Kimi 论文后中国训练集群需求——效率增益增 aggregate compute。若出口政策永久 cap 中国 MFU 增长则低配。",
            },
            "key_insights": [
                {
                    "view": "暴力美学即硬件协同设计。",
                    "question": "广密对中国论文论点是什么？",
                    "answer": "DeepSeek MLA 等优化真实集群拓扑——内存带宽与 MFU 非仅学术新奇。投资者应将论文读作 GPU 代际 capex 信号。",
                },
                {
                    "view": "干净算法在经济上胜。",
                    "question": "为何赞「最优美最干净」？",
                    "answer": "更简单注意力变体部署快、易 debug——每 flop 工程阻力低。发干净架构加开源的实验室迫西方 incumbent 匹配效率或烧毛利。",
                },
                {
                    "view": "效率可增 GPU 需求。",
                    "question": "MLA 是否伤 NVDA？",
                    "answer": "广密暗示杰文斯效应——更廉推理催生更多 Agent 与更长上下文，训练赛继续。NVDA 赢在 aggregate token 乘训练前沿，非仅每 token 租金。",
                },
            ],
            "top_investment_implications": [
                {
                    "ticker": "NVDA",
                    "direction": "Watch",
                    "confidence": "Medium",
                    "thesis": "英伟达（NVDA）：广密 DeepSeek/Kimi/MiniMax 注意力论文——观望中国集群需求随效率赛扩大总算力",
                },
            ],
            "golden_quotes": ["占位一", "占位二", "占位三"],
            "chronology": {
                "subject": "广密 · 注意力论文",
                "events": [
                    {"date": "2024", "event": "DeepSeek V2/V3 MLA 注意力突破"},
                    {"date": "2025-01", "event": "Kimi K1.5 与推理模型注意力变体"},
                    {"date": "2025-02", "event": "MiniMax 等稀疏注意力论文"},
                    {"date": "2025-03-02", "event": "广密论文讲解录制"},
                    {"date": "2025", "event": "中国实验室新架构驱动集群升级"},
                    {"date": "2026+", "event": "推理成本曲线与 Agent token 需求"},
                ],
            },
        },
    },
    "zj-ep93": {
        "en": {
            "keywords": ["META", "TCEHY", "AGI", "Recommendation Engine"],
            "conclusion": "Zhang Qianchuan's AGI warning after leaving ByteDance and MiniMax frames recommendation engines as proto-AGI — optimizing human attention at scale with opaque objectives. He cautions alignment and product ethics as labs race capability; META and Tencent (TCEHY) own distribution rent while private labs chase AGI. Investors should Watch META and TCEHY on AI engagement monetization versus societal backlash risk, not every model benchmark alone.",
            "background": "Zhang Xiaojun's Feb 20, 2025 interview with Zhang Qianchuan (former ByteDance Toutiao product head, former MiniMax product head) is a product-leader AGI threat warning. Zhang argues feed algorithms already reshape cognition — scaling to AGI without guardrails risks concentration of power. He knows recommendation systems from Toutiao and model products from MiniMax; episode bridges China consumer internet and foundation-model labs.",
            "important_facts": [
                "Recommendation as proto-AGI: Zhang Qianchuan says optimizing engagement at billion-user scale is alignment problem in production — Toutiao/Douyin mechanics preview AGI deployment risks. META and TCEHY platforms already run large-scale preference optimizers.",
                "ByteDance and MiniMax lens: Leaving both, Zhang warns capability races outpace governance — product leaders must design constraints, not only loss curves. Private Chinese labs (MiniMax, DeepSeek) plus ByteDance/Tencent distribution create fast feedback loops investors should not ignore.",
                "Investable Watch: Meta (META) — ad ARPU from AI engagement versus regulatory and reputational tail risk. Tencent (TCEHY) — WeChat and video AI integration with China policy overlay. Underweight pure capability bets without distribution or safety narrative.",
            ],
            "mental_model": {
                "name": "Engagement Optimizer × Alignment Lag × Distribution Landlord",
                "components": "Feeds are AGI with wrong objective function. Capability labs outrun governance. Landlords monetize attention; labs burn capex.",
                "application": "Meta (META) and Tencent (TCEHY): Watch AI feature engagement lift versus policy backlash — landlords survive if ARPU rises without regulatory break. Private labs: Watch as capability benchmark, not public tickers.",
            },
            "key_insights": [
                {
                    "view": "Feeds already are misaligned AGI.",
                    "question": "Why does a product guy warn about AGI?",
                    "answer": "Zhang Qianchuan built systems that maximize dwell time — that is powerful optimization without explicit human values. Scaling LLM agents extends the same risk with more action surface.",
                },
                {
                    "view": "Capability races governance.",
                    "question": "What did MiniMax and ByteDance teach him?",
                    "answer": "Product shipping speed beats safety committees — Zhang left to voice concern that labs optimize benchmarks while society lacks brakes. Investors should price regulatory and reputational optionality on META/TCEHY AI rollouts.",
                },
                {
                    "view": "Distribution landlords tax the AGI feast.",
                    "question": "Where is investable exposure?",
                    "answer": "META and TCEHY own attention rails recommendation engines need — even if a private lab wins models, landlords capture ad and payment rent. Public investors size engagement monetization, not AGI theology.",
                },
            ],
            "top_investment_implications": [
                {
                    "ticker": "META",
                    "direction": "Watch",
                    "confidence": "Medium",
                    "thesis": "Meta (META): Zhang Qianchuan AGI warning — Watch AI engagement ARPU versus alignment and regulatory tail risk",
                },
                {
                    "ticker": "TCEHY",
                    "direction": "Watch",
                    "confidence": "Medium",
                    "thesis": "Tencent (TCEHY): Recommendation-scale AI on WeChat/video — Watch monetization versus China policy and AGI backlash risk",
                },
            ],
            "golden_quotes": [
                "Recommendation engines are already AGI with the wrong objective — maximize attention, not human flourishing.",
                "Capability labs outrun governance; product leaders must design brakes, not only benchmarks.",
                "Distribution landlords will tax the AGI feast whether or not your favorite lab wins.",
            ],
            "chronology": {
                "subject": "Zhang Qianchuan · AGI Warning",
                "events": [
                    {"date": "2010s", "event": "Zhang builds Toutiao recommendation product at ByteDance"},
                    {"date": "2023–2024", "event": "MiniMax product leadership; model race accelerates"},
                    {"date": "2025", "event": "Zhang leaves; speaks on AGI societal risk"},
                    {"date": "2025-02-20", "event": "Zhang Xiaojun interview recorded"},
                    {"date": "2025–2026", "event": "China and US AI policy debates intensify"},
                    {"date": "2026+", "event": "Engagement AI versus agent action regulation"},
                ],
            },
        },
        "zh": {
            "keywords": ["META", "TCEHY", "AGI", "推荐引擎"],
            "conclusion": "离开字节与 MiniMax 后张前川的 AGI 预警将推荐引擎框为原生 AGI——大规模优化人类注意力且目标不透明。他示警实验室竞速能力时对齐与产品伦理落后；META 与腾讯（TCEHY）握分发租金而私募实验室追 AGI。投资者应观望 META、TCEHY 的 AI 互动变现对社会反弹风险，非仅模型 benchmark。",
            "background": "张小珺 2025 年 2 月 20 日访谈张前川（前今日头条产品负责人、前 MiniMax 产品负责人）——产品负责人视角的 AGI 威胁警告。张前川称信息流算法已重塑认知——无护栏扩至 AGI 恐权力集中。他熟今日头条推荐与 MiniMax 模型产品；节目桥接中国消费互联网与基础模型实验室。",
            "important_facts": [
                "推荐即原生 AGI：张前川称十亿用户规模优化互动是生产中的对齐问题——头条/抖音机制预览 AGI 部署风险。META 与腾讯（TCEHY）平台已跑大规模偏好优化器。",
                "字节与 MiniMax 透镜：离职后张前川警告能力赛跑赢治理——产品负责人须设计约束非仅 loss。中国私募实验室（MiniMax、DeepSeek）加字节/腾讯分发造快反馈环，投资者不可忽视。",
                "可投资观望：Meta（META）——AI 互动广告 ARPU 对监管与声誉尾部风险。腾讯（TCEHY）——微信与视频 AI 整合伴中国政策。无分发或安全叙事的纯能力赌注低配。",
            ],
            "mental_model": {
                "name": "互动优化器 × 对齐滞后 × 分发房东",
                "components": "信息流是目标函数错误的 AGI。能力实验室跑赢治理。房东变现注意力；实验室烧 capex。",
                "application": "Meta（META）与腾讯（TCEHY）：观望 AI 功能互动提升对政策反弹——ARPU 升且监管未断则房东存活。私募实验室作能力基准非公开标的。",
            },
            "key_insights": [
                {
                    "view": "信息流已是错位 AGI。",
                    "question": "产品人为何警告 AGI？",
                    "answer": "张前川建过最大化停留系统——强优化无显式人类价值。扩展 LLM Agent 以更多行动面延伸同风险。",
                },
                {
                    "view": "能力赛跑赢治理。",
                    "question": "字节与 MiniMax 教他什么？",
                    "answer": "产品交付速度胜安全委员会——张前川离职发声实验室优化 benchmark 而社会缺刹车。投资者应为 META/TCEHY AI rollout 定价监管与声誉期权。",
                },
                {
                    "view": "分发房东向 AGI 盛宴收税。",
                    "question": "可投资敞口在哪？",
                    "answer": "META 与 TCEHY 握推荐引擎要的注意力轨道——私募实验室赢模型房东仍收广告与支付租金。公开投资者按互动变现建仓非 AGI 神学。",
                },
            ],
            "top_investment_implications": [
                {
                    "ticker": "META",
                    "direction": "Watch",
                    "confidence": "Medium",
                    "thesis": "Meta（META）：张前川 AGI 警告——观望 AI 互动 ARPU 对对齐与监管尾部风险",
                },
                {
                    "ticker": "TCEHY",
                    "direction": "Watch",
                    "confidence": "Medium",
                    "thesis": "腾讯（TCEHY）：推荐规模 AI 于微信/视频——观望变现对中国政策与 AGI 反弹风险",
                },
            ],
            "golden_quotes": ["占位一", "占位二", "占位三"],
            "chronology": {
                "subject": "张前川 · AGI 预警",
                "events": [
                    {"date": "2010s", "event": "张前川在字节搭建今日头条推荐产品"},
                    {"date": "2023–2024", "event": "MiniMax 产品负责人；模型赛加速"},
                    {"date": "2025", "event": "离职；发声 AGI 社会风险"},
                    {"date": "2025-02-20", "event": "张小珺访谈录制"},
                    {"date": "2025–2026", "event": "中美 AI 政策争论加剧"},
                    {"date": "2026+", "event": "互动 AI 对 Agent 行动监管"},
                ],
            },
        },
    },
    "zj-ep89": {
        "en": {
            "keywords": ["GOOGL", "DeepSeek-R1", "o1", "Reasoning"],
            "conclusion": "Guangmi's line-by-line read of DeepSeek-R1, Kimi K1.5, and OpenAI o1 reports argues the cleanest reasoning algorithms win — RL on chain-of-thought, distillation, and test-time compute replace brute scaling alone. DeepSeek open-weights pressure GOOGL Gemini pricing; o1 proves paid reasoning tier. Investors should Watch GOOGL on Search and Cloud reasoning monetization as R1-class models compress API margins.",
            "background": "Zhang Xiaojun's Jan 26, 2025 episode with Guangmi dissects technical reports for DeepSeek-R1, Moonshot Kimi K1.5, and OpenAI o1 — 'cleanest and prettiest algorithms.' Guangmi explains GRPO, rejection sampling, long CoT RL, and why test-time compute is the second gold mine after pretrain. Chinese open releases shift competitive dynamics for Alphabet (GOOGL) and private OpenAI.",
            "important_facts": [
                "R1 mechanics: DeepSeek-R1 uses RL to elicit reasoning without heavy human CoT labels — open weights disrupt API rent. Kimi K1.5 parallels with long-context reasoning; o1 validates premium pricing for inference-heavy tasks.",
                "Clean algorithm thesis: Guangmi praises minimal pipelines — fewer hacks, more stable training. Investors should map reasoning capability to $/task willingness-to-pay, not leaderboard trivia.",
                "GOOGL Watch: Gemini must match R1 economics on Cloud and Search AI Overviews — margin pressure if open models commoditize mid-tier reasoning. Upside if GOOGL bundles reasoning into ads and Workspace ARPU.",
            ],
            "mental_model": {
                "name": "Test-Time Compute × Open R1 Commoditization × Reasoning ARPU",
                "components": "Second gold mine is inference-time thinking, not only pretrain. Open R1 compresses API spread. Landlords bundle reasoning into existing ARPU.",
                "application": "Alphabet (GOOGL): Watch Gemini reasoning tier pricing and Search AI monetization — defend margin as DeepSeek-R1 class models open-source. Long if reasoning lifts Cloud and ads yield without capex spiral.",
            },
            "key_insights": [
                {
                    "view": "R1 is RL on thinking, not more data alone.",
                    "question": "What is DeepSeek-R1's core trick?",
                    "answer": "Guangmi explains GRPO and RL that rewards valid reasoning chains — reduces reliance on human CoT labeling. Open release forces GOOGL and peers to compete on $/reasoning token.",
                },
                {
                    "view": "o1 proved paid reasoning tier.",
                    "question": "Why include OpenAI o1 in the same episode?",
                    "answer": "o1 commercialized test-time compute — users pay for longer thinking. Guangmi's frame: cleanest algorithms monetize at inference; pretrain scale alone commoditizes.",
                },
                {
                    "view": "Kimi K1.5 closes China reasoning gap.",
                    "question": "How does Kimi fit the trilogy?",
                    "answer": "K1.5 shows Moonshot competes on long CoT and multimodal reasoning — investors should not treat reasoning as US-only moat; GOOGL competes globally on distribution plus models.",
                },
            ],
            "top_investment_implications": [
                {
                    "ticker": "GOOGL",
                    "direction": "Watch",
                    "confidence": "Medium",
                    "thesis": "Alphabet (GOOGL): Guangmi R1/K1.5/o1 reports — Watch Gemini reasoning monetization as open R1 compresses API margins",
                },
            ],
            "golden_quotes": [
                "The prettiest reasoning algorithms are the cleanest — RL on thinking beats patchwork CoT hacks.",
                "DeepSeek-R1 open weights are a pricing event for every cloud API, including Google.",
                "Test-time compute is the second gold mine — o1 proved users will pay to think longer.",
            ],
            "chronology": {
                "subject": "Guangmi · Reasoning Reports",
                "events": [
                    {"date": "2024-09", "event": "OpenAI o1 preview; test-time compute thesis"},
                    {"date": "2025-01", "event": "DeepSeek-R1 and Kimi K1.5 reports ship"},
                    {"date": "2025-01-26", "event": "Guangmi line-by-line episode recorded"},
                    {"date": "2025", "event": "Open R1 disrupts API pricing globally"},
                    {"date": "2025–2026", "event": "GOOGL Gemini reasoning tiers rollout"},
                    {"date": "2026+", "event": "Reasoning ARPU versus commoditized mid-tier"},
                ],
            },
        },
        "zh": {
            "keywords": ["GOOGL", "DeepSeek-R1", "o1", "推理"],
            "conclusion": "广密逐句讲解 DeepSeek-R1、Kimi K1.5、OpenAI o1 技术报告——最优美算法最干净：思维链 RL、蒸馏与测试时算力取代纯 scaling。DeepSeek 开源压 GOOGL Gemini 定价；o1 证付费推理档。投资者应观望 GOOGL 搜索与云推理变现，R1 级模型压缩 API 毛利。",
            "background": "张小珺 2025 年 1 月 26 日与广密拆解 DeepSeek-R1、月之暗面 Kimi K1.5、OpenAI o1 技术报告——「最优美最干净的算法」。广密解释 GRPO、拒绝采样、长 CoT 强化学习及测试时算力为预训练后第二金矿。中国开源发布改变 Alphabet（GOOGL）与私募 OpenAI 竞争动态。",
            "important_facts": [
                "R1 机制：DeepSeek-R1 用 RL 引出推理减重度人工 CoT 标注——开源权重 disrupt API 租金。Kimi K1.5 并行长上下文推理；o1 验证推理重任务的溢价定价。",
                "干净算法论点：广密赞极简管线——少 hack、训练更稳。投资者应将推理能力映射 $/任务付费意愿非 leaderboard 琐事。",
                "GOOGL 观望：Gemini 须在云与搜索 AI Overviews 匹配 R1 经济学——开源模型商品化中端推理则毛利承压。若 GOOGL 将推理 bundle 进广告与 Workspace ARPU 则上行。",
            ],
            "mental_model": {
                "name": "测试时算力 × 开源 R1 商品化 × 推理 ARPU",
                "components": "第二金矿是推理时思考非仅预训练。开源 R1 压缩 API 价差。房东将推理 bundle 进既有 ARPU。",
                "application": "Alphabet（GOOGL）：观望 Gemini 推理档定价与搜索 AI 变现——DeepSeek-R1 级开源时守毛利。推理抬云与广告 yield 且 capex 未螺旋则看多。",
            },
            "key_insights": [
                {
                    "view": "R1 是思考上的 RL 非仅更多数据。",
                    "question": "DeepSeek-R1 核心技巧？",
                    "answer": "广密解释 GRPO 与奖励有效推理链的 RL——减依赖人工 CoT 标注。开源迫 GOOGL 与同行竞 $/推理 token。",
                },
                {
                    "view": "o1 证付费推理档。",
                    "question": "为何同集含 OpenAI o1？",
                    "answer": "o1 将测试时算力商业化——用户为更长思考付费。广密框架：最干净算法在推理变现；仅预训练 scale 则商品化。",
                },
                {
                    "view": "Kimi K1.5 缩小中国推理差距。",
                    "question": "Kimi 在三部曲中何位？",
                    "answer": "K1.5 示 Moonshot 在长 CoT 与多模态推理竞争——投资者勿将推理当美国独有护城河；GOOGL 全球以分发加模型竞争。",
                },
            ],
            "top_investment_implications": [
                {
                    "ticker": "GOOGL",
                    "direction": "Watch",
                    "confidence": "Medium",
                    "thesis": "Alphabet（GOOGL）：广密 R1/K1.5/o1 报告——观望 Gemini 推理变现随开源 R1 压缩 API 毛利",
                },
            ],
            "golden_quotes": ["占位一", "占位二", "占位三"],
            "chronology": {
                "subject": "广密 · 推理报告",
                "events": [
                    {"date": "2024-09", "event": "OpenAI o1 预览；测试时算力论点"},
                    {"date": "2025-01", "event": "DeepSeek-R1 与 Kimi K1.5 报告发布"},
                    {"date": "2025-01-26", "event": "广密逐句讲解节目录制"},
                    {"date": "2025", "event": "开源 R1 全球 disrupt API 定价"},
                    {"date": "2025–2026", "event": "GOOGL Gemini 推理档 rollout"},
                    {"date": "2026+", "event": "推理 ARPU 对商品化中端"},
                ],
            },
        },
    },
    "zj-ep88": {
        "en": {
            "keywords": ["GOOGL", "Private:OpenAI", "Operator", "Agent"],
            "conclusion": "Wu Yi's Operator technical decode frames OpenAI's browser agent as reasoning leaving the abstract world for the physical UI — computer use is the bridge from CoT to clicks. GOOGL competes via Gemini plus Chrome distribution; most Operator upside stays private. Investors should Watch GOOGL on agentic browser features and Private:OpenAI on Operator reliability as willingness-to-pay benchmark for action-layer AI.",
            "background": "Zhang Xiaojun's Jan 19, 2025 episode with Wu Yi (former OpenAI researcher, Tsinghua assistant professor) explains OpenAI Operator — an agent that navigates websites and executes tasks. Wu argues this is the start of models acting in digital physical environments, not just answering prompts. Technical topics: vision-language grounding, action spaces, safety, and why browser sandbox is the first production environment before robots.",
            "important_facts": [
                "Abstract to physical digital: Wu Yi says Operator moves reasoning from text worlds to DOM and UI — clicks and forms are actions with state. This is investable agent layer beyond chat; failures are visible (wrong purchase) versus hallucinated paragraphs.",
                "GOOGL competitive lens: Chrome and Android give Alphabet distribution for computer-use agents — Gemini integration Watch as public landlord response to Private:OpenAI Operator. Winner may be orchestrator plus trust, not raw model IQ alone.",
                "Safety and economics: Wu stresses guardrails on payment and account actions — agents need human-in-loop until reliability clears. Investors price action AI on task success rate and liability, not demo videos.",
            ],
            "mental_model": {
                "name": "UI as Physical World × Browser Sandbox × Distribution Landlord",
                "components": "Digital UI is first physical environment for agents. Browser sandbox limits blast radius while learning. Chrome/Android distribution taxes agent feast.",
                "application": "Alphabet (GOOGL): Watch Gemini computer-use in Chrome and Workspace — landlord wins if bundled into existing ARPU. Private:OpenAI: Watch Operator task success and pricing as private action-layer benchmark.",
            },
            "key_insights": [
                {
                    "view": "Operator is reasoning with hands on the web.",
                    "question": "Why does Wu call this physical world entry?",
                    "answer": "Websites are stateful environments — agents must perceive, plan, and act. Operator is first mass-market bridge from CoT to operational entropy reduction in real workflows.",
                },
                {
                    "view": "Browser beats robot for v1 economics.",
                    "question": "Why not jump to embodied agents?",
                    "answer": "Wu Yi notes UI actions scale in software — no hardware cycle, faster iteration. Robotaxi and factory robots come later; investors should size near-term agent revenue on digital tasks.",
                },
                {
                    "view": "GOOGL owns the browser toll booth.",
                    "question": "Where is public market exposure?",
                    "answer": "Chrome distribution lets GOOGL bundle computer-use agents — competing with Private:OpenAI on trust and integration, not only model benchmarks. Watch agent features in Search and Workspace monetization.",
                },
            ],
            "top_investment_implications": [
                {
                    "ticker": "GOOGL",
                    "direction": "Watch",
                    "confidence": "Medium",
                    "thesis": "Alphabet (GOOGL): Wu Yi Operator decode — Watch Gemini agentic browser and Workspace action features versus Private:OpenAI",
                },
                {
                    "ticker": "Private:OpenAI",
                    "direction": "Watch",
                    "confidence": "Medium",
                    "thesis": "Private:OpenAI: Operator computer-use — Watch task reliability and pricing as action-layer AI benchmark",
                },
            ],
            "golden_quotes": [
                "Operator is the moment reasoning leaves the abstract world and touches buttons on real websites.",
                "The browser is the first physical environment for agents — cheaper than robots, faster to iterate.",
                "Distribution on Chrome matters as much as model IQ for computer-use agents.",
            ],
            "chronology": {
                "subject": "Wu Yi · OpenAI Operator",
                "events": [
                    {"date": "2024", "event": "Computer-use and CUA research at OpenAI"},
                    {"date": "2025-01", "event": "OpenAI Operator preview launch"},
                    {"date": "2025-01-19", "event": "Wu Yi technical decode recorded"},
                    {"date": "2025", "event": "GOOGL Gemini agentic browser response"},
                    {"date": "2025–2026", "event": "Operator reliability and pricing tests"},
                    {"date": "2026+", "event": "Digital agents extend to enterprise workflows"},
                ],
            },
        },
        "zh": {
            "keywords": ["GOOGL", "Private:OpenAI", "Operator", "Agent"],
            "conclusion": "吴翼解读 OpenAI Operator 将浏览器 Agent 框为推理从抽象世界走向物理 UI——电脑操作是 CoT 到点击的桥梁。GOOGL 以 Gemini 加 Chrome 分发竞争；多数 Operator 上行留私募。投资者应观望 GOOGL 的 Agent 浏览器功能与 Private:OpenAI 的 Operator 可靠性作行动层 AI 付费意愿基准。",
            "background": "张小珺 2025 年 1 月 19 日与吴翼（OpenAI 前研究员、清华助理教授）解释 OpenAI Operator——浏览网站并执行任务的 Agent。吴翼称这是模型在数字物理环境行动而非仅答 prompt 的起点。技术话题：视觉语言接地、动作空间、安全及浏览器沙盒为何是先于机器人的首个生产环境。",
            "important_facts": [
                "抽象到数字物理：吴翼称 Operator 将推理从文本世界移至 DOM 与 UI——点击与表单是有状态行动。这是可投资 Agent 层超聊天；失败可见（错购）非幻觉段落。",
                "GOOGL 竞争透镜：Chrome 与 Android 给 Alphabet 电脑操作 Agent 分发——Gemini 整合观望作对 Private:OpenAI Operator 的公开房东回应。赢家或系编排加信任非仅模型 IQ。",
                "安全与经济学：吴翼强调支付与账户操作的护栏——可靠性清前须人在回路。投资者按任务成功率与责任定价行动 AI 非 demo 视频。",
            ],
            "mental_model": {
                "name": "UI 即物理世界 × 浏览器沙盒 × 分发房东",
                "components": "数字 UI 是 Agent 首个物理环境。浏览器沙盒限爆炸半径同时学习。Chrome/Android 分发向 Agent 盛宴收税。",
                "application": "Alphabet（GOOGL）：观望 Chrome 与 Workspace 的 Gemini 电脑操作——bundle 进既有 ARPU 则房东胜。Private:OpenAI：观望 Operator 任务成功与定价作私募行动层基准。",
            },
            "key_insights": [
                {
                    "view": "Operator 是带手的网页推理。",
                    "question": "吴翼为何称进入物理世界？",
                    "answer": "网站是有状态环境——Agent 须感知、规划、行动。Operator 是 CoT 到真实工作流操作减熵的首个大众桥梁。",
                },
                {
                    "view": "浏览器 v1 经济学胜机器人。",
                    "question": "为何不跳具身 Agent？",
                    "answer": "吴翼指 UI 行动在软件中 scale——无硬件周期、迭代更快。Robotaxi 与工厂机器人稍后；投资者应按数字任务定近期 Agent 收入。",
                },
                {
                    "view": "GOOGL 握浏览器收费站。",
                    "question": "公开市场监管敞口在哪？",
                    "answer": "Chrome 分发让 GOOGL bundle 电脑操作 Agent——与 Private:OpenAI 竞信任与整合非仅 benchmark。观望搜索与 Workspace Agent 功能变现。",
                },
            ],
            "top_investment_implications": [
                {
                    "ticker": "GOOGL",
                    "direction": "Watch",
                    "confidence": "Medium",
                    "thesis": "Alphabet（GOOGL）：吴翼 Operator 解读——观望 Gemini Agent 浏览器与 Workspace 行动功能对 Private:OpenAI",
                },
                {
                    "ticker": "Private:OpenAI",
                    "direction": "Watch",
                    "confidence": "Medium",
                    "thesis": "Private:OpenAI：Operator 电脑操作——观望任务可靠性与定价作行动层 AI 基准",
                },
            ],
            "golden_quotes": ["占位一", "占位二", "占位三"],
            "chronology": {
                "subject": "吴翼 · OpenAI Operator",
                "events": [
                    {"date": "2024", "event": "OpenAI 电脑操作与 CUA 研究"},
                    {"date": "2025-01", "event": "OpenAI Operator 预览发布"},
                    {"date": "2025-01-19", "event": "吴翼技术解读录制"},
                    {"date": "2025", "event": "GOOGL Gemini Agent 浏览器回应"},
                    {"date": "2025–2026", "event": "Operator 可靠性与定价考验"},
                    {"date": "2026+", "event": "数字 Agent 延伸至企业工作流"},
                ],
            },
        },
    },
    "zj-ep75": {
        "en": {
            "keywords": ["GOOGL", "Private:OpenAI", "o1", "Reasoning"],
            "conclusion": "Wu Yi's o1 decode calls test-time compute the second gold mine — after pretrain scaling, RL on reasoning chains monetizes at inference. o1 preview shifts AI economics toward paid thinking tokens; GOOGL must match on Gemini while Private:OpenAI owns first-mover pricing. Investors should Watch GOOGL on reasoning tier ARPU and Private:OpenAI on o1/o3 cadence as capability benchmark.",
            "background": "Zhang Xiaojun's Sep 22, 2024 interview with Wu Yi (former OpenAI researcher) explains OpenAI o1 — chain-of-thought RL, hidden reasoning tokens, and safety implications. Wu frames o1 as trumpet for mining inference-time compute: users and enterprises pay for longer internal deliberation. Episode predates R1 open weights but establishes investor lens for reasoning race GOOGL and Chinese labs now join.",
            "important_facts": [
                "Second gold mine: Wu Yi argues pretrain scaling returns diminish — o1 RL on reasoning opens new revenue vein via test-time flops. Private:OpenAI captures premium; GOOGL and peers must productize or lose API spread.",
                "Hidden CoT economics: o1 hides deliberation tokens — pricing power if tasks complete reliably. Investors track willingness-to-pay for coding, science, and planning versus flat chat subscriptions.",
                "GOOGL response Watch: Gemini reasoning modes and Search integration are public-market exposure — margin tradeoff between free search and paid deep think. Underweight chat-only wrappers as o1-class models commoditize mid-tier.",
            ],
            "mental_model": {
                "name": "Test-Time Gold Mine × Hidden CoT Pricing × Reasoning ARPU",
                "components": "Pretrain feast matures; inference thinking is next vein. Hidden CoT enables premium tiers. Landlords bundle or lose spread to open R1.",
                "application": "Alphabet (GOOGL): Watch Gemini reasoning SKUs and enterprise pricing — defend ARPU as o1/R1 commoditize. Private:OpenAI: Watch o-series cadence as private reasoning benchmark public cannot fully access.",
            },
            "key_insights": [
                {
                    "view": "o1 sounds the second gold mine horn.",
                    "question": "What does Wu mean by second gold mine?",
                    "answer": "After scaling laws on pretrain, RL improving reasoning at inference creates new economic layer — customers pay for thinking time, not just weights. This reframes capex from training-only to train-plus-infer.",
                },
                {
                    "view": "Hidden reasoning is pricing feature.",
                    "question": "Why hide chain-of-thought?",
                    "answer": "Wu Yi notes safety and competition — but economically it enables metered deliberation. Investors should model reasoning tokens as ARPU driver, not cost center only.",
                },
                {
                    "view": "GOOGL must productize deep think.",
                    "question": "Where do public investors participate?",
                    "answer": "Gemini reasoning in Cloud, Workspace, and Search AI Overviews — GOOGL bundles into existing landlord ARPU. Failure mode is free search giving away o1-class capability.",
                },
            ],
            "top_investment_implications": [
                {
                    "ticker": "GOOGL",
                    "direction": "Watch",
                    "confidence": "Medium",
                    "thesis": "Alphabet (GOOGL): Wu Yi o1 second gold mine — Watch Gemini reasoning ARPU as test-time compute monetizes",
                },
                {
                    "ticker": "Private:OpenAI",
                    "direction": "Watch",
                    "confidence": "Medium",
                    "thesis": "Private:OpenAI: o1 reasoning economics — Watch o-series cadence and pricing as private benchmark",
                },
            ],
            "golden_quotes": [
                "o1 is the trumpet sounding the second gold mine — test-time compute, not just bigger pretrain.",
                "Users will pay for hidden thinking when the answer reliably ships hard work.",
                "Every cloud landlord including Google must productize deep reasoning or lose API spread.",
            ],
            "chronology": {
                "subject": "Wu Yi · OpenAI o1",
                "events": [
                    {"date": "2024", "event": "OpenAI internal reasoning RL research matures"},
                    {"date": "2024-09", "event": "o1 preview launch"},
                    {"date": "2024-09-22", "event": "Wu Yi o1 decode with Zhang Xiaojun"},
                    {"date": "2025-01", "event": "DeepSeek-R1 open-weights reasoning wave"},
                    {"date": "2025–2026", "event": "GOOGL Gemini reasoning tiers"},
                    {"date": "2026+", "event": "Reasoning ARPU versus commoditization"},
                ],
            },
        },
        "zh": {
            "keywords": ["GOOGL", "Private:OpenAI", "o1", "推理"],
            "conclusion": "吴翼 o1 解读称测试时算力为第二金矿——预训练 scaling 之后，思维链 RL 在推理变现。o1 预览将 AI 经济学转向付费思考 token；GOOGL 须在 Gemini 匹配而 Private:OpenAI 握先发定价。投资者应观望 GOOGL 推理档 ARPU 与 Private:OpenAI o1/o3 节奏作能力基准。",
            "background": "张小珺 2024 年 9 月 22 日访谈吴翼（OpenAI 前研究员）解释 OpenAI o1——思维链 RL、隐藏推理 token 与安全含义。吴翼框 o1 为开挖推理时算力的号角：用户与企业为更长内部斟酌付费。节目早于 R1 开源但建立 GOOGL 与中国实验室现加入的推理赛投资透镜。",
            "important_facts": [
                "第二金矿：吴翼称预训练 scaling 回报递减——o1 推理 RL 经测试时 flop 开新收入矿脉。Private:OpenAI 捕获溢价；GOOGL 与同行须产品化否则失 API 价差。",
                "隐藏 CoT 经济学：o1 隐藏斟酌 token——任务可靠完成则有定价权。投资者跟编码、科学与规划的付费意愿对 flat 聊天订阅。",
                "GOOGL 回应观望：Gemini 推理模式与搜索整合是公开市场敞口——免费搜索与付费深思的毛利权衡。o1 级模型商品化中端时聊天套壳低配。",
            ],
            "mental_model": {
                "name": "测试时金矿 × 隐藏 CoT 定价 × 推理 ARPU",
                "components": "预训练盛宴成熟；推理思考是下一矿脉。隐藏 CoT 支撑溢价档。房东 bundle 否则失 spread 给开源 R1。",
                "application": "Alphabet（GOOGL）：观望 Gemini 推理 SKU 与企业定价——o1/R1 商品化时守 ARPU。Private:OpenAI：观望 o 系列节奏作公开市场无法完全获得的私募推理基准。",
            },
            "key_insights": [
                {
                    "view": "o1 吹响第二金矿号角。",
                    "question": "吴翼第二金矿何意？",
                    "answer": "预训练 scaling 定律后，推理时改善推理的 RL 造新经济层——客户为思考时间非仅权重付费。将 capex 从仅训练重框为训练加推理。",
                },
                {
                    "view": "隐藏推理是定价功能。",
                    "question": "为何隐藏思维链？",
                    "answer": "吴翼指安全与竞争——但经济学上 enable 计量斟酌。投资者应将推理 token 作 ARPU 驱动非仅成本中心。",
                },
                {
                    "view": "GOOGL 须产品化深思。",
                    "question": "公开投资者如何参与？",
                    "answer": "云、Workspace 与搜索 AI Overviews 的 Gemini 推理——GOOGL bundle 进既有房东 ARPU。失败模式是免费搜索赠送 o1 级能力。",
                },
            ],
            "top_investment_implications": [
                {
                    "ticker": "GOOGL",
                    "direction": "Watch",
                    "confidence": "Medium",
                    "thesis": "Alphabet（GOOGL）：吴翼 o1 第二金矿——观望 Gemini 推理 ARPU 随测试时算力变现",
                },
                {
                    "ticker": "Private:OpenAI",
                    "direction": "Watch",
                    "confidence": "Medium",
                    "thesis": "Private:OpenAI：o1 推理经济学——观望 o 系列节奏与定价作私募基准",
                },
            ],
            "golden_quotes": ["占位一", "占位二", "占位三"],
            "chronology": {
                "subject": "吴翼 · OpenAI o1",
                "events": [
                    {"date": "2024", "event": "OpenAI 内部推理 RL 研究成熟"},
                    {"date": "2024-09", "event": "o1 预览发布"},
                    {"date": "2024-09-22", "event": "吴翼 o1 解读张小珺节目"},
                    {"date": "2025-01", "event": "DeepSeek-R1 开源推理浪潮"},
                    {"date": "2025–2026", "event": "GOOGL Gemini 推理档"},
                    {"date": "2026+", "event": "推理 ARPU 对商品化"},
                ],
            },
        },
    },
    "tzs-ep155": {
        "en": {
            "keywords": ["600519.SZ", "Consumer", "Dining", "Moutai"],
            "conclusion": "Practical Investments ep.155 maps dining brands — Xibei, Haidilao, Mixue, Xiaocaiyuan — to investable consumer patterns: supply chain, franchise discipline, and occasion pricing. Moutai (600519.SZ) anchors luxury ritual in the same consumption conversation. Investors should Watch Kweichow Moutai (600519.SZ) on批价 and dining recovery as casual versus premium diverge.",
            "background": "David hosts ep.155 (Nov 2, 2025) on investment insights behind eat-and-drink — from hotpot and northwest cuisine to tea chains and baijiu ritual. Framework: user value per occasion, turnover versus ticket size, and franchise versus direct-operate economics. Xibei's parenting brand crisis and Haidilao's service moat illustrate operating risk; Mixue shows scale on thin margin; Moutai remains pricing-power benchmark in same consumer wallet.",
            "important_facts": [
                "Dining framework: Occasion-based segmentation — daily tea (Mixue) versus celebration hotpot (Haidilao) versus business baijiu (600519.SZ). Investors compare unit economics: franchise royalty versus direct-store labor intensity.",
                "Brand crisis lesson: Xibei episode shows reputation shocks hit faster in social media era — consumer investable names need governance and PR resilience, not only same-store growth.",
                "Moutai in wallet: Kweichow Moutai (600519.SZ) competes for premium consumption budget — Watch批价 spread as dining recovery and gift policy shift; not every food trend correlates with baijiu demand.",
            ],
            "mental_model": {
                "name": "Occasion Segmentation × Franchise Unit Economics × Brand Shock Velocity",
                "components": "Dining brands win on matched occasion and cost structure. Franchise scales fast with governance risk. Social media accelerates brand crises.",
                "application": "Kweichow Moutai (600519.SZ): Watch批价 and premium dining correlation — Long only at margin-of-safety versus liquor peers. Underweight if consumption downgrade hits ritual brands together.",
            },
            "key_insights": [
                {
                    "view": "Eat-and-drink is multiple investable theses.",
                    "question": "Why lump Xibei to Moutai in one episode?",
                    "answer": "Same consumer wallet, different occasions — hosts teach comparing turnover, ticket, and margin structures instead of treating 'consumer' as one sector trade.",
                },
                {
                    "view": "Franchise scale has hidden tail risk.",
                    "question": "What does Mixue versus Haidilao teach?",
                    "answer": "Mixue wins on supply-chain cost at massive unit count; Haidilao invests in service labor — investors must match model to valuation multiples, not revenue hype alone.",
                },
                {
                    "view": "Moutai is pricing-power north star.",
                    "question": "Where is listed exposure?",
                    "answer": "Among brands discussed, 600519.SZ is liquid investable anchor —批价 premium signals channel health while dining names are mostly private. Watch Moutai when macro consumption debates heat.",
                },
            ],
            "top_investment_implications": [
                {
                    "ticker": "600519.SZ",
                    "direction": "Watch",
                    "confidence": "Medium",
                    "thesis": "Kweichow Moutai (600519.SZ): Dining insights episode — Watch批价 and premium consumption as casual dining diverges",
                },
            ],
            "golden_quotes": [
                "Behind every dining brand is a different occasion — and a different unit-economic animal.",
                "Franchise scale is fast until governance or reputation breaks the flywheel.",
                "Moutai still sets the ceiling for premium consumption pricing power in China.",
            ],
            "chronology": {
                "subject": "David · Dining Insights",
                "events": [
                    {"date": "2024–2025", "event": "Xibei brand crisis; consumer PR velocity debate"},
                    {"date": "2025", "event": "Mixue and tea chain scale; Haidilao service moat"},
                    {"date": "2025", "event": "Moutai批价 and channel reform ongoing"},
                    {"date": "2025-11-02", "event": "Practical Investments ep.155 recorded"},
                    {"date": "2026", "event": "Dining recovery versus premium baijiu divergence"},
                ],
            },
        },
        "zh": {
            "keywords": ["600519.SZ", "消费", "餐饮", "茅台"],
            "conclusion": "投资实战派第 155 期将西贝、海底捞、蜜雪、小菜园等餐饮品牌映射为可投资消费模式：供应链、加盟纪律与场景定价。贵州茅台（600519.SZ）在同场消费对话中锚定奢侈品仪式。投资者应观望贵州茅台（600519.SZ）批价与餐饮复苏， casual 与高端分化。",
            "background": "大卫主持第 155 期（2025 年 11 月 2 日）谈吃吃喝喝背后投资——从火锅、西北菜到茶饮链与白酒仪式。框架：场景用户价值、周转对客单价、加盟对直营经济学。西贝育儿品牌危机与海底捞服务护城河示运营风险；蜜雪示薄利规模化；茅台仍是同钱包消费定价权基准。",
            "important_facts": [
                "餐饮框架：场景细分——日常茶（蜜雪）对庆祝火锅（海底捞）对商务白酒（600519.SZ）。投资者比单位经济学：加盟 royalty 对直营店劳动强度。",
                "品牌危机课：西贝案示声誉冲击在社媒时代更快——消费可投资名需治理与 PR 韧性非仅同店增长。",
                "茅台在钱包中：贵州茅台（600519.SZ）竞 premium 消费预算——观望批价利差随餐饮复苏与送礼政策变；非每条食品趋势与白酒需求相关。",
            ],
            "mental_model": {
                "name": "场景细分 × 加盟单位经济学 × 品牌冲击速度",
                "components": "餐饮品牌以匹配场景与成本结构胜。加盟快 scale 伴治理风险。社媒加速品牌危机。",
                "application": "贵州茅台（600519.SZ）：观望批价与高端餐饮相关——仅相对酒企 peer 安全边际看多。消费降级齐击仪式品牌则低配。",
            },
            "key_insights": [
                {
                    "view": "吃喝是多条可投资论点。",
                    "question": "为何西贝到茅台同集？",
                    "answer": "同消费者钱包、不同场景——主持教比周转、客单与毛利结构，非把「消费」当单一板块交易。",
                },
                {
                    "view": "加盟规模有隐藏尾部风险。",
                    "question": "蜜雪对海底捞教什么？",
                    "answer": "蜜雪以供应链成本胜海量门店；海底捞投服务劳动——投资者须将模式匹配估值倍数非仅收入 hype。",
                },
                {
                    "view": "茅台是定价权北极星。",
                    "question": "上市敞口在哪？",
                    "answer": "所议品牌中 600519.SZ 是流动性可投资锚——批价溢价信号渠道健康而餐饮多为私有。宏观消费争论热时观望茅台。",
                },
            ],
            "top_investment_implications": [
                {
                    "ticker": "600519.SZ",
                    "direction": "Watch",
                    "confidence": "Medium",
                    "thesis": "贵州茅台（600519.SZ）：餐饮洞察节目——观望批价与 premium 消费随 casual 餐饮分化",
                },
            ],
            "golden_quotes": ["占位一", "占位二", "占位三"],
            "chronology": {
                "subject": "大卫 · 餐饮洞察",
                "events": [
                    {"date": "2024–2025", "event": "西贝品牌危机；消费 PR 速度争论"},
                    {"date": "2025", "event": "蜜雪与茶饮链规模；海底捞服务护城河"},
                    {"date": "2025", "event": "茅台批价与渠道改革持续"},
                    {"date": "2025-11-02", "event": "投资实战派第 155 期录制"},
                    {"date": "2026", "event": "餐饮复苏对 premium 白酒分化"},
                ],
            },
        },
    },
    "tzs-ep127": {
        "en": {
            "keywords": ["6181.HK", "Laopu Gold", "New Consumer", "Luxury"],
            "conclusion": "Laopu Gold (6181.HK) episode debates heritage craft premium versus IQ tax — ancient-method gold jewelry rides cultural luxury and store experience, not commodity bullion alone. Guests split on sustainability of ASP lift versus gold-price beta. Investors should Watch Laopu Gold (6181.HK) on same-store growth, gross margin versus gold spot, and inventory days as new-consumer luxury fad or compounder.",
            "background": "Practical Investments ep.127 (Jun 15, 2025) chats Laopu Gold with consumer investors and shoppers — part of new-consumer series. Laopu prices craftsmanship and cultural storytelling above melt value; stores resemble luxury boutiques. Debate: real brand moat or cyclical gold hype with pretty packaging. Compare to traditional jewelers and Pop Mart-style emotional premium.",
            "important_facts": [
                "Craft premium thesis: Laopu Gold (6181.HK) sells heritage gold art — ASP multiples over bullion if brand sustains. Watch gross margin when gold spot volatility rises — inventory revaluation risk.",
                "Store experience moat: High-touch retail and limited SKUs create scarcity — similar to luxury fashion, not mass jewelry chains. Investors track new store productivity and repeat purchase, not only gold price rally.",
                "IQ tax risk: Skeptics argue Laopu is gold beta plus marketing — underweight if same-store slows while stores flood tier-2 cities. Long only if craftsmanship retention proves pricing power through cycle.",
            ],
            "mental_model": {
                "name": "Craft Premium × Gold Beta × Experience Retail",
                "components": "Heritage story justifies ASP over melt. Gold spot still drives inventory marks. Experience stores scale until scarcity dilutes.",
                "application": "Laopu Gold (6181.HK): Watch SSSG and margin ex-gold move — compounder thesis needs repeat emotional purchase, not only bullion rally. Trim on rapid store add without productivity.",
            },
            "key_insights": [
                {
                    "view": "Laopu sells story, not ounces.",
                    "question": "Is craft premium real?",
                    "answer": "Guests note ancient-method positioning and boutique UX — if customers return for design, 6181.HK is brand play; if only gold fever, it is leveraged bullion proxy.",
                },
                {
                    "view": "Gold spot is hidden beta.",
                    "question": "What risk do investors underprice?",
                    "answer": "Rising gold can flatter revenue while masking weak SSSG — hosts warn to strip commodity move from operating performance when sizing 6181.HK.",
                },
                {
                    "view": "New consumer luxury needs scarcity discipline.",
                    "question": "How does Laopu compare to Pop Mart?",
                    "answer": "Both sell emotional premium — Laopu tied to metal cycles, Pop Mart to IP pipeline. 6181.HK investors need store productivity discipline like 9992.HK IP hit rate.",
                },
            ],
            "top_investment_implications": [
                {
                    "ticker": "6181.HK",
                    "direction": "Watch",
                    "confidence": "Medium",
                    "thesis": "Laopu Gold (6181.HK): Heritage craft premium debate — Watch SSSG and margin versus gold beta as fad or compounder",
                },
            ],
            "golden_quotes": [
                "Laopu charges for the story in the gold, not just the gold in the story.",
                "When bullion rallies, every jeweler looks brilliant — same-store tells the truth.",
                "Experience retail scales until scarcity becomes ubiquity.",
            ],
            "chronology": {
                "subject": "Practical Investments · Laopu Gold",
                "events": [
                    {"date": "2023–2024", "event": "Laopu Gold listing and store expansion"},
                    {"date": "2025", "event": "Gold price rally boosts sector narrative"},
                    {"date": "2025-06-15", "event": "Ep.127 new-consumer chat recorded"},
                    {"date": "2025–2026", "event": "Tier-2 store rollout and SSSG tests"},
                    {"date": "2026+", "event": "Craft premium versus commodity cycle resolves"},
                ],
            },
        },
        "zh": {
            "keywords": ["6181.HK", "老铺黄金", "新消费", "奢侈品"],
            "conclusion": "老铺黄金（6181.HK）节目辩论古法工艺溢价还是智商税——古法金饰靠文化奢侈与店体验非仅商品金条。嘉宾分歧 ASP 提升可持续性与金价 beta。投资者应观望老铺黄金（6181.HK）同店增长、毛利对金价与库存天数，判新消费奢侈 fad 或复利器。",
            "background": "投资实战派第 127 期（2025 年 6 月 15 日）与消费投资人与顾客聊老铺黄金——新消费系列。老铺对工艺与文化叙事定价高于 melt value；门店似 luxury boutique。争论：真品牌护城河或周期性黄金 hype 加精美包装。对比传统金店与泡泡玛特式情感溢价。",
            "important_facts": [
                "工艺溢价论点：老铺黄金（6181.HK）卖传承金艺——品牌持续则 ASP 为 bullion 数倍。金价波动时观望毛利——库存重估风险。",
                "店体验护城河：高 touch 零售与有限 SKU 造稀缺——类 luxury 时装非 mass 金链。投资者跟新店效与复购非仅金价 rally。",
                "智商税风险：怀疑者称老铺是金价 beta 加营销——同店放缓而二线店泛滥则低配。仅当工艺留存证周期定价权时看多。",
            ],
            "mental_model": {
                "name": "工艺溢价 × 金价 Beta × 体验零售",
                "components": "传承故事 justify ASP 超 melt。金价仍驱动库存 mark。体验店 scale 至稀缺稀释。",
                "application": "老铺黄金（6181.HK）：观望 SSSG 与剔除金价波动的毛利——复利论点需重复情感购买非仅 bullion rally。无店效 rapid 扩店则减仓。",
            },
            "key_insights": [
                {
                    "view": "老铺卖故事非克数。",
                    "question": "工艺溢价是否真实？",
                    "answer": "嘉宾指古法定位与 boutique UX——若顾客为设计回头则 6181.HK 是品牌玩法；若仅黄金狂热则是杠杆 bullion 代理。",
                },
                {
                    "view": "金价是隐藏 beta。",
                    "question": "投资者低估何风险？",
                    "answer": "金价升可美化收入掩盖弱 SSSG——主持警告定价 6181.HK 时剥离商品波动对经营表现。",
                },
                {
                    "view": "新消费奢侈需稀缺纪律。",
                    "question": "老铺如何比泡泡玛特？",
                    "answer": "二者卖情感溢价——老铺绑金属周期，泡泡玛特绑 IP 管线。老铺黄金（6181.HK）投资者需如泡泡玛特（9992.HK）IP 命中率般的店效纪律。",
                },
            ],
            "top_investment_implications": [
                {
                    "ticker": "6181.HK",
                    "direction": "Watch",
                    "confidence": "Medium",
                    "thesis": "老铺黄金（6181.HK）：古法溢价辩论——观望 SSSG 与毛利对金价 beta 判 fad 或复利",
                },
            ],
            "golden_quotes": ["占位一", "占位二", "占位三"],
            "chronology": {
                "subject": "投资实战派 · 老铺黄金",
                "events": [
                    {"date": "2023–2024", "event": "老铺黄金上市与门店扩张"},
                    {"date": "2025", "event": "金价上涨抬板块叙事"},
                    {"date": "2025-06-15", "event": "第 127 期新消费畅聊录制"},
                    {"date": "2025–2026", "event": "二线 rollout 与同店考验"},
                    {"date": "2026+", "event": "工艺溢价对商品周期明朗"},
                ],
            },
        },
    },
    "tzs-ep125": {
        "en": {
            "keywords": ["9992.HK", "Pop Mart", "IP", "Art Toys"],
            "conclusion": "Pop Mart (9992.HK) episode asks beautiful bubble or plastic Moutai — IP flywheel and blind-box scarcity drive repeat buy; skeptics see fad SKUs without Spirit depth. David frames compounder versus bubble on IP renewal rate and overseas SSSG. Investors should Watch Pop Mart (9992.HK) on Labubu-class pipeline and international store productivity, not China mall hype alone.",
            "background": "Practical Investments ep.125 (Jun 5, 2025) deep-dives Pop Mart in new-consumer series — unique among Chinese consumer listings as pure IP collectibles play. David compares emotional premium to Moutai ritual and plastic commoditization risk. Labubu global breakout tests whether Pop Mart is platform or one-hit mascot factory.",
            "important_facts": [
                "IP compounder test: Pop Mart (9992.HK) needs recurring character hits — Watch new IP success rate and artist pipeline, not blind-box revenue alone. Labubu proved global taste; next IP validates platform thesis.",
                "Plastic Moutai debate: Bulls see pricing power and scarcity mechanics; bears see fad collectibles with landfill endings. Margin and overseas ASP differentiate bubble from compounder.",
                "Overseas second curve: International stores lift mix — investors track SSSG abroad versus diaspora tourists. Failure mode is exporting China hype without localized Spirit.",
            ],
            "mental_model": {
                "name": "IP Renewal Rate × Blind-Box Scarcity × Overseas SSSG",
                "components": "Compounder needs pipeline depth, not one mascot. Blind-box gamifies distribution. Global SSSG proves IP beyond China fad.",
                "application": "Pop Mart (9992.HK): Watch post-Labubu IP cadence and overseas productivity — Long thesis is global collectibles platform. Trim on SKU flood without character story.",
            },
            "key_insights": [
                {
                    "view": "Beautiful bubble if IP pipeline dries.",
                    "question": "How do hosts split bull and bear?",
                    "answer": "David asks whether Pop Mart is Disney-like renewal or plastic fad — 9992.HK bull case needs second and third global IP wins, not Labubu extrapolation.",
                },
                {
                    "view": "Plastic Moutai is scarcity economics.",
                    "question": "Why compare to Moutai?",
                    "answer": "Both sell ritual and scarcity — Moutai drinks, Pop Mart displays. Investable difference is IP must renew faster; track hit rate quarterly.",
                },
                {
                    "view": "Overseas proves globalization.",
                    "question": "What metric matters most now?",
                    "answer": "International same-store and local drops — if abroad repeat buy holds, 9992.HK deserves platform multiple; if only tourists, revert to fad multiple.",
                },
            ],
            "top_investment_implications": [
                {
                    "ticker": "9992.HK",
                    "direction": "Watch",
                    "confidence": "Medium",
                    "thesis": "Pop Mart (9992.HK): Bubble versus plastic Moutai debate — Watch IP pipeline and overseas SSSG as compounder proof",
                },
            ],
            "golden_quotes": [
                "Pop Mart is either a platform of spirits or a factory of plastic fads — IP renewal decides.",
                "Labubu globalized the story; the next character globalizes the thesis.",
                "Blind-box scarcity works until SKU flood kills the ritual.",
            ],
            "chronology": {
                "subject": "David · Pop Mart",
                "events": [
                    {"date": "2020", "event": "9992.HK listing; blind-box scale"},
                    {"date": "2023–2024", "event": "Labubu global breakout"},
                    {"date": "2025-06-05", "event": "Ep.125 new-consumer series recorded"},
                    {"date": "2025–2026", "event": "Overseas store expansion accelerates"},
                    {"date": "2026+", "event": "Second global IP validates platform"},
                ],
            },
        },
        "zh": {
            "keywords": ["9992.HK", "泡泡玛特", "IP", "潮玩"],
            "conclusion": "泡泡玛特（9992.HK）节目问美丽泡泡还是塑料茅台——IP 飞轮与盲盒稀缺驱动复购；怀疑者见无 Spirit 深度的 fad SKU。大卫以 IP 更新率与海外同店框复利对泡沫。投资者应观望泡泡玛特（9992.HK）Labubu 级管线与国际店效，非仅中国商场 hype。",
            "background": "投资实战派第 125 期（2025 年 6 月 5 日）新消费系列深度聊泡泡玛特——中国消费上市中独特的 IP 收藏纯标的。大卫将情感溢价比茅台仪式与塑料商品化风险。Labubu 全球破圈考验泡泡玛特是平台还是一次性吉祥物工厂。",
            "important_facts": [
                "IP 复利考验：泡泡玛特（9992.HK）需 recurring 角色命中——观望新 IP 成功率与艺术家管线非仅盲盒收入。Labubu 证全球口味；下一 IP 验证平台论点。",
                "塑料茅台争论：多头见定价权与稀缺机制；空头见 fad 收藏与 landfill 结局。毛利与海外 ASP 分 bubble 与 compounder。",
                "海外第二曲线：国际店抬 mix——投资者跟海外 SSSG 对侨胞游客。失败模式是输出中国 hype 无本地化 Spirit。",
            ],
            "mental_model": {
                "name": "IP 更新率 × 盲盒稀缺 × 海外 SSSG",
                "components": "复利需管线深度非单一吉祥物。盲盒 gamify 分发。全球 SSSG 证 IP 超中国 fad。",
                "application": "泡泡玛特（9992.HK）：观望 Labubu 后 IP 节奏与海外店效——看多论点是全球收藏平台。SKU 泛滥无角色故事则减仓。",
            },
            "key_insights": [
                {
                    "view": "IP 管线枯竭则美丽泡泡。",
                    "question": "主持如何分多空？",
                    "answer": "大卫问泡泡玛特是 Disney 式更新还是塑料 fad——泡泡玛特（9992.HK）多头需第二、第三个全球 IP 胜非 Labubu 外推。",
                },
                {
                    "view": "塑料茅台是稀缺经济学。",
                    "question": "为何比茅台？",
                    "answer": "二者卖仪式与稀缺——茅台喝、泡泡玛特摆。可投资差异是 IP 须更快更新；季度跟命中率。",
                },
                {
                    "view": "海外证全球化。",
                    "question": "现最关键指标？",
                    "answer": "国际同店与本地发售——若海外复购 hold 则 9992.HK 配平台倍数；若仅游客则回归 fad 倍数。",
                },
            ],
            "top_investment_implications": [
                {
                    "ticker": "9992.HK",
                    "direction": "Watch",
                    "confidence": "Medium",
                    "thesis": "泡泡玛特（9992.HK）：泡泡对塑料茅台辩论——观望 IP 管线与海外 SSSG 作复利验证",
                },
            ],
            "golden_quotes": ["占位一", "占位二", "占位三"],
            "chronology": {
                "subject": "大卫 · 泡泡玛特",
                "events": [
                    {"date": "2020", "event": "9992.HK 上市；盲盒规模化"},
                    {"date": "2023–2024", "event": "Labubu 全球破圈"},
                    {"date": "2025-06-05", "event": "第 125 期新消费系列录制"},
                    {"date": "2025–2026", "event": "海外门店扩张加速"},
                    {"date": "2026+", "event": "第二个全球 IP 验证平台"},
                ],
            },
        },
    },
    "tzs-ep133": {
        "en": {
            "keywords": ["605499.SH", "Eastroc Beverage", "Energy Drink", "New Consumer"],
            "conclusion": "Eastroc Beverage (605499.SH) stands out for counter-cyclical high growth — functional energy drink share gains via channel depth and Red Bull alternative positioning in China. David highlights supply-chain and distributor loyalty versus soda giants. Investors should Watch Eastroc (605499.SH) on volume growth, gross margin stability, and east/south China penetration as energy drink TAM expands.",
            "background": "Practical Investments ep.133 (Jul 10, 2025) new-consumer series on Eastroc — China's fast-growing energy drink challenger. Framework: functional beverage user value (energy, focus), aggressive channel rebates, and regional expansion from south China northward. Counter-cyclical growth means consumption downgrade pushes value energy versus coffee; risks are price war and Red Bull trademark dynamics.",
            "important_facts": [
                "Counter-cyclical growth: Eastroc (605499.SH) gained share while macro soft — energy drink occasion resilient for drivers and gig workers. Watch volume and ASP as competitors subsidize shelves.",
                "Channel moat: Distributor depth and freezer placement discipline — similar to Nongfu/soft drink playbook. Investors track dealer inventory and regional penetration, not headline revenue only.",
                "Margin discipline: High growth with improving scale — 605499.SH Watch on gross margin through PET and sugar costs. Underweight if price war erodes rebate economics sustainably.",
            ],
            "mental_model": {
                "name": "Functional Occasion × Channel Depth × Counter-Cyclical Share",
                "components": "Energy drink wins on placement and habit, not brand alone. Distributor loyalty scales regions. Downcycle can boost value functional versus premium coffee.",
                "application": "Eastroc Beverage (605499.SH): Watch northward expansion and margin — Long thesis is national energy #2 with channel compounder. Trim on inventory bloat or rebate war.",
            },
            "key_insights": [
                {
                    "view": "Energy drink is resilient occasion.",
                    "question": "Why counter-cyclical?",
                    "answer": "David notes gig and logistics workers keep functional spend — Eastroc captures Red Bull alternative demand when consumers trade down from Starbucks, not from caffeine.",
                },
                {
                    "view": "Channel beats billboard.",
                    "question": "What is the real moat?",
                    "answer": "Freezer placement and distributor profit sharing — 605499.SH growth is route-to-market story; investors should visit channel inventory health, not only sell-side growth models.",
                },
                {
                    "view": "National expansion is second act.",
                    "question": "What proves compounder vs regional fad?",
                    "answer": "Success north of traditional strongholds — if SSSG and volume hold in new provinces, Eastroc earns national multiple; else remain regional trade.",
                },
            ],
            "top_investment_implications": [
                {
                    "ticker": "605499.SH",
                    "direction": "Watch",
                    "confidence": "Medium",
                    "thesis": "Eastroc Beverage (605499.SH): Counter-cyclical energy drink growth — Watch channel penetration and margin through expansion",
                },
            ],
            "golden_quotes": [
                "Eastroc grew while macro slowed — functional caffeine is a resilient occasion.",
                "Freezer placement and distributor margin are the real energy-drink moat.",
                "National expansion northward is the compounder test, not one hot province.",
            ],
            "chronology": {
                "subject": "David · Eastroc Beverage",
                "events": [
                    {"date": "2021–2023", "event": "Eastroc share gains in south China"},
                    {"date": "2024–2025", "event": "Counter-cyclical revenue acceleration"},
                    {"date": "2025-07-10", "event": "Ep.133 new-consumer series recorded"},
                    {"date": "2025–2026", "event": "North and east China channel push"},
                    {"date": "2026+", "event": "National energy drink oligopoly shapes"},
                ],
            },
        },
        "zh": {
            "keywords": ["605499.SH", "东鹏饮料", "功能饮料", "新消费"],
            "conclusion": "东鹏饮料（605499.SH）以逆势高成长脱颖而出——功能能量饮靠渠道深度与红牛替代定位抢份额。大卫强调供应链与经销商忠诚对汽水巨头。投资者应观望东鹏（605499.SH）量增、毛利稳定与华中华东渗透，随能量饮 TAM 扩大。",
            "background": "投资实战派第 133 期（2025 年 7 月 10 日）新消费系列谈东鹏——中国快速成长能量饮挑战者。框架：功能饮用户价值（提神、专注）、激进渠道返利与华南向北扩张。逆势增长意味消费降级推 value 能量对咖啡；风险是价格战与红牛商标动态。",
            "important_facts": [
                "逆势增长：东鹏饮料（605499.SH）宏观疲软时抢份额——能量饮场景对司机与零工 resilient。竞品补贴货架时观望量与 ASP。",
                "渠道护城河：经销商深度与冰柜占位纪律——类农夫/汽水 playbook。投资者跟经销商库存与区域渗透非仅 headline 收入。",
                "毛利纪律：高增长伴规模改善——东鹏（605499.SH）观望 PET 与糖成本下毛利。返利经济学持续侵蚀则低配。",
            ],
            "mental_model": {
                "name": "功能场景 × 渠道深度 × 逆势份额",
                "components": "能量饮靠占位与习惯胜非仅品牌。经销商忠诚 scale 区域。下行周期可抬 value 功能对 premium 咖啡。",
                "application": "东鹏饮料（605499.SH）：观望北向扩张与毛利——看多论点是全国能量第二与渠道复利。库存 bloating 或返利战则减仓。",
            },
            "key_insights": [
                {
                    "view": "能量饮是 resilient 场景。",
                    "question": "为何逆势？",
                    "answer": "大卫指零工与物流从业者保持功能开支——东鹏捕获红牛替代需求，消费者从星巴克降级非从咖啡因降级。",
                },
                {
                    "view": "渠道胜 billboard。",
                    "question": "真护城河是什么？",
                    "answer": "冰柜占位与经销商利润分享——东鹏（605499.SH）增长是 route-to-market 故事；投资者应看渠道库存健康非仅卖方增长模型。",
                },
                {
                    "view": "全国扩张是第二幕。",
                    "question": "何证复利对区域 fad？",
                    "answer": "传统强势区以北成功——若新省 SSSG 与量 hold 则东鹏得全国倍数；否则仍区域交易。",
                },
            ],
            "top_investment_implications": [
                {
                    "ticker": "605499.SH",
                    "direction": "Watch",
                    "confidence": "Medium",
                    "thesis": "东鹏饮料（605499.SH）：逆势能量饮增长——观望渠道渗透与扩张中毛利",
                },
            ],
            "golden_quotes": ["占位一", "占位二", "占位三"],
            "chronology": {
                "subject": "大卫 · 东鹏饮料",
                "events": [
                    {"date": "2021–2023", "event": "东鹏华南份额提升"},
                    {"date": "2024–2025", "event": "逆势收入加速"},
                    {"date": "2025-07-10", "event": "第 133 期新消费系列录制"},
                    {"date": "2025–2026", "event": "华北华东渠道推进"},
                    {"date": "2026+", "event": "全国能量饮寡头格局成形"},
                ],
            },
        },
    },
    "tzs-ep130": {
        "en": {
            "keywords": ["600519.SZ", "Moutai", "Baijiu", "Distribution"],
            "conclusion": "Zhang Yaqun's 24-year Moutai life as dealer reveals channel reality —批价, relationship capital, and policy cycles shape Kweichow Moutai (600519.SZ) more than factory tours. All-in on Moutai ecosystem taught inventory risk and gift-economy swings. Investors should Watch Kweichow Moutai (600519.SZ) on dealer health, direct-sales mix, and批价 premium as grassroots signal.",
            "background": "Practical Investments ep.130 (Jun 29, 2025) interviews Zhang Yaqun — 24-year Moutai industry veteran and distributor. Oral history: joining dealer system, boom decades, anti-corruption and channel reform shocks, i茅台 digital shift. Zhang humanizes 600519.SZ thesis — brand is religion until批价 cracks; dealers are thermometer.",
            "important_facts": [
                "Dealer thermometer: Zhang Yaqun says批价 and dealer cash flow lead filings — Kweichow Moutai (600519.SZ) investors should track grassroots inventory, not only出厂价 hikes.",
                "24-year cycles: Gift economy and policy swings caused boom-bust in dealer profits — channel reform and i茅台 aim to flatten layers but threaten legacy distributor economics.",
                "All-in conviction: Zhang's life story shows brand loyalty at channel level — supports long-term moat narrative but warns entry price and批价 spread still matter for public investors.",
            ],
            "mental_model": {
                "name": "Dealer批价 × Policy Cycle × Channel Reform",
                "components": "Moutai earnings travel through dealers before filings.批价 is real-time demand. Reform raises transparency, stresses legacy rent.",
                "application": "Kweichow Moutai (600519.SZ): Watch批价 spread and dealer sentiment — Long moat thesis with margin-of-safety on PE. Trim if dealers destock simultaneously with widening discounts.",
            },
            "key_insights": [
                {
                    "view": "Dealers feel demand first.",
                    "question": "What do investors miss without channel voices?",
                    "answer": "Zhang Yaqun notes inventory and批价 move before quarterly reports — 24-year dealer lens is leading indicator for 600519.SZ channel health.",
                },
                {
                    "view": "Channel reform changes rent allocation.",
                    "question": "How does i茅台 matter?",
                    "answer": "Digital direct sales raise transparency and may compress dealer margin — bullish for company control, mixed for批价 volatility during transition.",
                },
                {
                    "view": "Brand religion has cyclical novices.",
                    "question": "Does Zhang confirm moat?",
                    "answer": "Lifetime all-in supports ritual brand — but Zhang lived through downcycles; public investors still need批价 and valuation discipline, not only storytelling.",
                },
            ],
            "top_investment_implications": [
                {
                    "ticker": "600519.SZ",
                    "direction": "Watch",
                    "confidence": "Medium",
                    "thesis": "Kweichow Moutai (600519.SZ): 24-year dealer Zhang Yaqun — Watch批价 and dealer health as grassroots demand signal",
                },
            ],
            "golden_quotes": [
                "Dealers feel the temperature of Moutai before the quarterly report does.",
                "Twenty-four years taught me brand is religion until批价 says otherwise.",
                "Channel reform moves margin from distributors to the factory — watch the spread.",
            ],
            "chronology": {
                "subject": "Zhang Yaqun · Moutai Dealer",
                "events": [
                    {"date": "2000s", "event": "Zhang enters Moutai dealer system"},
                    {"date": "2010s", "event": "Baijiu boom and gift-economy peak"},
                    {"date": "2020s", "event": "Anti-corruption and consumption policy shocks"},
                    {"date": "2023–2025", "event": "i茅台 and channel reform accelerate"},
                    {"date": "2025-06-29", "event": "Ep.130 interview recorded"},
                    {"date": "2026+", "event": "Dealer economics under direct-sales mix"},
                ],
            },
        },
        "zh": {
            "keywords": ["600519.SZ", "茅台", "白酒", "渠道"],
            "conclusion": "张亚群 24 年茅台经销商人生揭示渠道现实——批价、关系资本与政策周期塑造贵州茅台（600519.SZ）胜于工厂参观。All in 茅台生态教会库存风险与送礼经济波动。投资者应观望贵州茅台（600519.SZ）经销商健康、直营占比与批价溢价作草根信号。",
            "background": "投资实战派第 130 期（2025 年 6 月 29 日）访谈张亚群——24 年茅台从业者与经销商。口述史：入经销体系、黄金十年、反腐与渠道改革冲击、i茅台 数字化转型。张亚群人性化 600519.SZ 论点——品牌是宗教直至批价裂缝；经销商是温度计。",
            "important_facts": [
                "经销商温度计：张亚群称批价与经销商现金流领先财报——贵州茅台（600519.SZ）投资者应跟草根库存非仅出厂价上调。",
                "24 年周期：送礼经济与政策摆动致经销商利润 boom-bust——渠道改革与 i茅台 旨在扁平层级但威胁 legacy 分销商经济学。",
                "All in 信念：张亚群人生示渠道层品牌忠诚——支撑长期护城河叙事但警示公开投资者入场价与批价利差仍关键。",
            ],
            "mental_model": {
                "name": "经销商批价 × 政策周期 × 渠道改革",
                "components": "茅台盈利经经销商再到财报。批价是实时需求。改革抬透明度、压 legacy 租金。",
                "application": "贵州茅台（600519.SZ）：观望批价利差与经销商情绪——护城河论点加 PE 安全边际。经销商同步去库存且折价扩大则减仓。",
            },
            "key_insights": [
                {
                    "view": "经销商先感受需求。",
                    "question": "无渠道声音投资者漏什么？",
                    "answer": "张亚群指库存与批价动在季报前——24 年经销商透镜是 600519.SZ 渠道健康领先指标。",
                },
                {
                    "view": "渠道改革改租金分配。",
                    "question": "i茅台 何意？",
                    "answer": "数字直营抬透明度或压经销商毛利——对公司控制利好、过渡期批价波动 mixed。",
                },
                {
                    "view": "品牌宗教有周期信徒。",
                    "question": "张亚群确认护城河吗？",
                    "answer": "终身 all in 支撑仪式品牌——但张经历下行；公开投资者仍要批价与估值纪律非仅故事。",
                },
            ],
            "top_investment_implications": [
                {
                    "ticker": "600519.SZ",
                    "direction": "Watch",
                    "confidence": "Medium",
                    "thesis": "贵州茅台（600519.SZ）：24 年经销商张亚群——观望批价与经销商健康作草根需求信号",
                },
            ],
            "golden_quotes": ["占位一", "占位二", "占位三"],
            "chronology": {
                "subject": "张亚群 · 茅台经销商",
                "events": [
                    {"date": "2000s", "event": "张亚群进入茅台经销体系"},
                    {"date": "2010s", "event": "白酒 boom 与送礼经济峰值"},
                    {"date": "2020s", "event": "反腐与消费政策冲击"},
                    {"date": "2023–2025", "event": "i茅台 与渠道改革加速"},
                    {"date": "2025-06-29", "event": "第 130 期访谈录制"},
                    {"date": "2026+", "event": "直营 mix 下经销商经济学"},
                ],
            },
        },
    },
    "tzs-ep128": {
        "en": {
            "keywords": ["NVDA", "9660.HK", "AD Chips", "Domestic Substitution"],
            "conclusion": "AD chip experts Wang Kang and Luo Huichao map compute war to domestic substitution — NVIDIA (NVDA) leads training and high-end drive; Horizon Robotics (9660.HK) and peers fight for China OEM design wins on cost and compliance. Boom points: end-to-end AD adoption; trap points: commodityization and export controls. Investors should Watch NVDA on auto/data-center mix and 9660.HK on OEM attach versus domestic policy tailwinds.",
            "background": "Practical Investments ep.128 (Jun 22, 2025) with AD chip industry experts covers NVIDIA dominance, Horizon's China OEM path, and domestic substitution politics. Framework: training cloud versus edge inference, functional safety certification, and OEM dual-source strategies. Episode helps investors separate AD silicon hype from design-win revenue.",
            "important_facts": [
                "Compute war layers: NVDA wins cloud training and premium drive Orin-class; 9660.HK competes on China OEM volume with localized support and price — Watch design-win pipeline and SOP timing.",
                "Boom versus trap: End-to-end AD raises chip content per vehicle — boom. Trap is OEM dual-source forcing ASP erosion or policy favoring immature silicon — quality recalls destroy 9660.HK thesis.",
                "Export control overlay: NVDA China revenue risk from restrictions; domestic chips gain policy tailwind but must prove millions-unit quality — investors balance NVDA global AI feast with 9660.HK substitution optionality.",
            ],
            "mental_model": {
                "name": "Training vs Edge × OEM Design-Win × Substitution Policy",
                "components": "NVDA taxes training and premium auto. Domestic edge chips win on OEM dual-source and compliance. Policy accelerates substitution, not quality.",
                "application": "NVIDIA (NVDA): Watch data-center and auto revenue — global AD compute landlord. Horizon Robotics (9660.HK): Watch China OEM attach and margin — Long substitution only with quality-at-scale proof.",
            },
            "key_insights": [
                {
                    "view": "Next boom is edge AD silicon content.",
                    "question": "Where is chip TAM growth?",
                    "answer": "Experts say end-to-end driving raises TOPS per car — NVDA and 9660.HK both benefit if AD ships; difference is share per OEM geography.",
                },
                {
                    "view": "Trap is unqualified domestic win.",
                    "question": "What kills 9660.HK thesis?",
                    "answer": "Policy push without functional safety at scale — recalls or OEM write-offs erase design wins. Wang and Luo stress certification years, not press releases.",
                },
                {
                    "view": "OEMs dual-source by design.",
                    "question": "Can NVDA monopolize auto edge?",
                    "answer": "OEMs fear single-supplier risk — 9660.HK exists in dual-source slot even when NVDA leads performance. Investors track ASP trends under dual awards.",
                },
            ],
            "top_investment_implications": [
                {
                    "ticker": "NVDA",
                    "direction": "Watch",
                    "confidence": "Medium",
                    "thesis": "NVIDIA (NVDA): AD chip compute war — Watch training and premium auto silicon as end-to-end AD scales",
                },
                {
                    "ticker": "9660.HK",
                    "direction": "Watch",
                    "confidence": "Medium",
                    "thesis": "Horizon Robotics (9660.HK): Domestic AD chip substitution — Watch OEM design wins and quality-at-scale versus policy hype",
                },
            ],
            "golden_quotes": [
                "The AD chip boom is real TOPS per car; the trap is shipping silicon without functional safety at scale.",
                "OEMs always dual-source — Horizon lives in the second source slot even when NVIDIA leads.",
                "Domestic substitution is policy tailwind, not a substitute for millions-unit quality.",
            ],
            "chronology": {
                "subject": "Wang Kang & Luo Huichao · AD Chips",
                "events": [
                    {"date": "2020–2023", "event": "China AD chip localization policy accelerates"},
                    {"date": "2024", "event": "End-to-end AD raises OEM silicon content"},
                    {"date": "2025", "event": "NVDA export controls reshape China supply"},
                    {"date": "2025-06-22", "event": "Ep.128 expert conversation recorded"},
                    {"date": "2026+", "event": "OEM SOP awards clarify boom vs trap"},
                ],
            },
        },
        "zh": {
            "keywords": ["NVDA", "9660.HK", "智驾芯片", "国产替代"],
            "conclusion": "智驾芯片专家王康、罗慧超将算力战争映射国产替代——英伟达（NVDA）领训练与高端行车；地平线（9660.HK）等以成本与合规争中国 OEM 设计赢单。爆点：端到端智驾上车；坑点：商品化与出口管制。投资者应观望 NVDA 汽车/数据中心 mix 与地平线（9660.HK）OEM 搭载对国产政策顺风。",
            "background": "投资实战派第 128 期（2025 年 6 月 22 日）与智驾芯片产业专家谈英伟达主导、地平线中国 OEM 路径与国产替代政治。框架：训练云对边缘推理、功能安全认证与 OEM 双源策略。节目帮投资者分离智驾硅 hype 与设计赢单收入。",
            "important_facts": [
                "算力战争分层：NVDA 胜云训练与 premium Orin 级行车；地平线（9660.HK）以中国 OEM 量、本地化支持与价格竞争——观望设计赢单管线与 SOP 时点。",
                "爆点对坑点：端到端智驾抬单车芯片含量——爆点。坑点是 OEM 双源迫 ASP 侵蚀或政策捧不成熟硅——质量召回摧毁 9660.HK 论点。",
                "出口管制叠加：NVDA 中国收入受限制风险；国产芯片享政策顺风但须证百万辆质量——投资者平衡 NVDA 全球 AI 盛宴与 9660.HK 替代期权。",
            ],
            "mental_model": {
                "name": "训练对边缘 × OEM 设计赢单 × 替代政策",
                "components": "NVDA 向训练与 premium 汽车收税。国产边缘芯片以 OEM 双源与合规胜。政策加速替代非质量。",
                "application": "英伟达（NVDA）：观望数据中心与汽车收入——全球智驾算力房东。地平线（9660.HK）：观望中国 OEM 搭载与毛利——仅规模化质量验证时看多替代。",
            },
            "key_insights": [
                {
                    "view": "下一爆点是边缘智驾硅含量。",
                    "question": "芯片 TAM 增长在哪？",
                    "answer": "专家称端到端驾驶抬每车 TOPS——智驾落地则 NVDA 与 9660.HK 皆受益；差异在 OEM 地域份额。",
                },
                {
                    "view": "坑点是未达标国产赢单。",
                    "question": "何杀死 9660.HK 论点？",
                    "answer": "政策推而无规模化功能安全——召回或 OEM 核销抹去设计赢单。王康罗慧超强调认证年数非通稿。",
                },
                {
                    "view": "OEM 天生双源。",
                    "question": "NVDA 能否垄断车端边缘？",
                    "answer": "OEM 惧单一供应商——即使 NVDA 性能领先 9660.HK 占双源槽位。投资者跟双供下 ASP 趋势。",
                },
            ],
            "top_investment_implications": [
                {
                    "ticker": "NVDA",
                    "direction": "Watch",
                    "confidence": "Medium",
                    "thesis": "英伟达（NVDA）：智驾芯片算力战——观望训练与 premium 汽车硅随端到端智驾 scale",
                },
                {
                    "ticker": "9660.HK",
                    "direction": "Watch",
                    "confidence": "Medium",
                    "thesis": "地平线（9660.HK）：国产智驾芯片替代——观望 OEM 设计赢单与规模化质量对政策 hype",
                },
            ],
            "golden_quotes": ["占位一", "占位二", "占位三"],
            "chronology": {
                "subject": "王康、罗慧超 · 智驾芯片",
                "events": [
                    {"date": "2020–2023", "event": "中国智驾芯片国产化政策加速"},
                    {"date": "2024", "event": "端到端智驾抬 OEM 硅含量"},
                    {"date": "2025", "event": "NVDA 出口管制重塑中国供给"},
                    {"date": "2025-06-22", "event": "第 128 期专家对话录制"},
                    {"date": "2026+", "event": "OEM SOP 奖项明朗爆点与坑点"},
                ],
            },
        },
    },
    "tzs-ep116": {
        "en": {
            "keywords": ["NVDA", "GOOGL", "Tech Stocks", "Growth Investing"],
            "conclusion": "Yongqing's 25-year US equity analyst framework for high-growth tech — size positions on durable moat, reinvestment runway, and valuation versus narrative peaks. NVDA and GOOGL exemplify feast landlords; avoid chasing agent wrappers at wrong price. Investors should Watch NVDA on data-center cadence and GOOGL on AI ARPU with position sizing discipline from Curated 50.",
            "background": "Practical Investments ep.116 (May 5, 2025) features Yongqing sharing how a veteran US analyst invests high-growth tech — drawn from 25 years covering semis and internet. Checklist: TAM honesty, gross margin structure, management capital allocation, and multiple discipline. Uses NVDA AI cycle and GOOGL landlord thesis as live examples; warns retail on feast narratives without abacus.",
            "important_facts": [
                "Growth framework: Yongqing ranks moat durability, reinvestment ROI, and entry multiple — NVDA Watch when data-center growth and margin justify capex boom; not every AI name deserves NVDA multiple.",
                "Landlord versus volume: GOOGL distributes AI across Search, Cloud, YouTube — better public risk-reward than pre-revenue agents. Pair with NVDA as compute plus distribution barbell.",
                "Position sizing: Curated 50 discipline — add on mispricing when thesis intact, trim at narrative peak. High-growth tech requires explicit sell rules when growth decelerates or competition erodes margin.",
            ],
            "mental_model": {
                "name": "Moat × Reinvestment Runway × Multiple Discipline",
                "components": "High-growth investing needs three yes: durable edge, capital returns, sane price. Landlords and infra feast; wrappers bubble. Size positions, do not marry stories.",
                "application": "NVIDIA (NVDA): Watch data-center revenue and gross margin — Long only when growth and supply align. Alphabet (GOOGL): Watch AI monetization lift on ads and cloud — barbell versus speculative agents.",
            },
            "key_insights": [
                {
                    "view": "Not every AI stock is NVDA.",
                    "question": "What is Yongqing's core warning?",
                    "answer": "25 years taught him feast narratives overpay mediocrities — apply NVDA/GOOGL checklist to any high-growth name: moat, reinvestment, multiple.",
                },
                {
                    "view": "GOOGL is public AI barbell leg.",
                    "question": "Why pair with NVDA in framework?",
                    "answer": "NVDA is compute feast; GOOGL is distribution landlord — together cover AI stack with liquid large caps. Avoid double-counting same theme in oversized positions.",
                },
                {
                    "view": "Sell rules matter in growth.",
                    "question": "What differs from value investing?",
                    "answer": "Yongqing trims when growth decelerates or competition hits margin even if story sounds intact — high-growth requires faster thesis kill switches than baijiu compounders.",
                },
            ],
            "top_investment_implications": [
                {
                    "ticker": "NVDA",
                    "direction": "Watch",
                    "confidence": "Medium",
                    "thesis": "NVIDIA (NVDA): Yongqing 25-year growth framework — Watch data-center cadence and margin with position sizing discipline",
                },
                {
                    "ticker": "GOOGL",
                    "direction": "Watch",
                    "confidence": "Medium",
                    "thesis": "Alphabet (GOOGL): High-growth tech checklist — Watch AI ARPU on Search and Cloud as public landlord barbell",
                },
            ],
            "golden_quotes": [
                "High-growth tech investing is three questions: moat, reinvestment, and the price you pay.",
                "Not every AI name deserves an NVDA multiple — feast narratives overpay mediocrities.",
                "Pair compute landlords with distribution landlords — and know when to trim both.",
            ],
            "chronology": {
                "subject": "Yongqing · Growth Tech Framework",
                "events": [
                    {"date": "2000s–2010s", "event": "Yongqing US analyst career; semis and internet coverage"},
                    {"date": "2023–2024", "event": "AI feast accelerates; retail FOMO rises"},
                    {"date": "2025", "event": "Curated 50 position discipline formalized"},
                    {"date": "2025-05-05", "event": "Ep.116 framework episode recorded"},
                    {"date": "2026+", "event": "AI growth deceleration tests sell rules"},
                ],
            },
        },
        "zh": {
            "keywords": ["NVDA", "GOOGL", "科技股", "成长投资"],
            "conclusion": "永庆 25 年美股分析师高增长科技股框架——按持久护城河、再投资跑道与估值对叙事峰值建仓。NVDA 与 GOOGL 示范盛宴房东；勿在错价追 agent 套壳。投资者应观望 NVDA 数据中心节奏与 GOOGL AI ARPU，守精选 50 仓位纪律。",
            "background": "投资实战派第 116 期（2025 年 5 月 5 日）永庆分享资深美股分析师如何投高增长科技——源自 25 年覆盖半导体与互联网。清单：TAM 诚实、毛利结构、管理层资本配置与倍数纪律。以 NVDA AI 周期与 GOOGL 房东论点为 live 例；警示散户无算盘追盛宴叙事。",
            "important_facts": [
                "成长框架：永庆排序护城河耐久、再投资 ROI 与入场倍数——数据中心增长与毛利 justify capex boom 时观望 NVDA；非每个 AI 名配 NVDA 倍数。",
                "房东对 volume：GOOGL 在搜索、云、YouTube 分发 AI——较 pre-revenue agent 公开风险回报更佳。与 NVDA 配成算力加分发 barbell。",
                "仓位 sizing：精选 50 纪律——论点完好错价加仓、叙事峰值减仓。高增长科技须明示增长放缓或竞争侵蚀毛利时的卖出规则。",
            ],
            "mental_model": {
                "name": "护城河 × 再投资跑道 × 倍数纪律",
                "components": "高增长投资要三 yes：持久优势、资本回报、合理价。房东与 infra 盛宴；套壳泡沫。定仓位非嫁故事。",
                "application": "英伟达（NVDA）：观望数据中心收入与毛利——增长与供给对齐时看多。Alphabet（GOOGL）：观望广告与云上 AI 变现抬升——对投机 agent 的 barbell。",
            },
            "key_insights": [
                {
                    "view": "非每只 AI 股都是 NVDA。",
                    "question": "永庆核心警示？",
                    "answer": "25 年教盛宴叙事高估 mediocrity——对任何高增长名用 NVDA/GOOGL 清单：护城河、再投资、倍数。",
                },
                {
                    "view": "GOOGL 是公开 AI barbell 腿。",
                    "question": "为何与 NVDA 并提？",
                    "answer": "NVDA 是算力盛宴；GOOGL 是分发房东——合盖 AI 栈流动性大盘。避免同主题超配重复计。",
                },
                {
                    "view": "成长投资要有卖出规则。",
                    "question": "与价值投资何异？",
                    "answer": "永庆在增长放缓或竞争伤毛利时减仓即使故事仍好听——高增长须比白酒复利更快 thesis kill switch。",
                },
            ],
            "top_investment_implications": [
                {
                    "ticker": "NVDA",
                    "direction": "Watch",
                    "confidence": "Medium",
                    "thesis": "英伟达（NVDA）：永庆 25 年成长框架——观望数据中心节奏与毛利守仓位纪律",
                },
                {
                    "ticker": "GOOGL",
                    "direction": "Watch",
                    "confidence": "Medium",
                    "thesis": "Alphabet（GOOGL）：高增长科技清单——观望搜索与云 AI ARPU 作公开房东 barbell",
                },
            ],
            "golden_quotes": ["占位一", "占位二", "占位三"],
            "chronology": {
                "subject": "永庆 · 成长科技框架",
                "events": [
                    {"date": "2000s–2010s", "event": "永庆美股分析师生涯；半导体与互联网覆盖"},
                    {"date": "2023–2024", "event": "AI 盛宴加速；散户 FOMO 升"},
                    {"date": "2025", "event": "精选 50 仓位纪律成型"},
                    {"date": "2025-05-05", "event": "第 116 期框架节目录制"},
                    {"date": "2026+", "event": "AI 增长放缓考验卖出规则"},
                ],
            },
        },
    },
    "tzs-ep166": {
        "en": {
            "keywords": ["BABA", "PDD", "Consumer Internet", "Review"],
            "conclusion": "David and industry expert Teacher X replay 25 years of China consumer internet and 2026 outlook — mobile payment to super-apps to AI-augmented commerce. Alibaba (BABA) fights turnaround and cloud AI; PDD holds efficiency moat with Temu friction. Investors should Watch BABA on core commerce margin and cloud AI, and PDD on domestic take rate versus Temu unit economics.",
            "background": "Practical Investments ep.166 (Jan 12, 2026) — David dialogues with consumer/internet veteran on quarter-century arc: PC portal, mobile social commerce, livestream, and AI tools reshaping discovery. 2026 outlook: consumption分级, platform regulation stable, and overseas expansion costs. BABA and PDD positioned as two investable poles — asset-heavy turnaround vs efficient attacker.",
            "important_facts": [
                "25-year arc: Teacher X maps Alibaba ecosystem maturity versus PDD insurgent efficiency — BABA Watch on GMV stabilization and cloud AI contribution; PDD Watch on wallet share and Temu profitability per market.",
                "2026 consumption:分级 persists — premium and value platforms coexist; do not treat China consumer internet as single beta. BABA benefits if enterprise and cloud AI monetize; PDD if domestic moat holds while Temu losses cap.",
                "Investable poles: Alibaba (BABA) — sum-of-parts on commerce plus cloud; Pinduoduo (PDD) — supply-chain flywheel with rising compliance strike on Temu. Avoid binary China internet bet without unit economics.",
            ],
            "mental_model": {
                "name": "Platform Era Arc × 2026分级 × Commerce vs Cloud AI",
                "components": "Consumer internet matured from traffic growth to efficiency wars. 2026 is分级 consumption plus AI tools. BABA is turnaround plus cloud; PDD is attack plus Temu option.",
                "application": "Alibaba (BABA): Watch commerce EBIT recovery and cloud AI revenue — Long requires visible turnaround metrics. Pinduoduo (PDD): Watch take rate and Temu unit economics — trim if subsidy war erodes domestic moat.",
            },
            "key_insights": [
                {
                    "view": "Consumer internet entered efficiency war.",
                    "question": "What changed over 25 years?",
                    "answer": "Teacher X says traffic feast ended — winners optimize supply chain and AI discovery. BABA must prove org turnaround; PDD must prove Temu does not destroy domestic margin.",
                },
                {
                    "view": "2026 is分级, not collapse.",
                    "question": "How bullish is outlook?",
                    "answer": "Consumption splits premium and value — both BABA and PDD can coexist if thesis matches segment. Investors avoid one-size China internet short or long.",
                },
                {
                    "view": "AI augments commerce, not replaces platforms.",
                    "question": "Where does AI fit 2026?",
                    "answer": "Discovery, merchant tools, and cloud APIs — BABA cloud AI is re-rating lever; PDD uses AI internally for matching efficiency. Watch monetization, not model press releases.",
                },
            ],
            "top_investment_implications": [
                {
                    "ticker": "BABA",
                    "direction": "Watch",
                    "confidence": "Medium",
                    "thesis": "Alibaba (BABA): 25-year consumer internet review — Watch commerce margin recovery and cloud AI as 2026 turnaround proof",
                },
                {
                    "ticker": "PDD",
                    "direction": "Watch",
                    "confidence": "Medium",
                    "thesis": "Pinduoduo (PDD): 2026 outlook — Watch domestic take rate and Temu unit economics versus efficiency moat",
                },
            ],
            "golden_quotes": [
                "Twenty-five years of consumer internet ended the traffic feast — now it is efficiency and AI.",
                "2026 China consumption is分级 — premium and value platforms can both win their lane.",
                "Alibaba must show turnaround numbers; PDD must show Temu is not eating the domestic moat.",
            ],
            "chronology": {
                "subject": "David · Consumer Internet 25Y",
                "events": [
                    {"date": "2000s", "event": "PC portal and early e-commerce era"},
                    {"date": "2010s", "event": "Mobile payment and super-app rise"},
                    {"date": "2020s", "event": "PDD insurgency; BABA regulation and restructuring"},
                    {"date": "2025", "event": "AI commerce tools accelerate"},
                    {"date": "2026-01-12", "event": "Ep.166 review and 2026 outlook recorded"},
                    {"date": "2026+", "event": "BABA turnaround vs PDD Temu tests"},
                ],
            },
        },
        "zh": {
            "keywords": ["BABA", "PDD", "消费互联网", "复盘"],
            "conclusion": "大卫与产业专家小 X 老师复盘 25 年中国消费互联网与 2026 展望——移动支付到超级应用到 AI 增强电商。阿里巴巴（BABA）攻坚 turnaround 与云 AI；拼多多（PDD）守效率护城河伴 Temu 摩擦。投资者应观望 BABA 核心电商毛利与云 AI，以及 PDD 国内抽佣对 Temu 单位经济学。",
            "background": "投资实战派第 166 期（2026 年 1 月 12 日）——大卫与消费互联网老兵对话四分之一世纪弧：PC 门户、移动社交电商、直播与 AI 工具重塑发现。2026 展望：消费分级、平台监管趋稳与出海成本。BABA 与 PDD 定位为可投资两极——重资产 turnaround 对高效进攻者。",
            "important_facts": [
                "25 年弧：小 X 老师映射阿里生态成熟对 PDD 进攻型效率——BABA 观望 GMV 企稳与云 AI 贡献；PDD 观望钱包份额与分市场 Temu 盈利。",
                "2026 消费：分级持续——高端与 value 平台共存；勿将中国消费互联网当单一 beta。BABA 受益若企业服与云 AI 变现；PDD 若国内护城河 hold 且 Temu 亏损 cap。",
                "可投资两极：阿里巴巴（BABA）——电商加云分部估值；拼多多（PDD）——供应链飞轮伴 Temu 合规行权价升。无单位经济学勿二元中国互联网赌注。",
            ],
            "mental_model": {
                "name": "平台时代弧 × 2026 分级 × 电商对云 AI",
                "components": "消费互联网从流量增长成熟到效率战。2026 是分级消费加 AI 工具。BABA 是 turnaround 加云；PDD 是进攻加 Temu 期权。",
                "application": "阿里巴巴（BABA）：观望电商 EBIT 复苏与云 AI 收入——看多须可见 turnaround 指标。拼多多（PDD）：观望抽佣与 Temu 单位经济学——补贴战侵蚀国内护城河则减仓。",
            },
            "key_insights": [
                {
                    "view": "消费互联网进入效率战。",
                    "question": "25 年何变？",
                    "answer": "小 X 老师称流量盛宴结束——赢家优化供应链与 AI 发现。BABA 须证组织 turnaround；PDD 须证 Temu 不毁国内毛利。",
                },
                {
                    "view": "2026 是分级非崩坏。",
                    "question": "展望多乐观？",
                    "answer": "消费分 premium 与 value——BABA 与 PDD 若论点匹配细分可共存。投资者避免一刀切中国互联网多空。",
                },
                {
                    "view": "AI 增强电商非取代平台。",
                    "question": "AI 在 2026 何位？",
                    "answer": "发现、商家工具与云 API——BABA 云 AI 是重估杠杆；PDD 内部用 AI 提匹配效率。观望变现非模型通稿。",
                },
            ],
            "top_investment_implications": [
                {
                    "ticker": "BABA",
                    "direction": "Watch",
                    "confidence": "Medium",
                    "thesis": "阿里巴巴（BABA）：25 年消费互联网复盘——观望电商毛利复苏与云 AI 作 2026 turnaround 验证",
                },
                {
                    "ticker": "PDD",
                    "direction": "Watch",
                    "confidence": "Medium",
                    "thesis": "拼多多（PDD）：2026 展望——观望国内抽佣与 Temu 单位经济学对效率护城河",
                },
            ],
            "golden_quotes": ["占位一", "占位二", "占位三"],
            "chronology": {
                "subject": "大卫 · 消费互联网 25 年",
                "events": [
                    {"date": "2000s", "event": "PC 门户与早期电商"},
                    {"date": "2010s", "event": "移动支付与超级应用崛起"},
                    {"date": "2020s", "event": "PDD 崛起；BABA 监管与重组"},
                    {"date": "2025", "event": "AI 电商工具加速"},
                    {"date": "2026-01-12", "event": "第 166 期复盘与 2026 展望录制"},
                    {"date": "2026+", "event": "BABA turnaround 对 PDD Temu 考验"},
                ],
            },
        },
    },
    "tzs-ep165": {
        "en": {
            "keywords": ["600519.SZ", "Baijiu", "Snacks", "Distribution"],
            "conclusion": "Ma Zheng's consumer framework on baijiu and snacks stresses user value and channel revolution — products must earn shelf space through repeat utility, not rebates alone. Moutai (600519.SZ) is ritual user value; snacks win on flavor retention and DTC mix. Investors should Watch Kweichow Moutai (600519.SZ) on批价 and young-user substitution as channel digitalization reshapes liquor and food.",
            "background": "Practical Investments ep.165 (Jan 4, 2026) — Yongqing talks with consumer investor Ma Zheng on baijiu versus snack foods. Framework: user value (why consumer repurchases), channel revolution (DTC, membership, convenience stores), and margin structure. Baijiu ritual versus snack habit frequency — 600519.SZ faces generational headwind; snacks face intense SKU competition.",
            "important_facts": [
                "User value lens: Ma Zheng defines investable consumer as repeat utility — Moutai (600519.SZ) ritual and gift occasion; snacks need taste retention and package innovation at convenience price points.",
                "Channel revolution: Traditional dealer layers compress — i茅台 and snack DTC/test channels shift margin allocation. Watch 600519.SZ direct mix; snack names on convenience store penetration.",
                "Baijiu versus snacks: Lower frequency baijiu relies on pricing power; snacks need volume and channel efficiency — do not apply same multiple framework; 600519.SZ is quality anchor in episode's liquor discussion.",
            ],
            "mental_model": {
                "name": "User Value × Channel Revolution × Frequency Economics",
                "components": "Consumer moat is repurchase reason. Channels digitize and flatten. Baijiu is low-frequency pricing power; snacks are high-frequency execution.",
                "application": "Kweichow Moutai (600519.SZ): Watch批价 and youth substitution — Long moat with valuation discipline. Snack exposure via private names; listed anchor remains Moutai for liquor user-value benchmark.",
            },
            "key_insights": [
                {
                    "view": "User value beats channel rebates.",
                    "question": "What is Ma Zheng's first filter?",
                    "answer": "If consumer cannot articulate why they repurchase, model is rebate-driven fragile — Moutai passes on ritual; weak snacks fail when subsidies end.",
                },
                {
                    "view": "Channel revolution reallocates margin.",
                    "question": "How does digital hurt/help 600519.SZ?",
                    "answer": "i茅台 raises transparency and may stabilize出厂价 control — hurts dealer rent, helps company capture margin if demand holds.",
                },
                {
                    "view": "Baijiu and snacks are different animals.",
                    "question": "Why discuss together?",
                    "answer": "Same channel revolution theme — investors learn not to port snack turnover metrics onto baijiu PE; 600519.SZ stays pricing-power compounder with demographic risk.",
                },
            ],
            "top_investment_implications": [
                {
                    "ticker": "600519.SZ",
                    "direction": "Watch",
                    "confidence": "Medium",
                    "thesis": "Kweichow Moutai (600519.SZ): Ma Zheng user-value framework — Watch批价 and channel revolution as ritual brand meets generational shift",
                },
            ],
            "golden_quotes": [
                "User value is why they come back — rebates only rent shelf space temporarily.",
                "Channel revolution moves margin from layers to whoever owns the consumer relationship.",
                "Baijiu is ritual frequency; snacks are habit frequency — never swap their valuation lenses.",
            ],
            "chronology": {
                "subject": "Ma Zheng · Consumer User Value",
                "events": [
                    {"date": "2020s", "event": "Snack DTC and convenience channel rise"},
                    {"date": "2023–2025", "event": "i茅台 accelerates baijiu channel shift"},
                    {"date": "2025", "event": "Young consumer baijiu substitution debates"},
                    {"date": "2026-01-04", "event": "Ep.165 Yongqing-Ma Zheng talk recorded"},
                    {"date": "2026+", "event": "Channel digitalization across liquor and snacks"},
                ],
            },
        },
        "zh": {
            "keywords": ["600519.SZ", "白酒", "休闲食品", "渠道"],
            "conclusion": "马铮消费品框架论白酒与休闲零食强调用户价值与渠道革命——产品须以重复效用赢货架非仅返利。贵州茅台（600519.SZ）是仪式用户价值；零食以口味留存与 DTC mix 胜。投资者应观望贵州茅台（600519.SZ）批价与年轻用户替代，随渠道数字化重塑酒与食。",
            "background": "投资实战派第 165 期（2026 年 1 月 4 日）——永庆与消费品投资人马铮谈白酒对零食。框架：用户价值（消费者为何复购）、渠道革命（DTC、会员、便利店）与毛利结构。白酒仪式对零食习惯频次——600519.SZ 面临代际逆风；零食面临激烈 SKU 竞争。",
            "important_facts": [
                "用户价值透镜：马铮定义可投资消费为重复效用——贵州茅台（600519.SZ）仪式与送礼场景；零食需口味留存与便利价位包装创新。",
                "渠道革命：传统经销商层级压缩——i茅台 与零食 DTC/测试渠道移毛利分配。观望 600519.SZ 直营 mix；零食名看便利店渗透。",
                "白酒对零食：低频白酒靠定价权；零食要量与渠道效率——勿套用同一倍数框架；600519.SZ 是节目酒类讨论的质量锚。",
            ],
            "mental_model": {
                "name": "用户价值 × 渠道革命 × 频次经济学",
                "components": "消费护城河是复购理由。渠道数字化扁平化。白酒低频定价权；零食高频执行。",
                "application": "贵州茅台（600519.SZ）：观望批价与年轻替代——护城河加估值纪律看多。零食敞口多在私有；上市锚仍是茅台作酒类用户价值基准。",
            },
            "key_insights": [
                {
                    "view": "用户价值胜渠道返利。",
                    "question": "马铮第一滤镜？",
                    "answer": "若消费者说不清为何复购则模型靠返利脆弱——茅台过仪式关；弱零食补贴结束即败。",
                },
                {
                    "view": "渠道革命重分毛利。",
                    "question": "数字化如何伤/助 600519.SZ？",
                    "answer": "i茅台 抬透明度或稳出厂价控制——伤经销商租金、需求 hold 则公司捕获毛利。",
                },
                {
                    "view": "白酒与零食不同物种。",
                    "question": "为何放一起谈？",
                    "answer": "同渠道革命主题——投资者学勿把零食周转指标 port 到白酒 PE；600519.SZ 仍是定价权复利器伴人口风险。",
                },
            ],
            "top_investment_implications": [
                {
                    "ticker": "600519.SZ",
                    "direction": "Watch",
                    "confidence": "Medium",
                    "thesis": "贵州茅台（600519.SZ）：马铮用户价值框架——观望批价与渠道革命作仪式品牌遇代际变迁",
                },
            ],
            "golden_quotes": ["占位一", "占位二", "占位三"],
            "chronology": {
                "subject": "马铮 · 消费用户价值",
                "events": [
                    {"date": "2020s", "event": "零食 DTC 与便利店渠道崛起"},
                    {"date": "2023–2025", "event": "i茅台 加速白酒渠道变迁"},
                    {"date": "2025", "event": "年轻消费者白酒替代争论"},
                    {"date": "2026-01-04", "event": "第 165 期永庆马铮对话录制"},
                    {"date": "2026+", "event": "酒食渠道数字化纵深"},
                ],
            },
        },
    },
    "tzs-ep137": {
        "en": {
            "keywords": ["9633.HK", "2020.HK", "000333.SZ", "Distribution"],
            "conclusion": "Wen Yongsheng decodes channel winning codes behind Nongfu Spring (9633.HK), Midea (000333.SZ), and Anta (2020.HK) — deep distribution, dealer profit sharing, and category leadership beat ad spend alone. Each model differs: beverage freezer war, appliance tier-one network, sports DTC blend. Investors should Watch 9633.HK on beverage share and margin, 000333.SZ on overseas plus ToB mix, and 2020.HK on DTC and multi-brand synergy.",
            "background": "Practical Investments ep.137 (Jul 24, 2025) interviews distribution expert Wen Yongsheng on three consumer champions. Nongfu wins route-to-market and minerality brand; Midea leverages dealer grid and supply chain for appliances; Anta blends Anta/Fila brands with retail control. Episode teaches channel as moat — investors map ticker-specific KPIs, not generic 'China consumer' beta.",
            "important_facts": [
                "Nongfu (9633.HK): Freezer placement and water source narrative — beverage channel war is physical availability. Watch volume mix, packaging innovation, and competitor tea/water pressure on margin.",
                "Midea (000333.SZ): Tier-one dealer network and global OEM-to-brand shift — Watch overseas revenue and ToB robotics/ HVAC mix diversifying consumer cycle risk.",
                "Anta (2020.HK): Multi-brand sports retail with DTC rise — Watch Fila recovery, outdoor brands integration, and inventory discipline across franchise/direct stores.",
            ],
            "mental_model": {
                "name": "Route-to-Market Depth × Dealer Incentives × Category Leadership",
                "components": "Consumer moat is trucks and freezers, not slogans. Dealers stay loyal when profitable. Each ticker optimizes different channel physics.",
                "application": "Nongfu Spring (9633.HK): Watch placement and premium water share — compounder if channel depth holds. Midea (000333.SZ): Watch export and ToB — industrial diversification reduces pure consumer beta. Anta (2020.HK): Watch DTC mix and brand portfolio synergy.",
            },
            "key_insights": [
                {
                    "view": "Channel is the product in FMCG.",
                    "question": "What unifies the three companies?",
                    "answer": "Wen Yongsheng argues winning distribution beats ad — Nongfu freezers, Midea dealers, Anta stores are moat assets investors must KPI separately per ticker.",
                },
                {
                    "view": "Dealer profit sharing sustains loyalty.",
                    "question": "Why do networks not defect?",
                    "answer": "Each model shares margin so dealers push SKU — when rebates compress, watch inventory and sell-through before revenue headlines.",
                },
                {
                    "view": "Three tickers, three channel physics.",
                    "question": "Should investors basket them?",
                    "answer": "No — 9633.HK is beverage placement, 000333.SZ is appliance supply chain global, 2020.HK is sports brand retail. Same lesson, different unit economics and cyclicality.",
                },
            ],
            "top_investment_implications": [
                {
                    "ticker": "9633.HK",
                    "direction": "Watch",
                    "confidence": "Medium",
                    "thesis": "Nongfu Spring (9633.HK): Wen Yongsheng channel secrets — Watch freezer war share and beverage margin stability",
                },
                {
                    "ticker": "000333.SZ",
                    "direction": "Watch",
                    "confidence": "Medium",
                    "thesis": "Midea (000333.SZ): Dealer grid and global expansion — Watch overseas and ToB mix diversifying consumer cycle",
                },
                {
                    "ticker": "2020.HK",
                    "direction": "Watch",
                    "confidence": "Medium",
                    "thesis": "Anta Sports (2020.HK): Multi-brand DTC blend — Watch Fila and outdoor portfolio synergy with retail control",
                },
            ],
            "golden_quotes": [
                "In FMCG, the freezer and the truck are the product — not the slogan.",
                "Dealers stay when they earn; channel moats die when rebates lie.",
                "Nongfu, Midea, and Anta win three different channel games — never basket them as one consumer trade.",
            ],
            "chronology": {
                "subject": "Wen Yongsheng · Channel Secrets",
                "events": [
                    {"date": "2010s", "event": "Nongfu, Midea, Anta scale distribution moats"},
                    {"date": "2020s", "event": "DTC and digital tools augment dealer networks"},
                    {"date": "2024–2025", "event": "Beverage and sports competition intensifies"},
                    {"date": "2025-07-24", "event": "Ep.137 Wen Yongsheng interview recorded"},
                    {"date": "2026+", "event": "Channel KPIs test per-ticker theses"},
                ],
            },
        },
        "zh": {
            "keywords": ["9633.HK", "2020.HK", "000333.SZ", "渠道"],
            "conclusion": "文永生解读农夫山泉（9633.HK）、美的（000333.SZ）、安踏（2020.HK）背后渠道制胜密码——深度分销、经销商利润分享与品类 leadership 胜单纯广告。模式各异：饮料冰柜战、家电一线网络、运动 DTC 混合。投资者应观望农夫山泉（9633.HK）饮料份额与毛利、美的（000333.SZ）海外与 ToB mix、安踏（2020.HK）DTC 与多品牌协同。",
            "background": "投资实战派第 137 期（2025 年 7 月 24 日）访谈渠道专家文永生论三大消费冠军。农夫以 route-to-market 与水源叙事胜；美的以经销商网格与供应链胜家电；安踏以 Anta/Fila 品牌与零售控制混合。节目教渠道即护城河——投资者映射分标的 KPI，非泛化「中国消费」beta。",
            "important_facts": [
                "农夫山泉（9633.HK）：冰柜占位与水源叙事——饮料渠道战是物理可得性。观望量 mix、包装创新与茶饮/水竞品对毛利压力。",
                "美的（000333.SZ）：一线经销商网络与全球 OEM 向品牌转型——观望海外收入与 ToB 机器人/暖通 mix 分散消费周期风险。",
                "安踏（2020.HK）：多品牌运动零售伴 DTC 升——观望 Fila 复苏、户外品牌整合与加盟/直营库存纪律。",
            ],
            "mental_model": {
                "name": "Route-to-Market 深度 × 经销商激励 × 品类 Leadership",
                "components": "消费护城河是车队与冰柜非 slogan。经销商赚钱则忠诚。各标的优化不同渠道物理。",
                "application": "农夫山泉（9633.HK）：观望占位与 premium 水份额——渠道深度 hold 则复利。美的（000333.SZ）：观望出口与 ToB——工业多元化降纯消费 beta。安踏（2020.HK）：观望 DTC mix 与品牌组合协同。",
            },
            "key_insights": [
                {
                    "view": "快消渠道即产品。",
                    "question": "三家公司何共性？",
                    "answer": "文永生称赢分销胜广告——农夫冰柜、美的经销商、安踏门店是护城河资产，投资者须分标的 KPI。",
                },
                {
                    "view": "经销商分利维系忠诚。",
                    "question": "网络为何不叛逃？",
                    "answer": "各模式分享毛利使经销商推 SKU——返利压缩时先看库存与动销再信收入 headline。",
                },
                {
                    "view": "三标的、三种渠道物理。",
                    "question": "投资者该 basket 吗？",
                    "answer": "否——9633.HK 是饮料占位、000333.SZ 是全球家电供应链、2020.HK 是运动品牌零售。同课不同单位经济学与周期性。",
                },
            ],
            "top_investment_implications": [
                {
                    "ticker": "9633.HK",
                    "direction": "Watch",
                    "confidence": "Medium",
                    "thesis": "农夫山泉（9633.HK）：文永生渠道密码——观望冰柜战份额与饮料毛利稳定",
                },
                {
                    "ticker": "000333.SZ",
                    "direction": "Watch",
                    "confidence": "Medium",
                    "thesis": "美的（000333.SZ）：经销商网格与全球扩张——观望海外与 ToB mix 分散消费周期",
                },
                {
                    "ticker": "2020.HK",
                    "direction": "Watch",
                    "confidence": "Medium",
                    "thesis": "安踏体育（2020.HK）：多品牌 DTC 混合——观望 Fila 与户外组合协同及零售控制",
                },
            ],
            "golden_quotes": ["占位一", "占位二", "占位三"],
            "chronology": {
                "subject": "文永生 · 渠道密码",
                "events": [
                    {"date": "2010s", "event": "农夫、美的、安踏规模化分销护城河"},
                    {"date": "2020s", "event": "DTC 与数字化工具增强经销商网络"},
                    {"date": "2024–2025", "event": "饮料与运动竞争加剧"},
                    {"date": "2025-07-24", "event": "第 137 期文永生访谈录制"},
                    {"date": "2026+", "event": "分标的渠道 KPI 考验论点"},
                ],
            },
        },
    },
}
