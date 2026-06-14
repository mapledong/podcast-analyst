import type { Episode } from "../types";
import { episodeMatchesCompany, episodeMatchesRating } from "./discovery";
import { filterEpisodes } from "./search";

export interface EpisodeFilters {
  query: string;
  rating: number | null;
  company: string | null;
}

export function hasActiveFilters(filters: EpisodeFilters): boolean {
  return (
    filters.query.trim().length > 0 ||
    filters.rating != null ||
    filters.company != null
  );
}

export function applyEpisodeFilters(episodes: Episode[], filters: EpisodeFilters): Episode[] {
  let result = episodes;

  if (filters.query.trim()) {
    result = filterEpisodes(filters.query, result);
  }
  if (filters.rating != null) {
    result = result.filter((ep) => episodeMatchesRating(ep, filters.rating!));
  }
  if (filters.company) {
    result = result.filter((ep) => episodeMatchesCompany(ep, filters.company!));
  }

  return result;
}
