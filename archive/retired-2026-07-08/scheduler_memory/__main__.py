"""Entry point: python -m scheduler_memory <command>"""

import argparse
import sys
from pathlib import Path

# Vault root is two levels up from this file:
# scheduler_memory/__main__.py → scheduler_memory/ → EMERAULD/
VAULT_ROOT = str(Path(__file__).resolve().parent.parent)


def _state():
    from .state import SchedulerState
    return SchedulerState(VAULT_ROOT)


# ------------------------------------------------------------------
# Commands
# ------------------------------------------------------------------

def cmd_scan(args):
    from .scanner import scan_vault
    from .state import SchedulerState

    state = SchedulerState(VAULT_ROOT)
    print(f"Scanning {VAULT_ROOT} ...")
    scanned = scan_vault(VAULT_ROOT)
    state.merge_scan_results(scanned)
    state.update_scan()
    state.save()

    active = [i for i in state.items.values() if not i.get("dismissed")]
    print(f"  Found {len(scanned)} raw items → {len(active)} active tracked items.")


def cmd_session_start(args):
    from .scanner import scan_vault
    from .state import SchedulerState
    from .reporter import print_session_start

    state = SchedulerState(VAULT_ROOT)
    scanned = scan_vault(VAULT_ROOT)
    state.merge_scan_results(scanned)
    state.update_scan()
    state.update_session_start()
    state.save()

    due = state.get_due_items()
    print_session_start(due)


def cmd_session_end(args):
    state = _state()
    state.log_event("session_end", {})
    state.save()
    print("Session end logged.")


def cmd_before_commit(args):
    from .scanner import scan_vault
    from .state import SchedulerState
    from .reporter import print_context

    state = SchedulerState(VAULT_ROOT)
    scanned = scan_vault(VAULT_ROOT)
    state.merge_scan_results(scanned)
    state.save()

    due = state.get_due_items()
    urgent = [i for i in due if i.get("priority") in ("high", "urgent")]
    if urgent:
        print_context(urgent)


def cmd_list(args):
    from .reporter import print_list
    state = _state()
    print_list(list(state.items.values()))


def cmd_context(args):
    from .reporter import print_context
    state = _state()
    due = state.get_due_items()
    print_context(due)


def cmd_snooze(args):
    state = _state()
    if state.snooze(args.item_id, args.days):
        print(f"Snoozed {args.item_id} for {args.days} day(s).")
    else:
        print(f"Item not found: {args.item_id}", file=sys.stderr)
        sys.exit(1)


def cmd_dismiss(args):
    state = _state()
    if state.dismiss(args.item_id, args.reason or ""):
        print(f"Dismissed {args.item_id}.")
    else:
        print(f"Item not found: {args.item_id}", file=sys.stderr)
        sys.exit(1)


def cmd_install_shell(args):
    from .installer import install_shell
    install_shell(force=getattr(args, "force", False))


def cmd_print_aliases(args):
    from .installer import print_aliases
    print_aliases()


def cmd_help(args):
    print("""
EMERAULD scheduler — deadline and stale work detection
======================================================

Usage:
  python -m scheduler_memory <command> [options]

Commands:
  scan            Scan the vault and update tracked items
  session-start   Scan + print reminder block (used by shell wrappers)
  session-end     Log session end
  before-commit   Print high-priority items before committing
  context         Print compact context block
  list            List all active tracked items
  snooze ITEM_ID --days N    Snooze an item for N days
  dismiss ITEM_ID --reason R Dismiss an item with a reason
  install-shell   Create cc-emerauld and codex-emerauld in ~/.local/bin/
  install-shell --force      Overwrite existing scripts
  print-aliases   Print recommended shell aliases

Shell wrappers (after install-shell):
  cc-emerauld     Run scheduler check, then launch Claude Code in EMERAULD
  codex-emerauld  Run scheduler check, then launch Codex in EMERAULD

Recommended aliases (add to ~/.bashrc):
  alias c='cc-emerauld'
  alias ce='cc-emerauld'
  alias cx='codex-emerauld'

State files (under .scheduler/):
  config.json     Thresholds (stale days, cooldown hours, etc.)
  state.json      Last scan / session timestamps
  items.json      All tracked items
  events.jsonl    Append-only event log
""")


# ------------------------------------------------------------------
# CLI
# ------------------------------------------------------------------

def main():
    parser = argparse.ArgumentParser(
        prog="python -m scheduler_memory",
        description="EMERAULD vault scheduler",
        add_help=False,
    )
    sub = parser.add_subparsers(dest="command")

    sub.add_parser("scan")
    sub.add_parser("session-start")
    sub.add_parser("session-end")
    sub.add_parser("before-commit")
    sub.add_parser("list")
    sub.add_parser("context")

    p_snooze = sub.add_parser("snooze")
    p_snooze.add_argument("item_id")
    p_snooze.add_argument("--days", type=int, default=1)

    p_dismiss = sub.add_parser("dismiss")
    p_dismiss.add_argument("item_id")
    p_dismiss.add_argument("--reason", default="")

    p_install = sub.add_parser("install-shell")
    p_install.add_argument("--force", action="store_true")

    sub.add_parser("print-aliases")
    sub.add_parser("help")

    args = parser.parse_args()

    if args.command is None:
        cmd_help(args)
        return

    dispatch = {
        "scan": cmd_scan,
        "session-start": cmd_session_start,
        "session-end": cmd_session_end,
        "before-commit": cmd_before_commit,
        "list": cmd_list,
        "context": cmd_context,
        "snooze": cmd_snooze,
        "dismiss": cmd_dismiss,
        "install-shell": cmd_install_shell,
        "print-aliases": cmd_print_aliases,
        "help": cmd_help,
    }

    fn = dispatch.get(args.command)
    if fn:
        fn(args)
    else:
        parser.print_help()


if __name__ == "__main__":
    main()
