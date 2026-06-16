import {
  CHINA_LISTINGS,
  COMPANY_ALIASES,
  TICKER_ALIASES,
  type ChinaListingNames,
} from "./company_tickers.generated";
import type { SummaryLocale } from "./catalog";

function normalizeKey(value: string): string {
  return value.trim().toLowerCase();
}

const SIMPLE_TICKER_RE = /^[A-Z]{1,5}$/;
const DOTTED_TICKER_RE = /^[A-Z0-9]{1,5}\.[A-Z0-9]{1,4}$/;

export function isTickerSymbol(value: string): boolean {
  const raw = value.trim();
  return SIMPLE_TICKER_RE.test(raw) || DOTTED_TICKER_RE.test(raw);
}

function resolveTickerAlias(ticker: string): string {
  let upper = ticker.trim().toUpperCase();
  const seen = new Set<string>();
  while (TICKER_ALIASES[upper] && !seen.has(upper)) {
    seen.add(upper);
    upper = TICKER_ALIASES[upper];
  }
  return upper;
}

export function isCompanyKeyword(value: string): boolean {
  const trimmed = value.trim();
  if (!trimmed) return false;

  if (/^private:/i.test(trimmed)) return true;
  if (isTickerSymbol(trimmed)) return true;

  const upper = trimmed.toUpperCase();
  if (CHINA_LISTINGS[trimmed] ?? CHINA_LISTINGS[upper]) return true;

  const key = normalizeKey(trimmed);
  if (COMPANY_ALIASES[key]) return true;

  return isTickerSymbol(canonicalCompanyLabel(trimmed));
}

export function canonicalCompanyLabel(value: string): string {
  const trimmed = value.trim();
  if (!trimmed) return trimmed;

  const privatePrefix = trimmed.match(/^private:(.+)$/i);
  if (privatePrefix) {
    return canonicalCompanyLabel(privatePrefix[1]);
  }

  if (isTickerSymbol(trimmed)) {
    return resolveTickerAlias(trimmed);
  }

  const alias = COMPANY_ALIASES[normalizeKey(trimmed)];
  if (alias) return resolveTickerAlias(alias);

  return trimmed;
}

export function canonicalCompanyKey(value: string): string {
  return normalizeKey(canonicalCompanyLabel(value));
}

export function companyFilterMatches(extractedValue: string, filterValue: string): boolean {
  return canonicalCompanyKey(extractedValue) === canonicalCompanyKey(filterValue);
}

function chinaListingEntry(symbol: string): ChinaListingNames | undefined {
  return CHINA_LISTINGS[symbol] ?? CHINA_LISTINGS[symbol.toUpperCase()];
}

/** Format investment tickers for display; mirrors src/company_tickers.format_investment_ticker. */
export function formatInvestmentTicker(
  ticker: string,
  locale: SummaryLocale = "en",
  options?: { compact?: boolean },
): string {
  const raw = String(ticker ?? "").trim();
  if (!raw) return raw;

  const privatePrefix = raw.match(/^private:(.+)$/i);
  if (privatePrefix) return privatePrefix[1].trim();
  if (raw.startsWith("Basket:")) return raw;

  const symbol = resolveTickerAlias(raw.split(/\s+/)[0]);
  const entry = chinaListingEntry(symbol);
  if (!entry) return symbol;

  const name = (locale === "zh" ? entry.zh : entry.en) || entry.en || symbol;
  if (options?.compact) return name;

  if (locale === "zh") return `${name}（${symbol}）`;
  return `${name} (${symbol})`;
}
