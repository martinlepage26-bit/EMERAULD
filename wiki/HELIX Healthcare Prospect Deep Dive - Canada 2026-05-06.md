---
type: wiki
aliases: ["HELIX healthcare prospects", "HELIX health deep dive", "HELIX Canada health AI"]
tags: [helix, prospects, clients, commercial, ai-governance, healthcare, quebec, canada, law25, pipeda]
status: active
created: 2026-05-06
updated: 2026-05-06
---

# HELIX Healthcare Prospect Deep Dive - Canada 2026-05-06

## Summary

Deep research pass on Canadian healthcare AI prospects for [[HELIX — Value Proposition and Buyer Profile]]. Extends [[HELIX Regional Prospect Deep Sweep - Montreal Quebec Toronto Ottawa 2026-05-06]] and [[HELIX Hermes-Assisted Prospect Extension - Canada Regulated AI Routes 2026-05-06]]. All candidates have deployed or publicly announced AI inside regulated health workflows with documented auditability, traceability, or governance pressure.

Key intelligence: **Law 25 s.12.1 (Quebec automated decision disclosure, enforced September 2024)** is the sharpest HELIX entry point. First Quebec enforcement penalty (C$50K) landed late 2025. Every Quebec health AI deployment is now inside the enforcement window.

For the operator-side diagnostic method that keeps vendor claims bounded (truth-claim pressure, “ingestion” semantics, and booby-trap continuity tests), see [[EMERGENT HELIX Session — Truth Claims, Ingestion, and Booby-Trap Diagnostics (2026-05-07)]].

## Critical Intelligence

**Airudi is the single highest-priority new contact.** Montreal-based SME with two separate public-sector Quebec health AI deployments — Urgences-santé MODUS (prehospital dispatch) and MUHC ENACT (nursing assignment). One Airudi relationship opens both as HELIX buyers. They have a Mila partnership and explicit public governance framing.

**Law 25 s.12.1 is the sharpest entry point.** Automated decisions affecting patients, claimants, or workers in Quebec require disclosure of the logic and an offer of human review. The enforcement window opened September 2024. iA Financial, GreenShield Quebec members, MUHC, CHUM, and every CISSS are exposed.

**OntarioMD VOR multiplier.** The AI Scribe VOR program lists 18 vendors. Each vendor needs HELIX more than OntarioMD does. Target the vendors, not the broker.

**Canada Health Infoway AI Scribe Program** — 10,000+ physician AI tools deployed nationally. A Policy Options article (April 2026) explicitly named "privacy and safety risks." Infoway has procurement governance but no output-level audit instrument. HELIX is that instrument.

## Tier 1 — Initiate Immediately

### Airudi — Urgences-santé MODUS + MUHC ENACT
**Region:** Montreal, Quebec  
**AI deployed:**
- MODUS — ML dispatch optimization for Quebec prehospital 911 (Urgences-santé). Predicts call volume, allocates paramedic deployment scenarios.
- ENACT — AI patient assignment, task delegation, documentation automation, shift handover at Montreal General Hospital. $1.8M, Scale AI + MGH Foundation funded.

**Regulatory pressure:** Law 25 s.12.1 (automated decisions affecting paramedic staffing and patient assignment), MSSS AI Plan 2024-2027, Loi sur les services préhospitaliers d'urgence  
**HELIX fit:** MODUS dispatches paramedics via ML; ENACT assigns patients to nurses. Both are high-stakes automated decisions. Diagnostic: what reasoning trace exists if a dispatch is challenged or an assignment disputed? What does the audit log show after an adverse event?  
**First move:** Contact Airudi directly (Montreal SME, publicly reachable). Frame: "You're running ML decisions on Quebec's public emergency and hospital systems. Law 25 requires you to explain those decisions. HELIX gives you the audit-ready evidence packet before the MSSS asks."  
**Sources:**
- airudi.com/en/news/urgences-sante-capitalizes-on-artificial-intelligence-to-optimize-prehospital-care/
- muhc.ca/news-and-patient-stories/news/muhc-unlocks-nursing-potential-artificial-intelligence
- airudi.com/en/news/airudi-launches-enact-ai-solution-that-unlocks-full-potential-of-nursing/

---

### iA Financial Group — FICO Automated Underwriting
**Region:** Quebec City (HQ), national  
**AI deployed:** FICO Platform for automated life insurance underwriting. Currently 50%+ automation, targeting 80% by 2030. Won FICO Vanguard Award April 2025. Absorbed SSQ Vie (group health benefits).  
**Regulatory pressure:** Law 25 s.12.1, PIPEDA, AMF, OSFI model risk governance. Automated underwriting decisions touching health data are mandatory-disclosure automated decisions under Quebec law.  
**HELIX fit:** One automated underwriting decision output. What factors drove the decline or premium loading? Can iA produce a disclosure-ready explanation per Law 25 s.12.1?  
**First move:** Chief Compliance Officer or VP Actuarial/Underwriting Innovation. Frame: "You've publicly announced 80% automation by 2030. Law 25 requires you to explain every automated decision that materially affects a claimant. One HELIX diagnostic is cheaper than the first AMF inquiry."  
**Sources:**
- fico.com/en/newsroom/ia-financial-group-expands-insurance-underwriting-fico-platform-aiming-80-automation
- businesswire.com/news/home/20250423742134/en/iA-Financial-Group-Expands-Insurance-Underwriting-with-FICO-Platform-Aiming-for-80-Automation

---

### GreenShield Canada — Claim Watch AI Fraud Detection
**Region:** National (Toronto HQ; Quebec members)  
**AI deployed:** Claim Watch — benefits fraud detection AI since 2017. Peer-to-peer analysis, predictive modeling, social network analysis. Now contributing to CLHIA industry-wide AI data pooling. AI therapist matching algorithm (mental health, 94% match retention).  
**Regulatory pressure:** PIPEDA, Law 25 (fraud AI flags are automated decisions affecting claimants — mandatory disclosure), OSFI, provincial insurance regulation.  
**HELIX fit:** One Claim Watch decision on a flagged claim. What drove the flag? Can a claimant or adjudicator follow the reasoning chain? What is the human override process for a wrongly denied claim?  
**First move:** VP Benefits Operations or Chief Compliance Officer. Frame through the CLHIA data pooling angle — they are now sharing de-identified data across carriers through a central AI platform. That inter-carrier AI has shared governance liability. HELIX diagnostic before the first OPC or AMF complaint.  
**Sources:**
- greenshield.ca/en-ca/our-stories/claim-watch-ai-is-not-just-a-buzzword
- greenshield.ca/en-ca/newsroom/green-shield-canada-s-claim-watch-to-participate-in-data-pooling-to-reduce-benefits-fraud

---

### WELL Health / HEALWELL AI — WELLTRUST + Nexus AI + WELL AI Decision Support
**Region:** Vancouver HQ; national clinic network  
**AI deployed:**
- WELL AI Decision Support — embedded in EMR, flags clinical risk to physicians
- Nexus AI — ambient scribe deployed Canada-wide via Infoway program
- WELLTRUST — consent-first data governance and AI patient identification for clinical trials (February 2026)

**Regulatory pressure:** PIPEDA, PHIPA, Law 25 (Quebec clinics), Bill C-27. WELLTRUST explicitly claims "Canadian privacy and regulatory standards." TSX-listed (TSX:WELL).  
**HELIX fit:** (a) WELL AI Decision Support — one clinical flag output: what drove it, what is the physician override? (b) WELLTRUST — one clinical trial patient identification output: what made a patient eligible?  
**First move:** HEALWELL AI (subsidiary, separately listed as TSX:HWAIF). Chief Medical Officer or VP Clinical AI. Frame: "You've publicly committed to ethical AI. HELIX makes that claim independently auditable — useful for Infoway compliance and provincial college relationships."  
**Sources:**
- news.healwell.ai/news-releases/healwell-ai-and-well-health-launch-welltrust...
- well.company/well-ai-decision-support/
- news-releases.well.company/news-releases/wellstar-technologies-launches-nexus-ai...

---

## Tier 2 — Strong Fit, After Tier 1

### OntarioMD VOR Program — AI Scribe Vendor Channel
**Region:** Ontario (Toronto)  
**AI deployed:** VOR (Vendor of Record) program, April 2025–2028. 18 pre-vetted AI scribe vendors serving Ontario physicians. IPC (Ontario Information and Privacy Commissioner) issued guidance February 2026 requiring audit logs, privacy impact assessments, and breach notification.  
**HELIX fit:** Not OntarioMD as buyer — the 18 VOR vendors are the targets. Each vendor needs HELIX as compliance proof for VOR renewal. Top vendors to investigate: Suki AI, Abridge, Nuance DAX (Microsoft), Nabla, Tali AI, ScribeBerry.  
**First move:** Approach OntarioMD Director of Digital Health Adoption as a channel ("You have 18 VOR vendors and no output-level audit instrument — HELIX is that instrument"). Or approach individual VOR vendors directly.  
**Sources:**
- ontariomd.blog/2025/06/03/introducing-ontarios-first-vendor-of-record-vor-program-for-ai-scribes/
- supplyontario.ca/vor/software/tender-20123-artificial-intelligent-solutions-ai-scribe/

---

### Canada Health Infoway — AI Scribe Program (National Scale)
**Region:** National (Toronto HQ)  
**AI deployed:** Coordinating federally funded AI scribe licenses to 10,000+ primary care physicians across Canada.  
**Governance signals:** April 2026 Policy Options article explicitly named "privacy and safety risks" in the program's distributed AI scribes. Infoway has procurement governance but no output-level audit instrument.  
**HELIX fit:** Infoway as channel to 10,000 physicians and 18+ vendors. HELIX positioned as national output audit standard for AI scribe quality and governance compliance.  
**First move:** Infoway VP Digital Health Solutions or Director AI Initiatives. Frame: "You are accountable for 10,000 physician AI tools with no output-level audit. One HELIX run on a single vendor's workflow gives you a reproducible governance standard before the first OPC complaint."  
**Sources:**
- infoway-inforoute.ca/en/featured-initiatives/ai-scribe-program
- policyoptions.irpp.org/2026/04/ai-scribes-health-care-canada-privacy-safety-risks/

---

### CHUM — Infusion Clinic AI + Care Pathway Automation (Montreal)
**Region:** Montreal, Quebec  
**AI deployed:** (a) AI-driven infusion clinic scheduling (Scale AI funded, 5% efficiency gain, 11 extra treatment hours/day). (b) "Gray" system — automates and optimizes patient care pathways and appointment management.  
**Regulatory pressure:** Law 25 (public hospital, automated patient scheduling decisions), MSSS AI Plan 2024-2027, Santé Québec governance.  
**HELIX fit:** One infusion scheduling output. Why was this patient scheduled at this time? If treatment is delayed due to a model output, what is the audit record?  
**First move:** CHUM VP Operations or the CHUM École d'intelligence artificielle en santé (EIAS). EIAS is focused on responsible AI in clinical environments — natural HELIX ally. Frame as pilot validation study in the language of an academic hospital center.  
**Sources:**
- scaleai.ca/scale-ai-healthcare-initiative-21-million/
- eiaschum.ca/en/

---

### MUHC — Cardiac Imaging AI + Nursing AI (Scale AI funded)
**Region:** Montreal, Quebec  
**AI deployed:** Scale AI funded cardiac imaging AI (image analysis) and nursing staff management AI, separate from ENACT. Three total AI projects at MUHC.  
**HELIX fit:** Cardiac imaging diagnostic — what drove a flagged finding? What is the failure mode for a false negative on a critical cardiac finding?  
**First move:** Same relationship as ENACT — MUHC VP Research or Director Quality and Patient Safety covers all three projects.  
**Sources:**
- muhc.ca/news-and-patient-stories/news/scale-ai-funds-two-muhc-ai-projects-aimed-improving-cardiac-imaging

---

### Intelerad — InteleGence AI Radiology Platform (Montreal HQ)
**Region:** Montreal HQ; national and global deployments; Quebec via Imagix Medical (13 clinics, Brossard)  
**AI deployed:** InteleGence — AI integration layer for radiology. Open API ingesting third-party AI algorithms into PACS/VNA workflow. GE HealthCare acquisition pending (announced November 2024, close H1 2026).  
**Regulatory pressure:** Health Canada SaMD Class II/III, PIPEDA, Law 25, provincial health information acts.  
**HELIX fit:** Platform accountability vs. algorithm accountability gap. Who is responsible when a third-party AI algorithm running inside Intelerad flags something incorrectly — Intelerad, the vendor, or the radiologist? HELIX produces the evidence packet.  
**First move:** VP Product or Chief Medical Officer. Frame through GE acquisition: "GE's due diligence will ask about your AI algorithm accountability framework. HELIX gives you an auditable answer before they ask."  
**Sources:**
- intelerad.com/en/press-releases/intelerad-introduces-intelegence-to-power-ai-driven-radiology/
- investor.gehealthcare.com/news-releases/news-release-details/ge-healthcare-acquire-intelerad-advancing-cloud-enabled

---

### Jane App — AI Scribe + AI-Assisted Scheduling
**Region:** Vancouver HQ; national including Quebec clinics; 200,000+ practitioners  
**AI deployed:** AI Scribe (ambient clinical notes, 2024), AI-assisted scheduling, patient communication drafting. On Infoway VOR list.  
**Governance signals:** Published "AI Principles" page naming human review and transparency — aspirational, not operationally verified.  
**HELIX fit:** One AI Scribe session. Does the drafted note accurately reflect clinical reasoning? What is the failure mode when the AI mishears or misinterprets?  
**First move:** Chief Product Officer or Head Clinical Compliance. Frame: "Your AI Principles page is aspirational. HELIX makes it independently verifiable — useful for Infoway compliance and provincial college relationships."  
**Sources:**
- jane.app/guide/jane-s-ai-principles
- jane.app/features/charting-ai-scribe

---

### Avitia — AI Cancer Diagnostics (Montreal)
**Region:** Montreal, Quebec  
**AI deployed:** AI-powered molecular cancer testing platform. Built on Imagia Canexia assets. Mila partnership. 40,000+ cancer mutation tests run. $5M seed, February 2025.  
**Regulatory pressure:** Health Canada SaMD Class II/III, PIPEDA, Law 25. Highest patient-harm exposure of any healthcare AI application.  
**HELIX fit:** One cancer diagnostic output. What drove a mutation call? What is the false negative failure mode for a missed mutation?  
**First move:** Co-founders (Montreal startup, directly reachable). Frame: "You need Health Canada SaMD authorization. The governance documentation HELIX produces is exactly what Health Canada's pre-market ML device guidance expects. Run one diagnostic now rather than explaining a failure case later."  
**Sources:**
- avitia.bio/press/avitia-launches-ai-powered-platform-for-rapid-point-of-care-cancer-testing
- betakit.com/avitia-raises-5-million-seed-round-to-expand-reach-of-ai-powered-cancer-diagnostics-platform/

---

### TELUS Health — Kroll Clinical Decision Support + MyCare
**Region:** National (Vancouver/Calgary HQ)  
**AI deployed:** Kroll pharmacy management (50%+ Canadian pharmacy market share) — clinical decision support for minor ailment prescribing, RxVigilance drug interaction AI. MyCare virtual care platform (formerly Babylon).  
**Regulatory pressure:** PIPEDA, provincial pharmacy regulations, OPQ, Law 25. OPC previously raised concerns about MyCare privacy impact assessment gap.  
**HELIX fit:** (a) Kroll minor ailment prescribing decision. (b) MyCare symptom checker output.  
**First move:** Chief Privacy Officer or VP Digital Health Compliance. Frame HELIX as evidence of current compliance — address the historic OPC gap, not repeat it.  
**Sources:**
- telus.com/en/health/health-professionals/pharmacies/kroll

---

## Tier 3 — Viable, Longer Path

| Candidate | Region | Signal | Note |
|---|---|---|---|
| CHU de Québec-Université Laval | Quebec City | MRI AI + anesthesia AI (MSSS plan) | Academic hospital, long procurement cycle |
| Mednow / PocketPills | National | Digital pharmacy, prescription automation AI | Weak AI specificity in public sources |
| OntarioMD VOR vendors (Suki, Abridge, Nuance DAX, Nabla, Tali AI, ScribeBerry) | Ontario/National | Each on or pursuing the 18-vendor VOR list | Approach individually as compliance proof targets |

*Note: Imagia Canexia Health is defunct (August 2023 bankruptcy). Its assets are now Avitia.*

---

## Clinic and Hospital Buyer Routes

For **private clinics** (not hospital networks): Jane App (200k+ practitioners), AuraScribe (Quebec Law 25 positioning), and OntarioMD VOR vendors are the relevant routes — HELIX enters through the platform vendor, not the individual clinic.

For **hospital networks** (CISSS/CIUSSS, CHU, academic hospitals): Airudi (MUHC/Urgences-santé), CHUM EIAS, and CHU de Québec are the Quebec hospital targets. Scale AI is a funding-path signal — any hospital with a Scale AI-funded AI project has a governance documentation obligation attached to the funding.

CISSS/CIUSSS networks are administrative coordinators, not AI buyers — they don't build or procure AI systems directly. The AI in Quebec hospitals sits in research institutions with Scale AI/Mila partnerships (MUHC, CHUM) and in the platform vendors serving individual clinicians. No separate CISSS/CIUSSS sweep needed.

---

## Source URLs for Scraping

Priority scrape targets (raw captures not yet in vault):

- https://airudi.com/en/news/urgences-sante-capitalizes-on-artificial-intelligence-to-optimize-prehospital-care/
- https://airudi.com/en/
- https://muhc.ca/news-and-patient-stories/news/muhc-unlocks-nursing-potential-artificial-intelligence
- https://airudi.com/en/news/airudi-launches-enact-ai-solution-that-unlocks-full-potential-of-nursing/
- https://www.fico.com/en/newsroom/ia-financial-group-expands-insurance-underwriting-fico-platform-aiming-80-automation
- https://www.greenshield.ca/en-ca/our-stories/claim-watch-ai-is-not-just-a-buzzword
- https://www.greenshield.ca/en-ca/newsroom/green-shield-canada-s-claim-watch-to-participate-in-data-pooling-to-reduce-benefits-fraud
- https://news.healwell.ai/news-releases/healwell-ai-and-well-health-launch-welltrust-to-empower-patients-and-accelerate-ai-powered-ethical-patient-identification-for-clinical-research/
- https://well.company/well-ai-decision-support/
- https://news-releases.well.company/news-releases/wellstar-technologies-launches-nexus-ai-a-transformative-ai-platform-for-canadian-healthcare-providers/
- https://ontariomd.blog/2025/06/03/introducing-ontarios-first-vendor-of-record-vor-program-for-ai-scribes/
- https://www.infoway-inforoute.ca/en/featured-initiatives/ai-scribe-program
- https://policyoptions.irpp.org/2026/04/ai-scribes-health-care-canada-privacy-safety-risks/
- https://eiaschum.ca/en/
- https://www.scaleai.ca/scale-ai-healthcare-initiative-21-million/
- https://www.intelerad.com/en/press-releases/intelerad-introduces-intelegence-to-power-ai-driven-radiology/
- https://www.intelerad.com/en/all-products/intelegence/
- https://jane.app/guide/jane-s-ai-principles
- https://jane.app/features/charting-ai-scribe
- https://www.avitia.bio/press/avitia-launches-ai-powered-platform-for-rapid-point-of-care-cancer-testing
- https://betakit.com/avitia-raises-5-million-seed-round-to-expand-reach-of-ai-powered-cancer-diagnostics-platform/
- https://www.avitia.bio/platform

---

## Related

- [[HELIX Regional Prospect Deep Sweep - Montreal Quebec Toronto Ottawa 2026-05-06]]
- [[HELIX Hermes-Assisted Prospect Extension - Canada Regulated AI Routes 2026-05-06]]
- [[HELIX Potential Clients - Source Sweep 2026-05-06]]
- [[HELIX — Value Proposition and Buyer Profile]]
- [[PHAROS Commercial Strategy]]
- [[Supply Chain Enforcement — Secondary Pressure on AI System Vendors]]
- [[2026-05-05_artificial-intelligence]]
- [[2026-05-05_artificial-intelligence-at-rbc]]
- [[AI is speeding into healthcare. Who should regulate it]]
