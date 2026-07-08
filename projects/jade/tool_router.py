"""Jade tool router — classify, execute, and audit tool calls from the LLM."""
import json
import os
import re
import shlex
import subprocess
from datetime import datetime, timezone
from pathlib import Path

AUDIT_LOG = Path.home() / ".jade" / "audit.log"
HOME = Path.home().resolve()

# Tier 1: silent allowlist — read-only, local, no side effects
ALLOWLIST = {"pwd", "ls", "find", "rg", "cat", "date", "echo", "wc", "du", "file", "head", "tail", "stat", "uptime", "uname", "whoami"}

# Hard-block patterns — never execute regardless of allowlist
BLOCK_PATTERNS = [
    r"rm\b", r"sudo\b", r"ssh\b", r"scp\b", r"curl\b", r"wget\b",
    r"pip\b", r"npm\b", r"apt\b", r"brew\b",
    r"chmod\b", r"chown\b", r"mv\b", r"cp\b", r"mkdir\b", r"touch\b",
    r">\s*\S", r">>\s*\S",   # redirects
    r"[|;&]",                 # pipes, semicolons, AND/OR chaining
    r"`",                     # backtick subshell
    r"\$\(",                  # $() subshell
    r"~/.ssh", r"/etc/",      # sensitive paths
    r"\.\./"                  # path traversal
]

MAX_CAT_BYTES = 100_000  # 100 KB


class BlockedError(Exception):
    pass


def _is_blocked(raw: str) -> str | None:
    """Return the first matching block reason, or None if safe."""
    for pat in BLOCK_PATTERNS:
        if re.search(pat, raw):
            return f"blocked pattern: {pat!r}"
    return None


def _check_cat_constraint(parts: list[str]) -> None:
    """cat is only allowed for files inside $HOME under 100 KB."""
    for arg in parts[1:]:
        if arg.startswith("-"):
            continue
        p = Path(arg).expanduser().resolve()
        if not str(p).startswith(str(HOME)):
            raise BlockedError(f"cat blocked: {arg!r} is outside $HOME")
        
        # Block dotdirs, dotfiles, and sensitive names
        try:
            rel = p.relative_to(HOME)
            if any(part.startswith('.') for part in rel.parts):
                raise BlockedError(f"cat blocked: {arg!r} contains dotdir/dotfile")
        except ValueError:
            pass

        name_lower = p.name.lower()
        if "token" in name_lower or "key" in name_lower or "password" in name_lower:
            raise BlockedError(f"cat blocked: {arg!r} matches sensitive filename")

        if p.exists() and p.stat().st_size > MAX_CAT_BYTES:
            raise BlockedError(f"cat blocked: {arg!r} exceeds {MAX_CAT_BYTES} bytes")


def classify(cmd: str) -> dict:
    """Return {status, reason, argv, normalized}.

    status: 'safe' | 'blocked'
    reason: human-readable explanation
    argv:   shlex-parsed list, or [] if unparseable
    normalized: lowercased base command, or ''
    """
    block_reason = _is_blocked(cmd)
    if block_reason:
        return {"status": "blocked", "reason": block_reason, "argv": [], "normalized": ""}

    try:
        parts = shlex.split(cmd)
    except ValueError as e:
        return {"status": "blocked", "reason": f"parse error: {e}", "argv": [], "normalized": ""}

    if not parts:
        return {"status": "blocked", "reason": "empty command", "argv": [], "normalized": ""}

    base = parts[0]
    if base not in ALLOWLIST:
        return {
            "status": "blocked",
            "reason": f"command {base!r} not in allowlist",
            "argv": parts,
            "normalized": base.lower(),
        }

    return {"status": "safe", "reason": "allowlisted", "argv": parts, "normalized": base.lower()}


def execute(cmd: str) -> str:
    """Execute a command and return its output. Raises BlockedError if unsafe."""
    result = classify(cmd)
    if result["status"] == "blocked":
        _log(cmd, "blocked", result["reason"])
        raise BlockedError(result["reason"])

    parts = result["argv"]
    base  = result["normalized"]

    if base == "cat":
        _check_cat_constraint(parts)

    # find / rg — stay under HOME subtree
    if base in ("find", "rg"):
        for arg in parts[1:]:
            resolved = Path(arg).expanduser().resolve()
            if arg.startswith("/") and not str(resolved).startswith(str(HOME)):
                reason = f"{base} blocked: path {arg!r} outside $HOME"
                _log(cmd, "blocked", reason)
                raise BlockedError(reason)

    try:
        proc = subprocess.run(
            parts,
            capture_output=True,
            text=True,
            timeout=10,
            cwd=str(HOME),
        )
        output = (proc.stdout + proc.stderr).strip()
        _log(cmd, "executed", output[:200])
        return output
    except subprocess.TimeoutExpired:
        reason = "command timed out after 10s"
        _log(cmd, "blocked", reason)
        raise BlockedError(reason)
    except Exception as e:
        _log(cmd, "error", str(e))
        raise BlockedError(str(e))


def _log(cmd: str, status: str, detail: str = "") -> None:
    AUDIT_LOG.parent.mkdir(parents=True, exist_ok=True)
    entry = {
        "ts": datetime.now(timezone.utc).isoformat(),
        "cmd": cmd,
        "status": status,
        "detail": detail[:500],
    }
    with open(AUDIT_LOG, "a", encoding="utf-8") as f:
        f.write(json.dumps(entry) + "\n")
