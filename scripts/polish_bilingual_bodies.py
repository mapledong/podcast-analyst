"""Polish REFINED bodies: dedupe sentences and localize Chinese prose."""

from __future__ import annotations

import re
from typing import Any

# Order matters: longer phrases first.
_ZH_GLOSSARY: list[tuple[str, str]] = [
    (r"\btotal addressable market\b", "目标市场规模"),
    (r"\breturn on invested capital\b", "投入资本回报率"),
    (r"\bweighted average cost of capital\b", "加权平均资本成本"),
    (r"\bgross margin trajectory\b", "毛利率走势"),
    (r"\bmargin trajectory\b", "毛利率走势"),
    (r"\bcommercial recurring revenue\b", "商业经常性收入"),
    (r"\bannual recurring revenue\b", "年度经常性收入"),
    (r"\benterprise attach\b", "企业端绑定"),
    (r"\bworking estimate\b", "工作假设"),
    (r"\bbull case\b", "乐观情景"),
    (r"\bbear case\b", "悲观情景"),
    (r"\bproduct bet\b", "产品赌注"),
    (r"\bproduct bets\b", "产品赌注"),
    (r"\btop-down\b", "自上而下"),
    (r"\bworkflow\b", "工作流"),
    (r"\bworkflows\b", "工作流"),
    (r"\bdiligence\b", "尽职调查"),
    (r"\bcohorts\b", "用户群组"),
    (r"\bcohort\b", "用户群组"),
    (r"\battach\b", "绑定"),
    (r"\bcompounder\b", "复利型公司"),
    (r"\bcompounders\b", "复利型公司"),
    (r"\bguidance\b", "业绩指引"),
    (r"\bpipeline\b", "产品管线"),
    (r"\btrajectory\b", "走势"),
    (r"\bunderwrite\b", "押注"),
    (r"\bunderwriting\b", "押注"),
    (r"\bdistill(?:ation|ing)?\b", "蒸馏"),
    (r"\bchurn\b", "客户流失"),
    (r"\bcoding\b", "编程"),
    (r"\bagent\b", "智能体"),
    (r"\bagents\b", "智能体"),
    (r"\bsegment\b", "细分"),
    (r"\bsegments\b", "细分"),
    (r"\brecurring\b", "经常性"),
    (r"\balone\b", "单独"),
    (r"\braw\b", "原始"),
    (r"\bbet\b", "赌注"),
    (r"\bbets\b", "赌注"),
    (r"\bIQ\b", "智能"),
    (r"\blab\b", "实验室"),
    (r"\blabs\b", "实验室"),
    (r"\bARR\b", "年度经常性收入"),
    (r"\bROIC\b", "投入资本回报率"),
    (r"\bWACC\b", "加权平均资本成本"),
    (r"\bTAM\b", "目标市场规模"),
    (r"\bPE\b", "市盈率"),
    (r"\bmargin\b", "毛利率"),
    (r"\bmargins\b", "毛利率"),
    (r"\bpure play\b", "纯方向押注"),
    (r"\bpure bet\b", "纯方向赌注"),
    (r"\balpha\b", "超额收益"),
    (r"\bcapex\b", "资本开支"),
    (r"\bmark-to-cycle\b", "按周期定价"),
    (r"\bmark-to-hype\b", "按叙事定价"),
    (r"\bposition sizing\b", "仓位配置"),
    (r"\bscenario table\b", "情景分析表"),
    (r"\bvalue trap\b", "价值陷阱"),
    (r"\bde-risk(?:ing)?\b", "降低风险敞口"),
    (r"\bcontrarian\b", "逆向"),
    (r"\boverweight\b", "超配"),
    (r"\bunderweight\b", "低配"),
    (r"\bnarrative\b", "叙事"),
    (r"\bhyper-growth\b", "超高速增长"),
    (r"\bimpossible bar\b", "不可能的高标杆"),
    (r"\bfast-fashion\b", "快时尚"),
    (r"\bcharacter equity\b", "角色资产"),
    (r"\bfad\b", "风潮"),
    (r"\bchoke point\b", "关键瓶颈"),
    (r"\butilization\b", "产能利用率"),
    (r"\bfoundry\b", "晶圆代工"),
    (r"\bco-development\b", "联合研发"),
    (r"\blocalization\b", "本土化"),
    (r"\bfree cash flow\b", "自由现金流"),
    (r"\bFCF\b", "自由现金流"),
    (r"\bIPO\b", "首次公开发行"),
    (r"\bmacro\b", "宏观"),
    (r"\bstructural\b", "结构性"),
    (r"\bcyclical\b", "周期性"),
    (r"\bquality compounder\b", "优质复利型公司"),
    (r"\bquality compounders\b", "优质复利型公司"),
    (r"\bfriends of time\b", "时间的朋友"),
    (r"\btime-to-leader\b", "成为品类第一所需时间"),
    (r"\bstock keeping unit\b", "库存单位"),
    (r"\bSKU\b", "库存单位"),
    (r"\bSG&A\b", "销售及管理费用"),
    (r"\bDTC\b", "直营"),
    (r"\bOEM\b", "整车厂"),
    (r"\bASP\b", "平均售价"),
    (r"\bL2\+\b", "L2+"),
    (r"\bL4\b", "L4"),
    (r"\bsum-of-the-parts\b", "分部估值"),
    (r"\bburn\b", "现金消耗"),
    (r"\bwin rate\b", "胜率"),
    (r"\bwin-rate\b", "胜率"),
    (r"\bmoat\b", "护城河"),
    (r"\brunway\b", "再投资空间"),
    (r"\bcapital allocation\b", "资本配置"),
    (r"\bcapital cycle\b", "资本周期"),
    (r"\bintrinsic value\b", "内在价值"),
    (r"\bforward returns\b", "远期回报"),
    (r"\bovercapacity\b", "产能过剩"),
    (r"\bover-ownership\b", "过度持仓"),
    (r"\bchecklist\b", "检查清单"),
    (r"\bstress-test\b", "压力测试"),
    (r"\bfeed(?:ing)?\b", "承接"),
    (r"\bfunnel\b", "漏斗"),
    (r"\bprestige\b", "声望"),
    (r"\bstall\b", "停滞"),
    (r"\bupside\b", "上行"),
    (r"\bdownside\b", "下行"),
    (r"\block-in\b", "锁定"),
    (r"\bgo-to-market\b", "上市路径"),
    (r"\beval\b", "评测"),
    (r"\bevals\b", "评测"),
    (r"\bhero-founder\b", "英雄式创始人"),
    (r"\blone researcher\b", "孤胆研究者"),
    (r"\blone-researcher\b", "孤胆研究者"),
    (r"\bparameter counts\b", "参数量"),
    (r"\bleaderboard\b", "榜单"),
    (r"\bmindshare\b", "心智份额"),
    (r"\bvolume war\b", "拉量战"),
    (r"\bconsumer hits\b", "消费端爆款"),
    (r"\bflagship\b", "旗舰"),
    (r"\bretention\b", "留存"),
    (r"\btraining capex\b", "训练资本开支"),
    (r"\bmodel alpha\b", "模型超额收益"),
    (r"\bcommercialization\b", "商业化"),
    (r"\bcommercialization path\b", "商业化路径"),
    (r"\bIPO flood\b", "新股密集发行"),
    (r"\bmedia saturation\b", "媒体饱和"),
    (r"\binflows\b", "资金流入"),
    (r"\binflow\b", "资金流入"),
    (r"\bpositioning\b", "仓位"),
    (r"\bposition\b", "仓位"),
    (r"\bdrawdown\b", "回撤"),
    (r"\bdrawdowns\b", "回撤"),
    (r"\bthesis\b", "投资论点"),
    (r"\btrap\b", "陷阱"),
    (r"\bcomp\b", "可比公司"),
    (r"\bcomps\b", "可比公司"),
    (r"\bmiss\b", "不及预期"),
    (r"\btrigger\b", "触发"),
    (r"\btransition year\b", "过渡年"),
    (r"\btransition years\b", "过渡年"),
    (r"\bmultiple\b", "估值倍数"),
    (r"\bmultiples\b", "估值倍数"),
    (r"\bcompound\b", "复利"),
    (r"\bcompounding\b", "复利"),
    # Additional phrases for Chinese pilot cleanup
    (r"\bsustained\b", "持续"),
    (r"\bflatten(?:ing)?\b", "走平"),
    (r"\bflatten\b", "走平"),
    (r"\bcharacter[- ]IP\b", "角色知识产权"),
    (r"\bcharacter equity\b", "角色资产"),
    (r"\bcharacter-IP\b", "角色知识产权"),
    (r"\bfast[- ]fashion\b", "快时尚"),
    (r"\bimpossible bar\b", "不可能的高标杆"),
    (r"\bhyper[- ]growth\b", "超高速增长"),
    (r"\bperpetual\b", "永续"),
    (r"\bnear[- ]term\b", "短期"),
    (r"\bbull/base/bear\b", "乐观/基准/悲观"),
    (r"\bbull/bear\b", "多空"),
    (r"\bbase case\b", "基准情景"),
    (r"\bscenario\b", "情景"),
    (r"\bscenarios\b", "情景"),
    (r"\bexecute\b", "兑现"),
    (r"\bexecuted\b", "兑现"),
    (r"\btrigger\b", "触发"),
    (r"\bquarter\b", "季度"),
    (r"\bquarterly\b", "季度"),
    (r"\bposition sizing\b", "仓位配置"),
    (r"\bsizing\b", "配置"),
    (r"\btraditional\b", "传统"),
    (r"\bleadership\b", "领先地位"),
    (r"\badjacent\b", "相邻"),
    (r"\badjacents\b", "相邻品类"),
    (r"\boverweight\b", "超配"),
    (r"\bunderweight\b", "低配"),
    (r"\bexecution\b", "执行"),
    (r"\bhype\b", "炒作"),
    (r"\bjudgment\b", "判断力"),
    (r"\brespect\b", "重视"),
    (r"\bingest\b", "消化"),
    (r"\babundant\b", "充裕"),
    (r"\brace\b", "竞赛"),
    (r"\bpivot\b", "转向"),
    (r"\bquality\b", "优质"),
    (r"\bquality compounder\b", "优质复利型公司"),
    (r"\bcontrarian\b", "逆向"),
    (r"\ballocator\b", "资本配置者"),
    (r"\bcapital allocator\b", "资本配置者"),
    (r"\bmacro\b", "宏观"),
    (r"\bstructural\b", "结构性"),
    (r"\bstructural tailwind\b", "结构性顺风"),
    (r"\bmark-to-cycle\b", "按周期定价"),
    (r"\bmark-to-hype\b", "按叙事定价"),
    (r"\bmark to cycle\b", "按周期定价"),
    (r"\bmark to hype\b", "按叙事定价"),
    (r"\butilization\b", "产能利用率"),
    (r"\bmature\b", "成熟制程"),
    (r"\badvanced\b", "先进制程"),
    (r"\bvolume\b", "出货量"),
    (r"\bduplicate\b", "重复"),
    (r"\bdominance\b", "主导地位"),
    (r"\bcorrection\b", "修正"),
    (r"\binventory correction\b", "库存修正"),
    (r"\bco-development\b", "联合研发"),
    (r"\breliability\b", "可靠性"),
    (r"\bconflict\b", "冲突"),
    (r"\bdesign\b", "设计"),
    (r"\bfab\b", "产线"),
    (r"\bheadlines\b", "头条"),
    (r"\bheadline\b", "头条"),
    (r"\bsubsidy\b", "补贴"),
    (r"\btailwind\b", "顺风"),
    (r"\bchoke point\b", "关键瓶颈"),
    (r"\bbinary risk\b", "二元风险"),
    (r"\bloss-making\b", "亏损"),
    (r"\bbracket\b", "框定"),
    (r"\beconomics\b", "经济学"),
    (r"\bscale\b", "规模"),
    (r"\bcustomer\b", "客户"),
    (r"\bauto\b", "汽车"),
    (r"\bindustrial\b", "工业"),
    (r"\bmemory\b", "存储"),
    (r"\bmarathon\b", "马拉松"),
    (r"\bsingle tech bet\b", "单一技术赌注"),
    (r"\bROI\b", "投资回报"),
    (r"\bvalue trap\b", "价值陷阱"),
    (r"\btemporary mispricing\b", "暂时错价"),
    (r"\bde-risk(?:ing)?\b", "降低风险敞口"),
    (r"\bpositioning\b", "仓位"),
    (r"\bcurrent positioning\b", "当前仓位"),
    (r"\binflow\b", "资金流入"),
    (r"\binflows\b", "资金流入"),
    (r"\bIPO flood\b", "新股密集发行"),
    (r"\bmedia saturation\b", "媒体饱和"),
    (r"\bweekly inflow\b", "周度资金流入"),
    (r"\bconsensus comfort\b", "共识舒适区"),
    (r"\bindependent thesis\b", "独立投资论点"),
    (r"\bforward returns\b", "远期回报"),
    (r"\breinvestment\b", "再投资"),
    (r"\brunway\b", "再投资空间"),
    (r"\bdurable moat\b", "持久护城河"),
    (r"\bmoat\b", "护城河"),
    (r"\bprice discipline\b", "价格纪律"),
    (r"\bgrowth investing\b", "成长投资"),
    (r"\btrim\b", "减仓"),
    (r"\bentry\b", "入场"),
    (r"\bentry case studies\b", "入场案例"),
    (r"\breduce exposure\b", "降低敞口"),
    (r"\bsector\b", "板块"),
    (r"\bsectors\b", "板块"),
    (r"\bprofit\b", "利润"),
    (r"\bovercapacity\b", "产能过剩"),
    (r"\brecovery\b", "复苏"),
    (r"\btriad\b", "三角"),
    (r"\bmature compounder\b", "成熟复利型公司"),
    (r"\bjustify\b", "支撑"),
    (r"\bjustified\b", "有理由的"),
    (r"\btransition year\b", "过渡年"),
    (r"\btransition years\b", "过渡年"),
    (r"\bchecklist\b", "检查清单"),
    (r"\bverdict\b", "判断"),
    (r"\bindicator\b", "指标"),
    (r"\bcontrarian indicator\b", "逆向指标"),
    (r"\bmutual fund\b", "公募基金"),
    (r"\bmutual funds\b", "公募基金"),
    (r"\bmutual-fund\b", "公募基金"),
    (r"\bherding\b", "抱团"),
    (r"\bpeak\b", "峰值"),
    (r"\bpeaks\b", "峰值"),
    (r"\btrough\b", "低谷"),
    (r"\btroughs\b", "低谷"),
    (r"\bstable\b", "稳定"),
    (r"\bpremium\b", "溢价"),
    (r"\btrap\b", "陷阱"),
    (r"\bcompounders\b", "复利型公司"),
    (r"\bcompounder\b", "复利型公司"),
    (r"\bcompounders\b", "复利型公司"),
    (r"\bfrontier\b", "前沿"),
    (r"\bscaling\b", "规模扩张"),
    (r"\bstress-test\b", "压力测试"),
    (r"\bfeeding\b", "承接"),
    (r"\bteam\b", "团队"),
    (r"\bsegment\b", "细分"),
    (r"\bsegments\b", "细分"),
    (r"\brecurring\b", "经常性"),
    (r"\btop-down\b", "自上而下"),
    (r"\bsticky\b", "粘性"),
    (r"\bproduct roadmap\b", "产品路线图"),
    (r"\broadmap\b", "路线图"),
    (r"\bboom\b", "繁荣"),
    (r"\bcoincide\b", "重合"),
    (r"\bcoincides\b", "重合"),
    (r"\buntil cycle turns\b", "直至周期转折"),
    (r"\bclassical\b", "经典"),
    (r"\boversupply\b", "供给过剩"),
    (r"\binfrastructure\b", "基础设施"),
    (r"\binfra\b", "基础设施"),
    (r"\bmixed\b", "分化"),
    (r"\bmiss\b", "不及预期"),
    (r"\bplatform\b", "平台"),
    (r"\bcategory leader\b", "品类第一"),
    (r"\bcategory\b", "品类"),
    (r"\bcommodity\b", "大宗商品"),
    (r"\bceiling\b", "天花板"),
    (r"\bmental ceiling\b", "心理上限"),
    (r"\bexpansion\b", "扩张"),
    (r"\bcontext\b", "上下文"),
    (r"\btoken\b", "词元"),
    (r"\btokens\b", "词元"),
    (r"\bLLM\b", "大语言模型"),
    (r"\bPPT\b", "演示文稿"),
    (r"\bSKU\b", "库存单位"),
    (r"\bSG&A\b", "销售及管理费用"),
    (r"\bEPS\b", "每股收益"),
    (r"\bIDM\b", "垂直整合制造商"),
    (r"\bfoundry\b", "晶圆代工"),
    (r"\bnode\b", "制程节点"),
    (r"\blithography\b", "光刻"),
    (r"\bgeopolitical\b", "地缘政治"),
    (r"\blocalization\b", "本土化"),
    (r"\bLocalization\b", "本土化"),
    (r"\bAll-in\b", "全力押注"),
    (r"\ball-in\b", "全力押注"),
    (r"\bburn\b", "现金消耗"),
    (r"\bOEM\b", "整车厂"),
    (r"\babundant\b", "充裕"),
    (r"\bfeed\b", "承接"),
    (r"\bhero-founder\b", "英雄式创始人"),
    (r"\blone researcher\b", "孤胆研究者"),
    (r"\blone-researcher\b", "孤胆研究者"),
    (r"\bcoding\b", "编程"),
    (r"\bagent\b", "智能体"),
    (r"\bagents\b", "智能体"),
    (r"\braw\b", "原始"),
    (r"\bbet\b", "赌注"),
    (r"\bbets\b", "赌注"),
    (r"\bdiligence\b", "尽职调查"),
    (r"\bcohort\b", "用户群组"),
    (r"\bcohorts\b", "用户群组"),
    (r"\battach\b", "绑定"),
    (r"\balone\b", "单独"),
    (r"\blab\b", "实验室"),
    (r"\blabs\b", "实验室"),
    (r"\bCharacter\b", "角色"),
    (r"\bcharacter\b", "角色"),
]

# Preserve tickers, brands, and technical tokens.
_KEEP_LATIN = re.compile(
    r"\b(?:GOOGL|XPEV|TSLA|NVDA|AMZN|DIS|TSM|ASML|BRK\.B|"
    r"300866\.SZ|9992\.HK|0981\.HK|XPEV|"
    r"Google|Anthropic|OpenAI|Gemini|Claude|ChatGPT|Doubao|"
    r"Intel|Disney|Labubu|Hello Kitty|Apple|Nvidia|Tesla|"
    r"Figure|Optimus|IRON|GX|SMIC|TSMC|Graham|Buffett|Alphabet|"
    r"YouTube|Amazon|XPeng|Anker|Pop Mart|Jeff|David)\b",
    re.I,
)


def _split_sentences(text: str) -> list[str]:
    parts = re.split(r"(?<=[。！？!?])\s*|(?<=[.!?])\s+", text.strip())
    return [p.strip() for p in parts if p.strip()]


def _norm_sentence(s: str) -> str:
    return re.sub(r"\s+", " ", s.strip().lower())


def dedupe_text(text: str) -> str:
    if not text or not text.strip():
        return text
    seen: set[str] = set()
    kept: list[str] = []
    for sent in _split_sentences(text):
        norm = _norm_sentence(sent)
        if len(norm) < 12:
            kept.append(sent)
            continue
        if norm in seen:
            continue
        seen.add(norm)
        kept.append(sent)
    # Chinese: join without extra spaces; Latin-heavy: space join
    cjk = sum(1 for c in "".join(kept) if "\u4e00" <= c <= "\u9fff")
    if cjk > len("".join(kept)) * 0.3:
        return "".join(kept)
    return " ".join(kept)


def localize_zh_text(text: str) -> str:
    if not text:
        return text
    out = text
    for pattern, repl in _ZH_GLOSSARY:
        out = re.sub(pattern, repl, out, flags=re.IGNORECASE)
    # Clean leftover English filler phrases common in drafts
    out = re.sub(r"\s+alone\b", "", out, flags=re.I)
    out = re.sub(r"\s+not\s+", "而非", out, count=0)
    out = re.sub(r"\s{2,}", " ", out)
    return out.strip()


def _polish_string(s: str, locale: str) -> str:
    s = dedupe_text(s)
    # Chinese bodies are authored in full Chinese; glossary pass creates hybrid text.
    return s


def polish_body(body: dict[str, Any], locale: str) -> dict[str, Any]:
    out = dict(body)
    for key in ("conclusion", "background", "competitive_advantage"):
        if key in out and out[key]:
            out[key] = _polish_string(str(out[key]), locale)

    facts = []
    for fact in out.get("important_facts") or []:
        facts.append(_polish_string(str(fact), locale))
    out["important_facts"] = facts

    mm = dict(out.get("mental_model") or {})
    if mm:
        if mm.get("name"):
            mm["name"] = _polish_string(str(mm["name"]), locale) if locale == "zh" else dedupe_text(str(mm["name"]))
        if mm.get("components"):
            mm["components"] = _polish_string(str(mm["components"]), locale)
        if mm.get("application"):
            mm["application"] = _polish_string(str(mm["application"]), locale)
        out["mental_model"] = mm

    insights = []
    for item in out.get("key_insights") or []:
        row = dict(item)
        for field in ("view", "question", "answer"):
            if row.get(field):
                row[field] = _polish_string(str(row[field]), locale)
        insights.append(row)
    out["key_insights"] = insights

    clues = []
    for clue in out.get("top_investment_implications") or []:
        row = dict(clue)
        if row.get("thesis"):
            row["thesis"] = _polish_string(str(row["thesis"]), locale)
        clues.append(row)
    out["top_investment_implications"] = clues

    quotes = [_polish_string(str(q), locale) for q in out.get("golden_quotes") or []]
    out["golden_quotes"] = quotes

    chrono = dict(out.get("chronology") or {})
    if chrono.get("subject") and locale == "zh":
        chrono["subject"] = dedupe_text(str(chrono["subject"]))
    events = []
    for ev in chrono.get("events") or []:
        row = dict(ev)
        if row.get("event"):
            row["event"] = _polish_string(str(row["event"]), locale)
        events.append(row)
    if events:
        chrono["events"] = events
    if chrono:
        out["chronology"] = chrono

    return out


def polish_refined(refined: dict[str, dict[str, dict[str, Any]]]) -> dict[str, dict[str, dict[str, Any]]]:
    out: dict[str, dict[str, dict[str, Any]]] = {}
    for eid, locales in refined.items():
        out[eid] = {}
        for locale, body in locales.items():
            out[eid][locale] = polish_body(body, locale)
    return out
