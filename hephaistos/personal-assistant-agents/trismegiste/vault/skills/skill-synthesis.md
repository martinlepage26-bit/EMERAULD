---
type: skill-spec
title: 'Skill: Synthesis'
tags:
- skill
- agents
- trismegiste
- skill-spec
- personal-assistant-agents
- hephaistos
- prompted
- yyyy
- title
- synthesized
- facts
status: active
domain: governance
created: '2026-06-21'
updated: '2026-06-26'
vault_area: hephaistos
canonical_path: hephaistos/personal-assistant-agents/trismegiste/vault/skills/skill-synthesis.md
backlink_count: 1
backlinks:
- '[[wiki/Orphan Index — Vault-Level Graph Repair 2026-05-06]]'
name: synthesis
trigger: Use this skill when asked to process, convert, or synthesize a raw note into wiki format.
---

# Skill: Synthesis

## When to use
- User says "process this note", "convert to wiki", "synthesize"
- A raw/ note has been identified as useful and ready to promote

## Steps

1. Read the raw note fully
2. Identify the core question or context that prompted this note
3. Extract the key facts, decisions, or insights
4. Rewrite as a wiki note with this structure:

```markdown
---
tags: [relevant, tags]
updated: YYYY-MM-DD
source: raw/YYYY-MM-DD-original-title.md
---

# [Clear Title]

## Context
[The situation or question that prompted this note]

## Key Points
[Bullet list of main facts/decisions]

## Details
[Full synthesized content in your own words]

## Backlinks
- [[hub-[related-topic]]]
- [[other-related-note]]
```

5. Save to `wiki/[title].md`
6. Add a backlink entry in the relevant hub note
7. Move the original raw note to `archive/`

## Output
Confirm: "Synthesized → wiki/[title].md. Linked from [[hub-X]]."
