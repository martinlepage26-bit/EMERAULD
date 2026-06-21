#!/usr/bin/env python3
"""
Query the EMERAULD knowledge graph via LightRAG.
Token-efficient: only retrieves the relevant subgraph for each question.

Usage:
    python query.py "What do I know about recursive governance?"
    python query.py "How does PHAROS relate to AI governance?" --mode hybrid
    python query.py "Summary of all novel projects" --mode global

Modes:
    local   — specific entity lookup (lowest token cost)
    global  — broad community summary (medium cost)
    hybrid  — combines local + global (recommended default)
    naive   — flat vector search (no graph, fast)
    mix     — full graph + vector (highest quality, highest cost)
"""

import asyncio
import argparse
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))

_IMPORT_ERROR: Exception | None = None
try:
    from lightrag_config import make_rag
except Exception as e:  # keep CLI help usable even when deps are missing
    make_rag = None  # type: ignore[assignment]
    _IMPORT_ERROR = e


async def query(
    question: str,
    mode: str = "hybrid",
    max_tokens: int = 12000,
    top_k: int = 40,
    chunk_top_k: int = 30,
    max_entity_tokens: int | None = None,
    max_relation_tokens: int | None = None,
    enable_rerank: bool = False,
    fallback: bool = True,
):
    if make_rag is None:
        msg = (
            "LightRAG query deps are not available in this Python environment.\n"
            "Try running in the EMERAULD lightrag venv (WSL) or install deps locally.\n"
        )
        if _IMPORT_ERROR:
            msg += f"\nImport error: {_IMPORT_ERROR}\n"
        raise RuntimeError(msg)

    try:
        from lightrag import QueryParam
    except Exception as e:
        raise RuntimeError(
            "Missing `lightrag` dependency. Install it (and numpy, sentence-transformers, httpx) "
            "or run in the configured EMERAULD venv."
        ) from e

    # Prevent entity/relation token budgets from consuming all context budget
    # and leaving zero chunk tokens (common local/hybrid failure mode).
    default_graph_cap = min(2200, max(1000, max_tokens // 5))
    entity_tokens = (
        max_entity_tokens if max_entity_tokens is not None else default_graph_cap
    )
    relation_tokens = (
        max_relation_tokens if max_relation_tokens is not None else default_graph_cap
    )

    rag = make_rag()
    await rag.initialize_storages()
    try:
        async def run_mode(
            run_mode: str,
            run_top_k: int = top_k,
            run_chunk_top_k: int = chunk_top_k,
            only_need_context: bool = False,
        ):
            return await rag.aquery(
                question,
                param=QueryParam(
                    mode=run_mode,
                    max_total_tokens=max_tokens,
                    top_k=run_top_k,
                    chunk_top_k=run_chunk_top_k,
                    max_entity_tokens=entity_tokens,
                    max_relation_tokens=relation_tokens,
                    enable_rerank=enable_rerank,
                    only_need_context=only_need_context,
                ),
            )

        answer = await run_mode(mode)

        # Some local-mode builds can return no usable chunk context and answer
        # with a generic "not enough information". Fallback keeps queries useful.
        if fallback:
            low = str(answer).strip().lower()
            insufficient_markers = (
                "not enough information",
                "do not have enough information",
                "don't have enough information",
                "cannot answer",
                "can't answer",
                "insufficient context",
                "insufficient information",
                "unable to answer",
            )
            insufficient = (not low) or any(m in low for m in insufficient_markers)
            if insufficient:
                fallback_modes = []
                if mode == "local":
                    # Prefer graph-aware hybrid before any context-only fallback.
                    fallback_modes = ["hybrid"]
                elif mode == "hybrid":
                    fallback_modes = ["naive"]

                for fb_mode in fallback_modes:
                    fb_top_k = top_k
                    fb_chunk_top_k = chunk_top_k
                    if fb_mode == "naive":
                        # Naive fallback relies entirely on chunks; widen it.
                        fb_chunk_top_k = max(chunk_top_k, 80)
                    fb_answer = await run_mode(fb_mode, fb_top_k, fb_chunk_top_k)
                    fb_low = str(fb_answer).strip().lower()
                    fb_insufficient = (not fb_low) or any(
                        m in fb_low for m in insufficient_markers
                    )
                    if not fb_insufficient:
                        return f"[fallback:{fb_mode}] {fb_answer}"

                # Last-resort fallback: return retrieved context instead of
                # failing with a generic "not enough information".
                context_mode = "naive" if mode in {"local", "hybrid"} else mode
                context = await run_mode(
                    context_mode,
                    top_k,
                    max(chunk_top_k, 80),
                    only_need_context=True,
                )
                if context:
                    return f"[fallback:{context_mode}-context-only]\n{context}"

        return answer
    finally:
        await rag.finalize_storages()


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("question", help="What to ask the knowledge graph")
    parser.add_argument("--mode", default="hybrid",
                        choices=["local", "global", "hybrid", "naive", "mix"],
                        help="Retrieval mode (default: hybrid)")
    parser.add_argument("--max-tokens", type=int, default=12000,
                        help="Max tokens in retrieved context (default: 12000)")
    parser.add_argument("--top-k", type=int, default=40,
                        help="Entity/relation retrieval breadth (default: 40)")
    parser.add_argument("--chunk-top-k", type=int, default=30,
                        help="Chunk retrieval breadth (default: 30)")
    parser.add_argument("--max-entity-tokens", type=int, default=None,
                        help="Entity context token cap (default: auto from max-tokens)")
    parser.add_argument("--max-relation-tokens", type=int, default=None,
                        help="Relation context token cap (default: auto from max-tokens)")
    parser.add_argument("--enable-rerank", action="store_true",
                        help="Enable reranking (disabled by default unless a rerank model is configured)")
    parser.add_argument("--no-fallback", action="store_true",
                        help="Disable automatic fallback chain when answer is insufficient")
    args = parser.parse_args()

    try:
        result = asyncio.run(
            query(
                args.question,
                args.mode,
                args.max_tokens,
                args.top_k,
                args.chunk_top_k,
                args.max_entity_tokens,
                args.max_relation_tokens,
                args.enable_rerank,
                not args.no_fallback,
            )
        )
        print(result)
    except RuntimeError as e:
        print(str(e).strip(), file=sys.stderr)
        sys.exit(2)
