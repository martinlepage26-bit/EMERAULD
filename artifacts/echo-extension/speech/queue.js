// ECHO Reader — ordered sentence queue with cursor navigation.
(function (global) {
  'use strict';

  class EchoSentenceQueue {
    constructor(sentences = []) {
      this.sentences = sentences;
      this.index = -1; // cursor sits before the first unread sentence
    }

    get length() {
      return this.sentences.length;
    }

    get current() {
      return this.index >= 0 && this.index < this.sentences.length ? this.sentences[this.index] : null;
    }

    hasNext() {
      return this.index + 1 < this.sentences.length;
    }

    next() {
      if (!this.hasNext()) return null;
      this.index += 1;
      return this.sentences[this.index];
    }

    // Move the cursor so the following next() lands on `index`.
    seek(index) {
      const target = Math.max(0, Math.min(this.sentences.length - 1, index));
      this.index = target - 1;
      return target;
    }

    reset() {
      this.index = -1;
    }
  }

  global.EchoSentenceQueue = EchoSentenceQueue;
})(window);
