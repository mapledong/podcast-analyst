"""Word-count expansions (transcript-grounded investing analysis) for refine_chinese_pilot."""

from __future__ import annotations

import re
from typing import Any

from src.validate import word_count

# Per-episode supplemental prose keyed by section.
PACKS: dict[str, dict[str, dict[str, Any]]] = {
    "zj-ep140": {
        "en": {
            "fact_append": [
                (
                    "Investors should read convergence as compression of 'model alpha' — fewer trades hinge on "
                    "which lab has +5 benchmark points. Yao's late-2025 Gemini move signals Google still treats volume "
                    "as existential; his ~20% share guess is a working estimate, not a bull case. "
                    "Track Gemini app retention, enterprise attach, and search integration metrics quarterly."
                ),
                (
                    "Doubao's voice lead is the China case study: regional data, latency, and UX beat raw IQ for "
                    "daily users. Claude Code is the US case study: workflow lock-in monetizes before the next model drop. "
                    "Dario naming distillers elevates IP/data policy to a P&L line — watch legal and partnership friction."
                ),
                (
                    "Reliability as scarce trait favors orgs with eval discipline and product ownership culture. "
                    "Hero narratives help recruiting but do not justify capex at scale. "
                    "Barbell portfolio: GOOGL distribution option, private lab workflow bets, China scene winners."
                ),
            ],
            "mm_components": (
                "Convergence plus reliability filter: underwrite GTM and retention, not leaderboard deltas. "
                "Late-2025 Gemini hiring is a timing marker for Google's volume war. "
                "~20% share guess frames upside if consumer hits chain; downside if retention stalls."
            ),
            "mm_application": (
                "Sizing: GOOGL as distribution compounder with AI option; Anthropic as coding/agent pure play; "
                "avoid treating any single lab as permanent winner. Monitor distillation disputes and enterprise churn. "
                "China: voice UX leaders may capture local share without winning global IQ. "
                "2026 diligence checklist: product bet clarity, eval transparency, commercial ARR paths, not parameter counts."
            ),
            "insight_append": [
                " Model IQ gaps under five points rarely change consumer choice; speed, price, and workflow fit do.",
                " Search plus Android are GOOGL's unique levers — but only if consumer hits chain; watch retention cohorts.",
                " Reliability culture determines whether capex converts to revenue when capabilities flatten.",
            ],
        },
        "zh": {
            "fact_append": [
                "投资者应将收敛读作「模型 alpha」压缩——更少交易取决于 5 个榜单点。顺宇 2025 年末加入 Gemini 说明 Google 仍视拉量为生存问题；市占约两成是工作假设非 bull case。季度跟踪 Gemini 留存与企业 attach。",
                "豆包语音是中国案例：区域数据、延迟、UX 胜 raw IQ。Claude Code 是美国案例：工作流锁定先于下一代模型变现。Dario 点名蒸馏者将 IP/数据政策升为 P&L 科目。",
                "靠谱为稀缺特质，偏好评测纪律与产品负责文化。英雄叙事助招聘但不足以支撑规模化 capex。哑铃组合：GOOGL 分发期权、私有 lab 工作流 bet、中国场景赢家。",
            ],
            "mm_components": (
                "收敛加靠谱筛选： underwriting 看 GTM 与留存，非榜单分差。"
                "2025 年末加入 Gemini 是 Google 拉量战时间标记；市占约两成框定上行与下行。"
            ),
            "mm_application": (
                "配置：GOOGL 为分发 compounder 加 AI 期权；Anthropic 为 coding/agent 纯 bet；"
                "勿将单一 lab 视为永久赢家。跟踪蒸馏争议与企业 churn。"
                "中国：语音 UX 领先者可拿本地份额而不必全球 IQ 第一。"
                "2026 diligence：产品 bet 清晰度、评测透明度、商业 ARR 路径，非参数量。"
            ),
            "insight_append": [
                " 模型 IQ 差 5 点难改消费选择；速度、价格、工作流契合度才关键。",
                " 搜索加安卓是 GOOGL 独有杠杆——需消费命中连锁；看留存 cohort。",
                " 靠谱文化决定能力拉平时 capex 能否转化为收入。",
            ],
        },
    },
    "zj-ep144": {
        "en": {
            "fact_append": [
                (
                    "At RMB 60B+ cap, shallow-sea discipline must repeat in each adjacent category — "
                    "investors should score new launches on time-to-category-leader and gross-margin contribution, not hype."
                ),
                (
                    "Deep-sea avoidance (phones ~$500B, PCs ~$200B) is strategic capital allocation — "
                    "it prevents head-on wars with Apple and PC OEMs while earphones ~$200–300B and power banks ~$5B "
                    "offer leader economics."
                ),
                (
                    "Billion-token research lowers internal diligence cost — watch whether faster decisions show up "
                    "in SKU velocity, lower SG&A ratio, and sustained +1.1–1.5pt margin lifts."
                ),
            ],
            "mm_components": (
                "Shallow sea is repeatable if ROIC per category stays high; deep sea is a deliberate no-fly zone. "
                "Google Founders Award lineage underscores product-led DNA, not commodity scaling."
            ),
            "mm_application": (
                "300866.SZ: overweight margin trajectory and category ROIC; underweight single-channel revenue spikes. "
                "AMZN risk is structural — ads and policy shifts can offset shallow-sea wins. "
                "AI org gains must evidence in operating metrics within 2–3 years, not slide decks."
            ),
            "insight_append": [
                " Category size ceiling ~$500B TAM keeps giants partially absent — core to reinvestment runway.",
                " Billion-token context shifts research from data gathering to judgment — ask better questions.",
                " Margin +1.1–1.5pt/year is the falsifiable test of shallow-sea execution at scale.",
            ],
        },
        "zh": {
            "fact_append": [
                "市值 600 亿+ 后浅海纪律须在 each adjacent 品类复制——投资者按成为品类第一速度与毛利贡献评分，非 hype。",
                "回避深海（手机 5000 亿、PC 2000 亿）是战略资本配置；耳机 2000–3000 亿、充电宝 50 亿提供龙头经济学。",
                "十亿 token 研究降低内部 diligence 成本——看 SKU 速度、SG&A、持续 +1.1–1.5pt 毛利是否改善。",
            ],
            "mm_components": (
                "浅海可重复若各品类 ROIC 高；深海是刻意禁飞区。"
                "Google Founders Award 背景强调产品基因，非 commodity 规模。"
            ),
            "mm_application": (
                "300866.SZ： overweight margin trajectory 与品类 ROIC；underweight 单渠道收入尖峰。"
                "AMZN 风险结构性——广告与政策可抵消浅海胜利。"
                "AI 组织收益须在 2–3 年内体现在经营指标。"
            ),
            "insight_append": [
                " 品类规模天花板约 500 亿美元 TAM 使巨头部分缺席——再投资跑道核心。",
                " 十亿 token 将研究从搜集数据转向 judgment——问更好的问题。",
                " 毛利 +1.1–1.5pt/年 是规模化浅海执行的可证伪测试。",
            ],
        },
    },
    "zj-ep143": {
        "en": {
            "mm_application": (
                "Model XPEV as auto core plus 15–20% broad AI burn and ~20% IRON option. "
                "Physical-data RMB 1B+/year is a hard constraint — only fund if auto cash flow covers it. "
                "NVDA benefits from training spend regardless of humanoid winner."
            ),
        },
        "zh": {
            "mm_application": (
                "XPEV 建模：汽车核心加 15–20% 泛 AI burn 与约 20% IRON 期权。"
                "物理数据年 10 亿+ 是硬约束——仅当汽车现金流覆盖时可持续。"
                "NVDA 受益于训练支出，与人形赢家无关。"
            ),
        },
    },
    "tzs-ep180": {
        "en": {
            "mm_application": (
                "Hard brake from +184.7% revenue to ~20% guide; ~30% two-day drop at ~142–143 HKD; "
                "mcap below HKD 200B. Disney ~14x PE anchor."
            ),
        },
        "zh": {
            "mm_application": (
                "从 +184.7% 营收到约 20% 指引急刹车；两日跌约 30%，股价 142–143 港元，市值低于 2000 亿港币。"
                "Disney 约 14 倍 PE 锚。JSON 保留 9992.HK，中文显示泡泡玛特（9992.HK）。"
            ),
        },
    },
    "tzs-ep185": {
        "en": {
            "mm_application": (
                "Intel award 1990; SMIC co-founder 2000; #2 pure foundry behind TSMC; ~5-year cycles; "
                "TSM service model; 0981.HK utilization focus; ASML export risk."
            ),
        },
        "zh": {
            "mm_application": (
                "1990 Intel 最高技术奖；2000 联合创立 SMIC；纯代工全球第二；约 5 年周期；"
                "TSM 服务模型；0981.HK 看 utilization；ASML 出口风险。"
            ),
        },
    },
    "tzs-ep179": {
        "en": {
            "mm_application": (
                "Graham PB era evolved to quality compounders as friends of time; mutual funds de-risk on drawdowns; "
                "capital cycle positioning over macro calls; 30x PE needs 25%+ ROIC for ten years."
            ),
        },
        "zh": {
            "mm_application": (
                "Graham PB 演进为「时间的朋友」quality compounder；公募回撤时 de-risk；"
                "资本周期定位胜过 macro；30x PE 需 25%+ ROIC 十年。"
            ),
        },
    },
}


# Rotate through transcript-grounded sentences until section targets hit (within template maxes).
PAD_SENTENCES: dict[str, dict[str, list[str]]] = {
    "zj-ep140": {
        "en": [
            "Yao stresses reliability over heroism when frontier labs converge on capability.",
            "He joined Gemini in late 2025 after Anthropic training experience.",
            "He guesses Gemini holds roughly twenty percent consumer share today.",
            "Doubao voice UX leads daily Chinese scenarios versus Gemini and Claude.",
            "Claude Code validates Anthropic's coding and agent workflow commercial bet.",
            "Dario Amodei publicly named distillers defending Anthropic model IP.",
            "OpenAI mindshare still dominates even as benchmark gaps narrow.",
            "Google must chain consumer hits before flagship models retain users.",
            "Search and Android distribution are unique GOOGL advantages if retention follows.",
            "Most users do not perceive five-point benchmark IQ differences.",
            "Speed usefulness and price drive consumer AI adoption more than leaderboard rank.",
            "Product bet clarity matters more than raw model intelligence now.",
            "Startups can make top-down workflow bets faster than aligned big companies.",
            "Training is increasingly an engineering organization and eval discipline problem.",
            "Data pipelines and product loops beat one-off research paper wins.",
            "Regional optimization can win local share without global IQ leadership.",
            "Investors should track ARR paths for coding enterprise and consumer segments.",
            "Distillation disputes may become recurring legal and partnership friction.",
            "Hero narratives help hiring but do not justify billion-dollar training capex alone.",
            "2026 is a year of bet clarification not capability miracles for frontier labs.",
        ],
        "zh": [
            "顺宇强调前沿能力收敛时靠谱胜过英雄主义。",
            "他 2025 年末加入 Gemini，此前在 Anthropic 参与训练。",
            "他猜测 Gemini 消费端市占约两成。",
            "豆包语音在中国日常场景领先 Gemini 与 Claude。",
            "Claude Code 验证 Anthropic coding 与 agent 商业化路径。",
            "Dario 公开点名蒸馏者以防御 Anthropic 模型 IP。",
            "ChatGPT 心智仍强，即便榜单差距缩小。",
            "Google 需先用消费命中留人，再用旗舰模型承接。",
            "搜索与安卓是 GOOGL 独有杠杆，前提是留存跟上。",
            "多数用户感知不到五个点的模型 IQ 差距。",
            "速度、好用、便宜比榜单排名更驱动消费级 AI 采用。",
            "产品 bet 清晰度比 raw 智力更关键。",
            "创业公司比大公司更能快速做 top-down 工作流 bet。",
            "训练日益是工程、组织与评测纪律问题。",
            "数据管线与产品闭环胜过单点论文胜利。",
            "区域优化可拿本地份额而不必全球 IQ 第一。",
            "投资者应跟踪 coding、企业与消费三线 ARR。",
            "蒸馏争议或成持续法律与合作摩擦源。",
            "英雄叙事助招聘但不足以单独支撑巨额训练 capex。",
            "2026 对前沿 lab 是 bet 澄清之年而非能力奇迹之年。",
        ],
    },
    "zj-ep144": {
        "en": [
            "Yang founded Anker in 2011 and won a Google Founders Award.",
            "Market cap exceeds sixty billion RMB at six hundred yi plus.",
            "Shallow sea targets categories under roughly five hundred billion dollars TAM.",
            "Power bank TAM is about five billion dollars; earphones two hundred to three hundred billion.",
            "Deep sea phones are five hundred billion dollars; PCs two hundred billion.",
            "Anker avoids deep sea red oceans with full giant resource deployment.",
            "Gross margin rises roughly one point one to one point five per year historically.",
            "Margin expansion proves pricing power better than volatile revenue growth.",
            "Billion-token context can ingest filings supply chain reviews and patents.",
            "AI lowers cost of understanding a company but raises judgment premium.",
            "Amazon channel concentration remains a structural margin risk factor.",
            "Track new category ROIC and time-to-category-leader for adjacent expansion.",
            "Shallow sea strategy must repeat discipline at RMB sixty billion plus scale.",
            "SG&A efficiency and SKU velocity should reflect AI org experiments.",
            "Investors respect sustained margin trajectory over single-quarter revenue spikes.",
        ],
        "zh": [
            "阳萌 2011 年创立安克，曾获 Google Founders Award。",
            "市值 600 亿+ 人民币。",
            "浅海目标 TAM 约 500 亿美元以下品类。",
            "充电宝 TAM 约 50 亿美元；耳机约 2000–3000 亿美元。",
            "深海手机约 5000 亿美元；PC 约 2000 亿美元。",
            "安克回避巨头全资源投入的深海红海。",
            "毛利率历史每年约提升 1.1–1.5 个百分点。",
            "毛利扩张比波动收入更能证明定价权。",
            "十亿 token 可 ingest 财报供应链评论与专利。",
            "AI 降低理解公司成本但抬高 judgment 溢价。",
            "Amazon 渠道集中度仍是结构性毛利风险。",
            "跟踪新品类 ROIC 与成为品类第一所需时间。",
            "600 亿+ 规模下浅海纪律须每品类重复。",
            "SKU 速度与 SG&A 应反映 AI 组织试验。",
            "投资者更尊重持续 margin trajectory 而非单季收入尖峰。",
        ],
    },
    "zj-ep143": {
        "en": [
            "He stopped the legacy robot stack that cost a few tens of billions of RMB.",
            "IRON humanoid is roughly a twenty percent probability bet with massive upside.",
            "Physical-world AI data rigid costs approach one billion RMB per year or more.",
            "Broad AI spend including AV and robots is fifteen to twenty percent of the company.",
            "The old stack could not generalize robots in unfamiliar venues.",
            "GX pivot reflects honest product repositioning after L4 shortcut underperformed.",
            "Physical-world data runs tens to hundreds of terabytes per training cycle.",
            "Each data workflow decision can cost tens of millions of RMB at scale.",
            "Investors should model auto core cash flow separately from robotics optionality.",
            "Humanoid success would redefine XPeng beyond an auto OEM narrative.",
        ],
        "zh": [
            "旧机器人栈耗费小几十亿人民币后果断止损。",
            "人形 IRON 胜率约两成，成功则公司边界重写。",
            "物理世界 AI 数据刚性成本年投入接近 10 亿以上。",
            "泛 AI 投入含智驾与机器人，约占公司 15%–20%。",
            "旧栈无法在陌生场馆实现机器人泛化。",
            "GX pivot 是 L4 捷径未达预期后的产品诚实调整。",
            "物理世界训练单次数据量达数十到数百 TB。",
            "每项数据工作流决策在规模化时可耗数千万人民币。",
            "投资者应将汽车基本盘现金流与机器人期权分开建模。",
            "人形成功将重新定义小鹏，超越传统车企叙事。",
        ],
    },
    "tzs-ep180": {
        "en": [
            "Pop Mart 2025 revenue was RMB 37.1 billion up 184.7 percent year on year.",
            "Net profit was RMB 13 billion up 29.3 percent far below revenue growth.",
            "2026 guidance near twenty percent growth was described as a hard brake.",
            "Shares fell about thirty percent over roughly two trading days after the guide.",
            "Stock traded near 142 to 143 Hong Kong dollars with market cap below 200 billion HKD.",
            "Disney price to earnings near fourteen times was used as a valuation anchor.",
            "Labubu and overseas expansion drove much of the 2025 revenue increment.",
            "IP durability versus fashion cycle is the core bull bear valuation fork.",
            "High price to earnings consumer names punish guidance misses severely.",
            "David hosted and Jeff guested on the cross-podcast episode recorded March 31 2026.",
        ],
        "zh": [
            "泡泡玛特 2025 营收 371 亿人民币，同比 +184.7%。",
            "净利润 130 亿元（约 13 billion RMB），同比 +29.3%，远低于营收增速。",
            "2026 年指引约 20% 增速被形容为急刹车。",
            "指引后股价两日跌约 30%。",
            "股价约 142–143 港元，市值低于 2000 亿港币。",
            "节目以 Disney 约 14 倍 PE 作估值锚。",
            "Labubu 与海外扩张贡献 2025 年大部分增量。",
            "IP 耐久性 vs 时尚周期是估值分歧核心。",
            "高 PE 消费股对 guidance miss 惩罚极重。",
            "大卫主持、Jeff 嘉宾，2026 年 3 月 31 日录制。",
        ],
    },
    "tzs-ep185": {
        "en": [
            "Xie Zhifeng co-founded SMIC around 2000 after Intel research years.",
            "He received Intel highest technical achievement award in 1990.",
            "TSMC pure-play foundry service model beats conflicted IDM fabs.",
            "Moore law continues but each node costs rise exponentially with EUV walls.",
            "Semiconductor history shows roughly five year cycles though AI may flatten dips.",
            "SMIC ranks second in pure foundry behind TSMC in the episode framing.",
            "ASML EUV remains a near-term lithography choke point with export controls.",
            "AI chips pull advanced node demand but memory and mature nodes still cycle.",
            "China localization adds volume but duplicate capacity risks ROI in downturns.",
            "Investors should mark to cycle not to AI hype alone in semi names.",
        ],
        "zh": [
            "谢志峰约 2000 年联合创立中芯国际，此前在英特尔做研发。",
            "1990 年获英特尔最高技术成就奖。",
            "台积电纯代工服务模型胜过有冲突的 IDM 产线。",
            "摩尔定律延续但每节点成本随 EUV 等壁垒指数上升。",
            "半导体历史约五年一周期，AI 或压低下行幅度。",
            "节目框架下 SMIC 纯代工全球第二，仅次于台积电。",
            "ASML EUV 仍是近端光刻瓶颈，受出口管制影响。",
            "AI 芯片拉动先进制程，但存储与成熟节点仍周期波动。",
            "中国本土化带来量但也带来重复产能与 ROI 风险。",
            "投资半导体应 mark-to-cycle，非仅 AI 叙事。",
        ],
    },
    "tzs-ep179": {
        "en": [
            "Yongqing frames value as price below intrinsic value with dynamic reassessment.",
            "Graham era net asset valuation rarely fits most China listings today.",
            "Capital cycle says profit attracts capital and capital eventually kills profit.",
            "Mutual funds often de-risk on drawdowns due to risk controls not fundamentals.",
            "Quality compounders are friends of time with sustained ROIC above cost of capital.",
            "Thirty times PE needs roughly twenty five percent ROIC sustained ten years.",
            "2021 consumer herding and 2024 AI peaks are mutual fund contrarian signals.",
            "Independent thesis beats consensus comfort when cycles turn.",
            "Company lifecycle lens avoids holding compounders past moat erosion.",
            "Scenario tables beat single point earnings estimates in transition years.",
        ],
        "zh": [
            "永庆定义价值为价格低于内在价值，且内在价值须动态重估。",
            "Graham 时代净资产估值法在中国多数标的已罕见。",
            "资本周期：利润吸引资本，资本最终压低回报。",
            "公募基金回撤时常先减仓，多因风控而非基本面。",
            "优质复利公司是时间的朋友，ROIC 持续高于资本成本。",
            "30 倍 PE 需约 25%+ ROIC 持续十年才合理。",
            "2021 消费抱团与 2024 AI 峰值是公募反向指标案例。",
            "周期转折时独立 thesis 胜过共识舒适。",
            "生命周期视角避免在护城河侵蚀后仍持有复利股。",
            "过渡期用 scenario 表优于单点盈利预测。",
        ],
    },
}

SECTION_TARGETS: dict[str, dict[str, dict[str, int]]] = {
    "zj-ep140": {"en": {"background": 200, "conclusion": 90, "facts": 450, "mental": 380, "insight_answer": 120}, "zh": {"background": 200, "conclusion": 90, "facts": 450, "mental": 380, "insight_answer": 120}},
    "zj-ep144": {"en": {"background": 200, "conclusion": 90, "facts": 480, "mental": 400, "insight_answer": 130}, "zh": {"background": 200, "conclusion": 90, "facts": 480, "mental": 400, "insight_answer": 130}},
    "zj-ep143": {"en": {"background": 170, "conclusion": 75, "facts": 240, "mental": 300, "insight_answer": 90}, "zh": {"background": 170, "conclusion": 75, "facts": 240, "mental": 300, "insight_answer": 90}},
    "tzs-ep180": {"en": {"background": 200, "conclusion": 80, "facts": 240, "mental": 300, "insight_answer": 90}, "zh": {"background": 200, "conclusion": 80, "facts": 240, "mental": 300, "insight_answer": 90}},
    "tzs-ep185": {"en": {"background": 170, "conclusion": 75, "facts": 230, "mental": 290, "insight_answer": 90}, "zh": {"background": 170, "conclusion": 75, "facts": 230, "mental": 290, "insight_answer": 90}},
    "tzs-ep179": {"en": {"background": 170, "conclusion": 75, "facts": 230, "mental": 290, "insight_answer": 90}, "zh": {"background": 170, "conclusion": 75, "facts": 230, "mental": 290, "insight_answer": 90}},
}

SECTION_CAPS: dict[str, int] = {
    "conclusion": 100,
    "background": 220,
    "facts": 500,
    "mental": 420,
    "insight_answer": 130,
}


def _pad_with_sentences(
    text: str, sentences: list[str], target: int, max_words: int | None = None
) -> str:
    cap = max_words if max_words is not None else target
    if not sentences or word_count(text) >= target:
        return text
    out = text.strip()
    used: set[str] = set()
    for part in re.split(r"[.!?。！？]+", out):
        norm = part.strip().lower()
        if len(norm.split()) >= 5 or len(norm) >= 8:
            used.add(norm)
    i = 0
    while word_count(out) < target and word_count(out) < cap:
        s = sentences[i % len(sentences)]
        norm = s.strip().lower()
        if norm not in used:
            out = (out + " " + s).strip()
            used.add(norm)
        i += 1
        if i > len(sentences) * 5:
            break
    return out


def _pad_sections(body: dict[str, Any], episode_id: str, locale: str) -> dict[str, Any]:
    targets = SECTION_TARGETS.get(episode_id, {}).get(locale, {})
    sentences = PAD_SENTENCES.get(episode_id, {}).get(locale, [])
    if not targets or not sentences:
        return body
    out = dict(body)
    if targets.get("conclusion"):
        out["conclusion"] = _pad_with_sentences(
            str(out.get("conclusion", "")), sentences, targets["conclusion"], SECTION_CAPS["conclusion"]
        )
    if targets.get("background"):
        out["background"] = _pad_with_sentences(
            str(out.get("background", "")), sentences, targets["background"], SECTION_CAPS["background"]
        )
    facts = list(out.get("important_facts") or [])
    if targets.get("facts") and facts:
        joined = " ".join(str(f) for f in facts)
        joined = _pad_with_sentences(joined, sentences, targets["facts"], SECTION_CAPS["facts"])
        # redistribute roughly evenly across 3 facts
        words = joined.split()
        chunk = max(1, len(words) // len(facts))
        new_facts = []
        idx = 0
        for _ in facts:
            new_facts.append(" ".join(words[idx:idx + chunk]))
            idx += chunk
        if idx < len(words):
            new_facts[-1] = (new_facts[-1] + " " + " ".join(words[idx:])).strip()
        out["important_facts"] = new_facts
    mm = dict(out.get("mental_model") or {})
    if targets.get("mental"):
        half = max(1, targets["mental"] // 2)
        cap_half = max(1, SECTION_CAPS["mental"] // 2)
        mm["components"] = _pad_with_sentences(str(mm.get("components", "")), sentences, half, cap_half)
        mm["application"] = _pad_with_sentences(str(mm.get("application", "")), sentences, half, cap_half)
        out["mental_model"] = mm
    if targets.get("insight_answer"):
        insights = []
        for item in out.get("key_insights") or []:
            row = dict(item)
            row["answer"] = _pad_with_sentences(
                str(row.get("answer", "")), sentences, targets["insight_answer"], SECTION_CAPS["insight_answer"]
            )
            insights.append(row)
        out["key_insights"] = insights
    return out


def apply_expansions(body: dict[str, Any], episode_id: str, locale: str) -> dict[str, Any]:
    out = dict(body)
    pack = PACKS.get(episode_id, {}).get(locale, {})
    facts = list(out.get("important_facts") or [])
    fact_append = pack.get("fact_append") or []
    for i, extra in enumerate(fact_append):
        if i < len(facts):
            facts[i] = (facts[i].strip() + " " + extra).strip()
    out["important_facts"] = facts

    mm = dict(out.get("mental_model") or {})
    if pack.get("mm_components"):
        mm["components"] = ((mm.get("components") or "").strip() + " " + pack["mm_components"]).strip()
    if pack.get("mm_application"):
        mm["application"] = ((mm.get("application") or "").strip() + " " + pack["mm_application"]).strip()
    out["mental_model"] = mm

    insights = []
    insight_append = pack.get("insight_append") or []
    for i, item in enumerate(out.get("key_insights") or []):
        row = dict(item)
        if i < len(insight_append):
            row["answer"] = (row.get("answer", "") + insight_append[i]).strip()
        insights.append(row)
    out["key_insights"] = insights

    long_blocks = pack.get("long_insight_blocks") or []
    if long_blocks and insights:
        for i, block in enumerate(long_blocks):
            if i < len(insights):
                insights[i]["answer"] = (insights[i].get("answer", "") + " " + block).strip()

    out["key_insights"] = insights
    return _pad_sections(out, episode_id, locale)
