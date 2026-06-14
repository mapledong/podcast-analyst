import type { Episode } from "../types";
import { getPodcast } from "./catalog";

export function episodeSearchBlob(ep: Episode): string {
  const podcast = getPodcast(ep.podcastId);
  const ideaText = ep.investmentIdeas
    .map((i) => `${i.ticker} ${i.thesis}`)
    .join(" ");
  return [
    podcast?.name,
    ep.guest,
    ep.title,
    ep.displayTitle,
    ep.displaySubtitle,
    ep.conclusion,
    ep.guestRole,
    ideaText,
    ...ep.keywords,
    String(ep.episodeNumber),
  ]
    .filter(Boolean)
    .join(" ")
    .toLowerCase();
}

export function filterEpisodes(query: string, episodes: Episode[]): Episode[] {
  const q = query.trim().toLowerCase();
  if (!q) return episodes;
  return episodes.filter((ep) => episodeSearchBlob(ep).includes(q));
}
