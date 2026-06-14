import type { CSSProperties } from "react";
import { useMemo, useState } from "react";
import { Link } from "react-router-dom";
import DiscoveryFilters from "../components/DiscoveryFilters";
import InvestmentIdeasPreview from "../components/InvestmentIdeasPreview";
import PodcastCard from "../components/PodcastCard";
import StarRating from "../components/StarRating";
import { compareEpisodes, data, formatDate, getPodcast } from "../lib/catalog";
import { episodeHeadline, episodeSubtitle } from "../lib/displayTitles";
import { applyEpisodeFilters, hasActiveFilters } from "../lib/filters";
import { assetUrl } from "../lib/assets";

export default function HomePage() {
  const totalSummaries = data.episodes.length;
  const [query, setQuery] = useState("");
  const [rating, setRating] = useState<number | null>(null);
  const [company, setCompany] = useState<string | null>(null);

  const filters = useMemo(
    () => ({ query, rating, company }),
    [query, rating, company],
  );

  const filtering = hasActiveFilters(filters);

  const results = useMemo(
    () => applyEpisodeFilters(data.episodes, filters).sort(compareEpisodes),
    [filters],
  );

  const clearFilters = () => {
    setQuery("");
    setRating(null);
    setCompany(null);
  };

  return (
    <div className="page home-page">
      <section className="hero">
        <p className="eyebrow">Summary Library</p>
        <h1>Great podcasts, distilled for investors</h1>
        <p className="hero-lede">
          Browse PM-ready summaries — key facts, mental models, and top investment ideas — from the
          shows you already listen to.{" "}
          {totalSummaries > 0 && `${totalSummaries} episodes live.`}
        </p>
      </section>

      <section className="global-search">
        <input
          type="search"
          placeholder="Search guest, ticker, company, topic…"
          value={query}
          onChange={(e) => setQuery(e.target.value)}
          className="search-input search-input--wide"
        />
        <DiscoveryFilters
          rating={rating}
          company={company}
          onRatingChange={setRating}
          onCompanyChange={setCompany}
        />
      </section>

      {filtering ? (
        <section className="search-results">
          <h2 className="section-title">
            {results.length} result{results.length !== 1 ? "s" : ""}
          </h2>
          {results.length === 0 ? (
            <p className="empty-filter">No episodes match your filters.</p>
          ) : (
            <div className="search-result-list">
              {results.map((ep) => {
                const podcast = getPodcast(ep.podcastId);
                if (!podcast) return null;
                return (
                  <Link
                    key={ep.id}
                    to={`/podcast/${podcast.id}/${ep.id}`}
                    className="search-result-row"
                    style={{ "--accent": podcast.accent_color } as CSSProperties}
                  >
                    <img src={assetUrl(podcast.cover_url)} alt="" className="search-result-cover" />
                    <div className="search-result-body">
                      <div className="search-result-top">
                        <span className="episode-num">
                          {podcast.name} · EP.{ep.episodeNumber}
                        </span>
                        <StarRating rating={ep.rating} size="sm" />
                      </div>
                      <h3>{episodeHeadline(ep)}</h3>
                      {episodeSubtitle(ep) && (
                        <p className="episode-title">{episodeSubtitle(ep)}</p>
                      )}
                      {ep.conclusion && <p className="episode-hook">{ep.conclusion}</p>}
                      <InvestmentIdeasPreview ideas={ep.investmentIdeas} variant="minimal" />
                      <div className="episode-card-meta">
                        <span>{formatDate(ep.date)}</span>
                        <span>≈{ep.readMinutes} min read</span>
                      </div>
                    </div>
                  </Link>
                );
              })}
            </div>
          )}
          <p className="search-hint">
            <button type="button" className="text-button" onClick={clearFilters}>
              Clear filters
            </button>
            {" · "}
            or browse shows below
          </p>
        </section>
      ) : null}

      <section className="podcast-grid">
        {data.podcasts.map((podcast) => (
          <PodcastCard key={podcast.id} podcast={podcast} />
        ))}
      </section>
    </div>
  );
}
