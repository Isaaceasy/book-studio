#!/bin/bash
set -euo pipefail

# Only needed in Claude Code cloud sessions
if [ "${CLAUDE_CODE_REMOTE:-}" != "true" ]; then
  exit 0
fi

cd "${CLAUDE_PROJECT_DIR:-.}"

# Python packages go into the system Python, so there is no ignored directory
# to hold a hash file; pip is a fast no-op when everything is already installed.
pip install -q -r requirements.txt

# pandoc and LibreOffice normally ship with the cloud image; install only if missing.
if ! command -v pandoc >/dev/null 2>&1 || ! command -v soffice >/dev/null 2>&1; then
  apt-get update -qq
  apt-get install -y -qq pandoc libreoffice-writer
fi
