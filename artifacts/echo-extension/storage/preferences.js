// ECHO Reader — Chrome storage helpers. Loaded in content scripts and popup.
(function (global) {
  'use strict';

  const KEY = 'echoPrefs';
  const DEFAULTS = Object.freeze({
    voiceURI: '',
    rate: 1,
    pitch: 1,
    volume: 1,
    highlight: true,
    autoScroll: true
  });

  function storageArea() {
    if (typeof chrome === 'undefined' || !chrome.storage) return null;
    return chrome.storage.sync || chrome.storage.local;
  }

  async function getPrefs() {
    const area = storageArea();
    if (!area) return { ...DEFAULTS };
    try {
      const result = await area.get(KEY);
      return { ...DEFAULTS, ...(result[KEY] || {}) };
    } catch (_e) {
      return { ...DEFAULTS };
    }
  }

  async function setPrefs(patch) {
    const area = storageArea();
    const merged = { ...(await getPrefs()), ...patch };
    if (area) {
      try {
        await area.set({ [KEY]: merged });
      } catch (_e) {
        // Storage quota or transient failure: callers still get the merged value.
      }
    }
    return merged;
  }

  function onChange(callback) {
    if (typeof chrome === 'undefined' || !chrome.storage) return;
    chrome.storage.onChanged.addListener((changes) => {
      if (changes[KEY]) {
        callback({ ...DEFAULTS, ...(changes[KEY].newValue || {}) });
      }
    });
  }

  global.EchoPrefs = { DEFAULTS, getPrefs, setPrefs, onChange };
})(typeof window !== 'undefined' ? window : self);
