#!/usr/bin/env bash
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

if ! command -v git >/dev/null 2>&1; then
  echo "FAIL: git is not installed or not in PATH." >&2
  exit 1
fi

if ! git -C "$SCRIPT_DIR" rev-parse --is-inside-work-tree >/dev/null 2>&1; then
  echo "FAIL: $SCRIPT_DIR is not inside a Git working tree." >&2
  echo "Initialize or clone this folder as a Git repo, then rerun install-hooks.sh." >&2
  exit 1
fi

REPO_ROOT="$(git -C "$SCRIPT_DIR" rev-parse --show-toplevel)"
HOOK_FILE="$REPO_ROOT/hooks/pre-commit"
VALIDATOR="$REPO_ROOT/combinations/validate-combinations.sh"

chmod +x "$HOOK_FILE" "$VALIDATOR"
git -C "$REPO_ROOT" config core.hooksPath hooks

echo "PASS: pre-commit hook installed at $HOOK_FILE"
echo "PASS: core.hooksPath set to 'hooks'"
