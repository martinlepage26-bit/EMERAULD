---
type: raw-source
aliases: [orphan-raw-2026-05-06-002]
graph_repair: 2026-05-06
---

# DocSort — Python dependencies
See also [[Manuscript Pipeline MOC]].
# Install with: pip install -r requirements.txt

# Document extraction
python-docx>=1.1.0        # .docx reading + metadata
pypdf>=4.0.0              # PDF text extraction (fallback)
pdfplumber>=0.10.0        # PDF text extraction (preferred)
striprtf>=0.0.26          # .rtf extraction

# Optional — .doc support on non-Windows systems requires antiword (external binary)
# On Windows, the program uses Word COM automation if antiword is unavailable
# pywin32>=306             # uncomment on Windows for .doc COM fallback

# Standard library only (no extra install needed):
# tkinter, pathlib, csv, json, logging, collections, re, shutil, dataclasses
