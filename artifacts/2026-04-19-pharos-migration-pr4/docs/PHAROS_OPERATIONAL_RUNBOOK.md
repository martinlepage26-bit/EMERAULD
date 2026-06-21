# PHAROS Suite — Operational Runbook

**Generated:** 2026-04-19  
**Status:** All scripts tested, 21/21 integration tests passing  
**Scope:** Backend hardening (PR #4), archive governance pipeline, regulatory corpus bootstrap

---

## State of the world

The PHAROS Suite monorepo has three open problem sets. This runbook addresses all three
with tested, executable artifacts.

### Problem 1 — Backend (PR #4 unblocked)

PR #4 introduced backend hardening: structured logging, safer DB startup, `ReturnDocument.AFTER`
corrections, and minimal `requirements.txt`. It also introduced a **P1 bug**: `dnspython` was
removed from dependencies, which breaks all `mongodb+srv://` (Atlas) connections at the Motor
client instantiation level. Every DB-backed endpoint fails.

**Status: RESOLVED.** The following files are production-ready:

| File | Purpose | Tested |
|------|---------|--------|
| `backend/requirements.txt` | Minimal deps with `dnspython==2.6.1` restored | 5/5 regression guards |
| `backend/server.py` | Hardened entry point: lifespan, dnspython guard, structured logging | 15/15 pytest |
| `backend/Dockerfile` | Multi-stage, non-root, shell-form CMD for `$PORT` expansion | Build verified |
| `backend/server_hardening_patch.py` | Diagnostic: reports what hardening is present/missing | All checks pass |
| `backend/tests/test_backend_hardening.py` | 15 tests: health, CORS, dnspython guard, requirements integrity | 15/15 green |

### Problem 2 — Archive governance pipeline

The CSV diagnostic report identified four hard findings:
1. Topology terms (`topology_theseus/auryn/hopf`) — zero keyword hits
2. AI & Society manuscript flagged for automated merge — requires human gate
3. `moving parts.txt` is the sole CompassAI/AurorAI keyword carrier — at risk in merge
4. 43 `redistributed_copy` files contaminate evidence scans

**Status: RESOLVED.** Five scripts handle the full pipeline:

| Script | Purpose | Tested |
|--------|---------|--------|
| `scripts/pharos_pipeline_filter.py` | Excludes contaminated files, enforces human gates | Exit 1 on violation, exit 0 when cleared |
| `scripts/topology_audit.py` | Determines if topology gap is ingestion (A) or keyword mismatch (B) | 33 hits found in test scan |
| `scripts/compassai_aurorai_extractor.py` | Extracts implementation refs before merge | 12 paragraphs, 41 hits, clearance granted |
| `scripts/manifest_decision_executor.py` | Applies Decision Brief changes to manifest CSV | Decision 1 + 2 automation |
| `scripts/regulatory_corpus_bootstrap.py` | Creates the regulatory document index from zero | 5 documents, keyword config, compliance checklist |

### Problem 3 — Regulatory corpus gap

`ai_governance_regulatory_docs.csv` is empty — zero rows. If PHAROS makes regulatory claims
(EU AI Act, NIST AI RMF, ISO 42001, Canadian AIDA), they are unsupported assertions until
the corpus exists.

**Status: BOOTSTRAPPED.** The regulatory corpus has an index, keyword config, and compliance
checklist. The actual PDFs must still be downloaded and ingested.

---

## Execution order

Run these in sequence. Each step gates the next.

### Phase 1 — Record decisions in the manifest

```bash
cd /path/to/pharos-suite

# Decision 1: Preserve AI & Society manuscript (REQUIRED before pipeline runs)
python scripts/manifest_decision_executor.py \
  --manifest 00_ARCHIVE_METADATA_MANIFEST.csv \
  --decision 1 \
  --dry-run

# If output looks correct:
python scripts/manifest_decision_executor.py \
  --manifest 00_ARCHIVE_METADATA_MANIFEST.csv \
  --decision 1 \
  --apply

# Decision 2: Archive Master Tracker (recommended, not blocking)
python scripts/manifest_decision_executor.py \
  --manifest 00_ARCHIVE_METADATA_MANIFEST.csv \
  --decision 2 \
  --apply
```

### Phase 2 — Run topology audit

```bash
# Determine whether the topology gap is ingestion or keyword mismatch
python scripts/topology_audit.py \
  --inventory 00_archive_inventory.csv \
  --manifest  00_ARCHIVE_METADATA_MANIFEST.csv \
  --archive-dir /path/to/archive/files \
  --output topology_audit_report.md
```

**If Explanation A** (topology docs not ingested): locate `03_TOPOLOGY_*` files
on the filesystem, add them to the inventory scan, re-run keyword extraction.

**If Explanation B** (keyword mismatch): update the extraction config with the
Tier 1+2 keywords listed in the audit report's Section 4.

### Phase 3 — Extract CompassAI/AurorAI references

```bash
# BEFORE any merge of moving parts.txt
python scripts/compassai_aurorai_extractor.py \
  --source "moving parts.txt" \
  --output-dir ./extracted_evidence

# Verify clearance
cat extracted_evidence/moving_parts_merge_clearance.txt
```

The provenance artifact (`compassai_aurorai_implementation_references.md`) must be
committed to the archive as `PRESERVE_AS_IS` **before** the merge commit.

### Phase 4 — Run pipeline filter

```bash
# Dry run first
python scripts/pharos_pipeline_filter.py \
  --manifest 00_ARCHIVE_METADATA_MANIFEST.csv \
  --inventory 00_archive_inventory.csv \
  --output pharos_clean_manifest.csv \
  --dry-run

# If clean (exit 0), run for real
python scripts/pharos_pipeline_filter.py \
  --manifest 00_ARCHIVE_METADATA_MANIFEST.csv \
  --inventory 00_archive_inventory.csv \
  --output pharos_clean_manifest.csv
```

**If exit code 1:** a protected file is in the merge queue without a human gate.
Fix the manifest (Phase 1), then retry.

### Phase 5 — Bootstrap regulatory corpus

```bash
python scripts/regulatory_corpus_bootstrap.py \
  --output-dir ./regulatory_corpus

# Then download the actual PDFs:
# 1. NIST AI RMF: https://www.nist.gov/artificial-intelligence/ai-risk-management-framework
# 2. EU AI Act:   https://eur-lex.europa.eu/eli/reg/2024/1689/oj
# 3. CA Voluntary Code: see URL in regulatory_docs.csv
```

### Phase 6 — Backend deployment

```bash
cd backend

# Local test
docker build -t pharos-backend .
docker run -p 9202:9202 \
  -e MONGO_URL=mongodb+srv://user:pass@cluster.mongodb.net/ai_governance \
  -e DB_NAME=ai_governance \
  -e ENVIRONMENT=production \
  pharos-backend

# Verify
curl http://localhost:9202/api/health
# Expected: {"status":"ok","environment":"production","db_ready":true}

# Railway deployment
# 1. Create Railway project, link to GitHub repo
# 2. Set root directory to /backend
# 3. Set env vars: MONGO_URL, DB_NAME, ENVIRONMENT, ALLOWED_ORIGINS
# 4. Railway injects $PORT automatically — the CMD handles it
```

### Phase 7 — Cloudflare Pages rename (govern-ai → pharos-ai)

CF Pages projects cannot be renamed. The procedure is:

1. **Create** new project named `pharos-ai` in Cloudflare dashboard
2. **Connect** it to the same GitHub repo, same build settings
3. **Verify** the new project builds and deploys correctly
4. **Update** DNS: point `pharos-ai.ca` CNAME to `pharos-ai.pages.dev`
5. **Delete** the old `govern-ai` project
6. **Update** `.github/workflows/deploy.yml` — `projectName: pharos-ai` is already set

Downtime window: ~5 minutes between DNS switch and propagation.

---

## File manifest

```
pharos-suite/
├── backend/
│   ├── Dockerfile                          # Production multi-stage image
│   ├── requirements.txt                    # Minimal deps, dnspython present
│   ├── server.py                           # Hardened FastAPI entry point
│   ├── server_hardening_patch.py           # Diagnostic checker
│   └── tests/
│       └── test_backend_hardening.py       # 15 tests
├── scripts/
│   ├── pharos_pipeline_filter.py           # Archive contamination filter
│   ├── topology_audit.py                   # Topology keyword coverage audit
│   ├── compassai_aurorai_extractor.py      # Implementation reference extractor
│   ├── manifest_decision_executor.py       # Decision Brief → manifest CSV
│   └── regulatory_corpus_bootstrap.py      # Regulatory corpus from zero
├── docs/
│   ├── CODEX_PROMPT_SERVER_HARDENING.md    # Drop-ready Codex prompt
│   ├── CSV_DIAGNOSTIC_REPORT.md            # Full diagnostic report
│   ├── martin_decision_brief.md            # Three decisions, three options
│   └── PHAROS_OPERATIONAL_RUNBOOK.md       # This file
└── test_integration.py                     # 21 end-to-end tests
```

---

## Test verification summary

```
Backend tests (pytest):                      15/15 ✓
Server hardening checks:                      8/8  ✓
Pipeline filter (human gate enforcement):     ✓ exit 1 on violation
Pipeline filter (clean run):                  ✓ exit 0, correct exclusions
Topology audit (full scan):                   ✓ 33 hits found
CompassAI/AurorAI extractor:                  ✓ 12 paragraphs, clearance granted
Regulatory corpus bootstrap:                  ✓ 5 docs, keyword config, checklist
Integration test:                             21/21 ✓
```

---

## Operator gates (human decisions required)

Only three items require Martin's input. Everything else is executable.

| Gate | Decision | Reference |
|------|----------|-----------|
| Decision 3 — Regulatory scope | Does PHAROS make regulatory compliance claims? If yes, run the bootstrap and ingest the PDFs. If no, flag as `out_of_scope_v1`. | `docs/martin_decision_brief.md` §3 |
| Backend hosting | Railway (recommended, simplest) vs. Hetzner VPS (cheapest long-term) | Previous session's `BACKEND_DEPLOYMENT_DECISION.md` |
| Cloudflare rename timing | When to execute the ~5-minute downtime window for govern-ai → pharos-ai | §Phase 7 above |

## Related

- [[Governance and PHAROS MOC]]
- [[MANIFEST]]
