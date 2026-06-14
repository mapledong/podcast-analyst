#!/usr/bin/env bash
# Fail if staged files include mp3 or audio_cache (used before nightly commit).
set -euo pipefail

bad=$(git diff --cached --name-only | grep -E '(^data/audio_cache/|\.mp3$)' || true)
if [[ -n "$bad" ]]; then
  echo "ERROR: refusing commit — mp3/audio_cache must not be pushed:" >&2
  echo "$bad" >&2
  exit 1
fi
echo "OK: no mp3 or audio_cache in staged files"
