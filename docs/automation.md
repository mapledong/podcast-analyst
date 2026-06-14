# Public Site and Weekly Automation

## Deploy without Homebrew (Mac mini / no `brew`)

If `brew` and `gh` are not installed, use the bundled deploy script (downloads portable `gh` if needed):

```bash
cd /Users/maple/Projects/podcast-analyst
chmod +x scripts/deploy-github.sh
./scripts/deploy-github.sh
```

First run will prompt you to authenticate once:

```bash
/tmp/gh-extract/gh_2.74.2_macOS_arm64/bin/gh auth login
# or whatever path the script prints
```

**Alternative (no CLI):** create an empty public repo `podcast-analyst` on github.com, then:

```bash
git remote add origin https://github.com/mapledong/podcast-analyst.git
git push -u origin main
```

Enable **Settings → Pages → Source: GitHub Actions**, then run **Deploy Summary Library** from the Actions tab.

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


## Deploy without Homebrew (Mac mini)

If `brew` and `gh` are not installed, use the repo deploy script. It uses Apple **git** (already at `/usr/bin/git`) and optionally downloads **gh** into `.local/bin` (no Homebrew).

### One-time setup

1. **Create the GitHub repo** (pick one):
   - Browser: [Create repository](https://github.com/new?name=podcast-analyst) named `podcast-analyst` under **mapledong** (public, no README).
   - Or install gh locally and log in:
     ```bash
     cd ~/Projects/podcast-analyst
     INSTALL_GH=1 ./scripts/deploy-github.sh --check
     ./.local/bin/gh auth login
     ```

2. **Authenticate git to GitHub** (pick one):
   - **SSH (recommended):** add `~/.ssh/id_ed25519.pub` at [SSH keys](https://github.com/settings/keys), then:
     ```bash
     ssh-keyscan github.com >> ~/.ssh/known_hosts
     ssh -T git@github.com
     ```
   - **HTTPS:** create a [Personal Access Token](https://github.com/settings/tokens) with `repo` scope; use it as the password when git prompts.

3. **Optional PATH** (only if you use the downloaded gh often):
   ```bash
   echo 'export PATH="$HOME/Projects/podcast-analyst/.local/bin:$PATH"' >> ~/.zshrc
   source ~/.zshrc
   ```

### Push and publish

```bash
cd ~/Projects/podcast-analyst
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

After a successful push, enable **Settings → Pages → Source: GitHub Actions**, then run **Actions → Deploy Summary Library** once. Live site:

```text
https://mapledong.github.io/podcast-analyst/
```

See also `scripts/deploy-github.sh --help` and env vars `INSTALL_GH`, `USE_HTTPS`, `CREATE_REPO`.
