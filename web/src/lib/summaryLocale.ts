import type { SummaryLocale } from "./catalog";

/** Locale for company-name display on cards (default EN; use ?lang=zh for Chinese names). */
export function summaryDisplayLocale(searchParams: URLSearchParams): SummaryLocale {
  return searchParams.get("lang") === "zh" ? "zh" : "en";
}
