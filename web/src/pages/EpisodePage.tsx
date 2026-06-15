import type { CSSProperties } from "react";
import { useEffect, useMemo, useState } from "react";
import { Link, useParams, useSearchParams } from "react-router-dom";
import Breadcrumbs from "../components/Breadcrumbs";
import MarkdownSummary from "../components/MarkdownSummary";
import StarRating from "../components/StarRating";
import {
  formatDate,
  getEpisode,
  getPodcast,
  loadSummaryMarkdown,
  type SummaryLocale,
} from "../lib/catalog";
import { episodeHeadline, episodeSubtitle } from "../lib/displayTitles";

export default function EpisodePage() {
  const { podcastId = "", episodeId = "" } = useParams();
  const [searchParams, setSearchParams] = useSearchParams();
  const podcast = getPodcast(podcastId);
  const episode = getEpisode(podcastId, episodeId);
  const [markdown, setMarkdown] = useState<string | null>(null);
  const [error, setError] = useState<string | null>(null);

  const locales = episode?.availableLocales ?? ["en"];
  const defaultLocale: SummaryLocale = "en";
  const requested = searchParams.get("lang") as SummaryLocale | null;
  const locale: SummaryLocale =
    requested && locales.includes(requested) ? requested : defaultLocale;

  const summaryFile = useMemo(() => {
    if (!episode) return "";
    return locale === "zh" && episode.summaryFileZh ? episode.summaryFileZh : episode.summaryFile;
  }, [episode, locale]);

  useEffect(() => {
    if (!episode || !summaryFile) return;
    setMarkdown(null);
    setError(null);
    loadSummaryMarkdown(summaryFile, locale)
      .then(setMarkdown)
      .catch(() => setError("Could not load summary."));
  }, [episode, summaryFile, locale]);

  function setLocale(next: SummaryLocale) {
    const params = new URLSearchParams(searchParams);
    if (next === defaultLocale) params.delete("lang");
    else params.set("lang", next);
    setSearchParams(params, { replace: true });
  }

  if (!podcast || !episode) {
    return (
      <div className="page empty-state">
        <h1>Episode not found</h1>
        <p>
          <Link to="/">Back to library</Link>
        </p>
      </div>
    );
  }

  return (
    <div
      className="page episode-page"
      style={{ "--accent": podcast.accent_color } as CSSProperties}
    >
      <Breadcrumbs
        items={[
          { label: "Library", to: "/" },
          { label: podcast.name, to: `/podcast/${podcast.id}` },
          { label: `EP.${episode.episodeNumber}` },
        ]}
      />

      <header className="episode-header">
        <div className="episode-header-meta">
          <span className="episode-num">EP.{episode.episodeNumber}</span>
          {episode.rating != null && (
            <span className="episode-rating-wrap">
              <StarRating rating={episode.rating} />
              <span className="rating-label">{episode.rating}/5</span>
            </span>
          )}
          {locales.length > 1 && (
            <span className="locale-toggle" role="group" aria-label="Summary language">
              {locales.includes("en") && (
                <button
                  type="button"
                  className={locale === "en" ? "locale-btn active" : "locale-btn"}
                  onClick={() => setLocale("en")}
                >
                  EN
                </button>
              )}
              {locales.includes("zh") && (
                <button
                  type="button"
                  className={locale === "zh" ? "locale-btn active" : "locale-btn"}
                  onClick={() => setLocale("zh")}
                >
                  中文
                </button>
              )}
            </span>
          )}
        </div>
        <h1>{episodeHeadline(episode)}</h1>
        {episodeSubtitle(episode) && (
          <p className="episode-subtitle">{episodeSubtitle(episode)}</p>
        )}
        <div className="episode-header-stats">
          <span>{formatDate(episode.date)}</span>
          <span>{episode.durationMinutes} min episode</span>
          <span>≈{episode.readMinutes} min read</span>
          {episode.youtubeUrl && (
            <a href={episode.youtubeUrl} target="_blank" rel="noreferrer" className="text-link">
              Watch on YouTube →
            </a>
          )}
        </div>
      </header>

      <div className="summary-panel">
        {error && <p className="error-msg">{error}</p>}
        {!markdown && !error && <p className="loading-msg">Loading summary…</p>}
        {markdown && <MarkdownSummary content={markdown} variant="episode" />}
      </div>
    </div>
  );
}
