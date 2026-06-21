#!/usr/bin/env python3
"""
Watch raw/ and auto-ingest new Markdown notes into LightRAG.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import logging
import time
from pathlib import Path

import httpx
from watchdog.events import FileSystemEventHandler
from watchdog.observers import Observer


ROOT_DIR = Path(__file__).resolve().parents[1]
MEM_DIR = ROOT_DIR / "mem"
LOG_PATH = MEM_DIR / "vault-watcher.log"
INGESTED_DB = MEM_DIR / "vault-watcher-ingested.json"
MEM_DIR.mkdir(parents=True, exist_ok=True)

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    handlers=[logging.FileHandler(LOG_PATH), logging.StreamHandler()],
)
LOGGER = logging.getLogger("vault-watcher")


def load_ingested() -> set[str]:
    if not INGESTED_DB.exists():
        return set()
    try:
        data = json.loads(INGESTED_DB.read_text(encoding="utf-8"))
    except json.JSONDecodeError:
        return set()
    return {str(item) for item in data}


def save_ingested(ingested: set[str]) -> None:
    INGESTED_DB.write_text(
        json.dumps(sorted(ingested), indent=2, ensure_ascii=True) + "\n",
        encoding="utf-8",
    )


def file_hash(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def ingest_to_lightrag(content: str, filename: str, lightrag_url: str) -> bool:
    try:
        response = httpx.post(
            f"{lightrag_url}/documents/text",
            json={"text": content, "description": filename},
            timeout=60,
        )
        response.raise_for_status()
        LOGGER.info("Ingested: %s", filename)
        return True
    except Exception as exc:  # noqa: BLE001
        LOGGER.error("Failed to ingest %s: %s", filename, exc)
        return False


class VaultHandler(FileSystemEventHandler):
    def __init__(self, lightrag_url: str, ingested: set[str]) -> None:
        self.lightrag_url = lightrag_url
        self.ingested = ingested

    def on_created(self, event) -> None:  # type: ignore[override]
        if not event.is_directory:
            self._process(Path(event.src_path))

    def on_modified(self, event) -> None:  # type: ignore[override]
        if not event.is_directory:
            self._process(Path(event.src_path))

    def _process(self, path: Path) -> None:
        if path.suffix.lower() != ".md" or "raw" not in path.parts:
            return
        if path.name == "README.md" or not path.exists():
            return

        try:
            digest = file_hash(path)
            if digest in self.ingested:
                return
            content = path.read_text(encoding="utf-8", errors="replace")
        except OSError:
            return

        if len(content.strip()) < 10:
            return

        if ingest_to_lightrag(content, path.name, self.lightrag_url):
            self.ingested.add(digest)
            save_ingested(self.ingested)


def scan_existing(vault_path: Path, lightrag_url: str, ingested: set[str]) -> None:
    raw_dir = vault_path / "raw"
    if not raw_dir.exists():
        return

    for note in raw_dir.rglob("*.md"):
        if note.name == "README.md":
            continue
        try:
            digest = file_hash(note)
        except OSError:
            continue
        if digest in ingested:
            continue
        content = note.read_text(encoding="utf-8", errors="replace")
        if len(content.strip()) < 10:
            continue
        if ingest_to_lightrag(content, note.name, lightrag_url):
            ingested.add(digest)

    save_ingested(ingested)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Watch raw/ and auto-ingest to LightRAG")
    parser.add_argument("--vault", default=".", help="Path to the vault root")
    parser.add_argument("--lightrag-url", default="http://localhost:9621")
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    vault_path = Path(args.vault).expanduser().resolve()
    raw_path = vault_path / "raw"

    if not raw_path.exists():
        LOGGER.error("raw/ not found under %s", vault_path)
        return 1

    ingested = load_ingested()
    LOGGER.info("Vault watcher starting")
    LOGGER.info("Vault      : %s", vault_path)
    LOGGER.info("LightRAG   : %s", args.lightrag_url)
    LOGGER.info("Known docs : %s", len(ingested))

    scan_existing(vault_path, args.lightrag_url, ingested)

    observer = Observer()
    observer.schedule(VaultHandler(args.lightrag_url, ingested), str(raw_path), recursive=True)
    observer.start()

    LOGGER.info("Watching raw/ for new notes...")
    try:
        while True:
            time.sleep(5)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
