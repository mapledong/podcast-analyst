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

## Weekly Saturday Update

Workflow: `.github/workflows/weekly-update.yml`

Schedule: every Saturday 10:00 Beijing time.

It runs a Cursor SDK agent that:

- discovers new episodes from existing podcast series,
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
CURSOR_AGENT_MODEL=gpt-5.5-medium
```

## Weekly Sunday Email

Workflow: `.github/workflows/weekly-digest.yml`

Schedule: every Sunday 12:00 Beijing time.

Recipient:

```text
mapledong1996@hotmail.com
```

Required secrets:

```text
SMTP_HOST=smtp.office365.com
SMTP_PORT=587
SMTP_USER=<sender email>
SMTP_PASSWORD=<smtp or app password>
SMTP_FROM=<sender email>
```

The email includes the new summaries added in the last 7 days: podcast, theme/title, guest/subject, conclusion, and investment ideas.

## YouTube transcript rate limits

Founders/BB YouTube caption fetches default to 3 episodes per run with 60s spacing and exponential backoff on 429/IP blocks (`scripts/fetch_founders_youtube.py --transcripts`, `scripts/fetch_curated_youtube.py --transcripts`). Use `--all` / `--full-queue` for the full pending queue.

## Nightly BB/Founders expansion

Workflow: `.github/workflows/nightly-bb-founders.yml`

Schedule: **daily 02:00 Beijing** (18:00 UTC). Target **5–10 summaries per night** (default 10; set repo variable `NIGHTLY_BATCH_SIZE`).

Uses `scripts/overnight_bb_founders.py` (Cursor SDK) to write summaries for episodes in the `--ready` queue (full transcript, not yet approved). Commits only:

```text
data/approved/**  outputs/**  web/src/data/**  config/episodes.yaml
```

**Never** `data/audio_cache/` or `*.mp3` (also in `.gitignore`).

Required secret: `CURSOR_API_KEY` (same as weekly update).

Manual run: **Actions → Nightly BB/Founders Expansion → Run workflow**.

### Local Mac (optional)

If the Mac mini stays on overnight:

```bash
chmod +x scripts/install-overnight-launchd.sh scripts/overnight-local.sh
# CURSOR_API_KEY in .env
./scripts/install-overnight-launchd.sh
```

Logs: `tmp/overnight-logs/`. Prefer GitHub Actions if the machine sleeps at night.

Current curated progress: `python scripts/resolve_curated_bb_founders.py --stats`
