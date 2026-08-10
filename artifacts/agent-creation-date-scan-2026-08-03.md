# Agent Creation Date Scan - 2026-08-03

Scope: local scan of `C:`, `D:`, and `E:` for Martin-authored agent definitions, agent registries, and preserved agent audit records. System and third-party package folders produced some access/noise and were not treated as authoritative for Martin's agents.

Important distinction:

- `created:` frontmatter in EMERAULD mirrors often records vault import or wrapper creation, not the agent's original formation.
- `CreationTime` from Windows often records copy/import time, not authoring time.
- The best date below is the earliest date directly supported by the scanned files for the agent identity or the current authority contract.

## Main Agent Roster

| Agent | Best supported formation date | Current/contract date evidence | Later wrapper/import dates | Notes |
|---|---:|---|---|---|
| HEPHAISTOS | 2026-04-17 to 2026-04-18 | `CO-EQUAL-AUTHORITY-DECISION.md` says the co-equal decision was decided 2026-04-17; `HEPHAISTOS Agent Architecture.md` has `created: '2026-04-18'`; D canonical `HEPHAISTOS.md` has Contract Version 1.7 dated 2026-04-26. | EMERAULD mirror frontmatter `created: '2026-06-21'`; current `.github/agents/hephaistos.agent.md` wrapper `created: '2026-06-21'`; older `C:\Users\softinfo\.github\agents\hephaistos.agent.md` filesystem created 2026-05-14. | Do not treat June 21 as origin. It is a mirror/wrapper date. |
| Queen Keyport | 2026-04-17 to 2026-04-18 | Same co-equal decision dated 2026-04-17; `HEPHAISTOS Agent Architecture.md` `created: '2026-04-18'`; D canonical `QUEEN-KEYPORT.md` has Contract Version 1.7 dated 2026-04-26. | EMERAULD mirror frontmatter `created: '2026-06-21'`; current `.github/agents/queen-keyport.agent.md` wrapper `created: '2026-06-21'`; older `C:\Users\softinfo\.github\agents\queen-keyport.agent.md` filesystem created 2026-05-14. | Current role is governance co-authority, not a Tier 1 subordinate. |
| Hermes | 2026-04-18 | `HEPHAISTOS Agent Architecture.md` `created: '2026-04-18'`; audit inventory says canonical Hermes entrypoint and `.claude/agents/hermes.md` were last modified 2026-04-18; D canonical `HERMES.md` has Contract Version 1.7 dated 2026-04-26. | EMERAULD mirror frontmatter `created: '2026-06-21'`; current `.github/agents/hermes.agent.md` wrapper `created: '2026-06-21'`; older `C:\Users\softinfo\.github\agents\hermes.agent.md` filesystem created 2026-05-14. | Downstream routing/integration agent. |
| Argus | 2026-04-09 to 2026-04-18 | 2026-04-23 audit inventory records `argus-persona.md` last modified 2026-04-09, and Argus contract/formation files last modified 2026-04-18. D `argus-contract.md` has Contract Version 1.1 dated 2026-04-23. | `Areas/PHAROS/Argus.md` `created: '2026-05-06'`; `.github/agents/argus.agent.md` wrapper `created: '2026-06-21'`; root `ARGUS.md` constitutional entrypoint `created: '2026-07-08'`; Argus contract v1.2 amended 2026-07-09. | Best reading: Argus identity existed by 2026-04-09/18; current independent, flag-only placement was reconciled 2026-04-23. |
| Trismegiste / Trismégiste | 2026-04-18 | `Areas/PHAROS/Trismégiste — Personal AI Assistant.md` has `created: '2026-04-18'`; related eval note says the older architecture was abandoned on 2026-04-18 when Trismégiste became the dispatch identity via `CLAUDE.md`. | `.github/agents/trismegiste.agent.md` wrapper `created: '2026-06-21'`; older `C:\Users\softinfo\.github\agents\trismegiste.agent.md` filesystem created 2026-05-14. | Parallel continuity and synthesis layer, external to the HEPHAISTOS/QK/Hermes hierarchy. |
| HENRY | 2026-04-23 | D and EMERAULD `HENRY.md` state Contract Version 1.1, flag-only reconciliation, dated 2026-04-23, effective April 2026. 2026-04-23 audit inventory lists HENRY entrypoint and `.claude/agents/henry.md` last modified 2026-04-23. | `.github/agents/henry.agent.md` wrapper `created: '2026-06-21'`; older `C:\Users\softinfo\.github\agents\henry.agent.md` filesystem created 2026-05-14. | Independent specialist at Argus level in the current model. |
| Gadget | 2026-04-23 | D and EMERAULD `GADGET.md` state Contract Version 1.1, flag-only reconciliation, dated 2026-04-23, effective April 2026. 2026-04-23 audit inventory lists Gadget entrypoint and `.claude/agents/gadget.md` last modified 2026-04-23. | `.github/agents/gadget.agent.md` wrapper `created: '2026-06-21'`; older `C:\Users\softinfo\.github\agents\gadget.agent.md` filesystem created 2026-05-14. | Independent specialist at Argus level. |
| Bowie | 2026-05-08 for the named identity; 2026-06-21 or 2026-07-09 for the consolidation role | `AGENT ROSTER TRACKER.md` filesystem date 2026-05-08 lists Bowie as an active agent. EMERAULD `BOWIE.md` has `created: '2026-06-21'` and defines the current consolidation operator. `NAMED-AGENT-REGISTRY.md` was installed 2026-07-09 and defines Bowie as Consolidator. | D `bowie/` reports are 2026-07-09 consolidation runs. | The May 8 role was "creative framing, public voice, narrative synthesis"; the later governed role is consolidation/entropy reduction. |

## Roster and Registry Evidence

- `AGENT ROSTER TRACKER.md`, filesystem timestamp 2026-05-08, lists active agents: Hephaistos, Queen-Keyport, Hermès, Argus, Trismégiste, Gadget, Henry, Bowie.
- `NAMED-AGENT-REGISTRY.md`, installed 2026-07-09 in the raw intake copy, defines symbolic-operational boundaries for: Hephaistos, Queen Keyport, Hermes, Argus, Trismégiste, Gadget, Bowie.
- Registry gap: the 2026-07-09 named-agent registry authority clause names `HENRY.md`, and the contracts/roster include HENRY, but the registry body omits a HENRY section.

## Adjacent or Secondary Agents

| Agent/surface | Best supported date | Evidence | Notes |
|---|---:|---|---|
| Rook | 2026-03-03 for Rook v1.4; 2026-04-18 for the PHAROS note | Raw source `Agent Rook Full Explainer v1.4` states `Date: 2026-03-03`; `ROOK — Session Boundary Model.md` has `created: '2026-04-18'`. | Infrastructure/session harness beneath the governance stack, not one of the seven canonical agent identities. |
| Perplexity Computer | 2026-05-08 | `_vault/AGENTS.md` says that as of 2026-05-08 Perplexity Computer was welcomed as the temporary active counterpart; `wiki/PERPLEXITY-COMPUTER.md` has mirror frontmatter `created: '2026-06-21'`. | Workspace seat/counterpart, not the same thing as the new Perplexity agent spec. |
| PHAROS Method Perplexity agent | 2026-08-03 | `.github/agents/pharos-method-perplexity.agent.md` has `created: '2026-08-03'`. | New GitHub-style agent for applying the Pharos Method within Perplexity. |
| Thoth | 2026-05-15 filesystem creation only | `D:\Thoth\agent.md` has no internal `created:` date; Windows `CreationTime` and `LastWriteTime` are 2026-05-15 23:35:58. | AI governance and knowledge agent. Not found in the EMERAULD named-agent registry. |
| CODEX Writing Coach | last written 2026-03-17, copied/created on E 2026-05-09 | `E:\CODEX\AGENTS.md` has no internal `created:` date; Windows `LastWriteTime` is 2026-03-17 and `CreationTime` is 2026-05-09. | Adjacent Codex instruction surface, not an EMERAULD named agent. |
| Legacy `agent-hephaistos` architecture | superseded 2026-04-23 | `E:\PHAROS METHOD REPOSITORY\agent-hephaistos\AGENTS.md` says legacy/superseded 2026-04-23; Windows `LastWriteTime` is 2026-04-23 and `CreationTime` is 2026-05-09. | Old Master Agent / Shadow Auditors / Meta Council architecture. Not current. |
| InfraFabric harness archive | last written 2026-05-02, copied/created on E 2026-05-09 | `E:\HEPHAISTOS-ARCHIVE\extracted\AGENTS.md` is titled Martin Local-First InfraFabric Harness. | Harness/infrastructure surface, not clearly a named agent. |

## Claude Runtime Agent Corpus

The live folders `C:\Users\softinfo\.claude\agents` and `D:\.claude\agents` were not present in this Windows filesystem view. The strongest available evidence is:

- `Areas/PHAROS/Agent Scaffolds — ~agents vs .claude-agents Distinction.md`, `created: '2026-07-08'`, says `/home/martin/.claude/agents/` held 27 agent definition files on 2026-07-08.
- The 27 set included the core/current agents plus ops and reviewer agents.
- Six had matching design scaffolds in `/home/martin/agents/`: `analyst`, `data-query`, `doc-retriever`, `ship-announcer`, `deploy-checker`, `release-coordinator`.
- The remaining inline Claude definitions named in the note were: `hephaistos`, `queen-keyport`, `hermes`, `argus`, `bowie`, `gadget`, `henry`, `trismegiste`, `executor`, `Code-reviewer`, `Code-Simplifier`, `IF-story`, `OCI-Expert`, `Project-Manager`, `Project-Owner`, `Release-Engineer`, `Release-Manager-Resume-Specialist`, `Security-Reviewer`, `Tech-Lead`, `UX-Reviewer`, `WordPress-Coder`, plus the release-coordinator set as phrased in the source.

Because those live `.claude/agents/*.md` files were not mounted in the scanned C/D/E view, their per-file creation dates are not independently dateable from this scan. They are proven to have existed by 2026-07-08.

## Source Paths Used

- `C:\Users\softinfo\Documents\EMERAULD\governance\hephaistos\CO-EQUAL-AUTHORITY-DECISION.md`
- `C:\Users\softinfo\Documents\EMERAULD\Areas\PHAROS\HEPHAISTOS Agent Architecture.md`
- `C:\Users\softinfo\Documents\EMERAULD\governance\hephaistos\AGENT_AUDIT_2026-04-23.md`
- `D:\.AGENTS\hephaistos\HEPHAISTOS.md`
- `D:\.AGENTS\hephaistos\QUEEN-KEYPORT.md`
- `D:\.AGENTS\hephaistos\HERMES.md`
- `D:\.AGENTS\hephaistos\HENRY.md`
- `D:\.AGENTS\hephaistos\GADGET.md`
- `D:\.AGENTS\hephaistos\argus\argus-contract.md`
- `C:\Users\softinfo\Documents\EMERAULD\governance\hephaistos\BOWIE.md`
- `C:\Users\softinfo\Documents\EMERAULD\raw\c-documents-downloads-full-recursive-2026-07-14\Documents\AGENT ROSTER TRACKER.md`
- `C:\Users\softinfo\Documents\EMERAULD\raw\c-documents-downloads-full-recursive-2026-07-14\Downloads\AGENTS\hephaistos\NAMED-AGENT-REGISTRY.md`
- `C:\Users\softinfo\Documents\EMERAULD\Areas\PHAROS\Trismégiste — Personal AI Assistant.md`
- `C:\Users\softinfo\Documents\EMERAULD\Areas\PHAROS\Agent Scaffolds — ~agents vs .claude-agents Distinction.md`
- `C:\Users\softinfo\Documents\EMERAULD\Areas\PHAROS\ROOK — Session Boundary Model.md`
- `C:\Users\softinfo\Documents\EMERAULD\raw sources\infrafabric-archive\Agent Rook Full Explainer v1.4 (IF-2308 Air-Gap Autonomous Hardening).md`
- `C:\Users\softinfo\Documents\EMERAULD\wiki\PERPLEXITY-COMPUTER.md`
- `C:\Users\softinfo\Documents\EMERAULD\.github\agents\pharos-method-perplexity.agent.md`
- `D:\Thoth\agent.md`
- `E:\CODEX\AGENTS.md`
- `E:\PHAROS METHOD REPOSITORY\agent-hephaistos\AGENTS.md`
- `E:\HEPHAISTOS-ARCHIVE\extracted\AGENTS.md`
