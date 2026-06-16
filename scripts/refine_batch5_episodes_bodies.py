"""Body content for 10 batch-5 Chinese podcast episodes (imported by refine_chinese_pilot_bodies)."""

from __future__ import annotations

from typing import Any

BATCH5_EPISODES: dict[str, dict[str, dict[str, Any]]] = {
    "zj-ep118": {
        "en": {
            "keywords": ["LI", "CEO LLM", "MoE", "VLA"],
            "conclusion": "Li Xiang frames himself as a CEO MoE — technical, product, and org experts — and bets on Agent OS within five years, not a universal agent. AI must graduate from information and assistive tools to production tools users pay for; Li Auto trains domain VLA with 3.2B eight-expert MoE after embracing DeepSeek. Investors should Watch Li Auto (LI) on VLA fleet rollout and Agent OS monetization before treating chat copilots as autonomy proof.",
            "background": "Zhang Xiaojun's second three-hour AI Talk with Li Xiang (Oct 2025 full cut) treats the CEO as an MoE model — routing questions to technical, product, and organization experts. Li argues humans are smaller models optimized for entropy reduction; AI excels at scale but today's chat products remain information tools that rarely cut work hours. Production tools require action, willingness-to-pay, and domain data — Cursor and Deep Research are early examples. Post-DeepSeek, Li Auto reorganized: Lang models plus Agent OS for office work, end-to-end VL for Li Xiang assistant, and VLA for driving and factory robots. VLA training stacks pretrain (V/L/VL joint data), post-train imitation (driving-school analogy), and RL plus world-model data — 3.2B MoE distilled for Orin-X and Thor-U. Scale sits at the center; org changes only when user demand meets tech.",
            "important_facts": [
                "CEO as MoE: Li Xiang says Zhang Xiaojun invoked three experts — technical, product, organization — mirroring mixture-of-experts. DeepSeek V3's 671B MoE validated research-first pipeline: research → R&D → capability expression → business value. Li Auto applies the same to end-to-end, VLM, and VLA — foreign autonomy papers cite Li's driving research.",
                "Agent OS vs universal agent: Li rejects a general agent within five years; Agent OS — like iOS after Mac — will orchestrate tools. Three model lines: Lang + Agent OS for internal productivity; end-to-end VL for in-car and phone multimodal assistant; VLA for autonomy and robots. Post-DeepSeek January decision accelerated VLA versus prior roadmap; CTO reporting shifted so foundation-model teams serve distinct businesses like Qwen/OpenAI splits.",
                "VLA stack investable: Pretrain builds 3.2B eight-expert MoE (cloud retains full model); post-train adds Action via imitation learning (~4B); RLHF plus pure RL on world-model data targets comfort, collision avoidance, and traffic rules. Short CoT (two–three steps) for latency. Li Auto (LI) Watch — VLA ship speed and fleet miles prove domain-data moat; failure mode is treating open-weight Lang as sufficient for 3D vehicle semantics.",
            ],
            "mental_model": {
                "name": "CEO MoE × Tool Tiering × Domain VLA",
                "components": "MoE routes expertise — CEOs must not single-thread decisions. AI products tier: information (reference), assistive (better UX), production (paid action). Agent OS wins before universal agent; VLA needs vehicle traffic semantics open models lack.",
                "application": "Li Auto (LI): Watch VLA deployment cadence and paid Agent OS signals — production-tool test is willingness-to-pay, not demo miles. Compare Tesla FSD data scale; overweight if 3.2B MoE on-vehicle inference ships with transparent attention UX. Underweight if org chases generic LLM without user-demand trigger.",
            },
            "key_insights": [
                {
                    "view": "No universal agent — Agent OS within five years.",
                    "question": "Why does Li reject a general agent timeline?",
                    "answer": "Apple had Mac and ecosystem before iPhone — Li sees Agent OS as orchestration layer calling tools, not one model for everything. Manus steps toward production tools via SEC browsing and analyst reports, but breadth without domain data fails. Cars need VLA with 3D/high-res V tokens and traffic semantics — data OpenAI and DeepSeek do not train on.",
                },
                {
                    "view": "Production tools need action and payment.",
                    "question": "Why are work hours still rising with AI?",
                    "answer": "Chat AI must emit next-token answers — often entropy-increasing when indexed web is wrong. Assistive ADAS and voice nav help but do not replace KPI work. Production tools act on your behalf; colleagues self-pay for Cursor and Deep Research — Li's litmus test. Without action, even O3-level reasoning stays strategy slides, not output.",
                },
                {
                    "view": "DeepSeek accelerated Li Auto's model bet.",
                    "question": "What changed after DeepSeek?",
                    "answer": "January decision to build on open weights like Linux vs Android — Lang plus Agent OS internally, proprietary VLA for driving. Research-first MoE discipline from DeepSeek V3; Wan Zheng pushed VLA and multimodal acceleration harder than Li expected. Reorg aligned three model streams to three businesses — foundation models are infrastructure, not one chat bot.",
                },
            ],
            "top_investment_implications": [
                {
                    "ticker": "LI",
                    "direction": "Watch",
                    "confidence": "Medium",
                    "thesis": "Li Auto (LI): Li Xiang CEO-MoE, Agent OS, and domain VLA 3.2B MoE stack — Watch fleet VLA rollout and production-tool monetization as autonomy proof",
                },
            ],
            "golden_quotes": [
                "我觉得五年之内没有通用Agent，会有一个Agent OS。",
                "我觉得人工智能变成生产工具，然后才是真正人工智能爆发的时刻。",
                "MoE是个非常好的架构，它相当于一堆专家组合在一起。",
            ],
            "chronology": {
                "subject": "Li Xiang · Li Auto AI Talk S2",
                "events": [
                    {"date": "2024-04", "event": "First AI Talk season; Li Auto AI strategy public"},
                    {"date": "2025-01", "event": "Post-DeepSeek decision to build Lang + Agent OS and domain VLA"},
                    {"date": "2025", "event": "CTO reporting change; VLA acceleration vs prior plan"},
                    {"date": "2025", "event": "3.2B eight-expert MoE VLA pipeline: pretrain, imitation, RL"},
                    {"date": "2025-10-30", "event": "Second three-hour AI Talk recorded (full cut published later)"},
                    {"date": "2026+", "event": "Agent OS and VLA fleet deployment targets"},
                ],
            },
        },
        "zh": {
            "keywords": ["LI", "CEO大模型", "MoE", "VLA"],
            "conclusion": "李想将自身框为 CEO 大模型 MoE——技术、产品、组织专家——押注五年内出现 Agent OS 而非通用 Agent。AI 须从信息工具、辅助工具升级为愿付费的生产工具；理想在拥抱 DeepSeek 后自研领域 VLA，端侧 3.2B 八专家 MoE。投资者应观望理想（LI）VLA 车队落地与 Agent OS 变现，勿将聊天 Copilot 当作自动驾驶验证。",
            "background": "张小珺与李想第二次三小时 AI Talk（2025 年 10 月完整版）将 CEO 视作 MoE——向技术、产品、组织专家路由。李想称人类是更小的模型、擅长减熵；AI 擅长大规模信息但今日聊天产品仍是信息工具，工作时长未减。生产工具需行动、付费意愿与领域数据——Cursor 与 Deep Research 是早期样例。DeepSeek 后理想重组：办公 Lang 加 Agent OS、车机手机端端 VL、驾驶与工厂 VLA。VLA 训练分预训练（V/L/VL 联合）、后训练模仿（驾校类比）、RL 与世界模型数据——3.2B MoE 蒸馏上 Orin-X 与 Thor-U。规模居中；仅当用户需求与技术交汇时才调组织。",
            "important_facts": [
                "CEO 即 MoE：李想称张小珺调用技术、产品、组织三位专家，镜像混合专家。DeepSeek V3 的 671B MoE 验证研究优先流水线：研究→研发→能力表达→业务价值。理想用于端端、VLM、VLA——海外自动驾驶论文引用理想驾驶研究。",
                "Agent OS 对通用 Agent：李想否定五年内通用 Agent；Agent OS 如 Mac 之后的 iOS 编排工具。三条模型线：Lang 加 Agent OS 对内生产力；端端 VL 做车机手机多模态；VLA 做自动驾驶与机器人。DeepSeek 后一月决策加速 VLA 相对原路线图；CTO 汇报调整使基础模型团队服务不同业务，如通义/OpenAI 分拆。",
                "VLA 栈可投资：预训练建 3.2B 八专家 MoE（云端保留全模型）；后训练以模仿学习加 Action（约 4B）；RLHF 加纯 RL 用世界模型数据瞄准舒适、避碰与交规。短 CoT 两三步控延迟。理想（LI）观望——VLA 交付速度与车队里程证领域数据护城河；失败模式是把开源 Lang 当足够覆盖 3D 车况语义。",
            ],
            "mental_model": {
                "name": "CEO MoE × 工具分层 × 领域 VLA",
                "components": "MoE 路由专长——CEO 勿单线程决策。AI 产品分层：信息（参考）、辅助（体验）、生产（付费行动）。Agent OS 先于通用 Agent；VLA 需开源模型没有的车域交通语义。",
                "application": "理想（LI）：观望 VLA 部署节奏与付费 Agent OS 信号——生产工具试金石是付费意愿非 demo 里程。对比特斯拉 FSD 数据规模；若 3.2B MoE 上车且 attention 交互透明则超配。若组织追逐通用 LLM 而无用户需求触发则低配。",
            },
            "key_insights": [
                {
                    "view": "无通用 Agent——五年内 Agent OS。",
                    "question": "李想为何否定通用 Agent 时间表？",
                    "answer": "苹果先有 Mac 与生态再有 iPhone——李想见 Agent OS 为调用工具的编排层非一模型包打天下。Manus 经浏览 SEC 与投行报告迈向生产工具，但无领域数据的广度会失败。车需带 3D/高清 V token 与交通语义的 VLA——OpenAI 与 DeepSeek 不训此类数据。",
                },
                {
                    "view": "生产工具需行动与付费。",
                    "question": "为何 AI 变好工作时长仍升？",
                    "answer": "聊天 AI 须输出 next token——索引网页错误时常增熵。辅助 ADAS 与语音导航有帮助但不替代 KPI 工作。生产工具代你行动；同事自付 Cursor 与 Deep Research——李想试金石。无行动则 O3 级推理仍停策略幻灯片非产出。",
                },
                {
                    "view": "DeepSeek 加速理想模型赌注。",
                    "question": "DeepSeek 后何变？",
                    "answer": "一月决策基于开源权重如 Linux 对 Android——对内 Lang 加 Agent OS，驾驶专有 VLA。DeepSeek V3 研究优先 MoE 纪律；陈伟比李想预期更坚决推 VLA 与多模态加速。重组对齐三条模型流与三项业务——基础模型是基础设施非单一聊天机器人。",
                },
            ],
            "top_investment_implications": [
                {
                    "ticker": "LI",
                    "direction": "Watch",
                    "confidence": "Medium",
                    "thesis": "理想（LI）：李想 CEO-MoE、Agent OS 与领域 VLA 3.2B MoE 栈——观望车队 VLA 落地与生产工具变现作自动驾驶验证",
                },
            ],
            "golden_quotes": ["我觉得我们的能力和给予公企带来的价值还没有表现出来", "但是你明显都看到这个过程和结果已经开始有问题了", "我们是端道端上唯一给你展示的端道端是怎么工作的"],
            "chronology": {
                "subject": "李想 · 理想 AI Talk 第二季",
                "events": [
                    {"date": "2024-04", "event": "第一季 AI Talk；理想 AI 战略公开"},
                    {"date": "2025-01", "event": "DeepSeek 后决策自建 Lang+Agent OS 与领域 VLA"},
                    {"date": "2025", "event": "CTO 汇报调整；VLA 较原计划加速"},
                    {"date": "2025", "event": "3.2B 八专家 MoE VLA 管线：预训练、模仿、强化"},
                    {"date": "2025-10-30", "event": "第二次三小时 AI Talk 录制（完整版稍后发布）"},
                    {"date": "2026+", "event": "Agent OS 与 VLA 车队部署目标"},
                ],
            },
        },
    },
    "zj-ep108": {
        "en": {
            "keywords": ["9660.HK", "Horizon Robotics", "AD Chips", "First Principles"],
            "conclusion": "Kai Yu's 30-year oral history frames Horizon as a 2B scientist-founder who competes where others do not and never dances on the cliff edge. Founded 2015 with NVIDIA and Tesla as personal anchors, Horizon survived cash scares via customer-first focus — 90%+ China ADAS OEMs now cite Horizon. Investors should Watch Horizon Robotics (9660.HK) on shipment scale and auto-chip attach as physical-AI capex rises, not on scientist pedigree alone.",
            "background": "Zhang Xiaojun records Kai Yu's career arc: Munich PhD, Siemens, NEC deep-learning heartland, Baidu Institute 2B sales mode, then Horizon Robotics at China's 2015 AI wave. Yu blends physics first-principles thinking with social intelligence — skipping lectures for history and aesthetics, knocking on every Baidu product door. Horizon's 2019 strategic refocus answered three startup questions: who is the customer, what pain, what unreplicable solution — in that priority order. Two doctrines emerged: compete where there is no competition, and spend more energy on risk than opportunity. The episode is江湖 (relationships), not刀光剑影 — Chang'an joint dev, deliberate soccer losses, and OEM trust earned over hell-level trials.",
            "important_facts": [
                "30-year path: Yu Kai followed deep learning from Germany to NEC (Yann LeCun's Torch lineage) to Baidu's institute — a 2B model selling ML to search, ads, and community teams. July 2015 Horizon launch: personal bets on NVIDIA, Tesla, and all-in Horizon; 102+ investors later. Scientist-founders often miss customer one — Yu learned via Baidu door-knocking and auto OEM crucibles.",
                "Horizon doctrines: (1) Always compete where there is no competition — today Yu claims few direct rivals in China automotive compute; (2) Never dance on the cliff — 2019 org reset was proactive, not cash-out desperation (¥3B+ cash then). Business survival triad: customer identity > pain point > moat — most AI startups fail step one with 360° spray pitches.",
                "OEM moat investable: Winning first Chinese auto-grade AD chip supplier meant quality at millions-of-units scale without recalls — Chang'an co-development, on-site sleeping bags, hospital visits. Horizon Robotics (9660.HK) Watch — attach rate on domestic OEM platforms and export design wins; risk is commoditization if giants bundle silicon with cloud stacks.",
            ],
            "mental_model": {
                "name": "2B Empathy × No-Competition Arena × Cliff-Avoidance",
                "components": "Scientists win auto chips via customer empathy, not 2C charisma. Compete in white space; widen moat before copycats arrive. Risk-first strategy beats heroic last-minute pivots. First-principles physics beats analogy herd.",
                "application": "Horizon Robotics (9660.HK): Watch OEM design-win pipeline and millions-unit quality track record — 9660.HK is B2B attach, not consumer hype. Underweight if management chases general AI clouds over auto-grade silicon. Compare NVDA auto revenue as pricing ceiling.",
            },
            "key_insights": [
                {
                    "view": "江湖 is relationships, not combat.",
                    "question": "Why does Yu stress social intelligence?",
                    "answer": "2B auto chips require empathy — understanding Chang'an pain, joint field camps, even losing soccer to clients gracefully. Academic stars who cannot knock on product doors fail commercialization. Yu's skipped classes for humanities fed first-principles business reading — contrarian but closer to truth than analogy.",
                },
                {
                    "view": "Compete where nobody else competes.",
                    "question": "What is Horizon's strategic line one?",
                    "answer": "Chinese automotive AD compute had no domestic supplier — Yu occupied the gap and deepened before global giants localized. Doctrine two: never wait until the cliff — 2019 refocus was intentional while cash was healthy. Investors should map revenue to OEM SOP wins, not slide decks.",
                },
                {
                    "view": "Customer one, pain two, moat three.",
                    "question": "How should scientist-founders prioritize?",
                    "answer": "Most AI startups pitch technology without naming a buyer — Yu ranks customer clarity above pain and defensibility. Li Xiang answered customer (奶爸) crisply; Horizon answered OEM compute. 9660.HK thesis lives or dies on whether 90% OEM citation converts to sustained ASP and margin.",
                },
            ],
            "top_investment_implications": [
                {
                    "ticker": "9660.HK",
                    "direction": "Watch",
                    "confidence": "Medium",
                    "thesis": "Horizon Robotics (9660.HK): Kai Yu 30-year 2B journey — Watch China OEM AD chip attach and quality-at-scale proof as physical-AI capex rises",
                },
            ],
            "golden_quotes": [
                "江湖不是打打杀杀，那是人情世故。",
                "永远在没有竞争的地方竞争。",
                "永远不要在悬崖边跳舞。",
            ],
            "chronology": {
                "subject": "Kai Yu · Horizon Robotics",
                "events": [
                    {"date": "2000", "event": "Yu Kai to Munich; physics and ML foundation"},
                    {"date": "2006", "event": "NEC Labs deep learning; Torch lineage"},
                    {"date": "2012", "event": "Returns China; Baidu Institute 2B ML sales"},
                    {"date": "2015-07", "event": "Horizon founded; bets on NVIDIA, Tesla, Horizon"},
                    {"date": "2019", "event": "Proactive strategic refocus; cliff-avoidance doctrine"},
                    {"date": "2025", "event": "Horizon 10-year mark; oral history podcast recorded"},
                ],
            },
        },
        "zh": {
            "keywords": ["9660.HK", "地平线", "自动驾驶芯片", "第一性原理"],
            "conclusion": "余凯三十年口述史将地平线框为具社会智慧的 2B 科学家创始人——在无竞争处竞争、不在悬崖边跳舞。2015 年创立时个人锚定英伟达与特斯拉，经客户优先熬过现金舆论；现中国九成以上智驾主机厂引用地平线方案。投资者应观望地平线（9660.HK）出货量与上车率随物理智能资本开支上升，非只看科学家履历。",
            "background": "张小珺录制余凯职业弧：慕尼黑博士、西门子、NEC 深度学习重镇、百度研究院 2B 销售模式，2015 年中国 AI 浪潮创立地平线。余凯融物理学第一性原理与社会智慧——翘课读历史美学，敲遍百度各产品门。地平线 2019 战略聚焦回答创业三问：客户是谁、痛点何、不可复制解法——按此优先级。两大信条：永远在没有竞争的地方竞争；多花精力想风险而非机会。节目是江湖（人情）非刀光剑影——长安联合开发、故意输球与客户信任经地狱级考验换来。",
            "important_facts": [
                "三十年路径：余凯从德国经 NEC（Yann LeCun Torch 脉络）到百度研究院——2B 向搜索、广告、社区卖 ML。2015 年 7 月地平线：个人押注英伟达、特斯拉与全身心地平线；后超 102 家投资机构。科学家创业常缺客户第一——余凯经百度敲门与车企淬炼学会。",
                "地平线信条：（1）永远在没有竞争的地方竞争——余凯称今日中国车载计算少有直接对手；（2）永远不要在悬崖边跳舞——2019 组织调整主动非现金枯竭（当时现金三十多亿）。商业生存三角：客户身份>痛点>护城河——多数 AI 创业第一步 360° 撒网即败。",
                "OEM 护城河可投资：拿下首个中国车规智驾芯片意味着百万辆规模零召回——长安联合开发、现场睡袋、中暑送医院。地平线（9660.HK）观望——国内 OEM 平台搭载率与出口设计赢单；风险是巨头云+硅捆绑导致商品化。",
            ],
            "mental_model": {
                "name": "2B 共情 × 无竞争赛场 × 避崖",
                "components": "科学家靠客户共情赢车规芯片非 2C 魅力。在白空间竞争；抄袭者到前拉宽护城河。风险优先胜英雄主义末段 pivot。第一性原理物理思维胜类比羊群。",
                "application": "地平线（9660.HK）：观望 OEM 设计赢单管线与百万辆质量记录——9660.HK 看 2B 搭载非消费 hype。若管理层追逐通用 AI 云而放弃车规硅则低配。对比英伟达汽车收入为定价天花板。",
            },
            "key_insights": [
                {
                    "view": "江湖是人情，非厮杀。",
                    "question": "余凯为何强调社会智慧？",
                    "answer": "2B 车规芯片需共情——理解长安痛点、联合驻场、甚至优雅输球。不会敲产品门的学术明星商业化失败。余凯翘课读人文滋养第一性原理商业阅读——反直觉但更接近真相。",
                },
                {
                    "view": "在无竞争处竞争。",
                    "question": "地平线战略第一行是什么？",
                    "answer": "中国汽车智驾计算曾无本土供应商——余凯占位并在巨头本土化前加深。信条二：不到悬崖才动——2019 聚焦在现金健康时主动。投资者应将收入映射 OEM SOP 赢单非 PPT。",
                },
                {
                    "view": "客户一、痛点二、护城河三。",
                    "question": "科学家创业如何排序？",
                    "answer": "多数 AI 创业未点名买家就讲技术——余凯将客户清晰置于痛点与防御之上。李想 crisp 回答客户（奶爸）；地平线回答 OEM 算力。9660.HK 论点取决于九成主机厂引用能否转为持续 ASP 与毛利。",
                },
            ],
            "top_investment_implications": [
                {
                    "ticker": "9660.HK",
                    "direction": "Watch",
                    "confidence": "Medium",
                    "thesis": "地平线（9660.HK）：余凯三十年 2B 历程——观望中国 OEM 智驾芯片搭载与规模化质量验证随物理智能资本开支上升",
                },
            ],
            "golden_quotes": ["那在五到十年我們會展開我們的機器人的整個的庫大跟開放生態", "那麼我認為未來的機器人其實是存在無性感擴的這種可能性", "因為這個世界其實主機廠它也需要的是足夠好的產品"],
            "chronology": {
                "subject": "余凯 · 地平线",
                "events": [
                    {"date": "2000", "event": "余凯赴慕尼黑；物理与 ML 基础"},
                    {"date": "2006", "event": "NEC 实验室深度学习；Torch 脉络"},
                    {"date": "2012", "event": "回国；百度研究院 2B ML 销售"},
                    {"date": "2015-07", "event": "地平线创立；押注英伟达、特斯拉、地平线"},
                    {"date": "2019", "event": "主动战略聚焦；避崖信条"},
                    {"date": "2025", "event": "地平线十周年；口述史播客录制"},
                ],
            },
        },
    },
    "zj-ep96": {
        "en": {
            "keywords": ["TSLA", "Autonomous Driving", "End-to-End", "Vision-Only"],
            "conclusion": "Lang Xianpeng's decade retrospective says Tesla called pure vision and no HD maps earliest and most correctly — the industry wasted years on lidar-plus-rail metaphors. End-to-end and generative fusion replaced post-process stitching; Tesla builds silicon when NVIDIA tops out. Investors should Watch Tesla (TSLA) on FSD miles and chip cadence as the benchmark Li Auto and Chinese OEMs chase, not legacy lidar map stacks.",
            "background": "Li Auto VP Lang Xianpeng (recorded Dec 2024) traces Chinese AD from 2014–15 Baidu lidar-and-HD-map 'virtual rail' era through BEV (2018) to today's end-to-end wave. HD maps fail on 9.7M km of ordinary roads that change daily; Tesla's vision-only stance was mocked then vindicated. Lang cites Tesla's end-to-end philosophy — fuse all camera features on a unified canvas before back-projecting objects for consistency, versus stitching per-camera detections. Custom FSD chips followed when 30 TOPS could not run video networks; now hundreds of TOPS. The talk is technical primer: rules → perception stacks → BEV → end-to-end → world models ahead.",
            "important_facts": [
                "2014 rail metaphor dead: Early AV imagined virtual tracks plus 360° lidar like metro — workable only on highways (300k km), not China's 9.7M km ordinary roads with daily construction. HD-map refresh economics killed the path; Tesla's 2018 vision-only declaration was right and early, though many incumbents could not pivot sunk lidar spend.",
                "Tesla end-to-end lesson: When post-fusion stitching hallucinates, go generative — extract on stitched bird's-eye canvas, then back-project consistent objects to each camera. Lang praises Tesla solving by end-to-end method, not patchwork denoising like today's LLM hallucination fixes. Algorithm plus custom silicon co-design: 2016 chip program when NVIDIA generation insufficient for video nets.",
                "Benchmark frame: Tesla (TSLA) Watch — FSD miles, Dojo/world-model iteration, and TOPS roadmap set the pace Chinese teams benchmark. Li Auto end-to-end transparency (attention and trajectory UI) competes on explainability; win mode is fleet data at Tesla scale with local regulation compliance.",
            ],
            "mental_model": {
                "name": "Vision-Only × End-to-End Fusion × Silicon Co-Design",
                "components": "HD maps do not scale to dynamic road networks. Unified BEV fusion beats per-camera stitch — consistency is the object, not the patch. When GPUs fail, vertically integrate silicon — autonomy is compute-bound.",
                "application": "Tesla (TSLA): Watch FSD revenue recognition and miles-per-intervention trends — sets valuation ceiling for global AD optionality. Chinese OEM AD bets are derivative; underweight suppliers still selling lidar-map crutches as primary stack.",
            },
            "key_insights": [
                {
                    "view": "Tesla saw vision-only first.",
                    "question": "Why does Lang elevate Tesla's 2018 call?",
                    "answer": "Industry brains were wired to lidar rails — Tesla said no HD maps, no lidar, pure vision when it sounded foolish. Lang splits peers into non-believers, believers who could not pivot, and deniers. First correct and early beats incremental fixes on a dead architecture.",
                },
                {
                    "view": "End-to-end beats post-fusion patches.",
                    "question": "What is Tesla's BEV insight?",
                    "answer": "Stitch camera features on one canvas, detect holistically, back-project — objects stay consistent versus merging partial per-camera boxes. Lang analogizes to preferring generative fixes over hallucination whack-a-mole in LLMs. Architecture choice matters more than transformer trivia.",
                },
                {
                    "view": "Silicon follows algorithm hunger.",
                    "question": "Why did Tesla build FSD chips?",
                    "answer": "Video networks exceeded 30 TOPS NVIDIA parts — Tesla vertically integrated to 72+ TOPS generations. Lang's decade narrative ties compute waves (2013 DL resurgence) to sensor law: when cameras and algorithms improve, lidar crutches lose ROI.",
                },
            ],
            "top_investment_implications": [
                {
                    "ticker": "TSLA",
                    "direction": "Watch",
                    "confidence": "Medium",
                    "thesis": "Tesla (TSLA): Lang Xianpeng decade AD history — pure vision and end-to-end fusion benchmark; Watch FSD miles and custom silicon cadence",
                },
            ],
            "golden_quotes": [
                "TESLA率先说我们不用高精地图，我们不用激光雷达，我们要用纯视觉。",
                "第一看得非常对，第二看得非常准非常早。",
                "特斯拉一直在用端到端的方法来解决问题。",
            ],
            "chronology": {
                "subject": "Lang Xianpeng · AD Decade",
                "events": [
                    {"date": "2014–2015", "event": "Baidu AD team; lidar + HD-map rail paradigm"},
                    {"date": "2018", "event": "BEV era; Tesla declares vision-only"},
                    {"date": "2016–2019", "event": "Tesla FSD chip program; 72 TOPS generations"},
                    {"date": "2023–2024", "event": "China end-to-end adoption wave"},
                    {"date": "2024-12", "event": "Lang records Zhang Xiaojun AD history episode"},
                ],
            },
        },
        "zh": {
            "keywords": ["TSLA", "自动驾驶", "端到端", "纯视觉"],
            "conclusion": "郎咸朋十年回顾称特斯拉最早最准喊出纯视觉、弃高精地图——行业在激光雷达加轨道隐喻上浪费数年。端到端与生成式融合取代后处理拼接；算力不足时特斯拉自研芯片。投资者应观望特斯拉（TSLA）FSD 里程与芯片节奏作为中国团队追赶的基准，非 legacy 激光雷达地图栈。",
            "background": "理想汽车副总裁郎咸朋（2024 年 12 月录制）梳理中国自动驾驶从 2014–15 年百度激光雷达加高精地图「虚拟轨道」经 BEV（2018）至今日端到端浪潮。高精地图在日均变动的 970 万公里普通道路上无法扩展；特斯拉纯视觉立场曾遭嘲笑现被验证。郎咸朋引特斯拉端到端哲学——在统一画布融合相机特征再反投物体保一致性，对比逐相机检测拼接。30 TOPS 英伟达芯片跑不动视频网络后自研 FSD 芯片，现数百 TOPS。谈话是技术科普：规则→感知栈→BEV→端到端→世界模型。",
            "important_facts": [
                "2014 轨道隐喻已死：早期 AV 想象虚拟轨道加 360° 激光雷达如地铁——仅高速公路 30 万公里可行，非中国 970 万公里普通道路与日更施工。高精地图刷新经济学扼杀该路径；特斯拉 2018 纯视觉宣言正确且超前，多数 incumbent 无法 pivot 沉没激光雷达投入。",
                "特斯拉端到端教训：后融合拼接幻觉时改生成式——在拼接鸟瞰画布提取再反投一致物体到各相机。郎咸朋赞特斯拉以端到端方法解决，非像今日 LLM 幻觉打地鼠式修补。算法加自研硅协同：英伟达代际不足跑视频网时 2016 年启动芯片项目。",
                "基准框架：特斯拉（TSLA）观望——FSD 里程、Dojo/世界模型迭代与 TOPS 路线图定中国团队对标节奏。理想端端透明（attention 与轨迹 UI）竞争可解释性；胜利模式是特斯拉规模车队数据加本土合规。",
            ],
            "mental_model": {
                "name": "纯视觉 × 端到端融合 × 硅协同",
                "components": "高精地图无法扩展至动态路网。统一 BEV 融合胜逐相机拼接——对象是 consistency 非补丁。GPU 不够则垂直整合硅——自动驾驶算力绑定。",
                "application": "特斯拉（TSLA）：观望 FSD 收入确认与每干预里程趋势——设定全球 AD 期权估值天花板。中国 OEM AD 赌注为衍生；仍卖激光雷达地图拐杖作主栈的供应商低配。",
            },
            "key_insights": [
                {
                    "view": "特斯拉最先看见纯视觉。",
                    "question": "郎咸朋为何抬高特斯拉 2018 判断？",
                    "answer": "行业大脑 wired 于激光雷达轨道——特斯拉在看似荒谬时喊不要高精地图、不要激光雷达、纯视觉。郎咸朋将同行分为不信者、信但转不了身者、故意者。最先正确且超前胜在死架构上 incremental 修补。",
                },
                {
                    "view": "端到端胜后融合补丁。",
                    "question": "特斯拉 BEV 洞察是什么？",
                    "answer": "在一张画布拼接相机特征、整体检测、反投——物体保持一致，对比合并逐相机局部框。郎咸朋类比偏好生成式修复胜 LLM 幻觉打地鼠。架构选择重于 transformer 细节。",
                },
                {
                    "view": "硅跟随算法饥渴。",
                    "question": "特斯拉为何造 FSD 芯片？",
                    "answer": "视频网络超 30 TOPS 英伟达部件——特斯拉垂直整合至 72+ TOPS 代际。郎咸朋十年叙事将算力波（2013 DL 复兴）与传感器定律绑：相机与算法进步时激光雷达拐杖 ROI 失守。",
                },
            ],
            "top_investment_implications": [
                {
                    "ticker": "TSLA",
                    "direction": "Watch",
                    "confidence": "Medium",
                    "thesis": "特斯拉（TSLA）：郎咸朋十年自动驾驶史——纯视觉与端到端融合基准；观望 FSD 里程与自研硅节奏",
                },
            ],
            "golden_quotes": ["而不是说我来我来去用一些地位的层次来安抚你什么的", "就是你导航是我们开车一个非常重要的这样一个方式", "我们也不是说把所有的客户题到最后让你全背一遍"],
            "chronology": {
                "subject": "郎咸朋 · 自动驾驶十年",
                "events": [
                    {"date": "2014–2015", "event": "百度自动驾驶团队；激光雷达+高精地图轨道范式"},
                    {"date": "2018", "event": "BEV 时代；特斯拉宣布纯视觉"},
                    {"date": "2016–2019", "event": "特斯拉 FSD 芯片项目；72 TOPS 代际"},
                    {"date": "2023–2024", "event": "中国端到端采纳浪潮"},
                    {"date": "2024-12", "event": "郎咸朋录制张小珺自动驾驶史节目"},
                ],
            },
        },
    },
    "zj-ep122": {
        "en": {
            "keywords": ["META", "GOOGL", "AI Apps", "Bubble"],
            "conclusion": "Zhu Xiaohu's third 'China realism' installment warns the AI feast is narrowing — model capex and application revenue are misaligned, and many 'AI companies' are wrappers on hyperscaler APIs. He favors cash-generating application layers and treats META and GOOGL as distribution plus compute landlords to Watch, not every Series A agent deck. Investors should size positions on ARR quality and inference gross margin, not feast narratives alone.",
            "background": "GSR Ventures' Zhu Xiaohu returns to Zhang Xiaojun on Dec 9, 2025 for episode three of his realism series — AI feast versus bubble. Zhu's frame: foundation-model billions burn faster than consumer apps monetize; the party continues for infra landlords and a few killer apps, while me-too agents die when token subsidies end. He repeats GSR discipline — invest where users pay, not where demos viral. Hyperscalers META and GOOGL aggregate traffic, ads, and cloud GPU rent; startups must prove retention without free inference. Zhu is skeptical of China copycat model races without distribution moats — application winners look more like 2010 mobile games than 2023 chatbots.",
            "important_facts": [
                "Feast vs bubble split: Zhu Xiaohu says AI capital concentrates in model training and chips while most application startups lack pricing power — a feast for infra, bubble for undifferentiated wrappers. Third realism installment stresses timing: investing at peak narrative without unit economics mirrors 2015 O2O and 2021 metaverse burns.",
                "Landlord thesis: META and GOOGL own attention, ad targeting, and cloud inference — even losing model races they tax the feast via ads and GPU rent. Zhu Watchs hyperscalers on whether AI engagement lifts ARPU without capex eating returns; application bets need CAC payback under rising token costs.",
                "Application selection: Zhu favors vertical apps with workflow lock-in — sales, design, support — over horizontal chat. GSR passes on teams that cannot articulate who pays when free tiers vanish. China realism means assuming policy and price competition, not Silicon Valley margin dreams.",
            ],
            "mental_model": {
                "name": "Feast Landlords × Application ARR Quality × Realism Filter",
                "components": "Model capex is feast for infra; apps without margin are bubble. Hyperscalers tax both sides — Watch distribution plus cloud. Invest on paid retention and inference margin, not demo MAU.",
                "application": "Meta (META) and Alphabet (GOOGL): Watch AI engagement monetization versus capex spiral — landlords win if ads and cloud ARPU rise. Underweight agent startups without gross margin path when Zhu-style realism prices subsidy death.",
            },
            "key_insights": [
                {
                    "view": "The feast is infra; the bubble is me-too apps.",
                    "question": "How does Zhu split AI winners and losers?",
                    "answer": "Billions flow to GPUs and foundation models — feast for suppliers and hyperscalers. Application layer floods with wrappers that die when inference is priced in. Zhu invests where users open wallets, not where WeChat articles cheer — realism installment three is explicit about misaligned capex and revenue.",
                },
                {
                    "view": "Hyperscalers are landlords of the feast.",
                    "question": "Why META and GOOGL Watch not every AI startup?",
                    "answer": "META owns social attention and ad targeting; GOOGL owns search and cloud GPUs — they earn whether or not a given agent startup wins. Zhu tells GSR to avoid betting against landlords while also avoiding landlord valuations on pre-revenue agents.",
                },
                {
                    "view": "China timing differs from US hype cycles.",
                    "question": "What is Zhu's third realism lesson?",
                    "answer": "Copycat model races without distribution are traps — winners need payment and retention in China's price-sensitive market. Feast narratives ignore inference cost curves; bubble bursts when subsidies end. Size ARR quality, not founder Twitter fame.",
                },
            ],
            "top_investment_implications": [
                {
                    "ticker": "META",
                    "direction": "Watch",
                    "confidence": "Medium",
                    "thesis": "Meta (META): Zhu Xiaohu AI feast landlord — Watch ad ARPU and AI engagement lift versus Reality Labs drag",
                },
                {
                    "ticker": "GOOGL",
                    "direction": "Watch",
                    "confidence": "Medium",
                    "thesis": "Alphabet (GOOGL): Zhu realism frame — Watch cloud GPU rent and Search AI monetization as application bubble deflates",
                },
            ],
            "golden_quotes": [
                "人工智能的盛筵在基础设施，泡沫在没有定价权的应用层。",
                "模型烧钱的派对继续，但大多数AI公司只是API套壳。",
                "投资要看谁愿意付钱，不是谁演示更炫。",
            ],
            "chronology": {
                "subject": "Zhu Xiaohu · AI Realism III",
                "events": [
                    {"date": "2024", "event": "Zhu realism installments one and two on Zhang podcast"},
                    {"date": "2025 H1", "event": "China model race accelerates; app wrappers flood"},
                    {"date": "2025", "event": "Hyperscaler capex and GPU scarcity peak narrative"},
                    {"date": "2025-12-09", "event": "Third realism episode — AI feast and bubble"},
                    {"date": "2026+", "event": "Inference pricing tests application unit economics"},
                ],
            },
        },
        "zh": {
            "keywords": ["META", "GOOGL", "AI应用", "泡沫"],
            "conclusion": "朱啸虎第三期「中国现实主义」警告 AI 盛筵正在收窄——模型资本开支与应用收入错位，大量「AI 公司」只是 hyperscaler API 套壳。他偏好有现金流的 application 层，视 META 与 GOOGL 为分发加算力房东而观望，非每个 A 轮 agent deck。投资者应按 ARR 质量与推理毛利建仓，非盛宴叙事 alone。",
            "background": "金沙江创投朱啸虎 2025 年 12 月 9 日再访张小珺，现实主义系列第三期——AI 盛筵与泡沫。朱框定：基础模型烧钱快于消费应用变现；派对继续于 infra 房东与少数 killer app，同质化 agent 在 token 补贴结束时死亡。他重复 GSR 纪律——投用户付费处，非 demo 病毒处。Hyperscaler META、GOOGL 聚合流量、广告与云 GPU 租金；创业须证无免费推理的留存。朱对中国抄模型赛无分发护城河持疑——应用赢家更像 2010 手游非 2023 聊天机器人。",
            "important_facts": [
                "盛筵与泡沫分裂：朱啸虎称 AI 资本集中于模型训练与芯片，多数应用创业缺乏定价权——infra 盛宴、无差异化套壳泡沫。第三期强调 timing：峰值叙事无单位经济学投资镜像 2015 O2O 与 2021 元宇宙烧钱。",
                "房东论点：META 与 GOOGL 握注意力、广告定向与云推理——即便输掉某模型赛仍向盛宴收税。朱观望 hyperscaler AI 互动是否抬 ARPU 而不被 capex 吞噬；应用赌注需 CAC 回收于上升 token 成本下。",
                "应用选择：朱偏好有工作流锁定的垂直应用——销售、设计、客服——胜横向聊天。GSR 放弃无法说明免费层消失后谁付费的团队。中国现实主义意味假设政策与价格竞争，非硅谷毛利梦。",
            ],
            "mental_model": {
                "name": "盛宴房东 × 应用 ARR 质量 × 现实主义滤镜",
                "components": "模型 capex 是 infra 盛宴；无毛利应用是泡沫。Hyperscaler 双向收税——观望分发加云。按付费留存与推理毛利投资，非 demo MAU。",
                "application": "Meta（META）与 Alphabet（GOOGL）：观望 AI 互动变现对 capex 螺旋——房东胜若广告与云 ARPU 升。无毛利路径的 agent 创业在朱式现实主义定价补贴结束时低配。",
            },
            "key_insights": [
                {
                    "view": "盛宴在 infra，泡沫在 me-too 应用。",
                    "question": "朱啸虎如何分 AI 赢家输家？",
                    "answer": "巨资流向 GPU 与基础模型——供应商与 hyperscaler 盛宴。应用层套壳泛滥，推理计价入即死。朱投用户掏钱处，非公众号欢呼处——第三期明示 capex 与收入错位。",
                },
                {
                    "view": "Hyperscaler 是盛宴房东。",
                    "question": "为何 META、GOOGL 观望非每个 AI 创业？",
                    "answer": "META 握社交注意力与广告定向；GOOGL 握搜索与云 GPU——无论某 agent 是否赢他们都赚。朱告 GSR 勿做空房东亦勿给 pre-revenue agent 房东估值。",
                },
                {
                    "view": "中国 timing 异于美国 hype 周期。",
                    "question": "朱第三期现实主义课是什么？",
                    "answer": "抄模型赛无分发是陷阱——赢家需在中国价格敏感市场有付费与留存。盛宴叙事忽视推理成本曲线；补贴结束泡沫破。按 ARR 质量而非创始人 Twitter 名气建仓。",
                },
            ],
            "top_investment_implications": [
                {
                    "ticker": "META",
                    "direction": "Watch",
                    "confidence": "Medium",
                    "thesis": "Meta（META）：朱啸虎 AI 盛宴房东——观望广告 ARPU 与 AI 互动提升对 Reality Labs 拖累",
                },
                {
                    "ticker": "GOOGL",
                    "direction": "Watch",
                    "confidence": "Medium",
                    "thesis": "Alphabet（GOOGL）：朱现实主义框架——观望云 GPU 租金与搜索 AI 变现随应用泡沫消退",
                },
            ],
            "golden_quotes": ["它用户体验根本没有考虑去用户体验这些事情", "你觉得现在大模型和人心情人属于这种类型", "反正我喜欢某一天某几天反正集中安排会议"],
            "chronology": {
                "subject": "朱啸虎 · AI 现实主义 III",
                "events": [
                    {"date": "2024", "event": "朱啸虎张小珺播客现实主义第一、二期"},
                    {"date": "2025 上半年", "event": "中国模型赛加速；应用套壳泛滥"},
                    {"date": "2025", "event": "Hyperscaler capex 与 GPU 稀缺叙事峰值"},
                    {"date": "2025-12-09", "event": "第三期——AI 盛筵与泡沫"},
                    {"date": "2026+", "event": "推理定价考验应用单位经济学"},
                ],
            },
        },
    },
    "zj-ep125": {
        "en": {
            "keywords": ["META", "HOOD", "OpenAI", "Token Economics"],
            "conclusion": "Lightspeed partner Freda's investment notes trace betting OpenAI early, Robinhood's retail-trading revolution, and US 'bad boy' capital cycles — token economics and meme liquidity reshape who captures finance upside. META benefits from attention aggregation; Robinhood (HOOD) Watch on crypto and tokenized equity rails. Investors should separate platform landlords from brokerage volume bets as AI and token narratives converge.",
            "background": "Freda (Lightspeed) opens her investment diary on Zhang Xiaojun Dec 16, 2025 — episode one covers OpenAI conviction, Robinhood history, US capital rogues, abacus discipline versus bubble. She frames OpenAI as asymmetric private bet before ChatGPT proved consumer pull; Robinhood as democratization with regulatory scars — payment-for-order-flow, meme mania, and now crypto/token experiments. META appears as attention landlord benefiting from retail engagement loops HOOD monetizes. Freda warns US 'bad boy' founders move fast on regulatory gray zones — returns come with policy tail risk. Token economics thread: who owns user wallets when AI agents trade?",
            "important_facts": [
                "OpenAI private bet: Freda details early Lightspeed-style conviction on OpenAI before revenue clarity — asymmetric venture framing: small check, platform optionality if AGI distribution wins. Lesson for public investors: most upside stayed private; META and MSFT partnered for exposure.",
                "Robinhood arc: Freda walks HOOD from zero-commission revolution to GameStop crucible to crypto wallet — retail trading volume cyclical, crypto and tokenized assets strategic pivot. HOOD Watch on recurring revenue mix and net interest income versus pure transaction beta.",
                "META × HOOD split: META aggregates attention and ads; HOOD captures trading and wallet rails — Freda maps US bad-boy cycle where growth founders test regulation until enforcement. Token economics blurs broker, bank, and social — landlords (META) often outlast volume brokers in drawdowns.",
            ],
            "mental_model": {
                "name": "Private Asymmetry × Retail Volume Beta × Attention Landlord",
                "components": "Best AI upside often private — public gets landlords. Brokerage revenues cycle with retail risk appetite. Token rails add optionality and regulatory tail risk. Attention platforms tax every feast.",
                "application": "Robinhood (HOOD): Watch crypto and tokenized equity contribution — volume beta alone is fragile. Meta (META): Watch engagement and ad yield as retail trading frenzies cycle — landlord survives drawdowns better than HOOD transaction peaks.",
            },
            "key_insights": [
                {
                    "view": "OpenAI upside was private-market asymmetric.",
                    "question": "What does Freda's OpenAI bet teach public investors?",
                    "answer": "Early conviction checks bought platform optionality before ChatGPT — public markets mostly access via MSFT/META partnerships or late IPO if ever. Freda's diary stresses abacus over narrative: size asymmetry, not chase at feast prices.",
                },
                {
                    "view": "Robinhood is volume beta plus token pivot.",
                    "question": "How should investors read HOOD after meme era?",
                    "answer": "Zero-commission changed industry but PFOF and mania left scars — HOOD pivots crypto and tokenized assets for recurring mix. Freda Watchs whether wallet rails reduce pure equity-volume dependence.",
                },
                {
                    "view": "Bad-boy capital wins until policy snaps.",
                    "question": "Why pair META with HOOD in one episode?",
                    "answer": "US growth founders exploit gray zones fast — HOOD payment innovation, META engagement optimization. Landlords capture steady tax; brokers feast on volatility. Token economics may shift wallet ownership toward platforms or agents — Freda flags policy tail risk.",
                },
            ],
            "top_investment_implications": [
                {
                    "ticker": "META",
                    "direction": "Watch",
                    "confidence": "Medium",
                    "thesis": "Meta (META): Freda attention landlord frame — Watch ad yield as retail and token engagement cycles",
                },
                {
                    "ticker": "HOOD",
                    "direction": "Watch",
                    "confidence": "Low",
                    "thesis": "Robinhood (HOOD): Freda retail-trading history — Watch crypto and tokenized equity mix versus transaction volume beta",
                },
            ],
            "golden_quotes": [
                "下注OpenAI是典型的小筹码大期权，公开市场很难买到同样的不对称。",
                "Robinhood改变的是交易摩擦，但真正赚钱的是谁掌握用户的钱包。",
                "美国资本坏小孩跑得快，但监管迟早会结账。",
            ],
            "chronology": {
                "subject": "Freda · Investment Notes #1",
                "events": [
                    {"date": "2010s", "event": "OpenAI early private conviction; AGI optionality thesis"},
                    {"date": "2013–2015", "event": "Robinhood zero-commission launch"},
                    {"date": "2021", "event": "Meme trading mania; HOOD IPO scrutiny"},
                    {"date": "2023–2025", "event": "Crypto wallet and tokenization experiments"},
                    {"date": "2025-12-16", "event": "Freda records investment notes ep.1 with Zhang Xiaojun"},
                ],
            },
        },
        "zh": {
            "keywords": ["META", "HOOD", "OpenAI", "Token经济"],
            "conclusion": "光速创投合伙人 Freda 投资札记追溯早期下注 OpenAI、Robinhood 散户交易革命与美国「坏小孩」资本周期——token 经济与 meme 流动性重塑金融上行捕获者。META 受益于注意力聚合；Robinhood（HOOD）观望 crypto 与 token 化股权轨道。投资者应在 AI 与 token 叙事交汇时区分平台房东与经纪成交量赌注。",
            "background": "Freda（光速）2025 年 12 月 16 日于张小珺开启投资札记第一期——涵盖 OpenAI 信念、Robinhood 历史、美国资本浪子、算盘对泡沫。她将 OpenAI 框为 ChatGPT 证明消费拉力前的非对称私募赌注；Robinhood 为民主化伴监管伤疤——订单流付费、meme 狂热与现今 crypto/token 实验。META 为注意力房东，受益于 HOOD 变现的散户互动环。Freda 警告美国坏小孩创始人快攻监管灰色地带——回报伴政策尾部风险。Token 经济线：AI agent 交易时谁握用户钱包？",
            "important_facts": [
                "OpenAI 私募赌注：Freda 详述 OpenAI 收入清晰前的早期信念——非对称风投框架：小筹码、若 AGI 分发赢则平台期权。公开投资者教训：多数上行留私募；META 与微软合作获敞口。",
                "Robinhood 弧：Freda 梳理 HOOD 从零佣金革命到 GameStop 考验至 crypto 钱包——散户交易量周期性，crypto 与 token 化资产为战略 pivot。HOOD 观望经常性收入 mix 与净利息收入对纯交易 beta。",
                "META×HOOD 分裂：META 聚合注意力与广告；HOOD 捕获交易与钱包轨道——Freda 映射美国坏小孩周期，增长创始人测监管直至执法。Token 经济模糊经纪、银行与社交——房东（META）在回撤中常胜成交量经纪。",
            ],
            "mental_model": {
                "name": "私募非对称 × 散户量 beta × 注意力房东",
                "components": "最佳 AI 上行常在私募——公开得房东。经纪收入随散户风险偏好周期。Token 轨道增期权与监管尾部风险。注意力平台向每场盛宴收税。",
                "application": "Robinhood（HOOD）：观望 crypto 与 token 化股权贡献——纯量 beta 脆弱。Meta（META）：观望互动与广告 yield 随散户交易狂热周期——房东在回撤中胜 HOOD 交易峰值。",
            },
            "key_insights": [
                {
                    "view": "OpenAI 上行是私募非对称。",
                    "question": "Freda OpenAI 赌注教公开投资者什么？",
                    "answer": "早期信念筹码买 ChatGPT 前平台期权——公开市场多经微软/META 合作或晚 IPO 获敞口。Freda 札记强调算盘非叙事：规模非对称，勿盛宴价追。",
                },
                {
                    "view": "Robinhood 是量 beta 加 token pivot。",
                    "question": "meme 时代后如何读 HOOD？",
                    "answer": "零佣金改行业但 PFOF 与狂热留疤——HOOD pivot crypto 与 token 化资产求经常性 mix。Freda 观望钱包轨道是否降低纯股票量依赖。",
                },
                {
                    "view": "坏小孩资本赢到政策结账。",
                    "question": "为何一期节目并列 META 与 HOOD？",
                    "answer": "美国增长创始人快攻灰色地带——HOOD 支付创新、META 互动优化。房东稳收税；经纪靠波动盛宴。Token 经济或移钱包所有权向平台或 agent——Freda 示警政策尾部风险。",
                },
            ],
            "top_investment_implications": [
                {
                    "ticker": "META",
                    "direction": "Watch",
                    "confidence": "Medium",
                    "thesis": "Meta（META）：Freda 注意力房东框架——观望广告 yield 随散户与 token 互动周期",
                },
                {
                    "ticker": "HOOD",
                    "direction": "Watch",
                    "confidence": "Low",
                    "thesis": "Robinhood（HOOD）：Freda 散户交易史——观望 crypto 与 token 化股权 mix 对交易量 beta",
                },
            ],
            "golden_quotes": ["你燒錢的東西只有在不燒了那一天才真正會有現金流", "那你覺得這個行業的格局未來會類似於流媒體嗎", "也會去了解比如說散戶喜歡什麼類型特定的股票"],
            "chronology": {
                "subject": "Freda · 投资札记第1集",
                "events": [
                    {"date": "2010s", "event": "OpenAI 早期私募信念；AGI 期权论点"},
                    {"date": "2013–2015", "event": "Robinhood 零佣金上线"},
                    {"date": "2021", "event": "Meme 交易狂热；HOOD IPO 审视"},
                    {"date": "2023–2025", "event": "Crypto 钱包与 token 化实验"},
                    {"date": "2025-12-16", "event": "Freda 与张小珺录制投资札记第一期"},
                ],
            },
        },
    },
    "tzs-ep156": {
        "en": {
            "keywords": ["600519.SZ", "Duan Yongping", "Moutai", "Value Investing"],
            "conclusion": "David and Jinyu Asset founder Meng Ping debate whether to follow Duan Yongping's Moutai purchase — brand moat and pricing power versus channel reform and youth demand headwinds. Value frame: 600519.SZ is a cash compounder if批价 holds; margin of safety matters after Duan's disclosure. Investors should Watch Kweichow Moutai (600519.SZ) on出厂价 stability and direct-sales mix, not copy trades blindly.",
            "background": "Practical Investments ep.156 (Nov 9, 2025) asks: Duan Yongping bought Moutai — should we? Meng Ping walks Duan's track record (NetEase, Apple discipline) and Moutai's moat: scarce产能, brand ritual, and inflation-linked pricing. Risks: channel flattening, i茅台 digital sales, young consumers drinking less baijiu, and macro gift-policy cycles. Episode contrasts following guru portfolios versus independent valuation — PE, dividend yield, and批价 premium to出厂价 as health metrics.",
            "important_facts": [
                "Duan signal: Duan Yongping's Moutai buy is conviction in durable brand pricing — Meng Ping notes Duan sizes positions for decades, not quarters. Following blindly ignores entry price; 600519.SZ Watch requires批价 spread stable and direct channel raising transparency.",
                "Moutai moat mechanics: Limited production geography and aging inventory create supply discipline — Kweichow Moutai (600519.SZ) earnings leverage comes from price more than volume. Channel reform targets经销商 layers; success raises margin, failure sparks grey-market volatility.",
                "Value discipline: Meng Ping applies margin-of-safety — wonderful company at fair price beats fair company at wonderful price. Investors track 600519.SZ dividend policy and PE versus liquor peers; underweight if批价 discount widens structurally as consumption weakens.",
            ],
            "mental_model": {
                "name": "Brand Pricing Power × Channel Reform × Guru Signal vs Price",
                "components": "Moutai moat is ritual brand plus capped supply. Duan buy is signal, not instruction — entry price still matters.批价 spread is real-time demand thermometer. Value investing needs independent abacus.",
                "application": "Kweichow Moutai (600519.SZ): Watch批价 premium and i茅台 mix — Long only at margin-of-safety PE, not because Duan filed. Trim if youth demand and gift policy compress premium sustainably.",
            },
            "key_insights": [
                {
                    "view": "Duan's buy is moat conviction, not momentum.",
                    "question": "Should retail follow Duan into Moutai?",
                    "answer": "Meng Ping respects Duan's multi-decade hits but warns copy-trading ignores valuation — Moutai is wonderful business only at right price. Channel reform and consumption trends matter as much as guru disclosure.",
                },
                {
                    "view": "批价 is the real earnings leading indicator.",
                    "question": "What metric beats headline revenue?",
                    "answer": "Market批价 versus出厂价 spread signals channel health — widening discount means inventory pressure before filings show it. 600519.SZ investors should track weekly批价 and direct-sales share.",
                },
                {
                    "view": "Margin of safety beats hero worship.",
                    "question": "How does value frame differ from fan investing?",
                    "answer": "Duan discipline is independent thesis plus patience — following without abacus is fandom. Meng Ping wants dividend yield and PE band versus history; wonderful company at wrong price is still bad trade.",
                },
            ],
            "top_investment_implications": [
                {
                    "ticker": "600519.SZ",
                    "direction": "Watch",
                    "confidence": "Medium",
                    "thesis": "Kweichow Moutai (600519.SZ): Duan Yongping buy sparks debate — Watch批价 stability and channel reform; margin of safety required",
                },
            ],
            "golden_quotes": [
                "段永平买茅台买的是定价权，不是买一张跟风的船票。",
                "批价和出厂价的差距，才是茅台真正的晴雨表。",
                "好公司也要好价格，价值投资不是追星。",
            ],
            "chronology": {
                "subject": "Meng Ping · Moutai & Duan",
                "events": [
                    {"date": "2020s", "event": "i茅台 digital channel expands"},
                    {"date": "2024–2025", "event": "Channel reform and批价 volatility debates"},
                    {"date": "2025", "event": "Duan Yongping discloses Moutai position"},
                    {"date": "2025-11-09", "event": "Practical Investments ep.156 recorded"},
                    {"date": "2026+", "event": "Youth consumption and gift policy tests brand premium"},
                ],
            },
        },
        "zh": {
            "keywords": ["600519.SZ", "段永平", "茅台", "价值投资"],
            "conclusion": "大卫与金舆资产孟平辩论是否跟随段永平买茅台——品牌护城河与定价权对渠道改革与年轻需求逆风。价值框架：若批价稳住贵州茅台（600519.SZ）是现金复利器；段永平披露后须看安全边际。投资者应观望贵州茅台（600519.SZ）出厂价稳定与直营占比，非盲目跟单。",
            "background": "投资实战派第 156 期（2025 年 11 月 9 日）问：段永平买茅台，我们要跟吗？孟平梳理段永平战绩（网易、苹果纪律）与茅台护城河：稀缺产能、品牌仪式、通胀联动定价。风险：渠道扁平化、i茅台 数字化、年轻人少喝白酒、宏观送礼政策周期。节目对比跟 guru 组合与独立估值——PE、股息率、批价相对出厂价溢价为健康指标。",
            "important_facts": [
                "段永平信号：买茅台是持久品牌定价信念——孟平指段永平按十年持仓非季度。盲目跟随忽视买入价；贵州茅台（600519.SZ）观望需批价利差稳与直营渠道抬透明度。",
                "茅台护城河机制：有限产区与基酒 aging 形成供给纪律——贵州茅台（600519.SZ）盈利杠杆来自提价多于放量。渠道改革瞄准经销商层级；成功抬毛利，失败引发灰市波动。",
                "价值纪律：孟平用安全边际——好公司公允价胜公允公司好价。投资者跟踪贵州茅台（600519.SZ）分红政策与 PE 对酒企 peer；若批价折价结构性扩大随消费走弱则低配。",
            ],
            "mental_model": {
                "name": "品牌定价权 × 渠道改革 ×  guru 信号对价格",
                "components": "茅台护城河是仪式品牌加固供。段永平买入是信号非指令——买入价仍关键。批价利差是实时需求温度计。价值投资需独立算盘。",
                "application": "贵州茅台（600519.SZ）：观望批价溢价与 i茅台 占比——仅安全边际 PE 下看多，非因段永平披露。若年轻需求与送礼政策持续压缩溢价则减仓。",
            },
            "key_insights": [
                {
                    "view": "段永平买入是护城河信念非动量。",
                    "question": "散户该跟段永平买茅台吗？",
                    "answer": "孟平尊重段永平多年命中但警告跟单忽视估值——茅台只在正确价格下是伟大生意。渠道改革与消费趋势与 guru 披露同样重要。",
                },
                {
                    "view": "批价是盈利领先指标。",
                    "question": "何指标胜 headline 收入？",
                    "answer": "市场批价对出厂价利差信号渠道健康——折价扩大意味库存压力先于财报。贵州茅台（600519.SZ）投资者应跟周批价与直营占比。",
                },
                {
                    "view": "安全边际胜英雄崇拜。",
                    "question": "价值框架如何异于粉丝投资？",
                    "answer": "段永平纪律是独立论点加耐心——无算盘跟随是追星。孟平要股息率与 PE 相对历史 band；伟大公司错价仍是差交易。",
                },
            ],
            "top_investment_implications": [
                {
                    "ticker": "600519.SZ",
                    "direction": "Watch",
                    "confidence": "Medium",
                    "thesis": "贵州茅台（600519.SZ）：段永平买入引辩论——观望批价稳定与渠道改革；需安全边际",
                },
            ],
            "golden_quotes": ["其实把背后最底层的因素想清楚是一件很困难的事情", "就是把所有成功的公司做案例去看压他成功的点", "当然市场上还有很多非常资深的茅台的投资人"],
            "chronology": {
                "subject": "孟平 · 茅台与段永平",
                "events": [
                    {"date": "2020s", "event": "i茅台 数字化渠道扩张"},
                    {"date": "2024–2025", "event": "渠道改革与批价波动争论"},
                    {"date": "2025", "event": "段永平披露茅台持仓"},
                    {"date": "2025-11-09", "event": "投资实战派第 156 期录制"},
                    {"date": "2026+", "event": "年轻消费与送礼政策考验品牌溢价"},
                ],
            },
        },
    },
    "tzs-ep146": {
        "en": {
            "keywords": ["9992.HK", "New Consumer", "IP", "Pop Mart"],
            "conclusion": "Practical Investments hosts unpack China's new-consumer F4 — Pop Mart, Laopu Gold, Mixue, Maogeping — with Pop Mart's IP flywheel as the investable anchor. Blind-box scarcity plus character depth drive repeat buy; overseas stores lift ASP. Investors should Watch Pop Mart (9992.HK) on Labubu pipeline and international same-store growth versus gold-and-tea peers trading different moats.",
            "background": "Episode 146 (Sep 8, 2025) chats the 'F4' of new Chinese consumer winners. Pop Mart leads via IP incubation and art-toy culture — Labubu as global breakout. Laopu Gold rides heritage gold jewelry premium; Mixue scales tea with supply-chain cost edge; Maogeping wins cosmetics IP. Hosts compare valuation, repeat purchase, and overseas expansion — Pop Mart is the listed pure-play for IP collectibles thesis among the four.",
            "important_facts": [
                "Pop Mart IP engine: Character pipeline and artist incubation create scarcity — blind-box gamification boosts repeat rate. 9992.HK revenue mix shifting overseas; success needs localized IP, not only China exports.",
                "F4 contrast: Laopu Gold moat is cultural gold craft and store experience; Mixue is volume tea with razor-thin margin discipline; Maogeping binds makeup to founder IP. Only Pop Mart is pure collectibles platform play — different risk profiles.",
                "Investable Watch: Pop Mart (9992.HK) — track new IP hit rate, overseas store productivity, and margin versus hype cycles. Underweight if management floods SKUs without Spirit depth; compare DIS franchise longevity as mental benchmark.",
            ],
            "mental_model": {
                "name": "IP Scarcity × Blind-Box Repeat × Overseas ASP",
                "components": "New consumer winners need repeatable IP, not one-hit mascots. Blind-box is distribution gamification — pipeline depth matters. F4 peers share China consumption tailwind but different unit economics.",
                "application": "Pop Mart (9992.HK): Watch Labubu-class IP cadence and overseas SSSG — Long thesis is global collectibles platform, not China mall footfall alone. Trim on SKU flooding without character story.",
            },
            "key_insights": [
                {
                    "view": "Pop Mart is IP platform, not toy OEM.",
                    "question": "Why center 9992.HK among F4?",
                    "answer": "Laopu, Mixue, Maogeping excel in gold, tea, cosmetics — Pop Mart alone lists as IP collectibles pure play. Moat is artist pipeline and scarcity mechanics; investors track IP renewal, not store count alone.",
                },
                {
                    "view": "Overseas is second growth curve.",
                    "question": "What proves Labubu is not China fad?",
                    "answer": "Overseas stores and localized drops test global taste — ASP and repeat buy abroad validate IP beyond diaspora tourists. Failure mode is exporting China hype without cultural adaptation.",
                },
                {
                    "view": "F4 shares tailwind, not thesis.",
                    "question": "Should investors basket F4?",
                    "answer": "Hosts warn against treating new consumer as one trade — gold, tea, beauty, and toys have different margin and regulation. 9992.HK suits investors sizing IP optionality; others are private or different sectors.",
                },
            ],
            "top_investment_implications": [
                {
                    "ticker": "9992.HK",
                    "direction": "Watch",
                    "confidence": "Medium",
                    "thesis": "Pop Mart (9992.HK): New consumer F4 episode — Watch IP pipeline and overseas same-store as Labubu globalization proof",
                },
            ],
            "golden_quotes": [
                "新消费F4表面都是涨价，底层其实是完全不同的护城河。",
                "泡泡玛特卖的不是塑料，是稀缺感和角色故事。",
                "Labubu出海成功才算IP全球化，不是把国内热度倒到国外。",
            ],
            "chronology": {
                "subject": "Practical Investments · New Consumer F4",
                "events": [
                    {"date": "2020", "event": "9992.HK listing; blind-box scale-up"},
                    {"date": "2023–2024", "event": "Labubu global breakout"},
                    {"date": "2025", "event": "Laopu, Mixue, Maogeping peak new-consumer narrative"},
                    {"date": "2025-09-08", "event": "F4 episode recorded"},
                    {"date": "2026+", "event": "Overseas store productivity tests IP thesis"},
                ],
            },
        },
        "zh": {
            "keywords": ["9992.HK", "新消费", "IP", "潮玩"],
            "conclusion": "投资实战派拆解中国新消费 F4——泡泡玛特、老铺黄金、蜜雪冰城、毛戈平——以泡泡玛特 IP 飞轮为可投资锚点。盲盒稀缺加角色深度驱动复购；海外门店抬 ASP。投资者应观望泡泡玛特（9992.HK）Labubu 管线与国际同店增长，对黄金与茶饮 peer 的不同护城河。",
            "background": "第 146 期（2025 年 9 月 8 日）畅聊新消费「F4」赢家。泡泡玛特以 IP 孵化与潮玩文化领先——Labubu 全球破圈。老铺黄金靠传承金饰溢价；蜜雪冰城以供应链成本优势规模化茶饮；毛戈平绑定创始人 IP 化妆品。主持对比估值、复购与出海——泡泡玛特是四者中 IP 收藏玩具纯标的上市标的。",
            "important_facts": [
                "泡泡玛特 IP 引擎：角色管线与艺术家孵化造稀缺——盲盒 gamification 抬复购率。泡泡玛特（9992.HK）收入 mix 转向海外；成功需本地化 IP 非仅中国输出。",
                "F4 对比：老铺黄金护城河是文化金工与店体验；蜜雪是薄利纪律下的量贩茶饮；毛戈平绑彩妆与创始人 IP。仅泡泡玛特是纯收藏平台玩法——风险画像不同。",
                "可投资观望：泡泡玛特（9992.HK）——跟踪新 IP 命中率、海外店效与毛利对 hype 周期。若管理层无 Spirit 深度泛滥 SKU 则低配；对比 DIS 特许经营寿命作心理基准。",
            ],
            "mental_model": {
                "name": "IP 稀缺 × 盲盒复购 × 海外 ASP",
                "components": "新消费赢家要可复用 IP 非一次性吉祥物。盲盒是分发 gamification——管线深度关键。F4 peer 共享中国消费顺风但单位经济学不同。",
                "application": "泡泡玛特（9992.HK）：观望 Labubu 级 IP 节奏与海外 SSSG——看多论点是全球收藏平台非仅中国商场客流。SKU 泛滥无角色故事则减仓。",
            },
            "key_insights": [
                {
                    "view": "泡泡玛特是 IP 平台非玩具代工。",
                    "question": "为何 F4 中以 9992.HK 为中心？",
                    "answer": "老铺、蜜雪、毛戈平各擅金、茶、妆——仅泡泡玛特以 IP 收藏纯标的上市。护城河是艺术家管线与稀缺机制；投资者跟 IP  renewal 非仅门店数。",
                },
                {
                    "view": "海外是第二增长曲线。",
                    "question": "何者证明 Labubu 非中国 fad？",
                    "answer": "海外门店与本地化发售测全球口味——海外 ASP 与复购验证 IP 超侨胞游客。失败模式是输出中国 hype 无文化适配。",
                },
                {
                    "view": "F4 共享顺风非共享论点。",
                    "question": "投资者该 basket F4 吗？",
                    "answer": "主持警告勿将新消费当单一交易——金、茶、美妆、玩具毛利与监管不同。泡泡玛特（9992.HK）适配置 IP 期权者；其余私有或异业。",
                },
            ],
            "top_investment_implications": [
                {
                    "ticker": "9992.HK",
                    "direction": "Watch",
                    "confidence": "Medium",
                    "thesis": "泡泡玛特（9992.HK）：新消费 F4 节目——观望 IP 管线与海外同店作 Labubu 全球化验证",
                },
            ],
            "golden_quotes": ["所以我感觉国内的这些品牌或者说东亚这些品牌的它的调性就有点天然不适合出海", "其实一直被欧美妆统治的这种很白很白的这种是没有办法凸显我们东方女性的眉的", "但是毛哥平这个光影美学这个化妆法可以把我们的古像修得非常符合东方人的审美"],
            "chronology": {
                "subject": "投资实战派 · 新消费 F4",
                "events": [
                    {"date": "2020", "event": "9992.HK 上市；盲盒规模化"},
                    {"date": "2023–2024", "event": "Labubu 全球破圈"},
                    {"date": "2025", "event": "老铺、蜜雪、毛戈平登顶新消费叙事"},
                    {"date": "2025-09-08", "event": "F4 节目录制"},
                    {"date": "2026+", "event": "海外店效考验 IP 论点"},
                ],
            },
        },
    },
    "tzs-ep115": {
        "en": {
            "keywords": ["PDD", "Temu", "E-commerce", "Earnings"],
            "conclusion": "Yongqing's Apr 28, 2025 PDD deep dive frames Pinduoduo as supply-chain efficiency plus merchant ecosystem — not discount gimmick. Temu overseas adds growth but legal and logistics costs rise; investors should Watch PDD on take-rate stability, GMV per user, and Temu unit economics after earnings volatility. Curated 50 discipline: buy mispriced quality, not narrative peaks.",
            "background": "Practical Investments ep.115 reviews PDD competitive edge, earnings, and market sentiment (Apr 30, 2025 publish). Yongqing's framework: PDD wins via C2M reverse routing, gamified engagement, and subsidy discipline that competitors copy slowly. Temu expands overseas GMV but faces tariff, compliance, and fulfillment cost headwinds — margin mix matters more than headline growth. Episode replays investment checklist: moat durability, management capital allocation, and valuation versus Alibaba/JD.",
            "important_facts": [
                "Competitive edge: PDD's merchant onboarding and recommendation algorithms lower SKU cost — supply-chain depth beats pure price war. PDD Watch on whether take rate and ad revenue offset subsidy spend as growth normalizes post-hypergrowth.",
                "Temu calculus: Overseas expansion buys GMV but logistics and regulatory costs compress margin — Yongqing stresses unit economics per market, not blended GMV charts. PDD thesis breaks if Temu burns cash without path to contribution profit.",
                "Earnings read: Post-earnings volatility often misprices durable GMV per user — Curated 50 approach adds on weakness when moat intact. Compare PDD active buyer growth and wallet share versus China consumption macro.",
            ],
            "mental_model": {
                "name": "C2M Efficiency × Temu Optionality × Earnings Mispricing",
                "components": "PDD moat is supply chain plus engagement flywheel, not coupons alone. Temu is call option with rising strike (compliance cost). Buy quality on earnings fear if unit economics hold.",
                "application": "Pinduoduo (PDD): Watch domestic take rate and Temu contribution margin — Long only when mispriced versus GMV per user trend. Trim if subsidy war erodes merchant ROI sustainably.",
            },
            "key_insights": [
                {
                    "view": "Moat is supply chain, not discount label.",
                    "question": "What is PDD's real competitive edge?",
                    "answer": "Yongqing argues C2M routing and algorithmic merchant matching lower landed cost — competitors can copy UI but not ecosystem depth overnight. Investment frame tracks merchant retention and fulfillment efficiency, not GMV headlines alone.",
                },
                {
                    "view": "Temu is growth with rising friction.",
                    "question": "How should investors weight Temu?",
                    "answer": "Overseas GMV impresses but tariffs and local compliance raise strike price on profitability — PDD Watch requires per-market unit economics, not blended growth slides. Failure mode is buying narrative at peak Temu optimism.",
                },
                {
                    "view": "Earnings dips can be entry if moat holds.",
                    "question": "What is Curated 50 discipline here?",
                    "answer": "Yongqing reviews PDD after volatility — if active buyers and wallet share rise while market panics on margin, mispricing emerges. Abacus over sentiment; avoid catching falling knives if subsidy war structurally hurts take rate.",
                },
            ],
            "top_investment_implications": [
                {
                    "ticker": "PDD",
                    "direction": "Watch",
                    "confidence": "Medium",
                    "thesis": "Pinduoduo (PDD): Yongqing competitive-edge and earnings framework — Watch take rate and Temu unit economics post-volatility",
                },
            ],
            "golden_quotes": [
                "拼多多的护城河在供应链效率，不在打折标签。",
                "Temu是增长期权，但关税和合规成本正在抬高盈利门槛。",
                "财报波动是试金石，关键看活跃买家和人均GMV是不是还在涨。",
            ],
            "chronology": {
                "subject": "Yongqing · PDD Deep Dive",
                "events": [
                    {"date": "2015–2018", "event": "PDD rise via social commerce and C2M"},
                    {"date": "2022–2023", "event": "Temu overseas launch"},
                    {"date": "2024–2025", "event": "Tariff and compliance headwinds on Temu"},
                    {"date": "2025-04-28", "event": "PDD earnings and competitive review session"},
                    {"date": "2025-04-30", "event": "Episode 115 published"},
                ],
            },
        },
        "zh": {
            "keywords": ["PDD", "Temu", "电商", "财报"],
            "conclusion": "永庆 2025 年 4 月 28 日拼多多深度框架将拼多多（PDD）定为供应链效率加商家生态——非折扣噱头。Temu 海外增增长但法律与物流成本升；投资者应观望 PDD 抽佣稳定、人均 GMV 与 Temu 单位经济学。精选 50 纪律：买错价优质资产，非叙事峰值。",
            "background": "投资实战派第 115 期复盘 PDD 竞争优势、财报与市场情绪（2025 年 4 月 30 日发布）。永庆框架：拼多多凭 C2M 反向路由、游戏化互动与补贴纪律胜出——对手复制慢。Temu 扩海外 GMV 但面临关税、合规与履约成本逆风——毛利 mix 重于 headline 增长。节目重温投资清单：护城河耐久、管理层资本配置、相对阿里京东估值。",
            "important_facts": [
                "竞争优势：拼多多（PDD）商家入驻与推荐算法降 SKU 成本——供应链深度胜纯价格战。观望抽佣与广告收入能否抵消补贴随 hypergrowth 正常化。",
                "Temu 算术：海外扩张买 GMV 但物流与监管成本压毛利——永庆强调分市场单位经济学非 blended GMV 图。若 Temu 烧钱无贡献利润路径则 PDD 论点破裂。",
                "财报解读：财报后波动常错价 durably 人均 GMV——精选 50 在护城河完好时弱势加仓。对比 PDD 活跃买家增长与钱包份额对中国消费宏观。",
            ],
            "mental_model": {
                "name": "C2M 效率 × Temu 期权 × 财报错价",
                "components": "拼多多护城河是供应链加互动飞轮非仅券。Temu 是行权价上升的看涨期权（合规成本）。单位经济学完好时恐惧买优质。",
                "application": "拼多多（PDD）：观望国内抽佣与 Temu 贡献毛利——仅相对人均 GMV 趋势错价时看多。若补贴战持续侵蚀商家 ROI 则减仓。",
            },
            "key_insights": [
                {
                    "view": "护城河在供应链非折扣标签。",
                    "question": "PDD 真正竞争优势是什么？",
                    "answer": "永庆称 C2M 路由与算法商家匹配降落地成本——对手可复制 UI 非一夜复制生态深度。投资框架跟商家留存与履约效率，非仅 GMV headline。",
                },
                {
                    "view": "Temu 是增长伴摩擦上升。",
                    "question": "投资者如何加权 Temu？",
                    "answer": "海外 GMV 亮眼但关税与本地合规抬盈利行权价——拼多多（PDD）观望需分市场单位经济学非 blended 增长幻灯片。失败模式是 Temu 乐观峰值买叙事。",
                },
                {
                    "view": "财报下挫若护城河在可为入场。",
                    "question": "此处精选 50 纪律是什么？",
                    "answer": "永庆财报波动后复盘——若活跃买家与钱包份额升而市场恐慌毛利，错价浮现。算盘胜情绪；若补贴战结构性伤抽佣勿接飞刀。",
                },
            ],
            "top_investment_implications": [
                {
                    "ticker": "PDD",
                    "direction": "Watch",
                    "confidence": "Medium",
                    "thesis": "拼多多（PDD）：永庆竞争优势与财报框架——观望抽佣与 Temu 单位经济学于波动后",
                },
            ],
            "golden_quotes": ["或者是廣告投放體系本身也是拼多多的收入體系", "讓它把自己的這種產業帶上的規模化生產的能力", "成為國外一個品牌的一個代工方的這個情況存在"],
            "chronology": {
                "subject": "永庆 · 拼多多深度",
                "events": [
                    {"date": "2015–2018", "event": "拼多多凭社交电商与 C2M 崛起"},
                    {"date": "2022–2023", "event": "Temu 海外上线"},
                    {"date": "2024–2025", "event": "Temu 关税与合规逆风"},
                    {"date": "2025-04-28", "event": "PDD 财报与竞争复盘场次"},
                    {"date": "2025-04-30", "event": "第 115 期发布"},
                ],
            },
        },
    },
    "tzs-ep109": {
        "en": {
            "keywords": ["3690.HK", "Meituan", "Local Services", "Delivery"],
            "conclusion": "David's Curated 50 Meituan episode frames 3690.HK as local-commerce infrastructure — delivery density, merchant ad spend, and in-store digitization — under Douyin local-services attack. Profitability improved but competition caps take rate; investors should Watch Meituan (3690.HK) on order growth, operating margin, and instant-retail mix versus content-platform subsidies.",
            "background": "Practical Investments ep.109 (Apr 2, 2025) dissects Meituan business model, earnings, and investment view. David explains flywheel: more riders and merchants lower unit delivery cost; ads and SaaS monetize merchant lock-in. Risks: Douyin and Alibaba local deals subsidize entry; instant retail (闪购) raises AOV but capital intensive. Episode maps 3690.HK as oligopoly play on China's offline-to-online habit — wins if operating leverage returns without endless price war.",
            "important_facts": [
                "Infrastructure thesis: Meituan owns last-mile density — rider network and merchant POS integration create switching costs. 3690.HK Watch on delivery orders per rider and unit cost trend as instant retail scales.",
                "Competition frame: Content platforms buy GMV with subsidies — Meituan must defend frequency merchants, not just price. David tracks ad revenue and in-store数字化 as margin levers when delivery fees compress.",
                "Earnings lens: Post-2024 profitability focus shifts to sustainable operating margin — investors weigh闪购 capex against food delivery cash cow. Underweight if subsidy war forces structural margin give-up.",
            ],
            "mental_model": {
                "name": "Delivery Density × Merchant Lock-In × Subsidy Defense",
                "components": "Local commerce winner needs logistic scale plus merchant SaaS. Competitors buy traffic; Meituan defends habit and data. Profitability is margin discipline, not GMV at any cost.",
                "application": "Meituan (3690.HK): Watch order frequency and operating margin — Long thesis needs ad plus闪购 mix improving without Douyin forcing permanent subsidies. Trim on rider cost inflation without AOV lift.",
            },
            "key_insights": [
                {
                    "view": "Meituan is local-commerce OS.",
                    "question": "What is the core business model?",
                    "answer": "David frames delivery as infrastructure — density lowers cost per order; merchant ads and数字化 monetize lock-in. 3690.HK is not food app alone but offline merchant operating system.",
                },
                {
                    "view": "Douyin attack is subsidy, not product.",
                    "question": "How serious is content-platform competition?",
                    "answer": "Rivals buy local-services GMV with content traffic — Meituan defends with habit, rider speed, and merchant tools. Watch whether Meituan must match subsidies or can win on fulfillment reliability.",
                },
                {
                    "view": "闪购 raises stakes on capital efficiency.",
                    "question": "What changed post-profitability pivot?",
                    "answer": "Instant retail lifts basket size but needs inventory and rider utilization — David wants operating margin proof, not GMV reclaim at any cost. 3690.HK investors track闪购 contribution versus core delivery cash flow.",
                },
            ],
            "top_investment_implications": [
                {
                    "ticker": "3690.HK",
                    "direction": "Watch",
                    "confidence": "Medium",
                    "thesis": "Meituan (3690.HK): David business-model episode — Watch delivery density, operating margin, and subsidy defense vs Douyin",
                },
            ],
            "golden_quotes": [
                "美团本质上是本地商业的基础设施，不是单纯的外卖App。",
                "抖音用补贴买GMV，美团要靠履约效率和商家工具来守城。",
                "闪购提升客单价，但考验的是骑手人效和库存周转。",
            ],
            "chronology": {
                "subject": "David · Meituan Curated 50",
                "events": [
                    {"date": "2010s", "event": "Meituan scales food delivery density"},
                    {"date": "2018", "event": "3690.HK IPO; local services expansion"},
                    {"date": "2023–2024", "event": "Douyin local-services competition intensifies"},
                    {"date": "2025", "event": "Profitability and闪购 mix focus"},
                    {"date": "2025-04-02", "event": "Episode 109 recorded"},
                ],
            },
        },
        "zh": {
            "keywords": ["3690.HK", "美团", "本地生活", "外卖"],
            "conclusion": "大卫精选 50 美团节目将美团（3690.HK）框为本地商业基础设施——配送密度、商家广告与到店数字化——在抖音本地生活进攻下。盈利改善但竞争压制抽佣；投资者应观望美团（3690.HK）订单增长、经营利润率与即时零售 mix 对内容平台补贴。",
            "background": "投资实战派第 109 期（2025 年 4 月 2 日）拆解美团商业模式、财报与投资观点。大卫解释飞轮：更多骑手与商家降单均配送成本；广告与 SaaS 变现商家锁定。风险：抖音与阿里本地团购补贴入场；闪购抬客单价但资本密集。节目将美团（3690.HK）映射为中国线下线上习惯寡头玩法——若经营杠杆回归且非 endless 价格战则胜。",
            "important_facts": [
                "基础设施论点：美团握最后一公里密度——骑手网与商家 POS 整合造切换成本。美团（3690.HK）观望单骑手订单量与单位成本趋势随闪购规模化。",
                "竞争框架：内容平台用补贴买 GMV——美团须守商家频次非仅价。大卫跟广告收入与到店数字化作配送费压缩时的毛利杠杆。",
                "财报透镜：2024 后盈利聚焦转向可持续经营利润率——投资者权衡闪购 capex 对外卖现金牛。若补贴战迫结构性让利则低配。",
            ],
            "mental_model": {
                "name": "配送密度 × 商家锁定 × 补贴防守",
                "components": "本地生活赢家要物流规模加商家 SaaS。竞争者买流量；美团守习惯与数据。盈利是毛利纪律非不惜代价 GMV。",
                "application": "美团（3690.HK）：观望订单频次与经营利润率——看多需广告加闪购 mix 改善且抖音未迫永久补贴。骑手成本通胀无客单价抬升则减仓。",
            },
            "key_insights": [
                {
                    "view": "美团是本地商业 OS。",
                    "question": "核心商业模式是什么？",
                    "answer": "大卫框配送为基础设施——密度降单均成本；广告与数字化变现锁定。美团（3690.HK）非仅餐饮 App 而是线下商家操作系统。",
                },
                {
                    "view": "抖音进攻是补贴非产品。",
                    "question": "内容平台竞争多严重？",
                    "answer": "对手用内容流量补贴本地 GMV——美团以习惯、骑手速度与商家工具守城。观望美团是否须匹配补贴或以履约可靠胜。",
                },
                {
                    "view": "闪购抬高资本效率赌注。",
                    "question": "盈利 pivot 后何变？",
                    "answer": "即时零售抬篮但需库存与骑手利用率——大卫要经营利润率验证非不惜代价夺回 GMV。美团（3690.HK）投资者跟闪购贡献对核心配送现金流。",
                },
            ],
            "top_investment_implications": [
                {
                    "ticker": "3690.HK",
                    "direction": "Watch",
                    "confidence": "Medium",
                    "thesis": "美团（3690.HK）：大卫商业模式节目——观望配送密度、经营利润率与对抖音补贴防守",
                },
            ],
            "golden_quotes": ["就是我们就不需要把他们前面的业务", "待会儿我跟永庆和海塔我们在这个过程当中会再做一个深入探讨。", "我觉得散购可能会是为数不多的那种肉眼可见的量领的业态了,"],
            "chronology": {
                "subject": "大卫 · 美团精选 50",
                "events": [
                    {"date": "2010s", "event": "美团规模化外卖密度"},
                    {"date": "2018", "event": "3690.HK 上市；本地服务扩张"},
                    {"date": "2023–2024", "event": "抖音本地生活竞争加剧"},
                    {"date": "2025", "event": "盈利与闪购 mix 聚焦"},
                    {"date": "2025-04-02", "event": "第 109 期录制"},
                ],
            },
        },
    },
    "tzs-ep34": {
        "en": {
            "keywords": ["LI", "EV", "Intelligent Driving", "Valuation"],
            "conclusion": "David's 2024 Li Auto deep dive asks whether Li Xiang can win the second war — BEV platform shift plus intelligent-driving differentiation — and prices LI investment value versus risks. Family SUV niche and execution history support Watch; margin compression and AD catch-up costs threaten Long. Investors should track delivery cadence, software revenue mix, and BEV model success as proof of second-act thesis.",
            "background": "Practical Investments ep.34 (Apr 14, 2024) in the Global 50 series dissects Li Auto: Li Xiang's product focus (奶爸 family SUV), hybrid-to-BEV transition, and autonomous-driving bet. David weighs strengths — capital discipline, hit products L-series, brand in premium family segment — against risks: intensifying EV price war, Tesla/BYD tech lead, and need to monetize AD. Valuation frame compares LI PE and delivery growth to XPEV and BYD; second war is proving BEV platforms and AD are not one-hit wonder.",
            "important_facts": [
                "Second war defined: First war was surviving and scaling extended-range SUVs; second is BEV-native models plus AD software differentiation. Li Auto (LI) Watch on MEGA/BEV reception and whether Li Xiang retains product hit rate as market commoditizes.",
                "Execution premium: Li Xiang's focus and capital allocation historically beat Chinese EV peers — David credits clear customer definition (family) versus sprawling lineups. Risk is AD spend without FSD-like monetization timeline.",
                "Valuation tension: LI traded growth premium when deliveries surged — investors need gross margin stability through price war and rising software attach. Underweight if BEV pivot dilutes brand or AD lags Tesla benchmark Lang Xianpeng cites.",
            ],
            "mental_model": {
                "name": "Product Hit Rate × BEV Transition × AD Monetization",
                "components": "Li Auto won first war on focused SKUs; second war needs BEV plus software. Founder execution is moat until platform commoditizes. AD is cost center until miles monetize.",
                "application": "Li Auto (LI): Watch BEV model orders and software revenue mix — Long requires second-hit product and margin hold. Trim if price war forces sustained ASP collapse without AD offset.",
            },
            "key_insights": [
                {
                    "view": "Second war is BEV plus AD, not more hybrids.",
                    "question": "What is Li Auto's critical next phase?",
                    "answer": "David frames 2024+ as proving pure electric platforms and intelligent driving — hybrid success does not guarantee BEV copy. LI thesis lives on whether Li Xiang repeats product clarity in new powertrain era.",
                },
                {
                    "view": "Li Xiang execution is the core moat.",
                    "question": "Why did LI outperform many EV peers historically?",
                    "answer": "Focused 奶爸 segment and disciplined SKUs — David contrasts with sprawling OEM lineups. Execution premium fades if BEV models miss or AD spend lacks revenue path.",
                },
                {
                    "view": "Valuation needs margin plus AD proof.",
                    "question": "How should investors price LI in price war?",
                    "answer": "Delivery growth alone insufficient — gross margin stability and AD differentiation versus Tesla/BYD set fair multiple. Watch is default until BEV second act and software mix confirm.",
                },
            ],
            "top_investment_implications": [
                {
                    "ticker": "LI",
                    "direction": "Watch",
                    "confidence": "Medium",
                    "thesis": "Li Auto (LI): David Global 50 deep dive — Watch BEV second war, delivery cadence, and AD monetization versus price-war margin risk",
                },
            ],
            "golden_quotes": [
                "理想第一场战争是活下来并做成奶爸SUV，第二场是纯电平台和智能驾驶。",
                "李想的执行力是理想最核心的护城河，但电动车价格战正在考验这门护城河。",
                "估值不能只看交付增速，要看毛利率和软件收入能不能跟上。",
            ],
            "chronology": {
                "subject": "David · Li Auto Global 50",
                "events": [
                    {"date": "2021–2023", "event": "L-series scale; LI delivery surge"},
                    {"date": "2024", "event": "MEGA launch; BEV platform pivot debate"},
                    {"date": "2024", "event": "China EV price war intensifies"},
                    {"date": "2024-04-14", "event": "Episode 34 Li Auto deep dive recorded"},
                    {"date": "2025+", "event": "AD stack and BEV models prove second war"},
                ],
            },
        },
        "zh": {
            "keywords": ["LI", "新能源汽车", "智能驾驶", "估值"],
            "conclusion": "大卫 2024 年理想汽车深度问李想能否打赢第二场战争——纯电平台转型加智驾差异化——并定价理想（LI）投资价值与风险。家庭 SUV 细分与执行史支持观望；毛利压缩与智驾追赶成本威胁看多。投资者应跟踪交付节奏、软件收入占比与纯电车型成功作第二幕验证。",
            "background": "投资实战派第 34 期（2024 年 4 月 14 日）全球 50 系列拆解理想汽车：李想产品聚焦（奶爸家庭 SUV）、增程向纯电过渡与自动驾驶赌注。大卫权衡优势——资本纪律、L 系列爆款、高端家庭细分品牌——对风险：加剧的 EV 价格战、特斯拉/比亚迪技术领先、AD 变现需求。估值框架对比理想（LI）PE 与交付增长对 XPEV、比亚迪；第二战是证纯电平台与 AD 非昙花一现。",
            "important_facts": [
                "第二战定义：第一战是存活并规模化增程 SUV；第二是纯电原生车型加 AD 软件差异化。理想（LI）观望 MEGA/纯电接受度与李想在市场商品化时是否保持爆款率。",
                "执行溢价：李想聚焦与资本配置历史上胜中国 EV peer——大卫赞清晰客户定义（家庭）对 sprawling 产品线。风险是 AD 投入无 FSD 级变现时间表。",
                "估值张力：交付 surge 时 LI 享增长溢价——投资者需价格战中的毛利稳定与软件 attach 升。若纯电 pivot 稀释品牌或 AD 落后特斯拉基准则低配。",
            ],
            "mental_model": {
                "name": "爆款率 × 纯电过渡 × AD 变现",
                "components": "理想第一战靠聚焦 SKU 胜；第二战要纯电加软件。创始人执行是护城河直至平台商品化。AD 在里程变现前是成本中心。",
                "application": "理想（LI）：观望纯电车型订单与软件收入 mix——看多需第二款爆款与毛利守住。若价格战迫持续 ASP 崩且无 AD 对冲则减仓。",
            },
            "key_insights": [
                {
                    "view": "第二战是纯电加 AD，非更多增程。",
                    "question": "理想关键下一阶段是什么？",
                    "answer": "大卫框 2024+ 为证纯电平台与智驾——增程成功不保证纯电复制。理想（LI）论点系李想能否在新动力时代重复产品清晰。",
                },
                {
                    "view": "李想执行是核心护城河。",
                    "question": "为何 LI 历史上胜多数 EV peer？",
                    "answer": "聚焦奶爸细分与纪律 SKU——大卫对比 sprawling OEM 产品线。若纯电 miss 或 AD 投入无收入路径则执行溢价消退。",
                },
                {
                    "view": "估值需毛利加 AD 验证。",
                    "question": "价格战下如何给 LI 定价？",
                    "answer": "仅交付增长不够——毛利稳定与相对特斯拉/比亚迪 AD 差异化定合理倍数。默认观望直至纯电第二幕与软件 mix 确认。",
                },
            ],
            "top_investment_implications": [
                {
                    "ticker": "LI",
                    "direction": "Watch",
                    "confidence": "Medium",
                    "thesis": "理想（LI）：大卫全球 50 深度——观望纯电第二战、交付节奏与 AD 变现对价格战毛利风险",
                },
            ],
            "golden_quotes": ["所以其实对我们传统的零部件供应商的响应速度的要求", "他们都是采取了一个高度的垂直供应链的整合的战略", "我就谈一谈我们作为供应链跟他们打交道的一些体验"],
            "chronology": {
                "subject": "大卫 · 理想汽车全球 50",
                "events": [
                    {"date": "2021–2023", "event": "L 系列规模化；LI 交付 surge"},
                    {"date": "2024", "event": "MEGA 发布；纯电平台 pivot 争论"},
                    {"date": "2024", "event": "中国 EV 价格战加剧"},
                    {"date": "2024-04-14", "event": "第 34 期理想深度录制"},
                    {"date": "2025+", "event": "AD 栈与纯电车型证第二战"},
                ],
            },
        },
    },
}
