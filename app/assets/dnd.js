// Drag-and-drop boards: word order, matching and word-bank gaps.
// Pointer events cover mouse, touch and pen. Tapping a card (or pressing Enter on it) also moves it,
// so nothing depends on dragging. No third-party code.
(function () {
  'use strict';
  var h = UI.h;

  function targetAt(x, y) {
    var el = document.elementFromPoint(x, y); // the floating copy has pointer-events: none
    return el && el.closest ? el.closest('[data-drop]') : null;
  }

  /** Make a card draggable. hooks: locked(), tap(card), drop(card, target, x, y), over(target or null) */
  function drag(card, hooks) {
    card.addEventListener('pointerdown', function (e) {
      if (hooks.locked() || (e.pointerType === 'mouse' && e.button !== 0)) return;
      var sx = e.clientX, sy = e.clientY, moved = false, ghost = null, pid = e.pointerId;
      try { card.setPointerCapture(pid); } catch (er) {}
      function done() {
        card.removeEventListener('pointermove', move); card.removeEventListener('pointerup', up); card.removeEventListener('pointercancel', cancel);
        try { card.releasePointerCapture(pid); } catch (er) {}
        if (ghost) ghost.remove();
        card.classList.remove('dragging'); hooks.over(null);
      }
      function move(ev) {
        if (ev.pointerId !== pid) return;
        if (!moved && Math.hypot(ev.clientX - sx, ev.clientY - sy) > 6) {
          moved = true;
          ghost = card.cloneNode(true); ghost.className = 'chip ghost'; ghost.style.width = card.offsetWidth + 'px';
          document.body.appendChild(ghost); card.classList.add('dragging');
        }
        if (moved) {
          ghost.style.left = (ev.clientX - ghost.offsetWidth / 2) + 'px'; ghost.style.top = (ev.clientY - ghost.offsetHeight / 2) + 'px';
          hooks.over(targetAt(ev.clientX, ev.clientY));
        }
      }
      function up(ev) {
        if (ev.pointerId !== pid) return;
        var wasMoved = moved, t = moved ? targetAt(ev.clientX, ev.clientY) : null;
        done();
        if (!wasMoved) hooks.tap(card);
        else if (t) hooks.drop(card, t, ev.clientX, ev.clientY);
      }
      function cancel(ev) { if (ev.pointerId === pid) done(); }
      card.addEventListener('pointermove', move); card.addEventListener('pointerup', up); card.addEventListener('pointercancel', cancel);
    });
    // Enter / Space on a focused card (a click with no pointer: detail is 0)
    card.addEventListener('click', function (e) { if (e.detail === 0 && !hooks.locked()) hooks.tap(card); });
  }

  function chip(text, id) {
    return h('button', { type: 'button', class: 'chip', 'data-id': String(id) }, text);
  }

  /** Cards to put in order. Several answers can be right, the server decides. */
  function order(tokens, onChange) {
    var cards = tokens.map(function (t, i) { return { id: i, text: t }; });
    var line = [];
    var locked = false;
    var lineEl = h('div', { class: 'dnd-line empty', 'data-drop': 'line', role: 'group', 'aria-label': 'Your sentence' });
    var bankEl = h('div', { class: 'dnd-bank', 'data-drop': 'bank', role: 'group', 'aria-label': 'Cards' });
    var el = h('div', { class: 'dnd' }, lineEl, bankEl);

    function inLine(id) { return line.indexOf(id) >= 0; }
    function render() {
      lineEl.replaceChildren.apply(lineEl, line.map(function (id) { return mk(cards[id]); }));
      bankEl.replaceChildren.apply(bankEl, cards.filter(function (c) { return !inLine(c.id); }).map(mk));
      lineEl.classList.toggle('empty', !line.length);
      onChange();
    }
    function mk(c) {
      var b = chip(c.text, c.id);
      if (locked) b.disabled = true;
      drag(b, hooks);
      return b;
    }
    function insertIndex(x, y) {
      var kids = lineEl.querySelectorAll('.chip');
      for (var i = 0; i < kids.length; i++) {
        var r = kids[i].getBoundingClientRect();
        if (y < r.top || (y <= r.bottom && x < r.left + r.width / 2)) return i;
      }
      return kids.length;
    }
    var hooks = {
      locked: function () { return locked; },
      tap: function (card) {
        var id = +card.getAttribute('data-id');
        if (inLine(id)) line.splice(line.indexOf(id), 1); else line.push(id);
        render();
      },
      drop: function (card, target, x, y) {
        var id = +card.getAttribute('data-id');
        var was = line.indexOf(id);
        if (was >= 0) line.splice(was, 1);
        if (target.getAttribute('data-drop') === 'line') {
          var at = insertIndex(x, y);
          line.splice(Math.min(at, line.length), 0, id);
        }
        render();
      },
      over: function (target) {
        lineEl.classList.toggle('hover', !!target && target.getAttribute('data-drop') === 'line');
        bankEl.classList.toggle('hover', !!target && target.getAttribute('data-drop') === 'bank');
      },
    };
    render();
    return {
      el: el,
      answer: function () { return line.map(function (id) { return cards[id].text; }); },
      complete: function () { return line.length === cards.length; },
      lock: function () { locked = true; el.classList.add('locked'); render(); },
      mark: function (ok) { lineEl.classList.add(ok ? 'ok' : 'bad'); },
    };
  }

  /** Slots that take one card each, plus the bank of cards. Used by matching and by word-bank gaps. */
  function slotBoard(count, texts, onChange) {
    var cards = texts.map(function (t, i) { return { id: i, text: t }; });
    var slotCard = []; for (var i = 0; i < count; i++) slotCard.push(null);
    var locked = false;
    var slotEls = slotCard.map(function (_, i) { return h('span', { class: 'slot', 'data-drop': 'slot', 'data-slot': String(i), role: 'group', 'aria-label': 'Gap ' + (i + 1) }); });
    var bankEl = h('div', { class: 'dnd-bank', 'data-drop': 'bank', role: 'group', 'aria-label': 'Cards' });

    function slotOf(id) { return slotCard.indexOf(id); }
    function render() {
      slotEls.forEach(function (s, i) {
        var id = slotCard[i];
        s.classList.toggle('filled', id !== null);
        s.replaceChildren(id !== null ? mk(cards[id]) : null);
      });
      bankEl.replaceChildren.apply(bankEl, cards.filter(function (c) { return slotOf(c.id) < 0; }).map(mk));
      onChange();
    }
    function mk(c) {
      var b = chip(c.text, c.id);
      if (locked) b.disabled = true;
      drag(b, hooks);
      return b;
    }
    var hooks = {
      locked: function () { return locked; },
      tap: function (card) {
        var id = +card.getAttribute('data-id'), at = slotOf(id);
        if (at >= 0) { slotCard[at] = null; }
        else { var free = slotCard.indexOf(null); if (free >= 0) slotCard[free] = id; }
        render();
      },
      drop: function (card, target) {
        var id = +card.getAttribute('data-id'), from = slotOf(id);
        if (target.getAttribute('data-drop') === 'slot') {
          var to = +target.getAttribute('data-slot'), occupant = slotCard[to];
          slotCard[to] = id;
          if (from >= 0) slotCard[from] = occupant; // swap
        } else if (from >= 0) {
          slotCard[from] = null;
        }
        render();
      },
      over: function (target) {
        slotEls.forEach(function (s) { s.classList.toggle('hover', target === s); });
        bankEl.classList.toggle('hover', !!target && target.getAttribute('data-drop') === 'bank');
      },
    };
    render();
    return {
      slots: slotEls, bank: bankEl,
      answer: function () { return slotCard.map(function (id) { return id === null ? '' : cards[id].text; }); },
      complete: function () { return slotCard.indexOf(null) < 0; },
      lock: function () { locked = true; bankEl.classList.add('locked'); render(); },
      mark: function (marks) { slotEls.forEach(function (s, i) { var ok = Array.isArray(marks) ? marks[i] : marks; s.classList.add(ok ? 'ok' : 'bad'); }); },
    };
  }

  /** Match: each left text has a slot; drag the right-hand cards into them. */
  function match(lefts, rights, onChange) {
    var board = slotBoard(lefts.length, rights, onChange);
    var rows = lefts.map(function (l, i) { return h('div', { class: 'dnd-row' }, h('div', { class: 'dnd-left' }, l), board.slots[i]); });
    var el = h('div', { class: 'dnd' }, h('div', { class: 'dnd-rows' }, rows), board.bank);
    return { el: el, answer: board.answer, complete: board.complete, lock: board.lock, mark: board.mark };
  }

  /** Word bank gap: the sentence has inline slots and the learner drags words into them. Returns the sentence node too. */
  function bankGap(q, bank, onChange) {
    var parts = q.split('___');
    var board = slotBoard(parts.length - 1, bank, onChange);
    var sentence = h('div', { class: 'q dnd-sentence' });
    parts.forEach(function (p, i) {
      sentence.appendChild(document.createTextNode(p));
      if (i < parts.length - 1) sentence.appendChild(board.slots[i]);
    });
    return { sentence: sentence, el: h('div', { class: 'dnd' }, board.bank), answer: board.answer, complete: board.complete, lock: board.lock, mark: board.mark };
  }

  window.DnD = { order: order, match: match, bankGap: bankGap };
})();
