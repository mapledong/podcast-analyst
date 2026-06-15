export type SignalDirection = "Long" | "Short" | "Watch";

export interface InvestmentIdea {
  ticker: string;
  direction: SignalDirection;
  confidence: "High" | "Medium" | "Low";
  thesis: string;
}

export interface Podcast {
  id: string;
  name: string;
  host: string;
  description: string;
  cover_url: string;
  accent_color: string;
  youtube_url: string;
  episodeCount: number;
}

export interface Episode {
  id: string;
  podcastId: string;
  episodeNumber: number;
  title: string;
  guest: string;
  displayTitle?: string;
  displaySubtitle?: string;
  guestRole: string;
  date: string;
  durationMinutes: number;
  readMinutes: number;
  rating: number | null;
  conclusion: string;
  youtubeUrl: string;
  summaryFile: string;
  summaryFileZh?: string;
  availableLocales?: Array<"en" | "zh">;
  defaultLocale?: "en" | "zh";
  keywords: string[];
  investmentIdeas: InvestmentIdea[];
  chronologySubject?: string;
}

export interface Catalog {
  generatedAt: string;
  podcasts: Podcast[];
  episodes: Episode[];
}
