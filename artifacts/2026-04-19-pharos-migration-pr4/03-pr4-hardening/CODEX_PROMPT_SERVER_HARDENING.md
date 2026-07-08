---
type: artifact
title: CODEX PROMPT — server.py HARDENING
aliases:
- artifacts/2026-04-19-pharos-migration-pr4/03-pr4-hardening/CODEX_PROMPT_SERVER_HARDENING
tags:
- artifact
- pharos
- artifacts
- 2026-04-19-pharos-migration-pr4
- lifespan
- mongo
- server
- dnspython
- startup
- color-green
status: preserved
created: '2026-04-19'
updated: '2026-06-26'
vault_area: artifacts
canonical_path: artifacts/2026-04-19-pharos-migration-pr4/03-pr4-hardening/CODEX_PROMPT_SERVER_HARDENING.md
backlink_count: 2
backlinks:
- '[[Areas/Writing/Research and Papers MOC]]'
- '[[wiki/archive/Orphan Index — Artifacts And Archives — 2026-05-06]]'
---

# CODEX PROMPT — server.py HARDENING
# Scope: apply PR #4 hardening goals to the real backend entry point
# Target file: backend/server.py (NOT main.py — Dockerfile confirms server.py)
# Run from: pharos-suite repo root
# Completion check: all items in COMPLETION CHECKLIST are satisfied

## CONTEXT

The Dockerfile confirms:
  CMD uvicorn server:app ...

The backend entry point is backend/server.py. A previous session produced a
main.py template — ignore it. All hardening applies to server.py only.

The requirements.txt in this PR already has dnspython==2.6.1. That P1 bug is
fixed at the dependency level. This prompt addresses the application-level
hardening: structured logging, safe startup, dnspython guard, health endpoint.

## STEP 0 — Read the file first

```bash
cat backend/server.py
```

Report:
- How many lines
- Whether it uses @app.on_event("startup") or a lifespan context manager already
- Whether it has import logging
- Whether it has print() statements
- What the /health or /api/health endpoint currently returns
- What DB state variables exist at module level

Then proceed.

## STEP 1 — Add structured logging

At the top of server.py, after all import statements and before any route or
app-level code, ensure this block exists exactly once:

```python
import importlib.util
import logging

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s %(levelname)s %(name)s: %(message)s",
)
log = logging.getLogger("pharos")
```

Then: find every `print(` in the file. Replace each with the appropriate call:
- Informational output → `log.info(...)`
- Error or warning → `log.warning(...)` or `log.error(...)`

Report each replacement as: `LINE N: print(...) → log.info(...)`

Do NOT replace print() calls inside test files, only server.py.

## STEP 2 — Add module-level DB state

If the file does not already have module-level variables for DB state, add
these immediately before the lifespan/startup block:

```python
# Module-level DB state — set during lifespan startup
_mongo_client = None
_db_ready: bool = False
```

Use whatever naming convention already exists in the file. If a motor client
variable already exists, do not create a duplicate.

## STEP 3 — Add _check_dnspython()

Add this function before the lifespan/startup block:

```python
def _check_dnspython() -> None:
    """
    Warn at startup if dnspython is absent and MONGO_URL uses SRV scheme.
    Motor raises ConfigurationError at client instantiation without it.
    Uses importlib.util.find_spec — side-effect-free and mockable in tests.
    """
    mongo_url = os.environ.get("MONGO_URL", "")
    if not mongo_url.startswith("mongodb+srv://"):
        return
    if importlib.util.find_spec("dns") is None:
        log.critical(
            "MONGO_URL uses mongodb+srv:// but dnspython is not installed. "
            "Fix: ensure dnspython is in requirements.txt. "
            "Every DB-backed endpoint will fail at runtime until resolved."
        )
```

## STEP 4 — Convert startup to lifespan context manager

### 4a — If the file uses @app.on_event

If server.py uses `@app.on_event("startup")` and `@app.on_event("shutdown")`,
replace them with a lifespan context manager.

Ensure `from contextlib import asynccontextmanager` is imported.

The lifespan pattern:

```python
@asynccontextmanager
async def lifespan(app: FastAPI):
    global _mongo_client, _db_ready
    _check_dnspython()
    try:
        _mongo_client = AsyncIOMotorClient(
            os.environ.get("MONGO_URL", "mongodb://localhost:27017"),
            serverSelectionTimeoutMS=5000,
        )
        await _mongo_client.admin.command("ping")
        _db_ready = True
        log.info("MongoDB connected: db=%s", os.environ.get("DB_NAME", "ai_governance"))
    except Exception as exc:
        _db_ready = False
        log.warning(
            "MongoDB unavailable at startup — degraded mode. "
            "DB-backed endpoints will return 503 until connection is restored. "
            "Error: %s", exc
        )
    yield
    if _mongo_client is not None:
        _mongo_client.close()
        log.info("MongoDB connection closed.")

app = FastAPI(lifespan=lifespan, ...)
```

Pass lifespan= to the FastAPI() constructor. If app is already constructed
(e.g., app = FastAPI(title=...)), update that constructor call to add
lifespan=lifespan.

### 4b — If the file already uses a lifespan context manager

Add `_check_dnspython()` as the first call inside the lifespan function,
before any DB setup. Add the try/except degradation pattern around the DB
connection if it is not already there.

## STEP 5 — Update the health endpoint

Find the /health or /api/health endpoint. Update it to return db_ready:

```python
@app.get("/api/health")
@app.get("/health")
async def health():
    return {
        "status": "ok",
        "environment": os.environ.get("ENVIRONMENT", "production"),
        "db_ready": _db_ready,
    }
```

If the existing endpoint uses a different response model, add db_ready to it.
Do not remove existing fields.

## STEP 6 — Verify ReturnDocument usage

```bash
grep -n "find_one_and_update" backend/server.py
```

For each match, check whether `return_document=ReturnDocument.AFTER` is passed.
If missing or BEFORE is used, add/fix it.
Report: "FILE:LINE — added return_document=ReturnDocument.AFTER" for each fix.
Report: "No find_one_and_update calls found" if none exist.

## STEP 7 — Run the test suite

```bash
cd /home/cerebrhoe/repos/pharos-suite/backend
pip install -r requirements.txt
pytest tests/ -v --tb=short
```

If tests/test_backend_hardening.py exists (from the previous Codex session),
include it. If it does not exist, create it at tests/test_backend_hardening.py
using the content from the prior session (Claude's 16-test suite, adapted to
import from server instead of main).

All tests must pass. If any fail, fix the underlying code — do not skip.

## COMPLETION CHECKLIST

All of the following must be true:

- [ ] server.py has `import logging` and `log = logging.getLogger("pharos")`
- [ ] No bare `print()` statements remain in server.py
- [ ] `_check_dnspython()` exists and is called at startup
- [ ] DB connection failure does not crash the process (warns + sets db_ready=False)
- [ ] `/api/health` returns `{"status": "ok", "db_ready": bool, ...}`
- [ ] All `find_one_and_update` calls use `return_document=ReturnDocument.AFTER`
- [ ] `pytest tests/ -v` passes with no failures
- [ ] `import importlib.util` is present in server.py

Report each bullet as PASS or FAIL with one line of evidence.
Do not report completion unless all bullets are PASS.

## Related

- [[Research and Papers MOC]]
- [[SHOW-ME-WHAT-TO-DO]]
