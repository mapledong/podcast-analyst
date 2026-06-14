#!/usr/bin/env python3
"""Podcast analyst pipeline: YouTube transcript → structured JSON → markdown summary."""

from __future__ import annotations

import json
import sys
from pathlib import Path

import click
import yaml
from rich.console import Console
from rich.table import Table

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))

from src.extract import extract_summary, merge_with_metadata  # noqa: E402
from src.extract_acquired import extract_acquired_summary, merge_acquired_metadata  # noqa: E402
from src.fetch_transcript import fetch_transcript, save_transcript  # noqa: E402
from src.render import render_summary, save_summary  # noqa: E402
from src.template_config import template_path_for_podcast  # noqa: E402
from src.validate import (
    choose_rating,
    load_template_config,
    validate_rating_distribution,
    validate_summary,
)  # noqa: E402

console = Console()


def sync_web_catalog() -> None:
    """Refresh web/src/data after publish (best-effort)."""
    sync_script = ROOT / "web" / "scripts" / "sync-content.mjs"
    if not sync_script.exists():
        return
    import subprocess

    result = subprocess.run(
        ["node", str(sync_script)],
        cwd=str(ROOT / "web"),
        capture_output=True,
        text=True,
    )
    if result.returncode != 0:
        console.print("[yellow]Web sync skipped:[/yellow]", result.stderr.strip() or result.stdout)
        return
    console.print(f"[green]Web catalog synced[/green] ({result.stdout.strip()})")


def load_episodes_config(path: Path) -> dict:
    return yaml.safe_load(path.read_text(encoding="utf-8"))


def find_episode(cfg: dict, episode_id: str) -> dict | None:
    for ep in cfg.get("episodes", []):
        if ep["id"] == episode_id:
            return ep
    return None


def print_validation(report) -> None:
    table = Table(title="Validation Report")
    table.add_column("Section")
    table.add_column("Severity")
    table.add_column("Message")
    for issue in report.issues:
        table.add_row(issue.section, issue.severity, issue.message)
    console.print(table)
    console.print(
        f"Total words: {report.total_words} / {report.max_total_words} · "
        f"Status: {'PASS' if report.passed else 'FAIL'}"
    )


@click.group()
def cli() -> None:
    """Invest Like the Best (and other) podcast summary pipeline."""


@cli.command("fetch")
@click.option("--episode", "-e", required=True, help="Episode id from config/episodes.yaml")
@click.option("--config", default=str(ROOT / "config" / "episodes.yaml"))
def fetch_cmd(episode: str, config: str) -> None:
    """Step 1: Fetch YouTube transcript."""
    cfg = load_episodes_config(Path(config))
    ep = find_episode(cfg, episode)
    if not ep:
        raise click.ClickException(f"Episode not found: {episode}")

    url = ep.get("youtube_url")
    if not url:
        raise click.ClickException(f"No youtube_url for {episode}")

    console.print(f"Fetching transcript for EP.{ep['episode_number']} …")
    result = fetch_transcript(url)
    out = save_transcript(result, ROOT / "data" / "transcripts")
    console.print(f"[green]Saved[/green] {out} ({result.line_count} lines, {result.source})")


@cli.command("extract")
@click.option("--episode", "-e", required=True)
@click.option("--config", default=str(ROOT / "config" / "episodes.yaml"))
@click.option("--model", default=None, help="OpenAI model (default: PODCAST_ANALYST_MODEL or gpt-4.1-mini)")
@click.option(
    "--transcript",
    "-t",
    default=None,
    help="Path to transcript txt; default: data/transcripts/<video_id>.txt",
)
def extract_cmd(episode: str, config: str, model: str | None, transcript: str | None) -> None:
    """Step 2: LLM structured extraction → draft JSON (for human review)."""
    cfg = load_episodes_config(Path(config))
    ep = find_episode(cfg, episode)
    if not ep:
        raise click.ClickException(f"Episode not found: {episode}")

    if transcript:
        tpath = Path(transcript)
    else:
        from src.fetch_transcript import extract_video_id

        vid = extract_video_id(ep["youtube_url"])
        tpath = ROOT / "data" / "transcripts" / f"{vid}.txt"

    if not tpath.exists():
        raise click.ClickException(f"Transcript missing: {tpath}. Run: fetch -e {episode}")

    text = tpath.read_text(encoding="utf-8")
    if text.startswith("# video_id:"):
        text = text.split("\n\n", 1)[-1]

    model_name = model or __import__("os").environ.get("PODCAST_ANALYST_MODEL", "gpt-4.1-mini")
    podcast_name = cfg.get("podcast", "")
    console.print(f"Extracting summary with {model_name} …")
    meta = {**ep, "podcast": podcast_name}
    if podcast_name == "Acquired":
        extracted = extract_acquired_summary(text, meta, model=model_name)
        merged = merge_acquired_metadata(extracted, ep, model=model_name)
    else:
        extracted = extract_summary(text, meta, model=model_name)
        merged = merge_with_metadata(
            extracted,
            ep,
            cfg,
            transcript_source="youtube",
            model=model_name,
        )
    raw_rating = int(merged.get("episode_rating", {}).get("overall", 3))
    tmpl = load_template_config(template_path_for_podcast(podcast_name))
    merged["episode_rating"] = {
        "overall": choose_rating(
            raw_rating,
            tmpl,
            ROOT / "data" / "approved",
            podcast=podcast_name,
            episode_id=episode,
        )
    }

    out = ROOT / "data" / "drafts" / f"{episode}.json"
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(json.dumps(merged, indent=2, ensure_ascii=False), encoding="utf-8")
    console.print(f"[green]Draft JSON[/green] {out}")
    console.print("[yellow]Edit review_notes and fix any issues, then run: publish -e {episode}[/yellow]")


@cli.command("validate")
@click.option("--json", "json_path", required=True, help="Path to summary JSON")
@click.option("--template", default=str(ROOT / "config" / "template.yaml"))
def validate_cmd(json_path: str, template: str) -> None:
    """Validate word limits and investment table schema."""
    data = json.loads(Path(json_path).read_text(encoding="utf-8"))
    tmpl_path = template_path_for_podcast(data.get("podcast"))
    tmpl = load_template_config(tmpl_path if template == str(ROOT / "config" / "template.yaml") else Path(template))
    report = validate_summary(data, tmpl)
    rating = data.get("episode_rating", {}).get("overall")
    try:
        rating_int = int(rating)
        if float(rating) == rating_int and 1 <= rating_int <= 5:
            for issue in validate_rating_distribution(
                rating_int,
                tmpl,
                ROOT / "data" / "approved",
                podcast=data.get("podcast"),
                episode_id=data.get("episode_id"),
            ):
                report.add(issue.section, issue.message, issue.severity)
    except (TypeError, ValueError):
        pass
    print_validation(report)
    if not report.passed:
        raise SystemExit(1)


@cli.command("publish")
@click.option("--episode", "-e", required=True)
@click.option(
    "--from-json",
    default=None,
    help="Summary JSON path; default: data/drafts/<episode>.json or data/approved/<episode>.json",
)
@click.option("--template", default=str(ROOT / "config" / "template.yaml"))
@click.option("--skip-validation", is_flag=True)
def publish_cmd(episode: str, from_json: str | None, template: str, skip_validation: bool) -> None:
    """Step 3: Validate (optional) and render final markdown."""
    if from_json:
        jpath = Path(from_json)
    else:
        approved = ROOT / "data" / "approved" / f"{episode}.json"
        draft = ROOT / "data" / "drafts" / f"{episode}.json"
        jpath = approved if approved.exists() else draft

    if not jpath.exists():
        raise click.ClickException(f"JSON not found: {jpath}")

    data = json.loads(jpath.read_text(encoding="utf-8"))
    tmpl_path = (
        template_path_for_podcast(data.get("podcast"))
        if template == str(ROOT / "config" / "template.yaml")
        else Path(template)
    )
    tmpl = load_template_config(tmpl_path)

    if not skip_validation:
        report = validate_summary(data, tmpl)
        rating = data.get("episode_rating", {}).get("overall")
        try:
            rating_int = int(rating)
            rating_valid = float(rating) == rating_int and 1 <= rating_int <= 5
        except (TypeError, ValueError):
            rating_valid = False
        if rating_valid:
            for issue in validate_rating_distribution(
                rating_int,
                tmpl,
                ROOT / "data" / "approved",
                podcast=data.get("podcast"),
                episode_id=episode if jpath.parent.name == "approved" else None,
            ):
                report.add(issue.section, issue.message, issue.severity)
        print_validation(report)
        if not report.passed:
            raise click.ClickException("Validation failed. Fix JSON or use --skip-validation.")

    md = render_summary(data, ROOT / "templates", template_cfg=tmpl)
    ep_num = data.get("metadata", {}).get("episode_number", episode)
    out = ROOT / "outputs" / f"EP{ep_num}_{episode}.md"
    save_summary(md, out)
    console.print(f"[green]Published[/green] {out}")
    sync_web_catalog()


@cli.command("run")
@click.option("--episode", "-e", required=True)
@click.option("--config", default=str(ROOT / "config" / "episodes.yaml"))
@click.option("--model", default=None)
@click.option("--skip-validation", is_flag=True)
def run_cmd(episode: str, config: str, model: str | None, skip_validation: bool) -> None:
    """Full pipeline: fetch → extract → validate → publish."""
    ctx = click.get_current_context()
    ctx.invoke(fetch_cmd, episode=episode, config=config)
    ctx.invoke(extract_cmd, episode=episode, config=config, model=model, transcript=None)
    jpath = str(ROOT / "data" / "drafts" / f"{episode}.json")
    if not skip_validation:
        ctx.invoke(validate_cmd, json_path=jpath, template=str(ROOT / "config" / "template.yaml"))
    ctx.invoke(
        publish_cmd,
        episode=episode,
        from_json=jpath,
        template=str(ROOT / "config" / "template.yaml"),
        skip_validation=skip_validation,
    )


@cli.command("batch-run")
@click.option("--discover", is_flag=True, help="Refresh episode list from Apple RSS + YouTube")
@click.option("--limit", type=int, default=None, help="Max episodes to process this run")
@click.option("--oldest-first", is_flag=True)
@click.option("--fetch-only", is_flag=True, help="Only fetch transcripts (no LLM)")
def batch_run_cmd(discover: bool, limit: int | None, oldest_first: bool, fetch_only: bool) -> None:
    """Batch process ILTB episodes with resume state at data/batch_state.json."""
    import subprocess

    if discover:
        subprocess.run([sys.executable, str(ROOT / "scripts" / "discover_iltb.py")], check=True)
    if fetch_only:
        subprocess.run([sys.executable, str(ROOT / "scripts" / "fetch_transcripts_batch.py")], check=True)
        return
    result = subprocess.run(
        [sys.executable, str(ROOT / "scripts" / "batch_pipeline.py")]
        + ([] if limit is None else ["--limit", str(limit)])
        + (["--oldest-first"] if oldest_first else []),
        cwd=str(ROOT),
    )
    if result.returncode != 0:
        raise SystemExit(result.returncode)


@cli.command("batch-acquired")
@click.option("--discover", is_flag=True, help="Refresh Acquired episode list from RSS")
@click.option("--fetch", is_flag=True, help="Fetch transcripts from acquired.fm")
@click.option("--publish", is_flag=True, help="Validate and publish all acq-* summaries")
@click.option("--limit", type=int, default=50)
def batch_acquired_cmd(discover: bool, fetch: bool, publish: bool, limit: int) -> None:
    """Batch Acquired: discover → fetch transcripts → publish approved JSON."""
    import subprocess

    cmd = [sys.executable, str(ROOT / "scripts" / "batch_acquired_pipeline.py"), "--limit", str(limit)]
    if discover:
        cmd.append("--discover")
    if fetch:
        cmd.append("--fetch")
    if publish:
        cmd.append("--publish")
    subprocess.run(cmd, cwd=str(ROOT), check=bool(cmd[2:]))


@cli.command("approve")
@click.option("--episode", "-e", required=True)
@click.option("--notes", default="", help="Human review notes appended to JSON")
def approve_cmd(episode: str, notes: str) -> None:
    """Move draft JSON to approved/ after human review."""
    draft = ROOT / "data" / "drafts" / f"{episode}.json"
    if not draft.exists():
        raise click.ClickException(f"No draft: {draft}")

    data = json.loads(draft.read_text(encoding="utf-8"))
    if notes:
        data["review_notes"] = notes
    data.setdefault("extraction_meta", {})["status"] = "approved"

    approved = ROOT / "data" / "approved" / f"{episode}.json"
    approved.parent.mkdir(parents=True, exist_ok=True)
    approved.write_text(json.dumps(data, indent=2, ensure_ascii=False), encoding="utf-8")
    console.print(f"[green]Approved[/green] → {approved}")


if __name__ == "__main__":
    from src.env import load_dotenv

    load_dotenv()
    cli()
