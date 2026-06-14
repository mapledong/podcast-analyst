import { COMPANY_ALIASES, TICKER_ALIASES } from "./company_tickers.generated";

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
