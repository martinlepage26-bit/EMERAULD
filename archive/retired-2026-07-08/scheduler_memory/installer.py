"""Install shell wrappers cc-emerauld and codex-emerauld under ~/.local/bin/."""

import os
from pathlib import Path

VAULT_ROOT = "/mnt/c/Users/softinfo/Documents/EMERAULD"
BIN_DIR = Path.home() / ".local" / "bin"

_CC_SCRIPT = f"""\
#!/usr/bin/env bash
# cc-emerauld: launch Claude Code in EMERAULD with scheduler check
set -euo pipefail

VAULT="{VAULT_ROOT}"
cd "$VAULT" || {{ echo "ERROR: Cannot cd to $VAULT"; exit 1; }}

python3 -m scheduler_memory session-start 2>/dev/null || true

if command -v claude >/dev/null 2>&1; then
    exec claude "$@"
else
    echo ""
    echo "ERROR: 'claude' command not found."
    echo "Install Claude Code CLI from: https://claude.ai/code"
    echo "Then re-run: cc-emerauld"
    exit 1
fi
"""

_CODEX_SCRIPT = f"""\
#!/usr/bin/env bash
# codex-emerauld: launch Codex in EMERAULD with scheduler check
set -euo pipefail

VAULT="{VAULT_ROOT}"
cd "$VAULT" || {{ echo "ERROR: Cannot cd to $VAULT"; exit 1; }}

python3 -m scheduler_memory session-start 2>/dev/null || true

if command -v codex >/dev/null 2>&1; then
    exec codex "$@"
else
    echo ""
    echo "ERROR: 'codex' command not found."
    echo "Install Codex CLI with: npm install -g @openai/codex"
    echo "Then re-run: codex-emerauld"
    exit 1
fi
"""


def install_shell(force: bool = False):
    BIN_DIR.mkdir(parents=True, exist_ok=True)

    scripts = {
        "cc-emerauld": _CC_SCRIPT,
        "codex-emerauld": _CODEX_SCRIPT,
    }

    created = []
    skipped = []

    for name, content in scripts.items():
        dest = BIN_DIR / name
        if dest.exists() and not force:
            skipped.append(str(dest))
        else:
            dest.write_text(content, encoding="utf-8")
            _try_chmod(dest, 0o755)
            created.append(str(dest))

    if created:
        print("\nCreated:")
        for p in created:
            print(f"  {p}")

    if skipped:
        print("\nSkipped (already exist — pass --force to overwrite):")
        for p in skipped:
            print(f"  {p}")

    # PATH check
    path_dirs = os.environ.get("PATH", "").split(":")
    if str(BIN_DIR) not in path_dirs:
        print(f"\nNOTE: {BIN_DIR} is not in your $PATH.")
        print("Add to ~/.bashrc or ~/.zshrc:")
        print('  export PATH="$HOME/.local/bin:$PATH"')

    print()
    print_aliases()


def print_aliases():
    print("# Recommended shell config — add to ~/.bashrc or ~/.zshrc:")
    print('export PATH="$HOME/.local/bin:$PATH"')
    print("alias c='cc-emerauld'")
    print("alias ce='cc-emerauld'")
    print("alias cx='codex-emerauld'")


def _try_chmod(path: Path, mode: int):
    """Attempt chmod; silently skip if the filesystem doesn't support it (e.g. NTFS)."""
    try:
        path.chmod(mode)
    except (OSError, NotImplementedError):
        pass
