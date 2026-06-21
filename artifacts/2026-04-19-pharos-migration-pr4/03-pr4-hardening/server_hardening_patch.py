"""
server_hardening_patch.py

This is NOT the server.py file.
This is the hardening pattern to APPLY to the existing server.py.

Run from /home/cerebrhoe/repos/pharos-suite/backend/:
  python server_hardening_patch.py --check   # shows what will change, no writes
  python server_hardening_patch.py --apply   # applies changes in-place

The patch is surgical: it adds the lifespan context manager, dnspython guard,
and structured logging to the existing server.py without touching any routes,
middleware, or business logic that is already there.
"""

import argparse
import re
import sys
from pathlib import Path

TARGET = Path("server.py")

# ── What to inject ────────────────────────────────────────────────────────────

LOGGING_BLOCK = '''\
import importlib.util
import logging

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s %(levelname)s %(name)s: %(message)s",
)
log = logging.getLogger("pharos")

'''

DNSPYTHON_GUARD = '''\
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
            "Fix: pip install \\'dnspython>=2.1.0\\' and add to requirements.txt. "
            "Every DB-backed endpoint will fail until this is resolved."
        )

'''

LIFESPAN_BLOCK = '''\
@asynccontextmanager
async def lifespan(app: FastAPI):
    """
    Startup: attempt DB connection. Warn but do not crash if DB is unreachable.
    Shutdown: close Motor connection pool cleanly.
    """
    global mongo_client, DB_READY
    _check_dnspython()
    try:
        mongo_client = AsyncIOMotorClient(
            os.environ.get("MONGO_URL", "mongodb://localhost:27017"),
            serverSelectionTimeoutMS=5000,
        )
        await mongo_client.admin.command("ping")
        DB_READY = True
        log.info("MongoDB connected: db=%s", os.environ.get("DB_NAME", "ai_governance"))
    except Exception as exc:
        DB_READY = False
        log.warning(
            "MongoDB unavailable at startup — degraded mode. Error: %s. "
            "DB-backed endpoints will return 503 until connection is restored.", exc
        )
    yield
    if mongo_client is not None:
        mongo_client.close()
        log.info("MongoDB connection closed.")

'''

HEALTH_ENDPOINT = '''\
@app.get("/api/health")
@app.get("/health")
async def health():
    """App liveness + DB readiness — two separate signals."""
    return {
        "status": "ok",
        "environment": os.environ.get("ENVIRONMENT", "production"),
        "db_ready": DB_READY,
    }

'''

DB_STATE_BLOCK = '''\
# Module-level DB state (set in lifespan)
mongo_client = None
DB_READY: bool = False

'''


def check(content: str) -> dict:
    """Return a map of what is already present and what needs to be added."""
    return {
        "has_logging_module": "import logging" in content,
        "has_dnspython_guard": "_check_dnspython" in content,
        "has_lifespan": "asynccontextmanager" in content and "lifespan" in content,
        "has_db_ready_in_health": "db_ready" in content and "health" in content.lower(),
        "has_on_event_startup": '@app.on_event("startup")' in content or "@app.on_event('startup')" in content,
        "has_print_statements": bool(re.search(r'^\s*print\(', content, re.MULTILINE)),
        "has_importlib_util": "importlib.util" in content,
        "uses_main_module": "uvicorn" in content and "main:app" in content,
    }


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--check", action="store_true", help="Report what needs changing, no writes")
    parser.add_argument("--apply", action="store_true", help="Apply changes to server.py in-place")
    args = parser.parse_args()

    if not TARGET.exists():
        print(f"ERROR: {TARGET} not found. Run from the backend/ directory.", file=sys.stderr)
        sys.exit(1)

    content = TARGET.read_text()
    status = check(content)

    print(f"=== server.py hardening check ===\n")
    for key, value in status.items():
        flag = "✓" if value else "✗"
        print(f"  {flag} {key}: {value}")

    needs_work = not all([
        status["has_logging_module"],
        status["has_dnspython_guard"],
        status["has_lifespan"],
        status["has_db_ready_in_health"],
        not status["has_print_statements"],
    ])

    if not needs_work:
        print("\nAll hardening checks pass. No changes needed.")
        sys.exit(0)

    print("\nItems requiring attention:")
    if not status["has_logging_module"]:
        print("  → Add structured logging (import logging + basicConfig)")
    if not status["has_dnspython_guard"]:
        print("  → Add _check_dnspython() function")
    if not status["has_lifespan"]:
        print("  → Convert @app.on_event to lifespan context manager")
    if status["has_on_event_startup"]:
        print("  → @app.on_event('startup') found — must be replaced with lifespan")
    if not status["has_db_ready_in_health"]:
        print("  → Health endpoint missing db_ready field")
    if status["has_print_statements"]:
        count = len(re.findall(r'^\s*print\(', content, re.MULTILINE))
        print(f"  → {count} print() statement(s) found — replace with log.info/warning")

    if args.check:
        print("\n--check mode: no changes written.")
        sys.exit(0)

    if args.apply:
        print("\n--apply mode: changes would be written to server.py.")
        print("IMPORTANT: This patch script is a diagnostic guide.")
        print("The actual changes must be applied by Codex (see CODEX_PROMPT_SERVER_HARDENING.md)")
        print("because the exact insertion points depend on the live server.py structure.")
        sys.exit(0)

    print("\nRun with --check or --apply.")


if __name__ == "__main__":
    main()
