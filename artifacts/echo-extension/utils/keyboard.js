// ECHO Reader — in-page keyboard shortcuts. Global browser-level shortcuts
// (Alt+R, Alt+., Alt+,, Alt+X) are declared in manifest "commands" and routed
// through the service worker; these listeners cover the same keys when focus
// is inside the page, plus Escape to stop.
(function (global) {
  'use strict';

  function isTypingTarget(el) {
    if (!el) return false;
    const tag = el.tagName ? el.tagName.toLowerCase() : '';
    return tag === 'input' || tag === 'textarea' || tag === 'select' || el.isContentEditable;
  }

  global.addEventListener('keydown', (event) => {
    const player = global.EchoPlayer;
    if (!player) return;
    if (isTypingTarget(event.target)) return;

    if (event.altKey && !event.ctrlKey && !event.metaKey) {
      if (event.code === 'KeyR') {
        event.preventDefault();
        player.toggle();
      } else if (event.code === 'Period') {
        event.preventDefault();
        player.next();
      } else if (event.code === 'Comma') {
        event.preventDefault();
        player.prev();
      } else if (event.code === 'KeyX') {
        event.preventDefault();
        player.stop();
      }
    } else if (event.key === 'Escape' && player.getStatus().active) {
      player.stop();
    }
  }, true);
})(window);
