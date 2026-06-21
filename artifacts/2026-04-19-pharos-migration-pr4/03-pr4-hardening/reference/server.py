"""
backend/server.py — PR #4 target reference

This file is the TARGET STATE that Codex should produce when applying
the PR #4 backend-hardening pass plus the P1 dnspython fix.

Design decisions baked in:
  • Lifespan context manager replaces the deprecated @app.on_event pair.
  • DB startup is SAFE: a ping() failure puts the app into a degraded
    mode (db_ready=False) instead of crashing. Health probes stay 200.
  • Structured logging under the "pharos" logger, emitted as key=value
    pairs so CloudWatch/Railway/DataDog parsers can pick them up.
  • _check_dnspython() runs before Motor is constructed. If MONGO_URL
    is mongodb+srv://... and dnspython is not importable, we emit a
    CRITICAL log that breaks CI (the regression guard in the tests).
  • CORS is origin-list driven from ALLOWED_ORIGINS, comma-separated.
  • Two health routes: /health and /api/health (ingress-alias friendly).

Contract tested by tests/test_backend_hardening.py (15 cases).
Run from backend/:   pytest tests/test_backend_hardening.py -v
"""

from __future__ import annotations

import importlib.util
import logging
import os
from contextlib import asynccontextmanager
from typing import Any

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from motor.motor_asyncio import AsyncIOMotorClient

# ── Logging: single named logger, structured output ──────────────────────────
logger = logging.getLogger("pharos")
if not logger.handlers:
    _h = logging.StreamHandler()
    _h.setFormatter(logging.Formatter(
        "%(asctime)s level=%(levelname)s logger=%(name)s %(message)s"
    ))
    logger.addHandler(_h)
logger.setLevel(logging.INFO)


# ── P1 guard: fail loudly if dnspython is missing on an SRV URL ──────────────
def _check_dnspython() -> None:
    """
    Regression guard against the PR #4 Codex-flagged P1 bug.

    Atlas connection strings are always mongodb+srv://... which Motor
    (via pymongo) resolves by doing a DNS SRV lookup. That lookup
    requires the `dnspython` package. If it's missing, Motor raises
    ConfigurationError at client construction. Every DB-backed endpoint
    breaks at runtime with no earlier warning.

    We check here so failure is loud, CRITICAL, and easy to see in logs.
    """
    url = os.getenv("MONGO_URL", "")
    if url.startswith("mongodb+srv://"):
        if importlib.util.find_spec("dns") is None:
            logger.critical(
                "dnspython is not installed but MONGO_URL uses mongodb+srv:// — "
                "Motor will fail to resolve SRV records. "
                "Add `dnspython==2.6.1` to requirements.txt."
            )


# ── Lifespan: safe DB startup, clean shutdown ────────────────────────────────
@asynccontextmanager
async def lifespan(app: FastAPI):
    """Replaces the deprecated @app.on_event('startup'/'shutdown') pair."""
    _check_dnspython()

    mongo_url = os.getenv("MONGO_URL", "mongodb://localhost:27017")
    db_name = os.getenv("DB_NAME", "pharos")

    client = AsyncIOMotorClient(mongo_url, serverSelectionTimeoutMS=3000)
    app.state.mongo_client = client
    app.state.db = client[db_name]
    app.state.db_ready = False

    # Safe startup — ping, but do not crash on failure.
    try:
        await client.admin.command("ping")
        app.state.db_ready = True
        logger.info("event=db_ready db_name=%s", db_name)
    except Exception as exc:  # noqa: BLE001 — we log everything and degrade
        logger.warning(
            "event=db_unreachable db_name=%s error=%r "
            "note=app_continues_in_degraded_mode",
            db_name, exc,
        )

    try:
        yield
    finally:
        try:
            client.close()
            logger.info("event=db_closed")
        except Exception as exc:  # noqa: BLE001
            logger.warning("event=db_close_error error=%r", exc)


# ── App ──────────────────────────────────────────────────────────────────────
app = FastAPI(
    title="PHAROS Backend",
    description="Legible AI governance — deterministic under pressure.",
    version="0.4.0",
    lifespan=lifespan,
)

# CORS
_allowed = [
    o.strip()
    for o in os.getenv("ALLOWED_ORIGINS", "http://localhost:3000").split(",")
    if o.strip()
]
app.add_middleware(
    CORSMiddleware,
    allow_origins=_allowed,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# ── Health ───────────────────────────────────────────────────────────────────
def _health_payload() -> dict[str, Any]:
    return {
        "status": "ok",
        "db_ready": bool(getattr(app.state, "db_ready", False)),
        "environment": os.getenv("ENVIRONMENT", "development"),
        "version": app.version,
    }


@app.get("/health")
async def health() -> dict[str, Any]:
    return _health_payload()


@app.get("/api/health")
async def api_health() -> dict[str, Any]:
    """Ingress-alias of /health for backends mounted behind /api."""
    return _health_payload()
