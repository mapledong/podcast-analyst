# BB / Founders summary build instructions (template v4.10)

## Selection (long-term pool)
- Target **80+ episodes per podcast**; prioritize **public companies (上市公司)** and **unicorn startups (一级市场独角兽)**; prefer episodes with an existing **full transcript** before Whisper.

## Authenticity — NON-NEGOTIABLE
- Read transcript before writing (`data/transcripts/{prefix}-{slug}.txt` or episode_id).
- Use ONLY facts, numbers, and quotes from transcript or episode show notes.
- Do NOT invent statistics, dates, tickers, or milestones.
- Golden quotes must be transcript-grounded (paraphrase OK if faithful).

## Prose style
- Human analyst voice; no AI padding ("it's worth noting", "delve", "underscores").
- No duplicate sentences across Background, Key Facts, Mental Model.
- Key Facts: exactly 3 items, each with at least one number from transcript.

## Files
- Output: `data/approved/{episode_id}.json`
- Transcript prefix: `bb-` (Business Breakdowns), `fnd-` (Founders)
- Template: `config/template.yaml` v4.10 (standard profile)

## Metadata
- `podcast`: "Business Breakdowns" or "Founders"
- BB host: "Matt Reustle & Zack Fuss"; Founders host: "David Senra"
- Copy `episode_number`, `title`, `date`, `duration_minutes`, `colossus_url`, `youtube_url`, `audio_url` from discovered JSON
- BB `guest` = company name; `guest_role` = "Public · TICKER" or "Private · description"
- Founders `guest` = subject; `guest_role` = "Biography · Episode N"

## Word targets @ 200 wpm
- <60 min → total ≥ 700
- <90 min → total ≥ 900
- 90–179 min → total ≥ 1000

## Sections
1. `important_facts` — 3 items, 200–500 words combined, numbers required
2. `mental_model` — name + components + application, 150–420 words
3. `key_insights` — 3 Q&A pairs
4. `top_investment_implications` — 1–3 tickers; Long/Short preferred over Watch for tradable names
5. `golden_quotes` — 3 items
6. `chronology` — 5–10 events
7. `conclusion` — 40–100 words
8. `background` — max 220 words
9. `keywords` — 3–4 items; public companies as US tickers (NVDA, COST, LVMUY), not names

## Keywords / tickers
- `keywords` and investment `ticker` fields must use standard US ticker symbols for public companies
- Use company names only for private entities (`Private:Name`), people, or industry themes
- Foreign listings: prefer US ADR (e.g. LVMUY not MC.PA; RACE for Ferrari)

## Rating
- Use 3–5 stars; library caps 5★ ≤20%, 4★ ≤30% per podcast (check `scripts/report_rating_distribution.py`)

## After each episode
```bash
python scripts/publish_approved_batch.py EPISODE_ID
```
Append to `review_notes`: `| curated v4.10`

## Transcribe if missing

Priority order for curated episodes:
1. **YouTube** — Founders: `python3 scripts/fetch_founders_youtube.py --transcripts` (default **2/run**, **90s** delay + jitter); BB: `python3 scripts/fetch_curated_youtube.py --transcripts` (same). **Never bulk-fetch** (`--all` / `--full-queue` blocked unless `YOUTUBE_CAPTION_BULK_OK=1`). Prefer the scheduled `youtube-captions.yml` workflow (4× daily, 2 episodes each).
2. **Whisper** — only for YouTube-linked episodes still missing full transcript, or explicit IDs:
   ```bash
   python3 scripts/transcribe_colossus_audio.py EPISODE_ID
   python3 scripts/transcribe_from_cache.py EPISODE_ID
   ```
3. **Skip** non-YouTube episodes without a full transcript (do not run Whisper by default).

Check gaps: `python3 scripts/resolve_curated_bb_founders.py --stats`
Ready to summarize: `python3 scripts/resolve_curated_bb_founders.py --ready`
