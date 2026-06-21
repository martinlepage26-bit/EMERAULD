"""
tests/test_backend_hardening.py

Tests for PR #4 backend hardening + P1 dnspython bug fix.

Targets: backend/server.py (entry point confirmed by Dockerfile)
Falls back to main.py in isolated environments.
Run from backend/: pytest tests/test_backend_hardening.py -v

No live MongoDB required — Motor client is mocked throughout.
"""

from __future__ import annotations

import importlib.util
import logging
import os
import sys
from unittest.mock import AsyncMock, MagicMock, patch

import pytest
from fastapi.testclient import TestClient
import pathlib

# ── Path: ensure backend/ is on sys.path ──────────────────────────────────────
BACKEND_DIR = pathlib.Path(__file__).parent.parent
if str(BACKEND_DIR) not in sys.path:
    sys.path.insert(0, str(BACKEND_DIR))


# ── Test client factory ───────────────────────────────────────────────────────
def make_app(db_reachable: bool = True):
    """
    Build a fresh app instance with a mocked Motor client.
    Imports server.py (real entry point) or falls back to main.py.
    """
    for mod_name in ["server", "main"]:
        if mod_name in sys.modules:
            del sys.modules[mod_name]

    os.environ["MONGO_URL"] = "mongodb://localhost:27017"
    os.environ["DB_NAME"] = "pharos_test"
    os.environ["ENVIRONMENT"] = "test"

    ping_mock = AsyncMock()
    if db_reachable:
        ping_mock.return_value = {"ok": 1}
    else:
        ping_mock.side_effect = Exception("Connection refused (mock)")

    mock_client = MagicMock()
    mock_client.admin.command = ping_mock
    mock_client.close = MagicMock()

    with patch("motor.motor_asyncio.AsyncIOMotorClient", return_value=mock_client):
        try:
            import server as srv
        except ModuleNotFoundError:
            import main as srv
        return srv.app, srv


# ── Tests: /health and /api/health ───────────────────────────────────────────
class TestHealthEndpoint:
    def test_health_200_db_reachable(self):
        """200 + db_ready=true when MongoDB ping succeeds."""
        app, _ = make_app(db_reachable=True)
        with TestClient(app) as client:
            resp = client.get("/health")
        assert resp.status_code == 200
        body = resp.json()
        assert body["status"] == "ok"
        assert body["db_ready"] is True

    def test_api_health_alias(self):
        """/api/health is a valid route alias."""
        app, _ = make_app(db_reachable=True)
        with TestClient(app) as client:
            resp = client.get("/api/health")
        assert resp.status_code == 200

    def test_health_200_db_unreachable(self):
        """
        PR #4 — safer startup:
        App must not crash when MongoDB is unreachable.
        /health returns 200 with db_ready=False (degraded mode, not hard failure).
        """
        app, _ = make_app(db_reachable=False)
        with TestClient(app) as client:
            resp = client.get("/health")
        assert resp.status_code == 200
        body = resp.json()
        assert body["status"] == "ok"
        assert body["db_ready"] is False

    def test_health_includes_environment(self):
        """Health response includes 'environment' field."""
        app, _ = make_app(db_reachable=True)
        with TestClient(app) as client:
            resp = client.get("/health")
        assert "environment" in resp.json()

    def test_health_includes_db_ready(self):
        """Health response includes 'db_ready' field (required by migration runbook)."""
        app, _ = make_app(db_reachable=True)
        with TestClient(app) as client:
            resp = client.get("/health")
        assert "db_ready" in resp.json()


# ── Tests: CORS ───────────────────────────────────────────────────────────────
class TestCORSHeaders:
    def test_cors_header_for_known_origin(self):
        """CORS allow-origin header present for a configured origin."""
        os.environ.setdefault("ALLOWED_ORIGINS", "http://localhost:3000")
        app, _ = make_app(db_reachable=True)
        with TestClient(app) as client:
            resp = client.get("/health", headers={"Origin": "http://localhost:3000"})
        assert "access-control-allow-origin" in resp.headers

    def test_preflight_ok(self):
        """OPTIONS preflight for a known origin returns 200 or 204."""
        os.environ.setdefault("ALLOWED_ORIGINS", "http://localhost:3000")
        app, _ = make_app(db_reachable=True)
        with TestClient(app) as client:
            resp = client.options(
                "/health",
                headers={
                    "Origin": "http://localhost:3000",
                    "Access-Control-Request-Method": "GET",
                },
            )
        assert resp.status_code in (200, 204)


# ── Tests: dnspython guard ────────────────────────────────────────────────────
class TestDnspythonGuard:
    def _load_guard(self):
        for m in ["server", "main"]:
            if m in sys.modules:
                del sys.modules[m]
        try:
            import server as srv
        except ModuleNotFoundError:
            import main as srv
        return srv._check_dnspython

    def test_guard_silent_standard_url(self, caplog):
        """No CRITICAL log for standard mongodb:// URL."""
        os.environ["MONGO_URL"] = "mongodb://localhost:27017"
        guard = self._load_guard()
        with caplog.at_level(logging.CRITICAL, logger="pharos"):
            guard()
        assert not any("dnspython" in r.message for r in caplog.records)

    def test_guard_critical_srv_url_no_dns(self, caplog):
        """CRITICAL log when mongodb+srv:// and importlib can't find dns."""
        os.environ["MONGO_URL"] = "mongodb+srv://u:p@cluster.mongodb.net/pharos"
        guard = self._load_guard()
        with patch("importlib.util.find_spec", return_value=None):
            with caplog.at_level(logging.CRITICAL, logger="pharos"):
                guard()
        assert any(
            "dnspython" in r.message and r.levelno == logging.CRITICAL
            for r in caplog.records
        )

    def test_guard_silent_srv_url_dns_installed(self, caplog):
        """No CRITICAL log when mongodb+srv:// but dns IS installed."""
        os.environ["MONGO_URL"] = "mongodb+srv://u:p@cluster.mongodb.net/pharos"
        guard = self._load_guard()
        with patch("importlib.util.find_spec", return_value=MagicMock()):
            with caplog.at_level(logging.CRITICAL, logger="pharos"):
                guard()
        assert not any(
            "dnspython" in r.message and r.levelno == logging.CRITICAL
            for r in caplog.records
        )


# ── Tests: requirements.txt integrity ────────────────────────────────────────
class TestRequirementsIntegrity:
    """Regression guards — fail CI if critical packages are removed."""

    @pytest.fixture
    def req_content(self):
        for candidate in [
            BACKEND_DIR / "requirements.txt",
            BACKEND_DIR.parent / "requirements.txt",
        ]:
            if candidate.exists():
                return candidate.read_text()
        pytest.skip("requirements.txt not found")

    def test_dnspython_present(self, req_content):
        """
        REGRESSION GUARD: dnspython must be in requirements.txt.
        Motor cannot connect to mongodb+srv:// without it (PR #4 P1 bug).
        """
        assert "dnspython" in req_content, (
            "\nCRITICAL: dnspython missing from requirements.txt.\n"
            "Motor raises ConfigurationError at startup without it.\n"
            "All DB-backed endpoints fail on Atlas. Add: dnspython==2.6.1"
        )

    def test_motor_present(self, req_content):
        assert "motor" in req_content, "motor (async MongoDB driver) must be in requirements.txt"

    def test_fastapi_present(self, req_content):
        assert "fastapi" in req_content

    def test_pydantic_present(self, req_content):
        assert "pydantic" in req_content

    def test_uvicorn_present(self, req_content):
        assert "uvicorn" in req_content
