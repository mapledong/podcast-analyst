# Podcast Analyst

Automated pipeline for **Invest Like the Best** (and other) podcast summaries:

```
YouTube transcript → structured JSON (LLM) → human review → validated markdown
```

## Features

- **Fixed template v4.6** with word limits (`config/template.yaml`)
- **Top 3 investment implications** as numbered list (ticker, direction, confidence, thesis)
- **Validation** enforces section word caps before publish
- **Human review gate** via `drafts/` → `approved/` workflow

## Quick Start

```bash
cd ~/Projects/podcast-analyst
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt

export OPENAI_API_KEY=sk-...   # required for extract step
# Or: cp .env.example .env  (loaded automatically by pipeline + batch)

# Full pipeline for one episode
python src/pipeline.py run -e ep477

# Or step-by-step:
python src/pipeline.py fetch -e ep477
python src/pipeline.py extract -e ep477
# Edit data/drafts/ep477.json — add review_notes, fix facts
python src/pipeline.py approve -e ep477 --notes "Reviewed 2026-06-13"
python src/pipeline.py publish -e ep477
```

## Batch ILTB (5-year backfill)

Discovery + resume state live under `data/discovered/` and `data/batch_state.json`.

```bash
cp .env.example .env   # add OPENAI_API_KEY

# Process all YouTube-matched episodes (auto-resume, newest first)
python src/pipeline.py batch-run

# Smoke test
python src/pipeline.py batch-run --limit 3

# Refresh RSS + YouTube matching only
python src/pipeline.py batch-run --discover --fetch-only
```

**Note:** Apple RSS lists ~302 episodes since 2021-06-14, but `@ILTB_Podcast` only has ~57 YouTube uploads (~51 pending after ep475–477). Episodes without a YouTube match are skipped until audio transcription is added.

### Acquired batch (transcripts from acquired.fm)

```bash
# Discover 50 recent episodes, fetch transcripts, publish approved JSON
python src/pipeline.py batch-acquired --discover --fetch --publish

# Or step-by-step
python scripts/discover_acquired.py --limit 50
python scripts/fetch_acquired_transcripts_batch.py
# write data/approved/acq-*.json (manual or LLM with OPENAI_API_KEY)
python scripts/validate_acquired_batch.py --publish
```

Transcripts: `data/transcripts/acq-{slug}.txt` · Template: `config/template-acquired.yaml` (v5.1)

## Pipeline Steps

| Step | Command | Output |
|------|---------|--------|
| 1. Fetch | `fetch -e ep477` | `data/transcripts/<video_id>.txt` |
| 2. Extract | `extract -e ep477` | `data/drafts/ep477.json` |
| 3. Review | edit JSON + `approve -e ep477` | `data/approved/ep477.json` |
| 4. Publish | `publish -e ep477` | `outputs/EP477_ep477.md` + auto-syncs `web/` |

`publish` automatically runs `web/scripts/sync-content.mjs` so the library site stays current.

## Template v4.6 Structure

| Section | Notes |
|---------|-------|
| **Episode Rating** | Overall only (★ 1–5, whole stars) — single line under title |
| **Header meta** | Podcast, date, host, guest, duration, read time, listen links |
| **Conclusion** | Final takeaway blockquote |
| **Background** | Merged theme + guest story (one narrative arc) |
| Facts (F1–F3) | Objective, quantitative |
| **Mental Model** | Guest's signature framework |
| **Key Insights** | View + Q&A merged (3 blocks) |
| Top 3 Investment Implications | Numbered list (no ASCII table) |
| Golden Quotes | |
| **Chronology** | 5–10 dated milestones; excluded from word count |
| **Disclaimer** | Independent notes, rights, not advice, takedown |

**Target read time:** ~5 min (~900–1100 words).

## Add Episodes

Edit `config/episodes.yaml`:

```yaml
episodes:
  - id: ep474
    episode_number: 474
    title: "..."
    guest: "..."
    guest_role: "..."
    date: "2026-05-26"
    duration_minutes: 46
    youtube_url: "https://www.youtube.com/watch?v=..."
```

## Environment

| Variable | Default | Purpose |
|----------|---------|---------|
| `OPENAI_API_KEY` | — | Required for `extract` |
| `PODCAST_ANALYST_MODEL` | `gpt-4.1-mini` | Extraction model |

## Project Layout

```
config/template.yaml      # Section order & word limits
config/episodes.yaml      # Episode registry
prompts/extraction_system.txt
templates/summary.md.j2   # Markdown renderer
src/fetch_transcript.py
src/extract.py
src/validate.py
src/render.py
src/pipeline.py           # CLI entrypoint
data/transcripts/         # Raw YouTube transcripts
data/drafts/              # LLM output awaiting review
data/approved/            # Human-approved JSON
outputs/                  # Final markdown summaries
web/                      # Summary library site (Vite + React)
config/podcasts.yaml      # Podcast catalog for web UI
```

## Summary Library (Web)

Browse summaries in a local web UI — podcast covers, episode cards, full markdown rendering.

```bash
cd web
npm install
npm run dev      # syncs content + starts Vite at http://localhost:5173
npm run build    # production build to web/dist
npm run preview  # preview production build locally
```

**Features:** global search, Long/Short/Watch filters, dark mode toggle, local cover art, investment signal badges on episode cards.

**Deploy (static):**

```bash
cd web && npm run build
# Vercel: set root to web/ (vercel.json included)
# Netlify: publish directory web/dist (netlify.toml included)
```

### Public Deploy + Weekly Automation

This repo includes GitHub Actions for public hosting and scheduled updates:

| Workflow | Schedule | Purpose |
|---|---:|---|
| `deploy-pages.yml` | push to `main` | Builds `web/` and deploys to GitHub Pages |
| `nightly-content-update.yml` | Daily 01:00 Beijing | Discover new episodes, summarize (≤8/night), push to site |
| `weekly-digest.yml` | Friday 12:00 Beijing | Production weekly email (template v1) → `mapledong1996@hotmail.com` |
| `youtube-captions.yml` | 4× daily (small batches) | Extra YouTube caption fetch (2/podcast/run) |
| `weekly-update.yml` | Manual | Legacy backfill via Cursor SDK |
| `nightly-bb-founders.yml` | Manual | Legacy BB/Founders-only nightly (merged into nightly-content) |

To publish the site:

1. Push this repository to GitHub.
2. In GitHub, open **Settings → Pages** and set **Source** to **GitHub Actions**.
3. Run **Actions → Deploy Summary Library → Run workflow** once, or push to `main`.
4. Set repository variable `SITE_URL` to the final Pages URL (for example `https://<user>.github.io/<repo>/`) so weekly emails include the link.

Required GitHub secrets for weekly automation:

| Secret | Purpose |
|---|---|
| `CURSOR_API_KEY` | Lets `scripts/weekly_cursor_update.py` run a Cursor agent in GitHub Actions |
| `SMTP_HOST` | SMTP server for weekly email (for Outlook/Hotmail, usually `smtp.office365.com`) |
| `SMTP_PORT` | SMTP port, usually `587` |
| `SMTP_USER` | Sending mailbox |
| `SMTP_PASSWORD` | SMTP/app password for the mailbox |
| `SMTP_FROM` | From address, usually same as `SMTP_USER` |

Optional repository variable:

| Variable | Default | Purpose |
|---|---|---|
| `CURSOR_AGENT_MODEL` | `auto` | Cursor model for agent workflows (`auto`, `composer-2.5`, etc.) |

The weekly update workflow intentionally uses the Cursor SDK rather than the repo's OpenAI extraction scripts, so it does not require `OPENAI_API_KEY`. If you prefer OpenAI-based extraction later, add `OPENAI_API_KEY` and switch the workflow command to the existing batch scripts.

Podcast catalog: `config/podcasts.yaml` (ILTB, Acquired, Founders, Masters in Business).  
Local covers: `web/public/covers/*.svg` (optional remote upgrade via `cover_remote` in sync).  
Episodes sync from `config/episodes.yaml`, `data/approved/`, and `outputs/` via `web/scripts/sync-content.mjs`.

## Pre-built Summaries (EP.475–477)

Approved JSON and rendered markdown for the three most recent ILTB episodes are included as examples.

```bash
python src/pipeline.py validate --json data/approved/ep477.json
python src/pipeline.py publish -e ep477
```
