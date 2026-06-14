interface Props {
  keywords: string[];
  size?: "sm" | "md";
}

export default function KeywordTags({ keywords, size = "sm" }: Props) {
  if (!keywords.length) return null;
  return (
    <div className={`keyword-row keyword-row--${size}`}>
      {keywords.map((kw) => (
        <span key={kw} className="keyword-tag">
          {kw}
        </span>
      ))}
    </div>
  );
}
