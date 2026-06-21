# How to Write AI Skill Guides That Replace Prompt Engineering

**Platform:** Hashnode  
**Iteration:** 34 — Cycle 8  
**Angle:** Skill guide pattern — named markdown instruction files the agent executes by name  
**Tags:** obsidian, ai, developer-tools, knowledge-management, claudeai  
**Status:** READY TO POST

**Instructions:** Log into hashnode.com → Write → paste content below → tags: obsidian, ai, developer-tools, knowledge-management, claudeai → publish to your blog.

---

Prompt engineering has a maintenance problem.

You write a careful prompt for a task you do repeatedly — synthesizing research notes, auditing link hygiene, archiving stale material. It works. You save it in a prompts folder. Three months later you can't find it, can't remember whether you updated it, and when you do paste it in, the model behaves differently because you're in a different context.

The root problem: prompts are stateless. They live outside your project, outside your knowledge system, and outside the agent's reach. Every time you need the behavior, you hunt for the prompt, paste it in, and hope the context is right.

There's a better pattern. I've been using it for six months and it's made my AI workflows substantially more repeatable. I call them skill guides.

## What a skill guide is

A skill guide is a named markdown file that lives in your vault and contains explicit, step-by-step instructions the agent follows when you invoke it by name.

Not a prompt. Not a system instruction. A procedure — written for the agent the same way you'd write a runbook for a human teammate.

The key properties:

1. **Named** — you invoke it by name in conversation ("Run Ilyris on this note" or "Execute the synthesis guide on this source material")
2. **Explicit** — every step is spelled out, including what to check, what to produce, and what to do if something is missing
3. **Linked** — it lives in your vault, connected to the note types and structures it operates on
4. **Versioned** — it's a file you can update, diff, and maintain like any other note

## Three skill guides worth having

### 1. The synthesis guide

The most common task in a knowledge vault: you have raw source material and need to produce a synthesized wiki note with proper linking.

Without a skill guide, this means re-explaining the synthesis criteria every time: what makes a good note, what level of detail to include, what to link, how to format.

With a skill guide:

```markdown
# Skill: Synthesize

## Purpose
Convert raw source material into a durable wiki note with graph connections.

## When to invoke
When a raw/ capture needs to become a wiki/ note.
Invoke: "Run Synthesize on [file]" or "Synthesize this source."

## Steps

1. Read the source material completely before writing anything.

2. Identify the core claim or finding — the one thing this source
   establishes that is worth preserving.

3. Write a wiki note with this structure:
   - ## Summary — 2–3 sentences. Must include at least one [[link]].
   - ## Context — how this connects to current projects or prior notes.
     Must include inline [[links]] to related projects, concepts, or people.
   - ## Details — main content. All entities (projects, concepts, tools,
     decisions, people) must be linked inline if they exist in the vault.
   - ## Source — citation or reference to the raw/ file.

4. Before saving: verify that the note has at least 2 inline [[links]]
   in the body (not just in ## Source or a trailing Related section).
   If fewer than 2 links are present, search the vault for related notes
   and add them.

5. Identify which MOC, hub, or index page should link to this note.
   Add the note to that page before finishing.

6. Report: note title, number of links added, which hub/MOC was updated.

## What not to do
- Do not summarize the source title — synthesize the content.
- Do not create a new note if a closely related one already exists; update instead.
- Do not leave a note with zero links even if you can't find strong connections —
  create a stub link to the most relevant parent topic.
```

This is a repeatable procedure. You invoke it, it runs, you get a correctly structured, linked wiki note. No re-explaining what "good synthesis" means.

### 2. The link audit guide

Over time, vaults accumulate orphan notes — notes that got created but never wired into the graph. This is a maintenance task worth running periodically.

```markdown
# Skill: LinkAudit

## Purpose
Find and fix orphan notes and broken link patterns in the wiki/.

## When to invoke
Monthly maintenance, or before rebuilding the vector index.
Invoke: "Run LinkAudit" or "Audit link hygiene."

## Steps

1. Scan all files in wiki/. For each file, check:
   - Does it have at least 2 inline [[links]] in the body?
   - Is it linked FROM at least one other note (has backlinks)?
   - Is it listed on any MOC, hub, or index page?

2. Categorize findings:
   - ORPHAN: zero backlinks and not listed on any hub/MOC
   - LOW-LINK: fewer than 2 inline links in the body
   - DISCONNECTED: not reachable from the main entry point (CLAUDE.md)
     in 4 hops or fewer

3. For each ORPHAN note:
   - Search for 2–3 notes with related content.
   - Add inline links from those notes to the orphan.
   - Add the orphan to the most relevant hub or MOC.

4. For each LOW-LINK note:
   - Read the note content.
   - Identify 2+ entities (projects, concepts, people, decisions) that
     have wiki notes.
   - Add inline links in the body at the point where the connection is made.

5. Report: count of orphans fixed, links added, hubs updated.
   Flag any notes that couldn't be connected (genuinely isolated content).

## What not to do
- Do not add links just to meet the count — links must be meaningful.
- Do not delete orphan notes; fix their connections instead.
- Do not add links only in a trailing "Related" section —
  they must appear inline in the body.
```

### 3. The archive guide

As projects close and research becomes stale, notes accumulate that are no longer active. Archiving keeps the graph clean without losing history.

```markdown
# Skill: Archive

## Purpose
Identify and archive stale notes without breaking graph connections.

## When to invoke
Quarterly, or when a project closes.
Invoke: "Run Archive on [project name]" or "Archive closed project X."

## Steps

1. Identify candidates:
   - Notes with status: closed, complete, or superseded in frontmatter
   - Notes not linked or referenced in the past 90 days
   - Notes for projects explicitly marked complete

2. For each candidate, before archiving:
   - Check how many active notes link TO this note.
   - If 3+ active notes link to it, do not archive — it is still
     structurally active even if content is old.
   - If the note is a hub or MOC for an active area, do not archive.

3. Archive process:
   - Move file to archive/[year]/ (create the folder if needed).
   - Update frontmatter: status: archived, archived: [date].
   - In the original location, leave a redirect stub:
     "# [Title] — Archived
      This note has been archived. See [[archive/2026/Title]]."
   - Update the hub or MOC that linked to it: replace the link with
     the archive path.

4. Report: notes archived, stubs created, links updated.

## What not to do
- Do not delete — archive only.
- Do not archive notes that are still structurally connected to active work.
- Do not break backlinks — always leave a stub.
```

## Why this works better than prompt engineering

**Prompts are invocation-time.** You write a prompt, paste it in at the moment you need it. If the context is different, the behavior drifts.

**Skill guides are system-time.** The guide lives in the vault, linked to the note types it operates on. The agent can read it before invoking it. The instructions are stable across sessions.

**Prompts describe intent.** "Write a good synthesis of this source" is an instruction that depends entirely on the agent's interpretation of "good synthesis."

**Skill guides describe procedure.** Every step is explicit. The agent doesn't interpret — it executes. The result is consistent because the process is specified.

**Prompts are personal.** They live in your clipboard, your notes app, your prompts folder. Another team member doesn't have them.

**Skill guides are shared.** They live in the vault. Anyone with access to the vault has access to the procedures. Onboarding means reading the skill guides.

## How to write your own

The structure that works:

```markdown
# Skill: [Name]

## Purpose
One sentence: what this skill does and why it exists.

## When to invoke
The condition that triggers use, and the exact invocation phrase.

## Steps
Numbered. Explicit. Each step produces a concrete output or decision.
Include "if X, then Y" branches for the cases that actually come up.

## What not to do
The failure modes you've actually hit. These are as important as the steps.
```

A few principles worth following:

- **Write for execution, not inspiration.** The guide is a runbook. It should read like a checklist, not an explanation.
- **Include the edge cases you've actually hit.** If you've seen the agent do something wrong on this task, the guide should have a "what not to do" entry that prevents it.
- **Link the skill guide to the note types it operates on.** If the synthesis skill creates wiki notes, the skill guide should link to `[[Wiki Note Template]]`. The agent can cross-reference.
- **Keep each skill guide focused on one task.** A guide that does six things doesn't run reliably. Six guides that each do one thing do.

## Where skill guides fit in the vault

```
wiki/
  skill-guides/
    synthesize.md
    link-audit.md
    archive.md
    [your custom guides]
  templates/
    wiki-note.md
    hub-note.md
    decision-log.md
```

The `CLAUDE.md` entry file lists the available skill guides so the agent knows what procedures exist before you invoke them:

```markdown
## Available Skills
- Synthesize — convert raw/ captures to wiki/ notes (see [[Skill — Synthesize]])
- LinkAudit — find and fix orphan notes (see [[Skill — LinkAudit]])
- Archive — retire stale notes without breaking graph (see [[Skill — Archive]])
```

## The shift this creates

You stop re-explaining how to do recurring tasks. Instead you write the procedure once, maintain it as it evolves, and invoke it by name.

The agent's behavior becomes consistent because it's following an explicit procedure, not interpreting a one-off prompt. And because the skill guides live in your vault, they're part of your knowledge system — versioned, linked, and available across every session.

---

The vault template that ships with the synthesis, link audit, and archive skill guides — plus the hub templates, decision-log format, session-state protocol, and optional local runtime — is $49.

→ https://pharosml.gumroad.com/l/kvbhdo

$299 for a guided setup. $2,500 for teams.

The skill guides are the part most people don't realize they need until they've been running a vault for three months and discovered how much time goes into re-explaining routine tasks.

## Related

- [[manual]]
- [[Building Your First AI Agent with OpenAI_____]]
- [[Railway (one-click)]]
- [[Responses API Fundamentals]]
- [[README]]
- [[archive_guide]]
- [[link_guide]]
- [[synthesis_prompt]]
- [[community-posts]]
- [[devto-iter13-decision-log-deepdive]]
- [[devto-iter17-prompting-problem]]
- [[devto-iter21-roi-calculation]]
- [[devto-iter25-hallucination-fix]]
- [[devto-iter29-context-window-not-memory]]
- [[devto-iter33-architecture-guide]]
- [[devto-iter37-three-notes]]
- [[devto-iter41-code-review]]
- [[devto-iter49-claudemd-fails]]
- [[devto-iter9-comparison]]
- [[hashnode-iter14-scaling]]
- [[hashnode-iter18-no-rag]]
- [[hashnode-iter22-graph-vs-folders]]
- [[hashnode-iter26-synthesis-habit]]
- [[hashnode-iter30-hub-note-pattern]]
- [[hashnode-iter38-writing-for-ai]]
- [[hashnode-iter42-open-questions]]
- [[hashnode-iter46-active-constraints]]
- [[hashnode-iter6-feature-first]]
- [[medium-producthunt]]
- [[Porting-Buffer]]
- [[CHANGELOG]]
- [[SECURITY]]
- [[24 Profitable Digital Products to Sell in 2026 (Start Selling Today)]]
- [[2003 - Prepublication Copy of]]
- [[2021 - report_1]]
- [[2025 - PowerPoint Presentation [2]]]
- [[Microsoft Word - Turning your Dissertation into a Book-open sans]]
- [[2025 - PowerPoint Presentation_1]]
