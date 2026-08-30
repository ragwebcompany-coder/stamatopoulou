/* Psychoptia — Χριστίνα Σταματοπούλου, Κλινική Ψυχολόγος MSc — site behaviour
   Built by CLINICBRAIN · https://clinicbrain.gr/ */
(function () {
  "use strict";

  var q  = function (s, r) { return (r || document).querySelector(s); };
  var qa = function (s, r) { return Array.prototype.slice.call((r || document).querySelectorAll(s)); };
  var clamp = function (v) { return v < 0 ? 0 : v > 1 ? 1 : v; };
  var reduce = matchMedia("(prefers-reduced-motion: reduce)").matches;
  var EASE = "cubic-bezier(.16,1,.3,1)";
  var header = q("header");

  /* ---------------------------------------------------------- εμφάνιση σελίδας */
  var page = q('[data-anim="page"]');
  if (page && !reduce) {
    page.style.opacity = "0";
    page.style.filter = "blur(10px)";
    requestAnimationFrame(function () {
      page.style.transition = "opacity 1s ease-in-out, filter 1s ease-in-out";
      page.style.opacity = "1";
      page.style.filter = "blur(0px)";
    });
  }

  qa('[data-anim="hero-in"]').forEach(function (el) {
    if (reduce) return;
    var d = el.getAttribute("data-delay") || "0";
    el.style.opacity = "0";
    el.style.transform = "translateY(50px)";
    requestAnimationFrame(function () {
      el.style.transition = "opacity 1s " + EASE + " " + d + "s, transform 1s " + EASE + " " + d + "s";
      el.style.opacity = "1";
      el.style.transform = "none";
    });
  });

  var cue = q('[data-anim="cue"]');
  if (cue && !reduce) {
    cue.style.opacity = "0";
    setTimeout(function () {
      cue.style.transition = "opacity 1s ease";
      cue.style.opacity = "1";
    }, 1000);
  }

  /* ---------------------------------------------------------- εμφάνιση στο scroll */
  var revealables = qa("[data-reveal]");
  if (revealables.length) {
    if (reduce || !("IntersectionObserver" in window)) {
      revealables.forEach(function (el) { el.classList.add("is-in"); });
    } else {
      var io = new IntersectionObserver(function (entries) {
        entries.forEach(function (en) {
          if (en.isIntersecting) { en.target.classList.add("is-in"); io.unobserve(en.target); }
        });
      }, { rootMargin: "0px 0px -12% 0px", threshold: 0.08 });
      revealables.forEach(function (el) { io.observe(el); });
    }
  }

  /* ---------------------------------------------------------- parallax + marquees */
  var heroImg = q('[data-anim="hero-img"]');
  var heroContent = q('[data-anim="hero-content"]');
  var hero = heroImg && heroImg.closest("section");
  var marqs = qa('[data-anim="marq"]');
  var ticking = false;

  function frame() {
    ticking = false;
    var y = window.pageYOffset;
    if (hero) {
      var p = clamp(y / hero.offsetHeight);
      if (heroImg) heroImg.style.transform = "translateY(" + (40 * p) + "%) scale(" + (1 + 0.05 * p) + ")";
      if (heroContent) heroContent.style.opacity = String(1 - p);
    }
    var max = document.documentElement.scrollHeight - window.innerHeight;
    var sp = max > 0 ? clamp(y / max) : 0;
    marqs.forEach(function (m) {
      var dir = m.getAttribute("data-dir") === "1";
      m.style.transform = "translateX(" + (dir ? -50 * sp : -50 + 50 * sp) + "%)";
    });
  }
  function onScroll() { if (!ticking) { ticking = true; requestAnimationFrame(frame); } }
  if (!reduce && (hero || marqs.length)) {
    addEventListener("scroll", onScroll, { passive: true });
    addEventListener("resize", onScroll);
    frame();
  }

  /* ---------------------------------------------------------- FAQ */
  qa(".faq-answer").forEach(function (a) {
    var btn = a.parentElement.querySelector("button");
    if (!btn) return;
    btn.setAttribute("aria-expanded", "false");
    btn.addEventListener("click", function () {
      var open = a.classList.toggle("open");
      btn.setAttribute("aria-expanded", open ? "true" : "false");
      var ic = btn.querySelector("svg");
      if (ic) ic.style.transform = open ? "rotate(180deg)" : "";
    });
  });

  /* ---------------------------------------------------------- μενού κινητού */
  var menu = q("#cb-menu");
  var burger = q("header button.lg\\:hidden");
  function openMenu() {
    if (!menu) return;
    menu.classList.add("open");
    menu.setAttribute("aria-hidden", "false");
    document.body.classList.add("dln-locked");
    if (burger) burger.setAttribute("aria-expanded", "true");
    var f = menu.querySelector("a");
    if (f) f.focus();
  }
  function closeMenu() {
    if (!menu) return;
    menu.classList.remove("open");
    menu.setAttribute("aria-hidden", "true");
    document.body.classList.remove("dln-locked");
    if (burger) burger.setAttribute("aria-expanded", "false");
  }
  if (burger && menu) burger.addEventListener("click", openMenu);
  var mClose = q("#cb-menu-close");
  if (mClose) mClose.addEventListener("click", closeMenu);
  addEventListener("keydown", function (e) { if (e.key === "Escape") closeMenu(); });

  /* ---------------------------------------------------------- ομαλή κύλιση */
  document.addEventListener("click", function (e) {
    var a = e.target.closest && e.target.closest('a[href*="#"]');
    if (!a) return;
    var href = a.getAttribute("href") || "";
    var hash = href.indexOf("#") === 0 ? href : null;
    if (!hash || hash === "#") { if (menu) closeMenu(); return; }
    var el = q(hash);
    if (!el) return;
    e.preventDefault();
    closeMenu();
    var off = header ? header.getBoundingClientRect().height : 0;
    var y = el.getBoundingClientRect().top + window.pageYOffset - off - 8;
    window.scrollTo({ top: y < 0 ? 0 : y, behavior: reduce ? "auto" : "smooth" });
  });
  /* ------------------------------------------------- φόρμα επικοινωνίας
     Δύο τρόποι αποστολής, ανάλογα με το data-endpoint:
       • με endpoint  -> POST με fetch, χωρίς να φύγει ο χρήστης από τη σελίδα
       • χωρίς        -> συνθέτει mailto: και ανοίγει τον mail client
     Το δεύτερο είναι το fallback ώσπου να μπει πραγματικό backend, ώστε η
     φόρμα να μην είναι ποτέ «νεκρή». */
  qa("[data-contact-form]").forEach(function (form) {
    var status = form.querySelector("[data-form-status]");
    var btn = form.querySelector('button[type=submit]');

    function say(msg, state) {
      if (!status) return;
      status.textContent = msg;
      status.setAttribute("data-state", state);
    }

    form.addEventListener("submit", function (e) {
      e.preventDefault();
      if (!form.reportValidity()) return;

      var data = new FormData(form);
      var endpoint = form.getAttribute("data-endpoint");

      if (!endpoint) {
        var body =
          "Ονοματεπώνυμο: " + (data.get("name") || "") + "\n" +
          "Email: " + (data.get("email") || "") + "\n" +
          "Τηλέφωνο: " + (data.get("phone") || "—") + "\n\n" +
          (data.get("message") || "");
        window.location.href = "mailto:" + form.getAttribute("data-mailto") +
          "?subject=" + encodeURIComponent(form.getAttribute("data-subject") || "") +
          "&body=" + encodeURIComponent(body);
        say("Ανοίγει το πρόγραμμα email σας για να σταλεί το μήνυμα.", "ok");
        return;
      }

      btn.disabled = true;
      say("Αποστολή…", "");
      fetch(endpoint, { method: "POST", body: data, headers: { Accept: "application/json" } })
        .then(function (r) {
          if (!r.ok) throw new Error(r.status);
          form.reset();
          say("Ευχαριστώ — το μήνυμα στάλθηκε. Θα επικοινωνήσω μαζί σας σύντομα.", "ok");
        })
        .catch(function () {
          say("Κάτι πήγε στραβά. Δοκιμάστε ξανά ή καλέστε με στο τηλέφωνο.", "error");
        })
        .then(function () { btn.disabled = false; });
    });
  });

})();
