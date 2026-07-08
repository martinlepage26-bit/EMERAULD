---
type: project-mirror
title: 'Pharos AI x micro1: Missing Workstreams Before a Serious Data-Licensing Call'
tags:
- project-mirror
- projects
- micro1
status: active
created: '2026-06-08'
updated: '2026-07-08'
vault_area: projects
canonical_path: projects/micro1/4166-pharos-micro1-missing-workstreams-entanglement-ip-and-methodology-risk-2026-06-08.md
backlink_count: 1
backlinks:
- '[[wiki/Orphan Index — Vault-Level Graph Repair 2026-05-06]]'
---

# Pharos AI x micro1: Missing Workstreams Before a Serious Data-Licensing Call

Danny Stocker | InfraFabric Research | 2026-06-08  
Status: internal risk-and-readiness memo  
Companion docs:

- `/root/docs/4164-pharos-micro1-operational-data-licensing-blackboard-iftrace-assessment-2026-06-08.md`
- `/root/docs/4165-pharos-micro1-sample-blackboard-governance-dataset-2026-06-08.jsonl`

## Purpose

The first memo answered:

> Is there plausibly a fit between current Pharos / InfraFabric workflow data and what micro1 says it wants?

The answer was:

> Yes, probably.

This memo addresses the next and more serious question:

> What still has to be solved before that fit is negotiation-ready?

There are three major missing workstreams:

1. the **entanglement / licensability audit**,
2. the **joint IP / deal-ownership question**,
3. the **methodology reconstruction risk** specific to blackboard-style workflow data.

There is also one evidence refresh item:

4. a **fresh `if.trace` live-store count** if `if.trace` is going to be used as part of the numeric story.

## Executive Summary

The opportunity looks more credible after the blackboard count.

But there is still a big difference between:

- "we have workflow data that looks valuable,"

and

- "we have a clean, licensable, negotiation-ready dataset."

The current state is:

- **fit exists**
- **volume exists**
- **structure exists**
- **provenance exists**
- **commercial readiness is not yet complete**

The most important missing step is not more rhetoric.  
It is **separating what is licensable from what is merely interesting**.

## 1. The entanglement problem

### Why this matters

The blackboard volumes are meaningful:

- 10,524 task events
- 8,828 session events
- 14,737 signal events

But those are **gross operational totals**, not automatically licensable totals.

The main issue is that some of those flows may include:

- client-derived work,
- customer-identifying metadata,
- commercially sensitive topics,
- operator process details that are too revealing,
- mixed data where internal governance logic and client-specific substance are intertwined.

### The rule

Do **not** market the full blackboard volume as licensable until each relevant slice is classified.

### Minimum classification model

Every candidate data family should be sorted into one of four buckets:

#### A. Internal-only and probably licensable

Examples:

- internal coordination tasks,
- system review tasks,
- platform/runtime improvement traces,
- proof-packet formatting / claim-boundary workflows,
- generic evaluation flows without client substance.

#### B. Internal-dominant but needs redaction

Examples:

- tasks with internal methodology value but revealing titles,
- event streams with SIDs, host paths, or operator identifiers,
- traces with usable workflow structure but too much implementation detail.

#### C. Mixed / uncertain

Examples:

- tasks involving real third-party work,
- event streams where client facts and governance workflow are interleaved,
- review queues touching real account/customer/case material.

These should be treated as **non-licensable until proven otherwise**.

#### D. Client-derived / off limits

Examples:

- anything containing direct client substance,
- anything requiring client consent,
- anything whose anonymization still leaves commercial exposure.

### Fast audit plan

The first pass does not need to perfect the whole store.  
It needs to answer:

> Is there a sufficiently large, clean subset worth discussing with micro1?

Recommended fast audit:

1. Choose a candidate-safe subset by pillar and product.
2. Sample 50 to 100 rows from each candidate-safe bucket.
3. Mark each row:
   - `clean`
   - `clean_with_redaction`
   - `mixed`
   - `off_limits`
4. Estimate the recoverable licensable pool from the sampled rates.
5. Use **that** number on calls, not the gross total.

### Conservative hypothesis

Before audit, assume:

- `product`, `runtime`, `tooling`, some `docs`, and some `if.blackboard` / proof-desk flows are the safest starting pools
- `ops`, `review`, and any customer-facing domain lanes are higher risk

That is a heuristic only. It is not a substitute for sampling.

## 2. The joint IP and deal-ownership question

### Why this matters

Once the blackboard evidence is included, the story stops being:

> Pharos alone may have a small but interesting governance dataset.

It becomes:

> Pharos methodology plus InfraFabric operational evidence together produce a stronger data asset.

That is commercially better, but it creates a new problem:

> who is actually selling what?

This should be resolved **before** the micro1 call, not after a good call creates pressure.

### The minimum questions that need written answers

1. Who is the contracting party?
   - Pharos?
   - InfraFabric?
   - both?

2. What is the licensed asset?
   - Pharos-only sample packs?
   - blackboard/signals operational traces?
   - a joint packaged dataset?

3. What is explicitly excluded?
   - core methodology docs
   - reconstruction-enabling schemas
   - client-derived material
   - crown-jewel control-plane logic

4. How is revenue split?
   - fixed percentage
   - by dataset family
   - by originating system

5. Who approves samples?

6. Who controls press / disclosure / name usage?

7. Who bears indemnity or confidentiality breach risk if the other side contributed the problematic data?

### Recommended minimum deal hygiene between Pharos and InfraFabric

Before engaging micro1 seriously, write a short operator-side memo that states:

- parties,
- ownership boundaries,
- sample approval process,
- revenue split principle,
- exclusivity rule,
- no direct side-deal rule for the scoped dataset,
- IP carve-out rule,
- dispute resolution path if the deal advances.

It does not need to be elaborate to be useful.  
It does need to exist.

### Safer default posture

The cleanest default is:

- the data is presented as a **joint scoped evaluation/governance dataset**
- neither side can separately promise the other side's assets
- no exclusivity is discussed with micro1 unless both sides agree in writing first

## 3. Methodology reconstruction risk

### Why this matters

Blackboard is valuable partly because it is structured.

But the structure itself leaks information about the operational method.

A buyer does not need the design doc if the event shapes, sequencing, and labels already teach the logic.

### The risk in concrete terms

A sufficiently sophisticated AI lab could infer pieces of the governance model from patterns like:

```text
task created
-> checkpoint cadence
-> escalation threshold
-> response lane
-> closeout pattern
-> claim boundary language
-> signature placement
```

The risk is not just "they see documentation."  
The risk is:

> they learn the operating method from the outputs.

### Blackboard-specific leakage surfaces

Potentially revealing fields include:

- raw task titles,
- recurring acceptance-language patterns,
- checkpoint wording,
- trap naming,
- claim-boundary vocabulary,
- product_id combinations,
- source/path conventions,
- escalation wording,
- time spacing / cadence,
- signature placement and coverage patterns,
- owner / sid structures.

### Minimum mitigation set

If a sample or dataset is prepared, default controls should include:

1. **Field minimization**
   - remove everything not needed for the target training use

2. **Identifier replacement**
   - synthetic task IDs, synthetic session IDs, synthetic actor IDs

3. **Path stripping**
   - remove host paths, repo paths, machine names

4. **Title abstraction**
   - replace specific task names with neutral workflow labels where possible

5. **Time fuzzing**
   - preserve sequence, not exact operational cadence

6. **Vocabulary normalization**
   - remove house-style phrases that encode the method too directly

7. **Schema flattening where needed**
   - enough structure for utility, not enough for easy reverse-engineering

8. **Sample-level legal review**
   - not because the dataset is huge, but because the schema may itself be IP

### Key licensing clause needed

The commercial agreement should not only say:

> you may not access confidential documentation

It should also say something closer to:

> the licensed dataset does not transfer ownership of the workflow methodology, schema logic, governance procedures, control thresholds, or any derivative reconstruction rights beyond the permitted model-training use.

That needs proper lawyer language later, but the principle should be explicit from the start.

## 4. Fresh if.trace count

### Why this matters

`if.trace` is a useful asset in this story, but there is a difference between:

- "it exists and is real"
- and
- "it has current volume at a scale worth quoting"

The historical audit gives real numbers from `2026-04-07`, which is good.

But if `if.trace` is going to appear in a micro1 deck or on the call as a meaningful numeric support layer, the current live store should be re-counted.

### The rule

Until refreshed, use language like:

> `if.trace` is a shipped public receipt and integrity-verification layer with historically verified signed coverage.

Do not use language like:

> thousands of fully signed `if.trace` transactions

until there is a fresh count.

## Revised readiness model

### Current state

#### What is ready now

- the strategic fit story
- the blackboard operational-data story
- a structurally faithful sample specimen
- the claim-boundary discipline

#### What is not ready now

- clean licensable event-pool count
- joint IP/deal structure memo
- methodology reconstruction mitigation spec
- refreshed `if.trace` live volume

### Practical interpretation

You are ready for:

- an exploratory qualification call,
- if the call is disciplined and framed as discovery.

You are **not** ready for:

- sending a broad raw sample,
- quoting total licensable volume confidently,
- discussing exclusivity,
- negotiating price from a fully audited data inventory.

## Recommended sequence this week

1. **Settle the joint-asset question**
   - one short written memo between Pharos and InfraFabric

2. **Run a fast licensability audit**
   - sample candidate-safe blackboard buckets

3. **Refresh `if.trace` count**
   - only if it is going to be part of the numeric pitch

4. **Prepare one external one-pager**
   - scoped, high-level, with clear exclusions

5. **Then take the micro1 call**
   - discovery first, not premature disclosure

## Bottom line

The missing work is not cosmetic.  
It is exactly the work that separates:

- an interesting operator insight,

from

- a defendable data-licensing opportunity.

The encouraging part is that the gaps are concrete:

- licensability audit,
- joint deal structure,
- schema/IP protection,
- trace count refresh.

Those are solvable problems.

And solving them will likely increase both:

- the credibility of the pitch,
- and the realistic value of the deal.
