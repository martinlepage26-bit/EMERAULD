"""Format and print scheduler output to the terminal."""

from datetime import date


def print_session_start(due_items: list):
    """Print the session-start reminder block. Silent if nothing important."""
    if not due_items:
        # Completely quiet when nothing is due
        return

    overdue = [i for i in due_items if "OVERDUE" in i.get("_surface_reason", "")]
    due_soon = [i for i in due_items if "due in" in i.get("_surface_reason", "")]
    blocked = [i for i in due_items if "blocked" in i.get("_surface_reason", "")]
    stale = [i for i in due_items if "stale" in i.get("_surface_reason", "")]
    missing = [i for i in due_items if "missing deadline" in i.get("_surface_reason", "")]
    other = [
        i for i in due_items
        if i not in overdue and i not in due_soon and i not in blocked
        and i not in stale and i not in missing
    ]

    lines = ["", "EMERAULD scheduler check:"]
    if overdue:
        lines.append(f"  - {len(overdue)} overdue")
    if due_soon:
        lines.append(f"  - {len(due_soon)} due soon")
    if blocked:
        lines.append(f"  - {len(blocked)} blocked")
    if stale:
        lines.append(f"  - {len(stale)} stale")
    if missing:
        lines.append(f"  - {len(missing)} need a deadline")
    if other:
        lines.append(f"  - {len(other)} other")

    lines.append("")
    lines.append("Suggested focus:")

    max_show = 5
    for idx, item in enumerate(due_items[:max_show], 1):
        reason = item.get("_surface_reason", "")
        title = item.get("title", "")[:65]
        source = item.get("source_path", "")
        action = item.get("suggested_next_action", "Review this item.")

        lines.append(f"  {idx}. [{reason}] {title}")
        if source:
            lines.append(f"     {source}:{item.get('source_line', '')}")
        lines.append(f"     → {action}")

    if len(due_items) > max_show:
        lines.append(f"  ... +{len(due_items) - max_show} more")
        lines.append("  Run: python -m scheduler_memory list")

    lines.append("")
    print("\n".join(lines))


def print_list(items: list):
    """Print all active items in detail."""
    active = [i for i in items if not i.get("dismissed") and i.get("status") != "dismissed"]

    if not active:
        print("No active items.")
        return

    today = date.today()
    print(f"\n{len(active)} active items:\n")

    for item in active:
        status_parts = []
        snoozed = item.get("snoozed_until")
        if snoozed:
            status_parts.append(f"snoozed until {snoozed[:10]}")
        dl = item.get("deadline")
        if dl:
            try:
                days_left = (date.fromisoformat(dl) - today).days
                tag = f"OVERDUE {-days_left}d" if days_left < 0 else f"due {days_left}d ({dl})"
                status_parts.append(tag)
            except ValueError:
                pass

        status_str = f"  [{', '.join(status_parts)}]" if status_parts else ""
        title = item["title"][:70]
        print(f"  [{item['id']}] {title}{status_str}")
        print(f"    kind={item['kind']}  priority={item['priority']}  confidence={item['confidence']}")
        print(f"    {item['source_path']}:{item['source_line']}")
        if item.get("reminder_reason"):
            print(f"    reason: {item['reminder_reason']}")
        if item.get("suggested_next_action"):
            print(f"    → {item['suggested_next_action']}")
        print()


def print_context(due_items: list):
    """Compact context block for embedding in prompts or before-commit check."""
    if not due_items:
        return
    print("=== EMERAULD scheduler ===")
    for item in due_items[:10]:
        reason = item.get("_surface_reason", "")
        title = item.get("title", "")[:60]
        source = item.get("source_path", "")
        print(f"  [{reason}] {title}  ({source}:{item.get('source_line','')})")
    print("==========================\n")
