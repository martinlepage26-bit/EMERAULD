---
type: raw-source
aliases: [orphan-raw-2026-05-06-003]
graph_repair: 2026-05-06
---

# DocSort — Setup & Reference

## Quick start (Windows)

```
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt

# GUI (double-click or):
python docsort.py

# CLI:
python docsort.py "C:\Docs\Source" "C:\Docs\Sorted" --owner "Martin Lepage" --mode copy
```

For .doc files, also install pywin32 so DocSort can call Word via COM:
```
pip install pywin32
```
If pywin32 is absent, DocSort tries antiword (external binary) and then skips gracefully.

## Configuration (top of docsort.py)

| Variable               | Default          | Effect                                      |
|------------------------|------------------|---------------------------------------------|
| OWNER_NAME             | "Martin Lepage"  | Name searched in metadata, headers, body    |
| MIN_OWNER_CONFIDENCE   | 0.65             | Below this → Review/Low_Confidence          |
| MIN_CATEGORY_CONFIDENCE| 0.50             | Below this → Review/Uncategorized           |
| DRY_RUN                | True             | No files moved/copied until you set False   |
| MOVE_FILES             | False            | Requires DRY_RUN=False to take effect       |
| RECURSE                | True             | Scan sub-folders                            |

## Category-discovery method

DocSort runs in three sequential passes.

**Pass 1 — Text extraction.**
Every supported file is read. Text, filename, and (where available) document metadata
are extracted and stored in memory. Nothing is written yet.

**Pass 2 — Category inventory.**
DocSort scans every extracted text for self-labelling language: phrases that the
documents themselves use to describe what they are ("journal article", "rapport",
"thesis", "policy brief", "contrat", etc.). A curated list of ~30 patterns covers
common academic, administrative, and professional document types in both English and
French. Each match is normalized to a canonical slug (e.g., "mémoire" → "thesis",
"courriel" → "correspondence"). The result is a frequency table of labels actually
present in the corpus. No label is invented; no semantic clustering is performed.

**Pass 3 — Assignment and routing.**
Each file is checked against the discovered inventory. If a label from the inventory
appears in the file's text or filename, that label is assigned as the category.
Confidence is proportional to the number of label occurrences and their location
(filename > header > body). Files with no corpus-grounded label go to
Review/Uncategorized. Files with ambiguous ownership go to Review/Low_Confidence.

## Output folder structure

```
Sorted/
├── Mine/
│   ├── journal_article/
│   ├── thesis/
│   ├── report/
│   └── correspondence/
├── Not_Mine/
│   ├── report/
│   └── policy/
├── Review/
│   ├── Low_Confidence/
│   ├── Uncategorized/
│   └── Unreadable/
├── manifest.csv
├── manifest.json
├── category_inventory.json
└── processing_log.txt
```

Only categories actually discovered in the corpus appear as sub-folders.

## Reports

**manifest.csv / manifest.json** — one row per file:
- original_path, destination_path
- readable, extraction_method
- owner_status, owner_confidence, owner_evidence
- category, category_confidence, category_evidence
- error_reason, action_taken

**category_inventory.json** — every label found in the corpus with its frequency count.

**processing_log.txt** — timestamped log of every decision, warning, and error.

## Known limitations

1. **Image-only PDFs** — PDFs without embedded text are flagged and routed to
   Review/Unreadable. OCR is not performed.

2. **Legacy .doc files** — Require either pywin32 (Windows + Word installed) or
   the antiword binary. Without both, .doc files are skipped and logged.

3. **Encrypted or password-protected files** — Skipped and logged.

4. **Sparse corpora** — If the corpus contains fewer than ~5 readable files, the
   category inventory may be empty, routing everything to Review/Uncategorized.
   This is correct behaviour: DocSort refuses to invent categories.

5. **Non-Latin scripts** — Regex patterns are English/French. Category discovery
   will not work for documents in Arabic, Chinese, etc.

6. **Filename collisions at destination** — Handled by appending _1, _2, etc.
   to the destination filename. Original files are never overwritten.

7. **Owner detection is conservative** — A low false-positive rate is prioritised.
   Files with weak owner evidence go to Review rather than Mine.

## Related

- [[Research and Papers MOC]]
- [[D Library — Review Unreadable Cleanup (2026-05-04)]]
