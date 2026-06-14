import { useMemo } from "react";
import { data } from "../lib/catalog";
import { computeTopCompanies } from "../lib/discovery";

interface Props {
  rating: number | null;
  company: string | null;
  onRatingChange: (rating: number | null) => void;
  onCompanyChange: (company: string | null) => void;
}

function toggleChip<T>(current: T | null, value: T, onChange: (next: T | null) => void) {
  onChange(current === value ? null : value);
}

export default function DiscoveryFilters({
  rating,
  company,
  onRatingChange,
  onCompanyChange,
}: Props) {
  const topCompanies = useMemo(() => computeTopCompanies(data.episodes, 20), []);

  return (
    <section className="discovery-filters" aria-label="Discovery filters">
      <div className="discovery-section">
        <h3 className="discovery-label">Star rating</h3>
        <div className="filter-chips filter-chips--inline">
          {[5, 4, 3, 2, 1].map((stars) => (
            <button
              key={stars}
              type="button"
              className={`chip chip--rating${rating === stars ? " chip--active" : ""}`}
              onClick={() => toggleChip(rating, stars, onRatingChange)}
              title={`${stars}-star episodes`}
            >
              {"★".repeat(stars)}
            </button>
          ))}
        </div>
      </div>

      {topCompanies.length > 0 && (
        <div className="discovery-section">
          <h3 className="discovery-label">Companies</h3>
          <div className="filter-chips filter-chips--inline">
            {topCompanies.map((term) => (
              <button
                key={term.label}
                type="button"
                className={`chip${company === term.label ? " chip--active" : ""}`}
                onClick={() => toggleChip(company, term.label, onCompanyChange)}
              >
                {term.label}
                <span className="chip-count">{term.count}</span>
              </button>
            ))}
          </div>
        </div>
      )}
    </section>
  );
}
