---
type: template
title: Invoice Template Pharos-AI
aliases:
- Invoice Template Pharos-AI
- Facture Template Pharos-AI
- Pharos-AI Invoice
- templates/Invoice Template Pharos-AI
tags:
- template
- pharos-ai
- invoice
- billing
- templates
- invoice-template-pharos-ai-md
- navy
- client
- cream
- gold
- color-orange
status: active
created: '2026-04-25'
updated: '2026-06-26'
vault_area: templates
canonical_path: templates/Invoice Template Pharos-AI.md
backlink_count: 1
backlinks:
- '[[memory/clients/ExterminationDG]]'
---

# Invoice Template Pharos-AI

## Summary

Print-ready A5 invoice template for [[Pharos-AI]] using the canonical pharos-ai.ca brand palette (navy + gold + cream). The HTML companion lives at `templates/Invoice Template Pharos-AI.html` and is intended to be filled in token-by-token, then printed to PDF via headless Chrome. First production use: [[ExterminationDG]] facture 001 (2026-04-25).

## Context

Built when no Pharos-AI invoice template existed in the [[Hermes Dashboard — Professional Governance Tool]] client lane. Companion to the [[CLIENT ACCOUNTS]] tracker — every active client account ([[ExterminationDG]], [[Lavoie Construct]], [[Sante-France]], [[Progression]]) can use this template for billing.

Brand alignment is sourced from the production `site.css` of the pharos-ai-release-candidate-2026-03-14 build, not from the experimental cyan/navy logo SVG. The site's actual public identity is editorial navy + gold on cream, which fits an invoice's institutional posture better than a neon-cyan dashboard look.

## Details

### File location
- Template HTML: `/mnt/c/Users/softinfo/Documents/EMERAULD/templates/Invoice Template Pharos-AI.html`
- This note: `/mnt/c/Users/softinfo/Documents/EMERAULD/templates/Invoice Template Pharos-AI.md`

### Brand palette (extracted from pharos-ai.ca)
| Token | Hex | Role |
|---|---|---|
| `--navy-900` | `#10162A` | Primary text, accent bar start |
| `--navy-800` | `#13254C` | Mid-tone navy |
| `--navy-700` | `#20314F` | Body meta text |
| `--navy-600` | `#0F1D37` | Dark surface |
| `--gold` | `#D8C08A` | Accent, client border, total underline |
| `--cream` | `#FBF7EF` | Card background |
| `--cream-2` | `#FFFDF8` | Sheet background |
| `--line` | `#E8E1CF` | Divider lines |

### Typography
- Display / wordmark: `Sora`, `Avenir Next`, system-ui (Pharos canonical display font)
- Body: `Manrope`, `Inter`, Helvetica Neue, system-ui (Pharos canonical body font)
- Both fall back gracefully to OS sans-serif if the web fonts are not available offline (which is the print case).

### Logo
A minimal inline-SVG mark inspired by the [[Pharos]] lighthouse motif: navy disc with five gold beam rays, central gold node, and a triangular tower base with a horizontal beam. ~30 lines of SVG vs. the 300-line full mark — designed for fast PDF render and small physical size (14mm). Editable directly inside the template.

### Tokens to replace per invoice
- `{{INVOICE_NO}}` — e.g. `001`
- `{{INVOICE_DATE}}` — e.g. `25 avril 2026`
- `{{CLIENT_NAME}}` — e.g. `Extermination DG`
- `{{CLIENT_ADDRESS_LINE1}}` — e.g. `2481, rue Fillion`
- `{{CLIENT_CITY_PROVINCE_POSTAL}}` — e.g. `Saguenay (QC)  G7S 4S7`
- `{{CLIENT_PHONE}}`
- `{{CLIENT_EMAIL}}`
- `{{ITEM_DESCRIPTION}}`, `{{ITEM_QTY}}`, `{{ITEM_UNIT_PRICE}}`, `{{ITEM_TOTAL}}`
- `{{SUBTOTAL}}`, `{{TOTAL}}`
- (optional) `{{TPS}}`, `{{TVQ}}` if billing taxes — uncomment the rows in `.totals`

### Generating the PDF
From WSL:

```bash
"/mnt/c/Program Files/Google/Chrome/Application/chrome.exe" \
  --headless --disable-gpu --no-sandbox --no-pdf-header-footer \
  --print-to-pdf="C:\\path\\to\\output.pdf" \
  "file:///C:/path/to/filled-invoice.html"
```

Margins are baked into `@page { size: A5; margin: 12mm 14mm }` so do not pass extra margin flags.

### Hard rules
- Format A5, single page.
- No taxes calculated unless explicitly added (Pharos-AI is currently invoicing without provincial taxes by default; verify per-client before adding).
- Always show the Pharos-AI TPS/TVH number; never the client's tax numbers.
- `À confirmer` is the canonical placeholder for missing client address — never invent.

## Related

- [[Pharos-AI]] — emitter brand
- [[ExterminationDG]] — first client to use this template
- [[CLIENT ACCOUNTS]] — vault snapshot of active client accounts
- [[Hermes Dashboard — Professional Governance Tool]] — operator-facing billing surface
- [[Personal and Projects MOC]]
- [[Readme]]
- [[2021 - Martin Lepage - tax_or_finance [2]]]
- [[2026 - statement_or_bill]]
- [[Gestion de l'inventaire des kits de collection]]
- [[Lepage, Martin]]
