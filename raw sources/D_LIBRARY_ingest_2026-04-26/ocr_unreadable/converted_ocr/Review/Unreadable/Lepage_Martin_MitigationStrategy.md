---
type: raw
source_kind: pdf_ocr
source_path: /mnt/d/LIBRARY/Review/Unreadable/2026 - Martin Lepage - ocr_needed_1.pdf - 2026 - Martin Lepage - ocr_needed_1.pdf.pdf - 2026 - Martin Lepage - ocr_needed_1.pdf - 2026 - Martin Lepage - ocr_needed_1.pdf.pdf.pdf
source_rel: Review/Unreadable/2026 - Martin Lepage - ocr_needed_1.pdf - 2026 - Martin Lepage - ocr_needed_1.pdf.pdf - 2026 - Martin Lepage - ocr_needed_1.pdf - 2026 - Martin Lepage - ocr_needed_1.pdf.pdf.pdf
ocr_engine: tesseract.js
ocr_lang: eng+fra
pages_total: 2
pages_ocrd: [1, 2]
partial: false
ocr_text: text/Review/Unreadable/2026 - Martin Lepage - ocr_needed_1.pdf - 2026 - Martin Lepage - ocr_needed_1.pdf.pdf - 2026 - Martin Lepage - ocr_neede__5fd676405def.ocr.txt
pdfinfo:
  Custom Metadata: "no"
  Encrypted: "no"
  File size: "84008 bytes"
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
  Title: "Lepage_Martin_MitigationStrategy"
  UserProperties: "no"
dr_sort_original_filename: "2026 - Martin Lepage - ocr_needed_1.pdf - 2026 - Martin Lepage - ocr_needed_1.pdf.pdf - 2026 - Martin Lepage - ocr_neede__5fd676405def.md"
dr_sort_original_path: "raw sources/D_LIBRARY_ingest_2026-04-26/ocr_unreadable/converted_ocr/Review/Unreadable/2026 - Martin Lepage - ocr_needed_1.pdf - 2026 - Martin Lepage - ocr_needed_1.pdf.pdf - 2026 - Martin Lepage - ocr_neede__5fd676405def.md"
dr_sort_filename_normalized: "2026-05-06"
---

# Lepage_Martin_MitigationStrategy

## OCR Notes

- This is an OCR extraction pass over `Review/Unreadable/` when `pdftotext` was empty/failed.
- Page strategy: full OCR for short PDFs; first + last pages for long PDFs.

## Extracted Text

===== IMAGE: /tmp/unreadable_ocr_wtvbq30w/p00001.png =====

FS vite de commandes x +
:\Users\MVaziri\Desktop\AI>ython test_cases.py
lython* n’est pas reconnu en tant que commande interne
ou externe, un programme exécutable ou un fichier de commandes
:\Users\MVaziri\Desktop\Al>python test_cases.py
raceback (most recent call last):
File , line 1, in
Python
:\Users\MVaziri\Desktop\Al>python test_cases.py
— Running Tests —
[Test 1] Running with a valid 128x128 image
[input is valid. simulating prediction
est 1 PASSED
[Test 2] Running with a None input.
est 2 PASSED
[Test 31 Running with a string input
est 3 PASSED
[Test 4] Running with a 6Ux64 image
est 4 PASSED
— ALL Tests Passed Successfully! —-
B inertie chesferpy x |
Flenier Modifier Affchage o >
# You must edit this file to add input sanitization
+ Make sure you have the Pillow library installed: pip install Pillow
from Pir import Image
def predict (image_object) :
This ic the VULNERABLE function
It takes a PIL image cbioct and protends to return a prediction.
It does not perform any checks on the input 'image object
Your task: Add sanitization checks at the beginning of this function. It should check fo
three things:
1) The input is mot None
2) The input is actually a PIL Image object.
3) The image dimensions are exactly 126x128 pixels.
If any check fails, it should return the string: "Error: Invalid input
TE all checks pass, it should procesd to the “prediction” step
+ ——— INPUT SANTTIZATION ——- #
Sf image object ix Heme:
return "Error: Invalid input."
if not isinstance (image object, Image. Image)
return "Error: Invalid input."
if image object.size i= (128, 128
return “Error: Invalid input."
# -—- END SANITIZATION — #
# If the input is valid, the function simulates a prediction.
print ("Input is valid. Simulating prediction...”)
Fecurn "prediction: car”

===== IMAGE: /tmp/unreadable_ocr_wtvbq30w/p00002.png =====

; - ox
& reflecüonnoteut x +

Fichier Modifier | Affichage Hv =- B 7e a :8
By validating the input first (not None, actually a PIL image, and
exactly 128x126), the function exits cleanly instead of crashing with
an exception. That makes it harder for someone to overload the service
with bad inputs and helps reduce denial-of-service risk.

## Related

- [[Research and Papers MOC]]
- [[Operator-Check Skill — Burnout Cascade Interrupt]]
