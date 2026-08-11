// ECHO Reader — the controller that ties extractor, queue, speech engine,
// highlighter and overlay together, and answers commands from the popup,
// service worker and in-page keyboard shortcuts.
(function (global) {
  'use strict';

  if (global.__echoPlayerLoaded) return; // guard against double injection
  global.__echoPlayerLoaded = true;

  const engine = new global.EchoSpeechEngine();
  let queue = null;
  let overlay = null;
  let prefs = { ...global.EchoPrefs.DEFAULTS };
  let playing = false;   // a read-through is in progress (may be paused)
  let session = 0;       // increments to invalidate a running loop

  const prefsReady = global.EchoPrefs.getPrefs().then((loaded) => {
    prefs = loaded;
    engine.configure(prefs);
  });
  global.EchoPrefs.onChange((next) => {
    prefs = next;
    engine.configure(next);
    if (overlay && overlay.mounted) overlay.setState({ rate: next.rate });
  });

  function ensureOverlay() {
    if (overlay && overlay.mounted) return;
    overlay = new global.EchoOverlay({
      onPlayPause: toggle,
      onPrev: () => jump(-1),
      onNext: () => jump(1),
      onStop: stop,
      onClose: () => { stop(); overlay.destroy(); },
      onRate: (rate) => { global.EchoPrefs.setPrefs({ rate }); },
      onVoice: (voiceURI) => { global.EchoPrefs.setPrefs({ voiceURI }); }
    });
    overlay.mount();
    overlay.setState({ rate: prefs.rate, playing: false, status: 'Ready' });
    engine.getVoices().then((voices) => {
      if (overlay && overlay.mounted) overlay.setVoices(voices, prefs.voiceURI);
    });
  }

  async function startPage() {
    await prefsReady;
    const { sentences } = global.EchoExtractor.extractPage();
    start(sentences);
  }

  async function startSelection() {
    await prefsReady;
    const result = global.EchoExtractor.extractSelection();
    if (result) start(result.sentences);
    else startPage();
  }

  function start(sentences) {
    ensureOverlay();
    if (!global.EchoSpeechEngine.isSupported()) {
      overlay.setState({ status: 'Speech synthesis is not available in this browser.' });
      return;
    }
    if (!sentences || sentences.length === 0) {
      overlay.setState({ status: 'Nothing readable found on this page.' });
      return;
    }
    session += 1;
    engine.cancel();
    queue = new global.EchoSentenceQueue(sentences);
    playing = true;
    loop();
  }

  async function loop() {
    const mySession = session;
    while (playing && queue && queue.hasNext() && mySession === session) {
      const sentence = queue.next();
      if (overlay && overlay.mounted) {
        overlay.setState({ playing: true, index: queue.index, total: queue.length });
      }
      if (prefs.highlight) {
        global.EchoHighlighter.highlight(sentence, { autoScroll: prefs.autoScroll });
      }
      const result = await engine.speak(sentence.text);
      if (mySession !== session) return; // superseded by a newer start/stop/jump
      if (!result.ok && result.error === 'not-allowed') {
        playing = false;
        if (overlay && overlay.mounted) {
          overlay.setState({ playing: false, status: 'Blocked: interact with the page first, then press play.' });
        }
        return;
      }
      // Other errors (interrupted, synthesis glitches): move on to the next sentence.
    }
    if (mySession === session && playing) {
      playing = false;
      global.EchoHighlighter.clear();
      if (overlay && overlay.mounted) {
        overlay.setState({ playing: false, status: 'Done' });
      }
    }
  }

  function toggle() {
    if (playing && engine.speaking && !engine.paused) {
      engine.pause();
      if (overlay && overlay.mounted) overlay.setState({ playing: false, status: 'Paused' });
    } else if (playing && engine.paused) {
      engine.resume();
      if (overlay && overlay.mounted) overlay.setState({ playing: true, index: queue ? queue.index : 0, total: queue ? queue.length : 0 });
    } else {
      startPage();
    }
  }

  function jump(delta) {
    if (!queue || queue.length === 0) return;
    const target = Math.max(0, Math.min(queue.length - 1, queue.index + delta));
    queue.seek(target);
    session += 1;
    engine.cancel();
    playing = true;
    loop();
  }

  function stop() {
    playing = false;
    session += 1;
    engine.cancel();
    global.EchoHighlighter.clear();
    queue = null;
    if (overlay && overlay.mounted) {
      overlay.setState({ playing: false, status: 'Stopped' });
    }
  }

  function getStatus() {
    return {
      supported: global.EchoSpeechEngine.isSupported(),
      active: !!queue,
      playing: playing && !engine.paused,
      paused: engine.paused,
      index: queue ? queue.index : -1,
      total: queue ? queue.length : 0
    };
  }

  const commands = {
    'toggle': toggle,
    'play-page': startPage,
    'read-selection': startSelection,
    'pause': () => { engine.pause(); if (overlay && overlay.mounted) overlay.setState({ playing: false, status: 'Paused' }); },
    'resume': () => { engine.resume(); if (overlay && overlay.mounted) overlay.setState({ playing: true }); },
    'stop': stop,
    'next': () => jump(1),
    'prev': () => jump(-1)
  };

  if (typeof chrome !== 'undefined' && chrome.runtime && chrome.runtime.onMessage) {
    chrome.runtime.onMessage.addListener((message, _sender, sendResponse) => {
      if (!message || message.type !== 'ECHO_CMD') return;
      const handler = commands[message.cmd];
      if (handler) handler();
      sendResponse(getStatus());
    });
  }

  // In-page API for utils/keyboard.js.
  global.EchoPlayer = { toggle, startPage, startSelection, stop, next: () => jump(1), prev: () => jump(-1), getStatus };
})(window);
