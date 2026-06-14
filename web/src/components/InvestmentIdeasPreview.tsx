import type { InvestmentIdea } from "../types";
import DirectionBadge from "./DirectionBadge";

function formatTicker(ticker: string) {
  return ticker.replace(/^Private:/i, "").trim();
}

interface Props {
  ideas: InvestmentIdea[];
  variant?: "minimal" | "full";
}

export default function InvestmentIdeasPreview({ ideas, variant = "full" }: Props) {
  if (!ideas.length) return null;

  if (variant === "minimal") {
    return (
      <ul className="idea-preview idea-preview--minimal">
        {ideas.map((idea) => (
          <li key={`${idea.ticker}-${idea.direction}`} className="idea-chip">
            <span className="idea-ticker">{formatTicker(idea.ticker)}</span>
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
            <span className="idea-ticker">{formatTicker(idea.ticker)}</span>
            <DirectionBadge direction={idea.direction} size="sm" />
          </div>
          <p className="idea-thesis">{idea.thesis}</p>
        </li>
      ))}
    </ul>
  );
}
