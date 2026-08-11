// ECHO Reader — floating in-page control overlay, isolated in a shadow root.
(function (global) {
  'use strict';

  const OVERLAY_CSS = `
    :host { all: initial; }
    .panel {
      position: fixed;
      right: 20px;
      bottom: 20px;
      z-index: 2147483647;
      width: 264px;
      background: #1f2430;
      color: #e8eaf0;
      border-radius: 12px;
      box-shadow: 0 8px 28px rgba(0, 0, 0, 0.4);
      font: 13px/1.4 system-ui, -apple-system, "Segoe UI", sans-serif;
      user-select: none;
    }
    .header {
      display: flex;
      align-items: center;
      justify-content: space-between;
      padding: 8px 12px;
      cursor: grab;
      border-bottom: 1px solid rgba(255, 255, 255, 0.08);
    }
    .header:active { cursor: grabbing; }
    .brand { font-weight: 700; letter-spacing: 0.12em; font-size: 12px; color: #ffd54f; }
    .close {
      background: none; border: none; color: #9aa2b5; cursor: pointer;
      font-size: 16px; line-height: 1; padding: 2px 4px;
    }
    .close:hover { color: #fff; }
    .body { padding: 10px 12px 12px; }
    .status { color: #9aa2b5; font-size: 12px; margin-bottom: 8px; min-height: 16px; }
    .controls { display: flex; gap: 6px; justify-content: center; margin-bottom: 10px; }
    .controls button {
      flex: 0 0 auto;
      width: 40px; height: 34px;
      background: #2c3342; color: #e8eaf0;
      border: none; border-radius: 8px;
      font-size: 15px; cursor: pointer;
    }
    .controls button:hover { background: #3a4356; }
    .controls button.primary { background: #ffd54f; color: #1a1a1a; width: 52px; }
    .controls button.primary:hover { background: #ffca28; }
    .row { display: flex; align-items: center; gap: 8px; margin-top: 8px; }
    .row label { flex: 0 0 34px; color: #9aa2b5; font-size: 11px; }
    .row input[type="range"] { flex: 1; accent-color: #ffd54f; }
    .row .value { flex: 0 0 30px; text-align: right; font-size: 11px; color: #9aa2b5; }
    .row select {
      flex: 1;
      background: #2c3342; color: #e8eaf0;
      border: 1px solid rgba(255, 255, 255, 0.1);
      border-radius: 6px; padding: 4px; font-size: 12px;
      max-width: 176px;
    }
  `;

  class EchoOverlay {
    constructor(callbacks = {}) {
      this.callbacks = callbacks;
      this.host = null;
      this.el = {};
    }

    get mounted() {
      return !!(this.host && this.host.isConnected);
    }

    mount() {
      if (this.mounted) return;
      this.host = document.createElement('div');
      this.host.id = 'echo-reader-overlay';
      const shadow = this.host.attachShadow({ mode: 'closed' });

      const style = document.createElement('style');
      style.textContent = OVERLAY_CSS;
      shadow.appendChild(style);

      const panel = document.createElement('div');
      panel.className = 'panel';
      panel.innerHTML = `
        <div class="header" part="header">
          <span class="brand">ECHO</span>
          <button class="close" title="Close" aria-label="Close">&times;</button>
        </div>
        <div class="body">
          <div class="status"></div>
          <div class="controls">
            <button class="prev" title="Previous sentence (Alt+,)">&#9198;</button>
            <button class="primary playpause" title="Play / pause (Alt+R)">&#9654;</button>
            <button class="next" title="Next sentence (Alt+.)">&#9197;</button>
            <button class="stop" title="Stop (Alt+X)">&#9632;</button>
          </div>
          <div class="row">
            <label>Speed</label>
            <input class="rate" type="range" min="0.5" max="2.5" step="0.1" value="1">
            <span class="value rate-value">1.0&times;</span>
          </div>
          <div class="row">
            <label>Voice</label>
            <select class="voice"></select>
          </div>
        </div>
      `;
      shadow.appendChild(panel);

      this.el = {
        panel,
        status: panel.querySelector('.status'),
        playpause: panel.querySelector('.playpause'),
        prev: panel.querySelector('.prev'),
        next: panel.querySelector('.next'),
        stop: panel.querySelector('.stop'),
        rate: panel.querySelector('.rate'),
        rateValue: panel.querySelector('.rate-value'),
        voice: panel.querySelector('.voice'),
        close: panel.querySelector('.close'),
        header: panel.querySelector('.header')
      };

      this.el.playpause.addEventListener('click', () => this.callbacks.onPlayPause?.());
      this.el.prev.addEventListener('click', () => this.callbacks.onPrev?.());
      this.el.next.addEventListener('click', () => this.callbacks.onNext?.());
      this.el.stop.addEventListener('click', () => this.callbacks.onStop?.());
      this.el.close.addEventListener('click', () => this.callbacks.onClose?.());
      this.el.rate.addEventListener('input', () => {
        const rate = parseFloat(this.el.rate.value);
        this.el.rateValue.textContent = `${rate.toFixed(1)}×`;
        this.callbacks.onRate?.(rate);
      });
      this.el.voice.addEventListener('change', () => this.callbacks.onVoice?.(this.el.voice.value));

      this._makeDraggable();
      (document.body || document.documentElement).appendChild(this.host);
    }

    destroy() {
      if (this.host) {
        this.host.remove();
        this.host = null;
        this.el = {};
      }
    }

    setState({ status, playing, index, total, rate }) {
      if (!this.mounted) return;
      if (typeof status === 'string') {
        this.el.status.textContent = status;
      } else if (typeof index === 'number' && typeof total === 'number' && total > 0) {
        this.el.status.textContent = `Sentence ${Math.max(1, index + 1)} of ${total}`;
      }
      if (typeof playing === 'boolean') {
        this.el.playpause.innerHTML = playing ? '&#10074;&#10074;' : '&#9654;';
        this.el.playpause.title = playing ? 'Pause (Alt+R)' : 'Play (Alt+R)';
      }
      if (typeof rate === 'number') {
        this.el.rate.value = String(rate);
        this.el.rateValue.textContent = `${rate.toFixed(1)}×`;
      }
    }

    setVoices(voices, selectedURI) {
      if (!this.mounted) return;
      this.el.voice.innerHTML = '';
      for (const voice of voices) {
        const option = document.createElement('option');
        option.value = voice.voiceURI;
        option.textContent = `${voice.name} (${voice.lang})`;
        if (voice.voiceURI === selectedURI) option.selected = true;
        this.el.voice.appendChild(option);
      }
    }

    _makeDraggable() {
      const { header, panel } = this.el;
      let dragging = false;
      let offsetX = 0;
      let offsetY = 0;
      header.addEventListener('pointerdown', (event) => {
        if (event.target.closest('.close')) return;
        dragging = true;
        const rect = panel.getBoundingClientRect();
        offsetX = event.clientX - rect.left;
        offsetY = event.clientY - rect.top;
        header.setPointerCapture(event.pointerId);
      });
      header.addEventListener('pointermove', (event) => {
        if (!dragging) return;
        panel.style.left = `${Math.max(0, event.clientX - offsetX)}px`;
        panel.style.top = `${Math.max(0, event.clientY - offsetY)}px`;
        panel.style.right = 'auto';
        panel.style.bottom = 'auto';
      });
      header.addEventListener('pointerup', () => { dragging = false; });
    }
  }

  global.EchoOverlay = EchoOverlay;
})(window);
