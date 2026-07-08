---
type: governance-doc
title: Operator → Gadget Handoff Schema
aliases:
- Operator → Gadget Handoff Schema
tags:
- governance
- ai
- hephaistos
- gadget
- governance-doc
- mode
- scout
- credential
- launch
status: active
domain: governance
created: '2026-06-21'
updated: '2026-06-26'
vault_area: governance
canonical_path: governance/hephaistos/operator-to-gadget.md
backlink_count: 3
backlinks:
- '[[Areas/PHAROS/Governance and PHAROS MOC]]'
- '[[wiki/archive/Orphan Index — Runtime And Agents — 2026-05-06]]'
- '[[governance/hephaistos/HEPHAISTOS]]'
---

# Operator → Gadget Handoff Schema

## Purpose

This document defines the machine-checkable handoff from the Operator (Martin) to Gadget for direct invocation. Gadget is an independent specialist at Argus level — invoked by the Operator, not routed through the HEPHAISTOS / Queen Keyport / Hermes chain. This schema captures the constraints Gadget needs to do its job: scout vs. build mode, constraint set, security context, and output format.

**Scope:** external-system tasks — tool evaluation, MCP server discovery, framework selection, API integration, app build, launch pipeline. Any task that touches external systems or frontier tech.

---

## Required Fields

```json
{
  "handoff_version": "1.0",
  "task_id": "<uuid — optional for one-shot invocations>",
  "timestamp": "<ISO-8601>",
  "origin_agent": "Operator",
  "destination_agent": "Gadget",

  "mode": "<scout | builder-core | launch-pipeline>",

  "task": {
    "objective": "<one-sentence statement of what Gadget is producing>",
    "question": "<scout mode only: the question Gadget is evaluating (e.g., 'which orchestration framework fits this stack?')>",
    "build_spec": "<build-core/launch-pipeline mode only: what is being built (app name, core features, deploy target)>",
    "promotion_scope": "<launch-pipeline only: where the launch lands (Product Hunt, LinkedIn, cold email, SEO, social)>"
  },

  "constraints": {
    "language": "<Python | TypeScript | JavaScript | Rust | Go | polyglot | none>",
    "scale": "<target user count, request rate, data volume>",
    "latency": "<target response time | none>",
    "licensing": "<permissive-only | GPL-compatible | commercial-context | none>",
    "team_size": "<1 | small-team | enterprise>",
    "cloud_target": "<Cloudflare | AWS | GCP | local | self-hosted | none>",
    "existing_stack": [
      "<tool-1>",
      "<tool-2>"
    ]
  },

  "security_context": {
    "available_credentials": [
      "<credential-name (scoped; no secrets inline)>"
    ],
    "permission_boundaries": [
      "<what Gadget may access>",
      "<what Gadget must refuse>"
    ],
    "credential_rotation_status": "<current | rotation-pending | n/a>"
  },

  "methodological_reference": {
    "consults_hephaistos": "<true | false>",
    "hephaistos_docs": [
      "/home/cerebrhoe/hephaistos/HEPHAISTOS.md",
      "/home/cerebrhoe/hephaistos/HEPHAISTOS_OPERATIONS.md",
      "/home/cerebrhoe/hephaistos/QUEEN-KEYPORT.md"
    ],
    "binding_level": "reference-only"
  },

  "output_expected": {
    "format": "<ranked-shortlist | deployed-app-url | full-launch-package | status-report>",
    "candidates_max": "<integer — default 4 for scout mode>",
    "evidence_requirement": "<primary-sources-required | web-search-acceptable>"
  },

  "deadlines": {
    "desired_delivery": "<ISO-8601 | none>",
    "hard_deadline": "<ISO-8601 | none>"
  },

  "escalation_triggers": [
    "<condition that requires Gadget to stop and escalate to Operator — e.g., exposed credential found, permission denied on scoped resource, tool requires commercial license in non-commercial context>"
  ]
}
```

---

## Validation Rules

1. `mode` must be one of the three defined modes. Unknown modes are rejected.
2. If `mode == scout`, `task.question` is required and `task.build_spec` / `task.promotion_scope` must be empty.
3. If `mode == builder-core`, `task.build_spec` is required and must include deploy target.
4. If `mode == launch-pipeline`, both `task.build_spec` and `task.promotion_scope` are required.
5. `security_context.permission_boundaries` must be non-empty — Gadget never operates without declared boundaries.
6. `methodological_reference.binding_level` must be `reference-only`.
7. If any credential in `available_credentials` has status `rotation-pending`, Gadget must refuse operations that would use it until rotation completes (carries over from Fort Knox security discipline).

---

## Completion Gate

Gadget may treat the packet as complete only when:
- [ ] All required fields are present
- [ ] `mode` and the mode-specific fields are consistent
- [ ] `constraints.licensing` is set if `mode == builder-core` or `mode == launch-pipeline`
- [ ] `security_context.permission_boundaries` is non-empty
- [ ] `output_expected.format` aligns with mode (scout→shortlist, builder-core→URL, launch-pipeline→full package)

If any are missing, Gadget returns the packet with a scope-clarification request to the Operator (not an escalation to the three-agent stack).

---

## What this schema does NOT include

- No governance-decision field. Gadget is not gated by Queen Keyport approval. QK may flag security/governance concerns about Gadget's integrations post-delivery; the Operator decides.
- No Hermes routing directive. Gadget's delivery is direct to Operator.
- No HEPHAISTOS binding-instruction field. HEPHAISTOS guidelines are consulted as `reference-only`.
- No credential payload — secrets are never in the packet. Only scoped credential names.

---

## Status

**Active.** Created 2026-04-23 during Phase F remediation of the agent ecosystem audit (`AGENT_AUDIT_2026-04-23.md`), closes finding F-023.

## Related

- [[Governance and PHAROS MOC]]
- [[HEPHAISTOS]]
