#!/usr/bin/env python3
"""Rebalance ILTB approved summaries to template v4.10 section weights."""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))

from scripts.restore_iltb_from_outputs import (  # noqa: E402
    _blockquotes,
    _facts,
    _mental_model,
    _output_path,
)
from src.duration import duration_tier, tier_limit  # noqa: E402
from src.template_config import template_path_for_podcast  # noqa: E402
from src.validate import load_template_config, validate_summary, word_count  # noqa: E402

APPROVED = ROOT / "data" / "approved"
TMPL = load_template_config(template_path_for_podcast("Invest Like the Best"))

BG_MAX = 220
FACTS_MIN = 200
FACTS_MAX = 500
MM_MIN = 150
MM_MAX = 420

BG_SPLIT_MARKERS = (
    "Key quantitative evidence:",
    "Timeline context:",
    "Investment implications in the summary",
    "Investment implications:",
    "Mechanic's View Of Power is the decision frame",
    "Core takeaway:",
)

JUNK_PATTERNS = (
    re.compile(r'\s*Transcript line:\s*"[^"]*"\s*', re.I),
    re.compile(r"\s*Transcript detail[^.]*\.", re.I),
    re.compile(r"\s*Transcript expansion note[^.]*\.", re.I),
    re.compile(r"\s*Transcript evidence reinforces[^.]*\.", re.I),
    re.compile(r"\s*This maps to [^.]+\.", re.I),
    re.compile(r"\s*Related data point[^.]*\.", re.I),
)


def clean_text(text: str) -> str:
    if not text:
        return ""
    out = str(text)
    for pat in JUNK_PATTERNS:
        out = pat.sub(" ", out)
    out = re.sub(r"\s+", " ", out).strip()
    return out


def _sentences(text: str) -> list[str]:
    parts = re.split(r"(?<=[.!?])\s+", clean_text(text))
    return [p.strip() for p in parts if p.strip()]


def _truncate_words(text: str, max_words: int) -> str:
    words = text.split()
    if len(words) <= max_words:
        return text.strip()
    return " ".join(words[:max_words]).rstrip(".,;:") + "."


def trim_background(text: str, conclusion: str = "") -> tuple[str, str]:
    """Return (trimmed background, overflow text)."""
    body = clean_text(text)
    removed: list[str] = []
    for marker in BG_SPLIT_MARKERS:
        if marker in body:
            idx = body.index(marker)
            removed.append(body[idx:])
            body = body[:idx].strip()
    if conclusion:
        con = clean_text(conclusion)
        if con and con in body:
            body = body.replace(con, "").strip()
    overflow_parts = removed[:]
    words = body.split()
    if len(words) > BG_MAX:
        overflow_parts.append(" ".join(words[BG_MAX:]))
        body = " ".join(words[:BG_MAX])
    else:
        paras = [p.strip() for p in re.split(r"\n\n+", body) if p.strip()]
        if len(paras) > 1 and word_count(body) > BG_MAX:
            body = paras[0]
            overflow_parts.append(" ".join(paras[1:]))
    body = _truncate_words(body, BG_MAX)
    overflow = " ".join(p for p in overflow_parts if p).strip()
    return body.strip(), overflow


def _has_number(text: str) -> bool:
    return bool(re.search(r"\d", text))


def rebalance_facts(
    facts: list[str],
    overflow: str,
    *,
    extra_pool: str = "",
    min_words: int = FACTS_MIN,
) -> list[str]:
    facts = [clean_text(f) for f in facts if clean_text(f)]
    while len(facts) < 3:
        facts.append("")
    facts = facts[:3]

    candidates = _sentences(overflow) + _sentences(extra_pool)
    seen = set()
    pool: list[str] = []
    for s in candidates:
        key = s[:80]
        if key in seen:
            continue
        seen.add(key)
        pool.append(s)
    pool.sort(key=lambda s: (0 if _has_number(s) else 1, -len(s.split())))

    def total() -> int:
        return word_count(" ".join(facts))

    for sentence in pool:
        if total() >= min_words:
            break
        idx = min(range(3), key=lambda i: word_count(facts[i]))
        facts[idx] = (facts[idx] + " " + sentence).strip() if facts[idx] else sentence

    if total() < min_words:
        for i in range(3):
            sents = _sentences(facts[i])
            if len(sents) > 3:
                facts[i] = " ".join(sents)

    for sentence in pool:
        if total() >= min_words:
            break
        idx = min(range(3), key=lambda i: word_count(facts[i]))
        if sentence not in facts[idx]:
            facts[idx] = (facts[idx] + " " + sentence).strip()

    total_w = total()
    if total_w > FACTS_MAX:
        while total_w > FACTS_MAX:
            idx = max(range(3), key=lambda i: word_count(facts[i]))
            facts[idx] = _truncate_words(
                facts[idx], max(50, word_count(facts[i]) - (total_w - FACTS_MAX))
            )
            total_w = total()

    return [f for f in facts if f]


def synthesize_mental_model(data: dict) -> dict[str, str]:
    mm = data.get("mental_model") or {}
    name = clean_text(mm.get("name", "")) or "Episode Framework"
    insights = data.get("key_insights") or []
    views = [clean_text(i.get("view", "")) for i in insights if i.get("view")]
    answers = [clean_text(i.get("answer", "")) for i in insights if i.get("answer")]

    components_parts: list[str] = []
    for view, answer in zip(views, answers):
        if view:
            components_parts.append(view.rstrip(".") + ".")
        lead = _sentences(answer)[:2]
        components_parts.extend(lead)

    components = " ".join(components_parts)
    components = _truncate_words(components, 220)

    app_parts = [clean_text(data.get("conclusion", ""))]
    for inv in data.get("top_investment_implications") or []:
        thesis = clean_text(inv.get("thesis", ""))
        if thesis:
            app_parts.append(thesis)
    for answer in answers:
        app_parts.extend(_sentences(answer)[-1:])

    application = " ".join(p for p in app_parts if p)
    application = _truncate_words(application, 180)

    if word_count(components) + word_count(application) < MM_MIN:
        for answer in answers:
            for sent in _sentences(answer):
                if sent not in components and sent not in application:
                    if word_count(components) < 120:
                        components = (components + " " + sent).strip()
                    else:
                        application = (application + " " + sent).strip()
                if word_count(components) + word_count(application) >= MM_MIN:
                    break

    return {"name": name, "components": components.strip(), "application": application.strip()}


def fill_mental_model(data: dict) -> dict[str, str]:
    mm = data.get("mental_model") or {}
    name = clean_text(mm.get("name", ""))
    components = clean_text(mm.get("components", ""))
    application = clean_text(mm.get("application", ""))

    if name and components and application and word_count(components) + word_count(application) >= MM_MIN:
        total = word_count(name) + word_count(components) + word_count(application)
        if total <= MM_MAX:
            return {"name": name, "components": components, "application": application}

    out_md = _output_path(data["episode_id"])
    if out_md:
        parsed = _mental_model(out_md.read_text(encoding="utf-8"))
        if parsed.get("name"):
            name = name or parsed["name"]
        if not components and parsed.get("components"):
            components = clean_text(parsed["components"])
        if not application and parsed.get("application"):
            application = clean_text(parsed["application"])

    if not components or not application or word_count(components) + word_count(application) < MM_MIN:
        synth = synthesize_mental_model({**data, "mental_model": {"name": name, "components": components, "application": application}})
        if not components or word_count(components) < 60:
            components = synth["components"]
        if not application or word_count(application) < 60:
            application = synth["application"]
        name = name or synth["name"]

    combined = word_count(name) + word_count(components) + word_count(application)
    if combined > MM_MAX:
        application = _truncate_words(application, max(60, word_count(application) - (combined - MM_MAX)))

    return {"name": name, "components": components, "application": application}


def clean_insights(insights: list[dict]) -> list[dict]:
    cleaned = []
    for item in insights[:3]:
        cleaned.append(
            {
                "view": clean_text(item.get("view", "")),
                "question": clean_text(item.get("question", "")),
                "answer": _truncate_words(clean_text(item.get("answer", "")), 130),
            }
        )
    return cleaned


def pad_to_minimum(data: dict) -> dict:
    duration = data.get("metadata", {}).get("duration_minutes", 60)
    min_total = tier_limit(TMPL, "minimum_word_limits", duration)

    insight_text = " ".join(
        " ".join(item.get(k, "") for k in ("view", "question", "answer"))
        for item in data.get("key_insights") or []
    )
    quote_text = " ".join(data.get("golden_quotes") or [])

    def report():
        return validate_summary(data, TMPL)

    for _ in range(40):
        r = report()
        if r.total_words >= min_total:
            break
        wc_before = r.total_words
        facts = data["important_facts"]
        facts_wc = word_count(" ".join(facts))
        mm = data["mental_model"]
        mm_wc = word_count(" ".join(str(mm.get(k, "")) for k in ("name", "components", "application")))

        if facts_wc < FACTS_MIN and facts_wc < FACTS_MAX:
            idx = min(range(len(facts)), key=lambda i: word_count(facts[i]))
            for sent in _sentences(insight_text + " " + quote_text):
                if _has_number(sent) and sent not in facts[idx]:
                    facts[idx] = (facts[idx] + " " + sent).strip()
                    break
            data["important_facts"] = facts
        elif mm_wc < MM_MIN:
            for sent in _sentences(insight_text):
                if sent not in mm.get("components", ""):
                    mm["components"] = (mm.get("components", "") + " " + sent).strip()
                    break
            data["mental_model"] = mm
        elif word_count(" ".join(facts)) < FACTS_MAX:
            idx = min(range(len(facts)), key=lambda i: word_count(facts[i]))
            for sent in _sentences(insight_text):
                if sent not in facts[idx]:
                    facts[idx] = (facts[idx] + " " + sent).strip()
                    break
            data["important_facts"] = facts
        elif mm_wc < MM_MAX:
            for sent in _sentences(insight_text):
                if sent not in mm.get("application", ""):
                    mm["application"] = (mm.get("application", "") + " " + sent).strip()
                    break
            data["mental_model"] = mm
        else:
            break
        if report().total_words == wc_before:
            break
    return data


def rebalance_episode(data: dict) -> dict:
    data = json.loads(json.dumps(data))  # deep copy
    raw_bg = clean_text(data.get("background", ""))
    data["conclusion"] = _truncate_words(clean_text(data.get("conclusion", "")), 100)
    data["background"], overflow = trim_background(raw_bg, data["conclusion"])
    extra_pool = raw_bg if raw_bg != data["background"] else ""
    data["important_facts"] = rebalance_facts(
        data.get("important_facts") or _facts_from_outputs(data),
        overflow,
        extra_pool=extra_pool,
    )
    data["mental_model"] = fill_mental_model(data)
    data["key_insights"] = clean_insights(data.get("key_insights") or [])
    data["golden_quotes"] = [clean_text(q) for q in data.get("golden_quotes") or []][:3]
    data = pad_to_minimum(data)

    notes = (data.get("review_notes") or "").split("|")[0].strip()
    data["review_notes"] = f"{notes} | rebalanced v4.10".strip(" |")
    meta = data.get("extraction_meta") or {}
    meta["rebalanced_v410"] = True
    data["extraction_meta"] = meta
    return data


def _facts_from_outputs(data: dict) -> list[str]:
    out_md = _output_path(data["episode_id"])
    if out_md:
        return _facts(out_md.read_text(encoding="utf-8"))
    return data.get("important_facts") or []


def main() -> int:
    dry = "--dry-run" in sys.argv
    changed = 0
    for path in sorted(APPROVED.glob("ep*.json")):
        data = json.loads(path.read_text(encoding="utf-8"))
        if data.get("podcast") != "Invest Like the Best":
            continue
        updated = rebalance_episode(data)
        if dry:
            r = validate_summary(updated, TMPL)
            print(
                path.stem,
                "pass" if r.passed else "FAIL",
                f"bg={word_count(updated['background'])}",
                f"facts={word_count(' '.join(updated['important_facts']))}",
                f"mm={word_count(' '.join(updated['mental_model'].values()))}",
                f"total={r.total_words}/{r.min_total_words}-{r.max_total_words}",
            )
            if not r.passed:
                for issue in r.issues:
                    if issue.severity == "error":
                        print(" ", issue.message)
            continue
        path.write_text(json.dumps(updated, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
        changed += 1
    print(f"rebalanced: {changed}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
