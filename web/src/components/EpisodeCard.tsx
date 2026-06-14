import type { CSSProperties } from "react";
import { Link } from "react-router-dom";
import type { Episode, Podcast } from "../types";
import { formatDate } from "../lib/catalog";
import { episodeHeadline, episodeSubtitle } from "../lib/displayTitles";
import InvestmentIdeasPreview from "./InvestmentIdeasPreview";
import StarRating from "./StarRating";

interface Props {
  episode: Episode;
  podcast: Podcast;
}

export default function EpisodeCard({ episode, podcast }: Props) {
  return (
    <Link
      to={`/podcast/${podcast.id}/${episode.id}`}
      className="episode-card"
      style={{ "--accent": podcast.accent_color } as CSSProperties}
    >
      <div className="episode-card-top">
        <span className="episode-num">EP.{episode.episodeNumber}</span>
        <StarRating rating={episode.rating} size="sm" />
      </div>
      <h3>{episodeHeadline(episode)}</h3>
      {episodeSubtitle(episode) && (
        <p className="episode-title">{episodeSubtitle(episode)}</p>
      )}
      {episode.conclusion && <p className="episode-hook">{episode.conclusion}</p>}
      <InvestmentIdeasPreview ideas={episode.investmentIdeas} variant="minimal" />
      <div className="episode-card-meta">
        <span>{formatDate(episode.date)}</span>
        <span>{episode.durationMinutes} min</span>
        <span>≈{episode.readMinutes} min read</span>
      </div>
    </Link>
  );
}
