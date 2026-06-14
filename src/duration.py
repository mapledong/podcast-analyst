"""Duration tiers for summary length targets (episode length → read time)."""

from __future__ import annotations

from typing import Any

TIER_KEYS = ("under_60_min", "under_90_min", "90_to_180_min", "over_180_min")

# Legacy template keys (pre-90/180 breakpoints)
_LEGACY_TIER_MAP = {
    "under_90_min": "under_60_min",
    "90_to_180_min": "60_to_120_min",
    "over_180_min": "over_120_min",
}


def duration_tier(duration_minutes: int | float | None) -> str:
    """Map episode duration to template tier key."""
    d = int(duration_minutes or 60)
    if d < 60:
        return "under_60_min"
    if d < 90:
        return "under_90_min"
    if d < 180:
        return "90_to_180_min"
    return "over_180_min"


def tier_limit(template: dict[str, Any], key: str, duration_minutes: int | float | None) -> int:
    """Read a per-tier limit from template config with legacy fallback."""
    tier = duration_tier(duration_minutes)
    limits = template.get(key) or {}
    if tier in limits:
        return int(limits[tier])
    legacy = _LEGACY_TIER_MAP.get(tier)
    if legacy and legacy in limits:
        return int(limits[legacy])
    if int(duration_minutes or 60) < 90:
        return int(limits.get("under_60_min", 0))
    return int(limits.get("over_60_min", 0))


def target_read_minutes(template: dict[str, Any], duration_minutes: int | float | None) -> int:
    """Expected read time for an episode at 200 wpm."""
    return tier_limit(template, "target_read_minutes", duration_minutes) or 5
