#!/usr/bin/env bash
# Local nightly BB/Founders expansion + safe push (no mp3).
set -euo pipefail

ROOT="$(cd "$(dirname "$0")/.." && pwd)"
cd "$ROOT"

if [[ -f .env ]]; then
  set -a
  # shellcheck disable=SC1091
  source .env
  set +a
fi

export NIGHTLY_BATCH_SIZE="${NIGHTLY_BATCH_SIZE:-10}"
PY="${PY:-$ROOT/.venv/bin/python3}"
[[ -x "$PY" ]] || PY=python3

"$PY" scripts/overnight_bb_founders.py
"$PY" scripts/normalize_summary_tickers.py --publish || true
node web/scripts/sync-content.mjs

chmod +x scripts/verify_no_mp3_in_commit.sh
git add data/approved outputs web/src/data config/episodes.yaml
git reset HEAD -- 'data/audio_cache' '*.mp3' 2>/dev/null || true
./scripts/verify_no_mp3_in_commit.sh

if git diff --cached --quiet; then
  echo "No changes to commit."
  exit 0
fi

git commit -m "Nightly BB/Founders summaries (local)"
git push origin main
