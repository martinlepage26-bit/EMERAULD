---
type: wiki
title: voice11 — ElevenLabs TTS Pipeline
aliases:
- voice11
- TTS
- ElevenLabs
- text-to-speech
- mlen
- Quebec voice
- canonical voice sample
- wiki/voice11 — ElevenLabs TTS Pipeline
tags:
- tooling
- voice
- tts
- media-production
- elevenlabs
- voice-spec
- quebec-english
- wiki
- voice11-elevenlabs-tts-pipeline-md
- mlen
- render
- english
- color-orange
status: active
created: '2026-04-18'
updated: '2026-06-26'
vault_area: wiki
canonical_path: wiki/voice11 — ElevenLabs TTS Pipeline.md
backlink_count: 5
backlinks:
- '[[wiki/AI Infrastructure Stack]]'
- '[[Areas/Writing/HENRY — Research Paper Writing System]]'
- '[[wiki/Martin Voice Spec — Version Genealogy]]'
- '[[wiki/Obsidian Second Brain Product]]'
- '[[Areas/Personal/Personal and Projects MOC]]'
---

# voice11 — ElevenLabs TTS Pipeline

## Summary

voice11 is a local Python TTS pipeline at `/home/cerebrhoe/voice11/` that wraps ElevenLabs voice synthesis and Coqui XTTS v2 for local rendering, drag-and-drop batch processing, and reference voice cloning. `mlen.mp3` in this directory is the **canonical English voice reference sample** for [[Martin Lepage Professional Identity|Martin]]: Quebec English, recorded in English (not French), and used as the ground-truth reference for all voice cloning and TTS modulation. It also serves as the Quebec English voice modulation guide — a listener can extract the accent's phonetic profile directly from the clip.

## Context

The canonical voice sample is the audio anchor for the [[Martin Voice Spec — Version Genealogy|voice spec corpus]]: where the text specs define register and claim-boundary discipline, `mlen.mp3` defines the phonetic identity. Relevant to [[Obsidian Agent Vault — Launch Kit|HeyGen avatar demo video]] production and content repurposing. Connects to [[AI Personas — Agatha, DOTTIE, and MOBI|Agatha/DOTTIE/MOBI persona system]] and the broader [[Martin Voice Spec — Stage Map|voice production pipeline]].

## Details

### Canonical voice sample

| Property | Value |
|---|---|
| File | `mlen.mp3` |
| Format | MP3, 128 kbps, 44.1 kHz, Mono |
| Size | ~607 KB |
| WSL path | `/home/cerebrhoe/voice11/mlen.mp3` |
| Windows UNC | `\\wsl.localhost\Ubuntu\home\cerebrhoe\voice11\mlen.mp3` |
| Script-relative (bat) | `%SCRIPT_DIR%mlen.mp3` |
| Language | **English** (Quebec English accent — not French) |
| Status | **Canonical** — operator-confirmed 2026-05-03 |

**Note:** `render_reference_voice_tts.py` has a hardcoded fallback default pointing to `C:\Users\softinfo\Desktop\MODELS\VOICE 11\mlen.mp3`. That path does not exist. The `.bat` launchers correctly override it with `%SCRIPT_DIR%mlen.mp3` (same directory). Use the bat launchers or pass `--reference-audio-en` explicitly when calling the Python script directly.

### Quebec English voice modulation guide

`mlen.mp3` encodes the target phonetic profile. Key characteristics for modulating to this voice:

**Phonetic profile (Quebec English):**
- **Dental consonants** — /t/, /d/, /n/, /l/ articulated at the upper teeth rather than the alveolar ridge (French substrate influence); gives the voice its distinctive forward placement
- **Syllable-timed rhythm** — stress distribution is flatter than standard North American English; syllables carry more equal weight (French influence)
- **Intonation contour** — flatter than American English; pitch range is narrower, rise-fall patterns are compressed
- **Back vowels** — slightly rounded; GOAT/BOAT vowels trend monophthongal
- **Reduced affrication** — /t/ and /d/ do not strongly affricate before high front vowels (distinguishes from hyper-Quebec phonology)
- **Register** — formal and precise; no nasal exaggeration; no stereotyped Joual features

**ElevenLabs optimal parameters (derived from PVC render `Moi_pvc_sp100_s50_sb75_se0_b_m2`):**

| Parameter | Value | Rationale |
|---|---|---|
| Clone mode | PVC (Professional Voice Clone) | More stable than IVC for production |
| Stability | 100% | Quebec English is consistent, not stylistically varied |
| Similarity | 50% | Allows model latitude while preserving voice identity |
| Style boost | 75% | Best match found; IVC at 64% was less accurate |
| Style exaggeration | 0% | Accent is subtle; exaggeration distorts it |
| Model | m2 (multilingual turbo) | Handles EN/FR code-switching in source text |

**Coqui XTTS v2 parameters (for `render_reference_voice_tts.py`):**

| Parameter | Value |
|---|---|
| Model | `tts_models/multilingual/multi-dataset/xtts_v2` |
| Reference clip | `mlen.mp3`, max 12 s, offset 0 s |
| Reference WAV | Auto-converted to 24 kHz mono |
| Language | `en` (not `fr`) |
| Chunk size | 280 characters |

### Installation path

`/home/cerebrhoe/voice11/`

### Key files

| File | Purpose |
|---|---|
| `mlen.mp3` | **Canonical EN voice reference** (Quebec English) |
| `voice11_cli.py` | CLI entry point for TTS rendering |
| `voice_hub.py` | Hub controller (multi-voice routing) |
| `render_british_tts.py` | British accent render script |
| `render_reference_voice_tts.py` | Reference voice clone render (Coqui XTTS v2) |
| `tts_common.py` | Shared utilities (markdown stripping, language detection) |
| `voice_hub.bat` | Windows drag-and-drop launcher |
| `render_british_tts_dragdrop.bat` | Drag-and-drop British TTS |
| `render_british_tts_very_deep_dragdrop.bat` | Deep voice variant |
| `render_reference_voice_dragdrop.bat` | Reference voice drag-and-drop (uses mlen.mp3) |

### Other audio in directory

- `ElevenLabs_2026-02-28T14_03_32_Wow_ivc_sp100_s50_sb64_se0_b_m2.mp3` — IVC test render (sb64; less accurate)
- `ElevenLabs_2026-02-28T14_56_48_Moi_pvc_sp100_s50_sb75_se0_b_m2.mp3` — PVC render (sb75; source of optimal parameter table above)

## Open Questions

- Is there a `mlfr.mp3` French reference sample, or is French synthesis handled by language-auto with the EN reference?
- Is HENRY integrated with voice11 for audio output of paper narrations?

## Sources

- `/home/cerebrhoe/voice11/` (directory scan + operator confirmation 2026-05-03)
- ElevenLabs render filenames (parameter extraction)

## Related

- [[Martin Voice Spec — Version Genealogy]] — Voice spec corpus; mlen.mp3 is the audio anchor
- [[Martin Voice Spec — Stage Map]] — Stage discipline that voice production follows
- [[Martin Lepage Professional Identity]] — Identity the voice encodes
- [[Obsidian Agent Vault — Launch Kit]]
- [[AI Personas — Agatha, DOTTIE, and MOBI]]
- [[HENRY — Research Paper Writing System]]
