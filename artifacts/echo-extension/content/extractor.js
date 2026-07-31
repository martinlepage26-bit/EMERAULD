// ECHO Reader — turns the live page (or the current selection) into an
// ordered list of speakable sentences that keep references into the DOM
// so the highlighter can follow along.
(function (global) {
  'use strict';

  const MIN_SPOKEN_LENGTH = 2;

  function normalize(text) {
    return text.replace(/\s+/g, ' ').trim();
  }

  function sentencesFromBlock(block) {
    const raw = block.textContent;
    if (!raw || !raw.trim()) return [];
    const out = [];
    for (const seg of global.EchoDom.splitSentences(raw)) {
      const spoken = normalize(seg.text);
      if (spoken.length < MIN_SPOKEN_LENGTH) continue;
      out.push({ text: spoken, block, start: seg.start, end: seg.end });
    }
    return out;
  }

  // Extract the main article of the page as sentences.
  function extractPage() {
    const root = global.EchoReadability.findMainElement(document) || document.body;
    let blocks = global.EchoDom.getReadableBlocks(root);
    // Sparse result (index pages, plain-text pages): widen to the whole body.
    if (blocks.length === 0 && root !== document.body) {
      blocks = global.EchoDom.getReadableBlocks(document.body);
    }
    const sentences = [];
    for (const block of blocks) {
      sentences.push(...sentencesFromBlock(block));
    }
    // Plain-text or fully unstructured pages: read body text without DOM anchors.
    if (sentences.length === 0 && document.body) {
      const bodyText = normalize(document.body.innerText || '');
      for (const seg of global.EchoDom.splitSentences(bodyText)) {
        const spoken = normalize(seg.text);
        if (spoken.length >= MIN_SPOKEN_LENGTH) {
          sentences.push({ text: spoken, block: null, start: null, end: null });
        }
      }
    }
    return { title: global.EchoReadability.findTitle(document), sentences };
  }

  // Extract the current selection as sentences (block anchor only — offsets
  // in the selection string don't map to a single element's textContent).
  function extractSelection() {
    const selection = global.getSelection();
    if (!selection || selection.isCollapsed) return null;
    const anchor = selection.anchorNode
      ? (selection.anchorNode.nodeType === Node.ELEMENT_NODE
        ? selection.anchorNode
        : selection.anchorNode.parentElement)
      : null;
    const sentences = [];
    for (const seg of global.EchoDom.splitSentences(selection.toString())) {
      const spoken = normalize(seg.text);
      if (spoken.length >= MIN_SPOKEN_LENGTH) {
        sentences.push({ text: spoken, block: anchor, start: null, end: null });
      }
    }
    return sentences.length ? { title: 'Selection', sentences } : null;
  }

  global.EchoExtractor = { extractPage, extractSelection };
})(window);
