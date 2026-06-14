import type { Episode } from "../types";

/** Prefer catalog display fields; fall back to legacy guest/title. */
export function episodeHeadline(ep: Episode): string {
  return ep.displayTitle || ep.guest;
}

export function episodeSubtitle(ep: Episode): string {
  return ep.displaySubtitle ?? ep.title;
}
