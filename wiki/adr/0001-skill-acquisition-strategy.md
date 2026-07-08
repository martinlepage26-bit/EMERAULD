---
type: wiki
title: "ADR-0001: Skill Acquisition and Governance Strategy"
aliases:
- "ADR-0001: Skill Acquisition and Governance Strategy"
- ADR-0001
- wiki/adr/0001-skill-acquisition-strategy
tags:
- adr
- governance
- skills
- council
- superseded
status: archived
created: '2026-07-03'
updated: '2026-07-03'
vault_area: wiki
canonical_path: wiki/adr/0001-skill-acquisition-strategy.md
---

# ADR-0001: Skill Acquisition and Governance Strategy

## Status

**Superseded** (2026-07-03) by the canonical merged version at
`/home/martin/.agents/hephaistos/adrs/ADR-0001-council-skill-acquisition-strategy.md`.

This document (Antigravity's draft) and a second independent draft (Kimi's, at the
canonical path above) were both written for the same Queen Keyport ruling without
either agent knowing the other existed — a direct symptom of `EMERAULD/governance/hephaistos/`
being an unlabeled wiki mirror rather than an explicitly-marked copy of the real
governance repo at `~/.agents/hephaistos/` (now fixed — see the mirror notices added
to `EMERAULD/governance/hephaistos/*.md`). Kimi's version had stronger structural
detail (Considered Options analysis) and has been merged and corrected as the
canonical record. This file is kept, not deleted, to preserve the audit trail —
content below is the original text, no longer authoritative.

---

## (Original, superseded) Status

Accepted

## Context

The tmux AI council has the capability to discover and install external agent skills via the `npx skills` ecosystem. Recently, multiple agents executed parallel skill discoveries and installations. 
During this process, `multi-agent-orchestration` was flagged as High Risk. Antigravity told Kimi to proceed with installation, and Vibe issued a blanket "APPROVED" for all installations. However, Queen Keyport (a co-equal governance authority) ruled that skills flagged as High Risk must be held in pending status until governance clearance is formally recorded.
This highlighted a tension between operational momentum (Vibe/Antigravity) and governance (Queen Keyport), requiring a formalized decision on how skills are acquired, reviewed, and approved across the council.

## Decision

We will implement a governed skill-acquisition strategy with the following rules:

1. **Governance Gate for High Risk:** Any skill flagged as High Risk by any scanner (or agent) cannot be installed or used until explicit governance clearance is recorded by Queen Keyport or the Operator (Martin).
2. **Rejection of Blanket Approvals:** General "APPROVED" declarations from operational agents (like Vibe) do not supersede security or governance gates from Queen Keyport.
3. **Pending Status:** Flagged skills must remain in a "pending" state. Agents must not instruct each other to "proceed" with installation until clearance is confirmed in the shared session handoff.
4. **Mandatory Documentation:** Governance rulings regarding skill installations must be documented in the session state or handoff files before proceeding.

## Consequences

### Positive
- Prevents the execution or installation of untrusted or high-risk code.
- Establishes clear precedence: governance overrides operational momentum.
- Creates an auditable trail of skill approvals.

### Negative
- Slower skill acquisition process when flags are triggered.
- Requires council members to check handoff states before proceeding with installations.

## Related Rulings

- Queen Keyport ruling (2026-07-03): "skills flagged High Risk by any scanner must be held in pending status until governance clearance is recorded."

## Related

- [[HEPHAISTOS → Queen Keyport Scope Packet: Argus Drift-Audit on multi-agent-orchestration]] — scoped 2026-07-03, closes this ADR's outstanding action item (Argus drift-audit within 7 days), awaiting Queen Keyport clearance.
- [[HEPHAISTOS → Queen Keyport Scope Packet: Security Audit Phases 2-6]] — scoped 2026-07-03, closes this ADR's outstanding action item (scoped plan for security-audit Phases 2-6), awaiting Queen Keyport clearance.
