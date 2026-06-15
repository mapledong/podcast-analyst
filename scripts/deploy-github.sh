#!/usr/bin/env bash
# Push podcast-analyst to GitHub and print GitHub Pages setup steps.
# Works without Homebrew: optional local gh install, or pure git.
set -euo pipefail

GITHUB_OWNER="${GITHUB_OWNER:-mapledong}"
GITHUB_REPO="${GITHUB_REPO:-podcast-analyst}"
GITHUB_REMOTE_SSH="git@github.com:${GITHUB_OWNER}/${GITHUB_REPO}.git"
GITHUB_REMOTE_HTTPS="https://github.com/${GITHUB_OWNER}/${GITHUB_REPO}.git"
PAGES_URL="https://${GITHUB_OWNER}.github.io/${GITHUB_REPO}/"
BRANCH="${DEPLOY_BRANCH:-main}"

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
REPO_ROOT="$(cd "${SCRIPT_DIR}/.." && pwd)"
LOCAL_BIN="${REPO_ROOT}/.local/bin"
INSTALL_GH="${INSTALL_GH:-0}"
USE_HTTPS="${USE_HTTPS:-0}"
CREATE_REPO="${CREATE_REPO:-1}"

info() { printf '==> %s\n' "$*"; }
warn() { printf 'warning: %s\n' "$*" >&2; }
die() { printf 'error: %s\n' "$*" >&2; exit 1; }

machine_arch() {
  local arch
  arch="$(uname -m)"
  case "$arch" in
    arm64) echo "arm64" ;;
    x86_64) echo "amd64" ;;
    *) die "unsupported CPU architecture: $arch" ;;
  esac
}

find_gh() {
  local candidate
  for candidate in \
    "${GH_BIN:-}" \
    "$(command -v gh 2>/dev/null || true)" \
    "${LOCAL_BIN}/gh" \
    "${HOME}/.local/bin/gh" \
    /opt/homebrew/bin/gh \
    /usr/local/bin/gh; do
    [[ -n "$candidate" && -x "$candidate" ]] || continue
    printf '%s\n' "$candidate"
    return 0
  done
  return 1
}

install_gh_to() {
  local dest_dir="$1"
  local arch gh_arch zip_name url tmpdir version
  arch="$(machine_arch)"
  gh_arch="$arch"
  [[ "$arch" == "amd64" ]] && gh_arch="amd64"
  mkdir -p "$dest_dir"
  version="$(curl -fsSL https://api.github.com/repos/cli/cli/releases/latest \
    | python3 -c "import sys,json; print(json.load(sys.stdin)['tag_name'].lstrip('v'))")"
  zip_name="gh_${version}_macOS_${gh_arch}.zip"
  url="https://github.com/cli/cli/releases/download/v${version}/${zip_name}"
  tmpdir="$(mktemp -d)"
  trap 'rm -rf "$tmpdir"' RETURN
  info "Downloading gh v${version} (${gh_arch})…"
  curl -fsSL -o "${tmpdir}/gh.zip" "$url"
  unzip -o -q "${tmpdir}/gh.zip" -d "${tmpdir}/extract"
  cp "${tmpdir}/extract/${zip_name%.zip}/bin/gh" "${dest_dir}/gh"
  chmod +x "${dest_dir}/gh"
  info "Installed gh to ${dest_dir}/gh"
}

ensure_gh() {
  local gh_bin
  if gh_bin="$(find_gh)"; then
    printf '%s\n' "$gh_bin"
    return 0
  fi
  if [[ "$INSTALL_GH" == "1" ]]; then
    install_gh_to "$LOCAL_BIN"
    printf '%s\n' "${LOCAL_BIN}/gh"
    return 0
  fi
  return 1
}

ensure_github_host_key() {
  if [[ -f "${HOME}/.ssh/known_hosts" ]] && grep -q '^github.com ' "${HOME}/.ssh/known_hosts" 2>/dev/null; then
    return 0
  fi
  info "Adding github.com to ~/.ssh/known_hosts (first connect)…"
  mkdir -p "${HOME}/.ssh"
  chmod 700 "${HOME}/.ssh"
  ssh-keyscan -t ed25519,rsa github.com >> "${HOME}/.ssh/known_hosts" 2>/dev/null || true
}

remote_url() {
  if [[ "$USE_HTTPS" == "1" ]]; then
    printf '%s\n' "$GITHUB_REMOTE_HTTPS"
  else
    printf '%s\n' "$GITHUB_REMOTE_SSH"
  fi
}

ensure_git_repo() {
  cd "$REPO_ROOT"
  git rev-parse --git-dir >/dev/null 2>&1 || die "not a git repository: $REPO_ROOT"
  git show-ref --verify --quiet "refs/heads/${BRANCH}" || die "branch '${BRANCH}' does not exist locally"
}

configure_remote() {
  local url
  url="$(remote_url)"
  cd "$REPO_ROOT"
  if git remote get-url origin >/dev/null 2>&1; then
    local current
    current="$(git remote get-url origin)"
    if [[ "$current" != "$url" ]]; then
      info "Updating origin: $current -> $url"
      git remote set-url origin "$url"
    else
      info "origin already set: $url"
    fi
  else
    info "Adding origin: $url"
    git remote add origin "$url"
  fi
}

align_git_with_gh_auth() {
  local gh_bin="$1"
  "$gh_bin" auth setup-git --hostname github.com >/dev/null 2>&1 || true
  local protocol
  protocol="$("$gh_bin" config get git_protocol -h github.com 2>/dev/null || echo ssh)"
  if [[ "$protocol" == "https" && "$USE_HTTPS" != "1" ]]; then
    info "gh authenticated with HTTPS; using HTTPS remote for push"
    USE_HTTPS=1
    configure_remote
  fi
}

maybe_create_repo() {
  local gh_bin="$1"
  [[ "$CREATE_REPO" == "1" ]] || return 0
  if "$gh_bin" repo view "${GITHUB_OWNER}/${GITHUB_REPO}" >/dev/null 2>&1; then
    info "GitHub repo ${GITHUB_OWNER}/${GITHUB_REPO} already exists"
    return 0
  fi
  info "Creating public repo ${GITHUB_OWNER}/${GITHUB_REPO} on GitHub…"
  local -a create_args=(
    repo create "${GITHUB_OWNER}/${GITHUB_REPO}"
    --public
    --source="$REPO_ROOT"
    --push=false
    --description "Podcast summary library (GitHub Pages)"
  )
  if git remote get-url origin >/dev/null 2>&1; then
    info "origin already configured locally; creating repo without --remote=origin"
  else
    create_args+=(--remote=origin)
  fi
  "$gh_bin" "${create_args[@]}"
}

DEPLOY_WORKFLOW_NAME="${DEPLOY_WORKFLOW_NAME:-Deploy Summary Library}"

maybe_trigger_deploy() {
  local gh_bin="$1"
  [[ "${TRIGGER_DEPLOY:-1}" == "1" ]] || return 0
  if "$gh_bin" workflow run "$DEPLOY_WORKFLOW_NAME" --ref "${BRANCH}" >/dev/null 2>&1; then
    info "Triggered workflow: ${DEPLOY_WORKFLOW_NAME}"
  else
    warn "Could not trigger workflow '${DEPLOY_WORKFLOW_NAME}' (push may still start deploy if paths match)"
  fi
}

test_ssh_github() {
  ensure_github_host_key
  ssh -o BatchMode=yes -o ConnectTimeout=10 -T git@github.com 2>&1 | grep -qi 'successfully authenticated' && return 0
  return 1
}

push_main() {
  cd "$REPO_ROOT"
  info "Pushing ${BRANCH} to origin…"
  git push -u origin "${BRANCH}"
}

print_pages_steps() {
  cat <<EOF

----------------------------------------------------------------------
Next steps (GitHub Pages + automation)
----------------------------------------------------------------------
1. Open: https://github.com/${GITHUB_OWNER}/${GITHUB_REPO}/settings/pages
   Set **Build and deployment → Source: GitHub Actions**.

2. Trigger first deploy:
   https://github.com/${GITHUB_OWNER}/${GITHUB_REPO}/actions/workflows/deploy-pages.yml
   Click **Run workflow** (or push a change under web/, data/approved/, etc.).

3. Site URL (after deploy succeeds):
   ${PAGES_URL}

4. Repository secrets (Settings → Secrets and variables → Actions):
   - CURSOR_API_KEY  (weekly content agent)
   - SMTP_*          (weekly email digest; see docs/automation.md)

5. Optional repo variable:
   - CURSOR_AGENT_MODEL=auto  (or composer-2.5)

Docs: docs/automation.md
----------------------------------------------------------------------
EOF
}

print_auth_help() {
  cat <<EOF

----------------------------------------------------------------------
Authentication required before push
----------------------------------------------------------------------
Your Mac has git and an SSH key, but GitHub is not authenticated yet.

Option A — SSH (recommended; no Homebrew):
  1. Copy your public key:
       cat ~/.ssh/id_ed25519.pub
  2. Add it at: https://github.com/settings/keys
  3. Test:
       ssh -T git@github.com
  4. Re-run:
       ${REPO_ROOT}/scripts/deploy-github.sh

Option B — HTTPS + Personal Access Token:
  1. Create token: https://github.com/settings/tokens (repo scope)
  2. Run:
       USE_HTTPS=1 ${REPO_ROOT}/scripts/deploy-github.sh
     (git will prompt for username + token as password)

Option C — GitHub CLI login (local gh, no Homebrew):
  1. Install gh via this script:
       INSTALL_GH=1 ${REPO_ROOT}/scripts/deploy-github.sh --check
  2. Login:
       ${LOCAL_BIN}/gh auth login
  3. Re-run deploy script (creates repo if missing).

Create empty repo manually (no gh):
  https://github.com/new?name=${GITHUB_REPO}
  Then re-run this script with CREATE_REPO=0
----------------------------------------------------------------------
EOF
}

main() {
  local gh_bin=""
  ensure_git_repo
  configure_remote

  if gh_bin="$(ensure_gh)"; then
    export PATH="${LOCAL_BIN}:${HOME}/.local/bin:/opt/homebrew/bin:/usr/local/bin:${PATH}"
    info "Using gh: $gh_bin"
    if "$gh_bin" auth status >/dev/null 2>&1; then
      align_git_with_gh_auth "$gh_bin"
      maybe_create_repo "$gh_bin"
    else
      warn "gh found but not logged in; skipping repo create (use empty repo on github.com or gh auth login)"
    fi
  else
    warn "gh not found. Install with: INSTALL_GH=1 $0"
    warn "Or create https://github.com/${GITHUB_OWNER}/${GITHUB_REPO} in the browser first."
  fi

  if [[ "$USE_HTTPS" == "1" ]]; then
    if push_main; then
      info "Push succeeded."
      [[ -n "$gh_bin" ]] && maybe_trigger_deploy "$gh_bin"
      print_pages_steps
      exit 0
    fi
    die "git push failed over HTTPS"
  fi

  ensure_github_host_key
  if test_ssh_github; then
    if push_main; then
      info "Push succeeded."
      [[ -n "$gh_bin" ]] && maybe_trigger_deploy "$gh_bin"
      print_pages_steps
      exit 0
    fi
    die "git push failed (SSH authenticated but push rejected)"
  fi

  if [[ -n "$gh_bin" ]] && "$gh_bin" auth status >/dev/null 2>&1; then
    info "SSH unavailable; falling back to HTTPS with gh git credentials"
    USE_HTTPS=1
    "$gh_bin" auth setup-git --hostname github.com >/dev/null 2>&1 || true
    configure_remote
    if push_main; then
      info "Push succeeded (HTTPS)."
      maybe_trigger_deploy "$gh_bin"
      print_pages_steps
      exit 0
    fi
    die "git push failed over HTTPS (run: gh auth setup-git && git push -u origin ${BRANCH})"
  fi

  warn "SSH auth to GitHub failed (add ~/.ssh/id_ed25519.pub to GitHub or use USE_HTTPS=1)."
  print_auth_help
  exit 1
}

case "${1:-}" in
  --check)
    ensure_git_repo
    if gh_bin="$(ensure_gh)"; then
      "$gh_bin" --version
      "$gh_bin" auth status || true
    else
      warn "gh not installed. Run: INSTALL_GH=1 $0 --check"
    fi
    git -C "$REPO_ROOT" remote -v || true
    exit 0
    ;;
  --help|-h)
    sed -n '1,20p' "$0"
    echo "Env: USE_HTTPS=1 (force HTTPS) INSTALL_GH=1 CREATE_REPO=0 TRIGGER_DEPLOY=0 DEPLOY_WORKFLOW_NAME GITHUB_OWNER GITHUB_REPO DEPLOY_BRANCH"
    exit 0
    ;;
  *)
    main "$@"
    ;;
esac
