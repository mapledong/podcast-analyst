import type { SummaryLocale } from "../lib/catalog";
import { formatInvestmentTicker } from "../lib/tickers";
import type { InvestmentIdea } from "../types";
import DirectionBadge from "./DirectionBadge";

interface Props {
  ideas: InvestmentIdea[];
  variant?: "minimal" | "full";
  locale?: SummaryLocale;
}

export default function InvestmentIdeasPreview({
  ideas,
  variant = "full",
  locale = "en",
}: Props) {
  if (!ideas.length) return null;

  if (variant === "minimal") {
    return (
      <ul className="idea-preview idea-preview--minimal">
        {ideas.map((idea) => (
          <li key={`${idea.ticker}-${idea.direction}`} className="idea-chip">
            <span className="idea-ticker">
              {formatInvestmentTicker(idea.ticker, locale, { compact: true })}
            </span>
            <DirectionBadge direction={idea.direction} size="sm" />
          </li>
        ))}
      </ul>
    );
  }

  return (
    <ul className="idea-preview">
      {ideas.map((idea) => (
        <li key={`${idea.ticker}-${idea.direction}`} className="idea-preview-row">
          <div className="idea-preview-head">
            <span className="idea-ticker">
              {formatInvestmentTicker(idea.ticker, locale)}
            </span>
            <DirectionBadge direction={idea.direction} size="sm" />
          </div>
          <p className="idea-thesis">{idea.thesis}</p>
        </li>
      ))}
    </ul>
  );
}
