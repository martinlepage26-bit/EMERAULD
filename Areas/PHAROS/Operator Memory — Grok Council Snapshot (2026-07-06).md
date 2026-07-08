---
type: note
title: Operator Memory — Grok Council Snapshot (2026-07-06)
tags:
- grok
- operator-memory
- ai-council
- standing-context
- pharos
status: active
domain: pharos
created: '2026-07-08'
updated: '2026-07-08'
vault_area: Areas
canonical_path: Areas/PHAROS/Operator Memory — Grok Council Snapshot (2026-07-06).md
---

> For future Claude: this is Martin's own operator-maintained standing context for how to route work to Grok — treat it as a rule sheet to consult *before* assigning Grok a council role, not as a passive record. It is explicitly framed in the source as "operator-maintained fact, not agent self-report," so its claims about what Grok should/should not be asked to do carry more authority than an agent's inferred read of the same sessions.

## Summary

`martin-operator-memory-grok-council-2026-07-06.md` is a standing reference sheet defining Grok's role in Martin's tmux AI council: an operator-facing adversarial peer (not subordinate to Claude/Codex/Hephaistos routing), reporting directly to Martin, whose default posture is skeptical, short, and gap-finding. It compiles the same 23-session evidence base as the companion usage account into actionable operator rules — which hats to assign, what communication discipline to enforce, which decisions are already settled and should not be re-debated, and what should never be routed to Grok at all.

## Context

**Provenance:** loose file in `/home/martin/Downloads/martin-operator-memory-grok-council-2026-07-06.md`, file mtime **2026-07-06** (UTC), matching its filename date and internal "Last verified: 2026-07-06" header. Not previously represented in the vault (verified via grep across `wiki/` and `Areas/` prior to this note). Companion file: `martin-grok-usage-account-2026-07-06.md` — see [[Areas/PHAROS/Grok Usage Account — Operator Snapshot (2026-07-06)]] for the full session-by-session evidentiary account this sheet is distilled from.

## Details

Verified facts, stated directly in the source:

- **Role definition:** Grok reports to Operator directly; does not own council routing (that belongs to Claude/Hermes/Operator); flags governance concerns to Queen Keyport but findings remain recommendations, not overrides. Coordination happens only via tmux relay when explicitly assigned.
- **Ranked usage (by volume):** (1) tmux council relay/broadcast (~77% of prompts), (2) adversarial critique, (3) PHAROS product builds, (4) Lavoie client delivery, (5) EMERAULD vault ops, (6) full product launches (VoiceBridge, patent-workbench merge), (7) council infrastructure tooling, (8) micro1 partnership prep.
- **Reusable council hats** (quoted verbatim from source): REGRESSION + HARDENING reviewer; Business Strategy Critic; ADVERSARIAL CRITIC; CHALLENGER; Boundary auditor; Stress-tester. Source note: "Grok performs best with a named role + hard constraints (word limits, no tools, inspect-only, etc.)."
- **Communication rules Martin enforces:** short answers over Grok's default over-explaining; no scope creep into coordination; tmux double-Enter hygiene; no em dashes; execute-don't-plan language; real artifacts only ("not examples, real emails to send NOW"); no external send without explicit approval; auto-approve tools was set as a persistent rule from 2026-06-25.
- **Settled decisions flagged "do not re-debate unless Operator reopens":** the Lavoie pricing consensus (4.5k CAD diagnostic, 100% credited to Forfait A within 30 days if signed, at least one visible operational win required during diagnostic, straight-to-Forfait-A alternative at 6.5k if discovery is skipped). Client remains blocked on gates A1–A5 as of the session evidence.
- **PHAROS boundary audit Grok performed:** PHAROS surface (do not migrate off pharos-ai.ca) = pharos-suite, aurorai, compassai, helix, frontend, backend, PHAROS-NEWLOOK. Martin-surface-only = LOTUS, SCRIPTO, GAIA, ECHO, DR. SORT. Canonical repo path confirmed as `websites/pharos-suite/`, not `apps/web-apps/pharos-suite/`. This matches the PHAROS boundary already recorded in root `CLAUDE.md` and the user's persistent memory note on the PHAROS boundary rule.
- **EMERAULD standing council task** (recurring broadcast goal, source's own list): build the PHAROS evidence-to-publication bridge (HELIX/AurorA/COMPASSai → RDAIG/manuscript notes), repair canonical orphans, run `/obsidian-second-brain` on 511+ notes, and hold to "zero orphans tolerated." Retired numeric taxonomy folders (`00_Inbox`, `10_Projects`, etc.) are flagged as drift if any agent still emits them — flat structure is canonical.
- **Model/agent evolution table:** Jun 8–24 used `grok-build`/`grok-build-b` via `grok-build-plan` for heavy builds; Jun 25+ shifted to `grok-composer-2.5-fast` via `cursor` for council relay and lighter tasks. Source guidance: prefer `grok-build-plan` for large multi-hour builds, `grok-composer` via Cursor as current default for council bullets and handoff sync.
- **Explicit "what NOT to route to Grok" list:** council coordination ownership, client-facing email send without explicit approval, creative writing/novel/HEXA art/academic paper drafting, pure research with no build or validation anchor, governance override (Grok flags, Queen Keyport/Operator decide).
- **One-line operator stance, quoted verbatim:** "Grok is the council's contrarian engineer: stress-test first, ship when told, stay short, never coordinate unless asked."

## Related

- [[Areas/PHAROS/Grok Usage Account — Operator Snapshot (2026-07-06)]] — the full 23-session evidentiary account this operator-memory sheet distills into standing rules; read together, not in isolation.
- [[Areas/PHAROS/Trismégiste — Operator State]] — the vault's other operator-continuity snapshot pattern (state captured at a point in time for future-session reference); useful as a structural comparison for how operator memory notes are formatted in this vault.
- [[wiki/Codex Skills Inventory — Complete Registry (241 Skills)]] — comparable registry-style reference for another council agent (Codex), useful when cross-checking role boundaries between council members.
- [[Areas/PHAROS/multi-agent-orchestration Skill — Governance Case File]] — the governance case file for how multi-agent orchestration (including council role assignment) is itself audited in this vault.
- [[Areas/PHAROS/PHAROS Cross-AI Strategy Matrix]] — where Grok's role sits relative to the other AI CLI council members.
