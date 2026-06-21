#!/usr/bin/env python3
"""
Ingest EMERAULD wiki/ notes into LightRAG knowledge graph.
Run this after adding or updating wiki notes.

Usage:
    python ingest.py            # ingest all wiki notes
    python ingest.py --changed  # ingest only recently modified files
"""

import asyncio
import argparse
import os
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
_IMPORT_ERROR: Exception | None = None
try:
    from lightrag_config import make_rag, VAULT_ROOT
except Exception as e:  # keep CLI usable even when deps are missing
    make_rag = None  # type: ignore[assignment]
    VAULT_ROOT = Path(__file__).resolve().parents[1]  # type: ignore[assignment]
    _IMPORT_ERROR = e

WIKI_DIR = VAULT_ROOT / "wiki"


def load_note(path: Path) -> str:
    """Load a note, prepending its title as context."""
    text = path.read_text(encoding="utf-8", errors="ignore")
    return f"# FILE: {path.name}\n\n{text}"


def note_id(path: Path) -> str:
    """Build a stable unique ID relative to the wiki root."""
    return str(path.relative_to(WIKI_DIR).with_suffix("")).replace("\\", "/")


async def ingest_all():
    if make_rag is None:
        msg = (
            "LightRAG ingest deps are not available in this Python environment.\n"
            "Try running in the EMERAULD lightrag venv (WSL) or install deps locally.\n"
        )
        if _IMPORT_ERROR:
            msg += f"\nImport error: {_IMPORT_ERROR}\n"
        raise RuntimeError(msg)

    rag = make_rag()
    await rag.initialize_storages()
    try:
        notes = sorted(WIKI_DIR.rglob("*.md"))
        print(f"Found {len(notes)} wiki notes to ingest...")

        batch_size = 20
        for i in range(0, len(notes), batch_size):
            batch = notes[i : i + batch_size]
            texts = [load_note(p) for p in batch]
            ids = [note_id(p) for p in batch]
            await rag.ainsert(texts, ids=ids)
            print(f"  Ingested {min(i + batch_size, len(notes))}/{len(notes)}")

        print("Done. Knowledge graph built.")
    finally:
        await rag.finalize_storages()


async def ingest_changed(hours: int = 24):
    import time
    cutoff = time.time() - hours * 3600
    if make_rag is None:
        msg = (
            "LightRAG ingest deps are not available in this Python environment.\n"
            "Try running in the EMERAULD lightrag venv (WSL) or install deps locally.\n"
        )
        if _IMPORT_ERROR:
            msg += f"\nImport error: {_IMPORT_ERROR}\n"
        raise RuntimeError(msg)

    rag = make_rag()
    await rag.initialize_storages()
    try:
        notes = [p for p in WIKI_DIR.rglob("*.md") if p.stat().st_mtime > cutoff]
        if not notes:
            print(f"No notes modified in the last {hours}h.")
            return

        print(f"Ingesting {len(notes)} recently modified notes...")
        texts = [load_note(p) for p in notes]
        ids = [note_id(p) for p in notes]
        await rag.ainsert(texts, ids=ids)
        print("Done.")
    finally:
        await rag.finalize_storages()


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--changed", action="store_true", help="Only ingest recently modified notes")
    parser.add_argument("--hours", type=int, default=24, help="Hours window for --changed (default 24)")
    parser.add_argument(
        "--vectors",
        action="store_true",
        help="After ingest, rebuild the local vector store (.vector_store) for vsearch.py",
    )
    parser.add_argument(
        "--vector-full",
        action="store_true",
        help="When used with --vectors, do a full vector rebuild (otherwise incremental)",
    )
    args = parser.parse_args()

    try:
        if args.changed:
            asyncio.run(ingest_changed(args.hours))
        else:
            asyncio.run(ingest_all())

        if args.vectors:
            try:
                from embed import build_index, build_index_changed
            except Exception as e:
                raise RuntimeError(
                    "Vector store rebuild requested, but embed dependencies are missing. "
                    "Install numpy + sentence-transformers (and their deps), or run in the EMERAULD venv."
                ) from e
            if args.vector_full:
                build_index()
            else:
                build_index_changed()

    except RuntimeError as e:
        print(str(e).strip(), file=sys.stderr)
        sys.exit(2)
