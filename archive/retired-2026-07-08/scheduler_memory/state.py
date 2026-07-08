"""Manage scheduler state files under .scheduler/"""

import json
from datetime import date, datetime, timedelta
from pathlib import Path


class SchedulerState:
    def __init__(self, vault_root: str):
        self.vault_root = vault_root
        self.scheduler_dir = Path(vault_root) / ".scheduler"
        self.scheduler_dir.mkdir(exist_ok=True)

        self.config_path = self.scheduler_dir / "config.json"
        self.state_path = self.scheduler_dir / "state.json"
        self.items_path = self.scheduler_dir / "items.json"
        self.events_path = self.scheduler_dir / "events.jsonl"

        self.config = self._load_config()
        self.state = self._load_state()
        self.items = self._load_items()

    # ------------------------------------------------------------------
    # Loading
    # ------------------------------------------------------------------

    def _load_config(self) -> dict:
        if self.config_path.exists():
            try:
                return json.loads(self.config_path.read_text())
            except (json.JSONDecodeError, OSError):
                pass
        default = {
            "stale_task_days": 4,
            "stale_branch_days": 7,
            "stale_uncommitted_hours": 24,
            "reminder_cooldown_hours": 24,
            "max_items_shown": 5,
        }
        self._write_json(self.config_path, default)
        return default

    def _load_state(self) -> dict:
        if self.state_path.exists():
            try:
                return json.loads(self.state_path.read_text())
            except (json.JSONDecodeError, OSError):
                pass
        return {"last_scan": None, "last_session_start": None}

    def _load_items(self) -> dict:
        """Returns items keyed by id."""
        if self.items_path.exists():
            try:
                data = json.loads(self.items_path.read_text())
                if isinstance(data, list):
                    return {item["id"]: item for item in data}
                if isinstance(data, dict):
                    return data
            except (json.JSONDecodeError, OSError):
                pass
        return {}

    # ------------------------------------------------------------------
    # Saving
    # ------------------------------------------------------------------

    def save(self):
        self._write_json(self.state_path, self.state)
        self._write_json(self.items_path, list(self.items.values()))

    def log_event(self, event_type: str, data: dict):
        entry = {"ts": datetime.now().isoformat(), "event": event_type, **data}
        with open(self.events_path, "a", encoding="utf-8") as f:
            f.write(json.dumps(entry) + "\n")

    @staticmethod
    def _write_json(path, obj):
        path.write_text(json.dumps(obj, indent=2, default=str), encoding="utf-8")

    # ------------------------------------------------------------------
    # Merging scan results
    # ------------------------------------------------------------------

    def merge_scan_results(self, scanned_items: list):
        """Merge freshly scanned items into the tracked items dict."""
        now = datetime.now().isoformat()
        scanned_ids = set()

        for item in scanned_items:
            item_id = item["id"]
            scanned_ids.add(item_id)

            if item_id in self.items:
                existing = self.items[item_id]
                existing["last_seen"] = now
                # Content changed → update last_changed
                if existing.get("source_quote") != item.get("source_quote"):
                    existing["last_changed"] = now
                    existing["source_quote"] = item["source_quote"]
                # Always refresh deadline (it may have been edited)
                if item.get("deadline_type", "none") != "none":
                    existing["deadline"] = item["deadline"]
                    existing["deadline_text"] = item["deadline_text"]
                    existing["deadline_type"] = item["deadline_type"]
                    existing["unresolved_questions"] = item.get("unresolved_questions", [])
            else:
                self.items[item_id] = item

    # ------------------------------------------------------------------
    # Surfacing
    # ------------------------------------------------------------------

    def get_due_items(self) -> list:
        """Return items that should appear in session-start output, sorted by urgency."""
        now = datetime.now()
        today = date.today()
        result = []

        for item in self.items.values():
            if item.get("dismissed") or item.get("status") == "dismissed":
                continue

            # Check snooze
            snoozed = item.get("snoozed_until")
            if snoozed:
                try:
                    if now < datetime.fromisoformat(snoozed):
                        continue
                except (ValueError, TypeError):
                    pass

            reason = self._surface_reason(item, now, today)
            if reason:
                copy = dict(item)
                copy["_surface_reason"] = reason
                result.append(copy)

        p_order = {"urgent": 0, "high": 1, "medium": 2, "low": 3}
        result.sort(key=lambda x: (
            p_order.get(x.get("priority", "low"), 3),
            x.get("deadline") or "9999-99-99",
        ))
        return result

    def _surface_reason(self, item: dict, now: datetime, today: date):
        """Return a reason string if the item should surface, otherwise None."""
        cooldown_h = self.config.get("reminder_cooldown_hours", 24)
        stale_days = self.config.get("stale_task_days", 4)
        priority = item.get("priority", "low")

        # Low-priority items respect cooldown — skip if seen recently
        last_seen = item.get("last_seen")
        if last_seen and priority == "low":
            try:
                age_h = (now - datetime.fromisoformat(last_seen)).total_seconds() / 3600
                if age_h < cooldown_h:
                    return None
            except (ValueError, TypeError):
                pass

        # Explicit deadline: overdue or due within 7 days
        deadline_str = item.get("deadline")
        if deadline_str:
            try:
                deadline = date.fromisoformat(deadline_str)
                days_left = (deadline - today).days
                if days_left < 0:
                    return f"OVERDUE by {-days_left}d"
                if days_left <= 7:
                    return f"due in {days_left}d"
            except (ValueError, TypeError):
                pass

        # Event-relative deadline on medium+ priority
        if item.get("deadline_type") == "event_relative" and priority in ("medium", "high", "urgent"):
            return "event-relative deadline unresolved"

        # Blocked items surface always
        quote = (item.get("source_quote") or "").lower()
        reason_text = (item.get("reminder_reason") or "").lower()
        if "#blocked" in quote or "blocked" in reason_text or priority == "urgent":
            return "blocked"

        # Stale tasks
        last_changed = item.get("last_changed")
        if last_changed and item.get("kind") in ("task", "code_todo", "tagged", "deadline"):
            try:
                age_days = (now - datetime.fromisoformat(last_changed)).days
                if age_days >= stale_days:
                    return f"stale ({age_days}d unchanged)"
            except (ValueError, TypeError):
                pass

        # Missing deadline on medium+ after ≥2 days active
        if item.get("deadline_type") == "missing" and priority in ("medium", "high", "urgent"):
            first_seen = item.get("first_seen")
            if first_seen:
                try:
                    age_days = (now - datetime.fromisoformat(first_seen)).days
                    if age_days >= 2:
                        return "missing deadline on active item"
                except (ValueError, TypeError):
                    pass

        return None

    # ------------------------------------------------------------------
    # Actions
    # ------------------------------------------------------------------

    def snooze(self, item_id: str, days: int) -> bool:
        if item_id not in self.items:
            return False
        until = (datetime.now() + timedelta(days=days)).isoformat()
        self.items[item_id]["snoozed_until"] = until
        self.items[item_id]["status"] = "snoozed"
        self.log_event("snooze", {"item_id": item_id, "days": days, "until": until})
        self.save()
        return True

    def dismiss(self, item_id: str, reason: str = "") -> bool:
        if item_id not in self.items:
            return False
        self.items[item_id]["dismissed"] = True
        self.items[item_id]["status"] = "dismissed"
        self.items[item_id]["dismiss_reason"] = reason
        self.log_event("dismiss", {"item_id": item_id, "reason": reason})
        self.save()
        return True

    def update_session_start(self):
        self.state["last_session_start"] = datetime.now().isoformat()
        self.log_event("session_start", {})

    def update_scan(self):
        self.state["last_scan"] = datetime.now().isoformat()
