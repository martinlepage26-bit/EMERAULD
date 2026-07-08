#!/usr/bin/env python3
"""Jade — bounded local-first AI assistant. CLI loop, Ollama backend, SQLite memory."""
import re
import readline
import sqlite3
from datetime import datetime, timezone
from pathlib import Path

JADE_DIR = Path.home() / ".jade"
JADE_DIR.mkdir(exist_ok=True)

DB_PATH    = JADE_DIR / "memory.db"
AUDIT_LOG  = JADE_DIR / "audit.log"
MODEL      = "qwen2.5:7b"
HISTORY_WINDOW = 20   # turns kept in context (each turn = user + assistant pair)

# ── Ollama client ──────────────────────────────────────────────────────────────
try:
    import ollama
    def _llm(messages: list[dict]) -> str:
        resp = ollama.chat(model=MODEL, messages=messages)
        return resp["message"]["content"]
except ImportError:
    def _llm(messages):
        raise RuntimeError("ollama not installed — pip install ollama")

from tool_router import execute, BlockedError

# ── System prompt ──────────────────────────────────────────────────────────────
SYSTEM_PROMPT = """You are Jade, a bounded local assistant running on a Linux server.

TOOL FORMAT — use this exact syntax when you need to run a command:
  [TOOL: shell | <command>]

Rules:
- Emit AT MOST one [TOOL:] tag per response, on its own line.
- NEVER fabricate tool output. NEVER write "[ran: ...]" yourself — the system adds that.
- Wait for the [tool result] message before narrating any command output.
- If the request does not require a command, reply normally with NO tag.
- Never emit a tag for destructive, network, or write operations.

Allowed commands: pwd, ls, find, rg, cat, date, echo, wc, du, file
Forbidden: rm, sudo, ssh, curl, wget, pip, npm, pipes (|), semicolons (;), redirects (>), df, ps, top, kill, and everything not in the allowed list above.

--- EXAMPLES ---

User: What time is it?
Jade: Let me check.
[TOOL: shell | date]

User: What files are in my home directory?
Jade: I'll list them now.
[TOOL: shell | ls]

User: Who is the president of France?
Jade: The current president of France is Emmanuel Macron, in office since 2017.

User: Delete my logs folder.
Jade: I cannot do that. Destructive commands are outside my allowed set.

User: What is 2 + 2?
Jade: 4.

User: Check disk usage.
Jade: I cannot run df — it is not in my allowed command set.

--- END EXAMPLES ---"""

TOOL_RE = re.compile(r'\[TOOL:\s*shell\s*\|\s*(.+?)\]', re.IGNORECASE)

# ── SQLite memory ──────────────────────────────────────────────────────────────

def _db() -> sqlite3.Connection:
    con = sqlite3.connect(DB_PATH)
    con.execute("""
        CREATE TABLE IF NOT EXISTS turns (
            id        INTEGER PRIMARY KEY AUTOINCREMENT,
            session   TEXT    NOT NULL,
            ts        TEXT    NOT NULL,
            role      TEXT    NOT NULL,
            content   TEXT    NOT NULL
        )
    """)
    con.commit()
    return con


def _new_session_id() -> str:
    return datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ")


def load_history(session_id: str, window: int = HISTORY_WINDOW) -> list[dict]:
    """Load the last `window` turns (user+assistant pairs) from the DB."""
    with _db() as con:
        rows = con.execute(
            """SELECT role, content FROM turns
               WHERE session = ?
               ORDER BY id DESC LIMIT ?""",
            (session_id, window * 2),
        ).fetchall()
    return [{"role": r, "content": c} for r, c in reversed(rows)]


def save_turn(session_id: str, role: str, content: str) -> None:
    ts = datetime.now(timezone.utc).isoformat()
    with _db() as con:
        con.execute(
            "INSERT INTO turns (session, ts, role, content) VALUES (?, ?, ?, ?)",
            (session_id, ts, role, content),
        )
        con.commit()


def list_sessions() -> list[tuple[str, int]]:
    """Return [(session_id, turn_count), …] ordered newest first."""
    with _db() as con:
        return con.execute(
            "SELECT session, COUNT(*) FROM turns GROUP BY session ORDER BY MIN(id) DESC"
        ).fetchall()


# ── Parser helpers ─────────────────────────────────────────────────────────────

def _extract_tool(text: str) -> str | None:
    m = TOOL_RE.search(text)
    return m.group(1).strip() if m else None


def _strip_tool_tag(text: str) -> str:
    return TOOL_RE.sub("", text).strip()


# ── Core chat function ─────────────────────────────────────────────────────────

def chat(user_input: str, session_id: str, history: list[dict]) -> tuple[str, list[dict]]:
    """Send user_input, return (assistant_reply, updated_history).

    history is mutated in-place AND persisted to DB.
    """
    history.append({"role": "user", "content": user_input})
    save_turn(session_id, "user", user_input)

    messages = [{"role": "system", "content": SYSTEM_PROMPT}] + history
    reply = _llm(messages)
    cmd   = _extract_tool(reply)
    clean = _strip_tool_tag(reply)

    if cmd:
        try:
            tool_output = execute(cmd)
            history.append({"role": "assistant", "content": reply})
            save_turn(session_id, "assistant", reply)
            history.append({"role": "user", "content": f"[tool result]\n{tool_output}"})
            save_turn(session_id, "user", f"[tool result]\n{tool_output}")

            followup = _llm([{"role": "system", "content": SYSTEM_PROMPT}] + history)
            history.append({"role": "assistant", "content": followup})
            save_turn(session_id, "assistant", followup)
            clean = _strip_tool_tag(followup) + f"\n\n[ran: {cmd}]\n{tool_output}"
        except BlockedError as e:
            clean += f"\n\n[BLOCKED: {e}]"
            history.append({"role": "assistant", "content": clean})
            save_turn(session_id, "assistant", clean)
    else:
        history.append({"role": "assistant", "content": reply})
        save_turn(session_id, "assistant", reply)

    return clean, history


# ── CLI ────────────────────────────────────────────────────────────────────────

def main():
    import argparse
    parser = argparse.ArgumentParser(description="Jade local assistant")
    parser.add_argument("--resume", metavar="SESSION_ID",
                        help="Resume a previous session by ID")
    parser.add_argument("--sessions", action="store_true",
                        help="List all past sessions and exit")
    args = parser.parse_args()

    if args.sessions:
        sessions = list_sessions()
        if not sessions:
            print("No sessions found.")
        else:
            print(f"{'SESSION':30s}  TURNS")
            for sid, count in sessions:
                print(f"  {sid:30s}  {count}")
        return

    if args.resume:
        session_id = args.resume
        history    = load_history(session_id)
        print(f"Jade ({MODEL}) — resuming session {session_id} ({len(history)} messages)\n")
    else:
        session_id = _new_session_id()
        history    = []
        print(f"Jade ({MODEL}) — new session {session_id}")
        print("Commands: 'exit' quit · 'log' audit trail · 'memory' session list\n")

    while True:
        try:
            user = input("you: ").strip()
        except (EOFError, KeyboardInterrupt):
            print(f"\nSession {session_id} saved. Resume with: python3 jade.py --resume {session_id}")
            break

        if not user:
            continue
        if user.lower() in ("exit", "quit", "bye"):
            print(f"Session {session_id} saved. Resume with: python3 jade.py --resume {session_id}")
            break
        if user.lower() == "log":
            if AUDIT_LOG.exists():
                print(AUDIT_LOG.read_text())
            else:
                print("(no audit log yet)")
            continue
        if user.lower() == "memory":
            for sid, count in list_sessions():
                marker = " ← current" if sid == session_id else ""
                print(f"  {sid}  ({count} messages){marker}")
            continue

        try:
            reply, history = chat(user, session_id, history)
            print(f"\nJade: {reply}\n")
        except Exception as e:
            print(f"\n[error] {e}\n")


if __name__ == "__main__":
    main()
