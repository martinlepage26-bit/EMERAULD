// ECHO Reader — MV3 service worker: context menus, global keyboard commands,
// and on-demand content-script injection for tabs loaded before install.
'use strict';

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

const COMMAND_MAP = {
  'toggle-read': 'toggle',
  'next-sentence': 'next',
  'prev-sentence': 'prev',
  'stop-read': 'stop'
};

chrome.runtime.onInstalled.addListener(() => {
  chrome.contextMenus.create({
    id: 'echo-read-page',
    title: 'Read this page with ECHO',
    contexts: ['page']
  });
  chrome.contextMenus.create({
    id: 'echo-read-selection',
    title: 'Read selection with ECHO',
    contexts: ['selection']
  });
});

async function sendCommand(tabId, cmd) {
  const message = { type: 'ECHO_CMD', cmd };
  try {
    return await chrome.tabs.sendMessage(tabId, message);
  } catch (_e) {
    // Content scripts aren't there (tab loaded before install): inject, retry.
    try {
      await chrome.scripting.executeScript({ target: { tabId }, files: CONTENT_SCRIPTS });
      return await chrome.tabs.sendMessage(tabId, message);
    } catch (_e2) {
      return null; // restricted page (chrome://, Web Store, PDF viewer)
    }
  }
}

chrome.contextMenus.onClicked.addListener((info, tab) => {
  if (!tab || tab.id == null) return;
  if (info.menuItemId === 'echo-read-page') sendCommand(tab.id, 'play-page');
  else if (info.menuItemId === 'echo-read-selection') sendCommand(tab.id, 'read-selection');
});

chrome.commands.onCommand.addListener(async (command) => {
  const cmd = COMMAND_MAP[command];
  if (!cmd) return;
  const [tab] = await chrome.tabs.query({ active: true, currentWindow: true });
  if (tab && tab.id != null) sendCommand(tab.id, cmd);
});
