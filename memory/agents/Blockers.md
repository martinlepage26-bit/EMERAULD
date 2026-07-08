---
type: memory-register
title: Blockers
tags:
- memory
- agents
- memory-register
- claude
- workaround
- lightrag
- probable
- tracker
status: active
created: '2026-06-21'
updated: '2026-06-26'
vault_area: memory
canonical_path: memory/agents/Blockers.md
backlink_count: 10
backlinks:
- '[[archive/retired-2026-07-08/agent_bus/README]]'
- '[[index]]'
- '[[memory/agents/Antigravity]]'
- '[[memory/agents/Decisions]]'
- '[[memory/agents/Gemini]]'
- '[[memory/agents/Grok]]'
- '[[memory/agents/Journal]]'
- '[[memory/agents/Kimi]]'
- '[[memory/agents/Learning]]'
- '[[memory/agents/Vibe]]'
---

# Blockers

Recurring friction that slows work. Both Claude and Codex write here.
Only add blockers that have repeated or are likely to recur.

> **Append-only log. Do not edit or "fix" existing entries.** Historical entries preserve original paths and states at the time they were written — they are not errors or drift.

---

## 2026-04-25 — Codex does not auto-respond to peer channel pushes
- Blocker: Claude sends peer messages; broker delivers them (delivered=1); Codex does not respond.
- Context: claude-peers uses `claude/channel` push notifications. Codex has the MCP configured but does not surface unsolicited inbound messages to its LLM without operator direction.
- Frequency: Every session where cross-agent coordination is needed.
- Probable cause: Codex does not implement the `claude/channel` push-to-LLM loop the same way Claude Code does.
- Workaround: Include a brief message in the peer send asking Martin to direct Codex, OR preemptively send context before Codex is likely to encounter the issue.
- Related decision: [[Decisions]] — CLAUDEX shared Memory register
- See also: [[claude-peers-mcp — Claude Peer Network]] [[AI Infrastructure Stack]]

## 2026-05-02 — Tracker updates deferred to session close get lost under boil-the-ocean pressure
- Blocker: When the operator invokes `/boil-the-ocean` mid-campaign, focus shifts to completing the work artifact (vault edits, paper bridges, MOC updates). Operator-visible trackers (master tracker, VAULT ADDITIONS TRACKER, session-state) are deferred to "session close" and then forgotten because the campaign extends across iterations and the close never happens cleanly.
- Context: The 2026-05-01..02 vault linking campaign shipped substantial vault changes (4 MOCs restructured, 9 paper bridges, 2 new TOPICs/hubs, vector store rebuild). Auto-memory was current. The four operator-visible trackers and the five-register agent memory had no entry for two days of work until the operator caught it.
- Frequency: Recurrent. The same pattern occurred earlier when work was invisible to Codex until manually flagged.
- Probable cause: Boil-the-ocean rewards finishing the artifact; tracker updates feel like ceremony next to "real work." CLAUDE.md doctrine names this but the doctrine is consulted at session start, not enforced mid-session.
- Workaround: Update operator-visible trackers incrementally as work lands, not at the end. See [[Decisions]] entry "Tracker discipline is incremental, not session-close-only" (2026-05-02).
- Related decision: [[Decisions]] — Tracker discipline is incremental
- See also: [[Learning]] (auto-memory ≠ tracker discipline) [[VAULT ADDITIONS TRACKER]] [[Master Project Tracker — 2026]]

## 2026-05-09 — LightRAG changed ingest can expand into stale repair queue
- Blocker: `scripts/ingest.py --changed --hours 1` may begin with the intended changed wiki notes but then reset older PROCESSING/FAILED LightRAG documents to PENDING and start a broad repair queue.
- Context: During the AGENTS instruction-pack ingest, only four wiki notes had changed in the last hour, but LightRAG reset 318 older documents and began processing 319 total. The run was stopped after it completed a small number of older queued documents; the new bridge note remained `pending` in `.lightrag/storage/kv_store_doc_status.json`.
- Frequency: Likely to recur until the stale LightRAG doc-status queue is intentionally repaired or cleaned.
- Probable cause: LightRAG storage recovery behavior treats previous PROCESSING/FAILED records as resumable work before or alongside the requested changed-note insert.
- Workaround: For quick vault retrieval refreshes, use local `scripts/embed.py` and verify with `scripts/vsearch.py`. Use `scripts/ingest.py` only when an intentional LightRAG repair/rebuild window is acceptable.
- See also: [[EMERAULD Workspace Instructions - Perplexity Computer and Hermes Dashboard]] [[Events]]

## 2026-04-25 — CLAUDE.md routing gaps vs AGENTS.md
- Blocker: CLAUDE.md Load-on-Trigger section drifts from AGENTS.md Scope Recognition Table over time as agents are added to AGENTS.md without updating CLAUDE.md.
- Context: Four agents (HENRY, Gadget, Argus, Trismégiste) were in AGENTS.md but missing from CLAUDE.md.
- Frequency: Will recur whenever a new bound agent is added to the system.
- Probable cause: CLAUDE.md and AGENTS.md are maintained independently with no enforced sync.
- Workaround: After any agent addition to AGENTS.md, check CLAUDE.md Load-on-Trigger section and update it.
- Related decision: [[Decisions]] — CLAUDE.md routing doctrine updated
- See also: [[HEPHAISTOS Agent Architecture]] [[HEPHAISTOS Co-Equal Authority Cleanup — Wave 1 and 2 (2026-04-18)]]

## Related

- [[README]]
- [[STATE]]
- [[WHITE PAPER IF.STORY]]
