---
type: project-mirror
title: 'Pharos AI x micro1: Blackboard / Signals Licensability Audit v1'
tags:
- project-mirror
- projects
- micro1
status: active
created: '2026-06-09'
updated: '2026-07-08'
vault_area: projects
canonical_path: projects/micro1/4169-pharos-micro1-blackboard-signals-licensability-audit-v1-no-iftrace-2026-06-09.md
backlink_count: 1
backlinks:
- '[[wiki/Orphan Index — Vault-Level Graph Repair 2026-05-06]]'
---

# Pharos AI x micro1: Blackboard / Signals Licensability Audit v1

Document ID: 4169  
Danny Stocker | InfraFabric Research | 2026-06-09  
Status: preliminary internal licensability audit  
Scope: `if.blackboard` task/session-adjacent task events and `signals` governance events  
Explicitly out of scope: `if.trace`

Companion docs:

- `/root/docs/4164-pharos-micro1-operational-data-licensing-blackboard-iftrace-assessment-2026-06-08.md`
- `/root/docs/4165-pharos-micro1-sample-blackboard-governance-dataset-2026-06-08.jsonl`
- `/root/docs/4166-pharos-micro1-missing-workstreams-entanglement-ip-and-methodology-risk-2026-06-08.md`
- `/root/docs/4168-pharos-micro1-qualification-call-posture-v2-trading-names-and-deal-guardrails-2026-06-08.md`

## Executive Summary

This audit supports taking a micro1 qualification call.

It does **not** yet support sending a raw dataset, quoting final licensable volume, or discussing exclusivity.

The strongest current finding:

> In the candidate internal blackboard/signals buckets inspected here, there is a substantial recoverable pool of governance workflow events. Most of the value is likely licensable only after redaction, normalization, and methodology-leakage review.

First-pass candidate pool:

- audited candidate events: **17,713**
- clean raw-looking events: **578**
- clean-with-redaction events: **14,801**
- mixed / uncertain events: **1,732**
- off-limits events: **602**

Conservative interpretation:

- **578** rows are the only rows that look clean enough at first pass to discuss as near-raw examples.
- **15,379** rows are potentially recoverable if `clean` and `clean_with_redaction` are combined.
- That **15,379** number should **not** be quoted externally as final licensable volume until a manual audit validates the mechanical classification.

## Audit Scope

The audit inspected the current live append-only stores:

- `/root/.if_tasks/blackboard/tasks.events.jsonl`
- `/root/.if_tasks/signals/signals.events.jsonl`

It focused on candidate-safe internal buckets:

- task pillar `product`
- task pillar `runtime`
- task pillar `tooling`
- task pillar `docs` / `if.docs`
- task product / project `if.blackboard`
- task pillar `coordination` / `platform`
- signals with internal governance-like project/topic metadata, excluding obvious GGQ/Gmail/outreach lanes

This pass did **not** attempt to recover customer/domain-heavy lanes.

## Classification Model

Each candidate event was assigned one of four categories.

`clean`

No obvious redaction, client, credential, or methodology-leakage flags were detected.

`clean_with_redaction`

Likely useful and probably recoverable, but contains one or more of:

- internal file paths,
- SIDs or operator identifiers,
- host/container/infrastructure references,
- methodology vocabulary,
- dogfood/test markers,
- internal product-map details.

`mixed_uncertain`

Potentially useful, but includes terms suggesting client/domain/customer/workflow entanglement. These rows need manual review before inclusion.

`off_limits`

Contains credential/security terms or high-risk signals that should be excluded from any sample unless specifically cleared.

## Aggregate Result

| Bucket | Total | Clean | Clean with redaction | Mixed / uncertain | Off limits |
|---|---:|---:|---:|---:|---:|
| signals_internal_governance | 11,924 | 487 | 11,410 | 21 | 6 |
| task_blackboard_product | 3,166 | 32 | 1,528 | 1,209 | 397 |
| task_coordination_platform | 228 | 6 | 182 | 14 | 26 |
| task_pillar_docs | 926 | 38 | 750 | 77 | 61 |
| task_pillar_product | 993 | 11 | 530 | 371 | 81 |
| task_pillar_runtime | 273 | 1 | 237 | 14 | 21 |
| task_pillar_tooling | 203 | 3 | 164 | 26 | 10 |
| **Total** | **17,713** | **578** | **14,801** | **1,732** | **602** |

## Deterministic Sample Check

The audit also sampled up to 50 events from each bucket using a deterministic seed.

| Bucket | Sample size | Clean | Clean with redaction | Mixed / uncertain | Off limits |
|---|---:|---:|---:|---:|---:|
| signals_internal_governance | 50 | 2 | 47 | 0 | 1 |
| task_blackboard_product | 50 | 2 | 24 | 16 | 8 |
| task_coordination_platform | 50 | 1 | 41 | 4 | 4 |
| task_pillar_docs | 50 | 2 | 42 | 4 | 2 |
| task_pillar_product | 50 | 0 | 27 | 22 | 1 |
| task_pillar_runtime | 50 | 0 | 45 | 4 | 1 |
| task_pillar_tooling | 50 | 0 | 42 | 6 | 2 |

The sample agrees with the aggregate picture:

- signals are the most scalable candidate pool;
- most usable rows still need redaction;
- blackboard/product rows carry more methodology and domain entanglement;
- product/docs/runtime/tooling are usable, but not raw-export safe.

## Main Flag Types

The most common reasons for redaction or exclusion were:

- paths, SIDs, emails, host/container identifiers,
- methodology vocabulary,
- client/domain-specific terms,
- credential/security terms,
- dogfood/test markers.

This confirms the earlier risk analysis:

> the issue is not just anonymization; it is licensability and methodology-leakage control.

## What Can Be Said on the micro1 Qualification Call

Safe phrasing:

> We have completed a first-pass internal audit over candidate blackboard and signal governance-event buckets. The gross candidate pool in the audited internal slices is about 17.7k events, most of which appear potentially recoverable only after redaction and normalization. We are not treating that as final licensable volume yet.

Stronger but still safe phrasing:

> The audit suggests a meaningful recoverable pool exists, especially in internal governance signals, but we would only share a qualified estimate and redacted sample after NDA.

Do **not** say:

> We have 17.7k licensable events ready to sell.

Do **not** say:

> We can send the blackboard store.

Do **not** include:

- raw paths,
- SIDs,
- client/domain-heavy rows,
- credential/security rows,
- raw method-revealing checkpoint language.

## Recommended Sample Path

For pre-NDA:

- use the synthetic/redacted specimen in `/root/docs/4165-pharos-micro1-sample-blackboard-governance-dataset-2026-06-08.jsonl`;
- optionally provide a field map only.

For post-NDA:

- create a 25 to 50 row sample from `signals_internal_governance`,
- include 5 to 10 redacted task/checkpoint rows,
- exclude all `mixed_uncertain` and `off_limits` rows,
- strip paths, SIDs, hostnames, exact timestamps, raw owner names, and internal source paths,
- normalize method vocabulary where it teaches too much of the operating model.

For pilot:

- run manual review on the `clean_with_redaction` rows,
- split training/evaluation utility fields from operational/proprietary fields,
- create a disclosure manifest with row IDs and transformation notes,
- keep client-derived lanes excluded unless separately cleared.

## Remaining Work

Before any real sample:

1. Manually review the `clean_with_redaction` rows selected for sample.
2. Build a redaction transform and verify no paths/SIDs/emails/secrets remain.
3. Define a field map for utility-preserving schema flattening.
4. Confirm data-rights authority for each selected event family.
5. Decide whether exact timestamps are removed, rounded, or sequence-only.
6. Confirm no client-derived/domain-heavy rows enter the first sample.

Before any commercial negotiation:

1. Produce a final recoverable licensable-volume estimate.
2. Separate evaluation-only, RLHF, SFT, and general-training pricing assumptions.
3. Decide retention, deletion, downstream-use, and sublicensing boundaries.
4. Get legal/privacy review on the sample and license posture.

## Bottom Line

The audit improves confidence that there is a real micro1-relevant asset.

It also confirms the disciplined posture:

- qualify interest now,
- do not quote final volume yet,
- do not send raw stores,
- use synthetic/redacted pre-NDA material,
- prepare a controlled post-NDA sample from the cleanest signal/task subsets.

For the first call, the best answer remains:

> We are ready to qualify the fit and requirements. We are not yet treating the gross event count as final licensable volume.
