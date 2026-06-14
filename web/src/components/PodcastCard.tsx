import type { CSSProperties } from "react";
import { useState } from "react";
import { Link } from "react-router-dom";
import { assetUrl } from "../lib/assets";
import type { Podcast } from "../types";

interface Props {
  podcast: Podcast;
}

export default function PodcastCard({ podcast }: Props) {
  const hasEpisodes = podcast.episodeCount > 0;
  const [coverFailed, setCoverFailed] = useState(false);

  return (
    <Link
      to={`/podcast/${podcast.id}`}
      className="podcast-card"
      style={{ "--accent": podcast.accent_color } as CSSProperties}
    >
      <div className="podcast-card-cover">
        <img
          src={assetUrl(podcast.cover_url)}
          alt={`${podcast.name} cover art`}
          loading="lazy"
          className="podcast-cover-img"
          onError={() => setCoverFailed(true)}
        />
        <div className={`cover-fallback${coverFailed ? " visible" : ""}`} aria-hidden>
          {podcast.name
            .split(" ")
            .slice(0, 2)
            .map((w) => w[0])
            .join("")}
        </div>
      </div>
      <div className="podcast-card-body">
        <h2>{podcast.name}</h2>
        <p className="podcast-host">{podcast.host}</p>
        <p className="podcast-desc">{podcast.description}</p>
        <div className="podcast-card-meta">
          {hasEpisodes ? (
            <span className="badge badge-live">{podcast.episodeCount} summaries</span>
          ) : (
            <span className="badge badge-soon">Coming soon</span>
          )}
        </div>
      </div>
    </Link>
  );
}
