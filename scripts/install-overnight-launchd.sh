#!/usr/bin/env bash
# Install local nightly job (Mac). Requires: CURSOR_API_KEY in .env, Mac awake ~2am.
set -euo pipefail

ROOT="$(cd "$(dirname "$0")/.." && pwd)"
PLIST="$HOME/Library/LaunchAgents/com.podcast-analyst.nightly.plist"
LOG_DIR="$ROOT/tmp/overnight-logs"
mkdir -p "$LOG_DIR"

cat > "$PLIST" <<EOF
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
  <key>Label</key>
  <string>com.podcast-analyst.nightly</string>
  <key>ProgramArguments</key>
  <array>
    <string>/bin/bash</string>
    <string>$ROOT/scripts/overnight-local.sh</string>
  </array>
  <key>StartCalendarInterval</key>
  <dict>
    <key>Hour</key>
    <integer>2</integer>
    <key>Minute</key>
    <integer>0</integer>
  </dict>
  <key>StandardOutPath</key>
  <string>$LOG_DIR/nightly.log</string>
  <key>StandardErrorPath</key>
  <string>$LOG_DIR/nightly.err</string>
  <key>WorkingDirectory</key>
  <string>$ROOT</string>
</dict>
</plist>
EOF

launchctl unload "$PLIST" 2>/dev/null || true
launchctl load "$PLIST"
echo "Installed: $PLIST (runs daily at 02:00 local time)"
echo "Logs: $LOG_DIR/"
echo "Requires CURSOR_API_KEY in $ROOT/.env and Mac not sleeping at 2am."
echo "Prefer GitHub Actions nightly if the Mac is off overnight."
