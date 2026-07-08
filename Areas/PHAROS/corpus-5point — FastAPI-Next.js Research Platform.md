---
type: product
title: corpus-5point — FastAPI-Next.js Research Platform
tags:
- research-platform
- fastapi
- nextjs
- pgvector
- opensearch
- patent-workbench
- rights-aware-ingestion
- pharos
- vm-inventory
status: active
domain: pharos
created: '2026-07-08'
updated: '2026-07-08'
vault_area: Areas
canonical_path: Areas/PHAROS/corpus-5point — FastAPI-Next.js Research Platform.md
---

# corpus-5point — FastAPI-Next.js Research Platform

> For future Claude: this is a substantial, actively-scaffolded project
> (codename CORPUS) at `/home/martin/apps/web-apps/corpus-5point/`, not a
> throwaway prototype. It absorbed an entire prior project
> (patent-workbench) into a `legacy/` subfolder — but the absorption claim
> in its own README ("no standalone remains") is **contradicted by disk
> state**: a live, separately-modified copy of patent-workbench still exists
> at `~/patent-workbench`. Flag this duplication before assuming either copy
> is the sole source of truth.

## Summary

CORPUS is an "AI Research Intelligence Database" — a rights-aware,
multi-organization research-ingestion and dossier platform combining a
FastAPI/PostgreSQL/OpenSearch backend with a Next.js/Tailwind/shadcn
frontend. It reached a locked architectural decision on 2026-06-03
(reconciling two competing prior specs) and, per its own progress notes, had
completed core models, source-rights ledger, arXiv/OpenAlex connectors,
hybrid search, JWT multi-org auth, and public SSR dossier pages by
2026-06-01. In June 2026 it absorbed the older `patent-workbench` project's
features directly into its FastAPI backend, while also clean-migrating the
old repo's full source tree into `legacy/patent-workbench/`.

## Context

Sources read (read-only): `README.md`, `docs/HARDENING.md`,
`docs/PHASE1-SETUP.md`, `docs/PHASE1-PROGRESS.md`,
`docs/RECONCILIATION-NOTES.md`, and `legacy/patent-workbench/MIGRATION_MANIFEST.md`.
No `.env` or credential files were inspected. The directory has no git repo
of its own (`fatal: not a git repository` when checked) — file mtimes are
used for dating instead (docs dated 2026-05-31 through 2026-06-17).

## Details

### Locked architecture (RECONCILIATION-NOTES.md, dated 2026-06-01, decision "verrouillée" 2026-06-03)

Two competing prior specs — a "BUILD BRIEF v2" and a detailed "Product
Specification v1" — were reconciled (Option 3) rather than one replacing the
other:

- **Backend**: FastAPI + SQLAlchemy 2.0 (async) + Alembic, PostgreSQL 16 +
  pgvector, OpenSearch (hybrid lexical + vector search + facets), Airbyte +
  Temporal for durable ingestion workflows, GROBID + Apache Tika for PDF
  parsing.
- **Frontend**: Next.js 14 App Router + Tailwind + shadcn/ui, chosen
  specifically to support SSR/SEO on public dossier pages.
- **Data model**: `document` / `document_version` / `manifestation` /
  `identifier`, each source carrying a `source_policy` ledger
  (allow_metadata / allow_snippet / allow_fulltext / allow_embeddings +
  review_status) — a rights-aware ingestion gate, not an afterthought.
- Multi-organization model from day 1; multilingual embeddings
  (`multilingual-e5-large`/small); Stripe billing fields reserved in-schema
  even though billing activates in a later phase.

### Progress as of 2026-06-01 (PHASE1-PROGRESS.md)

Completed: full document/version/manifestation + SourcePolicy models,
Alembic migrations 001–002, source registry + rights-ledger CRUD with a
`can_ingest()` gating service, arXiv connector (source-policy aware),
a complete OpenAlex connector with controlled ingestion
(`services/openalex_ingestion.py`), a hybrid OpenSearch service (lexical +
vector + embedding generation) with automatic indexing on ingest, JWT +
multi-org auth with route protection, public SSR dossier pages (Next.js) +
matching backend public endpoint, and protected org-scoped dossier
creation. Next priorities noted: richer OpenAlex normalization, drag-drop
dossier persistence, BibTeX/PDF export, more connectors, richer watchlist
history.

### Hardening status (docs/HARDENING.md)

Done: source-policy ledger enforcement pre-ingestion, JWT + refresh tokens,
Pydantic v2 validation, RBAC-protected routes, consistent
`{detail, code}` error shape with no stack-trace leaks, in-memory
rate-limiting middleware, and detailed Row-Level-Security (RLS) design notes
with example SQL/migration pattern for Postgres multi-tenant isolation — but
RLS itself is documented as **not yet implemented** ("implementation in next
hardening pass"); app-level `org_id` filters remain the primary isolation
mechanism today. A prioritized backlog remains for secrets management,
structured logging/audit trails, DB hardening (pooling, backups), frontend
CSP/XSS/token-storage hardening, and expanded test/load coverage.

### Patent-workbench absorption and the duplication

The CORPUS README documents a June 2026 merge: patent-specific fields added
to the `Document` model (publication_number, claims, CPC, inventors,
patent_status, etc.), a new `/patents` FastAPI router with AI tools (claim
drafter — broad/narrow/system/method — prior-art summarizer, a "Lex-style"
patent-aware chat), a new Alembic migration (003), and a "Patent Tools"
panel added to the frontend dashboard. The README states plainly: "The
standalone `/home/martin/repos/patent-workbench` has been removed; no
standalone remains."

**That claim does not hold on this disk.** Two live copies exist:

1. `~/patent-workbench` (i.e. `/home/martin/patent-workbench`) — a full,
   independent working directory with its own `.git`, `node_modules`,
   `dist/`, and a `CLAUDE_TASK.md` file dated **2026-06-30**, i.e. modified
   *after* the migration manifest below was generated. This is not a stale
   leftover; it has continued to change.
2. `apps/web-apps/corpus-5point/legacy/patent-workbench/` — a clean-migrated
   copy produced by a `clean-migrate` protocol (verify-then-delete,
   utf8-lf, diamond-eyes), documented in
   `MIGRATION_MANIFEST.md` (generated 2026-06-17T04:05:06Z), which
   file-by-file hashes the migration from `repos/patent-workbench` into
   `legacy/patent-workbench/` — including the full `.git` history, backend,
   frontend, electron shell, and an inner `legacy/pharos-fto-workbench/`
   nested inside *that*.

This is a genuine duplication needing reconciliation: the migration manifest
asserts the standalone was removed, but a standalone copy exists and has
newer file activity than the manifest itself. Anyone editing patent-workbench
functionality should check both locations before assuming which one is
canonical.

## Related

- [[Areas/PHAROS/nexusos — Base44 App]] — another substantial app on the same VM; contrast in scale/stack (custom FastAPI/Next.js vs. Base44 low-code).
- [[Areas/PHAROS/PHAROS Product Stack]] — canonical PHAROS product-family bridge note; CORPUS is not yet formally listed there.
- [[Areas/PHAROS/AurorA — COMPASSai Input Module]] — another FastAPI backend in the PHAROS/Martin ecosystem (per the standing FastAPI+MongoDB stack used for AurorA/COMPASSai); useful contrast against CORPUS's FastAPI+PostgreSQL+pgvector+OpenSearch stack.
- [[Areas/PHAROS/ai-agent-board — Third-Party Tool Evaluation]] — an unrelated but co-located tool-evaluation note, useful as a contrast between "we are building this" (CORPUS) and "we cloned this to evaluate it" (ai-agent-board).
