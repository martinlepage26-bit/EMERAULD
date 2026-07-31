// ECHO Reader — DOM utilities shared by extractor, highlighter and reader.
(function (global) {
  'use strict';

  const BLOCK_SELECTOR = 'p, h1, h2, h3, h4, h5, h6, li, blockquote, pre, td, th, dd, dt, figcaption, caption';
  const SKIP_SELECTOR = 'script, style, noscript, template, nav, footer, header, aside, form, button, select, option, iframe, svg, [aria-hidden="true"], [hidden]';

  function isVisible(el) {
    if (!el || !el.isConnected) return false;
    const style = global.getComputedStyle(el);
    if (style.display === 'none' || style.visibility === 'hidden' || parseFloat(style.opacity) === 0) return false;
    const rect = el.getBoundingClientRect();
    return rect.width > 0 && rect.height > 0;
  }

  // Collect readable block-level elements under root, in document order,
  // skipping chrome (nav/footer/aside) and invisible nodes.
  function getReadableBlocks(root) {
    const blocks = [];
    const seen = new Set();
    const candidates = root.matches && root.matches(BLOCK_SELECTOR) ? [root] : [];
    root.querySelectorAll(BLOCK_SELECTOR).forEach((el) => candidates.push(el));
    for (const el of candidates) {
      if (seen.has(el)) continue;
      if (el.closest(SKIP_SELECTOR)) continue;
      // Skip containers whose text lives entirely in nested blocks (e.g. <li><p>…</p></li>).
      if (el.querySelector(BLOCK_SELECTOR) && directText(el).trim().length === 0) continue;
      if (!isVisible(el)) continue;
      if (!el.textContent || el.textContent.trim().length === 0) continue;
      seen.add(el);
      blocks.push(el);
    }
    return blocks;
  }

  function directText(el) {
    let out = '';
    for (const node of el.childNodes) {
      if (node.nodeType === Node.TEXT_NODE) out += node.nodeValue;
      else if (node.nodeType === Node.ELEMENT_NODE && !node.matches(BLOCK_SELECTOR)) out += node.textContent;
    }
    return out;
  }

  // Split text into sentences, preserving character offsets into the input
  // so highlight ranges can be rebuilt. Uses Intl.Segmenter when available.
  function splitSentences(text) {
    if (!text) return [];
    if (typeof Intl !== 'undefined' && Intl.Segmenter) {
      const segmenter = new Intl.Segmenter(undefined, { granularity: 'sentence' });
      const out = [];
      for (const seg of segmenter.segment(text)) {
        out.push({ text: seg.segment, start: seg.index, end: seg.index + seg.segment.length });
      }
      return out;
    }
    const out = [];
    const re = /[^.!?…]+[.!?…]+["»”’')\]]*\s*|[^.!?…]+\s*$/g;
    let match;
    while ((match = re.exec(text)) !== null) {
      out.push({ text: match[0], start: match.index, end: match.index + match[0].length });
    }
    return out;
  }

  // Build a Range covering [start, end) character offsets of el.textContent.
  function rangeFromOffsets(el, start, end) {
    const range = global.document.createRange();
    const walker = global.document.createTreeWalker(el, NodeFilter.SHOW_TEXT);
    let pos = 0;
    let node;
    let startSet = false;
    while ((node = walker.nextNode())) {
      const len = node.nodeValue.length;
      if (!startSet && start < pos + len) {
        range.setStart(node, Math.max(0, start - pos));
        startSet = true;
      }
      if (startSet && end <= pos + len) {
        range.setEnd(node, Math.max(0, end - pos));
        return range;
      }
      pos += len;
    }
    if (startSet) {
      range.setEndAfter(el.lastChild || el);
      return range;
    }
    return null;
  }

  function clamp(value, min, max) {
    return Math.min(max, Math.max(min, value));
  }

  global.EchoDom = { BLOCK_SELECTOR, SKIP_SELECTOR, isVisible, getReadableBlocks, splitSentences, rangeFromOffsets, clamp };
})(window);
