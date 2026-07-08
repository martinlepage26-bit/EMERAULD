"""Parse deadline text into structured deadline info."""

import re
from datetime import date, timedelta

WEEKDAY_NAMES = ["monday", "tuesday", "wednesday", "thursday", "friday", "saturday", "sunday"]

EVENT_PHRASES = [
    "before release", "before launch", "before deployment",
    "after approval", "after legal approval", "after review",
    "before submission", "after submission", "before go-live",
    "before merge", "after merge",
]


def parse_deadline(text: str) -> dict:
    """Return dict: deadline (ISO str|None), deadline_text, deadline_type, unresolved_questions."""
    if not text:
        return _none()

    t = text.strip()
    tl = t.lower()
    today = date.today()

    # Event-relative phrases — deadline is real but date unknown
    for phrase in EVENT_PHRASES:
        if phrase in tl:
            return {
                "deadline": None,
                "deadline_text": t,
                "deadline_type": "event_relative",
                "unresolved_questions": [f"What is the date for '{phrase}'?"],
            }

    # Explicit ISO date YYYY-MM-DD
    m = re.search(r'\b(\d{4}-\d{2}-\d{2})\b', t)
    if m:
        try:
            d = date.fromisoformat(m.group(1))
            return _explicit(d, t)
        except ValueError:
            pass

    # today / EOD / end of day
    if tl in ("today", "eod", "end of day", "by eod", "by today"):
        return _relative(today, t)

    # tomorrow
    if tl in ("tomorrow", "by tomorrow"):
        return _relative(today + timedelta(days=1), t)

    # end of week / eow → next Friday
    if "end of week" in tl or tl == "eow":
        days = (4 - today.weekday()) % 7 or 7
        return _relative(today + timedelta(days=days), t)

    # next week → next Monday
    if "next week" in tl:
        days = 7 - today.weekday()
        return _relative(today + timedelta(days=days), t)

    # this/next/by {weekday}
    for i, day in enumerate(WEEKDAY_NAMES):
        if f"next {day}" in tl or f"by {day}" in tl or f"this {day}" in tl:
            days = (i - today.weekday()) % 7 or 7
            return _relative(today + timedelta(days=days), t)

    return _none()


def _explicit(d: date, text: str) -> dict:
    return {"deadline": d.isoformat(), "deadline_text": text, "deadline_type": "explicit", "unresolved_questions": []}


def _relative(d: date, text: str) -> dict:
    return {"deadline": d.isoformat(), "deadline_text": text, "deadline_type": "relative", "unresolved_questions": []}


def _none() -> dict:
    return {"deadline": None, "deadline_text": "", "deadline_type": "none", "unresolved_questions": []}
