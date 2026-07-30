# GAP — PR #4 server.py spec alignment

**Surfaced:** 2026-04-19 (Track A/B closeout)
**Status:** OPERATOR DECISION REQUIRED
**Source of truth:** `session-state.md` §2026-04-19 (late) — Three-track operationalization closeout
**Owner:** Martin

---

## The gap

Live `pharos-suite/backend/server.py` (~797 lines) has lifespan + dnspython
pinned (`dnspython==2.8.0`, newer than the bundle's 2.6.1), but took a
different PR #4 trajectory than the L99 bundle spec. Both implementations are
internally coherent; they disagree on the `/health` response shape, the
dnspython guard surface, and the logger namespace.

**Shared — no divergence:**
- Lifespan context manager replaces `@app.on_event("startup"/"shutdown")`
- `dnspython` pinned (P1 closed — live uses 2.8.0, bundle uses 2.6.1; both
  solve the same Motor-on-Atlas ConfigurationError)

**Diverges — live vs. bundle spec:**

| # | Contract point                | Live server.py                                   | Bundle spec                                                       |
|---|-------------------------------|--------------------------------------------------|-------------------------------------------------------------------|
| 1 | `_check_dnspython()` guard    | absent (P1 closed via pin only, no runtime check) | present; logs CRITICAL on `mongodb+srv://` w/o dns at startup     |
| 2 | `/health` top-level status    | `status: "healthy"`                              | `status: "ok"`                                                    |
| 3 | `/health` second field        | `timestamp: <iso-time>`                          | `environment: <ENVIRONMENT env var>`                              |
| 4 | `/health` db readiness        | no `db_ready` field                              | `db_ready: bool` (readiness separate from liveness)               |
| 5 | Logger name                   | `logging.getLogger(__name__)`                    | `logging.getLogger("pharos")` (fixed)                             |

Net: the bundle's 15-test `test_backend_hardening.py` would fail **8+ of 15**
tests against the live server. The suite was deliberately **not installed** in
the Track B port — installing it would claim a regression lock that CI doesn't
actually enforce.

---

## Two paths, each minimal

### Path A — Adapt live server to bundle spec (RECOMMENDED)

Additive-only changes; no behavior removed. Preserves the bundle's regression
coverage and the runbook's degraded-mode invariants.

**Why recommended:**
- `_check_dnspython()` turns a silent Motor-on-Atlas misconfiguration
  into a CRITICAL log at startup. The pin alone does not protect against a
  future `requirements.txt` edit that removes dnspython again — which is
  exactly the P1 that just happened. The guard is a standing alarm.
- `db_ready` separates readiness from liveness. Railway and Cloudflare
  health probes benefit from the split: liveness ("process alive") → restart
  policy; readiness ("can serve DB-backed routes") → traffic routing.
  Collapsing them forces ops to guess whether a 200 means "healthy" or
  "healthy but serving 503s."
- `status: "ok"` + `environment` is the shape every bundle test, the
  runbook, and the Dockerfile healthcheck comment all expect. `"healthy"` +
  `timestamp` is equally valid as a contract — it just happens to be
  nobody-else's contract.
- Fixed logger name `"pharos"` lets log aggregation filter on a stable
  namespace. `__name__` means the filter key drifts with import path and
  module split.

Four surgical changes. Each is self-contained and independently verifiable.

#### Change 1 — rename logger

Find the top-of-module logger assignment:
```python
log = logging.getLogger(__name__)   # or: logger = logging.getLogger(__name__)
```

Replace the **argument** (not necessarily the variable name):
```python
log = logging.getLogger("pharos")
```

Keep whatever variable name (`log` vs `logger`) is already used throughout
the file. Only the string passed to `getLogger` changes.

#### Change 2 — add `_check_dnspython()` guard

Add after imports, before the lifespan definition:

```python
import importlib.util

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
```

Call it as the first line of the `lifespan` body:

```python
@asynccontextmanager
async def lifespan(app: FastAPI):
    _check_dnspython()   # ← add as first line
    ...existing body...
```

#### Change 3 — reshape `/health` response

Find the `/health` handler. Live currently returns something like:
```python
return {"status": "healthy", "timestamp": datetime.utcnow().isoformat()}
```

Replace with the bundle contract (keep both route decorators if both exist):
```python
@app.get("/api/health")
@app.get("/health")
async def health():
    return {
        "status": "ok",
        "environment": os.environ.get("ENVIRONMENT", "production"),
        "db_ready": DB_READY,      # ← module-level bool set by lifespan
    }
```

**Caller impact:** any frontend or uptime monitor keyed on `status: "healthy"`
or reading `timestamp` must update. Grep the frontend repo before flipping:

```bash
cd /path/to/pharos-frontend
grep -rn '"healthy"\|response\.timestamp' src/
```

If there are callers, update them in the same PR as the server change. If
none, the switch is transparent.

#### Change 4 — expose `DB_READY` from lifespan

If the live `lifespan` doesn't already set a module-level readiness flag,
add one:

```python
# Module-level readiness state (set in lifespan)
DB_READY: bool = False

@asynccontextmanager
async def lifespan(app: FastAPI):
    global DB_READY
    _check_dnspython()
    # ... try DB connect ...
    try:
        await client.admin.command("ping")
        DB_READY = True
    except Exception as exc:
        DB_READY = False
        log.warning("MongoDB unavailable at startup — degraded mode: %s", exc)
    yield
    # ... close connection ...
```

If the live lifespan crashes hard on DB failure instead of degrading, this is
the one **behavioral** (not purely additive) change in Path A: switch from
`raise` to `log.warning + DB_READY = False`. The bundle runbook relies on
degraded-mode startup so Railway can route traffic to a process that's
technically alive but not DB-backed yet (common during Atlas cold-starts).

#### Verify

```bash
# from pharos-suite root, on chore/pr4-archive-toolkit-and-docs
mkdir -p backend/tests
cp /path/to/EMERAULD/artifacts/2026-04-19-pharos-migration-pr4/backend/tests/test_backend_hardening.py \
   backend/tests/

cd backend
pytest tests/test_backend_hardening.py -v --basetemp=/tmp/pytest_pharos -p no:cacheprovider
```

Expected: **15 passed** in under 3 seconds. No live MongoDB required — Motor
is mocked throughout. If any test fails, the failure message names which
contract point is still diverged.

---

### Path B — Treat bundle tests as obsolete

Only the right call if at least one bundle-spec invariant is *wrong for your
deployment*:

- `_check_dnspython()` is wrong if you prefer no runtime check at all (but
  the pin-alone protection is weaker — a future `pip-compile` or manual
  requirements edit can silently remove dnspython).
- `db_ready` separation is wrong if you've deliberately collapsed liveness
  and readiness into one signal (unusual — CF and Railway both benefit from
  the split).
- Fixed logger `"pharos"` is wrong if you prefer per-module hierarchies
  (`pharos.server`, `pharos.routes.x`) — in which case the bundle's single
  name is a regression.
- `status: "healthy"` is the contract the frontend or an external uptime
  monitor already depends on, and the cost of flipping the contract exceeds
  the cost of a new test suite.

If Path B is chosen:

1. **Do not install** `backend/tests/test_backend_hardening.py` into
   `pharos-suite`. Leave it in the L99 archive as a reference-only spec for
   a design that was considered and diverged from.
2. **Write** `backend/tests/test_server.py` in `pharos-suite` that asserts
   the live contract: `status: "healthy"`, `timestamp` ISO-8601 parseable,
   whatever logger convention is in use, whatever startup guarantees hold.
3. **Record the decision** in a short ADR under `docs/ADR/` — why the
   bundle contract was declined, what replaced each invariant, what the new
   regression surface covers.
4. **Update** `_manifest/MANIFEST.md` and `_manifest/RUN-ORDER.md` in the
   L99 archive with a banner that the bundle test suite no longer reflects
   production.

Path B cost estimate: ~2 hours (new tests + ADR + manifest updates).
Path A cost estimate: ~15 minutes (four edits + one pytest run + one frontend
grep).

---

## Recommendation

**Path A.** The four divergences are low-cost to align and the bundle tests
become ongoing regression coverage not just for dnspython but for the full
hardening surface (CORS, requirements integrity, lifespan correctness). The
only load-bearing question is whether any caller depends on `status:
"healthy"` or `timestamp` — a 30-second grep resolves that.

---

## After the decision

- Mark the "PR #4 spec decision" row resolved in `session-state.md` §Track D.
- Add the outcome as a dated `Decisions Made` entry.
- Whichever patch was applied, include it in the same commit range on
  `chore/pr4-archive-toolkit-and-docs` before pushing.
- Then `git push -u origin chore/pr4-archive-toolkit-and-docs` and open the PR.

## Related

- [[Writing and Novels MOC]]
- [[artifacts/2026-04-19-pharos-migration-pr4/_manifest/MANIFEST]]
