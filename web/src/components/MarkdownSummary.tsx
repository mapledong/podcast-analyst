import type { Components } from "react-markdown";
import type { ReactNode } from "react";
import ReactMarkdown from "react-markdown";
import remarkGfm from "remark-gfm";

interface Props {
  content: string;
  variant?: "default" | "episode";
}

/** Drop duplicate page-header lines (title, rating, date) but keep Host through Disclaimer. */
function stripEpisodeHeader(markdown: string): string {
  const hostIdx = markdown.search(/^\*\*Host\*\*/m);
  if (hostIdx >= 0) return markdown.slice(hostIdx);
  return markdown;
}

function cleanSummaryMarkdown(content: string, variant: Props["variant"]): string {
  let md = content
    .replace(/\n---\n\n<p align="center"><sub>podcast-analyst[^<]*<\/sub><\/p>\s*$/i, "\n")
    .trimEnd();
  if (variant === "episode") md = stripEpisodeHeader(md);
  return md;
}

function nodeText(children: ReactNode): string {
  if (typeof children === "string") return children;
  if (Array.isArray(children)) return children.map(String).join("");
  return String(children ?? "");
}

function metaClass(text: string): string | undefined {
  if (text.startsWith("Host")) return "summary-meta";
  if (text.startsWith("Guest")) return "summary-meta";
  if (text.startsWith("Listen")) return "summary-meta";
  if (text.startsWith("Topics")) return "summary-meta summary-topics";
  return undefined;
}

const components: Components = {
  h2: ({ children, ...props }) => {
    const text = nodeText(children);
    const className =
      text === "Chronology"
        ? "section-chronology"
        : text === "Background"
          ? "section-background"
          : text === "Investment Ideas"
          ? "section-investment-ideas"
          : text === "Key Insights"
            ? "section-key-insights"
            : text === "Golden Quotes"
              ? "section-golden-quotes"
              : undefined;
    return (
      <h2 className={className} {...props}>
        {children}
      </h2>
    );
  },
  p: ({ children, ...props }) => {
    const text = nodeText(children);
    const className = metaClass(text);
    return (
      <p className={className} {...props}>
        {children}
      </p>
    );
  },
};

export default function MarkdownSummary({ content, variant = "default" }: Props) {
  return (
    <article className="summary-prose">
      <ReactMarkdown remarkPlugins={[remarkGfm]} components={components}>
        {cleanSummaryMarkdown(content, variant)}
      </ReactMarkdown>
    </article>
  );
}
