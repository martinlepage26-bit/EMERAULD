---
type: manifest
title: 'L99 — PHAROS Migration + PR #4 Hardening — Artifact Manifest'
tags:
- artifacts
- 2026-04-19-pharos-migration-pr4
- backend
- server
- hardening
- dnspython
- dockerfile
status: ready
created: '2026-04-19'
updated: '2026-06-26'
vault_area: artifacts
canonical_path: artifacts/2026-04-19-pharos-migration-pr4/_manifest/MANIFEST.md
backlink_count: 1
backlinks:
- '[[wiki/archive/Orphan Index — Artifacts And Archives — 2026-05-06]]'
level: L99
bundle: pharos-migration-pr4
date: '2026-04-19'
operator: Martin Lepage
agent: Trismégiste
integration_tests: 21/21 passing
pr4_path_a: landed
pr4_commit: 5a33fba
pr4_branch: chore/pr4-archive-toolkit-and-docs
pr4_contract_tests: 15/15 passing
pr4_edge_binding: live
pr4_edge_commit: 5fed95b
pr4_edge_smoke: api.pharos-ai.ca/health → 200 JSON ok:true
track_d_6_cf: closed
---

# L99 — PHAROS Migration + PR #4 Hardening — Artifact Manifest

> **2026-04-19 PR #4 resolution:** GAP surfaced at L99 closeout (see
> `GAP-pr4-server-spec-alignment.md`) was resolved via **Path A** — the live
> `pharos-suite/backend/server.py` was aligned to the bundle spec. Commit
> `5a33fba` on branch `chore/pr4-archive-toolkit-and-docs` applied all four
> edits (logger rename, `_check_dnspython` guard, `DB_READY` + lifespan
> degraded mode, `/health` shape flip). Bundle's `test_backend_hardening.py`
> was installed verbatim; pytest **15/15 green** against live code in 4.51s.
> Pre-push CI gate (44 pytest + 46 vitest + 61 smoke) also green. Branch
> pushed; PR open at
> `https://github.com/martinlepage26-bit/pharos-suite/pull/new/chore/pr4-archive-toolkit-and-docs`.

This bundle is the consolidated, verified, end-to-end set of deliverables for three
overlapping workstreams that converged on 2026-04-19:

1. **govern-ai → pharos-ai rename** (CF Pages, D1, R2, bindings, repo paths)
2. **PR #4 backend hardening** (lifespan, structured logging, ReturnDocument.AFTER, minimal requirements)
3. **P1 dnspython blocker** flagged by Codex review on PR #4
4. **Archive governance pipeline** (CSV diagnostic findings → executable filters)
5. **Regulatory corpus gap** (empty `ai_governance_regulatory_docs.csv` → bootstrap)

Every artifact below is Python-/YAML-/TOML-valid, every Python file compiles,
every invariant is explicitly checked, the full 15-test PR #4 contract passes
against `backend/server.py`, and the full 21-test end-to-end integration suite
passes against the bundled `test_fixtures/` corpus. Sha256 checksums are in
`_manifest/SHA256SUMS.txt`.

See [[L99 PHAROS Migration Artifacts 2026-04-19]] for the Obsidian-side note.

---

## Directory map (canonical layer)

```
artifacts/2026-04-19-pharos-migration-pr4/
├── _manifest/
│   ├── MANIFEST.md                      ← you are here
│   ├── RUN-ORDER.md                     ← step-by-step operator sequence
│   ├── PATCH-pr4-dnspython.diff         ← drop-in unified diff for PR #4
│   └── SHA256SUMS.txt                   ← integrity
│
├── backend/                             ← drop-in for <repo>/backend/
│   ├── server.py                        ← hardened FastAPI entry point
│   ├── requirements.txt                 ← minimal deps, dnspython pinned
│   ├── Dockerfile                       ← shell-form CMD for Railway $PORT
│   ├── server_hardening_patch.py        ← diagnostic (run with --check)
│   └── tests/
│       └── test_backend_hardening.py    ← 15-case PR #4 contract
│
├── scripts/                             ← drop-in for <repo>/scripts/
│   ├── pharos_pipeline_filter.py        ← contamination filter + human-gate enforcer
│   ├── topology_audit.py                ← topology keyword coverage audit
│   ├── compassai_aurorai_extractor.py   ← implementation-reference extractor
│   ├── manifest_decision_executor.py    ← Decision Brief → manifest CSV automation
│   └── regulatory_corpus_bootstrap.py   ← regulatory corpus + keyword config + audit
│
├── docs/                                ← drop-in for <repo>/docs/
│   ├── CODEX_PROMPT_SERVER_HARDENING.md ← ready-to-paste Codex prompt
│   ├── CSV_DIAGNOSTIC_REPORT.md         ← full 6-CSV diagnostic
│   ├── martin_decision_brief.md         ← three human-only decisions
│   └── PHAROS_OPERATIONAL_RUNBOOK.md    ← unified operational runbook
│
├── test_integration.py                  ← 21-case end-to-end test (single command)
├── test_fixtures/                       ← synthetic corpus for integration test
│   ├── 00_ARCHIVE_METADATA_MANIFEST.csv
│   ├── 00_archive_inventory.csv
│   └── archive_files/                   ← 10 synthetic archive files
│
├── 01-deploy-config/                    ← legacy layer (rename infra)
│   ├── requirements.txt                 ← superseded by backend/requirements.txt
│   ├── Dockerfile                       ← superseded; old exec-form CMD (do NOT use)
│   ├── deploy.yml                       ← GitHub Actions: test/backend/frontend
│   ├── wrangler.toml                    ← Aurora Worker config (3 TODOs)
│   └── migration-govern-to-pharos.md    ← authoritative rename runbook
│
├── 02-pipeline-triage/                  ← legacy layer (superseded by scripts/)
│   ├── pharos_pipeline_filter.py
│   ├── topology_audit.py
│   ├── compassai_aurorai_extractor.py
│   └── martin_decision_brief.md
│
└── 03-pr4-hardening/                    ← legacy layer (superseded by backend/)
    ├── Dockerfile                       ← same content as backend/Dockerfile
    ├── CODEX_PROMPT_SERVER_HARDENING.md
    ├── server_hardening_patch.py
    ├── test_backend_hardening.py
    └── reference/
        └── server.py                    ← minimal golden; backend/server.py is richer
```

**Canonical layer:** `backend/`, `scripts/`, `docs/`, `test_integration.py`,
`test_fixtures/`. These are the drop-in trees for the repo.

**Legacy layer:** `01-deploy-config/`, `02-pipeline-triage/`, `03-pr4-hardening/`.
Kept for diff-continuity and because `01-deploy-config/deploy.yml`, `wrangler.toml`,
and `migration-govern-to-pharos.md` have no superset elsewhere — they remain the
authoritative deploy-infra sources.

---

## Artifact-by-artifact

### backend/

**`server.py`** (249 lines) — PR #4 target state. Lifespan context manager replaces
deprecated `@app.on_event`. Safe DB startup (ping failure ⇒ `db_ready=False`, not
crash). `_check_dnspython()` emits CRITICAL log if SRV URL + missing dns module.
`ReturnDocument.AFTER` baked in for CRUD scaffolding. Structured logging under
the `pharos` logger. `/health` and `/api/health` routes both return the same
payload. Passes all 15 tests in `tests/test_backend_hardening.py`.

**`requirements.txt`** (29 lines) — `dnspython==2.6.1` on line 18 with an explicit
⚠️ DO-NOT-REMOVE warning. All core deps pinned (fastapi 0.115.0, uvicorn 0.30.6,
motor 3.6.0, pymongo 4.9.2, pydantic 2.9.2). This supersedes
`01-deploy-config/requirements.txt`.

**`Dockerfile`** — shell-form `CMD uvicorn server:app --port ${PORT:-9202}` so
Railway's `$PORT` injection expands. Health check also uses `${PORT:-9202}`. Non-root
user. Multi-stage build. This supersedes `01-deploy-config/Dockerfile`.

**`server_hardening_patch.py`** — diagnostic. Run from `backend/` with `--check`
before letting Codex touch the file. Reports which of the four hardening elements
are already present, which are missing.

**`tests/test_backend_hardening.py`** — 15 tests. Health (5) + CORS (2) +
dnspython guard (3) + requirements regression guards (5). Regression guards fail
CI forever if anyone removes `dnspython`, `motor`, `fastapi`, `pydantic`, or
`uvicorn` from `requirements.txt`.

### scripts/

**`pharos_pipeline_filter.py`** — contamination filter for the 116-file archive.
Excludes `redistributed_copy`, `superseded_but_important`, and `REVISE_AND_STRENGTHEN`
rows. Exits with code 1 if the `ai-anxiety-...md` manuscript is in a MERGE queue
without `human_gate_cleared=true`. Exits 0 on clean run.

**`topology_audit.py`** — determines whether the topology-vocabulary gap
(`topology_theseus`, `topology_auryn`, `topology_hopf` with zero hits across 116
files) is explained by (A) ingestion miss or (B) keyword mismatch. Produces a
report and a keyword-hits CSV. In the bundled synthetic corpus it finds 63 hits
across 3 tiers — which proves the scanner works; the production 0-hit finding is
either A or B and the report will say which.

**`compassai_aurorai_extractor.py`** — scans a source file for CompassAI and
AurorAI implementation references. Produces three artifacts:
`compassai_aurorai_implementation_references.md` (provenance),
`compassai_aurorai_keyword_hits.csv` (in text-hits format),
`moving_parts_merge_clearance.txt` (GRANTED/DENIED). Must be run BEFORE any
merge of `moving parts.txt`.

**`manifest_decision_executor.py`** — applies Decisions 1 and 2 from
`martin_decision_brief.md` to `00_ARCHIVE_METADATA_MANIFEST.csv`. Backs up
before writing. Timestamps every change. Dry-run mode shows diffs without
writing.

**`regulatory_corpus_bootstrap.py`** — fills the empty regulatory corpus from
zero. Produces an index of 5 regulatory documents (EU AI Act, NIST AI RMF,
ISO 42001, Canadian AIDA, CA Voluntary Code), a keyword-extraction config, and
a compliance-claim audit matrix mapping each PHAROS compliance claim to the
governing regulation, the specific PHAROS component, and evidence status.

### docs/

**`CODEX_PROMPT_SERVER_HARDENING.md`** — prompt to paste into Codex. Targets
`backend/server.py` (confirmed entry point). Instructs Codex to read before
touching, apply the four PR #4 hardening goals surgically, and not touch
endpoints or business logic.

**`CSV_DIAGNOSTIC_REPORT.md`** — full diagnostic from the earlier 6-CSV session.
Three hard findings: topology vocabulary gap, manuscript-in-merge conflict,
`moving parts.txt` implementation-evidence singleton. This is the source of
truth for the `02-pipeline-triage/` and `scripts/` work.

**`martin_decision_brief.md`** — three decisions that require Martin's input.
Decision 1 (AI & Society manuscript) blocks the pipeline until recorded.
Decision 2 (Archive Master Tracker) recommended. Decision 3 (regulatory scope)
determines whether to run `regulatory_corpus_bootstrap.py`.

**`PHAROS_OPERATIONAL_RUNBOOK.md`** — unified operational runbook covering all
seven phases (archive decisions → pipeline → topology → extraction → regulatory
→ backend deploy → Cloudflare rename). Every phase has copy-pasteable commands
and verification gates.

### test_integration.py + test_fixtures/

**`test_integration.py`** — single command, 21 checks across all 7 systems:

1. Backend pytest (15 inner assertions rolled up to 1 outer check)
2. Server hardening patch: all checks pass
3. Pipeline filter: human-gate violation ⇒ exit 1
4. Pipeline filter: clean run ⇒ exit 0
5. Topology audit: full scan + report + hits > 0
6. CompassAI/AurorAI extractor: provenance + CSV + clearance GRANTED
7. Regulatory bootstrap: CSV + 5 docs + keyword config + checklist

**`test_fixtures/`** — synthetic corpus: 10 archive files, a manifest with the
full column set (`filename, revision_status, evidence_status, action, confidence,
human_gate_cleared`), and an inventory. Constructed to exercise every branch:
the ai-anxiety manuscript triggers the human-gate violation; two
`redistributed_copy_*` files exercise the contamination filter; three topology
files exercise the keyword audit (63 hits across 3 tiers); `moving_parts.txt`
contains CompassAI + AurorAI + topology keywords so the extractor clearance
emerges GRANTED.

### _manifest/

**`MANIFEST.md`** — you are here.

**`RUN-ORDER.md`** — six operator phases with commands and gates.

**`PATCH-pr4-dnspython.diff`** — unified diff, drop-in on PR #4 branch. Adds
`dnspython==2.6.1` with an explanatory header comment. One commit closes the
P1 blocker.

**`SHA256SUMS.txt`** — sha256 checksums for every file in the bundle
(regenerated after absorption).

---

## Invariants verified

| Invariant | Verified by |
|---|---|
| All .py files compile | `python3 -m py_compile` (clean) |
| `deploy.yml` is valid YAML | `yaml.safe_load` (clean) |
| `requirements.txt` pins `dnspython==2.6.1` | grep confirms the line |
| `backend/Dockerfile` uses shell-form CMD | grep confirms `CMD uvicorn server:app` |
| Dockerfile entrypoint = `server:app` | grep confirms |
| PR #4 test suite passes end-to-end | `pytest` — 15/15 pass |
| **Full integration test passes** | `test_integration.py` — **21/21 pass** |

---

## What still requires operator action (not automatable)

1. Rename CF Pages project `govern-ai` → `pharos-ai` in the Cloudflare dashboard.
   (Runbook §1. Deploy pipeline is already pointed at the new name.)
2. Rename/migrate D1 database `govern-suite` → `pharos-suite` in CF dashboard;
   then update `wrangler.toml` line 31.
3. Rename/migrate R2 buckets `govern-artifacts` → `pharos-artifacts`,
   `govern-evidence` → `pharos-evidence` in CF dashboard; then update
   `wrangler.toml` lines 39, 45.
4. Fill `database_id` in `wrangler.toml` line 32 from CF dashboard.
5. Apply `PATCH-pr4-dnspython.diff` to PR #4 (or merge `backend/requirements.txt`
   into the PR branch wholesale).
6. Run `server_hardening_patch.py --check` from `backend/`, then paste
   `docs/CODEX_PROMPT_SERVER_HARDENING.md` into Codex with the real `server.py`
   in scope.
7. Decide the three items in `docs/martin_decision_brief.md` — especially
   Decision 3 (regulatory scope): if PHAROS makes regulatory compliance claims,
   run `scripts/regulatory_corpus_bootstrap.py` and ingest the PDFs; if not,
   flag the decision `out_of_scope_v1`.
8. Pick backend hosting: Railway (simplest, matches current `deploy.yml`) vs.
   Hetzner VPS (cheapest, needs new Dockerfile orchestration).

`_manifest/RUN-ORDER.md` sequences these with concrete commands.

---

## Related

- [[Home]] — vault entry
- [[Governance and PHAROS MOC]] — primary index
- [[session-state]] — live thread state
- [[L99 PHAROS Migration Artifacts 2026-04-19]] — Obsidian note for this bundle
- [[PHAROS-AI Webservice — pharos-ai.ca]] — deployment surface
- [[CSV_DIAGNOSTIC_REPORT]] — source of the `scripts/` + `docs/` toolkit
- [[GAP-pr4-server-spec-alignment]]
- [[PHAROS_OPERATIONAL_RUNBOOK]]
- [[README]]
