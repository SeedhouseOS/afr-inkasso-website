/* AFR Inkassokanzlei — Frontend JS
   Mobile-Menu, aktiver Nav-Link, Cookie-Banner. */
(function () {
  'use strict';

  /* ---- Mobile Menu Toggle ---- */
  var toggle = document.querySelector('.menu-toggle');
  var mobileNav = document.querySelector('.mobile-nav');
  if (toggle && mobileNav) {
    toggle.addEventListener('click', function () {
      var open = mobileNav.classList.toggle('open');
      toggle.setAttribute('aria-expanded', open ? 'true' : 'false');
    });
  }

  /* ---- Active Nav Link ---- */
  var current = location.pathname.replace(/\/$/, '') || '/index.html';
  if (current === '') current = '/index.html';
  var fname = current.split('/').pop() || 'index.html';
  document.querySelectorAll('[data-nav]').forEach(function (el) {
    if (el.getAttribute('data-nav') === fname) {
      el.classList.add('active');
    }
  });

  /* ---- Tabs ---- */
  document.querySelectorAll('.tabs').forEach(function (tabs) {
    var buttons = Array.prototype.slice.call(tabs.querySelectorAll('.tab-button'));
    var panels = buttons.map(function (b) { return document.getElementById(b.getAttribute('aria-controls')); });

    function activate(idx, focusBtn) {
      buttons.forEach(function (b, i) {
        var on = i === idx;
        b.setAttribute('aria-selected', on ? 'true' : 'false');
        b.setAttribute('tabindex', on ? '0' : '-1');
        if (panels[i]) panels[i].hidden = !on;
      });
      if (focusBtn) buttons[idx].focus();
    }

    buttons.forEach(function (b, i) {
      b.addEventListener('click', function () { activate(i, false); });
      b.addEventListener('keydown', function (e) {
        var idx = i;
        if (e.key === 'ArrowRight') idx = (i + 1) % buttons.length;
        else if (e.key === 'ArrowLeft') idx = (i - 1 + buttons.length) % buttons.length;
        else if (e.key === 'Home') idx = 0;
        else if (e.key === 'End') idx = buttons.length - 1;
        else return;
        e.preventDefault();
        activate(idx, true);
      });
    });
  });

  /* ---- Cookie Banner ---- */
  var banner = document.getElementById('cookie-banner');
  if (banner) {
    try {
      if (!localStorage.getItem('afr-cookie-ok')) {
        banner.classList.add('show');
      }
    } catch (e) { banner.classList.add('show'); }

    var ok = banner.querySelector('[data-cookie-accept]');
    if (ok) {
      ok.addEventListener('click', function () {
        try { localStorage.setItem('afr-cookie-ok', '1'); } catch (e) {}
        banner.classList.remove('show');
      });
    }
  }
})();
