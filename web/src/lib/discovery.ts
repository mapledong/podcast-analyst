import type { Episode } from "../types";
import { canonicalCompanyKey, canonicalCompanyLabel, companyFilterMatches } from "./tickers";

const BLOCKED_COMPANY_KEYS = new Set(["private", "n/a", "na", "tbd", "unknown", "various"]);

function extractFromTicker(ticker: string): string[] {
  const raw = ticker.trim();
  if (!raw) return [];

  const privatePrefix = raw.match(/^private:(.+)$/i);
  if (privatePrefix) {
    return [canonicalCompanyLabel(privatePrefix[1])];
  }

  if (raw.startsWith("Basket:")) {
    const rest = raw.slice("Basket:".length);
    const parenMatch = rest.match(/\(([^)]+)\)/);
    if (parenMatch) {
      return parenMatch[1]
        .split(/[/,]/)
        .map((part) => canonicalCompanyLabel(part))
        .filter(Boolean);
    }
    return [canonicalCompanyLabel(rest.split("(")[0])];
  }

  return [canonicalCompanyLabel(raw)];
}

export function extractEpisodeCompanies(ep: Episode): string[] {
  const seen = new Set<string>();
  const companies: string[] = [];

  const add = (value: string) => {
    const label = canonicalCompanyLabel(value);
    const key = canonicalCompanyKey(label);
    if (!key || BLOCKED_COMPANY_KEYS.has(key) || seen.has(key)) return;
    seen.add(key);
    companies.push(label);
  };

  for (const keyword of ep.keywords) add(keyword);
  if (ep.guest) add(ep.guest);
  for (const idea of ep.investmentIdeas) {
    for (const name of extractFromTicker(idea.ticker)) add(name);
  }
  if (ep.chronologySubject) {
    for (const part of ep.chronologySubject.split("·")) add(part);
  }

  return companies;
}

export interface RankedTerm {
  label: string;
  count: number;
}

function rankTerms(counts: Map<string, { label: string; count: number }>, limit: number): RankedTerm[] {
  return [...counts.values()]
    .sort((a, b) => b.count - a.count || a.label.localeCompare(b.label))
    .slice(0, limit);
}

export function computeTopCompanies(episodes: Episode[], limit = 20): RankedTerm[] {
  const counts = new Map<string, { label: string; count: number }>();

  for (const ep of episodes) {
    const seen = new Set<string>();
    for (const company of extractEpisodeCompanies(ep)) {
      const key = canonicalCompanyKey(company);
      if (!key || seen.has(key)) continue;
      seen.add(key);
      const existing = counts.get(key);
      if (existing) existing.count += 1;
      else counts.set(key, { label: company, count: 1 });
    }
  }

  return rankTerms(counts, limit);
}

export function episodeMatchesCompany(ep: Episode, company: string): boolean {
  return extractEpisodeCompanies(ep).some((name) => companyFilterMatches(name, company));
}

export function episodeMatchesRating(ep: Episode, rating: number): boolean {
  if (ep.rating == null) return false;
  return Math.round(ep.rating) === rating;
}
