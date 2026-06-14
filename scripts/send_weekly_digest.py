#!/usr/bin/env python3
"""Email a weekly digest of newly added podcast summaries."""

from __future__ import annotations

import argparse
import json
import os
import smtplib
import subprocess
from datetime import datetime, timezone
from email.message import EmailMessage
from pathlib import Path
from typing import Iterable


ROOT = Path(__file__).resolve().parent.parent
APPROVED = ROOT / "data" / "approved"
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


def _run_git(args: list[str]) -> str:
    return subprocess.check_output(["git", *args], cwd=str(ROOT), text=True, stderr=subprocess.DEVNULL)


def _changed_approved_files(days: int) -> list[Path]:
    since = f"{days} days ago"
    try:
        raw = _run_git(["log", f"--since={since}", "--name-only", "--pretty=format:", "--", "data/approved"])
    except Exception:
        raw = ""
    files = []
    seen: set[Path] = set()
    for line in raw.splitlines():
        line = line.strip()
        if not line.endswith(".json") or not line.startswith("data/approved/"):
            continue
        path = ROOT / line
        if path.exists() and path not in seen:
            seen.add(path)
            files.append(path)
    return sorted(files, key=lambda p: p.name)


def _investment_ideas(data: dict) -> list[str]:
    ideas = []
    for item in data.get("top_investment_implications") or []:
        ticker = item.get("ticker", "")
        direction = item.get("direction", "")
        confidence = item.get("confidence", "")
        thesis = item.get("thesis", "")
        head = " ".join(x for x in (ticker, direction, f"({confidence})" if confidence else "") if x)
        ideas.append(f"{head}: {thesis}".strip(": "))
    return ideas


def _digest_items(paths: Iterable[Path]) -> list[dict]:
    items = []
    for path in paths:
        try:
            data = json.loads(path.read_text(encoding="utf-8"))
        except Exception:
            continue
        meta = data.get("metadata") or {}
        items.append(
            {
                "id": data.get("episode_id", path.stem),
                "podcast": data.get("podcast", ""),
                "title": meta.get("title", ""),
                "guest": meta.get("guest", ""),
                "date": meta.get("date", ""),
                "conclusion": data.get("conclusion", ""),
                "ideas": _investment_ideas(data),
            }
        )
    items.sort(key=lambda x: (x["podcast"], x["date"], x["id"]), reverse=True)
    return items


def _plain_text(items: list[dict], *, site_url: str) -> str:
    now = datetime.now(timezone.utc).strftime("%Y-%m-%d")
    lines = [f"Podcast Analyst Weekly Update - {now}", ""]
    if site_url:
        lines += [f"Site: {site_url}", ""]
    if not items:
        lines.append("No new podcast summaries were added in the past week.")
        return "\n".join(lines)

    lines.append(f"New summaries this week: {len(items)}")
    lines.append("")
    for item in items:
        lines.append(f"- {item['podcast']} | {item['title'] or item['id']}")
        if item["guest"]:
            lines.append(f"  Guest / Subject: {item['guest']}")
        if item["conclusion"]:
            lines.append(f"  Conclusion: {item['conclusion']}")
        if item["ideas"]:
            lines.append("  Investment ideas:")
            for idea in item["ideas"]:
                lines.append(f"    - {idea}")
        lines.append("")
    return "\n".join(lines).strip() + "\n"


def _html(text: str) -> str:
    escaped = (
        text.replace("&", "&amp;")
        .replace("<", "&lt;")
        .replace(">", "&gt;")
        .replace("\n", "<br>\n")
    )
    return f"<html><body style=\"font-family: -apple-system, BlinkMacSystemFont, Segoe UI, sans-serif; line-height:1.45\">{escaped}</body></html>"


def send_email(subject: str, body: str, *, to_addr: str) -> None:
    missing = [k for k in ("SMTP_HOST", "SMTP_USER", "SMTP_PASSWORD") if not os.environ.get(k)]
    if missing:
        raise SystemExit(
            "Missing SMTP config: "
            + ", ".join(missing)
            + ". Add GitHub secrets (SMTP_HOST, SMTP_USER, SMTP_PASSWORD, SMTP_FROM) "
            "or create a local .env — see docs/automation.md."
        )
    host = os.environ["SMTP_HOST"]
    port = int(os.environ.get("SMTP_PORT") or "587")
    user = os.environ["SMTP_USER"]
    password = os.environ["SMTP_PASSWORD"]
    from_addr = os.environ.get("SMTP_FROM", user)

    msg = EmailMessage()
    msg["Subject"] = subject
    msg["From"] = from_addr
    msg["To"] = to_addr
    msg.set_content(body)
    msg.add_alternative(_html(body), subtype="html")

    with smtplib.SMTP(host, port) as smtp:
        smtp.starttls()
        smtp.login(user, password)
        smtp.send_message(msg)


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--days", type=int, default=7)
    parser.add_argument("--to", default=os.environ.get("WEEKLY_DIGEST_TO", DEFAULT_TO))
    parser.add_argument("--dry-run", action="store_true")
    parser.add_argument(
        "--trial",
        action="store_true",
        help="Mark email as a trial run ([Trial] subject prefix, footer note)",
    )
    parser.add_argument(
        "--max-items",
        type=int,
        default=0,
        help="Cap number of summaries in the email (0 = no limit)",
    )
    args = parser.parse_args()

    paths = _changed_approved_files(args.days)
    items = _digest_items(paths)
    if args.max_items > 0:
        items = items[: args.max_items]
    site_url = os.environ.get("SITE_URL", "")
    body = _plain_text(items, site_url=site_url)
    if args.trial:
        body += (
            "\n---\n"
            "[Trial run] This is a preview of the weekly digest format. "
            f"Showing {len(items)} of recent summaries (window: past {args.days} days).\n"
        )
    subject = f"Podcast Analyst weekly update: {len(items)} new summaries"
    if args.trial:
        subject = f"[Trial] {subject}"

    if args.dry_run:
        print(body)
        return 0

    send_email(subject, body, to_addr=args.to)
    print(f"Sent weekly digest to {args.to} ({len(items)} summaries)")
    return 0


if __name__ == "__main__":
    _load_dotenv()
    raise SystemExit(main())
