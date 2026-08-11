// ECHO Reader — lightweight Readability-style article detection.
// Self-contained (no vendored third-party code) so the extension stays
// fully offline. Exposes the subset of the Readability API that ECHO uses:
//   new EchoReadability(document).parse() -> { title, content, textContent, length }
//   EchoReadability.findMainElement(document) -> Element (in the live DOM)
(function (global) {
  'use strict';

  const CANDIDATE_SELECTOR = 'article, main, [role="main"], section, div';
  const NEGATIVE_RE = /comment|meta|footer|footnote|sidebar|sponsor|ad-|advert|promo|related|share|social|nav|menu|breadcrumb|cookie|banner|popup|modal|subscribe|newsletter/i;
  const POSITIVE_RE = /article|body|content|entry|main|page|post|text|story|blog/i;

  function textLength(el) {
    return (el.textContent || '').trim().length;
  }

  function linkDensity(el) {
    const total = textLength(el);
    if (total === 0) return 0;
    let linked = 0;
    el.querySelectorAll('a').forEach((a) => { linked += (a.textContent || '').trim().length; });
    return linked / total;
  }

  function scoreElement(el) {
    let score = 0;
    const className = `${el.className} ${el.id}`;
    if (NEGATIVE_RE.test(className)) score -= 30;
    if (POSITIVE_RE.test(className)) score += 30;
    const tag = el.tagName.toLowerCase();
    if (tag === 'article') score += 40;
    else if (tag === 'main' || el.getAttribute('role') === 'main') score += 30;
    else if (tag === 'section') score += 5;

    // Paragraph mass: long paragraphs are the strongest article signal.
    let paragraphScore = 0;
    el.querySelectorAll('p').forEach((p) => {
      const len = (p.textContent || '').trim().length;
      if (len > 80) paragraphScore += Math.min(3, len / 100);
      const commas = ((p.textContent || '').match(/[,，]/g) || []).length;
      paragraphScore += Math.min(2, commas * 0.25);
    });
    score += paragraphScore;

    // Penalize link farms (navs, index pages).
    score *= 1 - Math.min(0.9, linkDensity(el));
    return score;
  }

  function findMainElement(doc) {
    const body = doc.body;
    if (!body) return null;
    let best = null;
    let bestScore = 0;
    const candidates = body.querySelectorAll(CANDIDATE_SELECTOR);
    for (const el of candidates) {
      if (textLength(el) < 140) continue;
      const score = scoreElement(el);
      if (score > bestScore) {
        bestScore = score;
        best = el;
      }
    }
    // Prefer the deepest equally-good candidate: if best's single child holds
    // essentially all its text, descend into it.
    while (best) {
      let denser = null;
      for (const child of best.children) {
        if (textLength(child) > textLength(best) * 0.9 && child.matches(CANDIDATE_SELECTOR)) {
          denser = child;
          break;
        }
      }
      if (!denser) break;
      best = denser;
    }
    return best || body;
  }

  function findTitle(doc) {
    const h1 = doc.querySelector('article h1, main h1, h1');
    const h1Text = h1 && h1.textContent ? h1.textContent.trim() : '';
    if (h1Text && h1Text.length >= 8) return h1Text;
    return (doc.title || '').trim();
  }

  class EchoReadability {
    constructor(doc) {
      this.doc = doc;
    }

    parse() {
      const main = findMainElement(this.doc);
      if (!main) return null;
      const textContent = (main.textContent || '').replace(/\s+/g, ' ').trim();
      return {
        title: findTitle(this.doc),
        content: main.innerHTML,
        textContent,
        length: textContent.length
      };
    }
  }

  EchoReadability.findMainElement = findMainElement;
  EchoReadability.findTitle = findTitle;

  global.EchoReadability = EchoReadability;
})(window);
