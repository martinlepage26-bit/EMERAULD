---
type: governance-doc
title: STANDARD-BUILD-ORDER — Binding Build Discipline
tags:
  - standard-build-order
  - hephaistos
  - build-discipline
  - handoff-doc
  - three-agent-architecture
status: active
domain: governance
created: '2026-07-08'
updated: '2026-07-08'
vault_area: Areas
canonical_path: Areas/PHAROS/STANDARD-BUILD-ORDER — Binding Build Discipline.md
---

> For future Claude: this note synthesizes a governance artifact rather than
> reproducing it in full. Source:
> `/home/martin/.agents/hephaistos/STANDARD-BUILD-ORDER.md`. Do not paste updated
> copies of the standard itself into this note — if the standard changes, re-read the
> canonical file and update this synthesis; the canonical file is the only place the
> block itself may be edited.

## Summary

The Standard Build Order is a short, deliberately immutable block of directives that
gets pasted verbatim into every autonomous build or agent order issued inside the
[[Areas/PHAROS/HEPHAISTOS Agent Architecture|HEPHAISTOS]] three-agent stack. Its own
header states the design intent directly: "Paste verbatim into every autonomous
build/agent order. Do not edit per-task. Verbatim reuse is the point: the standard must
not drift between sessions or models." (Source:
`/home/martin/.agents/hephaistos/STANDARD-BUILD-ORDER.md`, lines 1-3.)

## Context

The file positions itself as a single source of truth referenced by `AGENTS.md` (the
canon) and its per-tool adapters (`CLAUDE.md`, `.codex/AGENTS.md`, `.grok/AGENTS.md`,
etc.) — consistent with the "one canon, thin adapters" meta-rule that governs the whole
`.agents/hephaistos/` repository. The closing line is explicit about the edit
discipline: "If you change the standard, change it here and let the references
inherit — never edit a pasted copy" (source file, line 27). This matters because the
Standard Build Order is meant to travel unchanged across every session, every model
(Claude, Codex, Grok, Gemini, Kimi, Vibe), and every autonomous build task — drift
between copies would defeat the point of having a shared standard at all.

## Details

### What it binds

The block covers eleven directives that apply to any autonomous build or agent order.
In substance, not verbatim, these bind:

- Inspecting git status before touching files, and never clobbering concurrent work.
- Never printing secrets, JWTs, API keys, proxy secrets, or credential contents.
- Never mutating live client data or polluting a real client org with demo data —
  tester accounts only.
- Routing all CLI/MCP behavior through the canonical API, never direct DB writes.
- Treating the canonical public surface as the only address consumers should be
  pointed at — never a tunnel, a raw DB, or a machine-local shortcut.
- Respecting data residency (the intended stack, not accidental cloud/client drift).
- Not over-claiming capability — anything touching law, money, or autonomy needs a
  human gate and must stay inside the provable envelope.
- Running relevant tests/builds/smokes before any completion claim.
- Committing and pushing only cohesive, passing chunks, with blockers documented in
  the handoff.
- The hard-stop handoff rule (below).
- Ending every completion report with changed files, commit hash, verification
  commands and results, and the strongest remaining concern.

### The hard-stop handoff rule

The rule that gives the standard its teeth: a build turn must never end without
writing or updating `docs/handoff/<name>.md`, and that file must contain what's done,
commit hashes, the exact verification commands run plus their results, live URLs,
risks, and the next decision. If the next-decision field cannot be filled in, the
standard's own wording is that the work is **abandoned**, not paused — there is no
neutral "paused" state available to a build turn that stops without a live next step.
This mirrors the Martin-facing rule already in force via `~/AGENTS.md`
(InfraFabric Hosted Task Discipline: `task.closed` is the only completed closeout
event; handoff docs are evidence, not the closeout itself) but operates one level
down, at the level of a single build turn rather than a whole hosted task.

### Where the canonical file lives

Canonical location: `/home/martin/.agents/hephaistos/STANDARD-BUILD-ORDER.md`. Per its
own closing note, this is "source of truth for the above block," referenced by
`AGENTS.md` (the canon) and its adapters — the standard is defined once here and
inherited everywhere else, never independently edited in a copy.

## Related

- [[Areas/PHAROS/HEPHAISTOS Agent Architecture|HEPHAISTOS Agent Architecture]]
- [[Areas/PHAROS/Architecture Translation Guide — Eight Operators to Three-Agent Stack]]
- [[RELAY-LEDGER — Live Governance Handoff Ledger]]
- [[HEPHAISTOS Phase 7 — Final Buildout Report]]
