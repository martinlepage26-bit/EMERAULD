---
type: raw
source_kind: pdf_text
source_path: /mnt/d/LIBRARY/Review/Unreadable/2026 - Martin Lepage - report.pdf - 2026 - Martin Lepage - report.pdf.pdf - 2026 - Martin Lepage - report.pdf - 2026 - Martin Lepage - report.pdf.pdf.pdf
source_rel: Review/Unreadable/2026 - Martin Lepage - report.pdf - 2026 - Martin Lepage - report.pdf.pdf - 2026 - Martin Lepage - report.pdf - 2026 - Martin Lepage - report.pdf.pdf.pdf
pages_total: 2
text_first_pages: 2
text_last_pages: 0
pdfinfo:
  Custom Metadata: "no"
  Encrypted: "no"
  File size: "76205 bytes"
  Form: "none"
  JavaScript: "no"
  Metadata Stream: "no"
  Optimized: "no"
  PDF version: "1.4"
  Page rot: "0"
  Page size: "596 x 842 pts (A4)"
  Pages: "2"
  Producer: "Skia/PDF m146 Google Docs Renderer"
  Suspects: "no"
  Tagged: "yes"
  Title: "Lepage_Martin_ATLAS_ThreatModeling_Report"
  UserProperties: "no"
dr_sort_original_filename: "2026 - Martin Lepage - report.pdf - 2026 - Martin Lepage - report.pdf.pdf - 2026 - Martin Lepage - report.pdf - 2026 - Martin Lepage - report.pdf.pdf.pdf.md"
dr_sort_original_path: "raw sources/D_LIBRARY_ingest_2026-04-26/ocr_unreadable/converted_ocr/Review/Unreadable/2026 - Martin Lepage - report.pdf - 2026 - Martin Lepage - report.pdf.pdf - 2026 - Martin Lepage - report.pdf - 2026 - Martin Lepage - report.pdf.pdf.pdf.md"
dr_sort_filename_normalized: "2026-05-06"
---

# Lepage_Martin_ATLAS_ThreatModeling_Report

## Extracted Text

ATLAS - Threat Modeling Report
ATLAS Technique ID Report
Data phase: T0821 (Data Poisoning)​
We’re pulling in public product FAQs that are scraped off the web, dumping them into a data
lake, then running ETL. That’s a pretty obvious weak spot: if someone manages to slip
garbage or manipulated content into what you’re scraping, that junk can end up shaping what
the model learns later.
Training phase: T0860 (AI Supply Chain Compromise)​
During training, we’re using open-source LLM libraries in the cloud. Which is fine, but it
also means your dependencies can become the attack path. If a library gets compromised, or a
“normal update” is actually malicious, you can end up training on top of a poisoned toolchain
and not even notice.
Deployment phase: T0843 (Model Inference)​
Then you deploy the chatbot behind a public API, and it’s trained using logs that contain PII.
So now people can hit the endpoint over and over, trying to coax the model into leaking
training details or sensitive info.
T0821: Someone messes with the scraped FAQ content so the model learns bad info or weird
behavior, and now your chatbot gives harmful answers and customers stop trusting it.
T0860: A compromised open-source dependency sneaks in a backdoor or changes model
behavior, and suddenly you’ve got a problem baked into the system at scale.
T0843: Attackers probe the API like a vending machine: keep shaking it until it drops private
stuff, like customer PII from the training logs.

Mitigation Recommendation Table
Phase

Technique
ID

Risk

Mitigation Recommendation

Data

T0821

Poisoned
web-scraped
FAQs contaminate the
dataset and bias model
behavior

Lock down where your data comes from. Use
source allowlists, run checks for “this looks
suspicious,” and do human spot-checks before
anything gets fed into training.

Model
Training

T0860

Compromised open-source
libraries inject malicious
code or model backdoors

Treat dependencies like a risk surface. Pin
versions, generate SBOMs, scan for known
issues, and only use signed artifacts in your
training pipeline.

Deployment

T0843

Model inference extracts
sensitive information from
training data via public
API probing

Don’t let the API be a free-for-all. Rate limit
it, monitor for probing behavior, filter outputs
for sensitive data, and ideally strip or redact
PII before it ever touches training in the first
place.

Reflection
MITRE ATLAS stops people from waving their hands about “AI risk” like it’s a vibe. It
makes you point to where things can get screwed: poisoned scraped data, sketchy third-party
libraries, and a public API people can probe until the model leaks something. Then you put
guardrails where they actually matter, not after it’s already a mess.

## Related

- [[Research and Papers MOC]]
- [[Reddit Data API — Access Terms and Rate Limits]]
