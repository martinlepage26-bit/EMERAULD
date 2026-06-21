# Roadmap: EMERAULD Vault Runtime

## Overview

This roadmap starts with the Python retrieval/runtime layer inside EMERAULD rather than the broader vault content or Hermes desktop surface. The immediate goal is to make the existing LightRAG ingestion and query scripts safer to operate and to give the repo a minimal local GSD scaffold for future brownfield work.

## Phases

- [ ] **Phase 1: LightRAG Script Runtime Hardening** - stabilize ingest/query cleanup, unique document IDs, and OAuth refresh failure handling

## Phase Details

### Phase 1: LightRAG Script Runtime Hardening
**Goal**: make the existing LightRAG-facing scripts fail safely and leave durable local planning context for follow-up work
**Depends on**: Nothing (first phase)
**Requirements**: [RAG-01, RAG-02, RAG-03, AUTH-01, AUTH-02, GOV-01]
**Success Criteria** (what must be TRUE):
  1. Ingest and query commands finalize LightRAG storages even when an operation raises
  2. Wiki-note ingestion IDs remain unique across subdirectories and filename collisions
  3. Claude OAuth refresh failures produce actionable errors instead of silently reusing stale tokens
  4. A minimal `.planning/` scaffold exists in this repo and accurately describes the runtime scope
**Plans**: 0 plans (seeded brownfield review/fix bootstrap)

## Progress

| Phase | Plans Complete | Status | Completed |
|-------|----------------|--------|-----------|
| 1. LightRAG Script Runtime Hardening | 0/0 | In progress | - |

## Related

- [[Governance and PHAROS MOC]]
- [[LightRAG — Graph-Based RAG System]]
