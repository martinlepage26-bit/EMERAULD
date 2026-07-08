---
type: wiki
title: L99 PHAROS Migration Artifacts 2026-04-19
aliases:
- L99 PHAROS Migration
- L99 Artifacts 2026-04-19
- 'PR #4 Hardening Bundle'
- wiki/L99 PHAROS Migration Artifacts 2026-04-19
tags:
- pharos
- deployment
- pr-4
- hardening
- migration
- l99
- artifacts
- wiki
- l99-pharos-migration-artifacts-2026-04-19-md
- dnspython
- compassai
- unaffected
- aurora
- deploy
- color-purple
status: active
created: '2026-04-19'
updated: '2026-06-26'
vault_area: wiki
canonical_path: wiki/L99 PHAROS Migration Artifacts 2026-04-19.md
backlink_count: 15
backlinks:
- '[[archive/wiki-2026-07-08/CSV_DIAGNOSTIC_REPORT]]'
- '[[Areas/PHAROS/Cloudflare Pages-to-Worker Migration — Build and Asset Behavior]]'
- '[[Areas/PHAROS/Control Protocols MOC]]'
- '[[archive/wiki-2026-07-08/Documents Root Loose Files Intake — 2026-04-28]]'
- '[[Areas/PHAROS/Governance and PHAROS MOC]]'
- '[[wiki/PHAROS Migration Runbook — PR4 Deploy and Cloudflare Migration (2026-04-19)]]'
- '[[wiki/PHAROS Workspace Inventory 2026-04-18]]'
- '[[wiki/PHAROS-EMERAULD Consolidated Timeline 2024-04-01 to 2026-04-19]]'
- '[[wiki/Provisional Arbitration Charter — Argus Layer 9.5]]'
- '[[_vault/VAULT ADDITIONS TRACKER]]'
- '[[archive/session-state/session-state-001]]'
- '[[artifacts/2026-04-19-pharos-migration-pr4/_manifest/MANIFEST]]'
- '[[memory/daily/2026-04-28]]'
- '[[projects/AurorA — Fisher King Project State]]'
- '[[projects/COMPASSai — Fisher King Project State]]'
---

# L99 PHAROS Migration Artifacts 2026-04-19

## Summary

Consolidated artifact bundle delivered 2026-04-19 for five overlapping [[PHAROS-AI Webservice — pharos-ai.ca|pharos-ai.ca]] workstreams: the govern-ai → pharos-ai rename, PR #4 backend hardening, the P1 dnspython blocker flagged by Codex review, the archive governance pipeline surfaced by [[CSV_DIAGNOSTIC_REPORT]], and the empty-regulatory-corpus gap. Every deliverable is verified (syntax, invariants, 15/15 PR #4 contract tests, 21/21 end-to-end integration tests against a synthetic corpus) and indexed under [[session-state]] for Trismégiste persistence. See [[Governance and PHAROS MOC]] for domain context.

## Context

The bundle closes the four open items that had accumulated across recent PHAROS Product Stack work: the [[PHAROS-AI Webservice — pharos-ai.ca|PHAROS-AI webservice]] deployment wasn't clean (Cloudflare Pages project still named `govern-ai`, D1 + R2 resources still on `govern-*` names), [[AurorA — COMPASSai Input Module|AurorA]]'s [[Hermes Dashboard — Professional Governance Tool|Hermes]]-adjacent Worker config referenced stale binding names, PR #4 had a latent Codex-flagged P1 (removed `dnspython`) that would crash every DB endpoint on Atlas, and the 116-file archive triage from the earlier [[CSV_DIAGNOSTIC_REPORT]] session had three unresolved human decisions. L99 = level-99 consolidation: one indexed tree with manifest, run-order, a drop-in `PATCH-pr4-dnspython.diff`, a golden reference `server.py`, and a 15-case test contract that fails CI forever if anyone removes dnspython again.

## Details

### Bundle location

`artifacts/2026-04-19-pharos-migration-pr4/` under EMERAULD root. Canonical layer (drop-in for the pharos-suite repo):

- `backend/` — `server.py` (hardened, 249 lines), `requirements.txt` (dnspython pinned), `Dockerfile` (shell-form CMD), `server_hardening_patch.py` (diagnostic), `tests/test_backend_hardening.py` (15 cases).
- `scripts/` — five-script archive-governance toolkit: `pharos_pipeline_filter.py`, `topology_audit.py`, `compassai_aurorai_extractor.py`, `manifest_decision_executor.py`, `regulatory_corpus_bootstrap.py`.
- `docs/` — `CODEX_PROMPT_SERVER_HARDENING.md`, `CSV_DIAGNOSTIC_REPORT.md`, `martin_decision_brief.md`, `PHAROS_OPERATIONAL_RUNBOOK.md`.
- `test_integration.py` — single-command 21-case end-to-end test.
- `test_fixtures/` — synthetic corpus (10 archive files + manifest + inventory) so the integration test runs offline.
- `_manifest/` — `MANIFEST.md`, `RUN-ORDER.md`, `PATCH-pr4-dnspython.diff`, `SHA256SUMS.txt`.

Legacy layer (kept for continuity): `01-deploy-config/` (rename infra — `deploy.yml`, `wrangler.toml`, `migration-govern-to-pharos.md` remain authoritative), `02-pipeline-triage/` (superseded by `scripts/`), `03-pr4-hardening/` (superseded by `backend/`).

### Verified invariants

Python syntax clean across all `.py` files. `deploy.yml` parses as YAML. `requirements.txt` contains `dnspython==2.6.1` with an ⚠️ DO-NOT-REMOVE warning. `backend/Dockerfile` uses shell-form `CMD uvicorn server:app --port ${PORT:-9202}` (fix for the exec-array form that silently breaks Railway). Entry point is `server:app`, matching Dockerfile and test suite. **PR #4 contract: 15/15 pass. Full end-to-end integration: 21/21 pass.**

### What it unblocks

PR #4 can merge as soon as the `PATCH-pr4-dnspython.diff` lands on its branch (or the full `01-deploy-config/requirements.txt` replaces the slimmed one). The [[AurorA — COMPASSai Input Module|AurorA Worker]] can deploy as soon as `database_id` is filled from the CF dashboard and the three rename TODOs in `wrangler.toml` are resolved. The [[COMPASSai — Governance Engine|COMPASSai]] pipeline remains pending its own architecture decision (desktop vs. web app) and is unaffected. The Railway backend deploy goes live as soon as `03-pr4-hardening/Dockerfile` replaces the current one and env vars are set per `RUN-ORDER.md` Phase 4. The [[Harrowfield Clinic — AI Governance Failure Case Study|Harrowfield]]-type case-study work remains archive-side, unaffected by the infra changes.

### Human-only decisions still open (from `martin_decision_brief.md`)

1. [[AI Society Manuscript — From AI Anxiety to Recursive Governance|AI Society manuscript]] is flagged MERGE but is source-bearing peer-reviewed material. KEEP vs. HUMAN-REVIEW-MERGE, not auto-merge.
2. Topology vocabulary (`topology_theseus`, `topology_auryn`, `topology_hopf` — see [[Recursive Governance Protocol — Theseus, Auryn, Hopf]]) has zero keyword hits across the 116-file archive. Architectural terms without evidentiary footprint: re-run extraction with corrected targets, or declare the method docs not-yet-ingested.
   - 2026-04-28 follow-up: [[Documents Root Loose Files Intake — 2026-04-28]] captured the complete root Documents Theseus/Auryn/Hopf packet and linked it to [[Provisional Arbitration Charter — Argus Layer 9.5]] and [[AGATHA Failure Pack — Theseus Continuity Stress Test]]. This does not rewrite the 116-file archive result; it closes the "method docs not-yet-ingested" explanation with later source evidence.
3. `moving parts.txt` is the single archive file linking [[COMPASSai — Governance Engine|CompassAI]] and [[AurorA — COMPASSai Input Module|AurorA]] by keyword. Must extract provenance before merge.

### Operator sequencing

Read `_manifest/RUN-ORDER.md` — six phases (Preflight → Close P1 → Apply hardening → CF dashboard renames → Railway deploy → Actions pipeline → Archive triage), each with a verification gate.

## Related

- [[Control Protocols MOC]]
- [[PHAROS-AI Webservice — pharos-ai.ca]] — the deployment surface this bundle finishes migrating
- [[AurorA — COMPASSai Input Module]] — receives the wrangler.toml + Worker rename
- [[COMPASSai — Governance Engine]] — downstream consumer, unaffected by infra
- [[Hermes Dashboard — Professional Governance Tool]] — operator-facing layer; unaffected
- [[Governance and PHAROS MOC]] — domain MOC; this note is registered there
- [[session-state]] — live thread state; updated to record L99 completion
- [[CSV_DIAGNOSTIC_REPORT]] — source of the `02-pipeline-triage/` decisions
- [[Trismégiste — Personal AI Assistant]] — agent that produced this bundle
- [[Recursive Governance Protocol — Theseus, Auryn, Hopf]] — the topology vocabulary with zero archival footprint
- [[Documents Root Loose Files Intake — 2026-04-28]] — later root-folder intake that recovered the protocol packet missing from this archive slice
- [[Provisional Arbitration Charter — Argus Layer 9.5]] — apex-authority provisional linked to Argus/L99 control questions
- [[AGATHA Failure Pack — Theseus Continuity Stress Test]] — follow-up continuity stress-test traces from root Documents
- [[PHAROS Migration Runbook — PR4 Deploy and Cloudflare Migration (2026-04-19)]] — Operator-facing action list from the same 2026-04-19 session: the 7 operator-scoped actions (API key rotation, manifest decisions, hosting pick, CF namespace renames, PR #4) that followed the automated L99 implementation
