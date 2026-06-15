"""Validate extracted summaries against template word limits."""

from __future__ import annotations

import json
import math
import re
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any

import yaml

from src.company_tickers import validate_keyword_tickers
from src.duration import duration_tier, tier_limit


def word_count(text: str) -> int:
    return len(text.split())


@dataclass
class ValidationIssue:
    section: str
    message: str
    severity: str = "error"


@dataclass
class ValidationReport:
    passed: bool
    total_words: int
    max_total_words: int
    min_total_words: int
    issues: list[ValidationIssue] = field(default_factory=list)

    def add(self, section: str, message: str, severity: str = "error") -> None:
        self.issues.append(ValidationIssue(section, message, severity))
        if severity == "error":
            self.passed = False


def load_template_config(path: Path) -> dict[str, Any]:
    return yaml.safe_load(path.read_text(encoding="utf-8"))


def _has_number(text: str) -> bool:
    return bool(re.search(r"\d", text))


def _rating_ok(value: Any) -> bool:
    try:
        n = float(value)
        return n == int(n) and 1 <= int(n) <= 5
    except (TypeError, ValueError):
        return False


_PROSE_SLOP_PATTERNS: list[tuple[str, re.Pattern[str]]] = [
    ("transcript meta-junk", re.compile(r"Transcript line\s*:", re.I)),
    ("transcript meta-junk", re.compile(r"This maps to\b", re.I)),
    ("transcript fragment junk", re.compile(r"He also gives a concrete magnitude:", re.I)),
    ("transcript fragment junk", re.compile(r"He states:\s*[\"']", re.I)),
    ("transcript fragment junk", re.compile(r"close of the discussion emphasizes operating truth", re.I)),
    ("transcript fragment junk", re.compile(r"It remains anchored in scale math and outcomes", re.I)),
    ("transcript fragment junk", re.compile(r"He ties execution to founder/customer reality:\s*[\"']", re.I)),
    ("incomplete transcript quote", re.compile(r"[\"'][A-Za-z][^\"']{0,60}\s*$")),
    ("AI boilerplate", re.compile(r"it['']s worth noting|it is worth noting", re.I)),
    ("AI boilerplate", re.compile(r"\bdelve\b", re.I)),
    ("AI boilerplate", re.compile(r"\bunderscores?\b", re.I)),
    ("AI boilerplate", re.compile(r"\bat its core\b", re.I)),
    ("AI boilerplate", re.compile(r"serves as a testament", re.I)),
    ("AI boilerplate", re.compile(r"In .+['']s framing", re.I)),
    ("stiff transition", re.compile(r"\b(Moreover|Furthermore)\b")),
]

_PROSE_BUZZWORDS = re.compile(
    r"\b(playbook|unlock|ecosystem|holistic|landscape|robust|paradigm|synergy|tapestry)\b",
    re.I,
)


def _summary_prose_blobs(data: dict[str, Any]) -> dict[str, str]:
    mm = data.get("mental_model") or {}
    blobs: dict[str, str] = {
        "conclusion": str(data.get("conclusion", "")),
        "background": str(data.get("background", "")),
        "competitive_advantage": str(data.get("competitive_advantage", "")),
        "important_facts": " ".join(str(f) for f in data.get("important_facts", [])),
        "mental_model": " ".join(
            str(mm.get(k, "")) for k in ("name", "components", "application")
        ),
    }
    for i, insight in enumerate(data.get("key_insights", [])):
        blobs[f"key_insights[{i}]"] = " ".join(
            str(insight.get(k, "")) for k in ("view", "question", "answer")
        )
    for i, clue in enumerate(data.get("top_investment_implications", [])):
        blobs[f"top_investment_implications[{i}]"] = str(clue.get("thesis", ""))
    return blobs


def _normalize_sentence(s: str) -> str:
    return re.sub(r"\s+", " ", s.strip().lower())


def _validate_prose_style(
    data: dict[str, Any], template: dict[str, Any], report: ValidationReport
) -> None:
    if not (template.get("content_policy") or {}).get("prose_style"):
        return

    blobs = _summary_prose_blobs(data)
    combined = " ".join(blobs.values())

    for section, text in blobs.items():
        if not text.strip():
            continue
        for label, pattern in _PROSE_SLOP_PATTERNS:
            if pattern.search(text):
                report.add(
                    "prose_style",
                    f"{section}: {label} detected — rewrite in plain analyst voice",
                    "warning",
                )
                break

    buzz_hits = sorted({m.group(0).lower() for m in _PROSE_BUZZWORDS.finditer(combined)})
    if len(buzz_hits) >= 3:
        report.add(
            "prose_style",
            f"Buzzword stacking ({', '.join(buzz_hits[:5])}) — prefer concrete analyst prose",
            "warning",
        )

    sentences: list[tuple[str, str]] = []
    for section, text in blobs.items():
        for raw in re.split(r"[.!?]+", text):
            norm = _normalize_sentence(raw)
            if len(norm.split()) >= 10:
                sentences.append((section, norm))

    seen: dict[str, str] = {}
    for section, norm in sentences:
        if norm in seen and seen[norm] != section:
            preview = norm[:60] + ("…" if len(norm) > 60 else "")
            report.add(
                "prose_style",
                f"Duplicate sentence in {section} and {seen[norm]}: “{preview}”",
                "warning",
            )
        else:
            seen.setdefault(norm, section)


def _is_tradable_ticker(ticker: str) -> bool:
    raw = str(ticker or "").strip()
    if not raw or raw.lower().startswith("private:"):
        return False
    symbol = raw.split()[0].upper()
    return bool(re.match(r"^[A-Z]{1,5}(\.[A-Z]{1,2})?$", symbol))


def _validate_investment_policy(
    clues: list[dict[str, Any]], template: dict[str, Any], report: ValidationReport
) -> None:
    policy = template.get("investment_policy") or {}
    if not clues or not policy:
        return

    watch_count = sum(1 for c in clues if c.get("direction") == "Watch")
    directional_count = sum(1 for c in clues if c.get("direction") in ("Long", "Short"))
    watch_max = int(policy.get("watch_max_count", 1))

    if watch_count > watch_max:
        report.add(
            "top_investment_implications",
            f"{watch_count} Watch ideas exceed max {watch_max}; prefer directional Long/Short",
            "warning",
        )

    watch_tradable = [
        c.get("ticker", "")
        for c in clues
        if c.get("direction") == "Watch" and _is_tradable_ticker(c.get("ticker", ""))
    ]
    if watch_tradable:
        report.add(
            "top_investment_implications",
            f"Use Long/Short (not Watch) for tradable tickers: {', '.join(watch_tradable)}",
            "warning",
        )

    tradable = [c for c in clues if _is_tradable_ticker(c.get("ticker", ""))]
    if policy.get("require_directional_when_tradable") and tradable and directional_count == 0:
        report.add(
            "top_investment_implications",
            "Include at least one directional Long or Short when tradable tickers are cited",
            "warning",
        )


def validate_summary(data: dict[str, Any], template: dict[str, Any]) -> ValidationReport:
    duration = data.get("metadata", {}).get("duration_minutes", 60)
    tier = duration_tier(duration)
    max_total = tier_limit(template, "total_word_limits", duration)
    min_total = tier_limit(template, "minimum_word_limits", duration)
    report = ValidationReport(
        passed=True, total_words=0, max_total_words=max_total, min_total_words=min_total
    )

    rating = data.get("episode_rating", {})
    if not _rating_ok(rating.get("overall")):
        report.add("episode_rating", "Missing or invalid overall rating (1–5)")

    for section_id, value in {
        "conclusion": data.get("conclusion", ""),
        "background": data.get("background", ""),
        "competitive_advantage": data.get("competitive_advantage", ""),
        "golden_quotes": " ".join(data.get("golden_quotes", [])),
    }.items():
        cfg = next((s for s in template["sections"] if s["id"] == section_id), None)
        if not cfg:
            continue
        wc = word_count(str(value))
        report.total_words += wc
        if not str(value).strip():
            report.add(section_id, "Required section is empty")
        min_w = cfg.get("min_words")
        if min_w and wc < min_w:
            report.add(section_id, f"{wc} words below minimum of {min_w}", "warning")
        max_w = cfg.get("max_words")
        if max_w and wc > max_w:
            report.add(section_id, f"{wc} words exceeds limit of {max_w}")

    facts = data.get("important_facts", [])
    facts_cfg = next((s for s in template["sections"] if s["id"] == "important_facts"), None)
    if facts_cfg:
        wc = word_count(" ".join(facts))
        report.total_words += wc
        expected = facts_cfg.get("item_count", 3)
        if len(facts) != expected:
            report.add("important_facts", f"Expected {expected} facts, got {len(facts)}")
        if facts_cfg.get("min_words") and wc < facts_cfg["min_words"]:
            report.add(
                "important_facts", f"{wc} words below minimum {facts_cfg['min_words']}", "warning"
            )
        if facts_cfg.get("max_words") and wc > facts_cfg["max_words"]:
            report.add("important_facts", f"{wc} words exceeds {facts_cfg['max_words']}")
        if facts_cfg.get("require_quantitative"):
            for i, fact in enumerate(facts):
                if not _has_number(str(fact)):
                    report.add("important_facts", f"F{i + 1} needs a number", "warning")

    mm = data.get("mental_model", {})
    mm_cfg = next((s for s in template["sections"] if s["id"] == "mental_model"), None)
    if mm_cfg:
        if not mm.get("name") or not mm.get("components") or not mm.get("application"):
            report.add("mental_model", "Missing name, components, or application")
        mm_text = " ".join(str(mm.get(k, "")) for k in ("name", "components", "application"))
        wc = word_count(mm_text)
        report.total_words += wc
        if mm_cfg.get("min_words") and wc < mm_cfg["min_words"]:
            report.add(
                "mental_model", f"{wc} words below minimum {mm_cfg['min_words']}", "warning"
            )
        if mm_cfg.get("max_words") and wc > mm_cfg["max_words"]:
            report.add("mental_model", f"{wc} words exceeds {mm_cfg['max_words']}")

    insights = data.get("key_insights", [])
    insights_cfg = next((s for s in template["sections"] if s["id"] == "key_insights"), None)
    expected_insights = insights_cfg.get("item_count", 3) if insights_cfg else 3
    if len(insights) != expected_insights:
        report.add("key_insights", f"Expected {expected_insights} insights, got {len(insights)}")
    for i, item in enumerate(insights):
        for field in ("view", "question", "answer"):
            if not item.get(field):
                report.add("key_insights", f"Insight {i + 1} missing {field}")
        report.total_words += word_count(
            " ".join(item.get(k, "") for k in ("view", "question", "answer"))
        )

    adv_cfg = next((s for s in template["sections"] if s["id"] == "competitive_advantage"), None)
    if adv_cfg and adv_cfg.get("required"):
        adv = str(data.get("competitive_advantage", "")).strip()
        if not adv:
            report.add("competitive_advantage", "Required section is empty")
        wc = word_count(adv)
        report.total_words += wc
        if adv_cfg.get("max_words") and wc > adv_cfg["max_words"]:
            report.add("competitive_advantage", f"{wc} words exceeds {adv_cfg['max_words']}")

    clues = data.get("top_investment_implications", [])
    clues_cfg = next(
        (s for s in template["sections"] if s["id"] == "top_investment_implications"), None
    )
    if clues_cfg:
        min_n = clues_cfg.get("item_count_min", clues_cfg.get("item_count", 1))
        max_n = clues_cfg.get("item_count_max", clues_cfg.get("item_count", 3))
        if len(clues) < min_n or len(clues) > max_n:
            report.add(
                "top_investment_implications",
                f"Expected {min_n}–{max_n} ideas, got {len(clues)}",
            )
    valid_dirs = set(template.get("investment_directions", []))
    valid_conf = set(template.get("investment_confidence", []))
    for i, clue in enumerate(clues):
        for col in ("ticker", "direction", "confidence", "thesis"):
            if col not in clue:
                report.add("top_investment_implications", f"Row {i + 1} missing {col}")
        if clue.get("direction") not in valid_dirs:
            report.add("top_investment_implications", f"Row {i + 1}: invalid direction")
        if clue.get("confidence") not in valid_conf:
            report.add("top_investment_implications", f"Row {i + 1}: invalid confidence")
        report.total_words += word_count(clue.get("thesis", ""))
    _validate_investment_policy(clues, template, report)

    if report.total_words > max_total:
        report.add("total", f"Total {report.total_words} exceeds {max_total}", "warning")
    if min_total and report.total_words < min_total:
        report.add(
            "total",
            f"Total {report.total_words} below minimum {min_total} for tier {tier}",
            "warning",
        )

    chrono = data.get("chronology", {})
    chrono_cfg = next((s for s in template["sections"] if s["id"] == "chronology"), None)
    if chrono_cfg:
        if not chrono.get("subject"):
            report.add("chronology", "Missing subject")
        events = chrono.get("events", [])
        min_n = chrono_cfg.get("item_count_min", 5)
        max_n = chrono_cfg.get("item_count_max", 10)
        if len(events) < min_n or len(events) > max_n:
            report.add("chronology", f"Expected {min_n}–{max_n} events, got {len(events)}")
        for i, entry in enumerate(events):
            for field in ("date", "event"):
                if not entry.get(field):
                    report.add("chronology", f"Event {i + 1} missing {field}")

    keywords = data.get("keywords", [])
    kw_cfg = next((s for s in template["sections"] if s["id"] == "keywords"), None)
    if kw_cfg:
        min_n = kw_cfg.get("item_count_min", 3)
        max_n = kw_cfg.get("item_count_max", 5)
        if len(keywords) < min_n or len(keywords) > max_n:
            report.add("keywords", f"Expected {min_n}–{max_n} keywords, got {len(keywords)}")
        for i, kw in enumerate(keywords):
            if not str(kw).strip():
                report.add("keywords", f"Keyword {i + 1} is empty")

    for _section, message in validate_keyword_tickers(data):
        report.add("keywords", message, "warning")

    _validate_golden_quotes(data, report)
    _validate_prose_style(data, template, report)

    return report


def _validate_golden_quotes(data: dict[str, Any], report: ValidationReport) -> None:
    for i, quote in enumerate(data.get("golden_quotes", [])):
        q = str(quote).strip()
        if not q:
            report.add("golden_quotes", f"Quote {i + 1} is empty")
            continue
        if re.match(r'^["\']+', q):
            report.add(
                "golden_quotes",
                f"Quote {i + 1} has leading quote marks — store bare text; template adds quotes",
                "warning",
            )
        if re.match(r'^["\'].+["\']', q) and not re.match(r'^[^"\']+ — ', q):
            report.add(
                "golden_quotes",
                f"Quote {i + 1} wraps spoken text in quotes — remove JSON quote marks",
                "warning",
            )
        if '""' in q or "''" in q:
            report.add(
                "golden_quotes",
                f"Quote {i + 1} has doubled quote marks — normalize to one pair at render",
                "warning",
            )


def expansion_warnings(data: dict[str, Any], template: dict[str, Any]) -> list[ValidationIssue]:
    """Warnings that indicate a summary should be expanded (word mins, investment policy, etc.)."""
    report = validate_summary(data, template)
    return [issue for issue in report.issues if issue.severity == "warning"]


def needs_expansion(data: dict[str, Any], template: dict[str, Any]) -> bool:
    return bool(expansion_warnings(data, template))


def word_gap(data: dict[str, Any], template: dict[str, Any]) -> int:
    report = validate_summary(data, template)
    return max(0, report.min_total_words - report.total_words)


def _rating_cap(total: int, pct: float, method: str) -> int:
    if total <= 0:
        return 0
    if method == "ceil":
        return math.ceil(total * pct)
    return math.floor(total * pct)


def _load_library_ratings(
    approved_dir: Path,
    *,
    podcast: str | None = None,
    exclude_episode_id: str | None = None,
) -> list[int]:
    ratings: list[int] = []
    if not approved_dir.is_dir():
        return ratings
    podcast_key = (podcast or "").strip().lower()
    for path in sorted(approved_dir.glob("*.json")):
        episode_id = path.stem
        if exclude_episode_id and episode_id == exclude_episode_id:
            continue
        try:
            data = json.loads(path.read_text(encoding="utf-8"))
        except (json.JSONDecodeError, OSError):
            continue
        if podcast_key and str(data.get("podcast", "")).strip().lower() != podcast_key:
            continue
        overall = data.get("episode_rating", {}).get("overall")
        if _rating_ok(overall):
            ratings.append(int(overall))
    return ratings


def rating_distribution_stats(
    template: dict[str, Any],
    approved_dir: Path,
    *,
    podcast: str | None = None,
) -> dict[str, Any]:
    """Return counts and caps for a podcast library (or all podcasts if podcast is None)."""
    cfg = template.get("rating_distribution") or {}
    five_max_pct = float(cfg.get("five_star_max_pct", 0.20))
    four_max_pct = float(cfg.get("four_star_max_pct", 0.30))
    cap_method = str(cfg.get("cap_method", "floor"))
    ratings = _load_library_ratings(approved_dir, podcast=podcast)
    total = len(ratings)
    five_count = sum(1 for r in ratings if r == 5)
    four_count = sum(1 for r in ratings if r == 4)
    five_cap = _rating_cap(total, five_max_pct, cap_method)
    four_cap = _rating_cap(total, four_max_pct, cap_method)
    return {
        "podcast": podcast or "ALL",
        "total": total,
        "five_count": five_count,
        "four_count": four_count,
        "five_cap": five_cap,
        "four_cap": four_cap,
        "five_pct": round(100 * five_count / total, 1) if total else 0.0,
        "four_pct": round(100 * four_count / total, 1) if total else 0.0,
        "cap_method": cap_method,
    }


def choose_rating(
    candidate: int,
    template: dict[str, Any],
    approved_dir: Path,
    *,
    podcast: str | None = None,
    episode_id: str | None = None,
    default_rating: int | None = None,
) -> int:
    """Pick the highest allowed rating ≤ candidate, falling back to default_rating or 3."""
    cfg = template.get("rating_distribution") or {}
    fallback = int(default_rating if default_rating is not None else cfg.get("default_rating", 3))
    for rating in range(int(candidate), 0, -1):
        issues = validate_rating_distribution(
            rating,
            template,
            approved_dir,
            podcast=podcast,
            episode_id=episode_id,
        )
        if not any(i.severity == "error" for i in issues):
            return rating
    return fallback


def validate_rating_distribution(
    rating: int,
    template: dict[str, Any],
    approved_dir: Path,
    *,
    podcast: str | None = None,
    episode_id: str | None = None,
) -> list[ValidationIssue]:
    """Ensure 5★ ≤20% and 4★ ≤30% of the podcast library after this episode."""
    cfg = template.get("rating_distribution") or {}
    min_enforce = int(cfg.get("min_episodes_to_enforce", 5))
    five_max_pct = float(cfg.get("five_star_max_pct", 0.20))
    four_max_pct = float(cfg.get("four_star_max_pct", 0.30))
    cap_method = str(cfg.get("cap_method", "floor"))
    scope = str(cfg.get("scope", "per_podcast"))
    library_podcast = podcast if scope == "per_podcast" else None

    library = _load_library_ratings(
        approved_dir,
        podcast=library_podcast,
        exclude_episode_id=episode_id,
    )
    library.append(rating)
    total = len(library)
    if total == 0:
        return []

    five_count = sum(1 for r in library if r == 5)
    four_count = sum(1 for r in library if r == 4)
    five_cap = _rating_cap(total, five_max_pct, cap_method)
    four_cap = _rating_cap(total, four_max_pct, cap_method)
    issues: list[ValidationIssue] = []
    severity = "error" if total >= min_enforce else "warning"
    scope_label = podcast or "library"

    if five_count > five_cap:
        pct = round(100 * five_count / total)
        issues.append(
            ValidationIssue(
                "rating_distribution",
                f"{scope_label}: 5★ episodes {five_count}/{total} ({pct}%) exceed cap {five_cap} ({int(five_max_pct * 100)}%)",
                severity,
            )
        )
    if four_count > four_cap:
        pct = round(100 * four_count / total)
        issues.append(
            ValidationIssue(
                "rating_distribution",
                f"{scope_label}: 4★ episodes {four_count}/{total} ({pct}%) exceed cap {four_cap} ({int(four_max_pct * 100)}%)",
                severity,
            )
        )
    return issues
