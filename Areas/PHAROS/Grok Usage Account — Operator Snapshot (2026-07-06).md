---
type: note
title: Grok Usage Account — Operator Snapshot (2026-07-06)
tags:
- grok
- ai-council
- usage-audit
- session-analysis
- pharos
- note
- areas
status: active
domain: pharos
created: '2026-07-08'
updated: '2026-07-08'
vault_area: Areas
canonical_path: Areas/PHAROS/Grok Usage Account — Operator Snapshot (2026-07-06).md
backlink_count: 3
backlinks:
- '[[Areas/PHAROS/Governance and PHAROS MOC]]'
- '[[Areas/PHAROS/Operator Memory — Grok Council Snapshot (2026-07-06)]]'
- '[[_vault/VAULT ADDITIONS TRACKER]]'
---

> For future Claude: this note records what a full scan of Martin's Grok CLI session history actually shows about how Grok gets used in the AI council, as opposed to how it is described in policy documents. Read it alongside the companion operator-memory snapshot before assigning Grok a role in any council task — it is evidence, not aspiration.

## Summary

`martin-grok-usage-account-2026-07-06.md` is a compiled account of 23 Grok CLI sessions (`~/.grok/sessions/%2Fhome%2Fmartin/`, 2026-06-08 through 2026-07-06, 454 distinct user queries) answering the question "what does Martin actually do with Grok." Bottom line stated in the source: Martin runs Grok as **one seat in a multi-agent operating system for PHAROS AI** — a skeptical, adversarial, execution-capable council peer that builds, critiques, deploys, stress-tests, and challenges other agents (Claude, Codex, Gemini, Kimi, DeepSeek/Hermes), not a generic chatbot.

## Context

**Provenance:** loose file in `/home/martin/Downloads/martin-grok-usage-account-2026-07-06.md`, file mtime **2026-07-06** (UTC), consistent with the date in its own filename and header ("Compiled: 2026-07-06"). Not previously represented in the vault (verified via grep across `wiki/` and `Areas/` prior to this note; existing "grok" hits were incidental mentions inside HELIX/PHAROS notes, not a dedicated usage audit). Companion file: `martin-operator-memory-grok-council-2026-07-06.md`, same directory, same timestamp — see the sibling note for the operator-facing standing-context version of this same evidence base.

## Details

Verified facts, as stated in the source document:

- **Corpus:** 23 sessions, 454 queries, Jun 8 – Jul 6 2026. Primary models: `grok-build` (14 sessions), `grok-composer-2.5-fast` (8), `grok-build-b` (1). Roughly 77% of query volume is tmux council traffic (broadcasts, relay prompts, cross-agent coordination); ~23% is direct build/review work.
- **Five roles observed in practice:** adversarial critic (pricing, strategy, architecture, governance claims), builder (HTML/React/Python, Cloudflare deploys, mock datasets, skills), council relay node (tmux broadcast receipt/relay), product validator (AurorA → COMPASSai → HELIX pipeline stress-testing), client delivery agent (Lavoie offer pages, pricing debates, Base44 review).
- **Named council hats already assigned to Grok** across sessions: REGRESSION + HARDENING reviewer, Business Strategy Critic (Lavoie), ADVERSARIAL CRITIC (EMERAULD/vault drift), CHALLENGER (dispute priority ordering), Agent B boundary auditor (PHAROS vs non-PHAROS classification).
- **Major deliverables shipped:** chaotic mock governance dataset (38 fixtures, 15+ use cases) stress-testing the AurorA → COMPASSai handoff pipeline; `helix-integration.ts` and HELIX Python stubs live inside COMPASSai on Railway; pharos-suite frontend work (EU AI Act "law challenge" page, hero rebrand, regression review); Lavoie offer page deploy + questionnaire flow; the largest single build was the VoiceBridge AAC Bridge Fund launch (2,919 messages) — full bilingual site, legal/grant docs, donor emails, Cloudflare Pages deploy at `voicebridge.pharos-ai.ca`.
- **Lavoie pricing council** (5 rounds, Jun 11–12): converged on a 4.5k CAD diagnostic credited 100% toward Forfait A, with Grok's standing objection flagged as extraction risk on a Saguenay cash-flow-sensitive client.
- **Communication discipline Martin enforces on Grok:** demands for shorter responses, direct correction when Grok "dérogé" from scope, explicit tmux double-Enter hygiene, no em dashes, imperative execution language ("go", "DO IT", "proceed").
- **Temporal arc (source's own periodization):** Phase 1 (Jun 8–14) product shipping/commercialization; Phase 2 (Jun 15–22) maximum execution depth (VoiceBridge, governance QA); Phase 3 (Jun 25–30) council infrastructure itself (broadcast, STT, agent auth); Phase 4 (Jul 3–6) synchronization and token economics.
- **Explicitly out of scope for Grok**, per the source: sustained creative writing, academic paper drafting, standalone research without a build/delivery anchor, client email sending without explicit stop/approval commands.

Inference (not stated verbatim, drawn from the pattern across sessions): the shift from `grok-build`/`grok-build-plan` to `grok-composer-2.5-fast`/`cursor` after Jun 25 tracks a shift in council usage from heavy solo builds toward lighter-weight relay and synchronization tasks — the source frames this as a model/agent evolution table rather than stating the causal claim outright.

## Related

- [[Areas/PHAROS/PHAROS Cross-AI Strategy Matrix]] — the standing comparison of what each council agent (Claude, Codex, Grok, Gemini, etc.) is for; this note supplies the evidentiary backing for Grok's entry specifically.
- [[Areas/PHAROS/HELIX Development Session — Grok Collaboration and v2.1 to v2.4 Build]] — an earlier, narrower record of Grok's role in HELIX protocol development, now superseded in scope by this full 23-session audit.
- [[Areas/PHAROS/argus-drift-audit-scope-multi-agent-orchestration]] — related audit work on multi-agent orchestration drift; relevant given this note's finding that Grok itself performed an adversarial audit of the EMERAULD vault (session `019ee908`).
- [[wiki/AI Infrastructure Stack]] — vault-level map of the AI tooling stack this Grok usage pattern sits inside.
- [[Areas/PHAROS/Operator Memory — Grok Council Snapshot (2026-07-06)]] — companion note synthesizing the same evidence base into standing operator guidance for future council routing decisions.
