// ─────────────────────────────────────────────
// Quebec Law 25 Compliance Engine
// Loi 25 — Loi modernisant des dispositions législatives
// en matière de protection des renseignements personnels
// ─────────────────────────────────────────────

import type { ImpactAssessment, GovernedSystem, Policy } from "../types";

// ── Law 25 Sections ────────────────────────────

export const LAW25_SECTIONS: Record<string, string> = {
  "3.8":  "Information about personnel responsibility must be published on website",
  "8":    "Consent must be given for collection of personal information",
  "8.1":  "Consent for sensitive personal information must be explicit",
  "12":   "Right to access personal information",
  "12.1": "Automated decision-making — transparency and right to human review",
  "17":   "Incident response — notification within 72 hours",
  "18.1": "Privacy Impact Assessment (PIA) required for new projects involving personal data",
  "20.1": "Data retention — destruction after purpose fulfilled",
  "21":   "Third-party data processing agreements",
  "26":   "Commissioner oversight and reporting",
};

export const SECTION_12_1_REQUIREMENTS = [
  "Disclose that an automated decision is being made",
  "Explain the personal information factors used in the decision",
  "Provide the right to request human review",
  "Offer opportunity to submit observations",
  "Inform about the right to request correction",
];

// ── Transparency Notice Generator ─────────────

export interface TransparencyNoticeOptions {
  systemName: string;
  decisionType: string;
  dataCategories: string[];
  retentionDays: number;
  hasHumanReview: boolean;
  contactEmail: string;
  organizationName: string;
  language: "en" | "fr";
}

export function generateSection12_1Notice(opts: TransparencyNoticeOptions): string {
  const {
    systemName,
    decisionType,
    dataCategories,
    retentionDays,
    hasHumanReview,
    contactEmail,
    organizationName,
    language,
  } = opts;

  if (language === "fr") {
    return `AVIS DE DÉCISION AUTOMATISÉE
Conformément à l'article 12.1 de la Loi 25 (Loi modernisant des dispositions législatives en matière de protection des renseignements personnels)

Système : ${systemName}
Organisation : ${organizationName}

1. NATURE DE LA DÉCISION AUTOMATISÉE
${organizationName} utilise un système d'aide à la décision automatisée (${systemName}) pour effectuer les évaluations suivantes : ${decisionType}.

2. RENSEIGNEMENTS PERSONNELS UTILISÉS
Les catégories de renseignements personnels suivantes sont utilisées dans le processus de décision :
${dataCategories.map((c) => `  • ${c}`).join("\n")}

3. DURÉE DE CONSERVATION
Les renseignements personnels utilisés dans ce processus sont conservés pendant ${retentionDays} jours, après quoi ils sont détruits de manière sécuritaire conformément à l'article 20.1 de la Loi 25.

4. VOS DROITS
Conformément à la Loi 25, vous disposez des droits suivants :
  • Droit d'accès à vos renseignements personnels (art. 12)
  • Droit à la rectification des renseignements inexacts (art. 12)
  ${hasHumanReview ? "• Droit de demander une révision humaine de la décision automatisée (art. 12.1)\n  • Droit de soumettre des observations avant qu'une décision finale soit prise (art. 12.1)" : "• Droit de contester la décision auprès du responsable de la protection des renseignements personnels"}
  • Droit de déposer une plainte auprès de la Commission d'accès à l'information (art. 26)

5. CONTACT
Pour exercer vos droits ou obtenir plus d'informations :
Responsable de la protection des renseignements personnels
${organizationName}
Courriel : ${contactEmail}

Date d'entrée en vigueur : ${new Date().toLocaleDateString("fr-CA")}`;
  }

  return `AUTOMATED DECISION NOTICE
Pursuant to Section 12.1 of Act 25 (An Act to modernize legislative provisions as regards the protection of personal information)

System: ${systemName}
Organization: ${organizationName}

1. NATURE OF AUTOMATED DECISION
${organizationName} uses an automated decision-support system (${systemName}) to perform the following assessments: ${decisionType}.

2. PERSONAL INFORMATION USED
The following categories of personal information are used in the decision process:
${dataCategories.map((c) => `  • ${c}`).join("\n")}

3. RETENTION PERIOD
Personal information used in this process is retained for ${retentionDays} days, after which it is securely destroyed in accordance with Section 20.1 of Act 25.

4. YOUR RIGHTS
Under Act 25, you have the following rights:
  • Right to access your personal information (s. 12)
  • Right to rectification of inaccurate information (s. 12)
  ${hasHumanReview ? "• Right to request human review of the automated decision (s. 12.1)\n  • Right to submit observations before a final decision is made (s. 12.1)" : "• Right to challenge the decision with the Privacy Officer"}
  • Right to file a complaint with the Commission d'accès à l'information (s. 26)

5. CONTACT
To exercise your rights or obtain further information:
Privacy Officer
${organizationName}
Email: ${contactEmail}

Effective Date: ${new Date().toLocaleDateString("en-CA")}`;
}

// ── Compliance Score Calculator ────────────────

export interface ComplianceCheckResult {
  score: number;           // 0–100
  checks: ComplianceCheck[];
  criticalGaps: string[];
  recommendations: string[];
}

export interface ComplianceCheck {
  section: string;
  description: string;
  status: "PASS" | "FAIL" | "WARN" | "NA";
  detail: string;
}

export function calculateComplianceScore(
  assessment: ImpactAssessment,
  system: GovernedSystem,
  policies: Policy[]
): ComplianceCheckResult {
  const checks: ComplianceCheck[] = [];
  const criticalGaps: string[] = [];
  const recommendations: string[] = [];

  // 3.8 — Published responsibility
  checks.push({
    section: "3.8",
    description: "Privacy responsibility published",
    status: "WARN",
    detail: "Cannot be automatically verified — requires manual confirmation",
  });

  // 8 — Consent
  const hasConsentPolicy = policies.some(
    (p) => p.law25Section === "8" && p.status === "ACTIVE"
  );
  checks.push({
    section: "8",
    description: "Consent collection policy active",
    status: hasConsentPolicy ? "PASS" : "FAIL",
    detail: hasConsentPolicy
      ? "Active L1/L2 policy governs consent collection"
      : "No active consent policy found",
  });
  if (!hasConsentPolicy) criticalGaps.push("Missing active consent collection policy (s. 8)");

  // 12.1 — Automated decision transparency
  if (assessment.automaticDecisionMaking) {
    checks.push({
      section: "12.1",
      description: "Automated decision transparency notice generated",
      status: assessment.section12_1Notice ? "PASS" : "FAIL",
      detail: assessment.section12_1Notice
        ? "Notice on file"
        : "Notice not yet generated",
    });
    checks.push({
      section: "12.1",
      description: "Human oversight (HITL) enabled",
      status: assessment.humanOversightEnabled ? "PASS" : "FAIL",
      detail: assessment.humanOversightEnabled
        ? "HITL queue configured"
        : "No human review mechanism defined",
    });
    if (!assessment.section12_1Notice)
      criticalGaps.push("Generate Section 12.1 transparency notice");
    if (!assessment.humanOversightEnabled)
      criticalGaps.push("Configure human-in-the-loop (HITL) review mechanism");
  } else {
    checks.push({
      section: "12.1",
      description: "Automated decision-making",
      status: "NA",
      detail: "System does not make automated decisions",
    });
  }

  // 17 — Incident response
  const hasIncidentPolicy = policies.some(
    (p) => p.law25Section === "17" && p.status === "ACTIVE"
  );
  checks.push({
    section: "17",
    description: "Incident response policy (72h notification)",
    status: hasIncidentPolicy ? "PASS" : "WARN",
    detail: hasIncidentPolicy
      ? "Incident response policy active"
      : "No incident response policy linked to Law 25 s.17",
  });
  if (!hasIncidentPolicy)
    recommendations.push("Define an incident response policy linked to s. 17 (72h notification)");

  // 18.1 — PIA
  checks.push({
    section: "18.1",
    description: "Privacy Impact Assessment completed",
    status:
      assessment.status === "COMPLETE"
        ? "PASS"
        : assessment.status === "IN_PROGRESS"
        ? "WARN"
        : "FAIL",
    detail:
      assessment.status === "COMPLETE"
        ? `PIA completed. Risk score: ${assessment.riskScore}/100`
        : assessment.status === "IN_PROGRESS"
        ? "PIA in progress"
        : "PIA not started",
  });
  if (assessment.status === "NOT_STARTED")
    criticalGaps.push("Complete Privacy Impact Assessment (PIA) per s. 18.1");

  // 20.1 — Retention
  checks.push({
    section: "20.1",
    description: "Data retention policy defined",
    status: assessment.retentionPeriodDays > 0 ? "PASS" : "FAIL",
    detail:
      assessment.retentionPeriodDays > 0
        ? `Retention: ${assessment.retentionPeriodDays} days`
        : "No retention period defined",
  });

  // 21 — Third-party
  if (assessment.thirdPartySharing) {
    const hasThirdPartyPolicy = policies.some(
      (p) => p.law25Section === "21" && p.status === "ACTIVE"
    );
    checks.push({
      section: "21",
      description: "Third-party processing agreements",
      status: hasThirdPartyPolicy ? "PASS" : "FAIL",
      detail: hasThirdPartyPolicy
        ? "Third-party policy active"
        : "Third-party sharing detected but no policy governs it",
    });
    if (!hasThirdPartyPolicy)
      criticalGaps.push("Third-party data sharing without governing policy (s. 21)");
  }

  // Score calculation
  const scorable = checks.filter((c) => c.status !== "NA");
  const passed = scorable.filter((c) => c.status === "PASS").length;
  const warned = scorable.filter((c) => c.status === "WARN").length;
  const score = scorable.length === 0
    ? 0
    : Math.round(((passed + warned * 0.5) / scorable.length) * 100);

  if (score < 60) recommendations.push("Immediate compliance remediation required — score below 60");
  else if (score < 80) recommendations.push("Review and address WARN items before next audit cycle");

  return { score, checks, criticalGaps, recommendations };
}