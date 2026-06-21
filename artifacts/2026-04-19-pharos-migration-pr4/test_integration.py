#!/usr/bin/env python3
"""
test_integration.py
───────────────────
PHAROS Suite — End-to-end integration test

Runs every archive script in the correct operational order,
verifies all outputs, and reports a final pass/fail status.

Run from: pharos-suite/
  python test_integration.py

Requires: test_fixtures/ directory with synthetic CSVs and archive files.
"""

import csv
import json
import os
import subprocess
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).parent
SCRIPTS = REPO_ROOT / "scripts"
FIXTURES = REPO_ROOT / "test_fixtures"
WORK_DIR = Path("/tmp/pharos_integration_test")

PASS = "✓ PASS"
FAIL = "✗ FAIL"
results: list[tuple[str, str, str]] = []


def run(label: str, cmd: list[str], expect_exit: int = 0, **kwargs) -> subprocess.CompletedProcess:
    """Run a command and record pass/fail."""
    r = subprocess.run(cmd, capture_output=True, text=True, **kwargs)
    if r.returncode == expect_exit:
        results.append((label, PASS, ""))
    else:
        detail = (r.stderr or r.stdout or "")[:200]
        results.append((label, FAIL, f"exit={r.returncode}, expected={expect_exit}: {detail}"))
    return r


def check(label: str, condition: bool, detail: str = ""):
    results.append((label, PASS if condition else FAIL, detail if not condition else ""))


def main():
    WORK_DIR.mkdir(parents=True, exist_ok=True)

    manifest = FIXTURES / "00_ARCHIVE_METADATA_MANIFEST.csv"
    inventory = FIXTURES / "00_archive_inventory.csv"
    archive_dir = FIXTURES / "archive_files"

    print("═" * 70)
    print("PHAROS SUITE — END-TO-END INTEGRATION TEST")
    print("═" * 70)

    # ── 1. Backend tests ──────────────────────────────────────────────────
    # --basetemp pins pytest's tempdir to /tmp/pharos_pytest_work so cleanup
    # can't fail on filesystems that restrict rmdir inside the repo tree
    # (e.g. certain read-only or sandboxed mounts). On normal dev machines
    # this is a no-op. -p no:cacheprovider prevents .pytest_cache pollution.
    pytest_tmp = Path("/tmp/pharos_pytest_work")
    pytest_tmp.mkdir(parents=True, exist_ok=True)
    print("\n[1/7] Backend test suite...")
    run(
        "Backend tests (pytest)",
        [sys.executable, "-m", "pytest",
         "backend/tests/test_backend_hardening.py",
         "-v", "--tb=short",
         f"--basetemp={pytest_tmp}",
         "-p", "no:cacheprovider"],
        cwd=REPO_ROOT,
        env={**os.environ, "MONGO_URL": "mongodb://localhost:27017", "DB_NAME": "pharos_test", "ENVIRONMENT": "test"},
    )

    # ── 2. Server hardening patch check ───────────────────────────────────
    print("[2/7] Server hardening patch check...")
    r = run(
        "Server hardening check",
        [sys.executable, "server_hardening_patch.py", "--check"],
        cwd=REPO_ROOT / "backend",
    )
    if r.returncode == 0:
        check("Hardening: all checks pass", "All hardening checks pass" in r.stdout, r.stdout[:200])

    # ── 3. Pipeline filter — human gate violation ─────────────────────────
    print("[3/7] Pipeline filter — human gate enforcement...")
    run(
        "Pipeline filter: human gate violation → exit 1",
        [sys.executable, str(SCRIPTS / "pharos_pipeline_filter.py"),
         "--manifest", str(manifest),
         "--inventory", str(inventory),
         "--output", str(WORK_DIR / "clean_manifest.csv"),
         "--dry-run"],
        expect_exit=1,
    )

    # ── 4. Pipeline filter — with gate cleared ────────────────────────────
    print("[4/7] Pipeline filter — clean run after gate cleared...")
    # Create fixed manifest
    fixed_manifest = WORK_DIR / "manifest_fixed.csv"
    with open(manifest, newline="", encoding="utf-8-sig") as f:
        rows = list(csv.DictReader(f))
        fieldnames = list(rows[0].keys()) if rows else []

    for row in rows:
        fn = row.get("filename", "")
        if "ai-anxiety" in fn:
            row["action"] = "PRESERVE_AND_LIGHTLY_CLEAN"
            row["human_gate_cleared"] = "true"

    if "human_gate_cleared" not in fieldnames:
        fieldnames.append("human_gate_cleared")
    with open(fixed_manifest, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames, extrasaction="ignore")
        writer.writeheader()
        writer.writerows(rows)

    r = run(
        "Pipeline filter: clean run → exit 0",
        [sys.executable, str(SCRIPTS / "pharos_pipeline_filter.py"),
         "--manifest", str(fixed_manifest),
         "--inventory", str(inventory),
         "--output", str(WORK_DIR / "clean_manifest.csv"),
         "--dry-run"],
        expect_exit=0,
    )
    if r.returncode == 0:
        check("Pipeline filter: exclusion count correct", "Excluded (contaminated)" in r.stdout)

    # ── 5. Topology audit ─────────────────────────────────────────────────
    print("[5/7] Topology audit...")
    topo_report = WORK_DIR / "topology_audit_report.md"
    r = run(
        "Topology audit: full scan",
        [sys.executable, str(SCRIPTS / "topology_audit.py"),
         "--inventory", str(inventory),
         "--manifest", str(fixed_manifest),
         "--archive-dir", str(archive_dir),
         "--output", str(topo_report)],
    )
    if r.returncode == 0:
        check("Topology: report file created", topo_report.exists())
        topo_hits = WORK_DIR / "topology_keyword_hits.csv"
        check("Topology: keyword hits found", topo_hits.exists() and topo_hits.stat().st_size > 0,
              "Expected non-empty topology_keyword_hits.csv")
        if topo_hits.exists():
            with open(topo_hits, encoding="utf-8") as f:
                hit_count = sum(1 for _ in csv.reader(f)) - 1
            check(f"Topology: hit count > 0 (got {hit_count})", hit_count > 0)

    # ── 6. CompassAI/AurorAI extractor ────────────────────────────────────
    print("[6/7] CompassAI/AurorAI extractor...")
    extract_dir = WORK_DIR / "extracted_evidence"
    r = run(
        "Extractor: moving_parts.txt",
        [sys.executable, str(SCRIPTS / "compassai_aurorai_extractor.py"),
         "--source", str(archive_dir / "moving_parts.txt"),
         "--output-dir", str(extract_dir)],
    )
    if r.returncode == 0:
        check("Extractor: provenance artifact created",
              (extract_dir / "compassai_aurorai_implementation_references.md").exists())
        check("Extractor: keyword hits CSV created",
              (extract_dir / "compassai_aurorai_keyword_hits.csv").exists())
        check("Extractor: merge clearance report created",
              (extract_dir / "moving_parts_merge_clearance.txt").exists())
        clearance = (extract_dir / "moving_parts_merge_clearance.txt").read_text()
        check("Extractor: merge clearance GRANTED", "MERGE CLEARANCE: GRANTED" in clearance)

    # ── 7. Regulatory corpus bootstrap ────────────────────────────────────
    print("[7/7] Regulatory corpus bootstrap...")
    reg_dir = WORK_DIR / "regulatory_corpus"
    r = run(
        "Regulatory bootstrap",
        [sys.executable, str(SCRIPTS / "regulatory_corpus_bootstrap.py"),
         "--output-dir", str(reg_dir)],
    )
    if r.returncode == 0:
        reg_csv = reg_dir / "ai_governance_regulatory_docs.csv"
        check("Regulatory: CSV created", reg_csv.exists())
        if reg_csv.exists():
            with open(reg_csv, encoding="utf-8") as f:
                doc_count = sum(1 for _ in csv.reader(f)) - 1
            check(f"Regulatory: 5 documents indexed (got {doc_count})", doc_count == 5)

        kw_config = reg_dir / "regulatory_keyword_extraction_config.json"
        check("Regulatory: keyword config created", kw_config.exists())
        if kw_config.exists():
            config = json.loads(kw_config.read_text())
            check("Regulatory: keyword tiers present", "keyword_tiers" in config)

        checklist = reg_dir / "regulatory_compliance_audit_checklist.md"
        check("Regulatory: compliance checklist created", checklist.exists())

    # ── Results ───────────────────────────────────────────────────────────
    print("\n" + "═" * 70)
    print("INTEGRATION TEST RESULTS")
    print("═" * 70)

    passed = 0
    failed = 0
    for label, status, detail in results:
        print(f"  {status}  {label}")
        if detail:
            print(f"         {detail}")
        if status == PASS:
            passed += 1
        else:
            failed += 1

    print(f"\n  {passed} passed, {failed} failed, {passed + failed} total")
    print("═" * 70)

    if failed > 0:
        print("\nINTEGRATION TEST: FAILED")
        sys.exit(1)
    else:
        print("\nINTEGRATION TEST: ALL PASSED")
        sys.exit(0)


if __name__ == "__main__":
    main()
