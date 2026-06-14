# Acquired expansion / optimization instructions (v5.4-acquired)

## Authenticity — NON-NEGOTIABLE
- Read the full transcript before editing (`src.expand.resolve_transcript_path`).
- Use ONLY facts, numbers, and quotes from the transcript.
- Do NOT invent statistics, dates, tickers, or company milestones.
- Do NOT contradict accurate claims already in the summary.
- Golden quotes must be transcript-grounded.
- `competitive_advantage` (What Makes It Work) must reflect moats/weaknesses stated in the episode — not generic MBA filler.

## Prose style — NON-NEGOTIABLE
- Human analyst voice; no AI padding to hit word counts.
- No: "it's worth noting", "delve", "underscores", "Transcript line:", "This maps to".
- Do not duplicate the same sentence across Background, Key Facts, Mental Model, and What Makes It Work.
- Key Facts: one idea per sentence; each of 5 facts must include a number from the transcript.

## Files
- Summary: `data/approved/{episode_id}.json`
- Transcript: `data/transcripts/acq-{slug}.txt` or `{episode_id}.txt`

## Preserve unchanged
- `episode_id`, `podcast`, `host`, `metadata`, `episode_rating.overall`

## Word targets (200 wpm)
- < 90 min → total ≥ 900, target 900–1100
- 90–179 min → total ≥ 1000, target 1000–1600
- 180+ min → total ≥ 1600, target 1600–2200

## Sections (priority order)
1. `important_facts` — exactly 5 items with numbers; 300–800 words combined
2. `competitive_advantage` — moat analysis; up to 580 words
3. `mental_model` — 150–520 words
4. `key_insights` — exactly 5; deepen answers toward 150 words
5. `conclusion` — 60–180 words
6. `background` — max 300 words; scene-setting only

## Investment ideas
- 1–3 rows; prefer Long/Short on tradable tickers cited in the episode
- Max one Watch; use Long/Short (not Watch) for tradable names when thesis is directional

## After each episode
```bash
python -c "
import json; from pathlib import Path
from src.validate import validate_summary, load_template_config, word_gap
from src.template_config import template_path_for_podcast
p=Path('data/approved/EPISODE_ID.json'); d=json.loads(p.read_text())
t=load_template_config(template_path_for_podcast('Acquired')); r=validate_summary(d,t)
print(r.total_words,'/',r.min_total_words,'gap',word_gap(d,t))
[w for w in r.issues if w.severity=='warning']
"
python scripts/publish_approved_batch.py EPISODE_ID
```

Append to `review_notes`: `| optimized v5.4`
