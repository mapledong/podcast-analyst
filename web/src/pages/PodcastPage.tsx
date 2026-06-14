import type { CSSProperties } from "react";
import { useMemo, useState } from "react";
import { useParams } from "react-router-dom";
import Breadcrumbs from "../components/Breadcrumbs";
import EpisodeCard from "../components/EpisodeCard";
import { compareEpisodes, data, getEpisodesForPodcast, getPodcast } from "../lib/catalog";
import { filterEpisodes } from "../lib/search";

export default function PodcastPage() {
  const { podcastId = "" } = useParams();
  const podcast = getPodcast(podcastId);
  const [query, setQuery] = useState("");

  const episodes = useMemo(() => getEpisodesForPodcast(podcastId), [podcastId]);

  const filtered = useMemo(() => {
    const scoped = filterEpisodes(query, episodes);
    return scoped.sort(compareEpisodes);
  }, [episodes, query]);

  if (!podcast) {
    return (
      <div className="page empty-state">
        <h1>Podcast not found</h1>
        <p>
          <a href="/">Back to library</a>
        </p>
      </div>
    );
  }

  const hasEpisodes = episodes.length > 0;

  return (
    <div
      className="page podcast-page"
      style={{ "--accent": podcast.accent_color } as CSSProperties}
    >
      <Breadcrumbs items={[{ label: "Library", to: "/" }, { label: podcast.name }]} />

      <header className="podcast-header">
        <img
          src={podcast.cover_url}
          alt=""
          className="podcast-header-cover"
          onError={(e) => {
            e.currentTarget.style.visibility = "hidden";
          }}
        />
        <div>
          <h1>{podcast.name}</h1>
          <p className="podcast-header-host">Hosted by {podcast.host}</p>
          <p className="podcast-header-desc">{podcast.description}</p>
          {podcast.youtube_url && (
            <a href={podcast.youtube_url} target="_blank" rel="noreferrer" className="text-link">
              Watch on YouTube →
            </a>
          )}
        </div>
      </header>

      {hasEpisodes ? (
        <>
          <div className="list-toolbar">
            <h2>{episodes.length} summaries</h2>
            <input
              type="search"
              placeholder="Search guest, ticker, topic…"
              value={query}
              onChange={(e) => setQuery(e.target.value)}
              className="search-input"
            />
          </div>
          <div className="episode-grid">
            {filtered.map((ep) => (
              <EpisodeCard key={ep.id} episode={ep} podcast={podcast} />
            ))}
            {filtered.length === 0 && (
              <p className="empty-filter">No episodes match your search.</p>
            )}
          </div>
        </>
      ) : (
        <div className="coming-soon-panel">
          <div className="coming-soon-icon" aria-hidden>
            ◌
          </div>
          <h2>Summaries coming soon</h2>
          <p>
            We&apos;re building summaries for <strong>{podcast.name}</strong>. Check back — or run
            the pipeline when new episodes are added.
          </p>
          <p className="muted">
            {data.episodes.length > 0
              ? `Meanwhile, browse ${data.podcasts.find((p) => p.episodeCount > 0)?.name ?? "another show"}.`
              : null}
          </p>
        </div>
      )}
    </div>
  );
}
