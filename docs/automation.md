# Public Site and Weekly Automation

## Deploy without Homebrew (Mac mini)

Homebrew is optional. Apple **git** (`/usr/bin/git`) is enough to publish. The deploy script can also download **gh** into `.local/bin` (gitignored) if you want `gh repo create` / `gh auth login` without `brew`.

### One-time setup

1. **Create the GitHub repo** (pick one):
   - Browser: [Create repository](https://github.com/new?name=podcast-analyst) named `podcast-analyst` under **mapledong** (public, empty — no README).
   - Or install gh locally and log in:
     ```bash
     cd ~/Projects/podcast-analyst
     INSTALL_GH=1 ./scripts/deploy-github.sh --check
     ./.local/bin/gh auth login
     ```

2. **Authenticate git to GitHub** (pick one):
   - **HTTPS + gh (easiest if you already use `gh auth login`):**
     ```bash
     gh auth setup-git
     ```
     Then run `./scripts/deploy-github.sh` (or `USE_HTTPS=1 ./scripts/deploy-github.sh`). If SSH is not configured on GitHub, the script falls back to HTTPS automatically when `gh` is logged in.
   - **SSH:** add `~/.ssh/id_ed25519.pub` at [SSH keys](https://github.com/settings/keys), then:
     ```bash
     ssh-keyscan github.com >> ~/.ssh/known_hosts
     ssh -T git@github.com
     ```
   - **HTTPS + PAT:** create a [Personal Access Token](https://github.com/settings/tokens) with `repo` scope; use it as the password when git prompts.

3. **Optional PATH** (if you use the downloaded gh often):
   ```bash
   echo 'export PATH="$HOME/Projects/podcast-analyst/.local/bin:$PATH"' >> ~/.zshrc
   source ~/.zshrc
   ```

### Push and publish

```bash
cd ~/Projects/podcast-analyst
chmod +x scripts/deploy-github.sh
./scripts/deploy-github.sh
```

If the repo was created in the browser and you do not use `gh`:

```bash
CREATE_REPO=0 ./scripts/deploy-github.sh
```

HTTPS instead of SSH:

```bash
USE_HTTPS=1 ./scripts/deploy-github.sh
```

After a successful push, enable **Settings → Pages → Source: GitHub Actions**, then trigger deploy once:

```bash
gh workflow run "Deploy Summary Library" --ref main
```

Or use **Actions → Deploy Summary Library → Run workflow**. Live site:

```text
https://mapledong.github.io/podcast-analyst/
```

See `scripts/deploy-github.sh --help` and env vars `INSTALL_GH`, `USE_HTTPS`, `CREATE_REPO`.

## Public Site

The site is deployed by `.github/workflows/deploy-pages.yml` to GitHub Pages.

1. Push the repository to GitHub.
2. In GitHub repository settings, enable **Pages → Source: GitHub Actions**.
3. Run **Actions → Deploy Summary Library** once.
4. The default URL is:

```text
https://<github-user>.github.io/<repo>/
```

For the default GitHub Pages path, no extra config is needed. If you use a custom domain, set repository variable:

```text
BASE_PATH=/
SITE_URL=https://your-domain.com/
```

## Nightly content update (01:00 Beijing)

Workflow: `.github/workflows/nightly-content-update.yml`

**Schedule:** every night **01:00 Beijing** (17:00 UTC).

Pipeline each night:

1. **Discover** new episodes — ILTB, Acquired, BB/Founders RSS (`discover_*.py`)
2. **Summarize** up to **8** episodes (default `NIGHTLY_BATCH_SIZE`):
   - Priority: **new releases** (past 7 days) with full transcript
   - Then: BB/Founders expand-pool backlog (`resolve_curated_bb_founders.py --ready`)
3. **Publish** — validate, sync web, commit + push → GitHub Pages deploy

YouTube captions are handled separately by `youtube-captions.yml` (4× daily, slow batch).

This keeps the **Friday 12:00 weekly digest** fed with the past week's episode dates.

Scripts: `scripts/report_new_episodes.py`, `scripts/nightly_content_update.py`

Required secret: `CURSOR_API_KEY`

Manual run: Actions → **Nightly Content Update**

### Legacy workflows (manual only)

- `weekly-update.yml` — large backfill via Cursor (formerly Saturday)
- `nightly-bb-founders.yml` — BB/Founders-only expansion (merged into nightly)

## Weekly Saturday Update (manual backfill)

Workflow: `.github/workflows/weekly-update.yml` (no schedule — use **Nightly Content Update** instead)

When run manually, it:
- creates transcript-grounded summaries,
- publishes approved JSON and markdown,
- normalizes company tickers,
- syncs the web catalog,
- commits changes back to `main`.

Required secret:

```text
CURSOR_API_KEY
```

Optional repository variable:

```text
CURSOR_AGENT_MODEL=auto
```

Use `auto` (server picks model; lower cost) or `composer-2.5` (faster, predictable). Override via repo variable if needed.

## Weekly Friday Email (template v1)

Workflow: `.github/workflows/weekly-digest.yml`  
Template config: `config/weekly_digest.yaml`  
Renderer: `scripts/weekly_digest_render.py`

**Schedule:** every **Friday 12:00 Beijing** (04:00 UTC). Production sends use template v1 with no `[Trial]` banner.

### Template layout

1. **Header** — Podcast Analyst · Weekly Update · episode date range  
2. **Merged index** — episode count, podcast tags, numbered list (title + guest with **org / title** from `metadata.guest_role`)  
3. **Details** — one card per episode: Conclusion, Investment Ideas (Long/Short badges), link to site  

**Filter:** episodes whose **`metadata.date`** (publish date) falls in the past **7 days** — not git commit time. If none match, the email says so and still sends.

**Subject:** `Podcast Analyst 周报 · N 期 · MM/DD–MM/DD`

Preview locally:

```bash
python scripts/send_weekly_digest.py --preview-html tmp/weekly_digest_preview.html
open tmp/weekly_digest_preview.html
```

Manual test (optional `[Trial]` banner): Actions → **Weekly Summary Digest Email** → Run workflow, check **Preview mode** only for tests.

### SMTP secrets

| Secret | Gmail example |
|--------|----------------|
| `SMTP_HOST` | `smtp.gmail.com` |
| `SMTP_PORT` | `587` |
| `SMTP_USER` | `alex.dongrufeng@gmail.com` |
| `SMTP_PASSWORD` | 16-char **App Password** (not login password) |
| `SMTP_FROM` | `alex.dongrufeng@gmail.com` |
| `WEEKLY_DIGEST_TO` | `mapledong1996@hotmail.com` (optional; defaults to hotmail) |

Secret names must match **exactly** (case-sensitive). Common mistakes:

- `SMTP_HOST` = your **email** → wrong; use `smtp.gmail.com`
- `SMTP_HOST` = `https://smtp.gmail.com` → wrong; no `https://`
- `SMTP_PASSWORD` = Gmail **login password** → wrong; use **App Password**

If `SMTP_HOST` is invalid, the workflow fails with `Name or service not known`.

**Gmail:** enable 2-Step Verification, then create an App Password at https://myaccount.google.com/apppasswords

Repository secrets (Settings → Secrets and variables → **Actions**):

YouTube caption fetches are **conservative by design** to avoid 429 / IP blocks:

| Setting | Default |
|---|---|
| Episodes per run | **2** (`YOUTUBE_CAPTION_BATCH_SIZE`) |
| Delay between episodes | **90s** + 8–30s random jitter |
| Backoff on failure | 90s → 180s → 360s (max 3 retries) |

**Do not bulk-fetch.** `--all` (Founders) and `--full-queue` (BB) are **blocked** unless you explicitly set `YOUTUBE_CAPTION_BULK_OK=1` for a one-off local run.

**Scheduled slow batch:** `.github/workflows/youtube-captions.yml` runs **4× daily** (Beijing ~05:00 / 11:00 / 17:00 / 23:00), **2 captions per podcast per run** (~16 new transcripts/day max). Manual:

```bash
python scripts/fetch_founders_youtube.py --transcripts   # 2 Founders, then stop
python scripts/fetch_curated_youtube.py --transcripts    # 2 BB, then stop
```

The **nightly summary job does not fetch captions** — it only writes summaries for episodes that already have transcripts.

## Nightly BB/Founders expansion

Workflow: `.github/workflows/nightly-bb-founders.yml`

**Long-term goal:** **80+ approved summaries per podcast** (Business Breakdowns + Founders). Expanded pool: `config/curated_bb_founders.yaml` (30 each) plus `config/expand_bb_founders.yaml` / auto-fill from `data/discovered/*.json` to `TARGET_PER_PODCAST` (default **80**).

**Selection policy:** prioritize **public companies (上市公司)** and **unicorn startups (一级市场独角兽)**; within the pool prefer episodes with a **full transcript** already in `data/transcripts/` (fetch YouTube captions before Whisper).

Schedule: **daily 02:00 Beijing** (18:00 UTC). Target **5–10 summaries per night** (default 10; set repo variable `NIGHTLY_BATCH_SIZE`).

Long-term goal: **80+ high-quality approved summaries per podcast** (Business Breakdowns + Founders). The nightly pool is `config/curated_bb_founders.yaml` (30 curated each) plus `config/expand_bb_founders.yaml` (fills to `target_per_podcast: 80`).

**Transcript-first policy:** episodes with a full transcript in `data/transcripts/` are summarized first. YouTube caption fetch is the fallback for pool episodes with a `youtube_url` but no transcript yet. Avoid Whisper in the nightly job unless no other source exists (run Whisper locally via `scripts/batch_bb_founders_pipeline.py --transcribe`).

Uses `scripts/overnight_bb_founders.py` (Cursor SDK) to write summaries for episodes from `resolve_curated_bb_founders.py --ready --limit N`. Commits only:

```text
data/approved/**  outputs/**  web/src/data/**  config/episodes.yaml
```

**Never** push podcast audio: `data/audio_cache/`, `*.mp3`, `*.m4a`, or other audio formats (all in `.gitignore`). Download audio locally for Whisper only; publish summary JSON/markdown to GitHub Pages.

Required secret: `CURSOR_API_KEY` (same as weekly update).

Optional repository variables:

| Variable | Default | Purpose |
|---|---|---|
| `NIGHTLY_BATCH_SIZE` | `10` | Max summaries per nightly run |
| `TARGET_PER_PODCAST` | `80` | Expanded pool size per podcast |

Manual run: **Actions → Nightly BB/Founders Expansion → Run workflow**.

### Pool progress and refresh

```bash
python scripts/resolve_curated_bb_founders.py --stats
python scripts/resolve_curated_bb_founders.py --ready --limit 10
```

Stats fields: `approved` / `target` / `ready_with_transcript` / `ready_total`, plus `youtube_no_transcript` and `needs_transcribe` for backlog.

Refresh the expand list after RSS discovery or new transcripts:

```bash
python scripts/discover_colossus_podcasts.py --founders-youtube   # optional: refresh RSS
python scripts/refresh_expand_bb_founders.py                      # rewrite expand yaml extras
python scripts/fetch_founders_youtube.py --transcripts            # 2/run — rerun or use workflow
python scripts/fetch_curated_youtube.py --transcripts           # 2/run — rerun or use workflow
```

See **YouTube caption rate limits** above; prefer `youtube-captions.yml` over manual loops.

Edit `config/curated_bb_founders.yaml` to change the core 30; edit `target_per_podcast` or per-episode `episode_number` entries in `config/expand_bb_founders.yaml` for manual overrides.

### Local Mac (optional)

If the Mac mini stays on overnight:

```bash
chmod +x scripts/install-overnight-launchd.sh scripts/overnight-local.sh
# CURSOR_API_KEY in .env
./scripts/install-overnight-launchd.sh
```

Logs: `tmp/overnight-logs/`. Prefer GitHub Actions if the machine sleeps at night.

Current expanded pool progress: `python scripts/resolve_curated_bb_founders.py --stats`
