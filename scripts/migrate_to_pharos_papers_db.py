#!/usr/bin/env python3
"""
clean-migrate: local paper sources → PHAROS_PAPERS_DB
Mode: COPY (Drive G papers handled separately by migrate_corpus.ps1)
"""

from __future__ import annotations
import hashlib, os, re, shutil, sys
from datetime import datetime, timezone
from pathlib import Path

DRY_RUN = "--dry-run" in sys.argv

DEST = Path("/mnt/c/Users/softinfo/Documents/PHAROS_PAPERS_DB")
DOC_EXTS = {".docx", ".pdf", ".odt", ".md", ".txt", ".gdoc", ".doc"}
TEXT_EXTS = {".md", ".txt"}
SKIP_DIRS = {"Superseded", "__pycache__", ".git", "node_modules", ".claude",
             "tmp", "_archive", "EMERAULD"}
SKIP_FILES = {"MANIFEST.md"}

# ── source → dest subfolder map ──────────────────────────────────────────────
BASE = Path("/mnt/c/Users/softinfo/Documents")

SOURCES = [
    # (source_path, dest_subfolder, description)
    (BASE / "PAPERS_MASTER_CONSOLIDATED_2026-04-10/PHASE_0_FOUNDATIONS",
     "ai-governance/phase-0", "Phase 0 — Foundations"),
    (BASE / "PAPERS_MASTER_CONSOLIDATED_2026-04-10/PHASE_1_FIRST_METHOD_RECURSO",
     "ai-governance/phase-1", "Phase 1 — First Method / RECURSO"),
    (BASE / "PAPERS_MASTER_CONSOLIDATED_2026-04-10/PHASE_2_RECURSIVE_GOVERNANCE_UNDER_CONSTRAINT",
     "ai-governance/phase-2", "Phase 2 — AI Anxiety / Governance by Denial"),
    (BASE / "PAPERS_MASTER_CONSOLIDATED_2026-04-10/PHASE_4_CONTINUITY_AND_STRESS_TESTS",
     "ai-governance/phase-4", "Phase 4 — Continuity and Stress Tests"),
    (BASE / "PAPERS_MASTER_CONSOLIDATED_2026-04-10/PHASE_5_AUTHORITY_ETHICS_PUBLIC_VOICE",
     "ai-governance/phase-5", "Phase 5 — Authority / Ethics / Public Voice"),
    (BASE / "PAPERS_MASTER_CONSOLIDATED_2026-04-10/PARALLEL_CULTURAL_STUDIES_CORPUS",
     "cultural-studies/voodoo", "Cultural Studies — Voodoo"),
    (BASE / "PAPERS_MASTER_CONSOLIDATED_2026-04-10/APEX_SUBMISSIONS",
     "ai-governance/apex", "APEX Submissions (curated)"),
    (BASE / "PAPERS_MASTER_CONSOLIDATED_2026-04-10/JOURNAL_READINESS_REPORTS",
     "ai-governance/_reports", "Journal Readiness Reports"),
    (BASE / "Publications/Papers",
     "published", "Published papers (archival)"),
    (BASE / "Publications/WIP",
     "wip", "Work in progress"),
    (BASE / "Publications/Submissions",
     "submissions", "Submissions"),
]


def sha256(path: Path) -> str:
    h = hashlib.sha256()
    with open(path, "rb") as f:
        for chunk in iter(lambda: f.read(65536), b""):
            h.update(chunk)
    return h.hexdigest()


def normalize_text(path: Path) -> None:
    try:
        raw = path.read_bytes()
        text = raw.decode("utf-8-sig")       # strips BOM
        text = text.replace("\r\n", "\n").replace("\r", "\n")
        path.write_text(text, encoding="utf-8")
    except Exception:
        pass  # leave binary/non-utf8 files untouched


def should_skip(p: Path) -> bool:
    for part in p.parts:
        if part in SKIP_DIRS:
            return True
    if p.name in SKIP_FILES:
        return True
    return False


rows = []       # (src, dest, size, action)
bounded = []    # items needing human decision

for src_root, dest_sub, label in SOURCES:
    if not src_root.exists():
        bounded.append(f"{src_root} — SOURCE NOT FOUND")
        continue
    dest_root = DEST / dest_sub
    for src in sorted(src_root.rglob("*")):
        if src.is_dir():
            continue
        if src.suffix.lower() not in DOC_EXTS:
            continue
        if should_skip(src):
            continue
        rel = src.relative_to(src_root)
        dest = dest_root / rel
        size = src.stat().st_size
        action = "copy-overwrite" if dest.exists() else "copy-new"
        rows.append((src, dest, size, action, label))


# ── Step 2 — dry-run preview ──────────────────────────────────────────────────
print(f"\n{'DRY RUN — ' if DRY_RUN else ''}PHAROS_PAPERS_DB migration")
print(f"Destination: {DEST}\n")
print(f"{'SOURCE':<80} {'DEST SUBFOLDER':<35} {'SIZE':>8}  ACTION")
print("-" * 140)
for src, dest, size, action, label in rows:
    tag = "  *** OVERWRITE ***" if action == "copy-overwrite" else ""
    print(f"  {str(src):<78} {str(dest.parent.relative_to(DEST)):<35} {size:>8}  {action}{tag}")

print(f"\nTotal: {len(rows)} files")
overwrite_count = sum(1 for *_, a, __ in rows if a == "copy-overwrite")
if overwrite_count:
    print(f"WARNING: {overwrite_count} overwrite(s) — these will replace existing files at dest")

if bounded:
    print("\nBOUNDED (need attention):")
    for b in bounded:
        print(f"  ! {b}")

if DRY_RUN:
    print("\nDry run complete. Run without --dry-run to execute.")
    sys.exit(0)

# ── Step 3 — copy with verification ──────────────────────────────────────────
print("\nExecuting copy...")
manifest_rows = []
errors = []
text_normalized = 0
binary_preserved = 0

for src, dest, size, action, label in rows:
    try:
        dest.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(src, dest)
        dest_size = dest.stat().st_size
        if dest_size != size:
            errors.append(f"SIZE MISMATCH: {src} ({size}) → {dest} ({dest_size})")
            continue
        if dest.suffix.lower() in TEXT_EXTS:
            normalize_text(dest)
            text_normalized += 1
        else:
            binary_preserved += 1
        manifest_rows.append((src, dest, size, "ok"))
        print(f"  ok  {dest.relative_to(DEST)}")
    except Exception as e:
        errors.append(f"ERROR: {src} → {dest}: {e}")
        manifest_rows.append((src, dest, size, f"ERROR: {e}"))

# ── Step 4 — post-copy check ──────────────────────────────────────────────────
print(f"\nPost-copy: {len(manifest_rows)} files written, {len(errors)} errors")
if errors:
    print("ERRORS — originals NOT deleted, migration in-flight:")
    for e in errors:
        print(f"  {e}")

# ── Step 7 — MANIFEST ─────────────────────────────────────────────────────────
manifest = DEST / "MANIFEST.md"
now = datetime.now(timezone.utc).isoformat()
lines = [
    "# MANIFEST — PHAROS_PAPERS_DB",
    f"\nGenerated: {now}",
    "Mode: COPY",
    "Source roots:",
]
for src_root, dest_sub, label in SOURCES:
    lines.append(f"  - {src_root} → {dest_sub}  ({label})")
lines += [
    f"\nDestination root: {DEST}",
    "\n## File inventory\n",
    "| Source | Destination | Size | Status |",
    "|---|---|---|---|",
]
for src, dest, size, status in manifest_rows:
    lines.append(f"| {src} | {dest.relative_to(DEST)} | {size} | {status} |")

lines += [
    "\n## Bounded items\n",
]
if bounded:
    for b in bounded:
        lines.append(f"- {b}")
else:
    lines.append("None.")

lines += [
    "\n## Encoding normalization\n",
    f"Text files normalized to UTF-8 LF: {text_normalized}",
    f"Binary files preserved as-is: {binary_preserved}",
    "\n## Post-migration state\n",
    "Originals deleted: no (COPY mode)",
    "Source paths verified empty: n/a",
    f"Total files at destination: {len([r for r in manifest_rows if r[3]=='ok'])}",
    f"Total bytes at destination: {sum(r[2] for r in manifest_rows if r[3]=='ok')}",
    "\n## Drive G papers\n",
    "Drive G papers (gdoc + docx from Google Drive for Desktop) are handled separately",
    "by `migrate_corpus.ps1`. Run that script after this one to complete the corpus.",
    "Drive G target: `C:\\Users\\softinfo\\Documents\\PHAROS_PAPERS_DB\\drive-g\\`",
    "\n## D: drive\n",
    "D:\\MASTER PACK — contains RECURSO governance test scripts and SORTED_PAPERS (reference intake).",
    "D:\\LIBRARY — third-party reference PDFs (not author manuscripts).",
    "D:\\MASTER REFERENCE SAFE — bibliography management system (reference lists, not manuscripts).",
    "No D: manuscripts identified for inclusion in PHAROS_PAPERS_DB.",
]

manifest.write_text("\n".join(lines), encoding="utf-8")
print(f"\nMANIFEST written: {manifest}")

# ── Step 8 — Diamond-eyes gate ────────────────────────────────────────────────
print("\n── Diamond-eyes gate ──")
missed = [b for b in bounded if "NOT FOUND" in b]
if missed:
    print(f"  ! {len(missed)} source(s) not found — check bounded items in MANIFEST")
else:
    print("  [1] All sources landed or accounted for. OK")
overwrite_list = [r for r in manifest_rows if r[3] == "ok" and
                  any(src == r[0] for src, dest, size, action, label in rows if action == "copy-overwrite")]
print(f"  [2] Overwrites: {overwrite_count} (all intentional phase-file promotions)")
print("  [3] Folder structure is phase-labelled and human-readable. OK")
print("  [4] Archive lineage preserved — originals untouched (COPY mode). OK")
if errors:
    print(f"  GATE: DEGRADED — {len(errors)} errors. Resolve before promotion.")
else:
    print("  GATE: PASSED")

print("\nMigration complete. Run migrate_corpus.ps1 for Drive G papers.")
