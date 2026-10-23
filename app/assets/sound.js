// Soft sounds for right and wrong answers. Off until the learner switches them on; the choice is kept on this device.
// The tones are made in the browser (no sound files, nothing to download).
(function () {
  'use strict';
  var ctx = null;

  function on() { try { return localStorage.getItem('ef_sound') === '1'; } catch (e) { return false; } }

  /** Browsers only start sound after a tap or key press, so this is called from one (and again on every tap while sound is on). */
  function unlock() {
    try {
      var AC = window.AudioContext || window.webkitAudioContext;
      if (!AC) return false;
      ctx = ctx || new AC();
      if (ctx.state === 'suspended') ctx.resume();
      return true;
    } catch (e) { return false; }
  }

  function set(v) {
    try { localStorage.setItem('ef_sound', v ? '1' : '0'); } catch (e) {}
    if (v) unlock();
  }

  // [pitch in Hz, start in s, length in s]
  var SOUNDS = {
    right: [[659.25, 0, 0.14], [880, 0.1, 0.26]],                                 // two rising notes
    wrong: [[349.23, 0, 0.2], [277.18, 0.13, 0.3]],                               // a soft fall, never harsh
    almost: [[440, 0, 0.22]],                                                      // one neutral note
    fixed: [[587.33, 0, 0.12], [880, 0.09, 0.12], [1174.66, 0.18, 0.14], [1760, 0.3, 0.4]],   // a bright rising chime: an old mistake is fixed
    done: [[523.25, 0, 0.14], [659.25, 0.12, 0.14], [783.99, 0.24, 0.14], [1046.5, 0.36, 0.45]]
  };

  function play(name) {
    if (!on() || !unlock() || !ctx || !SOUNDS[name]) return;
    var t0 = ctx.currentTime + 0.02;
    SOUNDS[name].forEach(function (n) {
      var osc = ctx.createOscillator(), gain = ctx.createGain();
      osc.type = 'sine'; osc.frequency.value = n[0];
      var a = t0 + n[1];
      gain.gain.setValueAtTime(0.0001, a);
      gain.gain.exponentialRampToValueAtTime(0.09, a + 0.02);     // quiet on purpose
      gain.gain.exponentialRampToValueAtTime(0.0001, a + n[2] + 0.12);
      osc.connect(gain); gain.connect(ctx.destination);
      osc.start(a); osc.stop(a + n[2] + 0.15);
    });
  }

  document.addEventListener('pointerdown', function () { if (on()) unlock(); }, { passive: true });
  window.Sound = { on: on, set: set, play: play };
})();
