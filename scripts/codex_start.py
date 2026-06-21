#!/usr/bin/env python3
"""Launch Codex with a startup token budget readout.

Default behavior:
  - read the active Codex model from ~/.codex/config.toml
  - print the model's context window and effective ceiling
  - start Codex with any forwarded arguments

Optional:
  --probe-status   run `codex exec '/status'` first and include the reported
                   `tokens used` value in the startup summary
  --status-only    print the summary and exit without launching Codex
"""

from __future__ import annotations

import argparse
import json
import os
import re
import subprocess
import sys
from pathlib import Path


def read_active_model(config_path: Path) -> str:
    try:
        import tomllib
    except ModuleNotFoundError as exc:  # pragma: no cover - Python 3.11+ expected
        raise RuntimeError("Python 3.11+ is required for tomllib support") from exc

    with config_path.open("rb") as handle:
        data = tomllib.load(handle)

    model = data.get("model")
    if not model:
        raise RuntimeError(f"Could not find a top-level 'model' entry in {config_path}")
    return str(model)


def fetch_model_limits(codex_bin: str, model: str) -> tuple[int, int, int]:
    raw = subprocess.check_output([codex_bin, "debug", "models"], text=True)
    payload = json.loads(raw)

    for entry in payload.get("models", []):
        if entry.get("slug") != model:
            continue

        context_window = int(entry["context_window"])
        effective_percent = int(entry.get("effective_context_window_percent", 100))
        effective_window = round(context_window * effective_percent / 100)
        return context_window, effective_percent, effective_window

    raise RuntimeError(f"Model {model!r} was not found in `codex debug models` output")


def probe_status_tokens(codex_bin: str) -> int | None:
    try:
        output = subprocess.check_output(
            [codex_bin, "exec", "/status"], stderr=subprocess.STDOUT, text=True
        )
    except subprocess.CalledProcessError as exc:
        output = exc.output or ""

    lines = [line.strip() for line in output.splitlines()]
    candidates: list[str] = []

    for index, line in enumerate(lines):
        lower = line.lower()
        if not lower.startswith("tokens used"):
            continue

        same_line = re.search(r"tokens used\D*([0-9][0-9,]*)", line, re.I)
        if same_line:
            candidates.append(same_line.group(1))
            continue

        if index + 1 < len(lines):
            next_line = re.search(r"([0-9][0-9,]*)", lines[index + 1])
            if next_line:
                candidates.append(next_line.group(1))

    if not candidates:
        return None

    return int(candidates[-1].replace(",", ""))


def format_int(value: int) -> str:
    return f"{value:,}"


def print_summary(
    model: str,
    context_window: int,
    effective_percent: int,
    effective_window: int,
    probe_tokens: int | None,
) -> None:
    print("Codex token budget", file=sys.stderr)
    print(f"  model: {model}", file=sys.stderr)
    print(f"  context window: {format_int(context_window)} tokens", file=sys.stderr)
    print(
        f"  effective ceiling: {format_int(effective_window)} tokens ({effective_percent}%)",
        file=sys.stderr,
    )

    if probe_tokens is None:
        print(
            "  exact remaining tokens: not exposed directly; use --probe-status for a fresh /status snapshot",
            file=sys.stderr,
        )
        return

    remaining = max(effective_window - probe_tokens, 0)
    print(f"  /status probe: {format_int(probe_tokens)} tokens used", file=sys.stderr)
    print(f"  estimated remaining after probe: {format_int(remaining)} tokens", file=sys.stderr)
    print(
        "  note: the probe is a separate Codex session, so this is a snapshot rather than the live run",
        file=sys.stderr,
    )


def should_register_codex_session(codex_args: list[str]) -> bool:
    """Return true for interactive/session launches, false for utility commands."""
    non_session_subcommands = {
        "debug",
        "exec",
        "mcp",
        "auth",
        "login",
        "logout",
        "completion",
        "sandbox",
    }
    skip_next = False
    for arg in codex_args:
        if skip_next:
            skip_next = False
            continue
        if arg in {"--model", "-m", "--config", "-c", "--cd", "-C", "--profile"}:
            skip_next = True
            continue
        if arg in {"--help", "-h", "--version", "-V"}:
            return False
        if arg.startswith("-"):
            continue
        return arg not in non_session_subcommands
    return True


def launch_switchboard_registration(codex_args: list[str]) -> None:
    """Start the remote-client switchboard registrar after any status probe."""
    if os.environ.get("IF_SWITCHBOARD_REGISTER_DISABLE") == "1":
        return
    if not should_register_codex_session(codex_args):
        return
    helper = Path.home() / ".local" / "bin" / "if-switchboard-register-session"
    if not helper.exists():
        return
    try:
        subprocess.Popen(
            [sys.executable, str(helper), "launch", "codex"],
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL,
            start_new_session=True,
        )
    except Exception:
        # Registration must never prevent Codex from starting.
        return


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Print a Codex token budget snapshot before launching Codex."
    )
    parser.add_argument(
        "--probe-status",
        action="store_true",
        help="Run `codex exec '/status'` first and include the reported `tokens used` value.",
    )
    parser.add_argument(
        "--status-only",
        action="store_true",
        help="Print the startup summary and exit without launching Codex.",
    )
    parser.add_argument(
        "--codex-bin",
        default=os.environ.get("CODEX_BIN", "codex"),
        help="Codex executable to run. Defaults to `codex` or CODEX_BIN.",
    )

    args, codex_args = parser.parse_known_args()

    config_path = Path.home() / ".codex" / "config.toml"
    model = read_active_model(config_path)
    context_window, effective_percent, effective_window = fetch_model_limits(
        args.codex_bin, model
    )
    probe_tokens = probe_status_tokens(args.codex_bin) if args.probe_status else None

    print_summary(model, context_window, effective_percent, effective_window, probe_tokens)

    if args.status_only:
        return 0

    launch_switchboard_registration(codex_args)
    os.execvp(args.codex_bin, [args.codex_bin, *codex_args])
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
