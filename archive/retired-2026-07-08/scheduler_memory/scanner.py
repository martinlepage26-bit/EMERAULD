"""Scan the EMERAULD vault for tasks, deadlines, blocked items, and stale work."""

import hashlib
import os
import re
import subprocess
import time
from datetime import datetime
from pathlib import Path

from .deadline import parse_deadline

# Directories to skip — never recurse into these
SKIP_DIRS = {
    ".git", "node_modules", ".scheduler", ".obsidian", ".vector_store",
    "__pycache__", ".venv", "venv", ".codex", "scheduler_memory",
    "artifacts",  # large asset bundles, not note content
}

MARKDOWN_EXTS = {".md", ".markdown"}
CODE_EXTS = {".py", ".js", ".ts", ".jsx", ".tsx", ".sh", ".bash", ".zsh"}

# --- Markdown patterns ---

# Unchecked task: "- [ ] text" with optional leading whitespace
RE_TASK = re.compile(r'^\s*-\s*\[\s*\]\s*(.+)', re.MULTILINE)

# Dataview-style inline field: [due:: 2026-05-01]
RE_DUE_INLINE = re.compile(r'\[(?:due|deadline|scheduled)::\s*([^\]]{1,60})\]', re.IGNORECASE)

# Property-style: "due:: value" or "deadline:: value"
RE_DUE_PROP = re.compile(r'^(?:due|deadline|scheduled)\s*::\s*(.+)$', re.IGNORECASE | re.MULTILINE)

# Simple colon: "due: value" (narrower match to avoid false positives)
RE_DUE_SIMPLE = re.compile(r'\b(?:due|deadline|scheduled)\s*:\s*(\S[^\n]{0,40})', re.IGNORECASE)

# Obsidian tags
RE_TAGS = re.compile(r'#(todo|waiting|blocked|followup)\b', re.IGNORECASE)

# Deadline-related phrases in free text
RE_PHRASES = re.compile(
    r'\b(?:waiting on|blocked by|follow[- ]?up|before launch|after approval|'
    r'by Friday|by tomorrow|next week|before release|after legal approval|'
    r'before the deadline|pending approval)\b',
    re.IGNORECASE,
)

# --- Code patterns ---

RE_CODE_TODO = re.compile(r'(?:#|//|--)\s*(TODO|FIXME|HACK|BUG|XXX|FOLLOWUP)\b[:\s]*(.*)', re.IGNORECASE)
RE_SKIP_TEST = re.compile(r'(?:pytest\.mark\.skip|@skip\s*\(|\.skip\s*\(|xit\s*\(|xtest\s*\()', re.IGNORECASE)

_PRIORITY_ORDER = {"urgent": 0, "high": 1, "medium": 2, "low": 3}


def _max_priority(a: str, b: str) -> str:
    return a if _PRIORITY_ORDER.get(a, 3) <= _PRIORITY_ORDER.get(b, 3) else b


def _item_id(path: str, line: int, text: str) -> str:
    h = hashlib.md5(f"{path}:{line}:{text[:40]}".encode()).hexdigest()[:10]
    return f"i{h}"


def _now_iso() -> str:
    return datetime.now().isoformat()


def _make_item(*, id, title, kind, source_path, source_line, source_quote,
               deadline_info, priority, confidence, reminder_reason, suggested_next_action):
    return {
        "id": id,
        "title": title[:100],
        "kind": kind,
        "status": "active",
        "source_path": source_path,
        "source_line": source_line,
        "source_quote": source_quote[:300],
        "branch": None,
        "first_seen": _now_iso(),
        "last_seen": _now_iso(),
        "last_changed": _now_iso(),
        "deadline": deadline_info.get("deadline"),
        "deadline_text": deadline_info.get("deadline_text", ""),
        "deadline_type": deadline_info.get("deadline_type", "none"),
        "reminder_reason": reminder_reason,
        "confidence": confidence,
        "priority": priority,
        "suggested_next_action": suggested_next_action,
        "unresolved_questions": deadline_info.get("unresolved_questions", []),
        "snoozed_until": None,
        "dismissed": False,
        "dismiss_reason": None,
    }


def scan_vault(vault_root: str) -> list:
    """Scan the vault and return a list of raw detected items."""
    items = []
    root = Path(vault_root)

    for filepath in _walk(root):
        ext = filepath.suffix.lower()
        rel = str(filepath.relative_to(root))

        if ext in MARKDOWN_EXTS:
            items.extend(_scan_markdown(filepath, rel))
        elif ext in CODE_EXTS:
            items.extend(_scan_code(filepath, rel))

    items.extend(_scan_git(vault_root))
    return items


def _walk(root: Path):
    for dirpath, dirnames, filenames in os.walk(root):
        dirnames[:] = [
            d for d in dirnames
            if d not in SKIP_DIRS and not d.startswith('.')
        ]
        p = Path(dirpath)
        for fn in filenames:
            yield p / fn


# ---------------------------------------------------------------------------
# Markdown scanning
# ---------------------------------------------------------------------------

def _scan_markdown(path: Path, rel: str) -> list:
    try:
        content = path.read_text(encoding="utf-8", errors="ignore")
    except OSError:
        return []

    items = []
    lines = content.split("\n")

    for lineno, line in enumerate(lines, 1):
        # Unchecked tasks
        m = RE_TASK.match(line)
        if m:
            task_text = m.group(1).strip()
            dl = _deadline_from_text(task_text + " " + line)
            tags = RE_TAGS.findall(line)
            has_phrase = bool(RE_PHRASES.search(line))
            priority = _tags_to_priority(tags)
            if dl["deadline"] or dl["deadline_type"] == "event_relative":
                priority = _max_priority(priority, "medium")
                confidence = "high"
            elif tags or has_phrase:
                confidence = "medium"
            else:
                confidence = "low"

            items.append(_make_item(
                id=_item_id(rel, lineno, task_text),
                title=task_text[:80],
                kind="task",
                source_path=rel,
                source_line=lineno,
                source_quote=line.strip(),
                deadline_info=dl,
                priority=priority,
                confidence=confidence,
                reminder_reason=_task_reason(tags, has_phrase, dl),
                suggested_next_action=_task_action(tags, dl),
            ))
            continue

        # Standalone due markers (outside tasks)
        for pattern in (RE_DUE_INLINE, RE_DUE_PROP):
            m = pattern.search(line)
            if m:
                dl_text = m.group(1).strip()
                dl = parse_deadline(dl_text)
                if dl["deadline_type"] != "none":
                    items.append(_make_item(
                        id=_item_id(rel, lineno, dl_text),
                        title=f"Deadline marker: {dl_text}",
                        kind="deadline",
                        source_path=rel,
                        source_line=lineno,
                        source_quote=line.strip(),
                        deadline_info=dl,
                        priority="high",
                        confidence="high",
                        reminder_reason="Explicit deadline marker",
                        suggested_next_action="Review and act on this deadline.",
                    ))
                break

        # Tagged non-task lines
        if not RE_TASK.match(line):
            tags = RE_TAGS.findall(line)
            if tags:
                priority = _tags_to_priority(tags)
                items.append(_make_item(
                    id=_item_id(rel, lineno, line[:30]),
                    title=line.strip()[:80] or f"Tagged line at {rel}:{lineno}",
                    kind="tagged",
                    source_path=rel,
                    source_line=lineno,
                    source_quote=line.strip(),
                    deadline_info={"deadline": None, "deadline_text": "", "deadline_type": "none", "unresolved_questions": []},
                    priority=priority,
                    confidence="medium",
                    reminder_reason=f"Tagged: #{', #'.join(t.lower() for t in tags)}",
                    suggested_next_action="Review and decide next action.",
                ))

    return items


# ---------------------------------------------------------------------------
# Code scanning
# ---------------------------------------------------------------------------

def _scan_code(path: Path, rel: str) -> list:
    try:
        content = path.read_text(encoding="utf-8", errors="ignore")
    except OSError:
        return []

    items = []
    p_map = {"FIXME": "high", "BUG": "high", "HACK": "medium",
              "TODO": "medium", "XXX": "medium", "FOLLOWUP": "low"}

    for lineno, line in enumerate(content.split("\n"), 1):
        m = RE_CODE_TODO.search(line)
        if m:
            kind = m.group(1).upper()
            note = m.group(2).strip()[:80]
            items.append(_make_item(
                id=_item_id(rel, lineno, line[:30]),
                title=f"{kind}: {note}" if note else kind,
                kind="code_todo",
                source_path=rel,
                source_line=lineno,
                source_quote=line.strip(),
                deadline_info={"deadline": None, "deadline_text": "", "deadline_type": "missing", "unresolved_questions": []},
                priority=p_map.get(kind, "low"),
                confidence="high",
                reminder_reason=f"{kind} comment in source",
                suggested_next_action=f"Resolve {kind} at {rel}:{lineno}.",
            ))

    return items


# ---------------------------------------------------------------------------
# Git scanning
# ---------------------------------------------------------------------------

def _scan_git(vault_root: str) -> list:
    items = []
    try:
        r = subprocess.run(
            ["git", "rev-parse", "--is-inside-work-tree"],
            cwd=vault_root, capture_output=True, text=True, timeout=5,
        )
        if r.returncode != 0:
            return items

        branch = subprocess.run(
            ["git", "rev-parse", "--abbrev-ref", "HEAD"],
            cwd=vault_root, capture_output=True, text=True, timeout=5,
        ).stdout.strip() or "unknown"

        # Uncommitted changes
        status = subprocess.run(
            ["git", "status", "--porcelain"],
            cwd=vault_root, capture_output=True, text=True, timeout=10,
        )
        if status.returncode == 0:
            dirty = [ln[3:].strip() for ln in status.stdout.split("\n") if ln.strip()]
            if dirty:
                it = _make_item(
                    id=_item_id("git", 0, "dirty"),
                    title=f"Uncommitted changes: {len(dirty)} file(s)",
                    kind="git_dirty",
                    source_path=f"[git:{branch}]",
                    source_line=0,
                    source_quote="\n".join(dirty[:8]),
                    deadline_info={"deadline": None, "deadline_text": "", "deadline_type": "none", "unresolved_questions": []},
                    priority="medium",
                    confidence="high",
                    reminder_reason="Uncommitted changes in working tree",
                    suggested_next_action="Commit, stash, or review these changes.",
                )
                it["branch"] = branch
                items.append(it)

        # Stale branch — no commits for ≥7 days
        log = subprocess.run(
            ["git", "log", "-1", "--format=%ct"],
            cwd=vault_root, capture_output=True, text=True, timeout=5,
        )
        if log.returncode == 0 and log.stdout.strip():
            age_days = (time.time() - int(log.stdout.strip())) / 86400
            if age_days >= 7:
                it = _make_item(
                    id=_item_id("git", 0, "stale"),
                    title=f"Stale branch '{branch}' — {int(age_days)}d since last commit",
                    kind="git_stale",
                    source_path=f"[git:{branch}]",
                    source_line=0,
                    source_quote=f"Last commit ~{int(age_days)} days ago",
                    deadline_info={"deadline": None, "deadline_text": "", "deadline_type": "missing", "unresolved_questions": []},
                    priority="low",
                    confidence="high",
                    reminder_reason=f"No commits for {int(age_days)} days",
                    suggested_next_action="Resume work or archive this branch.",
                )
                it["branch"] = branch
                items.append(it)

        # TODOs introduced in current diff
        diff = subprocess.run(
            ["git", "diff", "--unified=0"],
            cwd=vault_root, capture_output=True, text=True, timeout=10,
        )
        if diff.returncode == 0 and diff.stdout:
            for lineno, line in enumerate(diff.stdout.split("\n"), 1):
                if line.startswith("+") and not line.startswith("+++"):
                    m = RE_CODE_TODO.search(line[1:])
                    if m:
                        kind = m.group(1).upper()
                        note = m.group(2).strip()[:60]
                        it = _make_item(
                            id=_item_id("git-diff", lineno, line[:30]),
                            title=f"New {kind} in diff: {note}" if note else f"New {kind} in diff",
                            kind="git_todo",
                            source_path="[git diff]",
                            source_line=lineno,
                            source_quote=line[1:].strip(),
                            deadline_info={"deadline": None, "deadline_text": "", "deadline_type": "missing", "unresolved_questions": []},
                            priority="medium",
                            confidence="high",
                            reminder_reason=f"New {kind} introduced in diff",
                            suggested_next_action=f"Resolve {kind} before committing.",
                        )
                        it["branch"] = branch
                        items.append(it)

    except (subprocess.TimeoutExpired, FileNotFoundError, ValueError, OSError):
        pass

    return items


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

def _deadline_from_text(text: str) -> dict:
    """Extract deadline from a task line — try patterns then phrases."""
    for pattern in (RE_DUE_INLINE, RE_DUE_PROP, RE_DUE_SIMPLE):
        m = pattern.search(text)
        if m:
            dl = parse_deadline(m.group(1).strip())
            if dl["deadline_type"] != "none":
                return dl

    tl = text.lower()
    for phrase in [
        "today", "tomorrow", "end of week", "next week", "eod",
        "by friday", "by monday", "by tuesday", "by wednesday", "by thursday",
        "next monday", "next tuesday", "next wednesday", "next thursday", "next friday",
        "before launch", "after approval", "before release", "after legal approval",
    ]:
        if phrase in tl:
            dl = parse_deadline(phrase)
            if dl["deadline_type"] != "none":
                return dl

    return {"deadline": None, "deadline_text": "", "deadline_type": "none", "unresolved_questions": []}


def _tags_to_priority(tags: list) -> str:
    tl = [t.lower() for t in tags]
    if "blocked" in tl:
        return "urgent"
    if "todo" in tl or "followup" in tl:
        return "medium"
    if "waiting" in tl:
        return "low"
    return "low"


def _task_reason(tags: list, has_phrase: bool, dl: dict) -> str:
    parts = []
    if dl["deadline"]:
        parts.append(f"deadline: {dl['deadline_text']}")
    elif dl["deadline_type"] == "event_relative":
        parts.append("event-relative deadline")
    if tags:
        parts.append(f"#{', #'.join(t.lower() for t in tags)}")
    if has_phrase:
        parts.append("deadline phrase")
    return "; ".join(parts) if parts else "unchecked task"


def _task_action(tags: list, dl: dict) -> str:
    tl = [t.lower() for t in tags]
    if "blocked" in tl:
        return "Identify and resolve the blocker."
    if dl["deadline"]:
        return f"Complete by {dl['deadline_text']}."
    if dl["deadline_type"] == "event_relative":
        qs = dl.get("unresolved_questions", [])
        return f"Clarify: {'; '.join(qs)}" if qs else "Clarify the event-relative deadline."
    if "waiting" in tl:
        return "Follow up on what you're waiting for."
    return "Complete, assign a deadline, or dismiss if no longer relevant."
