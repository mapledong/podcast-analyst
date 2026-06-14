# Public Site and Weekly Automation

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

