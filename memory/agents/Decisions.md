---
type: memory-register
title: Decisions
tags:
- memory
- agents
- memory-register
- impact
- expected
- topic
- events
status: active
created: '2026-06-21'
updated: '2026-06-26'
vault_area: memory
canonical_path: memory/agents/Decisions.md
backlink_count: 11
backlinks:
- '[[Logs/2026-06-29]]'
- '[[index]]'
- '[[memory/agents/Antigravity]]'
- '[[memory/agents/Blockers]]'
- '[[memory/agents/Events]]'
- '[[memory/agents/Gemini]]'
- '[[memory/agents/Grok]]'
- '[[memory/agents/Journal]]'
- '[[memory/agents/Kimi]]'
- '[[memory/agents/Learning]]'
- '[[memory/agents/Vibe]]'
---

# Decisions

Structural decisions made across sessions. Both Claude and Codex read and write this register.
Do not add minor implementation choices — only decisions that change future method or architecture.

> **Append-only log. Do not edit or "fix" existing entries.** Historical entries preserve original paths and states at the time they were written — they are not errors or drift.

---

## 2026-04-25 — CLAUDEX shared Memory register created
- Decision: Implement five-register Memory system as a shared Claude/Codex surface inside [[Trismégiste — Personal AI Assistant|EMERAULD]].
- Why: Existing STATUS.md covers session state snapshots; auto-memory covers preferences/feedback. Neither captures cross-agent structural decisions, recurring blockers, or tool/API events. A shared governed register fills that gap without mirroring overhead.
- Alternatives refused: Per-project Memory folders (fragmented); adding registers to auto-memory (Claude-only, wrong schema).
- Impact expected: Both agents read context before starting; decisions persist across session resets.
- Links: [[Journal]] [[Events]] [[ROOK — Session Boundary Model]] [[GSD — Get Shit Done Context Engineering System]] [[Recursive Continuity Without Memory — AI Identity Across Sessions]] [[Governed Revision Loop — Responsible Self-Improving Agents]]

## 2026-04-25 — CLAUDE.md routing doctrine updated
- Decision: Replaced `## Load-on-Trigger Rules` with `## Load-on-Trigger / Custom Agent Routing` — added routing priority, selection rules, HENRY/Gadget/Argus/Trismégiste triggers, and Completion Rule.
- Why: CLAUDE.md was missing explicit triggers for four bound-identity agents already defined in AGENTS.md. GPT-suggested merge structure provided cleaner two-section format.
- Alternatives refused: Separate section (would duplicate existing escalation rules).
- Impact expected: Automatic scope-recognition loading for all seven bound agents.
- Links: [[Learning]] [[HEPHAISTOS Agent Architecture]] [[HEPHAISTOS Co-Equal Authority Cleanup — Wave 1 and 2 (2026-04-18)]]

## 2026-04-25 — Correction: shared Memory registers are in EMERAULD (not `/home/cerebrhoe/Memory/`)
- Decision: Treat `/mnt/c/Users/softinfo/Documents/EMERAULD/memory/agents/` as the canonical shared Memory register location (Decisions/Learning/Blockers/Journal/Events).
- Why: Martin is an AI Governance Consultant — agent operational memory belongs in his knowledge graph alongside client and governance work, not in a separate WSL silo.
- Impact expected: Stops path drift; session-start and session-close doctrine should reference the EMERAULD path.
- Links: [[Events]] [[Journal]] [[Governance and PHAROS MOC]] [[Martin Lepage — AI Governance Consulting Profile Assessment]]

## 2026-05-02 — Topic Indexes is the canonical discovery surface for MOCs
- Decision: Each MOC must populate a `Topic Indexes` section explicitly listing organizing TOPICs, organized by category. Body-prose inline links serve narrative, not navigation.
- Why: Pre-campaign audit found that [[Writing and Novels MOC]] had only 1 inline TOPIC link in its body; [[Personal and Projects MOC]] surfaced only 2 of 8 relevant TOPICs in its index; [[Governance and PHAROS MOC]] body referenced Authority/Care/Consent/Controls TOPICs without listing them in Topic Indexes. Readers scanning an MOC for organizing concepts use the section header — body links are not discoverable.
- Alternatives refused: rely on body links (insufficient); use a separate index file (fragments the MOC, defeats one-stop navigation).
- Impact expected: Future TOPIC additions get reflected in the relevant MOC's Topic Indexes section, not just inline.
- Links: [[Journal]] [[Learning]] [[Vault Cluster Discovery and Linking Opportunities — 2026-05-01]] [[Home]] [[Governance and PHAROS MOC]] [[Writing and Novels MOC]] [[Personal and Projects MOC]]

## 2026-05-02 — Foundational method papers must link to their organizing TOPIC in Summary
- Decision: Every method paper's Summary section must include an inline link to the organizing TOPIC. Pre-campaign audit found three foundational method papers ([[Recursive Deterministic AI Governance — Method and Paper]], [[First Method Paper — Recursive AI Governance as Executable Method]], [[Loop Papers and Recursive Governance]]) with no link to [[Recursive Governance Theory]]. This is the most critical class of linking gap because method papers anchor the conceptual scaffolding of the rest of the corpus.
- Why: Without the Summary-level link, the method paper appears in vector search but not in topic-driven traversal. A reader entering through the TOPIC cannot reach the foundational paper; a reader entering through the paper cannot ascend to the organizing concept.
- Alternatives refused: rely on Related/Sources sections (links there are not surfaced as prominently in backlinks; readers skip them).
- Impact expected: Future method-paper additions check Summary-link discipline against the organizing TOPIC before being considered complete.
- Links: [[Journal]] [[Learning]] [[Recursive Governance Theory]] [[Recursive Deterministic AI Governance — Method and Paper]] [[First Method Paper — Recursive AI Governance as Executable Method]] [[Loop Papers and Recursive Governance]]

## 2026-05-02 — Tracker discipline is incremental, not session-close-only
- Decision: Master tracker, VAULT ADDITIONS TRACKER, and the daily log are updated as work lands, not deferred to session close. The five-register agent memory (Decisions/Learning/Journal/Events/Blockers) is still session-close, but operator-visible trackers must reflect the work in real time.
- Why: The 2026-05-01..02 linking campaign demonstrated the failure mode. Vault file edits were persisted; auto-memory was current; but durable operator-visible trackers had not been updated until the operator caught the omission ("HAVE WE BEEN UPDATING TRACKERS?"). If the operator had not asked, the work would have been invisible to any future session that did not read auto-memory directly.
- Alternatives refused: continue session-close-only updates (recurrent failure mode); add a closing checklist (already in CLAUDE.md doctrine; was not honored under boil-the-ocean pressure).
- Impact expected: Linking campaigns and similar work-in-flight log to operator-visible trackers as they progress, not only at the end.
- Links: [[Journal]] [[Blockers]] [[Learning]] [[VAULT ADDITIONS TRACKER]] [[Master Project Tracker — 2026]]

## 2026-05-08 - Perplexity Computer temporary counterpart seat
- Decision: Treat Perplexity Computer as the temporary active counterpart in the workspace seat previously occupied by Claude.
- Why: Martin explicitly asked Codex to replace Claude with Perplexity Computer for now and welcome her.
- Boundary: Additive, not destructive. Claude-era files remain provenance, compatibility, and historical coordination surfaces until Martin explicitly promotes replacements.
- Impact expected: Codex addresses the temporary collaborator as Perplexity Computer for current coordination unless Martin says otherwise.
- Links: [[Events]] [[Journal]] [[Welcome]] [[AI Infrastructure Stack]]

## 2026-05-12 — Knowledge scan default locked to verified hard-move intake in /raw
- Decision: When Martin asks for new-knowledge scans, agents must execute a fixed chain: broad scan, verification first, hard-move verified sources into `/raw/`, wiki synthesis, graph linking, and final `verified` vs `inferred` reporting.
- Why: Operator explicitly requested this as default behavior (`from now on ... hard-moved in /raw, after verification`).
- Alternatives refused: scan-only manifests without synthesis; writing wiki first then provenance intake; defaulting new intake to legacy `raw sources/` lanes.
- Impact expected: Stronger source discipline, cleaner intake lane ownership, and less ambiguity between verified evidence and derived inference.
- Links: [[Events]] [[Welcome]] [[session-state]] [[Recursive Governance Memo — EMERAULD Control Packet (2026-05-12)]]

## 2026-05-12 — Knowledge scan workflow hardened as fail-closed with intake verifier
- Decision: Enforce a fail-closed gate for scan intake. No wiki synthesis may use unverified artifacts. Duplicate-hash artifacts are excluded from hard-move by default.
- Mechanism: Canonical script `/mnt/c/users/softinfo/documents/emerauld/scripts/verify_and_hardmove_to_raw.py` now verifies artifacts and hard-moves only verified, non-duplicate files to `/raw/`, emitting a machine-readable report (`verified` vs `rejected`).
- Why: Operator requested hardening after locking `/raw` as canonical intake lane.
- Impact expected: Intake runs become auditable, reproducible, and resistant to source/provenance drift.
- Links: [[Events]] [[Welcome]] [[session-state]] [[Recursive Governance Memo — EMERAULD Control Packet (2026-05-12)]]

## 2026-05-13 — Preserve scan-pack structure under /raw
- Decision: Scan packs should be hard-moved under `raw/<scan-label>/` with relative paths preserved, using the shared `raw/.intake-manifest.jsonl` for duplicate checks.
- Why: The May 12 scan packs contained multi-folder source sets; flattening them would erase useful provenance and create filename-collision risk.
- Mechanism: `scripts/verify_and_hardmove_to_raw.py` now supports `--dry-run`, `--preserve-relative-to`, and a global manifest path.
- Impact expected: Future scans can preview moves, preserve source layout, and report verified vs rejected artifacts without degrading provenance.
- Links: [[Events]] [[session-state]] [[D Drive Scan — 2026-05-12]] [[Desktop and Downloads Scan — 2026-05-12]]

---

## 2026-06-21 — Retire numeric taxonomy; adopt flat PARA structure (BACKFILL)
- Decision: Retire the `00_–90_` numeric folder taxonomy. Adopt flat PARA structure: `projects/`, `wiki/`, `archive/`, `resources/`, `raw/`, `memory/`. No more numbered prefixes.
- Why: The taxonomy was adding friction without adding retrieval value. Obsidian search and the vector store made it redundant. Flat structure is navigable by any agent without knowing a number map.
- Impact: Largest single structural pass in vault history. 879 notes migrated. All CLAUDE.md paths updated to current host. Vector store and graph store rebuilt.
- Links: [[session-state]] [[memory/daily/2026-06-22]]

## 2026-06-21 — Send HELIX outreach to Humania or Koios (BACKFILL — unexecuted as of 2026-06-29)
- Decision: Council decided to send one HELIX outreach message to a named buyer (Humania or Koios). HELIX regulatory arbitrage window (EU AI Act, August 2 2026) is the forcing function.
- Current state: Decision logged 2026-06-21; as of 2026-06-29 (8 days later) the send has not occurred. See [[arise-pattern-report-2026-06-29]] Pattern 3.
- Impact: 34-day window remaining as of 2026-06-29. The decision exists; execution does not.
- Links: [[projects/HELIX — Fisher King Project State]] [[artifacts/emerge-pattern-report-2026-06-29]]

## 2026-06-22 — Ship COMPASSai EU AI Act + Quebec Construction Classifier to Railway production (BACKFILL)
- Decision: Deliver the classifier to Railway production (commit 9bb696b). This is the only shipped external artifact in the June window.
- Why: Active client delivery; EU AI Act + Law 25 compliance classifier as proof-of-concept for COMPASSai governance engine.
- Impact: COMPASSai now has a production deployment. Creates evidentiary basis for at least one paper (Evidence-to-Publication Bridge).
- Links: [[projects/COMPASSai — Fisher King Project State]] [[memory/daily/2026-06-22]]

## 2026-06-29 — Execute Gumroad listing for Obsidian Agent Vault
- Decision: Selected by idea-discovery ranking as #1 next action (31 backlinks, all prerequisites complete, 90-minute action). Executed in full: listing copy finalized, clean zip built (28K, SHA256: 887c44f308a431fe7cb1ef8e6293c6f1b27940faf997985b97d7f2bfcfc7cc6c), social posts ready.
- Why now: EMERAULD 2026-06-29 session produced Obsidian OS scaffold, architecture notes, and pattern report — making the vault the strongest demo object it has ever been. All prerequisites done; only the manual gumroad.com product creation remains.
- Impact expected: First commercial listing for a PHAROS-adjacent product. $49 template pack. Revenue + proof-of-concept signal for the PHAROS product surface.
- Links: [[artifacts/marketplace/promo/gumroad-listing]] [[artifacts/marketplace/promo/social-posts]] [[projects/Second Brain — Fisher King Project State]] [[Areas/PHAROS/Obsidian Agent Vault — Launch Kit]]

## Related

- [[Operational indicators and discriminating evidence]]
