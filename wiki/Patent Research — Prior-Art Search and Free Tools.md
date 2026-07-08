---
type: wiki
title: Patent Research — Prior-Art Search and Free Tools
aliases:
- Patent search workflow
- Prior art search
- AI governance patent search
- Free patent prior-art tools
- wiki/Patent Research — Prior-Art Search and Free Tools
tags:
- patents
- prior-art
- search
- research
- ai-governance
- pharos
- wiki
- patent-research-prior-art-search-and-free-tools-md
- patent
- espacenet
- patentscope
- color-blue
status: active
created: '2026-05-08'
updated: '2026-06-26'
vault_area: wiki
canonical_path: wiki/Patent Research — Prior-Art Search and Free Tools.md
backlink_count: 6
backlinks:
- '[[Areas/Writing/Academic Paper Pipeline]]'
- '[[Areas/PHAROS/PHAROS Invention Disclosure]]'
- '[[Areas/PHAROS/PHAROS Method — Technical Reference]]'
- '[[Areas/PHAROS/PHAROS Scholarly Publication Track]]'
- '[[Areas/Writing/Research and Papers MOC]]'
- '[[memory/clients/helix-prospects/HELIX-hermes-assisted-prospect-extension-2026-05-06/2026-05-05_aida-caseware]]'
---

# Patent Research — Prior-Art Search and Free Tools

## Summary

Patent research checks whether an invention is new, non-obvious, and useful, and maps the patent landscape before filing or commercialization. It helps avoid infringement, spot innovation gaps, and decide whether a provisional or full application is worth pursuing.

For PHAROS/IP work, read this beside [[PHAROS Invention Disclosure]], [[Global Publication Search — PHAROS Method and Variants]], and [[PHAROS Method — Technical Reference]].

## Source Context

Source: current operator brief on patent research, plus [[00_Inbox/Raw/2026-05-06 — Patent agent email — provisional application contract + notes]] as the practical follow-on context.

## What Patent Researchers Look For

- Published applications and granted patents
- Claim language, because claims define protected scope
- Citations and patent families
- Inventors, assignees, and filing dates
- Close prior art and possible blocking claims
- Where the technology is moving and who is active in the field

## Typical Process

1. Define the invention clearly: the problem it solves, what makes it different, and likely competitors or assignees.
2. Run a preliminary prior-art search in Google Patents, Espacenet, WIPO PATENTSCOPE, or the USPTO Patent Public Search.
3. Refine the search with keywords, CPC/IPC classification codes, inventor or assignee names, publication numbers, and citation chasing.
4. Read the closest patents closely, especially the claims.
5. Assess patentability and risk, including novelty, non-obviousness, usefulness, and freedom-to-operate concerns.
6. Decide whether to file, often first with a provisional or invention disclosure in some workflows, then prepare the full application.

## Best Free Stack

| Need | Best free tool | Why |
|---|---|---|
| Quick first pass | Google Patents | Fast full-text search, claim reading, and citation lookup |
| Deep family work | Espacenet | Strong family, classification, and translation support |
| International or PCT search | WIPO PATENTSCOPE | Best for PCT filings and multilingual search |
| U.S. verification | USPTO Patent Public Search | Official U.S. prior-art and application record |
| Patents plus papers | Lens.org | Combines patent and scholarly literature search |

A practical stack is Google Patents for broad discovery, Espacenet for classification refinement, and PATENTSCOPE or USPTO for jurisdiction-specific verification. Lens.org is useful when broader prior-art coverage needs literature alongside patents.

## Search Tactics

- Use keywords, inventor names, assignee names, and classification codes together.
- Review cited patents and patent families, because they often lead to the closest earlier documents.
- Build synonym sets before searching, because the same idea is often described with different terms.
- Search the same concept in at least two databases, then compare overlaps and cited references.

### Copy-Paste Query Patterns

- `"invention keyword" AND "synonym"`
- `"problem phrase" patent claims`
- `inventor name OR assignee name`
- `site:patents.google.com "technical term"`
- `"invention keyword" CPC:H01L`

## Classification Strategy

If you do not know the right CPC or IPC code, use a class-suggestion helper if available, then confirm the symbol definitions before relying on them.

A good pattern is:

1. Start broad with keywords and find one or two close patent documents.
2. Extract the CPC or IPC codes from those results.
3. Browse the class hierarchy and adjacent sibling classes.
4. Combine one specific code and one broad code to capture both the core technology and nearby variants.
5. Re-run the search with classification symbols plus keywords to improve recall and precision.

## AI Governance and Deterministic Workflows

AI inventions are often described with words like training, inference, classification, monitoring, explainability, bias detection, fairness, audit logging, or human oversight. For governance-oriented inventions, the patent literature may describe the control mechanism rather than the governance label.

For deterministic workflow and agent systems, search for:

- deterministic workflow
- workflow orchestration
- process automation
- business process management
- repeatable execution
- state locking
- audit trail
- privilege-bounded execution
- fixed loops or bounded recursion
- human-in-the-loop review
- risk management and compliance guardrails

Useful combined patterns:

- `("AI agent" OR "LLM agent") AND ("deterministic control" OR "repeatable result")`
- `("human oversight" OR "human-in-the-loop") AND ("AI decision" OR "recommendation")`
- `("audit log" OR traceability OR monitoring) AND ("AI model" OR "AI system")`
- `("governance-as-a-service" OR "AI governance") AND (risk OR compliance OR audit)`

For PHAROS-style work, the practical search lens is usually workflow + determinism + governance/control rather than the phrase "recursive determinism" itself. Governance-as-a-service ideas often surface as risk management, monitoring, compliance, guardrails, or policy engines.

If you want a quick first pass, an AI-assisted prior-art tool such as PQAI can surface relevant results from a short description, but it should be followed by manual checking in Google Patents, Espacenet, PATENTSCOPE, or the USPTO tool.

## Simple Search Sequence

1. Write a 1-2 sentence description of the invention.
2. List synonyms and related technical terms.
3. Search in Google Patents with keywords and claim terms.
4. Repeat in Espacenet using classification codes.
5. Verify the closest hits in PATENTSCOPE or USPTO Patent Public Search.
6. Read claims and cited references for the top results.

## Search Worksheet

| Field | What to write |
|---|---|
| Invention name | Short descriptive title |
| Core concept | What the invention does |
| Key novelty | What seems different |
| Keywords | 5-15 terms and synonyms |
| Classes | IPC/CPC codes |
| Databases | Google Patents, Espacenet, PATENTSCOPE, USPTO |
| Closest prior art | Patent numbers and notes |
| Risk | Low, medium, or high |
| Next step | Revise search, draft filing, or do FTO review |

## Why It Matters

Good patent research can save time and money by preventing duplicate work, reducing infringement risk, and improving the quality of a future application. In academic and commercial settings, it can also surface licensing opportunities and possible partners.

## Related

- [[Research and Papers MOC]]
- [[PHAROS Invention Disclosure]]
- [[Global Publication Search — PHAROS Method and Variants]]
- [[PHAROS Method — Technical Reference]]
- [[Academic Paper Pipeline]]
- [[PHAROS Scholarly Publication Track]]
- [[AI Governance Manifesto — Upstream Institutional Practice]]
- [[Recursive Deterministic AI Governance — Method and Paper]]
- [[2026-05-05_aida-caseware]]
- [[Using pgvector, LLMs and LangChain with...le Cloud databases _ Google Cloud Blog]]
