// ECHO Reader — wrapper around window.speechSynthesis.
(function (global) {
  'use strict';

  const clamp = (v, min, max) => Math.min(max, Math.max(min, v));

  class EchoSpeechEngine {
    constructor() {
      this.synth = global.speechSynthesis;
      this.settings = { voiceURI: '', rate: 1, pitch: 1, volume: 1 };
      this._keepAliveTimer = null;
      this._voiceCache = null;
    }

    static isSupported() {
      return typeof global.speechSynthesis !== 'undefined' && typeof global.SpeechSynthesisUtterance !== 'undefined';
    }

    configure(patch) {
      Object.assign(this.settings, patch);
    }

    getVoices() {
      if (this._voiceCache && this._voiceCache.length) return Promise.resolve(this._voiceCache);
      return new Promise((resolve) => {
        const finish = (voices) => {
          this._voiceCache = voices;
          resolve(voices);
        };
        const now = this.synth.getVoices();
        if (now.length) return finish(now);
        // Voice list loads asynchronously on first access in Chrome.
        const timer = setTimeout(() => finish(this.synth.getVoices()), 1500);
        this.synth.addEventListener('voiceschanged', () => {
          clearTimeout(timer);
          finish(this.synth.getVoices());
        }, { once: true });
      });
    }

    async resolveVoice() {
      const voices = await this.getVoices();
      return (
        voices.find((v) => v.voiceURI === this.settings.voiceURI) ||
        voices.find((v) => v.default) ||
        voices[0] ||
        null
      );
    }

    // Speak one chunk of text. Resolves { ok } when the utterance ends,
    // { ok: false, error } when it errors or is cancelled.
    async speak(text) {
      if (!EchoSpeechEngine.isSupported()) return { ok: false, error: 'unsupported' };
      const utterance = new global.SpeechSynthesisUtterance(text);
      const voice = await this.resolveVoice();
      if (voice) {
        utterance.voice = voice;
        utterance.lang = voice.lang;
      }
      utterance.rate = clamp(Number(this.settings.rate) || 1, 0.5, 3);
      utterance.pitch = clamp(Number(this.settings.pitch) || 1, 0, 2);
      utterance.volume = clamp(Number(this.settings.volume) || 1, 0, 1);

      return new Promise((resolve) => {
        utterance.onend = () => {
          this._stopKeepAlive();
          resolve({ ok: true });
        };
        utterance.onerror = (event) => {
          this._stopKeepAlive();
          resolve({ ok: false, error: event.error || 'error' });
        };
        this.synth.speak(utterance);
        this._startKeepAlive();
      });
    }

    pause() {
      if (this.synth.speaking && !this.synth.paused) this.synth.pause();
    }

    resume() {
      if (this.synth.paused) this.synth.resume();
    }

    cancel() {
      this._stopKeepAlive();
      // Chrome ignores cancel() while paused on some platforms; resume first.
      if (this.synth.paused) this.synth.resume();
      this.synth.cancel();
    }

    get speaking() {
      return this.synth.speaking;
    }

    get paused() {
      return this.synth.paused;
    }

    // Chrome silently stops long utterances after ~15s of continuous audio.
    // ECHO speaks sentence-by-sentence so most utterances are short, but a
    // periodic pause/resume nudge keeps very long sentences alive.
    _startKeepAlive() {
      this._stopKeepAlive();
      this._keepAliveTimer = setInterval(() => {
        if (this.synth.speaking && !this.synth.paused) {
          this.synth.pause();
          this.synth.resume();
        }
      }, 12000);
    }

    _stopKeepAlive() {
      if (this._keepAliveTimer) {
        clearInterval(this._keepAliveTimer);
        this._keepAliveTimer = null;
      }
    }
  }

  global.EchoSpeechEngine = EchoSpeechEngine;
})(window);
