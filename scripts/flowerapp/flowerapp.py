#!/usr/bin/env python3
"""
FLOWERAPP / IRCM CLI — Individual Data Intake & Analysis Protocol
Single-file CLI (phone-first, desktop-compatible).

Core guarantees (non-negotiable):
- Visuals never stand alone.
- Text never stands without data.
- Data never stands without constraints.
- Symbolic inputs generate questions, not answers.
- Media is archived verbatim (copied, not edited).
- Tier A shapes scores. Tier B modifies. Tier C is meaning-layer only.

Equation lock:
  Agency (/100) = perceptual_latitude (0-25)
                + regulatory_bandwidth (0-25)
                + resource_access (0-25)
                + social_legibility (0-25)

Outputs (mandatory):
- reports/ircm_summary.txt
- reports/ircm_report.txt
- reports/ircm_tables.csv
- reports/ircm_metadata.json
Optional:
- visuals/*.png (10 modes) if matplotlib is installed.

Phone-first UX:
- All commands default to --project . (current folder).
- Short aliases: new, view, ev, media, go, events, ls-ev, list+, bulkimport.

Authoring note: accountable pipeline, not predictive engine.
"""

from __future__ import annotations

import argparse
import csv
import json
import re
import shutil
import unicodedata
from datetime import datetime
from pathlib import Path
from typing import Any, Dict, List, Optional, Tuple

# ----------------------------
# Constants
# ----------------------------

IRCM_VERSION = "FLOWERAPP-1.0"
DATASTORE_NAME = "ircm.json"

RECURRENCE_OPERATORS = [
    "Abandonment", "Silencing", "Bodily invisibility", "Conditional protection",
    "Humiliation", "Extraction", "Escape", "Boundary assertion",
]

OPERATOR_HINTS: Dict[str, List[str]] = {
    "Abandonment": ["#abandonment", "#leftalone", "#noone", "#ghosting", "#withdrawal",
                    "abandon", "left alone", "no one", "ghost", "withdraw"],
    "Silencing": ["#silenced", "#interrupted", "#shut_down", "#cut_off", "#not_allowed",
                  "silence", "stopped", "interrupted", "cut off", "not allowed to speak"],
    "Bodily invisibility": ["#pain", "#injury", "#sick", "#ignored_body", "#invisible",
                            "injury", "hurt", "pain", "sick", "ignored", "invisible"],
    "Conditional protection": ["#only_if", "#unless", "#conditional", "#compliance", "#rewarded",
                               "only if", "unless", "condition", "compliance", "rewarded"],
    "Humiliation": ["#humiliated", "#mocked", "#ridiculed", "#laughed_at", "#shame",
                    "humiliated", "laughed", "mocked", "ridicule", "shame"],
    "Extraction": ["#used", "#exploited", "#unpaid", "#undervalued", "#over_and_over",
                   "used", "exploited", "unpaid", "over and over", "undervalued"],
    "Escape": ["#escape", "#ran", "#fled", "#avoidance", "#got_away",
               "escaped", "fled", "got away", "avoid"],
    "Boundary assertion": ["#refused", "#boundary", "#stopped", "#left", "#broke_it_off",
                           "refused", "broke it off", "boundary"],
}

DEFAULT_DOMAINS = [
    "Family", "School", "Institution", "Work", "Health", "Relationships",
    "Creative", "Community", "Finance", "Spiritual/Symbolic", "Other",
]

COST_TYPES = ["economic", "bodily", "relational", "temporal", "reputational", "legal", "other"]

VIS_MODES = [
    ("VIZ-01", "Operator Distribution", "operator_distribution.png"),
    ("VIZ-02", "Temporal Timeline", "timeline.png"),
    ("VIZ-03", "Recurrence Loop Occurrences", "recurrence_loops.png"),
    ("VIZ-04", "Constraint Signatures Radar", "constraint_radar.png"),
    ("VIZ-05", "Convergence Audit", "convergence_audit.png"),
    ("VIZ-06", "Cost Accumulation", "cost_accumulation.png"),
    ("VIZ-07", "Collapse Frequency", "collapse_frequency.png"),
    ("VIZ-08", "Domain Distribution", "domain_distribution.png"),
    ("VIZ-09", "Subscore Snapshot", "subscores.png"),
    ("VIZ-10", "Loop vs Signature Scatter", "scatter_signal.png"),
]

DEFAULT_TIER_A_CAP = 19  # caps a 0-25 sub-score when Tier A active without buffer evidence

# ----------------------------
# Helpers
# ----------------------------

def now_iso() -> str:
    return datetime.now().isoformat(timespec="seconds")

def ensure_dir(p: Path) -> None:
    p.mkdir(parents=True, exist_ok=True)

def read_json(p: Path) -> Dict[str, Any]:
    if not p.exists():
        return {}
    try:
        return json.loads(p.read_text(encoding="utf-8"))
    except json.JSONDecodeError as e:
        raise SystemExit(
            f"Datastore JSON is corrupted:\n  {p}\n  {e}\n"
            f"Fix the JSON or re-init."
        )

def write_json(p: Path, data: Dict[str, Any]) -> None:
    ensure_dir(p.parent)
    p.write_text(json.dumps(data, indent=2, ensure_ascii=False), encoding="utf-8")

def safe_copy(src: Path, dst: Path) -> None:
    ensure_dir(dst.parent)
    shutil.copy2(str(src), str(dst))

def parse_int(s: str) -> Optional[int]:
    try:
        return int(s)
    except Exception:
        return None

def parse_date(s: str) -> Optional[str]:
    if re.match(r"^\d{4}-\d{2}-\d{2}$", s.strip()):
        return s.strip()
    return None

def has_matplotlib() -> bool:
    try:
        import matplotlib  # noqa: F401
        return True
    except Exception:
        return False

def project_paths(project_dir: Path) -> Dict[str, Path]:
    return {
        "root": project_dir,
        "datastore": project_dir / DATASTORE_NAME,
        "media": project_dir / "media",
        "media_handwriting": project_dir / "media" / "handwriting",
        "media_drawings": project_dir / "media" / "drawings",
        "reports": project_dir / "reports",
        "visuals": project_dir / "visuals",
        "data": project_dir / "data",
    }

def _norm_text(s: str) -> str:
    """Normalize text for keyword matching: lowercase, strip diacritics, collapse punctuation."""
    if not s:
        return ""
    # Strip diacritics
    s = unicodedata.normalize("NFKD", s)
    s = "".join(ch for ch in s if not unicodedata.combining(ch))
    s = s.lower().replace("_", " ").replace("#", " ")
    s = re.sub(r"[^a-z0-9\s]+", " ", s)
    s = re.sub(r"\s+", " ", s).strip()
    return s

# ----------------------------
# Numerology (Tier C, bounded)
# ----------------------------

PYTHAGOREAN_MAP = {
    **{c: 1 for c in "AJS"}, **{c: 2 for c in "BKT"}, **{c: 3 for c in "CLU"},
    **{c: 4 for c in "DMV"}, **{c: 5 for c in "ENW"}, **{c: 6 for c in "FOX"},
    **{c: 7 for c in "GPY"}, **{c: 8 for c in "HQZ"}, **{c: 9 for c in "IR"},
}
VOWELS_DEFAULT = set("AEIOU")  # Y consonant by default

def _digits(n: int) -> List[int]:
    return [int(ch) for ch in str(n) if ch.isdigit()]

def reduce_number(n: int, keep_masters: bool = True) -> int:
    while True:
        if keep_masters and n in (11, 22, 33):
            return n
        if n < 10:
            return n
        n = sum(_digits(n))

def normalize_name(name: str) -> str:
    """Unicode-normalize: convert é→E, etc., then keep A-Z only."""
    n = unicodedata.normalize("NFKD", name)
    n = "".join(ch for ch in n if not unicodedata.combining(ch))
    return re.sub(r"[^A-Za-z]", "", n).upper()

def numerology_grid(name: str, y_as_vowel: bool = False) -> List[Tuple[str, int, str]]:
    vowels = VOWELS_DEFAULT | ({"Y"} if y_as_vowel else set())
    cleaned = normalize_name(name)
    return [(ch, PYTHAGOREAN_MAP.get(ch, 0), "vowel" if ch in vowels else "consonant")
            for ch in cleaned]

def numerology_name_sums(name: str, y_as_vowel: bool = False) -> Dict[str, Any]:
    grid = numerology_grid(name, y_as_vowel)
    total = sum(v for _, v, _ in grid)
    vsum = sum(v for _, v, k in grid if k == "vowel")
    csum = sum(v for _, v, k in grid if k == "consonant")
    return {
        "grid": grid,
        "expression_raw": total, "expression": reduce_number(total),
        "hearts_desire_raw": vsum, "hearts_desire": reduce_number(vsum),
        "personality_raw": csum, "personality": reduce_number(csum),
    }

def numerology_life_path(dob: str) -> Dict[str, Any]:
    digits = [int(d) for d in re.sub(r"[^0-9]", "", dob)]
    raw = sum(digits)
    steps = [raw]
    cur = raw
    while cur >= 10 and cur not in (11, 22, 33):
        cur = sum(_digits(cur))
        steps.append(cur)
    return {"digits": digits, "raw": raw, "steps": steps, "life_path": cur}

def numerology_maturity(life_path: int, expression: int) -> Dict[str, Any]:
    raw = life_path + expression
    return {"raw": raw, "maturity": reduce_number(raw)}

# ----------------------------
# Iris symbolic (questions only)
# ----------------------------

def iris_questions_from_descriptors(desc: Dict[str, Any]) -> List[str]:
    """Symbolic prompts only. No medical, no diagnostic claims."""
    rings = (desc.get("rings") or "").strip().lower()
    flecks = (desc.get("flecks") or "").strip().lower()
    asym = (desc.get("asymmetry") or "").strip().lower()
    clarity = (desc.get("clarity") or "").strip().lower()
    notes = (desc.get("notes") or "").strip()

    qs: List[str] = []
    qs.append("What did you want to be seen as in that period, and what did you fear would be seen instead?")
    qs.append("Where do you over-control interpretation because uncertainty feels unsafe?")
    if rings:
        qs.append(f"Rings noted ('{rings}'): what patterns repeat when pressure rises?")
    if flecks:
        qs.append(f"Flecks noted ('{flecks}'): which details do you hide because they don't fit your clean narrative?")
    if asym:
        qs.append(f"Asymmetry noted ('{asym}'): where are public capacities not matched by private regulation?")
    if clarity:
        qs.append(f"Clarity noted ('{clarity}'): when clarity spikes during isolation/urgency, what checks do you skip?")
    if notes:
        qs.append("Notes present: what would disconfirm what you're trying to convince yourself of?")
    qs.append("What would count as external disconfirmation of your current interpretation?")
    qs.append("Which 3 independent lenses could validate or falsify this framing within 30 days?")
    return qs

# ----------------------------
# Datastore Schema
# ----------------------------

def new_datastore() -> Dict[str, Any]:
    return {
        "meta": {
            "ircm_version": IRCM_VERSION,
            "created_at": now_iso(),
            "updated_at": now_iso(),
        },
        "inputs": {
            "identity_symbolic": {
                "full_legal_name_birth": "",
                "name_variations": [],
                "mother_full_name": "",
                "father_full_name": "",
                "ancestry_migration_lineages": "",
            },
            "temporal_spatial": {
                "birth_date": "",
                "birth_time": "",
                "time_accuracy": "",  # exact / estimated
                "birth_place": "",
                "birth_circumstances": "",
            },
            "demographics_constraints": {
                "age_range": "",
                "current_location": "",
                "languages": [],
                "education_level": "",
                "work_situation": "",
                "economic_stability": "",  # stable/volatile/precarious
                "health_constraints": "",
                "recovery_support_structures": "",
                "care_obligations": "",
                "tools_infrastructure": "",
            },
            "lived_trajectory": {"events": []},
            "visual_material_trace_archive": {
                "handwriting": [], "drawings": [],
                "archival_rules_ack": True,
                "isolation_threshold_days": None,
            },
            "cultural_aesthetic_practice": {
                "films_tv": [], "books_authors_theory": [],
                "music_sound": [], "practices_hobbies": [],
            },
            "blindspots_distortions": {
                "known_blindspots": {"patterns_after_fact": "", "feedback_resisted": "", "motive_reading_unreliable": ""},
                "situational_blindspots": {"exhaustion": "", "praise": "", "rejection": "", "urgency": "", "isolation": "", "authority_pressure": "", "moral_certainty": ""},
                "narrative_distortions": {"roles_overidentified": "", "protective_stories": "", "quick_explanations": ""},
                "avoided_data": {"domains_resisted": "", "questions_disliked": "", "metrics_avoided": ""},
                "external_correctives": {"people_practices": "", "signals_trusted": ""},
            },
            "avoidance_of_isolation": {
                "risk_profile": {"conditions": "", "typical_duration_intensity": "", "early_warning_signals": ""},
                "functional_impact": {"increases": "", "degrades": ""},
                "counterweights": {"min_contacts": "", "cadence": "", "mode": "", "allowed_challenges": ""},
                "hard_stop_rules": "",
            },
            "convergence_check": {
                "lenses_selected": [],
                "convergence_criteria_ack": True,
                "divergence_handling_ack": True,
                "anti_prophecy": {"claims_refused": "", "inflationary_language_flagged": ""},
            },
            "symbolic_layer_optional": {
                "sky_chart": {"sun": "", "moon": "", "rising": "", "notes_questions_only": ""},
                "human_design": {"type": "", "authority": "", "profile": "", "notes_questions_only": ""},
                "other_symbolic_systems": [],
                "rule_questions_not_answers_ack": True,
                "iris_symbolic": {
                    "enabled": False,
                    "rule_questions_not_answers_ack": True,
                    "source": {"method": "", "photo_paths": [], "observer": "", "date": ""},
                    "descriptors": {"eye_color": "", "rings": "", "flecks": "", "asymmetry": "", "clarity": "", "notes": ""},
                },
                "numerology": {
                    "enabled": False,
                    "y_as_vowel": False,
                    "rule_questions_not_answers_ack": True,
                },
            },
            "scoring": {
                "raw_subscores": {
                    "perceptual_latitude": 0, "regulatory_bandwidth": 0,
                    "resource_access": 0, "social_legibility": 0,
                },
                "buffer_evidence": {
                    "perceptual_latitude": False, "regulatory_bandwidth": False,
                    "resource_access": False, "social_legibility": False,
                },
                "tierA_active": False,
            },
            "keyword_bank": {
                "recurrence_operators": [
                    "#abandonment #leftalone #withdrawal #ghosting #unreachable #noonecame #discarded",
                    "#silencing #interrupted #talkingover #shutdown #ndas #threatened",
                    "#bodilyinvisibility #painignored #symptomsdismissed #medicalgaslighting",
                    "#conditionalprotection #onlyif #compliance #stringsattached #conditionalcare",
                    "#humiliation #mocked #ridiculed #shamed #publicembarrassment #scapegoated",
                    "#extraction #used #exploited #unpaid #freework #emotionallabor #creditstolen",
                    "#escape #fled #avoided #disappeared #movedaway #quitfast",
                    "#boundaryassertion #refused #saidno #walkedout #blocked #cutcontact",
                ],
                "cost_types": [
                    "#economic #moneyloss #debt #jobloss #unpaid #financialpanic",
                    "#bodily #sleepdebt #pain #injury #illness #fatigue #somaticcrash",
                    "#relational #breakup #estrangement #trustloss #isolation #loneliness",
                    "#temporal #wastedtime #delay #stalledprojects #recoverytime",
                    "#reputational #shame #credibilityhit #blacklisted #statusloss",
                    "#legal #contractrisk #court #papertrail #compliancepressure",
                    "#other #valuesviolation #moralinjury #identitystrain #meaningcollapse",
                ],
                "isolation_signals": [
                    "#withdrawing #cancelingplans #notreplying #unreachable #stayinghome",
                    "#sleepflip #insomnia #hypersomnia #neglectinghygiene",
                    "#rumination #doomscrolling #catastrophizing #certaintyspike",
                    "#impulsivity #urgentdecisions #burnbridges #spendingspree #relapsetrigger",
                    "#irritability #shameflood #numbness #dissociation",
                    "#grandplans #allornothing #hyperfocus #overwork",
                    "#noexternalcheck #avoidfeedback #secrecy #refusinghelp #isolatedcertainty",
                ],
            },
        },
        "analysis": {
            "phase_iv_recurrence_loops": [],
            "phase_v_constraint_signatures": [],
            "phase_vi_purposes": [],
            "convergence_audit_log": [],
            "agency_score": None,
            "subscores_capped": {},
            "caps_applied": [],
            "numerology_outputs": {},
            "collapse_stats": {
                "burnout_episodes": 0, "relapse_episodes": 0,
                "institutional_ruptures": 0, "isolation_periods": 0,
            },
        },
        "exports": {"last_run_at": "", "outputs": {}},
    }

# ----------------------------
# Event matching
# ----------------------------

def next_id(prefix: str, existing: List[Dict[str, Any]]) -> str:
    nums = []
    for item in existing:
        m = re.match(rf"^{re.escape(prefix)}-(\d+)$", str(item.get("id", "")))
        if m:
            nums.append(int(m.group(1)))
    return f"{prefix}-{(max(nums) + 1 if nums else 1):03d}"

def event_operator_hints(text: str) -> List[str]:
    """Match operators in text using normalized hashtags + word boundaries for short tokens."""
    t = _norm_text(text)
    hits: List[str] = []
    for op, keys in OPERATOR_HINTS.items():
        for k in keys:
            kk = _norm_text(k)
            if not kk:
                continue
            if " " in kk:
                if kk in t:
                    hits.append(op); break
            else:
                if re.search(rf"\b{re.escape(kk)}\b", t):
                    hits.append(op); break
    return sorted(set(hits))

# ----------------------------
# CLI commands
# ----------------------------

def cmd_init(args: argparse.Namespace) -> None:
    project_dir = Path(args.project).resolve()
    paths = project_paths(project_dir)
    for k in ("root", "reports", "visuals", "media_handwriting", "media_drawings", "data"):
        ensure_dir(paths[k])

    ds_path = paths["datastore"]
    if ds_path.exists() and not args.force:
        raise SystemExit(f"Project exists at {project_dir}. Use --force to overwrite.")

    ds = new_datastore()
    if args.isolation_threshold_days is not None:
        ds["inputs"]["visual_material_trace_archive"]["isolation_threshold_days"] = int(args.isolation_threshold_days)
    write_json(ds_path, ds)
    print(f"Initialized FLOWERAPP project: {project_dir}")
    print(f"Datastore: {ds_path}")

def cmd_show(args: argparse.Namespace) -> None:
    ds = read_json(project_paths(Path(args.project).resolve())["datastore"])
    if not ds:
        raise SystemExit("No datastore. Run `init` first.")
    print(json.dumps(ds["inputs"], indent=2, ensure_ascii=False))

def _set_nested(ds: Dict[str, Any], path: str, value: Any) -> None:
    keys = path.strip().split(".")
    cur: Any = ds
    for k in keys[:-1]:
        if k not in cur or not isinstance(cur[k], dict):
            raise SystemExit(f"Path segment not found or not a dict: {k}")
        cur = cur[k]
    leaf = keys[-1]
    cur[leaf] = value

def cmd_set(args: argparse.Namespace) -> None:
    ds_path = project_paths(Path(args.project).resolve())["datastore"]
    ds = read_json(ds_path)
    if not ds:
        raise SystemExit("No datastore. Run `init` first.")
    if "=" not in args.kv:
        raise SystemExit("Use: --kv path.to.field=value")
    path, value = args.kv.split("=", 1)
    v: Any = value
    if value.strip().lower() in ("true", "false"):
        v = (value.strip().lower() == "true")
    elif re.match(r"^-?\d+$", value.strip()):
        v = int(value.strip())
    _set_nested(ds, path, v)
    ds["meta"]["updated_at"] = now_iso()
    write_json(ds_path, ds)
    print(f"Set {path} = {v}")

def cmd_add_list_item(args: argparse.Namespace) -> None:
    ds_path = project_paths(Path(args.project).resolve())["datastore"]
    ds = read_json(ds_path)
    if not ds:
        raise SystemExit("No datastore. Run `init` first.")
    keys = args.path.strip().split(".")
    cur: Any = ds
    for k in keys[:-1]:
        if k not in cur or not isinstance(cur[k], dict):
            raise SystemExit(f"Path not found: {k}")
        cur = cur[k]
    leaf = keys[-1]
    if leaf not in cur or not isinstance(cur[leaf], list):
        raise SystemExit("Target must be a list.")
    cur[leaf].append(args.item)
    ds["meta"]["updated_at"] = now_iso()
    write_json(ds_path, ds)
    print(f"Added to {args.path}: {args.item}")

def _prompt(label: str) -> str:
    while True:
        val = input(f"{label}: ").strip()
        if val:
            return val
        print("  (required — please enter a value)")

def _prompt_domain() -> str:
    print("Domain:")
    for i, d in enumerate(DEFAULT_DOMAINS, 1):
        print(f"  {i}. {d}")
    while True:
        raw = input("  Enter number or name: ").strip()
        if raw.isdigit() and 1 <= int(raw) <= len(DEFAULT_DOMAINS):
            return DEFAULT_DOMAINS[int(raw) - 1]
        if raw in DEFAULT_DOMAINS:
            return raw
        print("  Not recognized — try again.")

def _prompt_operators() -> str:
    print("Operators (comma-separated numbers or names, or blank to skip):")
    for i, o in enumerate(RECURRENCE_OPERATORS, 1):
        print(f"  {i}. {o}")
    raw = input("  > ").strip()
    if not raw:
        return ""
    parts = [p.strip() for p in raw.split(",") if p.strip()]
    chosen = []
    for p in parts:
        if p.isdigit() and 1 <= int(p) <= len(RECURRENCE_OPERATORS):
            chosen.append(RECURRENCE_OPERATORS[int(p) - 1])
        elif p in RECURRENCE_OPERATORS:
            chosen.append(p)
    return ",".join(chosen)

def cmd_add_event(args: argparse.Namespace) -> None:
    ds_path = project_paths(Path(args.project).resolve())["datastore"]
    ds = read_json(ds_path)
    if not ds:
        raise SystemExit("No datastore. Run `init` first.")

    if args.domain is None:
        args.domain = _prompt_domain()
    if not args.operators:
        args.operators = _prompt_operators()
    if args.what is None:
        args.what = _prompt("What happened")
    if args.why is None:
        args.why = _prompt("Why significant")
    if args.cost is None:
        args.cost = _prompt("Cost")
    if args.gain is None:
        args.gain = _prompt("Gain")

    events: List[Dict[str, Any]] = ds["inputs"]["lived_trajectory"]["events"]
    eid = next_id("EV", events)
    date_iso = parse_date(args.date) if args.date else None
    age_years = parse_int(args.age) if args.age else None
    ops = [o.strip() for o in (args.operators or "").split(",") if o.strip()]

    if args.add_hints:
        for h in event_operator_hints(" ".join([args.what, args.why, args.cost, args.gain])):
            if h not in ops:
                ops.append(h)

    unknown = [o for o in ops if o not in RECURRENCE_OPERATORS]
    if unknown:
        raise SystemExit(f"Unknown operators: {unknown}\nAllowed: {RECURRENCE_OPERATORS}")

    events.append({
        "id": eid, "created_at": now_iso(),
        "date_iso": date_iso or "", "age_years": age_years if age_years is not None else "",
        "domain": args.domain, "what_happened": args.what, "why_significant": args.why,
        "cost": args.cost, "gain": args.gain,
        "recurrence_operators": ops, "linkage": args.linkage or "",
        "notes": args.notes or "",
    })
    ds["meta"]["updated_at"] = now_iso()
    write_json(ds_path, ds)
    print(f"Added event {eid}")

def cmd_list_events(args: argparse.Namespace) -> None:
    ds = read_json(project_paths(Path(args.project).resolve())["datastore"])
    events = ds.get("inputs", {}).get("lived_trajectory", {}).get("events", [])
    if not events:
        print("No events.")
        return
    def key(ev):
        di = ev.get("date_iso") or "9999-99-99"
        ay = ev.get("age_years")
        ay2 = int(ay) if isinstance(ay, int) or (isinstance(ay, str) and str(ay).isdigit()) else 9999
        return (di, ay2, ev.get("created_at", ""))
    for ev in sorted(events, key=key):
        print(f"{ev['id']} | date={ev.get('date_iso','')} age={ev.get('age_years','')} | {ev.get('domain','')} | ops={ev.get('recurrence_operators',[])}")
        print(f"  what: {ev.get('what_happened','')[:120]}")

def cmd_add_media(args: argparse.Namespace) -> None:
    paths = project_paths(Path(args.project).resolve())
    ds = read_json(paths["datastore"])
    if not ds:
        raise SystemExit("No datastore. Run `init` first.")

    src = Path(args.file).expanduser().resolve()
    if not src.exists():
        raise SystemExit(f"File not found: {src}")
    kind = args.kind.lower().strip()
    if kind not in ("handwriting", "drawing"):
        raise SystemExit("kind must be: handwriting or drawing")

    archive_list = ds["inputs"]["visual_material_trace_archive"]["handwriting" if kind == "handwriting" else "drawings"]
    mid = next_id("HW" if kind == "handwriting" else "DR", archive_list)
    ts = datetime.now().strftime("%Y%m%d_%H%M%S")
    dst = (paths["media_handwriting"] if kind == "handwriting" else paths["media_drawings"]) / f"{mid}_{ts}{src.suffix.lower()}"
    safe_copy(src, dst)

    archive_list.append({
        "id": mid, "created_at": now_iso(),
        "source_file": str(src), "archived_file": str(dst),
        "approx_date": args.approx_date or "", "context": args.context or "",
        "medium": args.medium or "", "duration_minutes": args.duration_minutes or "",
        "made_alone": bool(args.made_alone) if kind == "drawing" else "",
        "made_with_others": bool(args.made_with_others) if kind == "drawing" else "",
        "made_during_isolation": bool(args.made_during_isolation) if kind == "drawing" else "",
        "preceded_written_explanation": bool(args.preceded_written_explanation) if kind == "drawing" else "",
        "followed_written_explanation": bool(args.followed_written_explanation) if kind == "drawing" else "",
        "notes": args.notes or "",
    })
    ds["meta"]["updated_at"] = now_iso()
    write_json(paths["datastore"], ds)
    print(f"Archived {kind} as {mid} -> {dst}")

# ----------------------------
# Bulk import
# ----------------------------

_SEP_LINE_RE = re.compile(r"^\s*([-—_]){6,}\s*$")

def _infer_approxdate(text: str) -> str:
    m = re.search(r"\b(19|20)\d{2}\b", text)
    if m:
        return m.group(0)
    m2 = re.search(r"\b(age|aged)\s+(\d{1,2})\b", text, flags=re.IGNORECASE)
    return f"age {m2.group(2)}" if m2 else ""

def _infer_age(text: str) -> str:
    t = text.lower()
    m = re.search(r"\bage\s+(\d{1,2})\b", t)
    if m: return m.group(1)
    m = re.search(r"\b(\d{1,2})\s*(yo|y/o|years old)\b", t)
    return m.group(1) if m else ""

def _text_to_event_blocks(raw_text: str) -> List[str]:
    blocks: List[List[str]] = []
    cur: List[str] = []
    for line in raw_text.splitlines():
        if _SEP_LINE_RE.match(line):
            if any(x.strip() for x in cur):
                blocks.append(cur)
            cur = []
        else:
            cur.append(line)
    if any(x.strip() for x in cur):
        blocks.append(cur)
    return ["\n".join(b).strip() for b in blocks if "\n".join(b).strip()]

def _block_to_event(block: str, sequence: int) -> Dict[str, Any]:
    first_line = block.splitlines()[0].strip()
    incident = first_line if len(first_line) <= 180 else first_line[:177] + "..."
    ops_inferred = event_operator_hints(block)
    return {
        "id": f"EV-{sequence:03d}",
        "created_at": now_iso(),
        "date_iso": "",
        "age_years": _infer_age(block),
        "approxdate": _infer_approxdate(block),
        "domain": "Other",
        "what_happened": incident,
        "why_significant": "",
        "cost": "",
        "gain": "",
        "recurrence_operators": ops_inferred,
        "evidence_type": "#selfreport_only",
        "linkage": "",
        "notes": "",
        "raw_block": block,
    }

def cmd_bulkimport(args: argparse.Namespace) -> None:
    project_dir = Path(args.project).resolve()
    ds_path = project_paths(project_dir)["datastore"]
    ds = read_json(ds_path)
    if not ds:
        raise SystemExit("No datastore. Run `init` first.")

    infile = Path(args.infile).expanduser().resolve()
    if not infile.exists():
        raise SystemExit(f"Input file not found: {infile}")
    raw = infile.read_text(encoding="utf-8", errors="replace")

    fmt = args.format
    if fmt == "auto":
        try:
            parsed = json.loads(raw)
            fmt = "json" if isinstance(parsed, list) else "text"
        except Exception:
            fmt = "text"

    new_events: List[Dict[str, Any]] = []
    existing_events = ds["inputs"]["lived_trajectory"]["events"]
    base_seq = len(existing_events) + 1

    if fmt == "json":
        parsed = json.loads(raw)
        if not isinstance(parsed, list):
            raise SystemExit("JSON import expects a list of event dicts.")
        for i, item in enumerate(parsed):
            if not isinstance(item, dict):
                continue
            item.setdefault("id", f"EV-{base_seq + i:03d}")
            item.setdefault("created_at", now_iso())
            item.setdefault("evidence_type", "#selfreport_only")
            item.setdefault("recurrence_operators", [])
            new_events.append(item)
    elif fmt == "text":
        for i, b in enumerate(_text_to_event_blocks(raw)):
            new_events.append(_block_to_event(b, base_seq + i))

    if args.dry_run:
        print(f"Dry run: parsed {len(new_events)} events")
        for ev in new_events[:5]:
            print(f"  {ev['id']}: {ev['what_happened'][:80]}")
        return

    if args.replace:
        ds["inputs"]["lived_trajectory"]["events"] = new_events
    else:
        ds["inputs"]["lived_trajectory"]["events"].extend(new_events)

    audit_path = project_paths(project_dir)["data"] / "events_imported.json"
    write_json(audit_path, new_events)

    ds["meta"]["updated_at"] = now_iso()
    write_json(ds_path, ds)
    print(f"Imported {len(new_events)} events. Audit: {audit_path}")

# ----------------------------
# Analysis pipeline
# ----------------------------

def infer_life_period(ev: Dict[str, Any]) -> str:
    ay = ev.get("age_years")
    if isinstance(ay, int) or (isinstance(ay, str) and str(ay).isdigit()):
        a = int(ay)
        if a <= 12: return "0-12"
        if a <= 17: return "13-17"
        if a <= 24: return "18-24"
        if a <= 34: return "25-34"
        if a <= 44: return "35-44"
        return "45+"
    di = ev.get("date_iso") or ""
    if re.match(r"^\d{4}-\d{2}-\d{2}$", di):
        return f"year-{di[:4]}"
    return "unknown"

def build_recurrence_loops(events: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
    groups: Dict[str, List[Dict[str, Any]]] = {}
    for ev in events:
        ops = ev.get("recurrence_operators", []) or []
        sig = "|".join(sorted(ops)) if ops else "NO_OPS"
        groups.setdefault(sig, []).append(ev)

    loops = []
    idx = 1
    for sig, evs in sorted(groups.items(), key=lambda x: len(x[1]), reverse=True):
        if sig == "NO_OPS":
            continue
        loops.append({
            "id": f"RL-{idx:02d}",
            "loop_name": f"Loop derived from operators: {sig}",
            "operators_signature": sig,
            "events": [e["id"] for e in evs],
            "domains_involved": sorted(set(e.get("domain", "") for e in evs if e.get("domain"))),
            "time_span": {
                "min_date": min([e.get("date_iso") for e in evs if e.get("date_iso")] + [""]) or "",
                "max_date": max([e.get("date_iso") for e in evs if e.get("date_iso")] + [""]) or "",
            },
            "trigger_condition": "", "structural_position": "", "predictable_response": "",
            "primary_cost": "", "verified_exit_condition": "",
            "status": "PARTIAL",
        })
        idx += 1
        if idx > 7:
            break
    return loops

def build_constraint_signatures(events: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
    pair_counts: Dict[Tuple[str, str], int] = {}
    for ev in events:
        ops = sorted(ev.get("recurrence_operators", []) or [])
        for i in range(len(ops)):
            for j in range(i + 1, len(ops)):
                pair = (ops[i], ops[j])
                pair_counts[pair] = pair_counts.get(pair, 0) + 1
    top = sorted(pair_counts.items(), key=lambda x: x[1], reverse=True)[:10]
    return [{
        "id": f"CS-{i+1:02d}",
        "constraint_combination": f"{a} + {b}",
        "occurrences": n,
        "activation_conditions": "", "failure_modes": "",
        "protective_overrides": "", "early_warning_signals": "",
        "status": "PARTIAL",
    } for i, ((a, b), n) in enumerate(top)]

def build_purpose_candidates(loops: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
    return [{
        "id": f"P-{i+1:02d}",
        "purpose_statement": "To [verb] [object] under [constraint], while preserving [non-negotiable value].",
        "derived_from_loop": loop["id"],
        "constraints_it_survives": "", "constraints_it_fails_under": "",
        "required_counterweights": "", "hijack_modes": "",
        "isolation_amplifiers": "", "required_convergence_evidence": "",
        "bounded_experiment_30d": "",
        "status": "EXPLORATORY",
    } for i, loop in enumerate(loops[:7])]

def apply_tier_caps(raw: Dict[str, int], tierA_active: bool, buffer_evidence: Dict[str, bool]) -> Tuple[Dict[str, int], List[str]]:
    capped = {}
    audit = []
    for sub, val in raw.items():
        v = max(0, min(25, int(val)))
        if tierA_active and not buffer_evidence.get(sub, False) and v > DEFAULT_TIER_A_CAP:
            audit.append(f"cap_applied_{sub}_raw_{v}_cap_{DEFAULT_TIER_A_CAP}")
            v = DEFAULT_TIER_A_CAP
        capped[sub] = v
    return capped, audit

# ----------------------------
# Exports
# ----------------------------

def export_tables_csv(out_csv: Path, events, loops, signatures, collapse_stats, subscores, agency) -> List[Dict[str, Any]]:
    ensure_dir(out_csv.parent)
    rows: List[Dict[str, Any]] = []

    by_period, by_domain, by_operator = {}, {}, {}
    for ev in events:
        by_period[infer_life_period(ev)] = by_period.get(infer_life_period(ev), 0) + 1
        by_domain[ev.get("domain") or "unknown"] = by_domain.get(ev.get("domain") or "unknown", 0) + 1
        for op in ev.get("recurrence_operators", []) or []:
            by_operator[op] = by_operator.get(op, 0) + 1

    for k, v in sorted(by_period.items()):
        rows.append({"table": "event_distribution_period", "key": k, "value": v})
    for k, v in sorted(by_domain.items(), key=lambda x: (-x[1], x[0])):
        rows.append({"table": "event_distribution_domain", "key": k, "value": v})
    for k, v in sorted(by_operator.items(), key=lambda x: (-x[1], x[0])):
        rows.append({"table": "event_distribution_operator", "key": k, "value": v})

    for loop in loops:
        rows.append({
            "table": "recurrence_frequency", "loop_id": loop["id"],
            "occurrences": len(loop.get("events", [])),
            "domains": ";".join(loop.get("domains_involved", [])),
            "operators_signature": loop.get("operators_signature", ""),
            "status": loop.get("status", ""),
        })

    cost_counts = {ct: 0 for ct in COST_TYPES}
    for ev in events:
        c = (ev.get("cost") or "").lower()
        if any(w in c for w in ["money", "debt", "rent", "job", "unpaid"]): cost_counts["economic"] += 1
        if any(w in c for w in ["pain", "injury", "sick", "health", "body"]): cost_counts["bodily"] += 1
        if any(w in c for w in ["breakup", "partner", "friend", "family", "alone"]): cost_counts["relational"] += 1
        if any(w in c for w in ["time", "months", "years", "delay", "wasted"]): cost_counts["temporal"] += 1
        if any(w in c for w in ["shame", "reputation", "humiliated"]): cost_counts["reputational"] += 1
        if any(w in c for w in ["legal", "court", "police"]): cost_counts["legal"] += 1
    for ct, v in sorted(cost_counts.items(), key=lambda x: (-x[1], x[0])):
        rows.append({"table": "cost_accumulation", "cost_type": ct, "frequency": v})

    for k, v in collapse_stats.items():
        rows.append({"table": "collapse_frequency", "metric": k, "value": v})

    for sub, val in subscores.items():
        rows.append({"table": "agency_subscore", "subscore": sub, "value_0_25": val})
    rows.append({"table": "agency_total", "agency_score_0_100": agency})

    fieldnames = sorted({k for r in rows for k in r.keys()})
    with out_csv.open("w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=fieldnames)
        w.writeheader()
        for r in rows:
            w.writerow(r)
    return rows

def render_visuals(project_dir: Path, table_rows, loops, signatures, subscores) -> Dict[str, Any]:
    if not has_matplotlib():
        return {"status": "SKIPPED_NO_MATPLOTLIB", "rendered": []}
    import matplotlib
    matplotlib.use("Agg")
    import matplotlib.pyplot as plt

    paths = project_paths(project_dir)
    ensure_dir(paths["visuals"])
    rendered = []

    def kv(name):
        out = []
        for r in table_rows:
            if r.get("table") == name:
                key = r.get("key") or r.get("metric") or r.get("cost_type") or r.get("loop_id") or r.get("subscore") or ""
                v = r.get("value") or r.get("frequency") or r.get("occurrences") or r.get("value_0_25") or 0
                try: out.append((str(key), float(v)))
                except: pass
        return out

    # VIZ-01: Operator distribution
    fig = plt.figure()
    op = kv("event_distribution_operator")
    if op:
        plt.pie([v for _, v in op], labels=[k for k, _ in op], autopct="%1.0f%%")
        plt.title("Operator Distribution")
    fig.savefig(paths["visuals"] / VIS_MODES[0][2], dpi=120, bbox_inches="tight")
    plt.close(fig)
    rendered.append({"viz_id": "VIZ-01", "file": str(paths["visuals"] / VIS_MODES[0][2])})

    # VIZ-02: Timeline
    fig = plt.figure()
    per = kv("event_distribution_period")
    if per:
        plt.bar([k for k, _ in per], [v for _, v in per])
        plt.title("Events by Life Period"); plt.xticks(rotation=45, ha="right")
    fig.savefig(paths["visuals"] / VIS_MODES[1][2], dpi=120, bbox_inches="tight")
    plt.close(fig)
    rendered.append({"viz_id": "VIZ-02", "file": str(paths["visuals"] / VIS_MODES[1][2])})

    # VIZ-03: Loops
    fig = plt.figure()
    if loops:
        plt.bar([lp["id"] for lp in loops], [len(lp.get("events", [])) for lp in loops])
        plt.title("Recurrence Loop Occurrences")
    fig.savefig(paths["visuals"] / VIS_MODES[2][2], dpi=120, bbox_inches="tight")
    plt.close(fig)
    rendered.append({"viz_id": "VIZ-03", "file": str(paths["visuals"] / VIS_MODES[2][2])})

    # VIZ-04: Constraint radar
    fig = plt.figure()
    if signatures:
        import math
        vals = [s.get("occurrences", 0) for s in signatures[:6]]
        labels = [s.get("id", "") for s in signatures[:6]]
        ax = fig.add_subplot(111, polar=True)
        n = max(len(vals), 1)
        angles = [2 * math.pi * i / n for i in range(n)] + [0]
        v = [float(x) for x in vals] + [float(vals[0]) if vals else 0]
        ax.plot(angles, v); ax.fill(angles, v, alpha=0.25)
        if labels:
            ax.set_thetagrids([a * 180 / math.pi for a in angles[:-1]], labels)
        ax.set_title("Constraint Signatures")
    fig.savefig(paths["visuals"] / VIS_MODES[3][2], dpi=120, bbox_inches="tight")
    plt.close(fig)
    rendered.append({"viz_id": "VIZ-04", "file": str(paths["visuals"] / VIS_MODES[3][2])})

    # VIZ-09: Subscores
    fig = plt.figure()
    if subscores:
        plt.bar(list(subscores.keys()), list(subscores.values()))
        plt.title("Agency Subscores (0-25)"); plt.xticks(rotation=20, ha="right")
        plt.ylim(0, 25)
    fig.savefig(paths["visuals"] / VIS_MODES[8][2], dpi=120, bbox_inches="tight")
    plt.close(fig)
    rendered.append({"viz_id": "VIZ-09", "file": str(paths["visuals"] / VIS_MODES[8][2])})

    # Cost
    fig = plt.figure()
    costs = kv("cost_accumulation")
    if costs:
        plt.bar([k for k, _ in costs], [v for _, v in costs])
        plt.title("Cost Accumulation"); plt.xticks(rotation=45, ha="right")
    fig.savefig(paths["visuals"] / VIS_MODES[5][2], dpi=120, bbox_inches="tight")
    plt.close(fig)
    rendered.append({"viz_id": "VIZ-06", "file": str(paths["visuals"] / VIS_MODES[5][2])})

    return {"status": "RENDERED", "rendered": rendered}

def write_executive_summary(path: Path, ds, loops, signatures, purposes, subscores, agency, audits):
    ensure_dir(path.parent)
    lines = [
        f"FLOWERAPP / IRCM — Executive Summary",
        f"Generated: {now_iso()}",
        f"Version: {IRCM_VERSION}",
        "",
        f"Agency Score: {agency}/100",
        "",
        "Subscores (/25):",
    ]
    for k, v in subscores.items():
        lines.append(f"  {k}: {v}")
    lines += ["", "Tier A cap audit:" ]
    for a in audits or ["  (none)"]:
        lines.append(f"  - {a}")
    lines += ["", f"A) Recurrence Loops (max 7, default PARTIAL):"]
    for lp in loops[:7]:
        lines.append(f"- {lp['id']}: {lp['loop_name']} [{lp.get('status','')}]")
    lines += ["", f"B) Constraint Signatures (max 10):"]
    for cs in signatures[:10]:
        lines.append(f"- {cs['id']}: {cs['constraint_combination']} (n={cs.get('occurrences',0)}) [{cs.get('status','')}]")
    lines += ["", f"C) Derived Purposes (max 7, EXPLORATORY):"]
    for p in purposes[:7]:
        lines.append(f"- {p['id']} from {p.get('derived_from_loop','')}")
    lines += [
        "",
        "Exclusions: no destiny language, no moral elevation, no narrative justification.",
        "Tier rule: A shapes scores. B modifies. C is meaning-layer only.",
    ]
    path.write_text("\n".join(lines), encoding="utf-8")

def write_detailed_report(path: Path, ds, loops, signatures, purposes, table_csv, subscores, agency, audits, numerology):
    ensure_dir(path.parent)
    lines = [
        "FLOWERAPP / IRCM — Detailed Analytical Report",
        f"Version: {IRCM_VERSION}",
        f"Generated: {now_iso()}",
        "",
        "0) Method Scope and Safeguards",
        "- Phase IV-VI computations and limits documented here.",
        "- Visual archives stored verbatim; no personality inference.",
        "- Symbolic inputs generate questions; lived data + constraints override symbolism.",
        "- Insights formed under isolation must be tagged UNVALIDATED and externally reviewed.",
        "",
    ]

    # Iris symbolic gate
    iris = ds.get("inputs", {}).get("symbolic_layer_optional", {}).get("iris_symbolic", {})
    if iris.get("enabled") and iris.get("rule_questions_not_answers_ack", False):
        lines += [
            "0.1) Iris Symbolic Layer (Questions Only, Non-Medical)",
            "- Symbolic prompts only. No diagnostic or predictive claims.",
        ]
        desc = iris.get("descriptors", {}) or {}
        lines.append(f"  Descriptors: {desc}")
        lines.append("  Prompts:")
        for q in iris_questions_from_descriptors(desc):
            lines.append(f"  - {q}")
        lines.append("")

    lines += [
        "1) Phase IV — Recurrence Loop Extraction",
        f"   Method: group events by operator-set signature; cap candidates at 7.",
        f"   Status: defaults PARTIAL until user validates trigger/position/response/cost/exit.",
    ]
    for lp in loops[:7]:
        lines.append(f"  [{lp['id']}] {lp['loop_name']} | status={lp.get('status','')}")
        lines.append(f"    operators: {lp.get('operators_signature','')}")
        lines.append(f"    events: {', '.join(lp.get('events', []))}")
        lines.append(f"    domains: {', '.join(lp.get('domains_involved', []))}")

    lines += [
        "",
        "2) Phase V — Constraint Signature Mapping",
        "   Method: count operator co-occurrences across events; top 10.",
    ]
    for cs in signatures[:10]:
        lines.append(f"  [{cs['id']}] {cs['constraint_combination']} | n={cs.get('occurrences',0)} [{cs.get('status','')}]")

    lines += [
        "",
        "3) Phase VI — Purpose Derivation",
        "   Default: EXPLORATORY until convergence evidence (>=3 lenses).",
    ]
    for p in purposes[:7]:
        lines.append(f"  [{p['id']}] from {p.get('derived_from_loop','')} [{p.get('status','')}]")

    lines += [
        "",
        "4) Agency Scoring",
        f"   Equation: A = PL + RB + RA + SL (each 0-25)",
        f"   Total: {agency}/100",
    ]
    for k, v in subscores.items():
        lines.append(f"   {k}: {v}/25")
    if audits:
        lines.append("   Cap audit:")
        for a in audits:
            lines.append(f"     - {a}")

    if numerology:
        lines += ["", "5) Numerology Container (Tier C, bounded — questions only)"]
        if "error" in numerology:
            lines.append(f"   Error: {numerology['error']}")
        else:
            lp = numerology.get("life_path", {})
            ns = numerology.get("name_sums", {})
            mat = numerology.get("maturity", {})
            lines.append(f"   Life Path: raw={lp.get('raw')} steps={lp.get('steps')} → {lp.get('life_path')}")
            lines.append(f"   Expression: {ns.get('expression')} (raw={ns.get('expression_raw')})")
            lines.append(f"   Heart's Desire: {ns.get('hearts_desire')} (raw={ns.get('hearts_desire_raw')})")
            lines.append(f"   Personality: {ns.get('personality')} (raw={ns.get('personality_raw')})")
            lines.append(f"   Maturity: {mat.get('maturity')} (raw={mat.get('raw')})")

    lines += [
        "",
        "6) Tables CSV",
        f"   {table_csv}",
        "",
        "Final accountability: no visualization stands alone; no text without data; no data without constraints.",
    ]
    path.write_text("\n".join(lines), encoding="utf-8")

def cmd_run(args: argparse.Namespace) -> None:
    project_dir = Path(args.project).resolve()
    paths = project_paths(project_dir)
    ds = read_json(paths["datastore"])
    if not ds:
        raise SystemExit("No datastore. Run `init` first.")

    # Iris gate enforcement
    iris = ds.get("inputs", {}).get("symbolic_layer_optional", {}).get("iris_symbolic", {})
    if iris.get("enabled") and not iris.get("rule_questions_not_answers_ack", False):
        raise SystemExit("Iris symbolic enabled but rule_questions_not_answers_ack is false. Refusing.")

    ensure_dir(paths["reports"])
    ensure_dir(paths["visuals"])

    events = ds["inputs"]["lived_trajectory"]["events"]
    loops = build_recurrence_loops(events)
    signatures = build_constraint_signatures(events)
    purposes = build_purpose_candidates(loops)

    raw_subscores = ds["inputs"]["scoring"]["raw_subscores"]
    tierA_active = bool(ds["inputs"]["scoring"].get("tierA_active", False))
    buffer_evidence = ds["inputs"]["scoring"]["buffer_evidence"]
    subscores, audits = apply_tier_caps(raw_subscores, tierA_active, buffer_evidence)
    agency = sum(subscores.values())

    # Numerology (if enabled)
    num = ds.get("inputs", {}).get("symbolic_layer_optional", {}).get("numerology", {})
    numerology_out = {}
    if num.get("enabled") and num.get("rule_questions_not_answers_ack", False):
        name = ds["inputs"]["identity_symbolic"].get("full_legal_name_birth", "").strip()
        dob = ds["inputs"]["temporal_spatial"].get("birth_date", "").strip()
        if name and dob:
            ns = numerology_name_sums(name, num.get("y_as_vowel", False))
            lp = numerology_life_path(dob)
            mat = numerology_maturity(lp["life_path"], ns["expression"])
            numerology_out = {
                "method": "pythagorean", "y_as_vowel": num.get("y_as_vowel", False),
                "name": name, "dob": dob,
                "life_path": lp, "name_sums": ns, "maturity": mat,
                "rule": "Translate into testable questions only. No prophecy.",
            }
        else:
            numerology_out = {"error": "Missing name or dob.", "rule": "Translate into testable questions only."}

    ds["analysis"]["phase_iv_recurrence_loops"] = loops
    ds["analysis"]["phase_v_constraint_signatures"] = signatures
    ds["analysis"]["phase_vi_purposes"] = purposes
    ds["analysis"]["agency_score"] = agency
    ds["analysis"]["subscores_capped"] = subscores
    ds["analysis"]["caps_applied"] = audits
    ds["analysis"]["numerology_outputs"] = numerology_out

    collapse_stats = ds["analysis"]["collapse_stats"]
    tables_csv = paths["reports"] / "ircm_tables.csv"
    table_rows = export_tables_csv(tables_csv, events, loops, signatures, collapse_stats, subscores, agency)

    summary_txt = paths["reports"] / "ircm_summary.txt"
    write_executive_summary(summary_txt, ds, loops, signatures, purposes, subscores, agency, audits)

    report_txt = paths["reports"] / "ircm_report.txt"
    write_detailed_report(report_txt, ds, loops, signatures, purposes, tables_csv, subscores, agency, audits, numerology_out)

    viz_result = render_visuals(project_dir, table_rows, loops, signatures, subscores)

    metadata = {
        "ircm_version": IRCM_VERSION,
        "run_at": now_iso(),
        "project": str(project_dir),
        "agency_score_0_100": agency,
        "subscores_0_25": subscores,
        "tierA_active": tierA_active,
        "caps_applied": audits,
        "outputs": {
            "summary": str(summary_txt), "report": str(report_txt),
            "tables_csv": str(tables_csv),
            "visuals_status": viz_result.get("status"),
            "visuals_rendered": viz_result.get("rendered", []),
        },
        "equations": {
            "agency_total": "A = PL + RB + RA + SL (each 0-25)",
            "tier_a_cap": "if tierA_active and not buffer_evidence[k]: k = min(k, 19)",
        },
        "accountability_rule": "No visualization alone. No text without data. No data without constraints.",
        "tier_rule": "Tier A shapes scores. Tier B modifies. Tier C is meaning-layer only.",
    }
    metadata_path = paths["reports"] / "ircm_metadata.json"
    write_json(metadata_path, metadata)

    ds["exports"]["last_run_at"] = metadata["run_at"]
    ds["exports"]["outputs"] = metadata["outputs"]
    ds["meta"]["updated_at"] = now_iso()
    write_json(paths["datastore"], ds)

    print(f"FLOWERAPP run complete.")
    print(f"  Agency: {agency}/100")
    print(f"  Subscores: {subscores}")
    print(f"  Summary:  {summary_txt}")
    print(f"  Report:   {report_txt}")
    print(f"  Tables:   {tables_csv}")
    print(f"  Metadata: {metadata_path}")
    print(f"  Visuals:  {viz_result.get('status')}")

# ----------------------------
# CLI Parser
# ----------------------------

def build_parser() -> argparse.ArgumentParser:
    p = argparse.ArgumentParser(
        prog="flowerapp",
        description="FLOWERAPP / IRCM — Individual Data Intake & Analysis Protocol",
        formatter_class=argparse.RawTextHelpFormatter,
    )
    sub = p.add_subparsers(dest="cmd", required=True)

    # init
    sp = sub.add_parser("init", aliases=["new"], help="Create new project (alias: new)")
    sp.add_argument("--project", default=".")
    sp.add_argument("--force", action="store_true")
    sp.add_argument("--isolation-threshold-days", type=int, default=None)
    sp.set_defaults(func=cmd_init)

    # show
    sp = sub.add_parser("show", aliases=["view"], help="Show inputs JSON (alias: view)")
    sp.add_argument("--project", default=".")
    sp.set_defaults(func=cmd_show)

    # set
    sp = sub.add_parser("set", help="Set nested field: --kv path.to.field=value")
    sp.add_argument("--project", default=".")
    sp.add_argument("--kv", required=True)
    sp.set_defaults(func=cmd_set)

    # add-list
    sp = sub.add_parser("add-list", aliases=["list+"], help="Append to list (alias: list+)")
    sp.add_argument("--project", default=".")
    sp.add_argument("--path", required=True)
    sp.add_argument("--item", required=True)
    sp.set_defaults(func=cmd_add_list_item)

    # add-event
    sp = sub.add_parser("add-event", aliases=["ev"], help="Add lived trajectory event (alias: ev)")
    sp.add_argument("--project", default=".")
    sp.add_argument("--date", default="")
    sp.add_argument("--age", default="")
    sp.add_argument("--domain", default=None, choices=DEFAULT_DOMAINS)
    sp.add_argument("--what", default=None)
    sp.add_argument("--why", default=None)
    sp.add_argument("--cost", default=None)
    sp.add_argument("--gain", default=None)
    sp.add_argument("--operators", default="")
    sp.add_argument("--linkage", default="", help="Subscore linkage hashtags")
    sp.add_argument("--add-hints", action="store_true")
    sp.add_argument("--notes", default="")
    sp.set_defaults(func=cmd_add_event)

    # list-events
    sp = sub.add_parser("list-events", aliases=["events", "ls-ev"], help="List events")
    sp.add_argument("--project", default=".")
    sp.set_defaults(func=cmd_list_events)

    # add-media
    sp = sub.add_parser("add-media", aliases=["media"], help="Archive image (alias: media)")
    sp.add_argument("--project", default=".")
    sp.add_argument("--kind", required=True, help="handwriting | drawing")
    sp.add_argument("--file", required=True)
    sp.add_argument("--approx-date", default="")
    sp.add_argument("--context", default="")
    sp.add_argument("--medium", default="")
    sp.add_argument("--duration-minutes", default="")
    sp.add_argument("--made-alone", action="store_true")
    sp.add_argument("--made-with-others", action="store_true")
    sp.add_argument("--made-during-isolation", action="store_true")
    sp.add_argument("--preceded-written-explanation", action="store_true")
    sp.add_argument("--followed-written-explanation", action="store_true")
    sp.add_argument("--notes", default="")
    sp.set_defaults(func=cmd_add_media)

    # bulkimport
    sp = sub.add_parser("bulkimport", help="Bulk import events from JSON or text")
    sp.add_argument("--project", default=".")
    sp.add_argument("--in", dest="infile", required=True)
    sp.add_argument("--format", default="auto", choices=["auto", "json", "text"])
    sp.add_argument("--replace", action="store_true")
    sp.add_argument("--dry-run", action="store_true")
    sp.set_defaults(func=cmd_bulkimport)

    # run
    sp = sub.add_parser("run", aliases=["go"], help="Run analysis + export (alias: go)")
    sp.add_argument("--project", default=".")
    sp.set_defaults(func=cmd_run)

    return p

def main() -> None:
    args = build_parser().parse_args()
    args.func(args)

if __name__ == "__main__":
    main()
