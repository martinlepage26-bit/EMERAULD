---
type: wiki
title: EMERAULD Automation — Detection Without Consumption
aliases:
- Detection Without Consumption
- Signal Decay
- Why the flags stopped working
- The missing consumer
tags:
- emerauld
- scripts
- scheduled-agents
- reliability
- governance
- failure-modes
- controls
status: active
created: '2026-07-13'
updated: '2026-07-13'
vault_area: wiki
canonical_path: wiki/EMERAULD Automation — Detection Without Consumption.md
date: '2026-07-13'
---

> For future Claude: every scheduled agent in this vault is a detector, and none is a consumer. The scans are accurate, the flags are correctly emitted, and nothing downstream acts on them: one overdue pair has been flagged 21 mornings running with zero movement, and the single line in `FAILURES.md` has sat unread for two days. Load this before adding another scan, another flag, or another audit, and before concluding that a detected problem is a managed problem.

## Summary

EMERAULD's automation layer is well instrumented and has no consumer. The four scheduled agents described in [[Architecture - EMERAULD Scripts - Overview]] detect reliably: the stale-project scan is correct, the overdue sweep is correct, the register thresholds and governance gates pass deterministically, and the [[wiki/Vault Health — 2026-07-12|health audits]] are accurate. What no agent, script, or prompt does is read those outputs and force a disposition. The result is a vault that produces a faithful daily record of problems it never closes. This note separates that pattern from the [[EMERAULD Scheduled Agents — Auth Dependency and Failure Modes|auth dependency]] recorded on 2026-07-11, which is a narrower instance of it.

## Context

This sits directly under the [[governance/EMERAULD-OS-BUILD-ORDER|EMERAULD OS build order]]: Stage 3 adds [[governance/EMERAULD-OS-SPEC — Event Triggers|event triggers]], and a trigger is a detector. Adding detectors to a system whose existing detectors are unread multiplies the signal without adding a consumer. The vault's own governance canon already states the test that is failing here: automations run only with a stop condition, an audit trail, and a rollback path. EMERAULD's scheduled agents have an excellent audit trail. They have no stop condition on their own flags, which is why a flag can be re-emitted 21 times and still be reported as if it were news.

## Details

### The record (evidence, on disk 2026-07-13)

- **The overdue sweep has flagged the same pair 21 mornings running.** The two [[Areas/PHAROS/External Data Registry — Phase 1 Build]] tasks have appeared in every morning run since the sweep began. Neither has moved. The Reddit API item carries a due date of 2026-04-20 and an "URGENT (Today)" marker, and is now 84 days past it. Source: [[memory/daily/2026-07-13]] and the identical tables in each prior daily note.
- **`Logs/scheduled/FAILURES.md` contains exactly one line and nobody has read it.** The line records the 2026-07-11 08:00 morning failure. It is still there, uncleared and unresolved, two days later. The handler that wrote it works. No prompt, script, or agent reads the file it writes to. Detection latency on that failure was 14 hours, and it was closed only because the nightly pass happened to investigate an empty scan.
- **The 2026-07-12 health audit fixed nothing, by design.** It found 316 actionable dangling links across 130 live notes, and preamble compliance of 51 notes out of 840. It was a read-only pass. No repair pass followed it, and none is scheduled. Source: [[wiki/Vault Health — 2026-07-12]].
- **The stale-project scan reports a number that carries no action.** 741 of the 763 flagged notes carry a single inherited `updated: 2026-06-26` value from a retired bulk touch, not 741 real edits. Today's daily note says so itself, instructing the reader to treat the figure as "a backlog marker, not a daily signal." The headline number is 763 regardless.
- **The nightly consolidation pass ran on an empty input set for the second time in three days.** On 2026-07-11 and again today, no note in the reconcile scope carried the day's date, so the contradiction check and the synthesis trigger had nothing to operate on by construction.

### The mechanism (evidence)

Each scheduled agent terminates in a write. `morning.sh` writes a daily note and a stale-projects artifact. The nightly pass writes a session-state line. The health check writes an audit note. The failure handler writes to `FAILURES.md`. Every one of those is a leaf. Nothing in `scripts/scheduled/` opens a file that a previous run produced and branches on its contents. The one exception is deterministic and narrow: `nightly.sh` remediates register thresholds and governance gates before the model pass, which is why those two surfaces are the only ones in the vault that never drift. That is the shape of the fix, and it was never generalized past those two surfaces.

### Interpretation (synthesis, not evidence)

- The pattern suggests a signal with no consumer does not stay neutral. It trains its reader to skip it. Twenty-one identical flags are not 21 reminders; they are one reminder re-emitted 21 times, and by now the flag is part of the background against which real change would have to be noticed. The instrumentation quality is what hides this: the scans are accurate, and accuracy reads as efficacy.
- One possible interpretation of the two empty nightly passes is that vault write activity has genuinely fallen off. Another is that work is happening outside the vault and is not being captured. The record on disk cannot distinguish these, because nothing measures the difference between "nothing happened" and "nothing was written down."
- The governance framing is sharper than the operational one. A control that is never read is not a weak control, it is an absent control that produces evidence of diligence. That is a worse failure than having no control, because the daily note looks like oversight.

### Unresolved

- Whether Martin reads the daily notes is not recorded anywhere in the vault and cannot be established from disk. Every claim above about "nobody reads X" is a claim about what the *agents* read, which is verifiable, not about what Martin reads, which is not.
- Whether the two External Data Registry tasks are still wanted. An item ignored 21 times may be dead rather than overdue, and nothing on disk distinguishes those two states. The sweep cannot tell the difference, and it currently assumes the second.

### Candidate controls (flagged, not executed)

Changing anything under `scripts/scheduled/` is an automation change and goes through the governed-task path, with a stop condition, an audit trail, and a rollback path. Martin decides; this note flags. Control 2 is the generalization of control 1 from the [[EMERAULD Scheduled Agents — Auth Dependency and Failure Modes|auth note]], which remains unimplemented.

1. **Age the flags.** A flag on its 21st emission should not render identically to a flag on its first. Printing the emission count and the age next to each overdue item costs one line in the prompt and makes decay visible in the artifact itself.
2. **Make the agents read what the agents write.** The morning and nightly prompts should open `Logs/scheduled/FAILURES.md` and the previous daily note's unchecked boxes, and surface unresolved entries. This is the single change that converts the lane from detect-only to detect-and-carry.
3. **Force a disposition on repeat flags.** After N emissions, an item must be re-committed, rescheduled, or explicitly killed. "Overdue" is not a stable state, and the sweep currently lets it be one indefinitely.
4. **Separate backlog markers from daily signals in the scan output.** The 741-note bulk cohort should be reported once, below the fold, so it stops inflating a headline that is read every morning.

Confidence: the record and the mechanism are `stated` (log lines, note contents, and script structure on disk). The reading of signal decay is `high` but is inference from the artifacts, not from observed behaviour. The two items under Unresolved are `speculation` and are marked as such. The controls are proposals, not decisions.

## Related

- [[EMERAULD Scheduled Agents — Auth Dependency and Failure Modes]]
- [[Architecture - EMERAULD Scripts - Overview]]
- [[Architecture - EMERAULD Scripts - Key Decisions]]
- [[governance/EMERAULD-OS-BUILD-ORDER]]
- [[governance/EMERAULD-OS-SPEC — Event Triggers]]
- [[wiki/Vault Health — 2026-07-12]]
- [[Areas/PHAROS/External Data Registry — Phase 1 Build]]
- [[memory/daily/2026-07-13]]
- [[session-state]]
