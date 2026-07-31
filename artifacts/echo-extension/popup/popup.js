// ECHO Reader — popup controls. Talks to the content-script player in the
// active tab and persists preferences via storage/preferences.js semantics.
'use strict';

const PREFS_KEY = 'echoPrefs';
const DEFAULTS = { voiceURI: '', rate: 1, pitch: 1, volume: 1, highlight: true, autoScroll: true };

const CONTENT_SCRIPTS = [
  'utils/dom.js',
  'reader/Readability.js',
  'storage/preferences.js',
  'speech/speech-engine.js',
  'speech/queue.js',
  'content/extractor.js',
  'content/highlighter.js',
  'content/overlay.js',
  'content/player.js',
  'utils/keyboard.js'
];

const el = {
  status: document.getElementById('status'),
  play: document.getElementById('play'),
  pause: document.getElementById('pause'),
  stop: document.getElementById('stop'),
  voice: document.getElementById('voice'),
  rate: document.getElementById('rate'),
  rateValue: document.getElementById('rate-value'),
  pitch: document.getElementById('pitch'),
  pitchValue: document.getElementById('pitch-value'),
  volume: document.getElementById('volume'),
  volumeValue: document.getElementById('volume-value'),
  highlight: document.getElementById('highlight'),
  autoscroll: document.getElementById('autoscroll')
};

const storage = chrome.storage.sync || chrome.storage.local;

async function getPrefs() {
  try {
    const result = await storage.get(PREFS_KEY);
    return { ...DEFAULTS, ...(result[PREFS_KEY] || {}) };
  } catch (_e) {
    return { ...DEFAULTS };
  }
}

async function setPrefs(patch) {
  const merged = { ...(await getPrefs()), ...patch };
  try {
    await storage.set({ [PREFS_KEY]: merged });
  } catch (_e) { /* transient storage failure: UI still reflects the change */ }
  return merged;
}

async function activeTab() {
  const [tab] = await chrome.tabs.query({ active: true, currentWindow: true });
  return tab || null;
}

async function sendCommand(cmd) {
  const tab = await activeTab();
  if (!tab || tab.id == null) return null;
  const message = { type: 'ECHO_CMD', cmd };
  try {
    return await chrome.tabs.sendMessage(tab.id, message);
  } catch (_e) {
    try {
      await chrome.scripting.executeScript({ target: { tabId: tab.id }, files: CONTENT_SCRIPTS });
      return await chrome.tabs.sendMessage(tab.id, message);
    } catch (_e2) {
      return null;
    }
  }
}

function renderStatus(status) {
  if (!status) {
    el.status.textContent = 'ECHO can’t read this page (browser page or restricted site).';
    el.play.disabled = true;
    el.pause.disabled = true;
    el.stop.disabled = true;
    return;
  }
  el.play.disabled = false;
  el.pause.disabled = !status.active;
  el.stop.disabled = !status.active;
  if (!status.supported) {
    el.status.textContent = 'Speech synthesis is not available in this browser.';
    el.play.disabled = true;
  } else if (status.active && status.paused) {
    el.status.textContent = `Paused at sentence ${status.index + 1} of ${status.total}`;
  } else if (status.active && status.playing) {
    el.status.textContent = `Reading sentence ${status.index + 1} of ${status.total}`;
  } else {
    el.status.textContent = 'Ready to read this page.';
  }
}

function populateVoices(selectedURI) {
  const fill = (voices) => {
    el.voice.innerHTML = '';
    const auto = document.createElement('option');
    auto.value = '';
    auto.textContent = 'System default';
    el.voice.appendChild(auto);
    for (const voice of voices) {
      const option = document.createElement('option');
      option.value = voice.voiceURI;
      option.textContent = `${voice.name} (${voice.lang})`;
      if (voice.voiceURI === selectedURI) option.selected = true;
      el.voice.appendChild(option);
    }
  };
  const now = speechSynthesis.getVoices();
  if (now.length) fill(now);
  else speechSynthesis.addEventListener('voiceschanged', () => fill(speechSynthesis.getVoices()), { once: true });
}

function bindSlider(input, valueEl, key, format) {
  input.addEventListener('input', () => {
    valueEl.textContent = format(parseFloat(input.value));
    setPrefs({ [key]: parseFloat(input.value) });
  });
}

async function init() {
  const prefs = await getPrefs();

  el.rate.value = String(prefs.rate);
  el.rateValue.textContent = `${prefs.rate.toFixed(1)}×`;
  el.pitch.value = String(prefs.pitch);
  el.pitchValue.textContent = prefs.pitch.toFixed(1);
  el.volume.value = String(prefs.volume);
  el.volumeValue.textContent = `${Math.round(prefs.volume * 100)}%`;
  el.highlight.checked = prefs.highlight;
  el.autoscroll.checked = prefs.autoScroll;

  populateVoices(prefs.voiceURI);

  bindSlider(el.rate, el.rateValue, 'rate', (v) => `${v.toFixed(1)}×`);
  bindSlider(el.pitch, el.pitchValue, 'pitch', (v) => v.toFixed(1));
  bindSlider(el.volume, el.volumeValue, 'volume', (v) => `${Math.round(v * 100)}%`);
  el.voice.addEventListener('change', () => setPrefs({ voiceURI: el.voice.value }));
  el.highlight.addEventListener('change', () => setPrefs({ highlight: el.highlight.checked }));
  el.autoscroll.addEventListener('change', () => setPrefs({ autoScroll: el.autoscroll.checked }));

  el.play.addEventListener('click', async () => {
    renderStatus(await sendCommand('play-page'));
    window.close(); // get the popup out of the way; the in-page overlay takes over
  });
  el.pause.addEventListener('click', async () => renderStatus(await sendCommand('toggle')));
  el.stop.addEventListener('click', async () => renderStatus(await sendCommand('stop')));

  renderStatus(await sendCommand('status'));
}

init();
