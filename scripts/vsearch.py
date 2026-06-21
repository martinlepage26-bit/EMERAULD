#!/usr/bin/env python3
"""
Semantic search over the EMERAULD wiki using the local vector store.
Build the store first with: python embed.py

Usage:
    python vsearch.py "your question"
    python vsearch.py "your question" --top 10
    python vsearch.py "your question" --full      # print full note content
"""

import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))

from lightrag_config import VAULT_ROOT, get_embed_model

STORE_DIR = VAULT_ROOT / ".vector_store"
EMBED_FILE = STORE_DIR / "embeddings.npy"
PATHS_FILE = STORE_DIR / "paths.json"


def search(query: str, top_k: int = 5, full: bool = False) -> list[dict]:
    import numpy as np

    if not EMBED_FILE.exists():
        raise RuntimeError(
            "Vector store not built. Run: python scripts/embed.py"
        )

    matrix = np.load(EMBED_FILE)
    paths = json.loads(PATHS_FILE.read_text(encoding="utf-8"))

    model = get_embed_model()
    q_emb = model.encode([query], normalize_embeddings=True)[0]

    scores = matrix @ q_emb
    top_idxs = scores.argsort()[::-1][:top_k]

    results = []
    for idx in top_idxs:
        path = VAULT_ROOT / paths[idx]
        content = path.read_text(encoding="utf-8", errors="ignore") if full else None
        results.append({
            "title": path.stem,
            "path": str(path.relative_to(VAULT_ROOT)),
            "score": float(scores[idx]),
            "content": content,
        })

    return results


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser()
    parser.add_argument("query", help="Search query")
    parser.add_argument("--top", type=int, default=5, help="Number of results (default 5)")
    parser.add_argument("--full", action="store_true", help="Print full note content")
    args = parser.parse_args()

    try:
        results = search(args.query, top_k=args.top, full=args.full)
    except RuntimeError as e:
        print(str(e), file=sys.stderr)
        sys.exit(2)

    for i, r in enumerate(results, 1):
        print(f"\n{'='*60}")
        print(f"#{i}  [{r['score']:.4f}]  {r['title']}")
        print(f"    {r['path']}")
        if r["content"]:
            print()
            print(r["content"][:3000])
            if len(r["content"]) > 3000:
                print(f"... [{len(r['content'])} chars total]")
