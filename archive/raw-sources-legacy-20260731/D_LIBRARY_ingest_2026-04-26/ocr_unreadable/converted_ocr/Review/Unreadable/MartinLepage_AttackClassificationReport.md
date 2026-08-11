---
type: raw
source_kind: pdf_text
source_path: /mnt/d/LIBRARY/Review/Unreadable/Invoice_2026_UnknownAuthor_MartinLepage_AttackClassificationReport.pdf - Invoice_2026_UnknownAuthor_MartinLepage_AttackClassificationReport.pdf - Invoice_2026_UnknownAuthor_MartinLepage_AttackClassificationRep.pdf
source_rel: Review/Unreadable/Invoice_2026_UnknownAuthor_MartinLepage_AttackClassificationReport.pdf - Invoice_2026_UnknownAuthor_MartinLepage_AttackClassificationReport.pdf - Invoice_2026_UnknownAuthor_MartinLepage_AttackClassificationRep.pdf
pages_total: 1
text_first_pages: 1
text_last_pages: 0
pdfinfo:
  Custom Metadata: "no"
  Encrypted: "no"
  File size: "58819 bytes"
  Form: "none"
  JavaScript: "no"
  Metadata Stream: "no"
  Optimized: "no"
  PDF version: "1.4"
  Page rot: "0"
  Page size: "596 x 842 pts (A4)"
  Pages: "1"
  Producer: "Skia/PDF m146 Google Docs Renderer"
  Suspects: "no"
  Tagged: "yes"
  Title: "MartinLepage_AttackClassificationReport"
  UserProperties: "no"
---

# MartinLepage_AttackClassificationReport

## Extracted Text

MartinLepage_AttackClassificationReport
Incident 1: Content Moderation AI
Attack type: Data Poisoning (pre-deployment through the learning loop).
Justification: The attackers did not “hack” the model directly. They hacked what the model
learns from by flooding it with coordinated reports, so the system’s continuous learning
pipeline started absorbing distorted feedback and building the wrong associations over time
Incident 2: Invoice Processing System
Attack type: Evasion Attack (post-deployment, at inference time).
Justification: The attackers tricked a live system with a document designed to mislead it. By
embedding hidden or layered text inside a PDF, they created an input that looks normal to a
human but pushes the extraction model into pulling the wrong invoice details.
Incident 3: Smart Healthcare Chatbot
Attack type: Inference Attack (post-deployment, privacy leakage).
Justification: The attackers treated the chatbot like a vault they could pick open by asking the
right questions. With carefully structured prompts, they tried to coax the model into revealing
sensitive traces of its training data, including phrases that could be linked back to real people.
Deliverable 2: Reflection
The stage that feels most exposed is Monitoring and ongoing improvement, especially when
continuous learning is enabled. That feedback stream is often assumed to be helpful and
authentic, but it is also an easy place to intervene because it sits between real user behavior
and future training data. If it is not protected like a security-critical asset, attackers can slowly
steer model behavior and make the drift look like normal change.
Deliverable 3: Two immediate actions
First, treat all feedback and retraining inputs as high-risk: add rate limits, bot and
coordination detection, data provenance checks, and human review for any update that could
materially shift model behavior. Second, harden the deployed system against crafted inputs
and extraction attempts by sanitizing documents (ex. stripping hidden layers in a PDF),
monitoring for abnormal query or output patterns, and adding privacy controls that reduce
memorization and block attempts to pull training data back out.

## Related

- [[Research and Papers MOC]]
- [[OPEN RISKS — Three Governance Blindspots Requiring Recursive Control]]
