"""Shared company name / ticker canonicalization (mirrors web/src/lib/tickers.ts)."""

from __future__ import annotations

import re
from functools import lru_cache
from pathlib import Path
from typing import Any

import yaml

ROOT = Path(__file__).resolve().parent.parent
DEFAULT_CONFIG = ROOT / "config" / "company_tickers.yaml"

_SIMPLE_TICKER_RE = re.compile(r"^[A-Z]{1,5}$")
_DOTTED_TICKER_RE = re.compile(r"^[A-Z0-9]{1,5}\.[A-Z0-9]{1,4}$")
_PRIVATE_PREFIX_RE = re.compile(r"^private:(.+)$", re.I)


def normalize_key(value: str) -> str:
    return value.strip().lower()


def is_ticker_symbol(value: str) -> bool:
    raw = value.strip()
    return bool(_SIMPLE_TICKER_RE.match(raw) or _DOTTED_TICKER_RE.match(raw))


@lru_cache(maxsize=1)
def load_company_tickers(config_path: Path | None = None) -> dict[str, Any]:
    path = config_path or DEFAULT_CONFIG
    data = yaml.safe_load(path.read_text(encoding="utf-8")) or {}
    aliases = {normalize_key(k): str(v).strip() for k, v in (data.get("aliases") or {}).items()}
    ticker_aliases = {
        str(k).strip().upper(): str(v).strip()
        for k, v in (data.get("ticker_aliases") or {}).items()
    }
    china_listings = data.get("china_listings") or {}
    return {"aliases": aliases, "ticker_aliases": ticker_aliases, "china_listings": china_listings}


def _resolve_ticker_alias(ticker: str, ticker_aliases: dict[str, str]) -> str:
    upper = ticker.strip().upper()
    seen: set[str] = set()
    while upper in ticker_aliases and upper not in seen:
        seen.add(upper)
        upper = ticker_aliases[upper]
    return upper


def canonical_company_label(value: str, *, config_path: Path | None = None) -> str:
    cfg = load_company_tickers(config_path)
    aliases: dict[str, str] = cfg["aliases"]
    ticker_aliases: dict[str, str] = cfg["ticker_aliases"]

    trimmed = value.strip()
    if not trimmed:
        return trimmed

    private_match = _PRIVATE_PREFIX_RE.match(trimmed)
    if private_match:
        return canonical_company_label(private_match.group(1), config_path=config_path)

    if is_ticker_symbol(trimmed):
        return _resolve_ticker_alias(trimmed, ticker_aliases)

    alias = aliases.get(normalize_key(trimmed))
    if alias:
        return _resolve_ticker_alias(alias, ticker_aliases)

    return trimmed


def canonical_company_key(value: str, *, config_path: Path | None = None) -> str:
    return normalize_key(canonical_company_label(value, config_path=config_path))


def company_filter_matches(extracted_value: str, filter_value: str, *, config_path: Path | None = None) -> bool:
    return canonical_company_key(extracted_value, config_path=config_path) == canonical_company_key(
        filter_value, config_path=config_path
    )


def keyword_should_use_ticker(keyword: str, *, config_path: Path | None = None) -> str | None:
    """Return canonical ticker if keyword is a known company name but not already a ticker."""
    trimmed = keyword.strip()
    if not trimmed or trimmed.lower().startswith("private:"):
        return None
    if is_ticker_symbol(trimmed):
        return None
    cfg = load_company_tickers(config_path)
    alias = cfg["aliases"].get(normalize_key(trimmed))
    if alias:
        return canonical_company_label(alias, config_path=config_path)
    return None


def normalize_keywords(keywords: list[Any], *, config_path: Path | None = None) -> tuple[list[str], list[tuple[str, str]]]:
    """Normalize keyword list; return (new_keywords, [(old, new), ...])."""
    changes: list[tuple[str, str]] = []
    normalized: list[str] = []
    seen: set[str] = set()

    for raw in keywords:
        original = str(raw).strip()
        if not original:
            continue

        ticker = keyword_should_use_ticker(original, config_path=config_path)
        label = ticker or original
        key = canonical_company_key(label, config_path=config_path)

        if key in seen:
            if ticker and original != label:
                changes.append((original, label))
            continue

        seen.add(key)
        if label != original:
            changes.append((original, label))
        normalized.append(label)

    return normalized, changes


def normalize_investment_ticker(ticker: str, *, config_path: Path | None = None) -> tuple[str, bool]:
    """Normalize investment row ticker; return (new_ticker, changed)."""
    raw = str(ticker or "").strip()
    if not raw or raw.lower().startswith("private:") or raw.startswith("Basket:"):
        return raw, False

    symbol = raw.split()[0]
    if not is_ticker_symbol(symbol):
        replacement = keyword_should_use_ticker(symbol, config_path=config_path)
        if replacement:
            suffix = raw[len(symbol) :]
            return replacement + suffix, True
        return raw, False

    canonical = canonical_company_label(symbol, config_path=config_path)
    if canonical != symbol:
        suffix = raw[len(symbol) :]
        return canonical + suffix, True
    return raw, False


def is_company_keyword(value: str, *, config_path: Path | None = None) -> bool:
    """True when a keyword/chip value is a company tag (ticker, Private:, or known alias)."""
    cfg = load_company_tickers(config_path)
    aliases: dict[str, str] = cfg["aliases"]
    china_listings: dict[str, Any] = cfg.get("china_listings") or {}

    trimmed = value.strip()
    if not trimmed:
        return False

    if _PRIVATE_PREFIX_RE.match(trimmed):
        return True
    if is_ticker_symbol(trimmed):
        return True

    upper = trimmed.upper()
    if trimmed in china_listings or upper in {k.upper() for k in china_listings}:
        return True

    if aliases.get(normalize_key(trimmed)):
        return True

    return is_ticker_symbol(canonical_company_label(trimmed, config_path=config_path))


def validate_keyword_company_tags(
    data: dict[str, Any], *, config_path: Path | None = None
) -> list[tuple[str, str]]:
    """Warn when keywords are search themes — valid for search, not company filter chips."""
    warnings: list[tuple[str, str]] = []
    for i, kw in enumerate(data.get("keywords") or []):
        original = str(kw).strip()
        if not original or is_company_keyword(original, config_path=config_path):
            continue
        warnings.append(
            (
                "keywords",
                f'Keyword {i + 1} “{original}” is a search theme, not a company tag '
                f"(use US tickers or Private:Name for companies)",
            )
        )
    return warnings


def validate_keyword_tickers(
    data: dict[str, Any], *, config_path: Path | None = None
) -> list[tuple[str, str]]:
    """Return soft warnings: (section, message) for name-form public company keywords."""
    warnings: list[tuple[str, str]] = []
    for i, kw in enumerate(data.get("keywords") or []):
        original = str(kw).strip()
        ticker = keyword_should_use_ticker(original, config_path=config_path)
        if ticker:
            warnings.append(
                (
                    "keywords",
                    f"Keyword {i + 1} “{original}” should use ticker {ticker} for public companies",
                )
            )
    return warnings


_CHINA_TICKER_RE = re.compile(r"^\d+\.(HK|SZ|SH)$", re.I)


def is_china_listing_symbol(symbol: str, *, config_path: Path | None = None) -> bool:
    """True if symbol is a HK/A-share style ticker (must be in china_listings)."""
    sym = symbol.strip().split()[0].upper()
    cfg = load_company_tickers(config_path)
    listings: dict[str, Any] = cfg.get("china_listings") or {}
    if sym in listings or sym in {k.upper() for k in listings}:
        return True
    return bool(_CHINA_TICKER_RE.match(sym))


def validate_adr_canonical_tickers(
    data: dict[str, Any], *, config_path: Path | None = None
) -> list[tuple[str, str]]:
    """Return errors when HK listing codes are used instead of US ADR tickers."""
    issues: list[tuple[str, str]] = []
    cfg = load_company_tickers(config_path)
    ticker_aliases: dict[str, str] = cfg["ticker_aliases"]

    def check(section: str, label: str, sym: str) -> None:
        raw = sym.strip().split()[0]
        if not raw or raw.lower().startswith("private:") or raw.startswith("Basket:"):
            return
        upper = raw.upper()
        adr = ticker_aliases.get(upper)
        if not adr or adr.upper() == upper:
            return
        if not _CHINA_TICKER_RE.match(upper):
            return
        issues.append(
            (
                section,
                f"{label} “{raw}” should use US ADR ticker {adr} (not HK listing code)",
            )
        )

    for i, kw in enumerate(data.get("keywords") or []):
        check("keywords", f"Keyword {i + 1}", str(kw))

    for i, clue in enumerate(data.get("top_investment_implications") or []):
        check("top_investment_implications", f"Investment idea {i + 1}", str(clue.get("ticker") or ""))

    return issues


def validate_china_listing_tickers(
    data: dict[str, Any], *, config_path: Path | None = None
) -> list[tuple[str, str]]:
    """Return errors for HK/A-share tickers missing from config/company_tickers.yaml china_listings."""
    issues: list[tuple[str, str]] = []
    cfg = load_company_tickers(config_path)
    listings: dict[str, Any] = cfg.get("china_listings") or {}
    listing_keys = {k.upper() for k in listings}
    ticker_aliases: dict[str, str] = cfg["ticker_aliases"]

    for i, kw in enumerate(data.get("keywords") or []):
        sym = str(kw).strip().split()[0]
        adr = ticker_aliases.get(sym.upper())
        if adr and adr.upper() != sym.upper() and _CHINA_TICKER_RE.match(sym.upper()):
            continue  # caught by validate_adr_canonical_tickers
        if is_china_listing_symbol(sym, config_path=config_path) and sym.upper() not in listing_keys:
            issues.append(
                (
                    "keywords",
                    f"Keyword {i + 1} “{sym}” is a China/HK listing — add zh/en names to "
                    f"config/company_tickers.yaml china_listings before publishing",
                )
            )

    for i, clue in enumerate(data.get("top_investment_implications") or []):
        sym = str(clue.get("ticker") or "").strip().split()[0]
        if not sym or sym.lower().startswith("private:"):
            continue
        adr = ticker_aliases.get(sym.upper())
        if adr and adr.upper() != sym.upper() and _CHINA_TICKER_RE.match(sym.upper()):
            continue
        if is_china_listing_symbol(sym, config_path=config_path) and sym.upper() not in listing_keys:
            issues.append(
                (
                    "top_investment_implications",
                    f"Investment idea {i + 1} ticker “{sym}” is a China/HK listing — add to "
                    f"config/company_tickers.yaml china_listings (card pills show company name, not raw ticker)",
                )
            )
    return issues


def format_investment_ticker(ticker: str, *, locale: str = "en", config_path: Path | None = None) -> str:
    """Format tickers for display; China/HK/A-share names show as 公司（TICKER）."""
    raw = str(ticker or "").strip()
    if not raw:
        return raw
    if raw.lower().startswith("private:"):
        label = raw.split(":", 1)[1].strip()
        return label
    if raw.startswith("Basket:"):
        return raw

    symbol = raw.split()[0]
    cfg = load_company_tickers(config_path)
    symbol = _resolve_ticker_alias(symbol, cfg["ticker_aliases"])
    listings: dict[str, Any] = cfg.get("china_listings") or {}
    entry = listings.get(symbol) or listings.get(symbol.upper())
    if isinstance(entry, dict):
        name = entry.get("zh" if locale == "zh" else "en") or entry.get("en") or symbol
        if locale == "zh":
            return f"{name}（{symbol}）"
        return f"{name} ({symbol})"
    return symbol
