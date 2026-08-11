from __future__ import annotations

import argparse
import shutil
from pathlib import Path


TEXT_SUFFIXES = {".txt", ".py", ".md", ".json", ".yaml", ".yml"}
SKIP_NAMES = {"rebuild_henry_bundle.py", "__pycache__"}

FILE_REPLACEMENTS = [
    ("PAPER BUILDER", "HENRY"),
    ("paper builder", "HENRY"),
    ("Martin Voice Spec", "HENRY Voice Spec"),
    ("Martin's voice CODE", "HENRY voice CODE"),
    ("martin_voice_optimizer", "henry_voice_optimizer"),
]

CONTENT_REPLACEMENTS = [
    ("PAPER BUILDER", "HENRY"),
    ("paper builder", "HENRY"),
    ("Martin Voice Spec", "HENRY Voice Spec"),
    ("Martin's voice CODE", "HENRY voice CODE"),
    ("Replicate Martin academic and scholarly voice", "Replicate HENRY academic and scholarly voice"),
    ("Martin Voice Profiler + Operator Flagging", "HENRY Voice Profiler + Operator Flagging"),
    ("# martin_voice_optimizer.py", "# henry_voice_optimizer.py"),
    ("martin_voice_optimizer.py", "henry_voice_optimizer.py"),
]


def rename_text(value: str, replacements: list[tuple[str, str]]) -> str:
    updated = value
    for old, new in replacements:
        updated = updated.replace(old, new)
    return updated


def copy_bundle(source_dir: Path, output_dir: Path) -> None:
    if output_dir.exists():
        shutil.rmtree(output_dir)
    output_dir.mkdir(parents=True)

    for source_path in sorted(source_dir.iterdir()):
        if source_path.name == output_dir.name or source_path.name in SKIP_NAMES:
            continue

        target_name = rename_text(source_path.name, FILE_REPLACEMENTS)
        target_path = output_dir / target_name

        if source_path.is_dir():
            shutil.copytree(source_path, target_path)
            continue

        if source_path.suffix.lower() in TEXT_SUFFIXES:
            text = source_path.read_text(encoding="utf-8")
            target_path.write_text(rename_text(text, CONTENT_REPLACEMENTS), encoding="utf-8")
            continue

        shutil.copy2(source_path, target_path)


def main() -> None:
    parser = argparse.ArgumentParser(description="Rebuild the paper.builder bundle as HENRY.")
    parser.add_argument(
        "--source",
        default=".",
        help="Source bundle directory. Defaults to the current directory.",
    )
    parser.add_argument(
        "--output",
        default="../HENRY",
        help="Output directory for the rebuilt HENRY bundle.",
    )
    args = parser.parse_args()

    source_dir = Path(args.source).resolve()
    output_dir = Path(args.output).resolve()

    if not source_dir.is_dir():
        raise SystemExit(f"Source directory not found: {source_dir}")

    copy_bundle(source_dir, output_dir)
    print(f"Built HENRY bundle at {output_dir}")


if __name__ == "__main__":
    main()
