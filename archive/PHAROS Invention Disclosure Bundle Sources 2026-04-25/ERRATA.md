---
type: archive-record
title: PHAROS Invention Disclosure V12 — Errata
aliases:
- archive/PHAROS Invention Disclosure Bundle Sources 2026-04-25/ERRATA
tags:
- archive
- pharos
- archive-record
- pharos-invention-disclosure-bundle-sources-2026-04-25
- passes
- counsel
- redesign
- inventor
- bundle
- color-green
status: archived
created: '2026-04-25'
updated: '2026-06-26'
vault_area: archive
canonical_path: archive/PHAROS Invention Disclosure Bundle Sources 2026-04-25/ERRATA.md
backlink_count: 1
backlinks:
- '[[wiki/Research and Papers MOC]]'
---

# PHAROS Invention Disclosure V12 — Errata

See also [[Research and Papers MOC]].
**Bundle:** V12 Evidence — 2026-04-21
**Errata prepared:** 2026-04-25

Internal inconsistencies in the V12 disclosure body that should be resolved by inventor sign-off before any filing draft is finalized. These are noted, not silently corrected — modifying signed disclosure language is an inventor decision.

---

## E1 — §6 Accompanying Materials: pass-count mismatch

**Location:** V12 §6 (anchor `00_PHAROS_Invention_Disclosure_v12.pdf`, page 14–15).

**As written:**
> *"PHAROS Recursive Redesign — Execution Output Passes 1–3 (Claude + GPT) — Full transcript of the **five-pass** recursive self-audit."*
> *"PHAROS Recursive Redesign — Execution Output Passes 1–2 (Claude) — Independent parallel redesign run for cross-model verification."*

**Internal contradiction:** the same sentence describes "Passes 1–3" as a "five-pass recursive self-audit." The numeric range and the word "five-pass" disagree.

**Bundle ground truth:**
- `03_PHAROS_Recursive_Redesign_Passes_1-5_Claude+GPT.txt`
- `04_PHAROS_Recursive_Redesign_Passes_1-5_Claude.txt`
- `REV_PHAROS_Recursive_Redesign_Passes_1-5_Claude+GPT.docx`
- `REV_PHAROS_Recursive_Redesign_Passes_1-5_Claude.docx`

All four transcript files in the bundle cover **passes 1 through 5**.

**Recommended resolution (counsel + inventor):** correct the V12 §6 list entries to "Passes 1–5 (Claude + GPT)" and "Passes 1–5 (Claude)" so the §6 list, the body description ("five-pass recursive self-audit"), and the bundle filenames all agree. This is a labeling correction; the substantive evidence is unchanged.

**Status in this bundle:** flagged, not edited. The disclosure document is unchanged from the 2026-04-21 V12 anchor.

---

## E2 — Reference to a "v6" protocol version inside a v12-numbered disclosure

**Location:** V12 §3 ("PHAROS Recursive AI Governance Protocol v6.0 on 28 March 2026") and §7 ("inherent limitations of the current protocol version (v6.0)").

**Observation:** the file revision is v12 but the protocol version inside the document is v6.0. This is intentional (file = drafting iteration count; protocol version = PHAROS architecture version), but readers commonly confuse the two.

**Recommended resolution (counsel + inventor):** add a one-sentence footnote to the title page or §1 distinguishing the two versioning schemes. No content change required.

**Status in this bundle:** flagged, not edited.

---

## E3 — Möbius Protocol filesystem-date attestation

**Location:** V12 §6 last bullet — *"Möbius Protocol (21 March 2025) — First operational articulation of the method, serving as the priority anchor for the conception date claim."*

**Observation:** no on-disk artifact dated 21 March 2025 survives. The five Möbius source files included in the bundle (item 08) are the fullest surviving descriptions but post-date the conception event. NTFS / WSL mount-time metadata is not a reliable attestation of authorship date. Already noted in `MANIFEST.md`.

**Recommended resolution (counsel + inventor):** if priority evidence for the 21 March 2025 conception claim is needed by counsel, retrieve the original artifact from external sources (Google Drive revision log, email attachments, git history of `martin-lepage-site` or related repos, calendar entries, conference talk recordings).

**Status in this bundle:** flagged, not editable from local sources alone. Operator action required if priority attestation is needed at filing.

---

## What this errata file is not

- Not a substantive critique of the disclosure's claims.
- Not a redrafting recommendation for the body of the disclosure.
- Not an attempt to silently smooth contradictions before counsel sees them.

These three items are the things in the V12 anchor that, if left unaddressed, will cost time during counsel review. Surfacing them up front keeps the review tight.
