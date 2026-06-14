import catalog from "../data/catalog.json";
import type { Catalog, Episode } from "../types";

export const data = catalog as Catalog;

/** Newest first. Acquired & Business Breakdowns use date; others use episode number. */
export function compareEpisodes(a: Episode, b: Episode): number {
  const dateSort = new Set(["acquired", "business-breakdowns"]);
  if (dateSort.has(a.podcastId) && dateSort.has(b.podcastId)) {
    return b.date.localeCompare(a.date);
  }
  if (dateSort.has(a.podcastId)) {
    return b.date.localeCompare(a.date);
  }
  if (dateSort.has(b.podcastId)) {
    return b.date.localeCompare(a.date);
  }
  return b.episodeNumber - a.episodeNumber;
}

export function getPodcast(id: string) {
  return data.podcasts.find((p) => p.id === id);
}

export function getEpisodesForPodcast(podcastId: string) {
  return data.episodes.filter((e) => e.podcastId === podcastId).sort(compareEpisodes);
}

export function getEpisode(podcastId: string, episodeId: string) {
  return data.episodes.find((e) => e.podcastId === podcastId && e.id === episodeId);
}

const summaryModules = import.meta.glob<string>("../data/summaries/*.md", {
  query: "?raw",
  import: "default",
  eager: true,
});

export function loadSummaryMarkdown(summaryFile: string): Promise<string> {
  const key = `../data/summaries/${summaryFile}`;
  const content = summaryModules[key];
  if (!content) return Promise.reject(new Error(`Summary not found: ${summaryFile}`));
  return Promise.resolve(content);
}

export function formatDate(iso: string) {
  return new Date(iso + "T12:00:00").toLocaleDateString("en-US", {
    month: "short",
    day: "numeric",
    year: "numeric",
  });
}
