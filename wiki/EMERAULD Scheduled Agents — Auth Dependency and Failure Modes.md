---
type: wiki
title: EMERAULD Scheduled Agents — Auth Dependency and Failure Modes
aliases:
- Scheduled Agents Failure Modes
- Cron Auth Dependency
- Why the morning agent failed
tags:
- emerauld
- scripts
- scheduled-agents
- reliability
- cron
- failure-modes
- governance
status: active
created: '2026-07-11'
updated: '2026-07-11'
vault_area: wiki
canonical_path: wiki/EMERAULD Scheduled Agents — Auth Dependency and Failure Modes.md
date: '2026-07-11'
---

> For future Claude: the four scheduled vault agents (morning, nightly, weekly, health-check) all depend on one ambient Claude Code OAuth session on the host, and cron cannot refresh it. When that session lapses, every model-backed scheduled agent fails at the same point and writes nothing but a line in `Logs/scheduled/FAILURES.md`, which no agent reads. Load this when a scheduled run is missing, when a daily note has a gap, or before changing anything under `scripts/scheduled/`.

## Summary

The vault automation layer described in [[Architecture - EMERAULD Scripts - Overview]] has a single shared point of failure that is not in any script's logic: the host's Claude Code OAuth session. `morning.sh`, `nightly.sh`, `weekly.sh` and `health-check.sh` each shell out to `/home/martin/.local/bin/claude --dangerously-skip-permissions -p "..."`. That binary authenticates against the ambient interactive session on the host. Cron runs non-interactively and cannot complete an OAuth refresh, so an expired session takes down the model half of every scheduled agent at once. This note records the first observed instance and the controls that would close it.

## Context

This failure mode sits underneath the [[governance/EMERAULD-OS-BUILD-ORDER|EMERAULD OS build order]] and the event-trigger design at [[governance/EMERAULD-OS-SPEC — Event Triggers]]: every OS stage that assumes a scheduled agent will wake up and act inherits this dependency. It is adjacent to, but distinct from, the freshness and navigation debt catalogued in [[docs/handoff/emerauld-reliability-audit-2026-07-10|the 2026-07-10 reliability audit]], which examined vault content rather than the automation lane that maintains it.

## Details

### The record (evidence, 2026-07-11)

- `morning.sh` exited 1 at 08:00. The entire contents of `Logs/scheduled/morning-2026-07-11.log`: `Failed to authenticate: OAuth session expired and could not be refreshed`.
- The script's own failure handler worked. `Logs/scheduled/FAILURES.md` gained: `- 2026-07-11 08:00 morning run FAILED (exit 1) — see Logs/scheduled/morning-2026-07-11.log`. This handler was added in the [[docs/handoff/vault-overhaul-2026-07-08|2026-07-08 overhaul]].
- Nothing else in the vault changed all day: no note carries `created: 2026-07-11` or `updated: 2026-07-11`, and there are no commits dated 2026-07-11. `FAILURES.md` was the only file written before 22:00.
- The 22:00 nightly run authenticated normally. Its deterministic half passed clean (six registers under threshold, four governed-task gates PASS, `audit-all` 0 violations), and the model pass ran, producing [[2026-07-11|the daily note for 2026-07-11]] after the fact.

### The mechanism (evidence)

- Both scheduled prompts are invoked the same way, through the same binary, with the same credential. There is no per-service key, no service account, and no credential scoped to the scheduled lane.
- Cron has no TTY and no browser. An OAuth flow that needs a refresh it cannot perform fails closed, which is correct behaviour and is why the run exited 1 rather than writing partial state.
- The blast radius is all four agents, not one. Any lapse spanning a scheduled time takes out whichever agents fire in that window.
- The failure is loud in exactly one place and silent everywhere else. `FAILURES.md` is append-only, and no prompt, script or agent reads it. `nightly.sh` carries a comment saying its deterministic remediation "closes the detect-without-fix loop" for registers and governance gates. That closure does not extend to cron-level failures: a failed run is detected, recorded, and then waited on indefinitely.

### Interpretation (synthesis, not evidence)

- The pattern suggests the automation layer's availability is coupled to Martin's interactive Claude usage on the host, since interactive use is what keeps the shared session fresh. Nobody designed that coupling; it is an emergent property of reusing the interactive credential in cron.
- One possible interpretation of 2026-07-11: the session lapsed overnight and was refreshed by ordinary interactive use later in the day, which is why 08:00 failed and 22:00 succeeded. Unresolved: no vault commit or note establishes what refreshed it, so this is inference from the two log lines, not a confirmed sequence.
- Detection latency today was 14 hours, and it was only closed because the nightly pass happened to investigate an empty scan. In the general case, a morning failure is invisible until someone reads `FAILURES.md`. If a lapse spanned both the morning and nightly windows, nothing would surface it at all.

### Candidate controls (flagged, not executed)

Changing anything under `scripts/scheduled/` is an automation change, so it goes through the governed-task path and needs a stop condition, an audit trail, and a rollback path. Martin decides; this note flags. In rough order of cost:

1. **Make `FAILURES.md` readable by the agents.** Have the morning and nightly prompts read `Logs/scheduled/FAILURES.md` and surface unresolved entries into the daily note. Cheapest option, and it extends the detect-and-fix closure to the cron layer.
2. **Preflight the credential.** Have each scheduled script probe auth before the main call and, on failure, write a distinct `AUTH-EXPIRED` marker rather than a generic exit-1 line. This separates "the model refused" from "the model was never reached".
3. **Notify out of band.** An append to `FAILURES.md` should reach Martin at 08:05, not at the next nightly pass. This is the only control that fixes detection latency rather than detection itself.
4. **Give the scheduled lane its own non-interactive credential.** An API key for cron removes the dependency on a refreshable interactive session entirely. Highest cost, and the only option that removes the failure mode rather than surfacing it faster.

Confidence: the record and the mechanism are `stated` (log lines and script source). The interpretation of what refreshed the session is `speculation`. The controls are proposals, not decisions.

## Related

- [[Architecture - EMERAULD Scripts - Overview]]
- [[Architecture - EMERAULD Scripts - Key Decisions]]
- [[governance/EMERAULD-OS-BUILD-ORDER]]
- [[governance/EMERAULD-OS-SPEC — Event Triggers]]
- [[docs/handoff/emerauld-reliability-audit-2026-07-10]]
- [[2026-07-11]]
- [[session-state]]
