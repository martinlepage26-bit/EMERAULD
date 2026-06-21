"""
server.py — PHAROS FastAPI backend entry point.

Hardening applied per PR #4 goals:
  1. Structured logging (no bare print())
  2. Safe lifespan startup (DB failure = degraded mode, not crash)
  3. dnspython guard (CRITICAL log if SRV URL + missing dns package)
  4. ReturnDocument.AFTER on all find_one_and_update calls
  5. Health endpoint exposes db_ready for deployment verification

Entry point: uvicorn server:app (confirmed by Dockerfile)
"""

from __future__ import annotations

import importlib.util
import logging
import os
from contextlib import asynccontextmanager
from typing import Any

from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from motor.motor_asyncio import AsyncIOMotorClient
from pydantic import BaseModel
from pymongo import ReturnDocument

# ── Structured logging ────────────────────────────────────────────────────────
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s %(levelname)s %(name)s: %(message)s",
)
log = logging.getLogger("pharos")


# ── Module-level DB state (set in lifespan) ───────────────────────────────────
mongo_client: AsyncIOMotorClient | None = None
DB_READY: bool = False
db: Any = None


# ── dnspython guard ───────────────────────────────────────────────────────────
def _check_dnspython() -> None:
    """
    Warn at startup if dnspython is absent and MONGO_URL uses the SRV scheme.
    Motor raises ConfigurationError at client instantiation without dnspython.
    Uses importlib.util.find_spec — side-effect-free and mockable in tests.
    """
    mongo_url = os.environ.get("MONGO_URL", "")
    if not mongo_url.startswith("mongodb+srv://"):
        return
    if importlib.util.find_spec("dns") is None:
        log.critical(
            "MONGO_URL uses mongodb+srv:// but dnspython is not installed. "
            "Fix: pip install 'dnspython>=2.1.0' and add to requirements.txt. "
            "Every DB-backed endpoint will fail until this is resolved."
        )


# ── Lifespan context manager ─────────────────────────────────────────────────
@asynccontextmanager
async def lifespan(app: FastAPI):
    """
    Startup: attempt DB connection. Warn but do not crash if DB is unreachable.
    Shutdown: close Motor connection pool cleanly.
    """
    global mongo_client, DB_READY, db
    _check_dnspython()

    mongo_url = os.environ.get("MONGO_URL", "")
    db_name = os.environ.get("DB_NAME", "ai_governance")

    if not mongo_url:
        log.warning(
            "MONGO_URL not set — running without database. "
            "DB-backed endpoints will return 503."
        )
        DB_READY = False
    else:
        try:
            mongo_client = AsyncIOMotorClient(
                mongo_url,
                serverSelectionTimeoutMS=5000,
            )
            await mongo_client.admin.command("ping")
            db = mongo_client[db_name]
            DB_READY = True
            log.info("MongoDB connected: db=%s", db_name)
        except Exception as exc:
            DB_READY = False
            log.warning(
                "MongoDB unavailable at startup — degraded mode. Error: %s. "
                "DB-backed endpoints will return 503 until connection is restored.",
                exc,
            )

    yield

    if mongo_client is not None:
        mongo_client.close()
        log.info("MongoDB connection closed.")


# ── App construction ──────────────────────────────────────────────────────────
app = FastAPI(
    title="PHAROS API",
    description="Backend for the PHAROS AI governance suite",
    version="1.0.0",
    lifespan=lifespan,
)

# CORS — configurable via ALLOWED_ORIGINS env var (comma-separated)
_origins_raw = os.environ.get(
    "ALLOWED_ORIGINS",
    "http://localhost:3000,http://localhost:5173,https://pharos-ai.ca",
)
_origins = [o.strip() for o in _origins_raw.split(",") if o.strip()]

app.add_middleware(
    CORSMiddleware,
    allow_origins=_origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# ── Helper: require DB ───────────────────────────────────────────────────────
def require_db():
    """Raise 503 if database is not ready."""
    if not DB_READY or db is None:
        raise HTTPException(
            status_code=503,
            detail="Database unavailable — service is in degraded mode.",
        )
    return db


# ── Health ────────────────────────────────────────────────────────────────────
@app.get("/api/health")
@app.get("/health")
async def health():
    """App liveness + DB readiness — two separate signals."""
    return {
        "status": "ok",
        "environment": os.environ.get("ENVIRONMENT", "production"),
        "db_ready": DB_READY,
    }


# ── Pydantic models ──────────────────────────────────────────────────────────
class DocumentCreate(BaseModel):
    title: str
    content: str | None = None
    tags: list[str] = []


class DocumentUpdate(BaseModel):
    title: str | None = None
    content: str | None = None
    tags: list[str] | None = None


# ── CRUD routes ───────────────────────────────────────────────────────────────
@app.get("/api/documents")
async def list_documents():
    """List all documents."""
    active_db = require_db()
    docs = []
    async for doc in active_db.documents.find():
        doc["_id"] = str(doc["_id"])
        docs.append(doc)
    return docs


@app.post("/api/documents", status_code=201)
async def create_document(doc: DocumentCreate):
    """Create a new document."""
    active_db = require_db()
    result = await active_db.documents.insert_one(doc.model_dump())
    return {"id": str(result.inserted_id), **doc.model_dump()}


@app.put("/api/documents/{doc_id}")
async def update_document(doc_id: str, update: DocumentUpdate):
    """
    Update a document.
    Uses return_document=ReturnDocument.AFTER so the response reflects
    the updated state, not the pre-update state.
    """
    from bson import ObjectId

    active_db = require_db()
    update_fields = {k: v for k, v in update.model_dump().items() if v is not None}
    if not update_fields:
        raise HTTPException(status_code=400, detail="No fields to update.")

    result = await active_db.documents.find_one_and_update(
        {"_id": ObjectId(doc_id)},
        {"$set": update_fields},
        return_document=ReturnDocument.AFTER,
    )
    if result is None:
        raise HTTPException(status_code=404, detail="Document not found.")
    result["_id"] = str(result["_id"])
    return result


@app.delete("/api/documents/{doc_id}")
async def delete_document(doc_id: str):
    """Delete a document."""
    from bson import ObjectId

    active_db = require_db()
    result = await active_db.documents.delete_one({"_id": ObjectId(doc_id)})
    if result.deleted_count == 0:
        raise HTTPException(status_code=404, detail="Document not found.")
    return {"deleted": True}


# ── Governance endpoints ──────────────────────────────────────────────────────
@app.get("/api/governance/status")
async def governance_status():
    """Return current governance configuration status."""
    active_db = require_db()
    config = await active_db.governance_config.find_one({"active": True})
    if config:
        config["_id"] = str(config["_id"])
    return {"config": config, "db_ready": DB_READY}


@app.put("/api/governance/config/{config_id}")
async def update_governance_config(config_id: str, update: dict):
    """
    Update governance configuration.
    Uses return_document=ReturnDocument.AFTER.
    """
    from bson import ObjectId

    active_db = require_db()
    result = await active_db.governance_config.find_one_and_update(
        {"_id": ObjectId(config_id)},
        {"$set": update},
        return_document=ReturnDocument.AFTER,
    )
    if result is None:
        raise HTTPException(status_code=404, detail="Config not found.")
    result["_id"] = str(result["_id"])
    return result
