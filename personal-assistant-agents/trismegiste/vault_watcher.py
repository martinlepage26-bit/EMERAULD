#!/usr/bin/env python3
"""
vault_watcher.py — 24/7 daemon that watches the vault's raw/ folder
and auto-ingests new .md files into LightRAG.

Usage:
    python3 vault_watcher.py --vault /path/to/vault --lightrag-url http://localhost:9621
"""

import argparse
import hashlib
import json
import logging
import time
from pathlib import Path

import httpx
from watchdog.events import FileSystemEventHandler
from watchdog.observers import Observer

LOG_FILE = Path("~/.vault-watcher.log").expanduser()

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    handlers=[
        logging.FileHandler(LOG_FILE),
        logging.StreamHandler(),
    ],
)
log = logging.getLogger("vault-watcher")

INGESTED_DB = Path("~/.vault-watcher-ingested.json").expanduser()


def load_ingested() -> set:
    if INGESTED_DB.exists():
        return set(json.loads(INGESTED_DB.read_text()))
    return set()


def save_ingested(ingested: set):
    INGESTED_DB.write_text(json.dumps(list(ingested)))


def file_hash(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def ingest_to_lightrag(content: str, filename: str, lightrag_url: str) -> bool:
    """Send a document to LightRAG for indexing."""
    try:
        resp = httpx.post(
            f"{lightrag_url}/documents/text",
            json={"text": content, "description": filename},
            timeout=60,
        )
        resp.raise_for_status()
        log.info(f"Ingested: {filename}")
        return True
    except Exception as e:
        log.error(f"Failed to ingest {filename}: {e}")
        return False


class VaultHandler(FileSystemEventHandler):
    def __init__(self, lightrag_url: str, ingested: set):
        self.lightrag_url = lightrag_url
        self.ingested = ingested

    def on_created(self, event):
        if event.is_directory:
            return
        path = Path(event.src_path)
        if path.suffix == ".md":
            self._process(path)

    def on_modified(self, event):
        if event.is_directory:
            return
        path = Path(event.src_path)
        if path.suffix == ".md":
            self._process(path)

    def _process(self, path: Path):
        h = file_hash(path)
        if h in self.ingested:
            return
        content = path.read_text(encoding="utf-8", errors="replace")
        if len(content.strip()) < 10:
            return
        if ingest_to_lightrag(content, path.name, self.lightrag_url):
            self.ingested.add(h)
            save_ingested(self.ingested)


def scan_existing(raw_dir: Path, lightrag_url: str, ingested: set):
    """On startup, ingest any raw/ notes not yet indexed."""
    if not raw_dir.exists():
        log.warning(f"raw/ dir not found: {raw_dir}")
        return
    for md in raw_dir.rglob("*.md"):
        if md.name == "README.md":
            continue
        h = file_hash(md)
        if h not in ingested:
            content = md.read_text(encoding="utf-8", errors="replace")
            if ingest_to_lightrag(content, md.name, lightrag_url):
                ingested.add(h)
    save_ingested(ingested)


def main():
    parser = argparse.ArgumentParser(description="Vault raw/ -> LightRAG watcher")
    parser.add_argument("--vault", required=True, help="Path to your Obsidian vault")
    parser.add_argument("--raw-folder", default="raw", help="Name of the raw folder inside vault (default: raw)")
    parser.add_argument("--lightrag-url", default="http://localhost:9621")
    args = parser.parse_args()

    vault_path = Path(args.vault).expanduser().resolve()
    if not vault_path.exists():
        log.error(f"Vault not found: {vault_path}")
        return

    raw_dir = vault_path / args.raw_folder

    ingested = load_ingested()
    log.info(f"Vault watcher starting. Vault: {vault_path}")
    log.info(f"  Watching: {raw_dir}")
    log.info(f"  LightRAG: {args.lightrag_url}")
    log.info(f"  Already ingested: {len(ingested)} notes")

    scan_existing(raw_dir, args.lightrag_url, ingested)

    handler = VaultHandler(args.lightrag_url, ingested)
    observer = Observer()
    observer.schedule(handler, str(raw_dir), recursive=True)
    observer.start()

    log.info("Watching raw/ for new notes...")
    try:
        while True:
            time.sleep(5)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()


if __name__ == "__main__":
    main()
