---
type: wiki
title: Stacklight-owner-explainer
aliases:
- Stacklight Owner Explainer
- Stacklight Governance Framework Owner
- Stacklight Product and Evidence Steward
tags:
- stacklight
- governance
- blackboard
- proof-desk
- ai-governance
- audit
- areas
- stacklight-owner-explainer-md
- proof
- product
- receipt
- color-purple
status: active
created: '2026-06-30'
updated: '2026-06-26'
vault_area: Areas
canonical_path: Areas/PHAROS/Stacklight-owner-explainer.md
backlink_count: 9
backlinks:
- '[[wiki/AI Infrastructure Stack]]'
- '[[Areas/PHAROS/Governance and PHAROS MOC]]'
- '[[Areas/PHAROS/InfraFabric MCP Stack — Remote Bundles]]'
- '[[Areas/PHAROS/InfraFabric R0.5 Rollout — Hosted API Migration (2026-06-29 to 2026-06-30)]]'
- '[[_vault/VAULT ADDITIONS TRACKER]]'
- '[[Areas/PHAROS/if.blackboard — Coordination Evidence Spec Sheet (2026-06-27)]]'
- '[[memory/daily/2026-06-30]]'
- '[[memory/daily/2026-07-01]]'
- '[[session-state]]'
source_path: /home/martin/governanceframework/README.md
---

# Stacklight-owner-explainer

This note explains where Martin sits in the white-label proof-desk and governance structure, where to find reference material, how to verify that things are working, and how to keep the governance model simple enough for clients and auditors to understand. It documents Stacklight as a configured product layered on top of [[InfraFabric Architecture]] modules tracked in [[AI Infrastructure Stack]].

> [!success] Contradiction resolved 2026-07-01
> This note's "Current durable authority" (`https://api.infrafabric.io`, `mtl-02` PostgreSQL, `if_blackboard.r05_events`) was flagged on 2026-06-30 as conflicting with the SSH/Proxmox MCP access pattern in [[InfraFabric MCP Stack — Remote Bundles]] and [[if.blackboard — Coordination Evidence Spec Sheet (2026-06-27)]]. Resolved: not a contradiction, a timeline gap. `if.blackboard` was migrated off SSH/script/JSONL mutation to the hosted API + `mtl-02` Postgres in the **R0.5 rollout on 2026-06-29** — one day before this note was created and two days after the other two notes were last updated. This note's claim was correct and current; the other two were stale on this one point and have been updated to match (2026-07-01). Evidence: `/home/martin/apps/stacklight/documentation/agents/5009-if-blackboard-postgres-authority-runbook-2026-06-29.md` and `5011-stacklight-blackboard-mtl03-fresh-session-handover-2026-06-30.md` — this machine is confirmed as `mtl-03` in the handover's host-role table. Separately worth noting: Stacklight-the-product's own customer data store is MongoDB (`stacklight_selfhost`, local), distinct from `if.blackboard`'s Postgres authority on `mtl-02` — Stacklight's backend *implements* the published `api.infrafabric.io/blackboard/api.html` contract as a spec, it does not store its own product data there.

## Martin's Role

Martin is not just a developer inside the system. Martin is the governance owner and product steward.

The role is to decide:

```text
What must be recorded?
What counts as evidence?
Who can review it?
What can safely be claimed?
What remains only internal tooling?
```

A simple title for this role:

```text
Governance Framework Owner
```

or, more product-facing:

```text
Product and Evidence Steward
```

## The Simple Model

Think of the configured product as four layers:

```text
1. Work happens
   Humans, AI agents, Codex, Hermes, tickets, code, docs, reviews.

2. Work becomes evidence
   The product records tasks, sessions, checkpoints, evidence refs, reviews, closeout.

3. Evidence becomes proof
   Proof Desk and Proof Packets reconstruct what happened.

4. Proof becomes verifiable
   Receipts bind hashes, signatures, and claim boundaries.
```

Martin sits above all four layers as the person who defines the rules, checks the implementation, and decides when something is ready for a client or auditor.

## Marketing Explainer

Customer-facing pages should describe the two jobs without naming the internal modules.

```text
The product turns AI-assisted work into a reviewable evidence record.

Working context keeps the current state alive:
  next actions, blockers, handoff notes, and enough history to resume.

The evidence record keeps durable proof:
  requests, decisions, checkpoints, approvals, artifacts, access, verification,
  and what cannot safely be claimed.

Proof packets export the record:
  what happened, what evidence supports it, what is missing, and what limits apply.
```

The buyer should hear:

```text
AI work is easy to lose in chats, terminals, tickets, and summaries.
This product gives teams a structured record they can review later.
```

The buyer should not need to hear internal names for the context layer, evidence layer, receipt layer, or coordination layer.

## Internal Naming Boundary

Internal/operator docs may still use module names where precision matters:

```text
Blackboard = durable evidence and proof runtime
if.context = bounded working-context and resume layer
if.trace = receipt, hash, and integrity binding
if.switchboard = coordination and wake/control lane
```

These names are not product brands. Public pages, sales copy, client-facing docs, and auditor explainers should use the white-label product name plus plain concepts like working context, evidence record, proof desk, proof packet, receipt, review, and claim boundary.

## Where To Find Things

Main working folder:

```bash
/home/martin/apps/stacklight
```

Start here:

```text
PRODUCT.md
```

That explains what Stacklight is supposed to be in plain language.

For implementation and handover:

```text
documentation/agents/5011-stacklight-blackboard-mtl03-fresh-session-handover-2026-06-30.md
```

For the architecture map:

```text
documentation/agents/5002-if-rook-harness-structurizr-c4-workspace-2026-06-27.dsl
```

For the roadmap:

```text
documentation/agents/5003-if-blackboard-rook-governance-saas-autoplan-roadmap-2026-06-27.md
```

For the rational architecture:

```text
documentation/agents/5007-if-blackboard-governance-saas-rationalized-architecture-2026-06-27.md
```

For API behavior:

```text
documentation/agents/5008-if-blackboard-governance-api-contract-v1-2026-06-27.md
```

For user and integrator guidance:

```text
documentation/agents/5009-if-blackboard-governance-cli-api-rest-mcp-user-guide-v1-2026-06-27.md
```

For operational evidence:

```text
documentation/agents/evidence/
```

Generated graphical architecture poster:

```text
/root/.codex/generated_images/019f1879-2c37-70b3-a3d9-cd39c7924472/ig_051e36fcdf910aeb016a43d11901c8819ca24750c2b4907209.png
```

## The Correct Governance Order

For governance, the order should be:

```text
1. Register the thing
   AI tool, agent, task, client request, system, or workflow.

2. Record the request
   What was asked, by whom, for what purpose.

3. Capture work evidence
   Sessions, checkpoints, files, links, decisions, tool outputs.

4. Review the evidence
   Human reviewer or policy gate checks sufficiency.

5. Classify claims
   Verified, inferred, missing, blocked, stale, or explicitly not claimed.

6. Close out
   Final result, known limits, evidence refs, future risks.

7. Export proof
   Proof packet for client, auditor, or internal review.

8. Bind receipt
   Hash, signature, or receipt where needed.
```

This is the core governance chain. Everything else is secondary.

## How To Check That Stacklight Works

For Martin, first check that the product is alive:

```bash
cd /home/martin/apps/stacklight
systemctl is-active caddy docker stacklight-api
curl -fsS http://127.0.0.1:8091/api/health
curl -fsS https://stacklight.pharos-ai.ca/api/health
```

For durable governance, the key question is:

```text
Is evidence going to the hosted evidence API/Postgres authority?
```

Not tmux. Not WebSocket. Not local files. Not memory.

Current durable authority:

```text
https://api.infrafabric.io
mtl-02 PostgreSQL
if_blackboard.r05_events
```

If that path is down, stop making audit or proof claims.

## What Clients Should See

Clients should see:

```text
Configured product name
Proof Desk
AI registry
Task history
Review status
Evidence references
Proof packets
Receipts
Claim boundaries
```

Clients should not need to understand:

```text
tmux
root sessions
Hermes lanes
Rook bootstrap
SSH
internal MCP wiring
operator bridges
```

Those are internal machinery.

## What Auditors Should See

Auditors need a calm evidence map:

```text
Control objective:
  What risk is being governed?

Evidence source:
  Where is the durable record?

Review step:
  Who checked it?

Integrity:
  What proves the record was not quietly changed?

Limits:
  What does this not prove?
```

The most important sentence for auditors:

```text
Receipts prove record integrity and provenance. They do not prove semantic correctness by themselves.
```

This keeps the product honest and avoids overclaiming.

## Consequence Rules

Use these rules when something breaks:

```text
Product UI down:
  Client preview problem, not necessarily evidence loss.

Evidence API down:
  Pause durable task and proof writes.

Postgres authority uncertain:
  Do not claim reliable proof history.

Receipt/integrity service unavailable:
  Proof packets may be readable, but not receipt-verified.

tmux/WebSocket down:
  Operator inconvenience only. Not a customer governance failure.

Local transcript exists:
  Useful context, not proof authority.
```

## How To Make It Simpler

Reduce the public and product model to five words:

```text
Register
Record
Review
Prove
Export
```

Everything in the configured product should fit into one of those.

Keep three separate views:

```text
1. Martin/operator view
   Full system, hosts, tools, tmux, APIs, drift, repair paths.

2. Client view
   What the product does, how evidence is reviewed, what proof packet they get.

3. Auditor view
   Authority, controls, evidence, integrity, limitations.
```

Do not make clients or auditors learn the operator machinery.

## Does Everything Need To Be Structured From The Start?

No.

At the beginning of the toolchain, work can be messy:

```text
chat
code
agent work
terminal commands
client notes
tickets
research
drafts
```

That is normal.

What matters is the governance boundary.

The rule should be:

```text
Once work becomes client-relevant, audit-relevant, security-relevant, or decision-relevant, it must enter the structured record.
```

So the early toolchain can stay light. But the moment the work may need to be relied on later, create or attach it to a product evidence record.

That gives speed without losing governance.

## Minimum Viable Governance Framework

For now, treat the product as:

```text
A proof desk for AI-assisted work.
```

Not a giant compliance universe.

Minimum viable governance framework:

```text
1. Inventory of AI tools and agents
2. Task and session evidence trail
3. Human review and claim classification
4. Proof packet export
5. Receipt and integrity binding
```

Defer the rest until those five are clean.

The structure should serve the work. If the structure becomes heavier than the work, it is no longer governance; it is paperwork wearing a hard hat.

## Related

- [[EMERAULD]]
- [[governance/governance-index]]
- [[AI Governance Reference Stack — Annotated Library (Operational 2026-03-11)]]
- [[AI Governance Offer Ladder - Montreal Quebec 90-Day Revenue Plan]]
