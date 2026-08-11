---
name: synthesis
trigger: "Use this skill when asked to process, convert, or synthesize a raw note into wiki format."
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
