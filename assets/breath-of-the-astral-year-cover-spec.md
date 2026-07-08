---
type: asset
title: Book Cover Spec — Breath of the Astral Year
aliases:
- assets/breath-of-the-astral-year-cover-spec
tags:
- asset
- assets
- breath-of-the-astral-year-cover-spec-md
- georgia
- cover
- serif
- opacity
- regular
- color-green
status: active
created: '2026-06-21'
updated: '2026-06-26'
vault_area: assets
canonical_path: assets/breath-of-the-astral-year-cover-spec.md
backlink_count: 1
backlinks:
- '[[wiki/Orphan Index — Vault-Level Graph Repair 2026-05-06]]'
---

# Book Cover Spec — Breath of the Astral Year
**Publisher:** HEX/ADECIMAL Press  
**Author:** Martin Lepage, PhD  
**Generated:** 2026-05-27  
**Reference visual:** `site/public/social/og-breath-of-the-astral-year.svg`  
**KDP baseline:** *Alchemy of the Wound* (ISBN 9798251826722)

---

## 1. File Specifications (Amazon KDP)

| Parameter | Value |
|---|---|
| Trim size | 6 × 9 inches (standard trade paperback) |
| Full cover canvas (front + spine + back) | Calculated after page count (see below) |
| Resolution | 300 DPI minimum |
| Color mode | RGB (KDP accepts RGB; converts to CMYK for print) |
| File format | PDF (preferred) or JPG/PNG for digital cover only |
| Bleed | 0.125 inch on all outer edges |
| Safe zone | 0.25 inch inward from all trim edges |
| Spine width formula | (page count × 0.002252) + 0.06 inches |
| Estimated page count | ~220–240 pages at 51,948 words, 6×9, 12pt body |
| Estimated spine width | ~0.57–0.60 inches |
| Full cover width | 6 + spine + 6 + 0.25 bleed = ~12.82–12.85 inches |
| Full cover height | 9 + 0.25 bleed = 9.25 inches |

**Canvas for digital front cover only (no spine/back):**  
- 1800 × 2700 px at 300 DPI (6 × 9 inches)

---

## 2. Color Palette

| Role | Hex | Description |
|---|---|---|
| Background — deep | `#09121f` | Near-black midnight blue |
| Background — mid | `#112539` | Deep ocean blue |
| Background — warm edge | `#20313e` | Slate teal |
| Accent — cold light | `#6ee2d0` | Pale teal / aqua |
| Accent — warm glow | `#f0b95f` | Amber / gold |
| Text primary | `#eef4f8` | Near-white, slightly blue-cool |
| Text secondary | `#d8e5ec` | Muted slate white |
| Inner glow | `#6ee2d0` at 34% opacity | Subtle ring highlight |

**Gradient rule:** Background runs diagonally from deep midnight (`#09121f`) top-left → slate teal (`#20313e`) bottom-right. Two radial mist overlays: teal mist upper-left, amber mist upper-right.

---

## 3. Typography

| Element | Font | Size (print) | Weight | Tracking |
|---|---|---|---|---|
| Super-title / genre label | Georgia, serif | 10–11pt | Regular | +6pt letter-spacing, caps |
| Main title line 1 | Georgia, serif | 36–40pt | Bold 700 | Default |
| Main title line 2 | Georgia, serif | 36–40pt | Bold 700 | Default |
| Subtitle / tagline | Georgia, serif | 14–16pt | Regular | Default |
| Author name | Georgia, serif | 14pt | Regular | +2pt letter-spacing |
| Publisher imprint | Georgia, serif | 9pt | Regular | Caps, light opacity |
| Spine title | Georgia, serif | 10–11pt | Bold | Rotated 90°, bottom to top |
| Spine author | Georgia, serif | 9pt | Regular | Rotated 90° |
| Back cover body | Georgia, serif | 10pt | Regular | Default |
| Back cover tagline | Georgia, serif | 13pt | Italic | Default |

---

## 4. Front Cover Layout

```
┌─────────────────────────────────────┐  ← 0.125" bleed edge
│                                     │
│  [TEAL RADIAL MIST — upper left]    │
│         [AMBER MIST — upper right]  │
│                                     │
│  ░░░░░░░░░░░░░░░  ●●●●●●●          │
│  ░ TEXT ZONE ░░░  ● ZODIAC ●        │
│  ░░░░░░░░░░░░░░░  ●  WHEEL ●        │
│                   ● (right ●        │
│                   ●  half) ●        │
│                   ●●●●●●●          │
│                                     │
└─────────────────────────────────────┘
```

### Text Zone (left 55% of cover)

**Line 1 — Genre label** (top, ~20% from top)
```
GAIALOGY · A BOOK OF SIGNS AND EARTHLY WEATHER
```
- 10pt Georgia caps, letter-spacing +6
- Opacity 78%
- Color: `#eef4f8`

**Lines 2–3 — Main title** (~28–42% from top)
```
Breath of the
Astral Year
```
- 38pt Georgia Bold
- Color: `#eef4f8`
- Two lines, tight leading (1.1×)

**Lines 4–5 — Tagline** (~48–55% from top)
```
A book that looks for meaning on Earth,
in weather, bodies, seasons, and the Sun.
```
- 14pt Georgia Regular
- Opacity 90%
- Color: `#eef4f8`

**Line 6 — Descriptive pull** (~62–67% from top)
```
Grounded symbolic life, kept close to Earth.
Signs as feeling, season, and Earth energy.
```
- 11pt Georgia
- Color: `#d8e5ec`
- Opacity 80%

**Author line** (bottom 15%)
```
Martin Lepage, PhD
```
- 13pt Georgia Regular
- Letter-spacing +2
- Color: `#eef4f8`

**Imprint line** (very bottom, inside safe zone)
```
HEX/ADECIMAL PRESS
```
- 8pt caps, opacity 55%

### Zodiacal Wheel (right 45% of cover, vertically centered)

Centered at approximately x=75%, y=50% of the cover.

**Rings (outermost to innermost):**
1. Outer ring: `stroke: url(#ring-gradient)` — amber-to-teal, 2.5px, opacity 0.9, r=206px equivalent scaled
2. Middle ring: `#eef4f8`, 1.5px, opacity 0.22, r=154px equivalent
3. Inner ring: `#6ee2d0`, 1.5px, opacity 0.34, r=96px equivalent
4. Center body: `#eef4f8` filled circle, opacity 0.9, r=28px equivalent
5. Center core: `#102538` filled, r=10px equivalent

**Cardinal spokes** (8 directions from center):
- Stroke: `#eef4f8`, opacity 0.44, 3px, rounded caps
- Extend 10% beyond outer ring

**12 zodiac glyphs** placed just outside middle ring at their degree positions:
- ♈ ♉ ♊ ♋ ♌ ♍ ♎ ♏ ♐ ♑ ♒ ♓
- Font: Georgia 30pt, fill `#eef4f8`, opacity 0.92

---

## 5. Spine Layout

**Orientation:** Text reads bottom-to-top when book lies flat face-up.

```
[bottom] HEX/ADECIMAL   Breath of the Astral Year   Martin Lepage [top]
```

- Background: same deep gradient as cover
- Title: Georgia Bold 10pt, `#eef4f8`
- Author: Georgia Regular 9pt, `#eef4f8`, opacity 80%
- Publisher: Georgia Regular 8pt caps, `#6ee2d0`, opacity 65%
- Thin amber rule (`#f0b95f`, 0.5px) separating title from publisher

---

## 6. Back Cover Layout

**Background:** Same midnight gradient (mirrored horizontally)  
**Zodiacal element:** Small partial wheel, low opacity, bottom-right corner — ghost of the front cover wheel

### Back Cover Content (top to bottom, left-aligned, inside safe zone)

**Pull quote — large** (top third)
```
"The zodiacal year is not a personality system.
It is a shared technology for naming collective time."
```
- 15pt Georgia Italic, `#eef4f8`, opacity 90%

**Body description** (middle third)
```
Breath of the Astral Year reads the twelve signs not as
personality types but as competences — capacities a community
needs distributed across seasons and bodies.

Each chapter moves through one zodiacal period and asks: what
is this season asking of us? What can only be done in this
light, at this temperature, under this pressure?

The book keeps its answers close to Earth: in weather, bodies,
ritual calendars, and the civic rhythms that shape a life
without ever being named. Signs as feeling. The year as practice.
```
- 10pt Georgia Regular, `#d8e5ec`, line-height 1.6

**Tagline / closing line**
```
A grammar of collective life.
```
- 13pt Georgia Italic, `#eef4f8`, centered

**Author bio block** (bottom third)
```
Martin Lepage, PhD is a scholar, governance researcher,
and writer. He is the founder of PHAROS / InfraFabric
and the author of several works under HEX/ADECIMAL Press.
```
- 9pt Georgia Regular, `#d8e5ec`

**ISBN barcode zone** (bottom-right corner)
- Standard KDP white-box barcode placement
- Minimum 1.5 × 1.0 inches, white background
- ISBN-13 below barcode in 8pt sans-serif

**Publisher imprint** (bottom-left)
```
HEX/ADECIMAL PRESS
hexadecimalmystic.substack.com
```
- 8pt caps, `#6ee2d0`, opacity 60%

---

## 7. Generation Instructions (for AI image tools or manual design)

### Prompt for AI cover generation (Midjourney / DALL-E / Ideogram)

```
Book cover for "Breath of the Astral Year" by Martin Lepage PhD. 
Publisher: HEX/ADECIMAL Press.
Style: scholarly literary non-fiction, not mystical or new-age.
Background: deep midnight blue to dark teal gradient, near-black.
Central graphic element: elegant zodiacal wheel with 12 glyphs (♈♉♊♋♌♍♎♏♐♑♒♓), 
concentric rings, thin amber-to-teal gradient outer ring, white inner rings at low opacity. 
Placed right-of-center, vertically centered.
Left side: Georgia serif typography, near-white text on dark field.
Accent colors: pale teal #6ee2d0 and warm amber #f0b95f — used sparingly for rings and glows.
Atmosphere: two soft radial mist glows — teal upper-left, amber upper-right, very low opacity.
Mood: grounded, serious, contemplative. Earth-bound, not cosmic escapism.
No planets. No mystical symbols beyond the zodiacal wheel. No excessive glow effects.
6x9 inch book cover format, portrait orientation.
```

### SVG / Figma / InDesign approach

1. Start from `site/public/social/og-breath-of-the-astral-year.svg` as the visual reference
2. Resize canvas to 1800×2700px (300dpi, 6×9 inches)
3. Rebuild the zodiacal wheel at larger scale (outer ring ~520px radius at this canvas size)
4. Apply the text hierarchy above
5. Export: PDF with bleed marks for KDP print; PNG for digital/Kindle cover

---

## 8. Kindle / Digital Cover Notes

- Digital cover: front cover only, no spine/back
- Canvas: 1600×2560px minimum (KDP recommendation); 1800×2700px preferred
- Same visual treatment as print front cover
- Ensure title is legible at thumbnail size (160×256px): test at 10% zoom
- No bleed required for digital

---

## 9. Cross-Reference

- Existing OG image: `site/public/social/og-breath-of-the-astral-year.svg` (1200×630 social card)
- Cover art should feel like a scaled, vertical version of that social card
- Sibling covers to reference for series consistency: *Alchemy of the Wound* (ISBN 9798251826722), *CORPUS ou le génie de l'insistance* (ISBN 9798275803334)
