"""Jade voice layer — detection and graceful stubs for openWakeWord, whisper.cpp, Piper.

This module is intentionally a stub: it detects what's installed and provides working
shims when components are missing. The CLI loop in jade.py works without this module.
Wire in voice by calling listen_and_transcribe() instead of input().

Architecture:
  Microphone → Wake word (openWakeWord) → STT (whisper / faster-whisper)
             → jade.chat() → TTS (Piper) → Speaker

Install the full stack:
  pip install openwakeword faster-whisper sounddevice numpy
  # Piper: https://github.com/rhasspy/piper (binary release, no pip)
"""
from __future__ import annotations
import shutil
import sys
from pathlib import Path

# ── Capability detection ────────────────────────────────────────────────────────

def _has(pkg: str) -> bool:
    import importlib.util
    return importlib.util.find_spec(pkg) is not None

HAS_OPENWAKEWORD  = _has("openwakeword")
HAS_FASTER_WHISPER = _has("faster_whisper")
HAS_WHISPER        = _has("whisper")          # openai-whisper fallback
HAS_SOUNDDEVICE    = _has("sounddevice")
HAS_NUMPY          = _has("numpy")
HAS_PIPER          = bool(shutil.which("piper"))

STT_AVAILABLE  = (HAS_FASTER_WHISPER or HAS_WHISPER) and HAS_SOUNDDEVICE and HAS_NUMPY
WAKE_AVAILABLE = HAS_OPENWAKEWORD and HAS_SOUNDDEVICE
TTS_AVAILABLE  = HAS_PIPER


def capabilities() -> dict:
    return {
        "wake_word":    WAKE_AVAILABLE,
        "stt":          STT_AVAILABLE,
        "stt_backend":  "faster-whisper" if HAS_FASTER_WHISPER else ("openai-whisper" if HAS_WHISPER else None),
        "tts":          TTS_AVAILABLE,
        "full_voice":   WAKE_AVAILABLE and STT_AVAILABLE and TTS_AVAILABLE,
    }


# ── Wake word ──────────────────────────────────────────────────────────────────

WAKE_MODEL = "hey_jade"   # or "alexa", "hey_mycroft" — any openWakeWord model

def wait_for_wake_word(threshold: float = 0.5) -> bool:
    """Block until wake word is detected. Returns True. Raises RuntimeError if unavailable."""
    if not WAKE_AVAILABLE:
        raise RuntimeError(
            "Wake word unavailable. Install: pip install openwakeword sounddevice numpy"
        )
    import numpy as np
    import sounddevice as sd
    from openwakeword.model import Model

    oww = Model(wakeword_models=[WAKE_MODEL], inference_framework="onnx")
    CHUNK = 1280   # 80ms at 16kHz, required by openWakeWord
    print(f"[voice] Listening for wake word '{WAKE_MODEL}'…", flush=True)

    with sd.InputStream(samplerate=16000, channels=1, dtype="int16", blocksize=CHUNK) as stream:
        while True:
            audio, _ = stream.read(CHUNK)
            flat = audio.flatten().astype(np.float32) / 32768.0
            oww.predict(flat)
            score = oww.prediction_buffer.get(WAKE_MODEL, [0])[-1]
            if score >= threshold:
                print("[voice] Wake word detected.", flush=True)
                return True


# ── STT ────────────────────────────────────────────────────────────────────────

STT_DURATION = 6      # seconds to record after wake word
STT_MODEL    = "tiny" # faster-whisper model size: tiny / base / small

def transcribe(duration: int = STT_DURATION) -> str:
    """Record audio for `duration` seconds and return transcribed text."""
    if not STT_AVAILABLE:
        raise RuntimeError(
            "STT unavailable. Install: pip install faster-whisper sounddevice numpy"
        )
    import numpy as np
    import sounddevice as sd

    print(f"[voice] Recording {duration}s…", flush=True)
    audio = sd.rec(
        int(duration * 16000),
        samplerate=16000,
        channels=1,
        dtype="float32",
    )
    sd.wait()
    flat = audio.flatten()

    if HAS_FASTER_WHISPER:
        from faster_whisper import WhisperModel
        model = WhisperModel(STT_MODEL, device="cpu", compute_type="int8")
        segments, _ = model.transcribe(flat, language="en")
        text = " ".join(s.text for s in segments).strip()
    else:
        import whisper
        model = whisper.load_model(STT_MODEL)
        result = model.transcribe(flat, fp16=False)
        text = result["text"].strip()

    print(f"[voice] Heard: {text!r}", flush=True)
    return text


# ── TTS ────────────────────────────────────────────────────────────────────────

PIPER_MODEL = Path.home() / ".local" / "share" / "piper" / "en_US-lessac-medium.onnx"
PIPER_BIN   = shutil.which("piper") or "piper"

def speak(text: str) -> None:
    """Speak text via Piper TTS. Raises RuntimeError if Piper is not installed."""
    if not TTS_AVAILABLE:
        raise RuntimeError(
            "TTS unavailable. Install Piper: https://github.com/rhasspy/piper/releases"
        )
    import subprocess
    if not PIPER_MODEL.exists():
        raise RuntimeError(
            f"Piper model not found at {PIPER_MODEL}. "
            "Download: https://github.com/rhasspy/piper/releases"
        )
    proc = subprocess.run(
        [PIPER_BIN, "--model", str(PIPER_MODEL), "--output-raw"],
        input=text,
        capture_output=True,
        text=True,
    )
    # Pipe raw audio to aplay (ALSA) or afplay (macOS)
    player = shutil.which("aplay") or shutil.which("afplay")
    if not player:
        raise RuntimeError("No audio player found (need aplay or afplay)")
    subprocess.run(
        [player, "-r", "22050", "-f", "S16_LE", "-c", "1", "-"],
        input=proc.stdout,
        text=False,
    )


# ── Full voice loop helper ─────────────────────────────────────────────────────

def listen_and_transcribe() -> str:
    """Wake-word → record → transcribe. Returns transcript string.
    Falls back to input() if any component is missing."""
    cap = capabilities()
    if not cap["full_voice"]:
        missing = [k for k, v in cap.items() if k != "full_voice" and not v]
        print(f"[voice] Stub mode (missing: {missing}). Type your input:")
        return input("you: ").strip()
    wait_for_wake_word()
    return transcribe()


# ── CLI: capability report ─────────────────────────────────────────────────────

if __name__ == "__main__":
    cap = capabilities()
    print("Jade voice capability report:")
    for k, v in cap.items():
        status = "✅" if v else "❌"
        print(f"  {status}  {k}: {v}")
    if not cap["full_voice"]:
        print("\nTo enable full voice:")
        if not cap["wake_word"]:
            print("  pip install openwakeword sounddevice numpy")
        if not cap["stt"]:
            print("  pip install faster-whisper sounddevice numpy")
        if not cap["tts"]:
            print("  # Download Piper from https://github.com/rhasspy/piper/releases")
            print("  # Place binary in PATH, model at ~/.local/share/piper/en_US-lessac-medium.onnx")
