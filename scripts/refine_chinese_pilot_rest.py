"""Episode body content for refine_chinese_pilot.py (transcript-verified)."""

from typing import Any

REFINED: dict[str, dict[str, dict[str, Any]]] = {
    "zj-ep144": {
        "zh": {
            "keywords": ["300866.SZ", "浅海战略", "AI 组织"],
            "conclusion": (
                "阳萌框架：安克市值 600 亿+ 人民币，坚持浅海（TAM <500 亿美元品类，如充电宝约 50 亿、耳机 2000–3000 亿）"
                "vs 深海（手机约 5000 亿、PC 约 2000 亿）。毛利率每年提升 1.1–1.5 个百分点是复利引擎。"
                "十亿 token context 可「读完」一家公司，改变 research 与决策。2011 年创立，曾获 Google Founders Award。"
                "对投资者：300866.SZ 看品类扩张 ROIC、毛利率 trajectory 与 Amazon 渠道依赖。"
            ),
            "background": (
                "三小时对话中，阳萌复盘安克从 2011 年创立（Google Founders Award）到市值 600 亿+ 人民币的路径。"
                "「浅海战略」：优先 TAM 约 500 亿美元以下、可建品类领导的赛道——充电宝 TAM 约 50 亿美元，"
                "耳机约 2000–3000 亿美元；深海如手机约 5000 亿、PC 约 2000 亿，巨头林立，安克主动回避。"
                "历史上毛利率每年约提升 1.1–1.5 个百分点。2025–2026 年 AI 渗透产品定义与内部知识管理；"
                "context 向十亿 token 演进，理论上可 ingest 财报、供应链、用户评论全集以理解一家公司。"
            ),
            "important_facts": [
                (
                    "安克市值已达 600 亿人民币以上；阳萌 2011 年创立公司，早期曾获 Google Founders Award。"
                    "品类选择比规模更重要：浅海目标常限定 TAM 约 500 亿美元以下——充电宝约 50 亿美元、"
                    "耳机约 2000–3000 亿美元（$200–300B），够大能养出第一，不够大引不来全部巨头。"
                ),
                (
                    "「深海」指手机（约 5000 亿美元）、PC（约 2000 亿美元）等红海，安克回避正面冲突。"
                    "浅海=竞争未固化、用户痛点清晰、凭产品与设计拿 category leader。"
                    "历史上毛利率每年约提升 1.1–1.5 个百分点，来自品牌溢价、供应链优化与 SKU 结构升级。"
                ),
                (
                    "阳萌描述 AI 组织变革：内部知识、用户反馈、竞品情报可被 LLM 整合；"
                    "context window 向十亿 token 演进，理解一家公司的边际成本骤降。"
                    "他暗示安克已在内部试验——领先应用 AI 的消费品牌可能获决策速度优势。"
                ),
            ],
            "mental_model": {
                "name": "浅海品类 × 毛利率复利 × 十亿 token 研究",
                "components": (
                    "选市场：TAM 适中（<~500 亿美元）、竞争未封死、产品力可拿第一。"
                    "做组织：十亿 token context 把分散文档变成可查询知识，缩短 insight 到 action。"
                    "看财务：毛利率年化 +1.1–1.5pt 比收入增速更能证明 brand moat。"
                    "深海（手机 5000 亿、PC 2000 亿）留给巨头，浅海（充电宝 50 亿、耳机 2000–3000 亿）养品类王。"
                ),
                "application": (
                    "投资映射：① 300866.SZ 估值 tied to 新品类 ROIC 与毛利率 trajectory；"
                    "② 浅海逻辑对标 DTC vs 平台依赖——跟踪 Amazon 占比；"
                    "③ AI 若提升决策效率，应体现在 faster SKU 迭代与 SG&A 效率。"
                    "600 亿+ 市值意味着 execution 已验证，下一章看 adjacent 品类命中率。"
                ),
            },
            "key_insights": [
                {
                    "view": "好生意常在「不够大」的市场——500 亿美元 TAM 是 mental ceiling。",
                    "question": "为何不直接打手机、笔记本等超级大盘？",
                    "answer": (
                        "手机约 5000 亿、PC 约 2000 亿深海吸引巨头全资源；"
                        "充电宝约 50 亿、耳机 2000–3000 亿浅海允许 2–3 年成品类第一再 adjacent expansion。"
                        "这与颠覆逻辑一致，但执行更偏品牌与产品而非纯低价。"
                    ),
                },
                {
                    "view": "十亿 token context 可能改写理解公司的 economics。",
                    "question": "对投资者意味着什么？",
                    "answer": (
                        "若模型 ingest 财报、供应链、评论、专利全集，research 边际成本下降，"
                        "alpha 转向问对问题与 judgment。阳萌暗示安克内部已试验；"
                        "消费品牌若领先 AI 应用或获决策速度优势，应体现在毛利率与 SKU 周期。"
                    ),
                },
                {
                    "view": "毛利率 +1.1–1.5pt/年 是最应 respect 的指标。",
                    "question": "如何验证浅海战略？",
                    "answer": (
                        "收入增速会波动，但 sustained gross margin expansion 说明定价权改善。"
                        "投资者警惕毛利率 flatten 或 SG&A 飙升——可能是浅海红利耗尽或品类扩张失焦。"
                        "600 亿+ 市值下 margin 轨迹比单季收入更重要。"
                    ),
                },
            ],
            "top_investment_implications": [
                {
                    "ticker": "300866.SZ",
                    "direction": "Long",
                    "confidence": "Medium",
                    "thesis": (
                        "Category expansion + brand premium + ~1.1–1.5pt annual gross margin lift at 600 亿+ RMB cap; "
                        "track new category hit rate and Amazon concentration"
                    ),
                },
                {
                    "ticker": "AMZN",
                    "direction": "Short",
                    "confidence": "Medium",
                    "thesis": (
                        "Anker remains Amazon-native; platform policy, ads cost, and private-label competition "
                        "directly affect 300866 margins despite shallow-sea category wins"
                    ),
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
                    {"date": "2011", "event": "阳萌创立 Anker；获 Google Founders Award"},
                    {"date": "2016–2020", "event": "多品类扩张，浅海战略成型"},
                    {"date": "2020", "event": "安克创新深交所上市 (300866.SZ)"},
                    {"date": "2021–2025", "event": "毛利率年化 +1.1–1.5pt；市值突破 600 亿 RMB"},
                    {"date": "2025–2026", "event": "AI 组织变革与十亿 token 研究框架提出"},
                ],
            },
        },
        "en": {
            "keywords": ["300866.SZ", "Shallow-Sea Strategy", "AI Organization"],
            "conclusion": (
                "Yang's framework: Anker at RMB 60B+ market cap plays shallow sea (categories under ~$500B TAM — "
                "power banks ~$5B, earphones ~$200–300B) vs deep sea (phones ~$500B, PCs ~$200B). "
                "+1.1–1.5pt annual gross margin lift is the compounding engine. Billion-token context can 'read' "
                "a whole company. Founded 2011, Google Founders Award. For investors: 300866.SZ on ROIC, margins, Amazon mix."
            ),
            "background": (
                "In a three-hour talk Yang retraces Anker since founding in 2011 (Google Founders Award) to RMB 60B+ cap. "
                "Shallow-sea strategy targets categories under ~$500B TAM — power banks ~$5B, earphones ~$200–300B — "
                "avoiding deep sea like phones (~$500B) and PCs (~$200B) where giants deploy full resources. "
                "Gross margin rises ~1.1–1.5 points per year historically. By 2025–26 AI penetrates product and knowledge work; "
                "context windows toward a billion tokens could ingest filings, supply chain, and reviews to understand a firm."
            ),
            "important_facts": [
                (
                    "Anker's market cap exceeds RMB 60B; Yang founded in 2011 and won a Google Founders Award early on. "
                    "Category choice beats raw scale: shallow-sea targets often sit below ~$500B TAM — power banks ~$5B, "
                    "earphones ~$200–300B — big enough for a leader, small enough that not every giant shows up."
                ),
                (
                    "Deep sea means phones (~$500B) and PCs (~$200B) red oceans Anker avoids. "
                    "Shallow sea = open competition, clear pain points, product/design can win #1. "
                    "Gross margin historically lifts ~1.1–1.5 points per year via brand, supply chain, and SKU mix."
                ),
                (
                    "Yang describes AI org change: internal knowledge, feedback, and competitive intel unified in LLM workflows; "
                    "context toward a billion tokens collapses the cost of understanding a company. "
                    "Anker is already experimenting — leading AI adopters in consumer brands may gain decision-speed edge."
                ),
            ],
            "mental_model": {
                "name": "Shallow-Sea Category × Gross-Margin Compounding × Billion-Token Research",
                "components": (
                    "Pick markets: moderate TAM (<~$500B), open structure, product can win #1. "
                    "Run org: billion-token context turns docs into queryable knowledge. "
                    "Read financials: +1.1–1.5pt annual gross margin proves brand moat more than volatile revenue. "
                    "Deep sea (phones $500B, PCs $200B) for giants; shallow sea (power banks $5B, earphones $200–300B) breeds leaders."
                ),
                "application": (
                    "Investing lens: (1) 300866.SZ on new-category ROIC and margin trajectory; "
                    "(2) shallow-sea vs Amazon dependence — track channel mix; "
                    "(3) AI decision gains should show in SKU cycles and SG&A. "
                    "At RMB 60B+ cap, execution is proven — next chapter is adjacent category hit rate."
                ),
            },
            "key_insights": [
                {
                    "view": "Great businesses hide in markets that aren't mega-sized — ~$500B TAM is a mental ceiling.",
                    "question": "Why not attack phones and PCs directly?",
                    "answer": (
                        "Phones ~$500B and PCs ~$200B deep sea attract full giant resources; "
                        "power banks ~$5B and earphones ~$200–300B shallow seas allow #1 in 2–3 years then adjacent moves. "
                        "Brand and product execution, not pure low price."
                    ),
                },
                {
                    "view": "Billion-token context may rewrite company-understanding economics.",
                    "question": "What does that mean for investors?",
                    "answer": (
                        "If models ingest filings, supply chain, reviews, and patents, research marginal cost falls — "
                        "alpha shifts to questions and judgment. Yang hints Anker experiments internally; "
                        "margin trajectory and SKU velocity should reflect AI-led decision speed."
                    ),
                },
                {
                    "view": "+1.1–1.5pt/year gross margin is Anker's most respect-worthy metric.",
                    "question": "How validate shallow-sea strategy?",
                    "answer": (
                        "Revenue wobbles; sustained gross-margin expansion proves pricing power. "
                        "Flattening margins or SG&A spikes may signal shallow-sea exhaustion or sprawl. "
                        "At RMB 60B+ cap, margin path beats single-quarter revenue."
                    ),
                },
            ],
            "top_investment_implications": [
                {
                    "ticker": "300866.SZ",
                    "direction": "Long",
                    "confidence": "Medium",
                    "thesis": (
                        "Category expansion + brand premium + ~1.1–1.5pt annual gross margin at RMB 60B+ cap; "
                        "track new category hit rate and Amazon concentration"
                    ),
                },
                {
                    "ticker": "AMZN",
                    "direction": "Short",
                    "confidence": "Medium",
                    "thesis": (
                        "Anker remains Amazon-native; platform policy, ad costs, and private-label competition "
                        "directly affect 300866 margins despite shallow-sea wins"
                    ),
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
                    {"date": "2011", "event": "Yang founds Anker; Google Founders Award"},
                    {"date": "2016–20", "event": "Multi-category expansion; shallow-sea strategy crystallizes"},
                    {"date": "2020", "event": "Anker Innovations lists on Shenzhen exchange (300866.SZ)"},
                    {"date": "2021–25", "event": "Gross margin +1.1–1.5pt/year; market cap crosses RMB 60B"},
                    {"date": "2025–26", "event": "AI org transformation and billion-token research frame emerge"},
                ],
            },
        },
    },
    "tzs-ep180": {
        "zh": {
            "keywords": ["9992.HK", "IP 消费", "估值"],
            "conclusion": (
                "大卫主持、Jeff 嘉宾（2026-03-31 录制）复盘泡泡玛特：2025 营收 371 亿人民币（+184.7%）、"
                "净利润 130 亿（+29.3%），但 2026 指引约 20% 增速（「急刹车」）触发两日股价约跌 30%。"
                "股价约 142–143 港元，市值低于 2000 亿港币；节目对比 Disney PE 约 14 倍。"
                "对投资者：9992.HK 需分离 Labubu 现象与 IP pipeline，高 PE 对 guidance 误差零容忍。"
            ),
            "background": (
                "大卫主持、Jeff 嘉宾，节目 2026 年 3 月 31 日录制，讨论泡泡玛特 2025 业绩与 2026 指引落差。"
                "营收 371 亿人民币同比 +184.7%，净利润 130 亿人民币同比 +29.3%——增长仍强但利润增速远低于收入。"
                "管理层 2026 年指引约 20% 增长，相对 2025 基数显著降速，市场两日股价跌约 30%。"
                "股价约 142–143 港元，市值跌破 2000 亿港币。嘉宾辩论 IP 潮玩 vs 时尚周期，"
                "并以 Disney 约 14 倍 PE 作估值参照。"
            ),
            "important_facts": [
                (
                    "2025 年营收 371 亿人民币，同比 +184.7%；净利润 130 亿人民币，同比 +29.3%。"
                    "2026 年管理层指引约 20% 收入增长——相对 2025 高基数「急刹车」，"
                    "触发估值杀：公告后约两个交易日股价跌约 30%。"
                ),
                (
                    "股价约 142–143 港元，市值低于 2000 亿港币（约 2000 亿港元以下）。"
                    "Labubu 等超级 IP 贡献大量增量，但单一 IP 集中度引发 fad vs character equity 争论。"
                    "海外扩张是第二曲线，本地化与渠道成本可能稀释 near-term margin。"
                ),
                (
                    "PE 辩论：bull 看 Disney/Hello Kitty 式 IP 复利；节目引用 Disney PE 约 14 倍作参照，"
                    "bear 看潮流周期与库存风险。高 PE 消费股对 guidance 误差惩罚极重——"
                    "从 +184% 到约 20%，叙事切换大于基本面微调。"
                ),
            ],
            "mental_model": {
                "name": "IP 复利 × 时尚周期 × Guidance 敏感度",
                "components": (
                    "Character 跨代际则值 Disney 倍数；潮流单品则值 fast-fashion 倍数。"
                    "Hyper-growth 后首次 guidance 降速是消费高 PE 最危险时刻——371 亿营收 +184.7% 设下 impossible bar。"
                    "净利润 +29.3% 低于收入增速提示 margin 与费用结构压力。"
                ),
                "application": (
                    "投资映射：① 9992.HK 看 IP pipeline 宽度、复购与会员；"
                    "② 股价 142–143 港元、市值 <2000 亿 HKD 后 multiple 从叙事 peak 回归；"
                    "③ Disney ~14x PE 是节目锚点，bull/bear 对 IP 持久性分歧决定溢价空间。"
                    "2026 约 20% guide 若 execute 仍优秀，但 position sizing 宜低于传统 compounder。"
                ),
            },
            "key_insights": [
                {
                    "view": "371 亿营收证明运营，净利润 +29.3% 不证明 perpetual hyper-growth。",
                    "question": "为何股价对约 20% guide 反应剧烈？",
                    "answer": (
                        "2025 +184.7% 设定 impossible bar；两日跌约 30% 显示 narrative 断裂。"
                        "资金在 peak 时给 peak multiple。Guide 降速 = 叙事切换。"
                        "投资者应预期 transition year volatility 放大，用 scenario table 而非单点 EPS。"
                    ),
                },
                {
                    "view": "IP vs 时尚是估值分叉点；Disney ~14x PE 是节目参照。",
                    "question": "如何判断 Labubu 属于哪一类？",
                    "answer": (
                        "多代产品、跨品类授权、海外自发传播 = IP 信号；"
                        "单季爆款、二手价崩盘 = 时尚信号。证据 mixed 是 bull/bear 分歧根源。"
                        "节目以 Disney 约 14 倍 PE 对比泡泡玛特当时溢价，争论 IP 是否支撑更高倍数。"
                    ),
                },
                {
                    "view": "市值跌破 2000 亿 HKD、股价 142–143 港元后，高 PE 对 miss 零容忍。",
                    "question": "实操框架？",
                    "answer": (
                        "Position sizing 低于 traditional compounder；bull/base/bear scenario。"
                        "任何 quarter miss 可 trigger 20–30% drawdown——9992 已演示。"
                        "跟踪同店、海外占比、IP 续约；分离 Labubu 现象与 pipeline 广度。"
                    ),
                },
            ],
            "top_investment_implications": [
                {
                    "ticker": "9992.HK",
                    "direction": "Long",
                    "confidence": "Medium",
                    "thesis": (
                        "Post-guide shock: ~20% 2026 growth, stock ~142–143 HKD, mcap <200B HKD after ~30% two-day drop; "
                        "IP pipeline breadth needed to sustain premium vs Disney ~14x anchor"
                    ),
                },
                {
                    "ticker": "DIS",
                    "direction": "Long",
                    "confidence": "Low",
                    "thesis": (
                        "Episode comps POP MART to character-IP compounders at Disney ~14x PE; "
                        "Disney park + media flywheel sets ceiling on pure toy/IP earnings power"
                    ),
                },
            ],
            "golden_quotes": [
                "371 亿营收是事实，净利润 130 亿——但市场买的是未来，从 184% 到 20%，叙事断了。",
                "两天跌三成，说明高 PE 消费股最怕「没那么好」。",
                "IP 和时尚的区别，三年后再看 Labubu 还在不在货架上。",
            ],
            "chronology": {
                "subject": "泡泡玛特 · 2025 业绩与估值回调",
                "events": [
                    {"date": "2020", "event": "泡泡玛特港交所上市 (9992.HK)"},
                    {"date": "2023–2024", "event": "Labubu 等 IP 全球化，营收加速"},
                    {"date": "2025", "event": "营收 371 亿 RMB (+184.7%)；净利润 130 亿 (+29.3%)"},
                    {"date": "2026-03-31", "event": "大卫与 Jeff 录制节目，讨论业绩与估值"},
                    {"date": "2026 Q1", "event": "2026 指引约 20%；两日股价跌约 30%；股价约 142–143 HKD"},
                ],
            },
        },
        "en": {
            "keywords": ["9992.HK", "IP Consumer", "Valuation"],
            "conclusion": (
                "David hosts, Jeff guests (recorded 2026-03-31): Pop Mart 2025 revenue RMB 37.1B (+184.7%), "
                "net profit RMB 13B (+29.3%), but ~20% 2026 growth guidance ('hard brake') triggered ~30% two-day drop. "
                "Stock ~142–143 HKD, market cap below HKD 200B; episode cites Disney PE ~14x. "
                "For investors: 9992.HK — separate Labubu phenomenon from IP pipeline; high PE punishes guidance misses."
            ),
            "background": (
                "David hosts and Jeff guests on a episode recorded 2026-03-31 unpacking Pop Mart's 2025 print vs 2026 guide. "
                "Revenue RMB 37.1B (+184.7% YoY), net profit RMB 13B (+29.3% YoY) — profit growth far below revenue. "
                "2026 guidance ~20% growth decelerates sharply off a high base; shares fell ~30% over about two trading days. "
                "Stock traded ~142–143 HKD with market cap below HKD 200B. Debate spans IP durability vs fashion cycle; "
                "Disney ~14x PE used as valuation reference."
            ),
            "important_facts": [
                (
                    "2025 revenue RMB 37.1B, +184.7% YoY; net profit RMB 13B, +29.3% YoY. "
                    "2026 guidance ~20% revenue growth — a sharp 'hard brake' off 2025's base — "
                    "sparked ~30% share decline over roughly two trading days after the guide."
                ),
                (
                    "Shares ~142–143 HKD; market cap below HKD 200B. "
                    "Super-IPs like Labubu drove much of the increment but concentration fuels fad vs character-equity debate. "
                    "Overseas expansion is curve two; localization may dilute near-term margins."
                ),
                (
                    "PE debate: bulls comp Disney/Hello Kitty IP compounding; episode cites Disney ~14x PE as anchor. "
                    "Bears comp trend cycles and inventory risk. High-PE consumer names punish guidance errors severely — "
                    "moving from +184.7% to ~20% is a narrative break, not a small tweak."
                ),
            ],
            "mental_model": {
                "name": "IP Compounding × Fashion Cycle × Guidance Sensitivity",
                "components": (
                    "Cross-generational characters earn Disney multiples; trend SKUs earn fast-fashion multiples. "
                    "First guidance deceleration after hyper-growth is the danger zone — RMB 37.1B revenue at +184.7% "
                    "set an impossible bar; net profit +29.3% shows margin and opex pressure vs revenue."
                ),
                "application": (
                    "Investing lens: (1) 9992.HK — IP pipeline width, repurchase, membership; "
                    "(2) at ~142–143 HKD and mcap <HKD 200B, multiples normalize from narrative peak; "
                    "(3) Disney ~14x PE is the episode anchor — IP durability debate sets premium room. "
                    "~20% 2026 guide is still strong if delivered; size below traditional compounders."
                ),
            },
            "key_insights": [
                {
                    "view": "RMB 37.1B revenue proves ops; RMB 13B net profit (+29.3%) doesn't prove perpetual hyper-growth.",
                    "question": "Why such a violent reaction to ~20% guidance?",
                    "answer": (
                        "+184.7% in 2025 set an impossible bar; ~30% two-day drop shows narrative break. "
                        "Capital at peak paid peak multiples. Guide deceleration shifts the story. "
                        "Use bull/base/bear scenarios; expect amplified volatility in transition years."
                    ),
                },
                {
                    "view": "IP vs fashion is the valuation fork; Disney ~14x PE is the episode reference.",
                    "question": "How to classify Labubu?",
                    "answer": (
                        "Multi-gen products, licensing, organic overseas spread = IP signal; "
                        "one-quarter hype, secondary-market collapse = fashion signal. Evidence mixed. "
                        "Episode contrasts Pop Mart premium to Disney ~14x PE — debate is whether IP supports higher multiple."
                    ),
                },
                {
                    "view": "Below HKD 200B mcap at ~142–143 HKD, high PE has zero tolerance for misses.",
                    "question": "Practical framework?",
                    "answer": (
                        "Size below compounders; scenario tables not single-point EPS. "
                        "Quarter misses can trigger 20–30% drawdowns — 9992 demonstrated. "
                        "Track comps, overseas mix, IP renewals; separate Labubu from pipeline breadth."
                    ),
                },
            ],
            "top_investment_implications": [
                {
                    "ticker": "9992.HK",
                    "direction": "Long",
                    "confidence": "Medium",
                    "thesis": (
                        "Post-guide shock: ~20% 2026 growth, ~142–143 HKD, mcap <HKD 200B after ~30% two-day drop; "
                        "IP pipeline breadth needed vs Disney ~14x PE anchor"
                    ),
                },
                {
                    "ticker": "DIS",
                    "direction": "Long",
                    "confidence": "Low",
                    "thesis": (
                        "Episode comps POP MART to character-IP names at Disney ~14x PE; "
                        "park + media flywheel caps pure toy/IP earnings power"
                    ),
                },
            ],
            "golden_quotes": [
                "RMB 37.1B revenue is fact, RMB 13B profit — the market buys the future. From 184% to 20%, the narrative broke.",
                "A thirty percent drop in two days — high-PE consumer stocks fear 'less amazing.'",
                "IP vs fashion: check whether Labubu is still on shelves three years from now.",
            ],
            "chronology": {
                "subject": "Pop Mart · 2025 Results & Valuation Reset",
                "events": [
                    {"date": "2020", "event": "Pop Mart lists in Hong Kong (9992.HK)"},
                    {"date": "2023–24", "event": "Labubu and IP global push accelerate revenue"},
                    {"date": "2025", "event": "Revenue RMB 37.1B (+184.7%); net profit RMB 13B (+29.3%)"},
                    {"date": "2026-03-31", "event": "David and Jeff record episode on results and valuation"},
                    {"date": "2026 Q1", "event": "~20% 2026 guide; ~30% two-day drop; stock ~142–143 HKD"},
                ],
            },
        },
    },
    "tzs-ep185": {
        "zh": {
            "keywords": ["TSM", "ASML", "0981.HK", "半导体周期"],
            "conclusion": (
                "谢志峰四十年产业视角：1990 年 Intel 最高技术奖、2000 年联合创立中芯国际；"
                "摩尔定律放缓但未死；TSMC 护城河是服务+生态而非单纯制程数字。"
                "半导体历史上约 5 年周期；中芯纯代工全球第二，仅次于 TSMC。"
                "对投资者：TSM/ASML 是先进制程 choke point；0981.HK 看 utilization 与政策资本 ROI。"
            ),
            "background": (
                "中芯国际联合创始人谢志峰回顾约 40 年半导体生涯：1990 年获 Intel 最高技术奖，"
                "2000 年联合创立 SMIC。他解释 TSMC 纯 foundry 服务模型如何击败 IDM 自建产线，"
                "摩尔定律在先进节点面临的经济与物理边界，以及 AI 算力如何改写 capex。"
                "半导体历史上典型约 5 年周期；SMIC 在纯代工领域全球排名第二，仅次于 TSMC。"
            ),
            "important_facts": [
                (
                    "谢志峰从业约 40 年：1990 年获 Intel 最高技术奖，2000 年联合创立中芯国际 (0981.HK)。"
                    "亲历中国半导体从 0 到 foundry 规模化，强调产业是 marathon 而非 single tech bet。"
                ),
                (
                    "摩尔定律放缓：EUV、材料、功耗墙使每 node 成本指数上升；"
                    "只有 TSMC 级 volume 与客户 co-development 能摊薄。"
                    "TSMC 护城河 = 工艺领先 + 设计生态 + 交付 reliability——Apple/Nvidia 级客户绑定是服务模型。"
                ),
                (
                    "半导体历史上约 5 年周期；AI 芯片拉高 advanced node 需求，但 memory 与 mature node 仍波动。"
                    "SMIC 纯代工全球排名第二，仅次于 TSMC；localization 带来 volume 但 advanced 节点受限。"
                ),
            ],
            "mental_model": {
                "name": "摩尔边界 × Foundry 服务模型 × 5 年半导体周期",
                "components": (
                    "制程进步继续但 economics 恶化——赢家需 scale + customer co-optimization。"
                    "TSMC 赢的是「让客户成功」的服务体系，晶圆是交付形式。"
                    "约 5 年历史周期叠加 AI structural tailwind；SMIC #2 pure foundry behind TSMC。"
                ),
                "application": (
                    "投资映射：① TSM 先进制程 + AI mix 仍是 quality compounder，警惕 capex peak；"
                    "② ASML EUV 垄断，地缘政治 binary risk；"
                    "③ 0981.HK 看 mature vs advanced mix、utilization、subsidy ROI，周期下行 loss-making node 先暴露。"
                ),
            },
            "key_insights": [
                {
                    "view": "TSMC 赢的不是制程数字，而是让客户成功的服务体系。",
                    "question": "为何 IDM 难以复制？",
                    "answer": (
                        "Intel/Samsung 兼顾 design 与 fab，foundry 客户担心 IP 与产能冲突；"
                        "TSMC 纯代工消除 conflict。Co-development 与 Apple/Nvidia 同步工艺与 product roadmap——"
                        "sticky 十年关系。谢志峰 1990 Intel 奖、2000 SMIC 创立见证产业重心转移。"
                    ),
                },
                {
                    "view": "AI 需求 structural，但半导体 stock 仍 cyclical（约 5 年周期）。",
                    "question": "如何不被 AI narrative 冲昏？",
                    "answer": (
                        "AI 拉高 advanced utilization，但 memory、auto、industrial 仍随 macro 波动。"
                        "Capex boom 后 12–18 个月常见 inventory correction。"
                        "Mark-to-cycle，非 mark-to-hype；摩尔放缓使每 node 更贵，放大周期振幅。"
                    ),
                },
                {
                    "view": "SMIC 全球纯代工第二，窗口与陷阱并存。",
                    "question": "0981.HK 怎么读？",
                    "answer": (
                        "Localization 带来 volume 与政策支持，但 advanced 节点受限 → 毛利结构不同于 TSM。"
                        "Duplicate capacity 在下行期成 national sunk cost。"
                        "看 utilization 与 free cash flow，非 solely 制程 headlines。"
                    ),
                },
            ],
            "top_investment_implications": [
                {
                    "ticker": "TSM",
                    "direction": "Long",
                    "confidence": "Medium",
                    "thesis": (
                        "Advanced-node choke point + AI customer mix; Xie frames moat as service/ecosystem; "
                        "watch ~5-year semi cycle for entry timing"
                    ),
                },
                {
                    "ticker": "ASML",
                    "direction": "Long",
                    "confidence": "Medium",
                    "thesis": (
                        "EUV monopoly as Moore economics worsen; lithography spend per node rises; "
                        "export controls remain key risk"
                    ),
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
                    {"date": "1990", "event": "谢志峰获 Intel 最高技术奖"},
                    {"date": "1980s–1990s", "event": "见证 IDM 时代与亚洲产能崛起"},
                    {"date": "2000", "event": "联合创立中芯国际 (SMIC)"},
                    {"date": "2010s", "event": "TSMC 纯 foundry dominance；摩尔放缓信号"},
                    {"date": "2023–2026", "event": "AI 推高 advanced capex；SMIC #2 pure foundry"},
                ],
            },
        },
        "en": {
            "keywords": ["TSM", "ASML", "0981.HK", "Semiconductor Cycle"],
            "conclusion": (
                "Xie's forty-year lens: Intel highest tech award 1990, co-founded SMIC 2000; Moore's Law slowing not dead; "
                "TSMC moat is service + ecosystem. Historically ~5-year semi cycles; SMIC #2 pure foundry behind TSMC. "
                "For investors: TSM/ASML advanced choke points; 0981.HK on utilization and subsidy ROI."
            ),
            "background": (
                "SMIC co-founder Xie Zhifeng traces ~40 years in semis: Intel highest technology award in 1990, "
                "co-founded SMIC in 2000. He explains TSMC's pure-play foundry service model, Moore's Law economic walls, "
                "and AI rewiring capex. Semiconductors historically run ~5-year cycles; SMIC ranks #2 in pure foundry behind TSMC."
            ),
            "important_facts": [
                (
                    "Xie has ~40 years in semis: Intel highest tech award 1990, co-founded SMIC (0981.HK) in 2000. "
                    "Watched China scale from zero to meaningful foundry capacity — marathon, not one tech bet."
                ),
                (
                    "Moore's Law slowing: EUV, materials, power walls raise cost per node exponentially; "
                    "only TSMC-scale volume and co-development amortizes. "
                    "TSMC moat = process lead + design ecosystem + reliability — Apple/Nvidia binding is a service model."
                ),
                (
                    "Historically ~5-year semiconductor cycles; AI chips pull advanced nodes but memory/mature nodes still cycle. "
                    "SMIC ranks #2 global pure-play foundry behind TSMC; localization brings volume but advanced nodes capped."
                ),
            ],
            "mental_model": {
                "name": "Moore Boundaries × Foundry Service Model × 5-Year Semi Cycle",
                "components": (
                    "Process progress continues but economics worsen — winners need scale + co-optimization. "
                    "TSMC wins on making customers succeed; wafers are delivery format. "
                    "~5-year historical cycles plus AI structural tailwind; SMIC #2 pure foundry behind TSMC."
                ),
                "application": (
                    "Investing lens: (1) TSM advanced + AI mix quality compounder — watch capex peaks; "
                    "(2) ASML EUV monopoly, geopolitics binary; "
                    "(3) 0981.HK mature vs advanced mix, utilization, subsidy ROI — loss-making nodes surface in downturns."
                ),
            },
            "key_insights": [
                {
                    "view": "TSMC wins on customer success, not node numbers alone.",
                    "question": "Why can't IDMs copy it?",
                    "answer": (
                        "Intel/Samsung design and fab — customers fear IP/capacity conflict; TSMC pure play removes it. "
                        "Co-development with Apple/Nvidia syncs roadmaps — decade-long stickiness. "
                        "Xie's 1990 Intel award and 2000 SMIC founding mark the industry shift."
                    ),
                },
                {
                    "view": "AI demand is structural; semi stocks stay cyclical (~5-year cycles).",
                    "question": "How not to get swept by AI narrative?",
                    "answer": (
                        "AI lifts advanced utilization; memory, auto, industrial still follow macro. "
                        "12–18 months post-capex boom often brings inventory correction. Mark-to-cycle, not hype; "
                        "Moore slowdown makes each node costlier, amplifying cycle swings."
                    ),
                },
                {
                    "view": "SMIC #2 pure foundry — window and trap together.",
                    "question": "How to read 0981.HK?",
                    "answer": (
                        "Localization brings volume and policy support but advanced limits → margin unlike TSM. "
                        "Duplicate capacity becomes sunk cost in downturns. Watch utilization and FCF, not headline nodes."
                    ),
                },
            ],
            "top_investment_implications": [
                {
                    "ticker": "TSM",
                    "direction": "Long",
                    "confidence": "Medium",
                    "thesis": (
                        "Advanced choke point + AI mix; Xie frames moat as service/ecosystem — "
                        "watch ~5-year cycle for timing"
                    ),
                },
                {
                    "ticker": "ASML",
                    "direction": "Long",
                    "confidence": "Medium",
                    "thesis": (
                        "EUV monopoly as Moore economics worsen; lithography spend per node rises; export controls key risk"
                    ),
                },
            ],
            "golden_quotes": [
                "Moore's Law isn't dead — it's just getting expensive. Only the largest ecosystems can pay.",
                "TSMC runs a service business; wafers are just the delivery format.",
                "Semiconductors are always cyclical — AI changes the slope, not the law.",
            ],
            "chronology": {
                "subject": "Xie Zhifeng · Four Decades in Semiconductors",
                "events": [
                    {"date": "1990", "event": "Xie wins Intel highest technology award"},
                    {"date": "1980s–90s", "event": "Witnesses IDM era and Asia capacity rise"},
                    {"date": "2000", "event": "Co-founds SMIC"},
                    {"date": "2010s", "event": "TSMC pure-play dominance; Moore slowdown signals"},
                    {"date": "2023–26", "event": "AI capex boom; SMIC #2 pure foundry globally"},
                ],
            },
        },
    },
    "tzs-ep179": {
        "zh": {
            "keywords": ["价值投资", "资本周期", "复利"],
            "conclusion": (
                "永庆系统阐述价值投资框架：价格围绕内在价值波动，内在价值需动态评估——"
                "公司生命周期与资本周期交织。Graham 时代看 PB；优质复利公司是「时间的朋友」。"
                "公募基金在回撤时常 de-risk，contrarian 需承受 relative underperformance。"
                "对投资者：以合理价格买入长期 ROIC 高于 WACC 的公司，资本周期过热时减仓。"
            ),
            "background": (
                "永庆以主讲身份分享投资实战派方法论：从 Graham/Buffett 传统价值到资本周期框架与中国市场实操。"
                "价值投资不等于低 PE——需区分 value trap 与 temporary mispricing。"
                "Graham 时代更重 PB；今日 quality compounder 是「时间的朋友」——ROIC 能持续十年以上。"
                "公募基金在 drawdown 时常 de-risk positioning，2021 消费抱团、2024–2025 AI 是案例。"
                "2025–2026 年 AI infra 与 IP 消费 capital cycle 分化，框架用于 current positioning。"
            ),
            "important_facts": [
                (
                    "价值投资核心 triad：ROIC、再投资 runway、management capital allocation。"
                    "价格低于内在价值才是 value，内在价值随生命周期变化——非静态低 PE。"
                    "Graham 时代 PB 框架在成熟复利公司上需升级。"
                ),
                (
                    "资本周期：高 profit → capital inflow → overcapacity → margin collapse → exit → recovery；"
                    "胜负在 cycle positioning。资本涌入的地方回报率必然下来，只是时间问题。"
                    "2021 消费赛道顶点、2022–2023 港股低谷是永庆复盘案例。"
                ),
                (
                    "优质复利公司（时间的朋友）：高 ROIC + long reinvestment，可在 mature 阶段持续 10+ 年若 moat 稳固。"
                    "公募基金在 narrative peak 仓位最重，drawdown 时 de-risk；"
                    "contrarian 投资者需 independent thesis，承受 until cycle turns。"
                ),
            ],
            "mental_model": {
                "name": "内在价值 × 资本周期 × 生命周期",
                "components": (
                    "Buy quality (ROIC > WACC, durable moat) at reasonable price，timing 靠资本周期相位。"
                    "Avoid sectors where inflow 已摧毁 forward returns。"
                    "Lifecycle lens 防止持有 compounder 超过 moat 侵蚀点。"
                    "Mutual fund de-risking on drawdowns 是 contrarian indicator。"
                ),
                "application": (
                    "投资映射：① 消费 quality（9992 需区分 cycle vs compounder）；"
                    "② 半导体按资本周期择时 TSM/ASML；"
                    "③ 公募重仓赛道（新能源、AI）用 capital cycle checklist 检验 over-ownership。"
                    "30x PE ok if ROIC 25%+ sustains 10yr；30x for 15% ROIC = trap。"
                ),
            },
            "key_insights": [
                {
                    "view": "资本周期比 macro 预测更可靠——profit attracts capital, capital kills profit.",
                    "question": "2025–2026 哪些 sector 可能过热？",
                    "answer": (
                        "AI infra capex、部分 IP 消费 narrative peak 已现；"
                        "when everyone owns the same story, forward returns compress。"
                        "Semis 需区分 AI structural vs classical oversupply。"
                    ),
                },
                {
                    "view": "Quality compounder 是「时间的朋友」，识别标准应跨周期 stable。",
                    "question": "与 growth investing 边界？",
                    "answer": (
                        "Growth 付 premium for runway；value 要求 price discipline。"
                        "Compounders 是交集——高 ROIC + long reinvestment。"
                        "Pay 30x if ROIC 25%+ sustains 10yr；否则 trap。"
                    ),
                },
                {
                    "view": "公募基金 positioning 与 drawdown de-risk 是 contrarian indicator。",
                    "question": "实操如何使用？",
                    "answer": (
                        "Weekly inflow + media saturation + IPO flood coincide 时 reduce exposure。"
                        "2018–2019 消费低谷、2022 港股低谷是 entry case studies。"
                        "Independent thesis > consensus comfort；回撤时公募 de-risk 常加剧低点。"
                    ),
                },
            ],
            "top_investment_implications": [
                {
                    "ticker": "BRK.B",
                    "direction": "Long",
                    "confidence": "Medium",
                    "thesis": (
                        "Archetypal quality compounder + capital allocator; "
                        "Yongqing's ROIC and capital-cycle discipline align with Buffett framework"
                    ),
                },
                {
                    "ticker": "TSM",
                    "direction": "Long",
                    "confidence": "Medium",
                    "thesis": (
                        "Semi quality compounder but capital-cycle timing matters — "
                        "add on utilization dips, trim when capex/Revenue peaks and funds overweight"
                    ),
                },
            ],
            "golden_quotes": [
                "价值不是便宜的代名词，是价格低于内在价值——而内在价值会变。",
                "资本涌入的地方，回报率一定下来，只是时间问题。",
                "复利公司的关键不是快，是久——ROIC 能持续十年以上，才是时间的朋友。",
            ],
            "chronology": {
                "subject": "永庆 · 价值投资与资本周期",
                "events": [
                    {"date": "Graham 时代", "event": "PB 框架主导的价值投资起源"},
                    {"date": "2015–2020", "event": "永庆建立投资实战派，实践 quality value"},
                    {"date": "2021", "event": "消费赛道 capital cycle 顶点，公募抱团 peak"},
                    {"date": "2022–2023", "event": "港股低谷 compounder 布局；公募 de-risk"},
                    {"date": "2025–2026", "event": "AI infra 与 IP 消费 cycle 分化，框架应用于 positioning"},
                ],
            },
        },
        "en": {
            "keywords": ["Value Investing", "Capital Cycle", "Compounding"],
            "conclusion": (
                "Yongqing's value framework: price oscillates around intrinsic value, reassessed dynamically — "
                "lifecycle and capital cycle interact. Graham era weighted PB; quality compounders are 'friends of time.' "
                "Mutual funds de-risk on drawdowns; contrarians need independent theses. "
                "Buy ROIC > WACC at reasonable prices; trim when capital cycles overheat."
            ),
            "background": (
                "Yongqing teaches the show's methodology — Graham/Buffett value to capital-cycle thinking in China. "
                "Value ≠ low PE: separate traps from mispricing. Graham era emphasized PB; today's quality compounders "
                "are friends of time — ROIC sustained ten-plus years. Mutual funds peak weight at narrative tops and "
                "de-risk on drawdowns (2021 consumer, 2024–25 AI). 2025–26 AI infra vs IP consumer cycles diverge."
            ),
            "important_facts": [
                (
                    "Value triad: ROIC, reinvestment runway, capital allocation. "
                    "Price below intrinsic value defines value; intrinsic value shifts with lifecycle — not static low PE. "
                    "Graham-era PB frameworks need upgrading for mature compounders."
                ),
                (
                    "Capital cycle: high profit → inflows → overcapacity → margin collapse → exit → recovery. "
                    "Where capital floods, returns must fall — only a matter of time. "
                    "2021 consumer peak and 2022–23 HK trough are Yongqing's case studies."
                ),
                (
                    "Quality compounders (friends of time): high ROIC + long reinvestment, 10+ years in maturity if moat holds. "
                    "Mutual funds max weight at narrative peaks and de-risk on drawdowns; "
                    "contrarians need independent theses until the cycle turns."
                ),
            ],
            "mental_model": {
                "name": "Intrinsic Value × Capital Cycle × Lifecycle",
                "components": (
                    "Buy quality (ROIC > WACC, durable moat) at reasonable price — timing via capital-cycle phase. "
                    "Avoid sectors where inflows destroyed forward returns. Lifecycle lens avoids holding past moat erosion. "
                    "Mutual fund de-risking on drawdowns is a contrarian signal."
                ),
                "application": (
                    "Investing lens: (1) consumer quality — 9992.HK cycle vs compounder; "
                    "(2) time TSM/ASML with capital cycle; "
                    "(3) mutual-fund overweight sectors — capital-cycle checklist. "
                    "30x PE ok if 25%+ ROIC sustains 10 years; 30x for 15% ROIC is trap."
                ),
            },
            "key_insights": [
                {
                    "view": "Capital cycle beats macro forecasting — profit attracts capital, capital kills profit.",
                    "question": "Which 2025–26 sectors look overheated?",
                    "answer": (
                        "AI infra capex and parts of IP consumer narrative may have peaked; "
                        "when everyone owns the same story, forward returns compress. "
                        "Separate AI structural tailwind from classical semi oversupply."
                    ),
                },
                {
                    "view": "Quality compounders are friends of time — criteria stable across cycles.",
                    "question": "Boundary with growth investing?",
                    "answer": (
                        "Growth pays for runway; value demands price discipline. "
                        "Compounders = high ROIC + long reinvestment overlap. "
                        "30x PE ok if 25%+ ROIC sustains 10 years; otherwise trap."
                    ),
                },
                {
                    "view": "Mutual fund positioning and drawdown de-risking are contrarian indicators.",
                    "question": "How to use in practice?",
                    "answer": (
                        "When inflows + media saturation + IPO flood coincide, reduce exposure. "
                        "2018–19 consumer trough and 2022 HK lows are entry case studies. "
                        "Independent thesis beats consensus; fund de-risking often deepens troughs."
                    ),
                },
            ],
            "top_investment_implications": [
                {
                    "ticker": "BRK.B",
                    "direction": "Long",
                    "confidence": "Medium",
                    "thesis": (
                        "Archetypal quality compounder and capital allocator; "
                        "Yongqing's framework mirrors Buffett ROIC and cycle discipline"
                    ),
                },
                {
                    "ticker": "TSM",
                    "direction": "Long",
                    "confidence": "Medium",
                    "thesis": (
                        "Semi quality compounder but cycle timing matters — "
                        "add on utilization dips, trim at capex peaks when funds overweight"
                    ),
                },
            ],
            "golden_quotes": [
                "Value doesn't mean cheap — it means price below intrinsic value, and intrinsic value changes.",
                "Where capital floods in, returns must come down — it's only a matter of time.",
                "Compounders aren't about speed, they're about duration — ROIC sustained ten-plus years, friends of time.",
            ],
            "chronology": {
                "subject": "Yongqing · Value Investing & Capital Cycles",
                "events": [
                    {"date": "Graham era", "event": "PB-weighted value investing origins"},
                    {"date": "2015–20", "event": "Yongqing builds Investment Practical School; quality value in A/H"},
                    {"date": "2021", "event": "Consumer capital-cycle peak; mutual-fund herding"},
                    {"date": "2022–23", "event": "HK trough entries; mutual funds de-risk on drawdowns"},
                    {"date": "2025–26", "event": "AI infra vs IP consumer cycles diverge; framework applied"},
                ],
            },
        },
    },
}


# zj-ep140 and zj-ep143 bodies (seed baseline + transcript patches)
import json as _json
from pathlib import Path as _Path

_ep140_143 = _json.loads((_Path(__file__).resolve().parent / "_ep140_143.json").read_text(encoding="utf-8"))

# Patch zj-ep143 transcript-verified facts
_ep143_zh = _ep140_143["zj-ep143"]["zh"]
_ep143_zh["keywords"] = ["XPEV", "人形机器人", "物理世界 AI"]
_ep143_zh["conclusion"] = (
    "何小鹏核心判断：旧机器人栈累计投入「小几十个亿」且无法泛化，约 2025 年果断停掉；"
    "人形 IRON 胜率他自评约两成，但成功回报极高。泛 AI 投入占公司 15–20%，"
    "物理世界数据采集刚性成本每年「接近 10 个亿以上」。对投资者：XPEV 需 sum-of-the-parts。"
)
_ep143_zh["background"] = (
    "张小珺对话何小鹏，复盘机器人与智驾战略大调整。"
    "旧机器人栈累计「小几十个亿」（非数百亿），约 2025 年因无法泛化而停掉。"
    "All-in 人形 IRON——自评胜率约 20%。泛 AI 占公司 15–20%；"
    "物理世界数据每年刚性成本「接近 10 个亿以上」。"
)
_ep143_zh["important_facts"] = [
    (
        "旧机器人路线累计「小几十个亿」（非数百亿），约 2025 年因无法泛化停掉——继续投是沉没成本陷阱。"
    ),
    (
        "人形 IRON 约 20% 胜率（「我们大概有个两成」）；泛 AI 投入占公司 15–20%。"
    ),
    (
        "物理世界 AI 数据刚性成本每年「接近 10 个亿以上」；L4 捷径未达预期，GX pivot 调整产品匹配。"
    ),
]
_ep143_zh["golden_quotes"] = [
    "旧机器人那条路花了小几十个亿，必须停——不停才是最大的浪费。",
    "IRON 这个项目，我自己评估胜率大概两成，但成了就是另一家公司。",
    "物理世界的 AI，数据才是真的贵，一年接近十个亿以上。",
]
_ep143_zh["chronology"]["events"] = [
    {"date": "2020–2023", "event": "投入上一代机器人与 L4，累计「小几十个亿」"},
    {"date": "约 2025", "event": "旧栈因无法泛化停掉"},
    {"date": "2025–2026", "event": "All-in IRON；泛 AI 占公司 15–20%"},
    {"date": "2025–2026", "event": "物理世界数据年刚性成本 10 亿+"},
    {"date": "2026", "event": "GX pivot；L4 纯视觉捷径证伪"},
]

_ep143_en = _ep140_143["zj-ep143"]["en"]
_ep143_en["keywords"] = ["XPEV", "Humanoid Robotics", "Physical-World AI"]
_ep143_en["conclusion"] = (
    "He: legacy robot stack cost a few tens of billions RMB (not hundreds), stopped ~2025 for failed generalization. "
    "IRON ~20% win rate; broad AI 15–20% of company; physical-world data RMB 1B+/year rigid cost. "
    "XPEV needs sum-of-the-parts."
)
_ep143_en["background"] = (
    "He Xiaopeng on the robotics reset: old stack cost a few tens of billions RMB, stopped ~2025 without generalization. "
    "All-in IRON at ~20% win probability. Broad AI 15–20% of company; physical-world data rigidly RMB 1B+/year."
)
_ep143_en["important_facts"] = [
    "Old robot route: few tens of billions RMB (not hundreds); stopped ~2025 — could not generalize.",
    "IRON ~20% win probability; broad AI spend 15–20% of the company.",
    "Physical-world data rigidly RMB 1B+/year; L4 shortcut underperformed; GX pivot.",
]
_ep143_en["golden_quotes"] = [
    "We spent a few tens of billions on the old robot path — stopping is the real savings.",
    "I put IRON's win probability at roughly twenty percent — but if it works, we're a different company.",
    "In physical-world AI, data is what's truly expensive — close to ten billion a year.",
]
_ep143_en["chronology"]["events"] = [
    {"date": "2020–23", "event": "Prior robot stack and L4 — few tens of billions RMB"},
    {"date": "~2025", "event": "Old stack stopped — failed to generalize"},
    {"date": "2025–26", "event": "All-in IRON; broad AI 15–20% of company"},
    {"date": "2025–26", "event": "Physical-world data budget; RMB 1B+/year rigid"},
    {"date": "2026", "event": "GX pivot; L4 vision-only shortcut disproved"},
]

REFINED.update(_ep140_143)
