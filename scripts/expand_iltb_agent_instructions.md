# ILTB expansion instructions (v4.10)

## Authenticity — NON-NEGOTIABLE
- Read the full YouTube transcript for each episode before editing.
- Use ONLY facts, numbers, and quotes that appear in the transcript.
- Do NOT invent statistics, dates, deals, or guest statements.
- Do NOT contradict the existing summary's accurate claims.
- Golden quotes must be traceable to transcript dialogue (paraphrase OK, fabrication NOT OK).
- When expanding, pull additional detail FROM THE TRANSCRIPT — not from general knowledge.

## Prose style — NON-NEGOTIABLE
- Sound like a human analyst wrote a proper summary — not an AI padding word counts.
- Use plain, direct sentences. Vary length. Prefer concrete names and numbers over abstract framing.
- Do NOT use: "it's worth noting", "delve", "underscores", "at its core", "In [Name]'s framing", "Moreover/Furthermore".
- Do NOT stack buzzwords: playbook, leverage, unlock, ecosystem, holistic, landscape, robust, paradigm.
- Do NOT paste the same fact or phrase into Background, Key Facts, and Mental Model to hit limits.
- Do NOT leave transcript junk ("Transcript line:", "This maps to …") in any field.
- Key Facts: one idea per sentence; reads like a research note, not a bulleted essay template.
- Mental Model: explain the idea in your own words — not a stitched list of insight titles.

## Files
- Summary: `data/approved/{episode_id}.json`
- Transcript: resolve via `src.expand.resolve_transcript_path(data)` — usually `data/transcripts/{youtube_video_id}.txt`

## Preserve unchanged
- `episode_id`, `podcast`, `host`, `metadata`, `episode_rating.overall`

## Word targets by episode duration (200 wpm)
- < 90 min → total counted words ≥ 900, target 900–1100
- 90–179 min → total counted words ≥ 1000, target 1000–1600
- 180+ min → total counted words ≥ 1600

## Sections to deepen (priority order)
1. `important_facts` — 3 items, each with a number; target 200–500 words combined
2. `mental_model` — components + application; target 150–420 words total
3. `key_insights[].answer` — longer, with logic and numbers from transcript
4. `conclusion` — 40–100 words
5. `background` — max 220 words; brief scene-setting only; last resort for word gap

## Investment ideas
- 1–3 rows; prefer Long/Short on tradable tickers
- Max one Watch per episode; change Watch to Long/Short when transcript supports directional view

## After each episode
```bash
cd /Users/maple/Projects/podcast-analyst
python -c "
import json
from pathlib import Path
from src.validate import validate_summary, load_template_config, word_gap
from src.template_config import template_path_for_podcast
data = json.loads(Path('data/approved/EPISODE_ID.json').read_text())
tmpl = load_template_config(template_path_for_podcast(data['podcast']))
r = validate_summary(data, tmpl)
print(r.total_words, '/', r.min_total_words, 'gap', word_gap(data, tmpl))
for i in r.issues:
    if i.severity=='warning': print(i.section, i.message)
"
```

## extraction_meta
Append to review_notes: `| expanded agent v4.10`
Update extraction_meta with `"expanded_by": "agent-v4.10"`.
