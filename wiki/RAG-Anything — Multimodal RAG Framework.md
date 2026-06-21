---
type: wiki
aliases: [RAG-Anything, multimodal RAG, HKUDS RAG-Anything, raganything]
tags: [ai-tooling, retrieval, rag, multimodal, infrastructure, knowledge-graph, python]
status: active
created: 2026-04-16
updated: 2026-04-16
---

# RAG-Anything — Multimodal RAG Framework

## Summary

RAG-Anything (HKUDS/RAG-Anything, arXiv 2510.12323) is a comprehensive All-in-One Multimodal Document Processing RAG system built on [[LightRAG — Graph-Based RAG System]]. It handles any document type — PDFs, Office files, images, tables, mathematical equations — through a 5-stage pipeline that extracts multimodal entities into a cross-modal knowledge graph, enabling hybrid retrieval across the full document surface without multiple specialized tools.

## Context

RAG-Anything sits one layer above [[LightRAG — Graph-Based RAG System]] in the HKUDS retrieval stack. It is the natural extension point when the [[EMERAULD Second Brain — Project Context]] needs to ingest non-text materials — scanned PDFs, image-embedded tables, or research papers with figures — into the same knowledge graph that [[LightRAG — Graph-Based RAG System]] manages for wiki notes. It connects to the [[GSD — Get Shit Done Context Engineering System]] pattern of reducing friction in information capture by handling source diversity at the ingestion layer. The enriched source was captured on 2026-04-16.

## Details

### Core Architecture: 5-Stage Pipeline

RAG-Anything implements a multi-stage multimodal pipeline that extends traditional RAG architectures:

| Stage | What It Does |
|---|---|
| 1. Document Parsing | High-fidelity extraction via MinerU, Docling, or PaddleOCR; segments text, images, tables, equations while preserving hierarchy |
| 2. Multi-Modal Content Understanding | Autonomous content categorization and routing through concurrent pipelines; preserves document hierarchy |
| 3. Multimodal Analysis Engine | Modality-aware processors: Visual Content Analyzer (VLM), Structured Data Interpreter, Mathematical Expression Parser, Extensible Modality Handler |
| 4. Multimodal Knowledge Graph Index | Extracts multimodal entities, establishes cross-modal relationships, preserves hierarchical "belongs_to" chains, applies weighted relevance scoring |
| 5. Modality-Aware Retrieval | Hybrid vector-graph fusion search; modality-aware ranking; relational coherence maintenance |

### Supported Input Types

**Document Formats:**
- PDFs — research papers, reports, presentations
- Office Documents — DOC, DOCX, PPT, PPTX, XLS, XLSX (requires LibreOffice)
- Images — JPG, PNG, BMP, TIFF, GIF, WebP
- Text Files — TXT, MD

**Multimodal Elements:**
- Images — photographs, diagrams, charts, screenshots
- Tables — data tables, comparison charts, statistical summaries
- Equations — mathematical formulas in LaTeX format
- Generic content — custom types via extensible processors

### Available Parsers

Three parser backends are available:

- **MinerU** — default; strong OCR, PDF, table extraction, GPU acceleration support; uses command-line parameters (MinerU 2.0+, no config file)
- **Docling** — optimized for Office documents and HTML; better document structure preservation
- **PaddleOCR** — OCR-focused for images and PDFs; `pip install raganything[paddleocr]`

### Query Modes

Three query types are available:

1. **Pure Text Queries** — direct [[LightRAG — Graph-Based RAG System]] knowledge base search; modes: `hybrid`, `local`, `global`, `naive`
2. **VLM Enhanced Queries** — automatically integrates retrieved images into a vision model for direct visual analysis; auto-enabled when `vision_model_func` is provided
3. **Multimodal Queries** (`aquery_with_multimodal`) — enhanced queries with specific multimodal content (table data, equations, etc.) passed alongside the question

### Installation

```bash
pip install raganything           # Basic
pip install 'raganything[all]'   # All optional Python features
# LibreOffice must be installed separately for Office document support
```

- Python 3.10+
- uv-ready: `uv sync` or `uv sync --all-extras`
- Verify: `python -c "from raganything import RAGAnything"`

### Direct Content List Insertion

A notable feature: bypass document parsing entirely by inserting pre-parsed content lists directly. Useful when:
- Source comes from external parsers (not MinerU/Docling)
- Cached parsing results need reuse
- Programmatically generated content must be ingested

Content list format supports `text`, `image`, `table`, `equation`, and custom `type` entries, each with a `page_idx` field.

### Relationship to LightRAG

RAG-Anything is built on [[LightRAG — Graph-Based RAG System]] and inherits its graph storage, query modes, and backend support. It adds a preprocessing and multimodal analysis layer on top. An existing [[LightRAG — Graph-Based RAG System]] instance can be passed directly to `RAGAnything(lightrag=existing_instance)` without re-initializing storage.

### Source Repository

- GitHub: HKUDS/RAG-Anything
- Paper: arXiv 2510.12323 (Guo, Ren, Xu, Zhang, Huang, 2025)
- PyPI: `raganything`

## Key Ideas

- RAG-Anything does not replace [[LightRAG — Graph-Based RAG System]] — it extends it. The retrieval engine is the same; the input surface is wider.
- The primary use case is document corpora that resist plain text: research PDFs with figures, scanned materials, tables exported from spreadsheets, Office presentations.
- For EMERAULD's current use (wiki notes in markdown), LightRAG alone is sufficient. RAG-Anything becomes relevant when ingesting assets from the `assets/` folder or external PDFs.
- VLM Enhanced Query mode (2025.08) is a significant capability: the system can retrieve image paths from context and send them live to a vision model for direct visual analysis, not just caption lookup.
- The extensible modality handler enables custom content type processors via plugin architecture — future modalities can be added without changing the core pipeline.

## Open Questions

- Is RAG-Anything stable for production use, or still in active research preview?
- Does the VLM Enhanced Query mode require a specific vision model or work with any OpenAI-compatible VLM endpoint?
- What is the performance overhead of multimodal preprocessing vs. plain text ingestion for a vault the size of EMERAULD?
- Does PaddleOCR parser produce equivalent knowledge graph quality compared to MinerU for academic PDFs?

## Sources

- `raw sources/rag-anything-2026-04-16.md` (enriched 2026-04-16)
- arXiv 2510.12323

## Related

- [[LightRAG — Graph-Based RAG System]]
- [[EMERAULD Second Brain — Project Context]]
- [[claude-mem — Persistent Memory Compression for Claude Code]]
- [[Plugin Recommendations]]
- [[GSD — Get Shit Done Context Engineering System]]
- [[2025 - PowerPoint Presentation]]
