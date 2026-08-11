# ECHO Reader — Chrome Extension

Offline-first Chrome extension that extracts the main article from any webpage and reads it aloud with sentence-by-sentence highlighting. No network calls, no external dependencies: extraction, speech, and preferences all run locally.

## Features

- **Article extraction** — Readability-style scoring (`reader/Readability.js`) finds the main content in the live DOM, skipping navigation, footers, sidebars, and ads.
- **Read aloud** — sentence-by-sentence playback through `speechSynthesis` (`speech/speech-engine.js` + `speech/queue.js`), with a keep-alive workaround for Chrome's long-utterance cutoff.
- **Pause / resume / skip** — full transport controls: play, pause, resume, stop, next sentence, previous sentence.
- **Sentence highlighting** — CSS Custom Highlight API highlights the exact sentence being spoken (no DOM mutation), with a block-level fallback; auto-scrolls to keep it in view.
- **Voice selection** — pick any installed system voice; rate, pitch, and volume sliders.
- **Floating overlay** — draggable in-page control panel (shadow DOM, style-isolated).
- **Popup controls** — start/stop from the toolbar and edit preferences.
- **Context menu** — "Read this page with ECHO" and "Read selection with ECHO".
- **Keyboard shortcuts** — `Alt+R` play/pause, `Alt+.` next, `Alt+,` previous, `Alt+X` stop, `Esc` stop (in-page). Global equivalents are declared in the manifest `commands` and configurable at `chrome://extensions/shortcuts`.
- **Persistent preferences** — voice, rate, pitch, volume, highlighting, and auto-scroll stored in `chrome.storage.sync` (falls back to local).

## Install (unpacked)

1. Open `chrome://extensions`.
2. Enable **Developer mode** (top right).
3. Click **Load unpacked** and select this folder.
4. Open any article, click the ECHO toolbar icon, and press **Read page** — or press `Alt+R`.

## Architecture

```
manifest.json                 MV3 manifest: content scripts, commands, context menus
background/service-worker.js  Context menus, global shortcuts, injection fallback
content/player.js             Controller: wires extractor → queue → engine → highlighter → overlay
content/extractor.js          Page/selection → ordered sentences with DOM anchors
content/highlighter.js        CSS Custom Highlight API + block fallback
content/overlay.js            Draggable shadow-DOM control panel
reader/Readability.js         Self-contained Readability-style main-content detection
speech/speech-engine.js       speechSynthesis wrapper (voices, keep-alive, transport)
speech/queue.js               Sentence queue with cursor navigation
storage/preferences.js        chrome.storage helpers shared by popup and content scripts
popup/                        Toolbar popup (controls + preferences)
utils/dom.js                  Block collection, sentence splitting, range building
utils/keyboard.js             In-page keyboard shortcuts
```

## Limitations

- Cannot run on browser-internal pages (`chrome://`, Web Store, PDF viewer); the popup says so instead of failing silently.
- Voice availability depends on the operating system's installed speech voices.
