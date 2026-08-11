---
type: raw-source
aliases: [orphan-raw-2026-05-06-018]
graph_repair: 2026-05-06
---

# engine.py
from __future__ import annotations

from typing import Dict, List, Tuple, Optional

from aigov_builder.models.core import (
    RendererInput,
    ControlAssessment,
    GovernanceAssessmentResult,
)
from aigov_builder.reporting.roadmap import generate_remediation_roadmap

# ----------------------------
# Query mappers
# ----------------------------
def doc_maps_from_queries(inp: RendererInput) -> tuple[Dict[str, str], Dict[str, str]]:
    """
    Returns:
      - doc_status_by_control: Documented | Partial | Missing | NA
      - doc_result_by_control: Meets | DoesNotMeet | Unknown
    """
    doc_status_by_control: Dict[str, str] = {}
    doc_result_by_control: Dict[str, str] = {}

    for q in (inp.queries or []):
        cid = (getattr(q, "query_id", None) or "").strip()
        if not cid:
            continue

        status = (getattr(q, "status", None) or "Open").strip()
        sev = (getattr(q, "severity", None) or "INFO").strip()

        # Defaults
        doc_status = "Missing"
        doc_result = "Unknown"

        if status == "Resolved":
            doc_status = "Documented"
            doc_result = "Meets"
        elif status == "AcceptedRisk":
            doc_status = "NA"
            doc_result = "Unknown"
        else:
            doc_status = "Missing" if sev == "BLOCKING" else "Partial"
            doc_result = "Unknown"

        # Optional overrides if your query schema includes them
        if getattr(q, "doc_status", None):
            doc_status = str(getattr(q, "doc_status")).strip()
        if getattr(q, "doc_result", None):
            doc_result = str(getattr(q, "doc_result")).strip()

        doc_status_by_control[cid] = normalize_doc_status(doc_status)
        doc_result_by_control[cid] = doc_result

    return doc_status_by_control, doc_result_by_control

def doc_status_by_control_from_queries(inp: RendererInput) -> Dict[str, str]:
    doc_status_by_control, _ = doc_maps_from_queries(inp)
    return doc_status_by_control

def doc_result_by_control_from_queries(inp: RendererInput) -> Dict[str, str]:
    _, doc_result_by_control = doc_maps_from_queries(inp)
    return doc_result_by_control

def impl_status_by_control_from_queries(inp: RendererInput) -> Dict[str, str]:
    """
    Returns a per-control implementation status derived from queries.

    Expected values:
      Observed | Partial | Missing | NA
    """
    out: Dict[str, str] = {}

    for q in (inp.queries or []):
        cid = (getattr(q, "query_id", None) or "").strip()
        if not cid:
            continue

        status = (getattr(q, "status", None) or "Open").strip()
        sev = (getattr(q, "severity", None) or "INFO").strip()

        impl_status = "Missing"
        if status == "Resolved":
            impl_status = "Observed"
        elif status == "AcceptedRisk":
            impl_status = "NA"
        else:
            impl_status = "Missing" if sev == "BLOCKING" else "Partial"

        # Optional override
        if getattr(q, "impl_status", None):
            impl_status = str(getattr(q, "impl_status")).strip()

        out[cid] = normalize_impl_status(impl_status)

    return out

def evidence_refs_by_control_from_queries(inp: RendererInput) -> Dict[str, List[str]]:
    """
    Collects evidence references per control from queries.

    Supports common field names:
      - evidence_refs: List[str]
      - evidence_ref: str
      - evidence: List[str] or str
      - evidence_urls: List[str]
    """
    out: Dict[str, List[str]] = {}

    for q in (inp.queries or []):
        cid = (getattr(q, "query_id", None) or "").strip()
        if not cid:
            continue

        refs: List[str] = []

        if getattr(q, "evidence_refs", None):
            val = getattr(q, "evidence_refs")
            refs.extend(val if isinstance(val, list) else [str(val)])
        if getattr(q, "evidence_ref", None):
            refs.append(str(getattr(q, "evidence_ref")))
        if getattr(q, "evidence", None):
            val = getattr(q, "evidence")
            refs.extend(val if isinstance(val, list) else [str(val)])
        if getattr(q, "evidence_urls", None):
            val = getattr(q, "evidence_urls")
            refs.extend(val if isinstance(val, list) else [str(val)])

        # Normalize + dedupe while preserving order
        seen = set()
        cleaned: List[str] = []
        for r in refs:
            r = str(r).strip()
            if not r or r in seen:
                continue
            seen.add(r)
            cleaned.append(r)

        if cleaned:
            out.setdefault(cid, []).extend(cleaned)

    # Final per-control dedupe (in case multiple queries share the same cid)
    for cid, refs in list(out.items()):
        seen = set()
        deduped: List[str] = []
        for r in refs:
            if r in seen:
                continue
            seen.add(r)
            deduped.append(r)
        out[cid] = deduped

    return out

# ----------------------------
# Sector helpers (ONE version only)
# ----------------------------
MATURITY_LABELS_EN = {
    0: "Absent",
    20: "Initial",
    40: "Developing",
    60: "Defined",
    80: "Managed",
    100: "Optimized",
}

MATURITY_LABELS_FR = {
    0: "Absent",
    20: "Initial",
    40: "En développement",
    60: "Défini",
    80: "Maîtrisé",
    100: "Optimisé",
}

HIGH_RISK_SECTORS = {
    "healthcare",
    "public",
    "public_sector",
    "education",
    "finance",
    "banking",
    "insurance",
    "critical_infrastructure",
}

def normalize_sector(sector: str) -> str:
    return (sector or "").strip().lower().replace("-", "_").replace(" ", "_")

def is_high_risk_sector(sector: str) -> bool:
    return normalize_sector(sector) in HIGH_RISK_SECTORS

# Baseline category weights (must sum to 1 after normalization).
BASELINE_WEIGHTS: Dict[str, float] = {
    "scope": 0.10,
    "data": 0.20,
    "evaluation": 0.20,
    "oversight": 0.15,
    "monitoring": 0.20,
    "change": 0.15,

    # Compatibility keys (if your result schema expects them)
    "human_oversight": 0.00,
    "resilience": 0.00,
    "lifecycle": 0.00,
    "documentation": 0.00,
}

SECTOR_WEIGHT_DELTAS: Dict[str, Dict[str, float]] = {
    "saas": {"monitoring": +0.05, "change": +0.05, "oversight": -0.05, "scope": -0.05},
    "healthcare": {"evaluation": +0.10, "data": +0.05, "oversight": +0.05, "monitoring": -0.10, "change": -0.05, "scope": -0.05},
    "public": {"scope": +0.05, "oversight": +0.05, "data": +0.05, "monitoring": -0.05, "evaluation": -0.05, "change": -0.05},
    "finance": {"data": +0.05, "monitoring": +0.05, "change": +0.05, "scope": -0.05, "evaluation": -0.05, "oversight": -0.05},
}

def apply_sector_weights(sector: str) -> Dict[str, float]:
    s = normalize_sector(sector)

    weights = dict(BASELINE_WEIGHTS)
    deltas = SECTOR_WEIGHT_DELTAS.get(s, {})
    for k, d in deltas.items():
        if k in weights:
            weights[k] = max(0.0, weights[k] + float(d))

    total = sum(weights.values())
    if total <= 0:
        core = ["scope", "data", "evaluation", "oversight", "monitoring", "change"]
        return {k: (1.0 / len(core)) for k in core}

    for k in list(weights.keys()):
        weights[k] = weights[k] / total

    return weights

# ----------------------------
# 1) Control-level maturity criteria
# ----------------------------
DOC_STATUS_TO_MATURITY = {
    "Missing": 0,
    "Documented": 100,
    "Partial": 60,
    "NA": 0,
}

DOC_STATUS_TO_CONFIDENCE = {
    "Missing": 0.0,
    "Partial": 0.5,
    "Documented": 1.0,
    "NA": 0.0,
}

IMPL_STATUS_TO_MATURITY = {
    "Missing": 0,
    "Partial": 60,
    "Observed": 100,
    "NA": 0,
}

def normalize_doc_status(value: str) -> str:
    v = (value or "").strip()
    return v if v in ("Documented", "Partial", "Missing", "NA") else "Missing"

def normalize_impl_status(value: str) -> str:
    v = (value or "").strip()
    return v if v in ("Observed", "Partial", "Missing", "NA") else "Missing"

def doc_score(doc_status: str) -> int:
    return int(DOC_STATUS_TO_MATURITY.get(normalize_doc_status(doc_status), 0))

def impl_score(impl_status: str) -> int:
    return int(IMPL_STATUS_TO_MATURITY.get(normalize_impl_status(impl_status), 0))

def evidence_confidence_from_controls(controls: List[ControlAssessment]) -> float:
    if not controls:
        return 0.0
    vals: List[float] = []
    for c in controls:
        vals.append(float(DOC_STATUS_TO_CONFIDENCE.get(getattr(c, "doc_status", "Missing"), 0.0)))
    return round(sum(vals) / len(vals), 3)

# ----------------------------
# 3) Risk tier mapping
# ----------------------------
def risk_tier_from(score: int, critical_flags: List[str]) -> str:
    if critical_flags:
        return "HIGH"
    if score >= 80:
        return "LOW"
    if score >= 60:
        return "MEDIUM"
    if score >= 40:
        return "ELEVATED"
    return "HIGH"

# ----------------------------
# 4) Readiness label mapping (sector-aware)
# ----------------------------
def readiness_label(score: int, sector: str, language: str) -> str:
    s = normalize_sector(sector)

    ready = 80
    conditional = 60
    not_ready = 40

    if s == "healthcare":
        ready, conditional, not_ready = 85, 65, 45
    elif s == "public":
        ready, conditional, not_ready = 80, 60, 40
    elif s == "saas":
        ready, conditional, not_ready = 80, 55, 35

    if score >= ready:
        return "READY_TO_RENDER" if language == "EN" else "PRÊT_À_PRODUIRE"
    if score >= conditional:
        return "CONDITIONAL" if language == "EN" else "CONDITIONNEL"
    if score >= not_ready:
        return "NEEDS_WORK" if language == "EN" else "À_RENFORCER"
    return "BLOCKED" if language == "EN" else "BLOQUÉ"

# ----------------------------
# 5) Sector override rules
# ----------------------------
def apply_sector_overrides(
    sector: str,
    language: str,
    category_maturity: Dict[str, int],
    controls: List[ControlAssessment],
) -> Tuple[List[str], List[str]]:
    s = normalize_sector(sector)
    critical_flags: List[str] = []
    overrides: List[str] = []

    maturity_by_id = {c.control_id: int(getattr(c, "maturity", 0)) for c in controls}

    if category_maturity.get("data", 0) < 60:
        critical_flags.append("DATA_GOVERNANCE_BELOW_DEFINED")
        overrides.append("DATA_MIN_60")

    if category_maturity.get("change", 0) < 60:
        critical_flags.append("CHANGE_CONTROL_BELOW_DEFINED")
        overrides.append("CHANGE_MIN_60")

    if s == "healthcare":
        if category_maturity.get("evaluation", 0) < 80:
            critical_flags.append("HEALTH_EVALUATION_BELOW_MANAGED")
            overrides.append("HEALTH_EVAL_MIN_80")
        if category_maturity.get("oversight", 0) < 80:
            critical_flags.append("HEALTH_OVERSIGHT_BELOW_MANAGED")
            overrides.append("HEALTH_OVERSIGHT_MIN_80")

    if s == "saas":
        if category_maturity.get("monitoring", 0) < 60:
            critical_flags.append("SAAS_MONITORING_BELOW_DEFINED")
            overrides.append("SAAS_MONITOR_MIN_60")

    if s == "public":
        if category_maturity.get("scope", 0) < 60:
            critical_flags.append("PUBLIC_SCOPE_BELOW_DEFINED")
            overrides.append("PUBLIC_SCOPE_MIN_60")
        if category_maturity.get("oversight", 0) < 60:
            critical_flags.append("PUBLIC_OVERSIGHT_BELOW_DEFINED")
            overrides.append("PUBLIC_OVERSIGHT_MIN_60")

    if maturity_by_id.get("MON-CORE-01", 100) < 60:
        critical_flags.append("MON_CORE_CONTROL_BELOW_DEFINED")
        overrides.append("MON_CORE_MIN_60")

    return critical_flags, overrides

# ----------------------------
# 6) Control scoring
# ----------------------------
def score_controls(
    inp: RendererInput,
    sector: str,
    language: str = "EN",
    doc_status_by_control: Optional[Dict[str, str]] = None,
    impl_status_by_control: Optional[Dict[str, str]] = None,
    evidence_refs_by_control: Optional[Dict[str, List[str]]] = None,
) -> List[ControlAssessment]:
    doc_status_by_control = doc_status_by_control or {}
    impl_status_by_control = impl_status_by_control or {}
    evidence_refs_by_control = evidence_refs_by_control or {}

    controls: List[ControlAssessment] = []

    def d(cid: str, default: str = "Missing") -> str:
        return normalize_doc_status(doc_status_by_control.get(cid, default))

    def i(cid: str, default: str = "Missing") -> str:
        return normalize_impl_status(impl_status_by_control.get(cid, default))

    def maturity(cid: str) -> int:
        # additive, capped at 100 (your style)
        return min(100, doc_score(d(cid)) + impl_score(i(cid)))

    # Scope
    scope_doc = "Documented" if getattr(inp.ai_system, "intended_use", None) else "Missing"
    controls.append(
        ControlAssessment(
            control_id="SCP-01",
            doc_status=d("SCP-01"),
            control_name="Use case and scope definition" if language == "EN" else "Définition de l’usage et du périmètre",
            category="scope",
            maturity=min(100, doc_score(scope_doc) + impl_score(i("SCP-01"))),
            finding=(
                "Use case and scope are documented."
                if scope_doc == "Documented"
                else "No documented use case or scope was provided."
            ) if language == "EN" else (
                "L’usage et le périmètre sont documentés."
                if scope_doc == "Documented"
                else "Aucun usage ou périmètre documenté n’a été fourni."
            ),
            control_library_ref="Scope/UseCase/Boundaries",
        )
    )

    # Data
    data_doc = "Documented" if getattr(inp.ai_system, "data_sources", None) else "Missing"
    controls.append(
        ControlAssessment(
            control_id="DAT-01",
            doc_status=d("DAT-01"),
            control_name="Data sources and permissions" if language == "EN" else "Sources de données et autorisations",
            category="data",
            maturity=min(100, doc_score(data_doc) + impl_score(i("DAT-01"))),
            finding=(
                "Data sources and permissions are documented."
                if data_doc == "Documented"
                else "No documented data sources or permissions were provided."
            ) if language == "EN" else (
                "Les sources de données et autorisations sont documentées."
                if data_doc == "Documented"
                else "Aucune source de données ou autorisation documentée n’a été fournie."
            ),
            control_library_ref="Data/Inventory/Access",
        )
    )

    # Evaluation
    eval_doc = "Documented" if getattr(inp.ai_system, "evaluation_method", None) else "Missing"
    controls.append(
        ControlAssessment(
            control_id="EVAL-01",
            doc_status=d("EVAL-01"),
            control_name="Validation method and baseline" if language == "EN" else "Méthode de validation et référence",
            category="evaluation",
            maturity=min(100, doc_score(eval_doc) + impl_score(i("EVAL-01"))),
            finding=(
                "Validation method and baseline are documented."
                if eval_doc == "Documented"
                else "No documented validation method or baseline was provided."
            ) if language == "EN" else (
                "La méthode de validation et la référence sont documentées."
                if eval_doc == "Documented"
                else "Aucune méthode de validation ou référence documentée n’a été fournie."
            ),
            control_library_ref="Evaluation/Baseline/QA",
        )
    )

    # Oversight
    ov_doc = "Documented" if getattr(inp.ai_system, "human_override", None) else "Missing"
    controls.append(
        ControlAssessment(
            control_id="HUM-01",
            doc_status=d("HUM-01"),
            control_name="Human override and escalation" if language == "EN" else "Contournement humain et escalade",
            category="oversight",
            maturity=min(100, doc_score(ov_doc) + impl_score(i("HUM-01"))),
            finding=(
                "Override and escalation are documented."
                if ov_doc == "Documented"
                else "No documented override or escalation pathway was provided."
            ) if language == "EN" else (
                "Le contournement et l’escalade sont documentés."
                if ov_doc == "Documented"
                else "Aucun mécanisme de contournement ou escalade documenté n’a été fourni."
            ),
            control_library_ref="Oversight/Override/Escalation",
        )
    )

    # Monitoring
    mon_doc = d("MON-CORE-01")
    controls.append(
        ControlAssessment(
            control_id="MON-CORE-01",
            doc_status=mon_doc,
            control_name="Monitoring signals, thresholds, owners, evidence" if language == "EN" else "Suivi: signaux, seuils, responsables, preuves",
            category="monitoring",
            maturity=maturity("MON-CORE-01"),
            finding=(
                "Monitoring plan is documented."
                if mon_doc == "Documented"
                else "No documented monitoring signals, thresholds, owners, cadence, or evidence were provided."
            ) if language == "EN" else (
                "Le plan de suivi est documenté."
                if mon_doc == "Documented"
                else "Aucun plan documenté de suivi (signaux, seuils, responsables, cadence, preuves) n’a été fourni."
            ),
            control_library_ref="Monitoring/Signals/Thresholds/Evidence",
        )
    )

    # Change management
    chg_doc = d("CHG-01")
    controls.append(
        ControlAssessment(
            control_id="CHG-01",
            doc_status=chg_doc,
            control_name="Change control and traceability" if language == "EN" else "Contrôle des changements et traçabilité",
            category="change",
            maturity=maturity("CHG-01"),
            finding=(
                "Change control is documented."
                if chg_doc == "Documented"
                else "No documented change control, approvals, or traceability evidence were provided."
            ) if language == "EN" else (
                "Le contrôle des changements est documenté."
                if chg_doc == "Documented"
                else "Aucun contrôle des changements documenté (approbations, traçabilité, preuves) n’a été fourni."
            ),
            control_library_ref="Change/Approvals/Versioning",
        )
    )

    # Attach evidence refs if model supports it
    for c in controls:
        cid = getattr(c, "control_id", "")
        refs = evidence_refs_by_control.get(cid)
        if refs:
            try:
                setattr(c, "evidence_refs", refs)
            except Exception:
                pass

    return controls

# ----------------------------
# 7) assess_governance()
# ----------------------------
def assess_governance(
    inp: RendererInput,
    sector: str,
    language: str = "EN",
) -> GovernanceAssessmentResult:
    high_risk = is_high_risk_sector(sector)
    weights = apply_sector_weights(sector)

    doc_status_by_control = doc_status_by_control_from_queries(inp)
    impl_status_by_control = impl_status_by_control_from_queries(inp)
    evidence_refs_by_control = evidence_refs_by_control_from_queries(inp)

    controls = score_controls(
        inp,
        sector=sector,
        language=language,
        doc_status_by_control=doc_status_by_control,
        impl_status_by_control=impl_status_by_control,
        evidence_refs_by_control=evidence_refs_by_control,
    )

    # Category maturity (avg of controls per category key present in weights)
    by_cat: Dict[str, List[int]] = {k: [] for k in weights.keys()}
    for c in controls:
        if c.category in by_cat:
            by_cat[c.category].append(int(c.maturity))

    category_maturity: Dict[str, int] = {}
    for cat, vals in by_cat.items():
        category_maturity[cat] = round(sum(vals) / len(vals)) if vals else 0

    # Monitoring layering (kept as in your draft)
    monitoring_core01 = 0
    monitoring_core02 = 0
    for c in controls:
        if c.control_id == "MON-CORE-01":
            monitoring_core01 = int(c.maturity)
    monitoring_core02 = monitoring_core01
    monitoring_composite = round(monitoring_core01 * 0.4 + monitoring_core02 * 0.6)
    category_maturity["monitoring"] = monitoring_composite

    # Human Oversight layering (kept as in your draft; controls may not exist yet)
    human_core01 = 0
    human_core02 = 0
    for c in controls:
        if c.control_id == "HOV-CORE-01":
            human_core01 = int(c.maturity)
        if c.control_id == "HOV-CORE-02":
            human_core02 = int(c.maturity)
    if human_core02 == 0:
        human_core02 = human_core01
    human_composite = round(human_core01 * 0.5 + human_core02 * 0.5)
    category_maturity["human_oversight"] = human_composite

    # Weighted scoring
    category_points: Dict[str, float] = {}
    total_points = 0.0
    for cat, w in weights.items():
        m = category_maturity.get(cat, 0)
        pts = float(m) * float(w)
        category_points[cat] = pts
        total_points += pts

    score = int(round(total_points))
    score = max(0, min(100, score))

    # Missing elements
    missing_elements = [
        c.control_name for c in controls if int(c.maturity) == 0 and getattr(c, "doc_status", "") != "NA"
    ]

    # Evidence confidence
    raw_conf = evidence_confidence_from_controls(controls)
    evidence_confidence = int(round(raw_conf * 100))

    # Sector overrides
    critical_flags, overrides = apply_sector_overrides(
        sector=sector,
        language=language,
        category_maturity=category_maturity,
        controls=controls,
    )

    # Risk tier & readiness
    risk_tier = risk_tier_from(score, critical_flags)
    readiness = readiness_label(score, sector, language)
    if critical_flags:
        readiness = "BLOCKED" if language == "EN" else "BLOQUÉ"

    # Normative compliance layer (kept from your draft)
    normative_alignment: Dict[str, bool] = {
        "iso_42001": (
            category_maturity.get("monitoring", 0) >= 60
            and category_maturity.get("resilience", 0) >= 60
            and category_maturity.get("lifecycle", 0) >= 60
        ),
        "nist_ai_rmf": score >= 60,
        "eu_ai_act_lifecycle": category_maturity.get("lifecycle", 0) >= 60,
    }

    compliance_gaps: List[str] = []
    if category_maturity.get("resilience", 0) < 60:
        compliance_gaps.append("Resilience/adversarial robustness below normative expectations (MON-CORE-05).")
    if category_maturity.get("lifecycle", 0) < 60:
        compliance_gaps.append("Lifecycle governance/sunset authority below normative expectations (MON-CORE-06).")

    high_risk_mode = high_risk
    if high_risk_mode and compliance_gaps:
        regulatory_positioning = "Regulatory defensibility materially constrained."
    else:
        regulatory_positioning = "Governance posture broadly defensible subject to documentation evidence."

    # Optional roadmap generation
    roadmap = None
    try:
        roadmap = generate_remediation_roadmap(controls=controls, sector=sector, language=language)
    except Exception:
        roadmap = None

    result = GovernanceAssessmentResult(
        score=score,
        readiness=readiness,
        risk_tier=risk_tier,
        category_weights={k: round(v, 4) for k, v in weights.items()},
        category_maturity=category_maturity,
        category_weighted_points={k: round(v, 2) for k, v in category_points.items()},
        monitoring_core01=monitoring_core01,
        monitoring_core02=monitoring_core02,
        monitoring_composite=monitoring_composite,
        evidence_confidence=evidence_confidence,
        missing_elements=missing_elements,
        critical_flags=critical_flags,
        controls=controls,
        human_core01=human_core01,
        human_core02=human_core02,
        human_composite=human_composite,
        normative_alignment=normative_alignment,
        compliance_gaps=compliance_gaps,
        high_risk_mode=high_risk_mode,
        regulatory_positioning=regulatory_positioning,
    )

    # Attach extras if your model supports it
    for name, val in {"overrides": overrides, "remediation_roadmap": roadmap}.items():
        if val is None:
            continue
        try:
            setattr(result, name, val)
        except Exception:
            pass

    return result

## Related

- [[Research and Papers MOC]]
- [[PHAROS Recalibration — Unified Governance Architecture]]
