#!/usr/bin/env bash
# Validate SMTP GitHub secrets before send (does not print secret values).
set -euo pipefail

missing=0
for name in SMTP_HOST SMTP_USER SMTP_PASSWORD; do
  val="${!name:-}"
  if [ -z "${val// /}" ]; then
    echo "::error title=Missing SMTP secret::Add repository secret '$name' under Settings → Secrets and variables → Actions."
    missing=1
  fi
done
[ "$missing" -eq 0 ] || exit 1

clean="${SMTP_HOST// /}"
clean="${clean#https://}"
clean="${clean#http://}"
clean="${clean//\"/}"
clean="${clean%%/*}"
clean="${clean%%:*}"

if [[ "$clean" == *"@"* ]]; then
  echo "::error title=Wrong SMTP_HOST::SMTP_HOST must be smtp.gmail.com — not your email address (use SMTP_USER for that)."
  exit 1
fi

if [[ ! "$clean" =~ ^[a-zA-Z0-9][a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$ ]]; then
  echo "::error title=Invalid SMTP_HOST::Expected a hostname like smtp.gmail.com (length ${#clean}). Check for typos or extra characters in the secret."
  exit 1
fi

echo "SMTP secrets present."
echo "SMTP_HOST hostname OK (${#clean} chars)."
echo "SMTP_USER configured."
