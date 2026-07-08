---
type: project-mirror
title: Camilo Meeting Cheat Sheet
tags:
- project-mirror
- projects
- micro1
status: active
created: '2026-07-08'
updated: '2026-07-08'
vault_area: projects
canonical_path: projects/micro1/camilo-meeting-cheat-sheet.md
backlink_count: 1
backlinks:
- '[[wiki/Orphan Index — Vault-Level Graph Repair 2026-05-06]]'
---

# Camilo Meeting Cheat Sheet

## Goal

Get Camilo to confirm whether Micro1 wants blackboard-style agent-work traces, identify the highest-value signal types and delivery format, and agree to NDA + a controlled evaluation batch.

## Opening

"InfraFabric operates if.blackboard, an append-only agent task ledger. Every AI task is recorded as structured events with session binding, acceptance criteria, typed checkpoints, traps, and hashed closeout.

The useful question for us is not whether Micro1 wants workflow data in the abstract, but which signal types and delivery format matter most to your clients right now.

From there we can scope the fastest next step: a controlled evaluation batch, then a broader pilot or feed if the structure fits."

Then stop.

## Ask These

1. Which signal types are highest priority right now?
2. Do you want full append-only event streams or canonical per-entry snapshots?
3. Who uses the data downstream?
4. Is the field of use evaluation, red-teaming, RLHF, SFT, or broader training?
5. What schema, provenance, or hash-chain requirements matter most in a first batch?
6. What batch size is enough for you to decide whether to proceed?
7. Are you looking for a one-time historical export or an ongoing delta feed?
8. Are there domains, rights boundaries, or retention constraints we should treat as hard stops?

## If They Press

### "How much data do you have?"
"The blackboard currently contains 3,800+ task IDs across 10 months. The current Micro1 catalogue presents 49 curated entries. We can expand by domain or signal type once we know what your evaluation target actually is."

### "Can you send a sample now?"
"Pre-NDA we can share the catalogue, structure, and example fields. For a meaningful evaluation batch that reflects real task structure, we would want NDA first. After that, a 200-entry internal assessment batch is feasible if the fit is real."

### "Can you provide the raw ledger?"
"Potentially, but I would separate evaluation access from broader transfer rights. The first step is to align on signal class, format, field of use, and controls."

### "What does it cost?"
"That depends on whether you want a curated evaluation batch, a one-time historical export, or an ongoing delta feed, plus field of use and downstream rights."

## Red Lines

- Lead with blackboard, not the older generic governance/professional-data framing.
- Do not quote counts beyond the approved set: 3,800+ task IDs, 49 curated entries, 200-entry evaluation batch.
- Do not promise raw-ledger transfer or broad downstream rights on the call.
- Do not discuss exclusivity.
- Do not explain proprietary methodology beyond the documented fields and controls.
- Do not lead with price.

## Close

"This is helpful. Based on what you've said, it sounds like [repeat back the signal types, format, and use case] are the right starting point. The fastest path on our side would be NDA, then a curated evaluation batch with the exact structure and documentation you need. If the signals hold up in your review, we can scope either a broader historical export or an ongoing feed."

## Immediately After

- Send a thank-you note within 30 minutes.
- Record the signal types they named.
- Record requested format, field of use, downstream users, and target batch size.
- Note whether they want a one-time historical set or an ongoing feed.
- Note any requests for raw-ledger access, broad downstream rights, exclusivity, or unusual retention terms.
