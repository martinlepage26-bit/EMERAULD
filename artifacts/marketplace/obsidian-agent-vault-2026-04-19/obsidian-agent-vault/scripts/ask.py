#!/usr/bin/env python3
"""
Query the optional local agent runtime from the terminal.

Usage:
    python3 scripts/ask.py "What are my active projects?"
    python3 scripts/ask.py --mode global "Summarize my research notes"
    python3 scripts/ask.py --vault-only "What skills do I have?"
"""

from __future__ import annotations

import argparse
import os
import sys
from pathlib import Path

try:
    import httpx
except ModuleNotFoundError:
    root = Path(__file__).resolve().parents[1]
    venv_root = root / ".venv"
    venv_python = venv_root / "bin" / "python3"
    if venv_python.exists() and os.environ.get("VIRTUAL_ENV") != str(venv_root):
        os.execv(str(venv_python), [str(venv_python), __file__, *sys.argv[1:]])
    raise


ROOT_DIR = Path(__file__).resolve().parents[1]
VAULT_DIR = ROOT_DIR
LIGHTRAG_URL = os.environ.get("LIGHTRAG_URL", "http://localhost:9621")


def query_lightrag(question: str, mode: str = "hybrid") -> str:
    try:
        response = httpx.post(
            f"{LIGHTRAG_URL}/query",
            json={"query": question, "mode": mode},
            timeout=60,
        )
        response.raise_for_status()
        return response.json().get("response", "No response from LightRAG.")
    except httpx.ConnectError:
        return "LightRAG is not running. Start it with: systemctl --user start lightrag"
    except Exception as exc:  # noqa: BLE001
        return f"LightRAG error: {exc}"


def query_vault(question: str) -> str:
    results: list[str] = []
    words = [word for word in question.lower().split() if word]
    for folder in ("wiki", "skills", "raw"):
        folder_path = VAULT_DIR / folder
        if not folder_path.exists():
            continue
        for note in folder_path.rglob("*.md"):
            content = note.read_text(encoding="utf-8", errors="replace")
            lowered = content.lower()
            if any(word in lowered for word in words):
                excerpt = content[:500].strip()
                results.append(f"\n## {note.relative_to(VAULT_DIR)}\n{excerpt}...")
    if not results:
        return "No matching notes found in this vault."
    return "\n".join(results[:5])


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Query the optional local agent runtime")
    parser.add_argument("question", nargs="?", help="Your question")
    parser.add_argument(
        "--mode",
        choices=["naive", "local", "global", "hybrid", "mix"],
        default="hybrid",
        help="LightRAG retrieval mode",
    )
    parser.add_argument(
        "--vault-only",
        action="store_true",
        help="Skip LightRAG and search the vault files directly",
    )
    parser.add_argument("--stdin", action="store_true", help="Read the question from stdin")
    return parser.parse_args()


def main() -> int:
    args = parse_args()

    if args.question:
        question = args.question
    elif args.stdin or not sys.stdin.isatty():
        question = sys.stdin.read().strip()
    else:
        print("Usage: python3 scripts/ask.py 'your question'")
        return 1

    print(f"\nQuery: {question}")
    print(f"Mode : {'vault-only' if args.vault_only else args.mode}\n")
    print("-" * 60)

    if args.vault_only:
        print(query_vault(question))
    else:
        print(query_lightrag(question, args.mode))

    print("-" * 60)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
