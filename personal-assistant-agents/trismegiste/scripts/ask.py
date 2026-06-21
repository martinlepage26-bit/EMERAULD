#!/usr/bin/env python3
"""
ask.py — Query your personal assistant from the terminal.

Usage:
    python3 ask.py "What did I write about project X?"
    python3 ask.py --mode hybrid "Summarize my notes on health"
    python3 ask.py --vault-only "What skills do I have?"
    echo "..." | python3 ask.py --stdin
"""

import argparse
import sys
from pathlib import Path

import httpx

LIGHTRAG_URL = "http://localhost:9621"
VAULT_DIR = Path("~/personal-assistant/vault").expanduser()


def query_lightrag(question: str, mode: str = "hybrid") -> str:
    """Query LightRAG with a question."""
    try:
        resp = httpx.post(
            f"{LIGHTRAG_URL}/query",
            json={"query": question, "mode": mode},
            timeout=60,
        )
        resp.raise_for_status()
        return resp.json().get("response", "No response from LightRAG.")
    except httpx.ConnectError:
        return "⚠️  LightRAG not running. Start with: systemctl --user start lightrag"
    except Exception as e:
        return f"⚠️  LightRAG error: {e}"


def query_vault(question: str) -> str:
    """Simple grep-based vault search (no RAG)."""
    results = []
    q = question.lower()
    for folder in ["wiki", "skills", "raw"]:
        folder_path = VAULT_DIR / folder
        if not folder_path.exists():
            continue
        for md in folder_path.glob("*.md"):
            content = md.read_text(encoding="utf-8", errors="replace")
            if any(word in content.lower() for word in q.split()):
                results.append(f"\n## {md.relative_to(VAULT_DIR)}\n{content[:500]}...")
    if not results:
        return "No matching notes found in vault."
    return "\n".join(results[:5])


def main():
    parser = argparse.ArgumentParser(description="Query your personal assistant")
    parser.add_argument("question", nargs="?", help="Your question")
    parser.add_argument(
        "--mode",
        choices=["naive", "local", "global", "hybrid", "mix"],
        default="hybrid",
        help="LightRAG retrieval mode (default: hybrid)",
    )
    parser.add_argument(
        "--vault-only",
        action="store_true",
        help="Skip LightRAG, search vault files directly",
    )
    parser.add_argument(
        "--stdin", action="store_true", help="Read question from stdin"
    )
    args = parser.parse_args()

    if args.stdin or not sys.stdin.isatty():
        question = sys.stdin.read().strip()
    elif args.question:
        question = args.question
    else:
        print("Usage: python3 ask.py 'your question'")
        sys.exit(1)

    print(f"\n🔍 Query: {question}")
    print(f"   Mode: {'vault-only' if args.vault_only else args.mode}\n")
    print("─" * 60)

    if args.vault_only:
        print(query_vault(question))
    else:
        print(query_lightrag(question, args.mode))

    print("─" * 60)


if __name__ == "__main__":
    main()
