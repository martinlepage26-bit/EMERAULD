---
type: note
title: Canonical Paper Corpus Structure
tags:
- note
- paper
- tmp
- drive-audit-2026-04-18
- gdoc
- manuscript
- archive
- anxiety
status: temporary
created: '2026-04-18'
updated: '2026-06-26'
vault_area: tmp
canonical_path: tmp/drive-audit-2026-04-18/corpus_structure.md
backlink_count: 2
backlinks:
- '[[wiki/APEX Papers — Research Archive Map]]'
- '[[Areas/Writing/Research and Papers MOC]]'
---

# Canonical Paper Corpus Structure
Generated: 2026-04-18

## Design principles

1. One folder per paper, named with a lowercase-hyphenated slug.
2. All companion artifacts live inside that folder — no companions scattered at the Drive root.
3. Old versions and working drafts go into `_archive\` inside the paper folder. Nothing deleted.
4. File role is encoded in the filename, not in the folder name.
5. Format (`.docx`, `.gdoc`, `.pdf`) is kept as-is; the role suffix disambiguates.
6. Status (in-progress, submitted, rejected) is tracked in `_status.md` per paper, not in folder hierarchy.

---

## Canonical root

```
G:\Mon disque\Papers\
```

Two domain subfolders:
```
G:\Mon disque\Papers\ai-governance\
G:\Mon disque\Papers\media-studies\
```

---

## Filename convention

```
[slug]_[role].[ext]
```

Roles:
| Role token | What goes there |
|---|---|
| `manuscript` | The working or submitted full draft |
| `cover-letter` | Journal cover letter |
| `abstract` | Abstract or proposal (standalone) |
| `references` | Bibliography / references file |
| `reviewer-response` | Response to reviewers |
| `title-page` | Anonymized title page |
| `supplementary` | Appendices, workflow schematics, figures |
| `notes` | Working notes, alignment memos, submission guidelines |

If multiple formats of the same role exist (e.g., `.docx` and `.pdf`), keep both with the same role suffix.

---

## Canonical folder map

### ai-governance papers

```
Papers\ai-governance\
  ai-anxiety\                       AI Society submission
    ai-anxiety_manuscript.docx
    ai-anxiety_manuscript.md
    ai-anxiety_cover-letter.pdf
    ai-anxiety_reviewer-response.docx
    ai-anxiety_title-page.docx
    ai-anxiety_supplementary.docx
    _status.md
    _archive\

  governance-by-denial\             JPP submission
    governance-by-denial_manuscript.docx
    governance-by-denial_notes.md   (submission alignment note)
    _status.md
    _archive\

  recursive-det-gov\                Recursive Deterministic AI Governance
    recursive-det-gov_manuscript.docx
    recursive-det-gov_manuscript.md
    _status.md
    _archive\

  recursive-continuity\             Recursive Continuity Without Memory
    recursive-continuity_manuscript.docx
    _status.md
    _archive\

  first-method-paper\               Very Long / Long / Medium Narrative
    first-method-paper_very-long-narrative.gdoc
    first-method-paper_long-narrative.gdoc
    first-method-paper_medium-narrative.gdoc
    first-method-paper_very-long-narrative.docx
    first-method-paper_very-long-narrative.pdf
    _status.md
    _archive\

  anthro-pharos\
    anthro-pharos_manuscript.docx
    anthro-pharos_manuscript.pdf
    _status.md
    _archive\

  ai-governance-whos-the-boob\
    ai-governance-whos-the-boob_manuscript.md
    ai-governance-whos-the-boob_manuscript.docx
    _status.md
    _archive\

  pharos-invention-disclosure\      Patent disclosure
    pharos-invention-disclosure_v12.docx
    pharos-invention-disclosure_v12.pdf
    pharos-invention-disclosure_patent-counsel.docx
    pharos-invention-disclosure_patent-counsel.pdf
    _status.md
    _archive\                       v5, v6, v7, v8, v9, v10, v11 go here
```

### media-studies papers

```
Papers\media-studies\
  buffy\
    buffy_manuscript.docx           BUFFY_FINAL_with_selected_bibliography
    _status.md
    _archive\                       revised_with_bibliography, (1) variant

  compress-without-opacity\
    compress-without-opacity_manuscript.docx   CompressOpaq-TRUE.docx
    _status.md
    _archive\                       all BACKUP, CITED, drafts, .gdoc, .odt variants

  sealed-card-protocol\
    sealed-card-protocol_manuscript.docx   The Sealed Card Protocol - TRUE (1).docx
    sealed-card-protocol_manuscript.pdf
    sealed-card-protocol_final.pdf         Sealed_Card_Protocol_FINAL (1).pdf
    _status.md
    _archive\                       Rewrite_9000_words variants, MERGED, SAKURA layers

  authority-without-ethics\
    authority-without-ethics_manuscript.gdoc   Authority Without Ethics_REVISED.gdoc
    _status.md
    _archive\                       original non-REVISED .gdoc

  recurso\
    recurso_manuscript.docx
    recurso_manuscript.gdoc
    _status.md
    _archive\

  social-compass-agatha\
    social-compass-agatha_manuscript.gdoc
    _status.md
    _archive\

  this-paper-may-not-exist\
    this-paper-may-not-exist_manuscript.gdoc
    this-paper-may-not-exist_manuscript.docx
    _status.md
    _archive\
```

---

## What does NOT go in Papers\

| Item | Stays where |
|---|---|
| `AI\Responsible AI Governance Pack.gdoc` | `AI\` — it's a service deliverable, not a paper |
| `AI\Responsible AI Services Menu.gdoc` | `AI\` — same |
| `AI Ethics Audit Report – Ex Libris AI.gdoc` | `AI\` — client deliverable |
| `codex-skills\*` | stays in `codex-skills\` |
| `PHAROS_Invention_Disclosure_v12.pdf` on Desktop | local copy, leave in place |
| `Shared with ChatGPT\Papers\` | no action — leave in place to avoid breaking ChatGPT link |

---

## _status.md template

```md
# [Paper slug] — Status

## Current status
[draft | in-review | submitted | revision-requested | accepted | rejected | published]

## Journal / venue
[target journal or conference]

## Submission date

## Last action

## Missing companion artifacts
[ ] abstract
[ ] references
[ ] cover-letter
[ ] reviewer-response

## Notes
```

---

## Migration approach

Migration is implemented in `migrate_corpus.ps1`.
It moves files (not copies) so Drive quota is not doubled.
Files moved to `_archive\` are not deleted — they are relocated inside the paper folder.
Run with `-DryRun` first to verify paths before executing.

## Related

- [[Research and Papers MOC]]
- [[APEX Papers — Research Archive Map]]
