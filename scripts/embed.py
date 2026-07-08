#!/usr/bin/env python3
"""
Build the EMERAULD local vector store from wiki/, maps/, projects/, and graph/ notes.
Embeddings are saved to .vector_store/ (numpy matrix + path index).

Usage:
    python embed.py           # full rebuild
    python embed.py --changed # incremental (only notes modified in last 24h)
    python embed.py --check   # print store state without rebuilding

Importable API:
    from embed import build_index, build_index_changed
"""

import json
import sys
import time
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))

from lightrag_config import VAULT_ROOT, get_embed_model

CORPUS_DIRS = [
    "wiki", "maps", "projects", "graph",
    "Areas", "Resources", "Inbox", "artifacts", "governance", "memory",
    "archive", "hephaistos", "PEER-REVIEW", "Publications",
]
EXCLUDED_PARTS = {"node_modules", ".git", ".trash", ".obsidian"}
STORE_DIR = VAULT_ROOT / ".vector_store"
EMBED_FILE = STORE_DIR / "embeddings.npy"
PATHS_FILE = STORE_DIR / "paths.json"
META_FILE = STORE_DIR / "meta.json"


def _load_note(path: Path) -> str:
    return path.read_text(encoding="utf-8", errors="ignore")


def _all_notes() -> list[Path]:
    return sorted(
        p
        for d in CORPUS_DIRS
        for p in (VAULT_ROOT / d).rglob("*.md")
        if (VAULT_ROOT / d).exists()
        and not (set(p.relative_to(VAULT_ROOT).parts) & EXCLUDED_PARTS)
    )


def build_index(notes: list[Path] | None = None, verbose: bool = True) -> None:
    """Full rebuild of the vector store for the given notes (default: all wiki notes)."""
    import numpy as np

    if notes is None:
        notes = _all_notes()

    if not notes:
        print("No wiki notes found.", file=sys.stderr)
        return

    model = get_embed_model()
    texts = [_load_note(p) for p in notes]

    if verbose:
        print(f"Embedding {len(notes)} notes...")

    embeddings = model.encode(texts, normalize_embeddings=True, show_progress_bar=verbose)
    matrix = np.array(embeddings, dtype=np.float32)

    STORE_DIR.mkdir(exist_ok=True)
    np.save(EMBED_FILE, matrix)
    PATHS_FILE.write_text(
        json.dumps([str(p.relative_to(VAULT_ROOT)) for p in notes], ensure_ascii=False, indent=2),
        encoding="utf-8",
    )
    META_FILE.write_text(
        json.dumps({"built_at": time.time(), "count": len(notes)}, indent=2),
        encoding="utf-8",
    )

    if verbose:
        print(f"Vector store built: {len(notes)} notes → {EMBED_FILE}")


def build_index_changed(hours: int = 24, verbose: bool = True) -> None:
    """Incremental rebuild: embed notes modified in the last `hours` hours."""
    import numpy as np

    cutoff = time.time() - hours * 3600
    changed = [p for p in _all_notes() if p.stat().st_mtime > cutoff]

    if not changed:
        if verbose:
            print(f"No notes modified in the last {hours}h. Store unchanged.")
        return

    # Load existing store if present, otherwise do a full build.
    if not EMBED_FILE.exists() or not PATHS_FILE.exists():
        if verbose:
            print("No existing store — doing full build.")
        build_index(verbose=verbose)
        return

    existing_paths = json.loads(PATHS_FILE.read_text(encoding="utf-8"))
    existing_matrix = np.load(EMBED_FILE)

    path_to_idx = {p: i for i, p in enumerate(existing_paths)}
    model = get_embed_model()

    changed_rel = [str(p.relative_to(VAULT_ROOT)) for p in changed]
    new_texts = [_load_note(p) for p in changed]

    if verbose:
        print(f"Re-embedding {len(changed)} changed notes...")

    new_embeddings = model.encode(new_texts, normalize_embeddings=True, show_progress_bar=verbose)

    # Update existing rows or append new ones.
    rows = list(existing_matrix)
    paths = list(existing_paths)

    for rel, emb in zip(changed_rel, new_embeddings):
        if rel in path_to_idx:
            rows[path_to_idx[rel]] = emb
        else:
            rows.append(emb)
            paths.append(rel)

    matrix = np.array(rows, dtype=np.float32)
    np.save(EMBED_FILE, matrix)
    PATHS_FILE.write_text(
        json.dumps(paths, ensure_ascii=False, indent=2), encoding="utf-8"
    )
    META_FILE.write_text(
        json.dumps({"built_at": time.time(), "count": len(paths)}, indent=2),
        encoding="utf-8",
    )

    if verbose:
        print(f"Updated {len(changed)} notes. Store now has {len(paths)} entries.")


def check_store() -> None:
    if not EMBED_FILE.exists():
        print("Vector store not built yet. Run: python embed.py")
        return

    meta = json.loads(META_FILE.read_text()) if META_FILE.exists() else {}
    count = meta.get("count", "?")
    built_at = meta.get("built_at")
    age = f"{(time.time() - built_at) / 3600:.1f}h ago" if built_at else "unknown age"
    print(f"Vector store: {count} notes, built {age}")
    print(f"  {EMBED_FILE}")


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser()
    parser.add_argument("--changed", action="store_true", help="Incremental: only re-embed recently modified notes")
    parser.add_argument("--hours", type=int, default=24, help="Hours window for --changed (default 24)")
    parser.add_argument("--check", action="store_true", help="Print store state without rebuilding")
    args = parser.parse_args()

    if args.check:
        check_store()
    elif args.changed:
        build_index_changed(hours=args.hours)
    else:
        build_index()
