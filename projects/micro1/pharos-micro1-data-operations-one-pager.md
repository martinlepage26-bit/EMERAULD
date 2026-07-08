---
type: project-mirror
title: Pharos AI — Data Production Operations (for micro1 qualification)
tags:
- project-mirror
- projects
- micro1
status: active
created: '2026-07-08'
updated: '2026-07-08'
vault_area: projects
canonical_path: projects/micro1/pharos-micro1-data-operations-one-pager.md
backlink_count: 1
backlinks:
- '[[wiki/Orphan Index — Vault-Level Graph Repair 2026-05-06]]'
---

# Pharos AI — Data Production Operations (for micro1 qualification)

**One-page external version**  
**Date**: 2026-06-09  
**Company**: Pharos AI (InfraFabric and LegiPro are product/trading surfaces of the same entity)

## What we operate

Pharos AI runs two deterministic, governance-constrained data production pipelines that generate structured evaluation and decision traces. We do not sell raw source text or client data. We sell the outputs of expert workflows: how work is authorized, how exceptions are escalated and resolved, how claims are bounded, and how evidence is produced and validated.

### Product Line 1: Governance Evaluation Data (Blackboard / COMPASS / HELIX)

**Core pattern**: Task → checkpoint → escalation / veto / override → documented rationale → bounded claim / proof packet / resolution.

**What the data contains**:
- Append-only task, session, and signal records from real operational governance workflows.
- Adversarial evaluation traces (HELIX): probe type (ANCHOR, MIRROR, TRAP, etc.), model responses, hedge counts, failure classification, human correction with rationale.
- Governance decision logs: risk tier (high/critical), outcome (DEFER / APPROVE_WITH_CONDITIONS / etc.), triage status, coverage status.
- Signed / provenance-carrying events (partial cryptographic receipts already present).

**Current audited candidate pool** (preliminary licensability pass, if.trace excluded):
- ~15,379 potentially recoverable events across Blackboard pillars.
- Strongest slice: signals (11,897 / 11,924 audited) — clean internal governance events.
- Production characteristics: deterministic workflow, versioned methodology, claim-boundary enforcement at every step.

**Why this is non-commodity for AI labs**:
Frontier labs need high-quality red-teaming and governance evaluation data — not just "the model answered." They need records of *how* institutional constraints were applied, where overrides happened, and what the expert rationale was. Our traces document exactly that loop.

### Product Line 2: Professional Domain Evaluation Data (LegiPro)

**Core pattern**: Messy professional query / source material → normalized intent → source-family routing + bias rules → extraction / validation → claim-boundary enforcement → accepted / quarantined outcome.

**Key assets**:
- Conveyor extraction and validation traces (7,350+ accepted candidates): full lifecycle events, manifests, patch records, validation gates, quarantine/acceptance decisions, artifact provenance.
- Extraction JSON + tests (8,888 artifacts + 9,344 tests): domain-specific claim-boundary enforcement, overclaim prevention, source-path validation patterns (e.g., `test_no_forbidden_overclaim_language`).
- Autocomplete intent transformation packs: raw French accounting/tax queries → professional intent → safe display label → intent hint → source-family bias → expected result → bad-source rejection rules (62k+ raw rows; transformation logic is the high-value layer).

**Why this is valuable**:
This is agentic workflow data for *professional* AI systems (accounting, tax, legal). It teaches retrieval, intent understanding, source selection discipline, and safe claim generation in a high-stakes domain where overclaim or wrong-source errors are costly.

## Production characteristics (common to both lines)

- **Deterministic & versioned**: Same generation → test → correction → annotation protocol every time. Quality does not degrade with volume.
- **Governed at source**: Claim-boundary checks, source-authority scoring, rights posture, validation gates, and human review/override are built into the workflow (not added after the fact).
- **Structured & export-ready**: JSON/structured records with explicit field maps, timestamps, reviewer identity, and outcome.
- **Domain-specific expertise**: PhD-level socio-anthropological + technical governance depth applied to institutional, regulatory, and professional contexts. Rare in the current data supply market.

## What a partnership looks like (pilot structure)

We propose starting with a paid proof-of-operation pilot rather than a large data dump:

- **Phase 1 (30 days)**: 200–300 records in the agreed schema and format (mix of governance evaluation traces and/or professional domain traces). Delivered with field documentation and QA summary. Fixed fee in the $25K–$40K range.
- **Phase 2 (90 days)**: Scaled production (1,000–2,000+ records/month), tiered by complexity (standard vs. expert-annotated vs. custom scenario design).
- **Ongoing**: Dedicated stream + custom evaluation protocol work. Non-exclusive, renewable.

This structure lets micro1 validate the pipeline and output quality under contract before committing to volume.

## Contact for qualification

Martin Lepage  
Founder, Pharos AI  
ml@pharos-ai.ca

(We are prepared to share a controlled, redacted sample under NDA immediately after a qualification conversation confirms category fit.)
