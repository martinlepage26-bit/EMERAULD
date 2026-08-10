// ECHO Reader — sentence highlighting. Prefers the CSS Custom Highlight API
// (no DOM mutation); falls back to a background class on the sentence's block.
(function (global) {
  'use strict';

  const HIGHLIGHT_NAME = 'echo-sentence';
  const BLOCK_CLASS = 'echo-active-block';
  const STYLE_ID = 'echo-reader-style';

  let lastBlock = null;

  function supportsHighlightAPI() {
    return typeof global.CSS !== 'undefined' && 'highlights' in global.CSS && typeof global.Highlight === 'function';
  }

  function ensureStyle() {
    if (document.getElementById(STYLE_ID)) return;
    const style = document.createElement('style');
    style.id = STYLE_ID;
    style.textContent = [
      `::highlight(${HIGHLIGHT_NAME}) { background-color: rgba(255, 213, 79, 0.85); color: #1a1a1a; }`,
      `.${BLOCK_CLASS} { background-color: rgba(255, 213, 79, 0.25); transition: background-color 0.2s ease; }`
    ].join('\n');
    (document.head || document.documentElement).appendChild(style);
  }

  function clearBlock() {
    if (lastBlock) {
      lastBlock.classList.remove(BLOCK_CLASS);
      lastBlock = null;
    }
  }

  function highlight(sentence, options = {}) {
    ensureStyle();
    clearBlock();
    if (supportsHighlightAPI()) global.CSS.highlights.delete(HIGHLIGHT_NAME);

    const block = sentence.block;
    if (!block || !block.isConnected) return;

    if (options.autoScroll !== false) {
      block.scrollIntoView({ block: 'center', behavior: 'smooth' });
    }

    if (supportsHighlightAPI() && sentence.start != null && sentence.end != null) {
      const range = global.EchoDom.rangeFromOffsets(block, sentence.start, sentence.end);
      if (range) {
        global.CSS.highlights.set(HIGHLIGHT_NAME, new global.Highlight(range));
        return;
      }
    }
    // Fallback: mark the whole block.
    lastBlock = block;
    block.classList.add(BLOCK_CLASS);
  }

  function clear() {
    if (supportsHighlightAPI()) global.CSS.highlights.delete(HIGHLIGHT_NAME);
    clearBlock();
  }

  global.EchoHighlighter = { highlight, clear };
})(window);
