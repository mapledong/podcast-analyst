import type { SignalDirection } from "../types";

const LABELS: Record<SignalDirection, string> = {
  Long: "LONG",
  Short: "SHORT",
  Watch: "WATCH",
};

interface Props {
  direction: SignalDirection;
  size?: "sm" | "md";
}

export default function DirectionBadge({ direction, size = "sm" }: Props) {
  return (
    <span className={`dir-badge dir-badge--${direction.toLowerCase()} dir-badge--${size}`}>
      {LABELS[direction]}
    </span>
  );
}
