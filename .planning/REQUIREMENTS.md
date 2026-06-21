# Requirements: EMERAULD Vault Runtime

**Defined:** 2026-04-23
**Core Value:** The vault must remain a reliable, source-faithful memory surface that agents and operator scripts can query without silently corrupting state.

## v1 Requirements

### Retrieval Runtime

- [ ] **RAG-01**: `scripts/ingest.py` assigns stable unique IDs for every ingested wiki note
- [ ] **RAG-02**: `scripts/ingest.py` finalizes LightRAG storages even if ingestion fails mid-run
- [ ] **RAG-03**: `scripts/query.py` finalizes LightRAG storages even if query execution raises

### Auth and Operator Feedback

- [ ] **AUTH-01**: `scripts/lightrag_config.py` fails clearly when Claude OAuth credentials are missing or refresh fails
- [ ] **AUTH-02**: refreshed Claude OAuth credentials are persisted back to disk only after a valid access token is returned

### Governance Bootstrap

- [ ] **GOV-01**: this repo has a minimal `.planning/` scaffold that accurately scopes brownfield runtime work

## v2 Requirements

### Verification

- **VER-01**: add dedicated runtime tests for the LightRAG script layer
- **VER-02**: widen phase planning beyond the retrieval runtime only after the executable surfaces are mapped

## Out of Scope

| Feature | Reason |
|---------|--------|
| Hermes desktop UI changes | Separate source tree and workflow |
| Vault-wide note refactors | Not required to stabilize the runtime scripts |
| Full multi-phase EMERAULD roadmap across all content domains | Too broad for the current bootstrap/fix pass |

## Traceability

| Requirement | Phase | Status |
|-------------|-------|--------|
| RAG-01 | Phase 1 | In Progress |
| RAG-02 | Phase 1 | In Progress |
| RAG-03 | Phase 1 | In Progress |
| AUTH-01 | Phase 1 | In Progress |
| AUTH-02 | Phase 1 | In Progress |
| GOV-01 | Phase 1 | In Progress |

**Coverage:**
- v1 requirements: 6 total
- Mapped to phases: 6
- Unmapped: 0 ✓

---
*Requirements defined: 2026-04-23*
*Last updated: 2026-04-23 after seeded runtime review/fix bootstrap*

## Related

- [[Research and Papers MOC]]
- [[Learning]]
