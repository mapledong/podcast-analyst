"""HTML + plain-text rendering for the weekly podcast digest email."""

from __future__ import annotations

import html
import json
from datetime import date, timedelta
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parent.parent
APPROVED = ROOT / "data" / "approved"

PODCAST_SLUG: dict[str, str] = {
    "Invest Like the Best": "invest-like-the-best",
    "Acquired": "acquired",
    "Founders": "founders",
    "Business Breakdowns": "business-breakdowns",
}

PODCAST_ACCENT: dict[str, str] = {
    "Invest Like the Best": "#C45D3E",
    "Acquired": "#1B3A4B",
    "Founders": "#2D5016",
    "Business Breakdowns": "#0068B3",
}

DIR_STYLES: dict[str, tuple[str, str]] = {
    "Long": ("#248a3d", "rgba(52,199,89,0.12)"),
    "Short": ("#d70015", "rgba(255,59,48,0.10)"),
    "Watch": ("#c93400", "rgba(255,149,0,0.12)"),
}


def parse_episode_date(raw: str) -> date | None:
    if not raw:
        return None
    try:
        return date.fromisoformat(str(raw)[:10])
    except ValueError:
        return None


def date_window(*, days: int, end: date | None = None) -> tuple[date, date]:
    end = end or date.today()
    start = end - timedelta(days=days)
    return start, end


def load_weekly_items(*, days: int = 7, end: date | None = None) -> tuple[list[dict[str, Any]], date, date]:
    start, end_d = date_window(days=days, end=end)
    items: list[dict[str, Any]] = []
    for path in sorted(APPROVED.glob("*.json")):
        try:
            data = json.loads(path.read_text(encoding="utf-8"))
        except Exception:
            continue
        meta = data.get("metadata") or {}
        ep_date = parse_episode_date(meta.get("date") or "")
        if ep_date is None or not (start <= ep_date <= end_d):
            continue
        podcast = data.get("podcast", "")
        slug = PODCAST_SLUG.get(podcast, podcast.lower().replace(" ", "-"))
        eid = data.get("episode_id", path.stem)
        site_base = ""  # filled by caller
        items.append(
            {
                "id": eid,
                "podcast": podcast,
                "podcast_slug": slug,
                "accent": PODCAST_ACCENT.get(podcast, "#1d1d1f"),
                "title": meta.get("title", "") or eid,
                "guest": meta.get("guest", ""),
                "guest_role": meta.get("guest_role", ""),
                "guest_line": _format_guest_affiliation(
                    meta.get("guest", "") or "",
                    meta.get("guest_role", "") or "",
                ),
                "date": ep_date.isoformat(),
                "date_display": ep_date.strftime("%b %d, %Y"),
                "conclusion": (data.get("conclusion") or "").strip(),
                "ideas": _structured_ideas(data),
                "rating": (data.get("episode_rating") or {}).get("overall"),
                "keywords": data.get("keywords") or [],
            }
        )
    items.sort(key=lambda x: (x["date"], x["podcast"], x["title"]), reverse=True)
    return items, start, end_d


def _structured_ideas(data: dict) -> list[dict[str, str]]:
    out: list[dict[str, str]] = []
    for item in data.get("top_investment_implications") or []:
        out.append(
            {
                "ticker": str(item.get("ticker") or ""),
                "direction": str(item.get("direction") or ""),
                "confidence": str(item.get("confidence") or ""),
                "thesis": str(item.get("thesis") or "").strip(),
            }
        )
    return out


def _esc(text: str) -> str:
    return html.escape(text or "")


def _format_guest_affiliation(guest: str, guest_role: str) -> str:
    """Guest name plus institution / title from metadata.guest_role."""
    guest = (guest or "").strip()
    role = (guest_role or "").strip()
    if not guest:
        return role
    if not role:
        return guest

    # ILTB-style: "Founder, Whale Rock Capital Management"
    if "·" not in role and "," in role:
        return f"{guest} · {role}"

    parts = [p.strip() for p in role.split("·")]
    parts = [p for p in parts if p]
    if parts and parts[0].lower() == "biography":
        parts = parts[1:]
    parts = [p for p in parts if not p.lower().startswith("episode")]
    if not parts:
        return guest
    if len(parts) == 1:
        return f"{guest} · {parts[0]}"
    title, org = parts[0], parts[1]
    if any(k in org.lower() for k in ("biography", "episode")):
        return f"{guest} · {title}"
    return f"{guest} · {title}, {org}"


def _dir_badge(direction: str) -> str:
    d = direction if direction in DIR_STYLES else "Watch"
    color, bg = DIR_STYLES.get(d, DIR_STYLES["Watch"])
    label = d.upper()
    return (
        f'<span style="display:inline-block;font-size:10px;font-weight:700;letter-spacing:0.04em;'
        f"padding:2px 7px;border-radius:4px;color:{color};background:{bg};margin-right:6px;\">{label}</span>"
    )


def render_html(
    items: list[dict[str, Any]],
    *,
    site_url: str,
    start: date,
    end: date,
    trial: bool = False,
) -> str:
    base = site_url.rstrip("/")
    range_label = f"{start.strftime('%Y-%m-%d')} — {end.strftime('%Y-%m-%d')}"
    podcasts = sorted({i["podcast"] for i in items})
    podcast_pills = " ".join(
        f'<span style="display:inline-block;font-size:11px;font-weight:600;color:{PODCAST_ACCENT.get(p, "#1d1d1f")};'
        f'background:{PODCAST_ACCENT.get(p, "#1d1d1f")}18;padding:3px 10px;border-radius:999px;margin:0 6px 6px 0;">'
        f"{_esc(p)}</span>"
        for p in podcasts
    )

    toc_rows = []
    for idx, item in enumerate(items, start=1):
        link = f"{base}/podcast/{item['podcast_slug']}/{item['id']}" if base else "#"
        guest_line = item.get("guest_line") or item.get("guest") or ""
        toc_rows.append(
            f"""
            <tr>
              <td style="padding:14px 0;border-bottom:1px solid rgba(0,0,0,0.06);vertical-align:top;width:28px;color:#86868b;font-size:13px;font-weight:600;">{idx}</td>
              <td style="padding:14px 0;border-bottom:1px solid rgba(0,0,0,0.06);vertical-align:top;">
                <div style="margin-bottom:6px;">
                  <span style="display:inline-block;font-size:11px;font-weight:600;color:{item['accent']};background:{item['accent']}18;padding:2px 8px;border-radius:999px;">{_esc(item['podcast'])}</span>
                  <span style="font-size:12px;color:#86868b;margin-left:8px;">{item['date_display']}</span>
                </div>
                <a href="{_esc(link)}" style="color:#1d1d1f;font-size:15px;font-weight:600;text-decoration:none;line-height:1.35;">{_esc(item['title'])}</a>
                {f'<div style="font-size:13px;color:#424245;margin-top:6px;line-height:1.45;">{_esc(guest_line)}</div>' if guest_line else ''}
              </td>
            </tr>"""
        )

    detail_blocks = []
    for idx, item in enumerate(items, start=1):
        link = f"{base}/podcast/{item['podcast_slug']}/{item['id']}" if base else "#"
        ideas_html = ""
        if item["ideas"]:
            idea_rows = []
            for idea in item["ideas"]:
                conf = f" · {idea['confidence']}" if idea.get("confidence") else ""
                idea_rows.append(
                    f"""
                    <div style="padding:12px 14px;background:#fbfbfd;border:1px solid rgba(0,0,0,0.06);border-radius:10px;margin-bottom:8px;">
                      <div style="margin-bottom:6px;">
                        {_dir_badge(idea.get('direction', ''))}
                        <span style="font-size:13px;font-weight:600;color:#1d1d1f;">{_esc(idea.get('ticker', ''))}{_esc(conf)}</span>
                      </div>
                      <div style="font-size:14px;line-height:1.5;color:#424245;">{_esc(idea.get('thesis', ''))}</div>
                    </div>"""
                )
            ideas_html = f"""
              <div style="margin-top:18px;">
                <div style="font-size:11px;font-weight:700;letter-spacing:0.06em;text-transform:uppercase;color:#86868b;margin-bottom:10px;">Investment Ideas</div>
                {''.join(idea_rows)}
              </div>"""

        detail_blocks.append(
            f"""
            <div id="ep-{idx}" style="background:#ffffff;border:1px solid rgba(0,0,0,0.08);border-radius:18px;padding:24px;margin-bottom:20px;box-shadow:0 1px 3px rgba(0,0,0,0.06),0 4px 16px rgba(0,0,0,0.04);">
              <div style="display:flex;align-items:flex-start;justify-content:space-between;gap:12px;margin-bottom:12px;">
                <div>
                  <div style="font-size:12px;font-weight:600;color:{item['accent']};margin-bottom:6px;">#{idx} · {_esc(item['podcast'])} · {item['date_display']}</div>
                  <h2 style="margin:0;font-size:20px;font-weight:700;line-height:1.25;color:#1d1d1f;">{_esc(item['title'])}</h2>
                  {f'<div style="margin-top:8px;font-size:14px;color:#424245;line-height:1.45;">{_esc(item.get("guest_line") or item.get("guest", ""))}</div>' if item.get('guest') or item.get('guest_line') else ''}
                </div>
              </div>
              <div style="margin-top:16px;padding:16px 18px;background:#f5f5f7;border-radius:12px;border-left:4px solid {item['accent']};">
                <div style="font-size:11px;font-weight:700;letter-spacing:0.06em;text-transform:uppercase;color:#86868b;margin-bottom:8px;">Conclusion</div>
                <div style="font-size:15px;line-height:1.55;color:#1d1d1f;">{_esc(item.get('conclusion', ''))}</div>
              </div>
              {ideas_html}
              <div style="margin-top:16px;">
                <a href="{_esc(link)}" style="font-size:14px;font-weight:600;color:#0066cc;text-decoration:none;">Read full summary →</a>
              </div>
            </div>"""
        )

    empty = """
      <div style="padding:32px;text-align:center;color:#86868b;background:#ffffff;border-radius:18px;border:1px solid rgba(0,0,0,0.08);">
        No episodes with a podcast date in this window had summaries on the library yet.
      </div>"""

    trial_banner = ""
    if trial:
        trial_banner = """
          <div style="margin-bottom:20px;padding:12px 16px;background:#fff8e6;border:1px solid #ffd60a;border-radius:12px;font-size:13px;color:#6e5a00;">
            Trial preview — filtered by <strong>episode publish date</strong>, not git commit date.
          </div>"""

    return f"""<!DOCTYPE html>
<html lang="zh-CN">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>Podcast Analyst Weekly</title>
</head>
<body style="margin:0;padding:0;background:#f5f5f7;font-family:-apple-system,BlinkMacSystemFont,'SF Pro Text','Segoe UI',Roboto,Helvetica,Arial,sans-serif;color:#1d1d1f;-webkit-font-smoothing:antialiased;">
  <div style="max-width:640px;margin:0 auto;padding:24px 16px 40px;">
    <div style="text-align:center;margin-bottom:28px;">
      <div style="font-size:13px;font-weight:600;letter-spacing:0.08em;text-transform:uppercase;color:#86868b;margin-bottom:8px;">Podcast Analyst</div>
      <h1 style="margin:0 0 8px;font-size:28px;font-weight:700;letter-spacing:-0.02em;">Weekly Update</h1>
      <div style="font-size:14px;color:#86868b;">Episode dates {range_label}</div>
    </div>
    {trial_banner}
    <div style="background:#ffffff;border-radius:18px;border:1px solid rgba(0,0,0,0.08);padding:24px 24px 8px;margin-bottom:32px;box-shadow:0 1px 3px rgba(0,0,0,0.06),0 4px 16px rgba(0,0,0,0.04);">
      <div style="display:flex;align-items:flex-end;justify-content:space-between;gap:16px;margin-bottom:16px;flex-wrap:wrap;">
        <div>
          <div style="font-size:11px;font-weight:700;letter-spacing:0.08em;text-transform:uppercase;color:#86868b;margin-bottom:6px;">This Week</div>
          <div style="font-size:22px;font-weight:700;color:#1d1d1f;line-height:1.2;">{len(items)} episode{'s' if len(items) != 1 else ''}</div>
          <div style="font-size:13px;color:#86868b;margin-top:4px;">{range_label}</div>
        </div>
        {f'<a href="{_esc(base)}" style="font-size:13px;font-weight:600;color:#0066cc;text-decoration:none;white-space:nowrap;">Browse library →</a>' if base else ''}
      </div>
      {f'<div style="margin-bottom:18px;">{podcast_pills}</div>' if podcast_pills else ''}
      <table role="presentation" cellpadding="0" cellspacing="0" width="100%" style="border-collapse:collapse;">
        {''.join(toc_rows) if toc_rows else f'<tr><td style="padding:20px 0;color:#86868b;">{empty}</td></tr>'}
      </table>
    </div>

    {f'<div style="margin-bottom:12px;font-size:11px;font-weight:700;letter-spacing:0.08em;text-transform:uppercase;color:#86868b;">Details</div>{"".join(detail_blocks)}' if detail_blocks else ''}

    <div style="text-align:center;margin-top:32px;font-size:12px;color:#86868b;line-height:1.6;">
      Podcast Analyst · curated podcast summaries<br>
      {f'<a href="{_esc(base)}" style="color:#0066cc;text-decoration:none;">{ _esc(base) }</a>' if base else ''}
    </div>
  </div>
</body>
</html>"""


def render_plain(
    items: list[dict[str, Any]],
    *,
    site_url: str,
    start: date,
    end: date,
    trial: bool = False,
) -> str:
    range_label = f"{start.isoformat()} — {end.isoformat()}"
    lines = [
        "Podcast Analyst · Weekly Update",
        f"Episode dates: {range_label}",
        "",
    ]
    if site_url:
        lines.append(f"Site: {site_url.rstrip('/')}")
        lines.append("")
    if not items:
        lines.append("No episodes in this date window.")
        return "\n".join(lines) + "\n"

    lines.append(f"This week: {len(items)} episode(s)")
    lines.append("")
    lines.append("=== INDEX ===")
    for idx, item in enumerate(items, start=1):
        lines.append(f"{idx}. [{item['date']}] {item['podcast']} — {item['title']}")
        guest_line = item.get("guest_line") or item.get("guest")
        if guest_line:
            lines.append(f"   {guest_line}")
    lines.append("")
    lines.append("=== DETAILS ===")
    for idx, item in enumerate(items, start=1):
        lines.append(f"\n--- {idx}. {item['podcast']} | {item['title']} ({item['date']}) ---")
        if item.get("conclusion"):
            lines.append(f"Conclusion: {item['conclusion']}")
        if item["ideas"]:
            lines.append("Investment ideas:")
            for idea in item["ideas"]:
                head = " ".join(
                    x for x in (idea.get("ticker"), idea.get("direction"), idea.get("confidence")) if x
                )
                lines.append(f"  • {head}: {idea.get('thesis', '')}")
    if trial:
        lines.append("\n[Trial] Filtered by episode publish date.")
    return "\n".join(lines).strip() + "\n"
