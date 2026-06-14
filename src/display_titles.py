"""Resolve non-redundant display titles for podcast episodes."""

from __future__ import annotations

import re
from typing import Any

COMPANY_FIRST_PODCASTS = frozenset({"Acquired", "Business Breakdowns", "acquired", "business-breakdowns"})
ACQUIRED_PODCASTS = frozenset({"Acquired", "acquired"})

CEO_PATTERN = re.compile(r"^(.+?)\s+CEO\s+(.+)$", re.I)
WITH_PATTERN = re.compile(r"^(.+?)\s+with\s+(.+)$", re.I)
WITH_PAREN_PATTERN = re.compile(r"^(.+?)\s*\([^)]*?\bwith\s+(.+?)\)$", re.I)
INTERVIEW_PATTERN = re.compile(r"^The\s+(.+?)\s+Interview$", re.I)
COLON_PATTERN = re.compile(r"^([^:]+):\s*(.+)$")
PART_PATTERN = re.compile(r"^(.+?)\s+Part\s+([IVX\d]+)\s*:?\s*(.*)$", re.I)
VOLUME_PATTERN = re.compile(r"^(.+?)\s+Volume\s+([IVX\d]+)\s*$", re.I)
GUEST_PREFIX_PATTERN = re.compile(r"^(.+?)\s*[:—–-]\s*(.+)$")
SEASON_EPISODE_PREFIX = re.compile(
    r"^(?:Acquired\s+)?Season\s+(\d+),?\s+Episode\s+(\d+):\s*(.+)$",
    re.I,
)
EPISODE_NUMBER_COLON = re.compile(r"^Episode\s+(\d+):\s*(.+)$", re.I)
EPISODE_NUMBER_SPACE = re.compile(r"^Episode\s+(\d+)\s+(.+)$", re.I)
EDITORIAL_COLON_PREFIX = re.compile(
    r"^(Interview|Special|Sessions|Short|ACQ Sessions):\s*(.+)$",
    re.I,
)
PERSON_ON_THEME = re.compile(r"^(.+?)\s+on\s+(.+)$", re.I)
GENERIC_HEADLINE = re.compile(
    r"^(Interview|Special|Sessions|Short|Episode\s+\d+|Season\s+\d+(?:,\s*Episode\s+\d+)?|"
    r"Acquired(?:\s+Season\s+\d+\s+Episode\s+\d+)?)$",
    re.I,
)

EDITORIAL_WORDS = re.compile(
    r"\b(who|that|from|lessons|saved|story|interview|special|sessions|playbook|dynamism|capital)\b",
    re.I,
)


def _norm(text: str) -> str:
    return re.sub(r"\s+", " ", str(text or "").strip())


def _norm_key(text: str) -> str:
    return _norm(text).lower()


def titles_redundant(title: str, guest: str) -> bool:
    t, g = _norm_key(title), _norm_key(guest)
    if not t or not g:
        return False
    if t == g:
        return True
    if len(g) > 3 and g in t:
        return True
    if len(t) > 3 and t in g:
        return True
    return False


def _format_subtitle(*parts: str) -> str:
    seen: set[str] = set()
    out: list[str] = []
    for raw in parts:
        p = _norm(raw)
        if not p:
            continue
        key = _norm_key(p)
        if key in seen:
            continue
        seen.add(key)
        out.append(p)
    return " · ".join(out)


def _is_entity_label(text: str) -> bool:
    """Short company / institution / sport name — not a narrative sentence."""
    t = _norm(text)
    if not t or len(t) > 55:
        return False
    if len(t.split()) > 7:
        return False
    if EDITORIAL_WORDS.search(t):
        return False
    if t.endswith(")") or "(" in t:
        return False
    return True


def _is_editorial_title(text: str, subject: str = "") -> bool:
    """Acquired's long hook title vs a short subject label."""
    t = _norm(text)
    if not t:
        return False
    if subject and _norm_key(t) != _norm_key(subject):
        if len(t) > len(subject) + 8:
            return True
        if len(t.split()) >= 6:
            return True
        if EDITORIAL_WORDS.search(t):
            return True
    return len(t.split()) >= 7 or bool(EDITORIAL_WORDS.search(t))


def _looks_like_person_name(text: str) -> bool:
    t = _norm(text)
    if not t or not _is_entity_label(t):
        return False
    words = t.split()
    if len(words) < 2 or len(words) > 4:
        return False
    if any(ch.isdigit() for ch in t):
        return False
    if re.search(r"\b(inc|corp|llc|ltd|group|systems|technologies|part|volume|season)\b", t, re.I):
        return False
    return all(w[0].isupper() for w in words if w)


def _series_tagline(title: str) -> str:
    title = _norm(title)
    if m := PART_PATTERN.match(title):
        tail = _norm(m.group(3))
        part = f"Part {m.group(2)}"
        return f"{part}: {tail}" if tail else part
    if m := VOLUME_PATTERN.match(title):
        return f"Volume {m.group(2)}"
    if m := COLON_PATTERN.match(title):
        return _norm(m.group(2))
    return ""


def _parse_episode_framing(title: str) -> tuple[str, str]:
    """Strip season/episode or editorial prefixes; return (subject, framing label)."""
    title = _norm(title)
    if m := SEASON_EPISODE_PREFIX.match(title):
        return _norm(m.group(3)), f"Season {m.group(1)} · Episode {m.group(2)}"
    if m := EPISODE_NUMBER_COLON.match(title):
        return _norm(m.group(2)), f"Episode {m.group(1)}"
    if m := EPISODE_NUMBER_SPACE.match(title):
        return _norm(m.group(2)), f"Episode {m.group(1)}"
    if m := EDITORIAL_COLON_PREFIX.match(title):
        return _norm(m.group(2)), ""
    return title, ""


def _headline_from_subject(subject: str) -> tuple[str, str]:
    """Return (headline, optional tagline for subtitle)."""
    subject = _norm(subject)
    if m := WITH_PAREN_PATTERN.match(subject):
        return m.group(1).strip(), m.group(2).strip()
    if m := re.match(r"^(.+?)\s+\(([^)]+)\)$", subject):
        left, right = m.group(1).strip(), m.group(2).strip()
        if re.match(r"^Part\s+", right, re.I):
            return subject, ""
        if _looks_like_person_name(left) or len(left.split()) <= 3:
            return left, right
    if m := PERSON_ON_THEME.match(subject):
        left, right = m.group(1).strip(), m.group(2).strip()
        if "&" in left or _looks_like_person_name(left) or len(left.split()) <= 6:
            return left, right
    headline = _company_headline(subject)
    tagline = _series_tagline(subject)
    if tagline and _norm_key(tagline) != _norm_key(headline):
        return headline, tagline
    return headline, ""


def _merge_framing(guest_role: str, framing: str) -> str:
    if not framing:
        return guest_role
    if guest_role and _norm_key(framing) in _norm_key(guest_role):
        return guest_role
    return _format_subtitle(guest_role, framing)


def _company_headline(title: str) -> str:
    title = _norm(title)
    subject, _ = _parse_episode_framing(title)
    title = subject
    if m := PART_PATTERN.match(title):
        return m.group(1).strip()
    if m := VOLUME_PATTERN.match(title):
        return m.group(1).strip()
    if m := WITH_PAREN_PATTERN.match(title):
        return m.group(1).strip()
    if m := COLON_PATTERN.match(title):
        left, right = m.group(1).strip(), m.group(2).strip()
        if GENERIC_HEADLINE.match(left) or _is_editorial_title(left):
            return right
        if _is_entity_label(left):
            return left
        if len(left.split()) <= 4:
            return left
        return right
    return title


def _parse_title(title: str) -> dict[str, str]:
    title = _norm(title)
    if m := CEO_PATTERN.match(title):
        return {"company": m.group(1), "person": m.group(2), "role": "CEO"}
    if m := WITH_PATTERN.match(title):
        return {"company": m.group(1), "person": m.group(2)}
    if m := COLON_PATTERN.match(title):
        return {"company": m.group(1), "tagline": m.group(2)}
    return {"company": title}


def _resolve_acquired_titles(
    title: str, guest: str, guest_role: str
) -> tuple[str, str, str | None, str]:
    title = _norm(title)
    guest = _norm(guest)
    guest_role = _norm(guest_role)

    subject, framing = _parse_episode_framing(title)
    if guest and _norm_key(guest) == _norm_key(title):
        guest = subject

    if m := CEO_PATTERN.match(subject):
        company = m.group(1).strip()
        person = m.group(2).strip()
        subtitle = _format_subtitle(person, "CEO", _merge_framing(guest_role, framing))
        return company, subtitle, person, "CEO"

    if m := WITH_PAREN_PATTERN.match(subject):
        company = m.group(1).strip()
        person = m.group(2).strip()
        subtitle = _format_subtitle(person, _merge_framing(guest_role, framing))
        return company, subtitle, person, guest_role

    if m := INTERVIEW_PATTERN.match(subject):
        person = m.group(1).strip()
        subtitle = _format_subtitle("Interview", _merge_framing(guest_role, framing))
        return person, subtitle, person, guest_role

    if m := WITH_PATTERN.match(subject):
        company = m.group(1).strip()
        person = m.group(2).strip()
        subtitle = _format_subtitle(person, _merge_framing(guest_role, framing))
        return company, subtitle, person, guest_role

    if (
        guest
        and subject
        and _norm_key(guest) != _norm_key(subject)
        and _is_entity_label(guest)
        and _is_editorial_title(subject, guest)
    ):
        subtitle = _format_subtitle(subject, _merge_framing(guest_role, framing))
        return guest, subtitle, None, guest_role

    if guest and _looks_like_person_name(guest) and subject and _norm_key(guest) != _norm_key(subject):
        company = _company_headline(subject)
        if company and _norm_key(company) != _norm_key(guest):
            subtitle = _format_subtitle(guest, _merge_framing(guest_role, framing))
            return company, subtitle, guest, guest_role

    headline, tagline = _headline_from_subject(subject)
    subtitle = _format_subtitle(tagline, _merge_framing(guest_role, framing)) if tagline else _merge_framing(guest_role, framing)
    return headline, subtitle, None, guest_role


def _resolve_business_breakdowns_titles(
    title: str, guest: str, guest_role: str
) -> tuple[str, str, str | None, str]:
    parsed = _parse_title(title)
    headline = parsed["company"]
    guest_name: str | None = None
    guest_line_role = guest_role

    if person := parsed.get("person"):
        guest_name = person
        guest_line_role = parsed.get("role") or guest_role
        subtitle = _format_subtitle(
            person,
            guest_line_role if guest_line_role else "",
            guest_role if guest_role and guest_line_role != guest_role else "",
        )
        return headline, subtitle, guest_name, guest_line_role

    if guest and not titles_redundant(title, guest) and _norm_key(guest) != _norm_key(headline):
        guest_name = guest
        subtitle = _format_subtitle(
            guest,
            guest_role,
            parsed.get("tagline", ""),
        )
        return headline, subtitle, guest_name, guest_line_role

    subtitle = _format_subtitle(parsed.get("tagline", ""), guest_role)
    return headline, subtitle, guest_name, guest_line_role


def resolve_display_titles(
    podcast: str,
    title: str,
    guest: str,
    guest_role: str = "",
) -> tuple[str, str, str | None, str]:
    """Return headline, subtitle, guest line name, guest line role."""
    title = _norm(title)
    guest = _norm(guest)
    guest_role = _norm(guest_role)

    if podcast in ACQUIRED_PODCASTS:
        return _resolve_acquired_titles(title, guest, guest_role)

    if podcast in COMPANY_FIRST_PODCASTS:
        return _resolve_business_breakdowns_titles(title, guest, guest_role)

    headline = guest or title
    subtitle = title
    guest_name = guest or None
    guest_line_role = guest_role

    if titles_redundant(title, guest):
        subtitle = guest_role
    elif guest and title.lower().startswith(guest.lower()):
        if m := GUEST_PREFIX_PATTERN.match(title):
            rest = _norm(m.group(2))
            if rest:
                subtitle = rest
                if podcast == "Founders" and guest_role and rest.lower() not in guest_role.lower():
                    subtitle = _format_subtitle(rest, guest_role)
            else:
                subtitle = guest_role

    if subtitle and _norm_key(subtitle) == _norm_key(headline):
        subtitle = guest_role

    return headline, subtitle, guest_name, guest_line_role


def normalize_episode_metadata(title: str, guest: str, guest_role: str = "") -> dict[str, str]:
    """Clean stored title/guest so season/editorial framing lives in guest_role only."""
    title = _norm(title)
    guest = _norm(guest)
    guest_role = _norm(guest_role)
    subject, framing = _parse_episode_framing(title)

    new_title = subject
    new_guest = guest
    new_role = _merge_framing(guest_role, framing)

    if guest and _norm_key(guest) == _norm_key(title):
        if m := WITH_PAREN_PATTERN.match(subject):
            new_title = m.group(1).strip()
            new_guest = m.group(2).strip()
        elif m := PERSON_ON_THEME.match(subject):
            new_guest = m.group(1).strip()
            new_title = m.group(2).strip()
        elif m := WITH_PATTERN.match(subject):
            person = m.group(2).strip()
            if _looks_like_person_name(person):
                new_title = m.group(1).strip()
                new_guest = person
            else:
                new_guest = subject
        else:
            new_guest = subject
    elif guest and (EPISODE_NUMBER_SPACE.match(guest) or EPISODE_NUMBER_COLON.match(guest)):
        new_guest = new_title

    return {"title": new_title, "guest": new_guest, "guest_role": new_role}


def display_fields_from_summary(data: dict[str, Any]) -> dict[str, str | None]:
    meta = data.get("metadata") or {}
    podcast = str(data.get("podcast") or "")
    headline, subtitle, guest_name, guest_role = resolve_display_titles(
        podcast,
        str(meta.get("title") or ""),
        str(meta.get("guest") or ""),
        str(meta.get("guest_role") or ""),
    )
    return {
        "display_title": headline,
        "display_subtitle": subtitle,
        "display_guest": guest_name,
        "display_guest_role": guest_role,
    }
