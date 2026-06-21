# Events

Tool, API, dependency, and workflow changes. Both Claude and Codex write here.
Only add events that could affect future agent behavior or session setup.

> **Append-only log. Do not edit or "fix" existing entries.** Historical entries preserve original paths and states at the time they were written — they are not errors or drift.

---

## 2026-04-25 — CLAUDE.md section renamed and expanded
- Event: `## Load-on-Trigger Rules` renamed to `## Load-on-Trigger / Custom Agent Routing` with new subsections.
- Tool affected: Claude Code (CLAUDE.md boot config).
- Why important: Old section name may appear in prior session notes or logs; new section is a superset with different structure.
- Action: If referencing the old section name in any doc, update to new name.
- See also: [[HEPHAISTOS Agent Architecture]]

## 2026-04-25 — claudex/codex/gotchas.md updated with Agent Routing section
- Event: New `## Agent Routing` section added to Codex-side gotchas. Includes gsd-agent trigger map and bound-identity agent note.
- Tool affected: Codex (claudex skill, codex/gotchas.md). See [[GSD — Get Shit Done Context Engineering System]].
- Why important: Codex now has explicit routing guidance; prior sessions had no routing section here.
- Action: None — active immediately.

## 2026-04-25 — claudex/codex/references.md updated with Bound-identity routing table
- Event: New table added mapping all seven bound-identity agents to their canonical entrypoint paths.
- Tool affected: Codex (claudex skill, codex/references.md). Agents covered: [[HENRY — Research Paper Writing System]], [[Trismégiste — Personal AI Assistant]], [[HEPHAISTOS Agent Architecture]].
- Why important: Codex previously had no single reference for bound-agent entrypoints.
- Action: None — active immediately.

## 2026-04-25 — /home/cerebrhoe/Memory/ created
- Event: Five-register shared memory system created for Claude and Codex.
- Tool affected: Both Claude Code and Codex.
- Why important: New session-start and session-close protocol — both agents should read/update this folder.
- Action: Both agents wire session-start read and session-close update into their operating procedure.
- See also: [[Recursive Continuity Without Memory — AI Identity Across Sessions]] [[Governed Revision Loop — Responsible Self-Improving Agents]] [[Agent Session Phenomenology]] [[ROOK — Session Boundary Model]]

## 2026-04-25 — Correction: canonical Memory path is EMERAULD
- Event: Canonical shared registers confirmed at `/mnt/c/Users/softinfo/Documents/EMERAULD/memory/agents/`; `/home/cerebrhoe/Memory/` is not present.
- Tool affected: Both Claude Code and Codex (session-start / session-close doctrine).
- Why important: Prevents re-introducing a dead path into CLAUDEX docs and checklists.
- Action: If any doc references `/home/cerebrhoe/Memory/`, update it to the EMERAULD path; do not recreate `/home/cerebrhoe/Memory/` without an explicit new decision.
- See also: [[Trismégiste — Personal AI Assistant]] [[Governance and PHAROS MOC]] [[Decisions]]

## 2026-05-02 — EMERAULD vector store rebuilt (358 embeddings)
- Event: LightRAG vector store rebuilt after 2026-05-01..02 linking campaign. 358 embeddings indexed using sentence-transformers `all-MiniLM-L6-v2` (fully local, ~2 min build time).
- Tool affected: `scripts/embed.py` and `scripts/vsearch.py` under `/mnt/c/Users/softinfo/Documents/EMERAULD/scripts/`. Run via `/home/cerebrhoe/.venvs/lightrag/bin/python3.12`.
- Why important: New TOPIC ([[Disability Epistemology and Institutional Critique]]), new hub (Narrative-Method Integration), and the cluster-discovery roadmap ([[Vault Cluster Discovery and Linking Opportunities — 2026-05-01]]) are now searchable. Existing TOPICs with new inbound links surface differently in semantic queries.
- Action: None — active immediately. Operators using `vsearch.py` get current results.
- See also: [[Journal]] [[Vault Cluster Discovery and Linking Opportunities — 2026-05-01]]

## 2026-05-02 — HENRY closeout audit added to vault discipline
- Event: Operator invocation of `Henry, load, and verify that all important things were noted and written down` after a long campaign session demonstrated a useful pattern: invoke HENRY at session close to audit documentation completeness against the actual work performed.
- Tool affected: HENRY agent (`/home/cerebrhoe/hephaistos/HENRY.md`). Workflow pattern; no code change.
- Why important: HENRY's Claim→Evidence audit applied to the documentation trail catches gaps between "work done" and "work recorded." Caught the master-tracker / session-state / agent-memory omission in this session.
- Action: Consider adopting as a standing practice for long campaign sessions where boil-the-ocean pressure tends to push tracker updates to the end.
- See also: [[HENRY — Research Paper Writing System]] [[Journal]] [[Decisions]]

## 2026-05-08 - Perplexity Computer welcomed into EMERAULD
- Event: `PERPLEXITY-COMPUTER.md` added as the temporary orientation note, `AGENTS.md` now records the temporary seat, and `Welcome.md` points incoming collaborators to the new note.
- Tool affected: Cross-agent workspace coordination for EMERAULD.
- Why important: The active collaborator seat is no longer assumed to be Claude for current coordination, while Claude-era files remain preserved as historical and compatibility context.
- Action: Use Perplexity Computer as the current counterpart name unless Martin explicitly routes work back to Claude.
- See also: [[Decisions]] [[Journal]] [[Welcome]] [[AI Infrastructure Stack]]

## 2026-05-09 - AGENTS instruction pack promoted into graph/vector retrieval
- Event: Root `AGENTS.md` instructions for the Perplexity Computer seat and Hermes Dashboard design system were captured as a raw source and promoted into a wiki bridge note.
- Tool affected: Cross-agent workspace coordination, EMERAULD retrieval, Hermes Dashboard implementation context.
- Why important: Root instructions are outside `wiki/`, so they need a graph-facing bridge to be retrievable through the vault knowledge layer.
- Retrieval status: Local vector index rebuilt successfully with 748 embeddings; `vsearch` returns the bridge note as the top result. LightRAG registered the note but left it pending because `scripts/ingest.py --changed --hours 1` expanded into a stale 319-document repair queue and was stopped.
- Action: Treat `AGENTS.md` as the runtime source of truth and [[EMERAULD Workspace Instructions - Perplexity Computer and Hermes Dashboard]] as the retrieval/navigation bridge.
- See also: [[Welcome]] [[Hermes Dashboard — Professional Governance Tool]] [[Governance and PHAROS MOC]]

## 2026-05-12 — Canonical /raw intake lane activated for knowledge scans
- Event: Operator locked new-knowledge scan workflow to verified hard-move intake in `/raw/` (`C:\Users\softinfo\Documents\EMERAULD\raw`).
- Tool affected: Cross-agent vault intake workflow (`AGENTS.md`, `CLAUDE.md`, `PERPLEXITY-COMPUTER.md`, `Welcome.md`).
- Why important: Separates verified source intake from legacy raw lanes and enforces evidence-first sequencing before wiki synthesis.
- Action: For future scans, verify first (integrity, readability, provenance, duplicates), then hard-move verified source artifacts into `/raw/`, then write wiki notes and report `verified` vs `inferred`.
- See also: [[Decisions]] [[Welcome]] [[session-state]]

## 2026-05-12 — Fail-closed verifier script activated for /raw intake
- Event: Added `scripts/verify_and_hardmove_to_raw.py` and made it executable.
- Tool affected: EMERAULD knowledge intake workflow and all agent scan passes.
- Why important: Converts `/raw` policy into enforceable process with duplicate exclusion and report artifacts.
- Action: Run verifier before wiki synthesis in scan workflows; treat report JSON as runtime evidence boundary (`verified` vs `rejected`).
- See also: [[Decisions]] [[Welcome]] [[session-state]]

## 2026-05-13 — May 12 scan packs hard-moved into verified /raw lane
- Event: The D-drive and Desktop/Downloads scan packs were verified and hard-moved from legacy staging into `/raw/`.
- Tool affected: `scripts/verify_and_hardmove_to_raw.py`, `/raw/.intake-manifest.jsonl`, scan index notes, and `VAULT ADDITIONS TRACKER.md`.
- Why important: Brings the freshest scan outputs into alignment with the fail-closed intake rule instead of leaving their evidence path in legacy `raw sources/`.
- Result: D-drive report `raw/intake-report-d-drive-scan-2026-05-12.json` (`41 verified`, `5 rejected`); Desktop/Downloads report `raw/intake-report-desktop-downloads-scan-2026-05-12.json` (`22 verified`, `0 rejected`).
- Action: Future scan notes should cite the verifier report and `/raw/<scan-label>/` path as the evidence boundary.
- See also: [[D Drive Scan — 2026-05-12]] [[Desktop and Downloads Scan — 2026-05-12]] [[session-state]]

## Related

- [[01-REVIEW-FIX]]
- [[CHANGELOG]]
- [[BalancedPool]]
