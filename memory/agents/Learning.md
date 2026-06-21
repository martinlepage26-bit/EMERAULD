# Learning

Reusable lessons that change future method. Both Claude and Codex write here.
Only add entries that are non-obvious and likely to prevent future error.

> **Append-only log. Do not edit or "fix" existing entries.** Historical entries preserve original paths and states at the time they were written — they are not errors or drift.

---

## 2026-04-25 — CLAUDEX peer messaging requires explicit operator direction
- Observation: Claude sent MIRROR REQUIRED messages to Codex via claude-peers. All messages showed `delivered: 1` in broker DB. Codex did not respond automatically even though it was active.
- What changes: Do not assume Codex will react to unsolicited peer messages. Codex needs Martin to explicitly direct it to check the channel, or a preemptive context message to unblock it.
- New rule: After posting MIRROR REQUIRED, tell Martin "go direct Codex to check the peer channel" rather than waiting for an automatic response.
- Links: [[Events]] [[Decisions]] [[claude-peers-mcp — Claude Peer Network]] [[GSD — Get Shit Done Context Engineering System]]

## 2026-04-25 — CLAUDE.md is a consumer of AGENTS.md, not a peer
- Observation: CLAUDE.md Load-on-Trigger rules were missing HENRY, Gadget, Argus, Trismégiste — all four were already correctly defined in AGENTS.md. The gap was in the consumer, not the source.
- What changes: When auditing routing gaps, check AGENTS.md Scope Recognition Table as the authoritative source. CLAUDE.md should mirror it, not define it.
- New rule: AGENTS.md is authoritative for bound-agent scope recognition. CLAUDE.md convenience rules must be kept in sync with it.
- Links: [[Decisions]] [[HEPHAISTOS Agent Architecture]] [[Trismégiste — Personal AI Assistant]] [[HENRY — Research Paper Writing System]] [[Emotional Alliance vs. Evidentiary Discipline in AI]] [[Narrative Capture Failure Taxonomy — Substituting Theory for Contact]]

## 2026-05-02 — Topic-hub backlink count is a cheap, reliable asymmetry detector
- Observation: Counting inbound links to each topic hub is a fast, mechanical audit that surfaces structural asymmetries vector search misses. Pre-campaign scan found three method papers with 0 backlinks from [[Recursive Governance Theory]] despite being the core method literature; vector search returned them as semantically central but did not flag the missing topical bridge.
- What changes: Backlink count is now part of vault traversability audits. Run `grep -c "Hub Title" wiki/*.md` (or equivalent) against each topic hub; flag any hub under 4 inbound for review. Median across the 26 vault topic hubs is ~10; floor of 4 is the empirically observed lower bound for healthy discoverability.
- New rule: When adding or auditing a topic hub, verify that all foundational papers in its scope link to it explicitly in their Summary section. Vector adjacency is necessary but not sufficient.
- Links: [[Decisions]] [[Journal]] [[Vault Cluster Discovery and Linking Opportunities — 2026-05-01]] [[Recursive Governance Theory]]

## 2026-05-02 — Auto-memory is not tracker discipline
- Observation: During the 2026-05-01..02 linking campaign, Claude's auto-memory (`project_vault_linking_audit.md`, `project_vault_linking_iteration2.md`) captured the campaign accurately. The operator-visible trackers (master tracker, session-state, VAULT ADDITIONS TRACKER) and the shared agent memory registers (Journal/Decisions/Learning/Events) did not. Auto-memory satisfies the "what would future-Claude need to know" question; it does not satisfy the "what would Codex, the operator, or any non-Claude reader find on disk" question.
- What changes: Treat auto-memory as a Claude-private cache, not a substitute for shared trackers. The shared trackers are the durable record; auto-memory is a private notebook that happens to persist across sessions.
- New rule: At every major milestone (not just session close), confirm both layers are updated — auto-memory AND the operator-visible trackers. If auto-memory has the work but trackers don't, the work is undocumented for everyone except future-Claude.
- Links: [[Decisions]] [[Blockers]] [[Journal]] [[VAULT ADDITIONS TRACKER]] [[Master Project Tracker — 2026]]

## 2026-05-02 — Bidirectional discipline requires both ends — outbound link does not raise inbound count
- Observation: During Phase 5 sweep, adding a topic link inside a paper's Summary section raised the topic's inbound count but did NOT raise the paper's inbound count. The paper became MORE discoverable from the topic, but no MORE discoverable from anywhere else. To make the paper discoverable from the topic's backlinks panel, the topic page itself must list the paper.
- Empirical confirmation: Single-pass Python inverse-index over 356 notes, before vs. after Phase 5 outbound-only edits, showed paper inbound counts unchanged. After symmetric TOPIC-page edits adding the papers to existing or new sections, paper inbound counts moved from 1 to 3–5.
- What changes: Paper-to-TOPIC linking is a two-edit operation, not one. Edit the paper's Summary AND edit the TOPIC page's relevant section. The CLAUDE.md "Bidirectional Awareness" rule names this; the empirical confirmation here is that one direction does nothing for the other direction's discoverability metrics.
- New rule: When closing linking gaps, run an inverse-index pre/post check. If a paper's inbound count did not increase, the symmetric edit was missed.
- Links: [[Decisions]] [[Journal]] [[Master Project Tracker — 2026]] [[VAULT ADDITIONS TRACKER]]

## Related

- [[REQUIREMENTS]]
- [[CHANGELOG]]
- [[HISTORY]]
- [[README]]
