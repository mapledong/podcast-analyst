#!/usr/bin/env python3
"""Send the production weekly digest email (template v1).

Filter: episode publish date in the past N days (default 7, see config/weekly_digest.yaml).
Scheduled: Sunday 12:00 Beijing via .github/workflows/weekly-digest.yml
"""

from __future__ import annotations

import argparse
import os
import smtplib
import sys
from datetime import date
from email.message import EmailMessage
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))

from scripts.weekly_digest_render import (  # noqa: E402
    default_lookback_days,
    load_weekly_items,
    render_html,
    render_plain,
)

DEFAULT_TO = "mapledong1996@hotmail.com"


def _load_dotenv() -> None:
    path = ROOT / ".env"
    if not path.exists():
        return
    for line in path.read_text(encoding="utf-8").splitlines():
        line = line.strip()
        if not line or line.startswith("#") or "=" not in line:
            continue
        key, _, val = line.partition("=")
        key = key.strip()
        val = val.strip().strip("'\"")
        if key and key not in os.environ:
            os.environ[key] = val


def _normalize_smtp_host(raw: str) -> str:
    host = raw.strip().strip('"').strip("'")
    for prefix in ("https://", "http://"):
        if host.lower().startswith(prefix):
            host = host[len(prefix) :]
    host = host.split("/")[0].strip()
    if "@" in host:
        raise SystemExit(
            "SMTP_HOST looks like an email address. "
            "Set SMTP_HOST=smtp.gmail.com and SMTP_USER=your@gmail.com separately."
        )
    if "." not in host:
        raise SystemExit(
            f"SMTP_HOST={host!r} is not a mail server hostname. "
            "Use SMTP_HOST=smtp.gmail.com and put your email in SMTP_USER."
        )
    if ":" in host:
        host = host.rsplit(":", 1)[0]
    return host


def _smtp_config() -> tuple[str, int, str, str, str]:
    missing = [k for k in ("SMTP_HOST", "SMTP_USER", "SMTP_PASSWORD") if not (os.environ.get(k) or "").strip()]
    if missing:
        raise SystemExit(
            "Missing SMTP config: "
            + ", ".join(missing)
            + ". In GitHub: repo Settings → Secrets and variables → Actions. See docs/automation.md."
        )
    host = _normalize_smtp_host(os.environ["SMTP_HOST"])
    if host.lower() in {"smtp.google.com", "googlemail.com", "smtp.googlemail.com"}:
        host = "smtp.gmail.com"
    if not host or " " in host or "." not in host:
        raise SystemExit(f"Invalid SMTP_HOST after cleanup: {host!r}. For Gmail use smtp.gmail.com")
    raw_port = (os.environ.get("SMTP_PORT") or "587").strip() or "587"
    port = int(raw_port)
    user = os.environ["SMTP_USER"].strip()
    password = os.environ["SMTP_PASSWORD"].replace(" ", "").strip()
    from_addr = (os.environ.get("SMTP_FROM") or user).strip()
    return host, port, user, password, from_addr


def send_email(subject: str, plain: str, html: str, *, to_addr: str) -> None:
    host, port, user, password, from_addr = _smtp_config()
    use_ssl = (os.environ.get("SMTP_USE_SSL") or "").strip().lower() in {"1", "true", "yes"}
    if host.endswith("gmail.com") and port == 25:
        port = 587

    msg = EmailMessage()
    msg["Subject"] = subject
    msg["From"] = from_addr
    msg["To"] = to_addr
    msg.set_content(plain)
    msg.add_alternative(html, subtype="html")

    try:
        if use_ssl or port == 465:
            with smtplib.SMTP_SSL(host, port, timeout=30) as smtp:
                smtp.login(user, password)
                smtp.send_message(msg)
        else:
            with smtplib.SMTP(host, port, timeout=30) as smtp:
                smtp.ehlo()
                smtp.starttls()
                smtp.ehlo()
                smtp.login(user, password)
                smtp.send_message(msg)
    except smtplib.SMTPAuthenticationError as exc:
        raise SystemExit(
            f"SMTP login failed for {user} @ {host}:{port}. "
            "Gmail: use an App Password. "
            f"Detail: {exc}"
        ) from exc
    except OSError as exc:
        raise SystemExit(f"Cannot connect to SMTP {host}:{port} ({exc}).") from exc
    except smtplib.SMTPException as exc:
        raise SystemExit(f"SMTP send failed: {exc}") from exc


def main() -> int:
    parser = argparse.ArgumentParser(description="Weekly digest by episode publish date")
    parser.add_argument("--days", type=int, default=default_lookback_days(), help="Look back N days by episode date")
    parser.add_argument("--to", default=os.environ.get("WEEKLY_DIGEST_TO", DEFAULT_TO))
    parser.add_argument("--dry-run", action="store_true", help="Print plain-text digest to stdout")
    parser.add_argument("--preview-html", metavar="PATH", help="Write HTML preview to file")
    parser.add_argument("--trial", action="store_true", help="Mark as trial in subject/banner")
    parser.add_argument("--max-items", type=int, default=0, help="Cap episodes (0 = no limit)")
    parser.add_argument("--test-smtp", action="store_true", help="Send SMTP connectivity test only")
    args = parser.parse_args()

    if args.test_smtp:
        host, port, user, _, _ = _smtp_config()
        print(f"SMTP config OK: host={host} port={port} user={user}")
        send_email(
            "[SMTP test] Podcast Analyst",
            "SMTP connectivity test.",
            "<p>SMTP connectivity test.</p>",
            to_addr=args.to,
        )
        print(f"SMTP test email sent to {args.to}")
        return 0

    items, start, end = load_weekly_items(days=args.days)
    if args.max_items > 0:
        items = items[: args.max_items]
    site_url = os.environ.get("SITE_URL", "")
    plain = render_plain(items, site_url=site_url, start=start, end=end, trial=args.trial)
    html = render_html(items, site_url=site_url, start=start, end=end, trial=args.trial)

    if args.preview_html:
        out = Path(args.preview_html)
        out.parent.mkdir(parents=True, exist_ok=True)
        out.write_text(html, encoding="utf-8")
        print(f"Wrote HTML preview: {out}")

    subject = f"Podcast Analyst 周报 · {len(items)} 期 · {start.strftime('%m/%d')}–{end.strftime('%m/%d')}"
    if args.trial:
        subject = f"[Trial] {subject}"

    if args.dry_run:
        print(plain)
        return 0

    if args.preview_html and not os.environ.get("SMTP_HOST"):
        print("No SMTP configured — preview only.")
        return 0

    send_email(subject, plain, html, to_addr=args.to)
    print(f"Sent weekly digest to {args.to} ({len(items)} episodes, dates {start}–{end})")
    return 0


if __name__ == "__main__":
    _load_dotenv()
    raise SystemExit(main())
