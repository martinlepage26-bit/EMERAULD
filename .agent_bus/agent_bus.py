#!/usr/bin/env python3
"""Small durable SQLite message bus for local Claude/Codex coordination."""

from __future__ import annotations

import argparse
import json
import sqlite3
import sys
import time
from datetime import datetime, timezone
from pathlib import Path
from typing import Iterable


BUS_DIR = Path(__file__).resolve().parent
DB_PATH = BUS_DIR / "messages.sqlite"
AGENTS = {"codex", "claude"}


def utc_now() -> str:
    return datetime.now(timezone.utc).isoformat(timespec="seconds").replace("+00:00", "Z")


def connect() -> sqlite3.Connection:
    BUS_DIR.mkdir(parents=True, exist_ok=True)
    conn = sqlite3.connect(DB_PATH, timeout=30)
    conn.row_factory = sqlite3.Row
    conn.execute("PRAGMA busy_timeout = 5000")
    conn.execute("PRAGMA journal_mode = WAL")
    ensure_schema(conn)
    return conn


def ensure_schema(conn: sqlite3.Connection) -> None:
    conn.executescript(
        """
        CREATE TABLE IF NOT EXISTS messages (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            thread TEXT NOT NULL,
            sender TEXT NOT NULL,
            recipient TEXT NOT NULL,
            body TEXT NOT NULL,
            created_at TEXT NOT NULL,
            read_at TEXT
        );

        CREATE INDEX IF NOT EXISTS idx_messages_recipient_read
            ON messages (recipient, read_at, id);

        CREATE INDEX IF NOT EXISTS idx_messages_thread
            ON messages (thread, id);

        CREATE TABLE IF NOT EXISTS heartbeats (
            agent TEXT PRIMARY KEY,
            status TEXT NOT NULL,
            note TEXT NOT NULL DEFAULT '',
            updated_at TEXT NOT NULL
        );
        """
    )
    conn.commit()


def validate_agent(agent: str) -> str:
    if agent not in AGENTS:
        allowed = ", ".join(sorted(AGENTS))
        raise SystemExit(f"Unknown agent '{agent}'. Expected one of: {allowed}.")
    return agent


def body_from_args(args: argparse.Namespace) -> str:
    if args.body is not None:
        return args.body
    if args.body_file:
        if args.body_file == "-":
            return sys.stdin.read()
        return Path(args.body_file).read_text(encoding="utf-8")
    if not sys.stdin.isatty():
        return sys.stdin.read()
    raise SystemExit("Message body required. Use --body, --body-file, or pipe stdin.")


def rows_to_dicts(rows: Iterable[sqlite3.Row]) -> list[dict[str, object]]:
    return [dict(row) for row in rows]


def print_messages(rows: list[sqlite3.Row], as_json: bool = False) -> None:
    if as_json:
        print(json.dumps(rows_to_dicts(rows), indent=2))
        return

    if not rows:
        print("No unread messages.")
        return

    for row in rows:
        read_state = "read" if row["read_at"] else "unread"
        print(
            f"[{row['id']}] {row['created_at']} "
            f"from={row['sender']} to={row['recipient']} "
            f"thread={row['thread']} {read_state}"
        )
        print(row["body"])
        print()


def send_message(args: argparse.Namespace) -> None:
    sender = validate_agent(args.from_agent)
    recipient = validate_agent(args.to_agent)
    body = body_from_args(args).rstrip("\n")
    if not body:
        raise SystemExit("Message body cannot be empty.")

    with connect() as conn:
        created_at = utc_now()
        cur = conn.execute(
            """
            INSERT INTO messages (thread, sender, recipient, body, created_at)
            VALUES (?, ?, ?, ?, ?)
            """,
            (args.thread, sender, recipient, body, created_at),
        )
        conn.commit()
        print(
            f"sent id={cur.lastrowid} thread={args.thread} "
            f"from={sender} to={recipient} at={created_at}"
        )


def inbox(args: argparse.Namespace) -> None:
    agent = validate_agent(args.agent)
    with connect() as conn:
        sql = "SELECT * FROM messages WHERE recipient = ?"
        params: list[object] = [agent]
        if not args.all:
            sql += " AND read_at IS NULL"
        sql += " ORDER BY id ASC LIMIT ?"
        params.append(args.limit)
        rows = list(conn.execute(sql, params))
        print_messages(rows, args.json)
        if args.mark_read and rows:
            mark_ids(conn, agent, [int(row["id"]) for row in rows])


def mark_ids(conn: sqlite3.Connection, agent: str, ids: list[int]) -> int:
    if not ids:
        return 0
    placeholders = ",".join("?" for _ in ids)
    params: list[object] = [utc_now(), agent, *ids]
    cur = conn.execute(
        f"""
        UPDATE messages
        SET read_at = COALESCE(read_at, ?)
        WHERE recipient = ? AND id IN ({placeholders})
        """,
        params,
    )
    conn.commit()
    return cur.rowcount


def mark_read(args: argparse.Namespace) -> None:
    agent = validate_agent(args.agent)
    with connect() as conn:
        if args.all:
            cur = conn.execute(
                """
                UPDATE messages
                SET read_at = COALESCE(read_at, ?)
                WHERE recipient = ? AND read_at IS NULL
                """,
                (utc_now(), agent),
            )
            conn.commit()
            print(f"marked_read count={cur.rowcount} agent={agent}")
            return

        ids = [int(value) for value in args.id]
        count = mark_ids(conn, agent, ids)
        print(f"marked_read count={count} agent={agent}")


def upsert_heartbeat(agent: str, status: str, note: str = "") -> str:
    updated_at = utc_now()
    with connect() as conn:
        conn.execute(
            """
            INSERT INTO heartbeats (agent, status, note, updated_at)
            VALUES (?, ?, ?, ?)
            ON CONFLICT(agent) DO UPDATE SET
                status = excluded.status,
                note = excluded.note,
                updated_at = excluded.updated_at
            """,
            (agent, status, note or "", updated_at),
        )
        conn.commit()
    return updated_at


def heartbeat(args: argparse.Namespace) -> None:
    agent = validate_agent(args.agent)
    updated_at = upsert_heartbeat(agent, args.status, args.note)
    print(f"heartbeat agent={agent} status={args.status} at={updated_at}")


def peers(args: argparse.Namespace) -> None:
    with connect() as conn:
        rows = list(conn.execute("SELECT * FROM heartbeats ORDER BY agent ASC"))
    if args.json:
        print(json.dumps(rows_to_dicts(rows), indent=2))
        return
    if not rows:
        print("No heartbeats recorded.")
        return
    for row in rows:
        note = f" note={row['note']}" if row["note"] else ""
        print(f"{row['agent']} status={row['status']} updated_at={row['updated_at']}{note}")


def watch(args: argparse.Namespace) -> None:
    agent = validate_agent(args.agent)
    seen: set[int] = set()
    print(f"watching inbox for {agent}; press Ctrl-C to stop", flush=True)

    try:
        while True:
            upsert_heartbeat(agent, args.status, args.note)
            with connect() as conn:
                rows = list(
                    conn.execute(
                        """
                        SELECT * FROM messages
                        WHERE recipient = ? AND read_at IS NULL
                        ORDER BY id ASC
                        """,
                        (agent,),
                    )
                )
                fresh = [row for row in rows if int(row["id"]) not in seen]
                if fresh:
                    print_messages(fresh, as_json=False)
                    seen.update(int(row["id"]) for row in fresh)
                    if args.mark_read:
                        mark_ids(conn, agent, [int(row["id"]) for row in fresh])
            time.sleep(args.interval)
    except KeyboardInterrupt:
        updated_at = upsert_heartbeat(agent, "offline", "watch stopped")
        print(f"heartbeat agent={agent} status=offline at={updated_at}")


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Local SQLite message bus for Claude/Codex.")
    sub = parser.add_subparsers(dest="command", required=True)

    send = sub.add_parser("send", help="Send a message.")
    send.add_argument("--from", dest="from_agent", required=True)
    send.add_argument("--to", dest="to_agent", required=True)
    send.add_argument("--thread", required=True)
    send.add_argument("--body")
    send.add_argument("--body-file")
    send.set_defaults(func=send_message)

    inbox_parser = sub.add_parser("inbox", help="Read inbox messages.")
    inbox_parser.add_argument("--agent", required=True)
    inbox_parser.add_argument("--all", action="store_true", help="Show read and unread messages.")
    inbox_parser.add_argument("--json", action="store_true")
    inbox_parser.add_argument("--limit", type=int, default=50)
    inbox_parser.add_argument("--mark-read", action="store_true")
    inbox_parser.set_defaults(func=inbox)

    mark = sub.add_parser("mark-read", help="Mark messages read.")
    mark.add_argument("--agent", required=True)
    mark.add_argument("--id", action="append", default=[], help="Message id to mark read.")
    mark.add_argument("--all", action="store_true", help="Mark all unread messages read.")
    mark.set_defaults(func=mark_read)

    hb = sub.add_parser("heartbeat", help="Update an agent heartbeat.")
    hb.add_argument("--agent", required=True)
    hb.add_argument("--status", default="online")
    hb.add_argument("--note", default="")
    hb.set_defaults(func=heartbeat)

    peer_parser = sub.add_parser("peers", help="List recorded heartbeats.")
    peer_parser.add_argument("--json", action="store_true")
    peer_parser.set_defaults(func=peers)

    watch_parser = sub.add_parser("watch", help="Watch unread inbox messages.")
    watch_parser.add_argument("--agent", required=True)
    watch_parser.add_argument("--interval", type=float, default=4.0)
    watch_parser.add_argument("--status", default="online")
    watch_parser.add_argument("--note", default="watching")
    watch_parser.add_argument("--mark-read", action="store_true")
    watch_parser.set_defaults(func=watch)

    return parser


def main(argv: list[str] | None = None) -> int:
    parser = build_parser()
    args = parser.parse_args(argv)
    if hasattr(args, "id") and not args.all and not args.id:
        parser.error("mark-read requires --id or --all")
    args.func(args)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
