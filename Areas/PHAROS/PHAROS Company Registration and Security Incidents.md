---
type: wiki
title: PHAROS Company Registration and Security Incidents
aliases:
- PHAROS Company Registration and Security Incidents
tags:
- areas
- pharos
- pharos-company-registration-and-security-incidents-md
- manus
- fiscal
- registration
- rotation
- entreprise
- color-red
status: active
created: '2026-06-21'
updated: '2026-06-26'
vault_area: Areas
canonical_path: Areas/PHAROS/PHAROS Company Registration and Security Incidents.md
backlink_count: 16
backlinks:
- '[[Areas/PHAROS/Founder Charter — Lepage and Stocker]]'
- '[[Areas/PHAROS/Governance and PHAROS MOC]]'
- '[[wiki/Home]]'
- '[[wiki/Legal and Institutional Cases]]'
- '[[wiki/Martin Lepage Professional Identity]]'
- '[[Areas/PHAROS/Martin Lepage — Professional Profile]]'
- '[[Areas/PHAROS/PHAROS AI and Ethics Submission — Architecture Paper]]'
- '[[Areas/PHAROS/PHAROS Commercial Strategy]]'
- '[[Areas/PHAROS/PHAROS Legal Classification — CAE Code Strategy]]'
- '[[Areas/PHAROS/PHAROS Procurement-Unblock Sprint]]'
- '[[Areas/PHAROS/PHAROS-AI Webservice — pharos-ai.ca]]'
- '[[wiki/PHAROS-EMERAULD Consolidated Timeline 2024-04-01 to 2026-04-19]]'
- '[[Areas/Personal/Personal and Projects MOC]]'
- '[[wiki/TPS-TVQ PHAROS]]'
- '[[_vault/VAULT ADDITIONS TRACKER]]'
- '[[maps/PHAROS Method Map]]'
---

# PHAROS Company Registration and Security Incidents

## Summary
Administrative records for PHAROS Inc. (Québec) and a documented security incident involving an exposed API key. Related to [[PHAROS Runbook SOP]] and [[PHAROS Procurement-Unblock Sprint]].
For the Québec fiscal registration document that captures the TVQ + TPS/GST identifiers as a PDF artifact, see [[TPS-TVQ PHAROS]].

---

## Company Registration — PHAROS

**NEQ (Numéro d'entreprise du Québec)**: 2282012550

**Filings**:
- April 3, 2026: reference 020200132259394
- April 8, 2026: reference 020200132340191
- April 8, 2026: reference 020200132340205

**Payment confirmed**: 2026-04-08 13:29:03, authorization number 07097Z

**Start-up business registration (Inscription d'une entreprise en démarrage)**:
- Transmitted: 8 April 2026, 14:05:29 by Martin Lepage
- Reference number: 010500307500133

**Revenu Québec fiscal identifiers**:
- TVQ (Taxe de vente du Québec): `40 3352 4507 TQ 0001`
- TPS (Taxe sur les produits et services) / GST: `78997 3377 RT 0001`

These fiscal numbers activate PHAROS as a tax-collecting entity in Québec and federally, completing the registration loop that began with the NEQ assignment. See [[PHAROS Legal Classification — CAE Code Strategy]] for how the company is categorized for activity-code purposes.
See also [[TPS-TVQ PHAROS]] for the dedicated fiscal-registration PDF artifact.

---

## Security Incident — MANUS API Key Exposure

**What happened**: A Desktop Manus note contained a live API key in plaintext. Sanitized on 2026-03-31.

**Required action**: Rotate the Manus API key immediately in the Manus account surface before using it again. Keep the replacement key out of Desktop files.

**Safer local pattern after rotation**:
```bash
printf "export MANUS_API_KEY='REPLACE_AFTER_ROTATION'\n" > ~/.manus_env.sh
chmod 600 ~/.manus_env.sh
source ~/.manus_env.sh
```

**Status as of filing**: sanitized and noted; rotation required.

---

## Governance Note

Per the AGENTS.md and QUEEN-KEYPORT constraints: if a live token is exposed during work, rotation is part of closure, not optional cleanup. The MANUS note documents the first half (sanitization). The second half (actual rotation in the Manus account surface) must be verified.

---

## Sources
- `raw sources/DEMANDES REGISTRAIRE ENTREPRISE PHA.txt`
- `raw sources/MANUS.txt`
- Related: [[PHAROS Runbook SOP]]
- Related: [[TPS-TVQ PHAROS]] — fiscal registration PDF (TVQ + TPS identifiers)
- Related: [[Governance and PHAROS MOC]] — primary index for PHAROS administrative and legal records

## Related

- [[2022 - tax_or_finance_1.pdf - 2022 - tax_or_finance_1.pdf.pdf - 2022 - tax_or_finance_1.pdf - 2022 -]]
