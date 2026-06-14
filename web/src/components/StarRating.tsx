interface Props {
  rating: number | null;
  size?: "sm" | "md";
}

export default function StarRating({ rating, size = "md" }: Props) {
  if (rating == null) return null;
  const n = Math.max(1, Math.min(5, Math.round(rating)));
  const stars = "★".repeat(n) + "☆".repeat(5 - n);
  return (
    <span className={`star-rating star-rating--${size}`} title={`${n}/5`}>
      {stars}
    </span>
  );
}
