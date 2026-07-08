---
type: wiki
title: ChatGPT Apps SDK — Planning, Metadata, Deployment, and Operations
aliases:
- ChatGPT Apps SDK planning guide
- Apps SDK deployment guide
- Apps SDK metadata guide
- wiki/ChatGPT Apps SDK — Planning, Metadata, Deployment, and Operations
tags:
- openai
- chatgpt-apps
- apps-sdk
- mcp
- metadata
- deployment
- security
- troubleshooting
- app-development
- wiki
- chatgpt-apps-sdk-planning-metadata-deployment-and-operations-md
- apps
- golden
- connector
- chatgpt
- prompts
- color-blue
status: active
created: '2026-04-23'
updated: '2026-06-26'
vault_area: wiki
canonical_path: wiki/ChatGPT Apps SDK — Planning, Metadata, Deployment, and Operations.md
backlink_count: 12
backlinks:
- '[[.trash/ACTOR Framework Worksheet]]'
- '[[wiki/ACTOR Framework — Agent vs Chatbot Decision Tool]]'
- '[[wiki/AI Infrastructure Stack]]'
- '[[wiki/Ask Vault — EMERAULD Vault Briefing Skill]]'
- '[[wiki/Custom GPT Products — PHAROS AI GPT Roster]]'
- '[[wiki/Emergent.sh — Agentic App Builder Spec Sheet (2026-06-27)]]'
- '[[wiki/Home]]'
- '[[Areas/PHAROS/MCP and Runtime Integration MOC]]'
- '[[wiki/Personal and Projects MOC]]'
- '[[memory/clients/helix-prospects/HELIX-hermes-assisted-prospect-extension-2026-05-06/2026-05-05_how-td-helps-advance-ai-innovation]]'
- '[[memory/local-session/reference_seven_pillars_stack]]'
- '[[raw/Clippings/AI Agent Operations and Governance Manager]]'
---

# ChatGPT Apps SDK — Planning, Metadata, Deployment, and Operations

## Summary

Consolidated operational note derived from a pasted Apps SDK documentation pack. Covers use-case research, golden-prompt design, metadata optimization, deployment shape, security and privacy, and troubleshooting. Raw capture: `raw sources/2026-04-23_chatgpt-apps-sdk-docs-pack.md`.

## Context

The pasted pack appears to be a local capture of Apps SDK guidance rather than a live-synced mirror of the current documentation. Treat it as a working reference inside EMERAULD, then re-verify against the current official docs before production decisions. This belongs to the same practical build layer as [[AI Infrastructure Stack]], [[CLI-Anything — Agent Harness for Tool Integration]], and [[InfraFabric MCP Stack — Remote Bundles]].

## Details

### 1. Start with use cases, not tooling

The pack is explicit that connector discovery is model-driven: ChatGPT chooses an app when the use case, tool metadata, and prompt language all line up. Before writing tools:

- define the user persona, working context, and success condition for each scenario
- collect direct asks, indirect asks, and system constraints
- write a golden prompt set with direct prompts, indirect prompts, and negative prompts
- rank scenarios by user impact and implementation effort

The practical implication is that a connector should start with one sharp P0 scenario, not a broad surface area.

### 2. Translate scope into a tool contract

Once a use case is in scope, the next move is not UI polish but contract design:

- inputs should be explicit, bounded, and enum-driven where possible
- outputs should include machine-legible fields such as IDs, timestamps, and statuses
- component intent should be chosen deliberately: read-only viewer, editor, or multiturn workspace
- write access should be gated and persistence needs should be identified early

This is the point where legal, privacy, or compliance review should happen if the app touches sensitive or regulated data.

### 3. Treat metadata like product copy

The metadata section frames tool naming and descriptions as a discovery surface:

- use domain-plus-action naming, e.g. `calendar.create_event`
- begin descriptions with `Use this when...`
- state disallowed cases directly to improve precision
- document parameters with examples and defaults
- use `readOnlyHint`, `destructiveHint`, and `openWorldHint` intentionally

The pack recommends evaluating metadata in ChatGPT developer mode against the golden prompt set, changing one field at a time, and logging revision outcomes so recall and precision can be tuned without guessing.

### 4. Deployment requirements are operational, not cosmetic

The deployment section is less about vendor choice than runtime behavior:

- local development can be exposed through `ngrok` to `/mcp`
- every code change implies three steps: rebuild the widget bundle, restart the MCP server, refresh connector metadata
- production needs stable HTTPS, streaming responses on `/mcp`, dependable TLS, logs, and metrics
- cold starts and proxy buffering are real product risks because they can break streaming behavior

The pack names Alpic and Vercel as fast-start paths, then containers, serverless platforms, and Kubernetes as broader hosting options.

### 5. Security and privacy are part of the tool surface

The security guidance is straightforward and production-oriented:

- request least privilege only
- make write access and account linking legible to the user
- assume prompt injection and validate everything server-side
- redact PII in logs
- require confirmation for irreversible actions
- enforce OAuth scopes on every tool call

It also notes that widgets live in a CSP-restricted iframe, so any network or iframe dependency must be designed with resource CSP metadata in mind.

### 6. Troubleshooting should isolate the failing layer

The troubleshooting section repeatedly comes back to one habit: decide whether the failure is in the server, the component, or the ChatGPT client.

Key checks called out in the pack:

- no tools listed: confirm the server is running and the connector points to `/mcp`
- no component rendering: verify `_meta.ui.resourceUri` and the HTML resource profile
- widget state not persisting: verify `window.openai.setWidgetState` and mount-time rehydration
- wrong tool selected: revisit metadata and the negative prompt set
- 401 loops: return `WWW-Authenticate` so auth can restart cleanly
- streaming failures: inspect load balancer or CDN buffering behavior

## Practical Sequence

If Martin wants to turn this note into a real first build, the shortest sane path is:

1. Pick one P0 use case only.
2. Write at least five direct prompts, five indirect prompts, and a negative set for that one use case.
3. Draft one read-only tool first, with strict parameters and a `Use this when...` description.
4. Build only the minimum component needed to answer the prompt inline.
5. Test the golden prompt set in ChatGPT developer mode and log what fired, what arguments were passed, and what failed.
6. Only after precision is good, add write actions, broader metadata, and production hosting.

## Chosen P0 Use Case (2026-04-23)

### P0 choice

Start with a **read-only EMERAULD vault briefing app**: the user asks about a project, note, timeline event, or system component already documented in the vault, and the app returns a short retrieval-backed answer plus the most relevant canonical notes.

This is the best first Apps SDK use case because it matches the current stack and the note's own sequencing rule:

- it is read-only
- it uses an existing dataset (`wiki/`, tracker notes, timeline notes, vector index)
- it can answer real questions Martin already asks
- it avoids premature write flows, auth complexity, and confirmation logic

### Use-case sentence

When Martin asks ChatGPT about a project, system, note, or date already documented in EMERAULD, the app should retrieve the most relevant vault notes and return a concise briefing with links to the canonical artifacts.

### Minimum lovable output

- short answer in plain language
- top 3 relevant notes with titles and paths
- one canonical note clearly marked when confidence is high
- optional metadata bar: note type, updated date, status, and related links

### Golden Prompt Set

#### Direct prompts

1. "Search EMERAULD for the current status of ComplyScan and show me the canonical note."
2. "Use the EMERAULD vault to brief me on Trismégiste and link the main note."
3. "Query my EMERAULD notes for the PHAROS-EMERAULD timeline around March 2026."
4. "Look in EMERAULD and tell me which note explains the AI infrastructure stack."
5. "Show me the relevant EMERAULD notes for the Master Project Tracker and active software projects."

#### Indirect prompts

1. "What am I actively working on right now across software and writing?"
2. "When did the company formation happen relative to the invention disclosure?"
3. "I need the note that best explains my personal AI assistant setup."
4. "What should I read first to understand the history of this whole PHAROS project?"
5. "Which note should I open first for the compliance SaaS idea I picked?"

#### Negative prompts

- "What is the weather in Montreal today?"
- "Write a new 1500-word essay on AI governance."
- "Deploy my MCP server to production."
- "Find the latest OpenAI Apps SDK pricing."
- "Summarize this brand-new document I just uploaded."

### Why this P0 wins over ComplyScan-first

[[ComplyScan — Bilingual Law 25 - AI Act Compliance SaaS]] is still a strong later Apps SDK target, but it is not the best first connector. A first release should prove discovery and retrieval before adding regulation-specific questionnaires, reports, exports, and higher-stakes write or generation flows. EMERAULD vault briefing is the narrower, safer, and more testable P0.

## Working Checklist

- Use-case sentence written
- Golden prompt set drafted
- Tool contract bounded
- Metadata tested in developer mode
- Streaming `/mcp` endpoint reachable
- Logs and metrics visible
- Security review completed
- Troubleshooting log template prepared

## Open Questions

- Which concrete product or dataset should be the first Apps SDK connector target?
- Does the first version need write access, or should it stay read-only through the first dogfood cycle?
- Should the first hosted version live on Cloudflare, Vercel, or another surface already in Martin's stack?

## Sources

- `raw sources/2026-04-23_chatgpt-apps-sdk-docs-pack.md`

## Related

- [[AI Infrastructure Stack]]
- [[CLI-Anything — Agent Harness for Tool Integration]]
- [[InfraFabric MCP Stack — Remote Bundles]]
- [[Plugin Recommendations]]
- [[ACTOR Framework Worksheet]]
- [[AI Agent Operations and Governance Manager]]
- [[README]]
- [[THREAT_MODEL]]
- [[MockPool]]
- [[writing-tests]]
- [[2026-05-05_how-td-helps-advance-ai-innovation]]
- [[reference_seven_pillars_stack]]
- [[2026 - audit_or_assessment [3]]]
- [[2026 - policy_or_guidance.pdf - 2026 - policy_or_guidance.pdf.pdf - 2026 - policy_or_guidance.pdf -]]
- [[PHAROS LinkedIn Schedule — April 2026]]
- [[LINKEDIN-SCHEDULE-NOW]]
