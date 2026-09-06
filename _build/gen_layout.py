# -*- coding: utf-8 -*-
"""Layout (head / header / footer) + πρόσθετο CSS — Psychoptia."""
import json
from gen_common import *


def alternates(canonical):
    """Τα δύο URL της ίδιας σελίδας, ως (ελληνικό slug, αγγλικό slug).

    Προκύπτουν από το canonical αντί να περνούν ως όρισμα: κάθε σελίδα δηλώνει
    ήδη το canonical της, οπότε το να το ξαναδηλώνει και ως slug θα ήταν δύο
    πηγές αλήθειας που κάποια στιγμή θα αποκλίνουν.
    """
    cur = canonical[len(SITE_URL):].lstrip("/") or "index.html"
    el_slug = EN_TO_EL.get(cur, cur)
    return el_slug, PAGE_SLUGS.get(el_slug)


def head(*, depth, title, description, canonical, ld_graph, og_type="website", noindex=False):
    r = rel(depth)
    el_slug, en_slug = alternates(canonical)
    # Το x-default δείχνει στα ελληνικά: είναι η κύρια αγορά του γραφείου.
    alt = ""
    if en_slug and not noindex:
        alt = (f'<link rel="alternate" hreflang="el" href="{SITE_URL}/{el_slug}">\n'
               f'<link rel="alternate" hreflang="en" href="{SITE_URL}/{en_slug}">\n'
               f'<link rel="alternate" hreflang="x-default" href="{SITE_URL}/{el_slug}">\n')
    lang = i18n.LANG
    locale = "el_GR" if lang == "el" else "en_GB"
    graph = json.dumps({"@context": "https://schema.org", "@graph": ld_graph}, ensure_ascii=False)
    robots = "noindex, nofollow" if noindex else "index, follow, max-image-preview:large, max-snippet:-1"
    return f"""<!DOCTYPE html>
<html lang="{lang}">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title}</title>
<meta name="description" content="{description}">
<meta name="robots" content="{robots}">
<link rel="canonical" href="{canonical}">
{alt}
<meta name="author" content="{pname()}, {specialty()}">
<meta name="theme-color" content="#131257">
<meta name="geo.region" content="GR-A1">
<meta name="geo.placename" content="{city()}, {region()}">
<meta name="geo.position" content="{LAT};{LON}">
<meta name="ICBM" content="{LAT}, {LON}">
<meta property="og:type" content="{og_type}">
<meta property="og:locale" content="{locale}">
<meta property="og:site_name" content="{brand()}">
<meta property="og:title" content="{title}">
<meta property="og:description" content="{description}">
<meta property="og:url" content="{canonical}">
<meta property="og:image" content="{SITE_URL}/assets/img/og-image.jpg">
<meta property="og:image:width" content="1200">
<meta property="og:image:height" content="675">
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:title" content="{title}">
<meta name="twitter:description" content="{description}">
<meta name="twitter:image" content="{SITE_URL}/assets/img/og-image.jpg">
<link rel="icon" href="{r}assets/img/favicon.svg" type="image/svg+xml">
<link rel="apple-touch-icon" href="{r}assets/img/og-image.jpg">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Cormorant+Garamond:ital,wght@0,300;0,400;0,500;0,600;1,300;1,400&amp;family=Inter:wght@300;400;500;600&amp;display=swap" rel="stylesheet">
<link rel="stylesheet" href="{r}assets/css/{ASSETS['css']}">
<script type="application/ld+json">{graph}</script>
</head>
<body>"""


def logo_block(depth, footer=False):
    """Το λογότυπο του πελάτη: το μωβ μαντάλα-λουλούδι πάνω από τον λεκτικό τίτλο.

    Το πρωτότυπο είναι τυπωμένο σε βαθύ indigo φόντο. Στο header χρειαζόμαστε
    διαφανές λογότυπο σε ανοιχτό φόντο, γι' αυτό το `make_assets.py` παράγει
    δύο εκδοχές: `logo.png` (σκούρο μελάνι, για το ανοιχτό header) και
    `logo-light.png` (ανοιχτό μελάνι, για το σκούρο footer)."""
    r = rel(depth)
    # Το ίδιο σήμα σε δύο αναλογίες: κάθετο στο footer, οριζόντιο στο header.
    src, w, h = ("logo-light.png", 900, 685) if footer else ("logo.png", 1155, 330)
    cls = " cb-logo--footer" if footer else ""
    # Δεν μπαίνει υπότιτλος: το ίδιο το λογότυπο γράφει ήδη «ΚΛΙΝΙΚΗ ΨΥΧΟΛΟΓΟΣ MSc».
    return (f'<a class="cb-logo{cls}" href="{r}{page_slug('index.html')}" aria-label="{brand()} — {T("home.link")}">'
            f'<img src="{r}assets/img/{src}" alt="{brand()}" width="{w}" height="{h}" '
            f'{"" if footer else "fetchpriority=\"high\""} decoding="async"></a>')


def nav_links(depth, active):
    """Η κύρια πλοήγηση.

    Όποια καρτέλα στεγάζει επιμέρους πλαίσια κρύβει από κάτω της υπομενού με τα
    παιδιά της — ανοίγει με hover και με πληκτρολόγιο (:focus-within), χωρίς
    JavaScript. Παραμένει κανονικός σύνδεσμος προς τη σελίδα της, ώστε σε οθόνη
    αφής το πάτημα να οδηγεί κάπου αντί να μη κάνει τίποτα.
    """
    r = rel(depth)
    by_href = {S(c): c for c in CATEGORIES}
    out = []
    for label, href in nav_items():
        is_active = href == active
        cls = " is-active" if is_active else ""
        cur = ' aria-current="page"' if is_active else ""
        cat = by_href.get(href)

        if not cat or not cat["children"]:
            out.append(f'<a class="cb-nav__link{cls}" href="{r}{href}"{cur}>{label}</a>')
            continue

        items = "".join(
            f'<a href="{r}{S(k)}">{icon(k["icon"], "w-5 h-5")}'
            f'<span><span class="cb-nav__dt">{L(k, "short")}</span>'
            f'<span class="cb-nav__dd">{L(k, "who")}</span></span></a>'
            for k in cat_children(cat)
        )
        out.append(
            f'<span class="cb-nav__item">'
            f'<a class="cb-nav__link{cls}" href="{r}{href}"{cur} aria-haspopup="true">'
            f'{label}{icon("chev", "cb-nav__caret", "2")}</a>'
            f'<span class="cb-nav__drop">'
            f'<span class="cb-nav__drop__in">{items}'
            f'<a class="cb-nav__drop__all" href="{r}{href}">'
            f'<span>{T("nav.overview")}</span><span>&#8594;</span></a>'
            f'</span></span></span>'
        )
    return "".join(out)


def lang_switch(depth, el_slug, cls="cb-lang"):
    """Ο σύνδεσμος προς την ΙΔΙΑ σελίδα στην άλλη γλώσσα.

    Θέλει το ελληνικό slug της τρέχουσας σελίδας ως κοινό κλειδί των δύο
    εκδόσεων — όχι το `active` του μενού: μια σελίδα υπηρεσίας έχει active
    «ypiresies.html», οπότε ο διακόπτης θα οδηγούσε στον κόμβο υπηρεσιών αντί
    στη μετάφραση της ίδιας σελίδας.
    """
    other = PAGE_SLUGS.get(el_slug)
    if not other:
        return ""
    href = rel(depth) + (other if i18n.LANG == "el" else el_slug)
    return (f'<a class="{cls}" href="{href}" hreflang="{"en" if i18n.LANG == "el" else "el"}" '
            f'aria-label="{T("lang.switchAria")}">{T("lang.switch")}</a>')


def header(depth, active, el_slug=None):
    r = rel(depth)
    links = nav_links(depth, active)
    menu_links = "".join('<a href="%s%s">%s</a>' % (r, href, label) for label, href in nav_items())
    # Οι τρεις κατηγορίες βρίσκονται πλέον στο κυρίως μενού, οπότε εδώ έχει νόημα
    # να φανούν τα φύλλα τους — αλλιώς το υπομενού θα επαναλάμβανε τα ίδια.
    svc_links = "".join('<a href="%s%s">%s</a>' % (r, S(x), L(x, "nav")) for x in SERVICES)
    return f"""<a class="cb-skip" href="#main">{T("skip")}</a>
<div class="cb-topbar">
<div class="cb-topbar__in">
<a class="cb-topbar__item" href="{MAPS}" target="_blank" rel="noopener noreferrer">{icon('pin','w-4 h-4')}<span>{street()}, {city()}</span></a>
<span class="cb-topbar__item cb-topbar__item--hours">{icon('clock','w-4 h-4')}<span>{T("cc.byAppt")}</span></span>
<a class="cb-topbar__item cb-topbar__item--tel" href="tel:+30{PHONE}">{icon('phone','w-4 h-4')}<span>{PHONE_P}</span></a>
</div>
</div>
<header class="cb-header">
<div class="container mx-auto px-6 md:px-12 flex justify-between items-center">
{logo_block(depth)}
<div class="cb-navbar hidden xl:flex items-center gap-8">
<nav class="cb-nav" aria-label="{T("nav.main")}">{links}</nav>
{lang_switch(depth, el_slug)}
<a class="cb-btn cb-btn--sm" href="{r}{page_slug('epikoinonia.html')}#rantevou">{T("cta.book")}</a>
</div>
<button class="xl:hidden cb-burger" aria-label="{T("nav.open")}" aria-controls="cb-menu" aria-expanded="false">
<svg xmlns="http://www.w3.org/2000/svg" width="26" height="26" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" aria-hidden="true"><path d="M4 6h16"/><path d="M4 12h16"/><path d="M4 18h16"/></svg>
</button>
</div>
</header>
<div id="cb-menu" class="dln-overlay" aria-hidden="true">
<button id="cb-menu-close" class="dln-overlay__close" aria-label="{T("nav.close")}">&#215;</button>
<nav class="dln-overlay__nav" aria-label="{T("nav.mobile")}">
{menu_links}
<span class="dln-overlay__sep">{T("nav.services")}</span>
<span class="dln-overlay__sub">{svc_links}</span>
<a class="dln-overlay__tel" href="tel:+30{PHONE}">{PHONE_P}</a>
{lang_switch(depth, el_slug, cls="dln-overlay__lang")}
</nav>
</div>"""


def marquee(word, dir="1", top="16%", dark=False, repeat=4):
    """Γιγαντιαία υπόλευκα γράμματα στο βάθος, που μετακινούνται με το scroll."""
    spans = "".join("<span>%s</span>" % word for _ in range(repeat))
    tone = " cb-marq--dark" if dark else ""
    return (f'<div class="cb-marq{tone}" style="top:{top}" aria-hidden="true">'
            f'<div class="cb-marq__track" data-anim="marq" data-dir="{dir}">{spans}</div></div>')


def mandala_art(depth=0):
    """Το εικαστικό του hero: το μαντάλα-λουλούδι του λογοτύπου, ξαναχτισμένο
    ως καθαρή γραμμή. Τα πέταλα σχεδιάζονται ένα-ένα προς τα έξω, όπως ανοίγει
    ένα άνθος, και κλείνουν με το σύμβολο του απείρου στο κέντρο.

    Ζει σε ξεχωριστό αρχείο SVG ώστε να μη βαραίνει το HTML· η animation
    γράφεται μέσα στο ίδιο το SVG, γιατί το CSS της σελίδας δεν φτάνει σε
    στοιχεία που φορτώνονται μέσω <img>. Παράγεται στο build()."""
    return (f'<img class="cb-thread" src="{rel(depth)}assets/img/mandala.svg" alt="" '
            f'width="1200" height="420" aria-hidden="true" decoding="async">')


def footer_loop():
    """Η ατέρμονη ταινία κειμένου στο βάθος του footer."""
    return ('<div class="cb-footer__loop" aria-hidden="true">'
            '<div data-anim="loop" data-from="0" data-to="-1000">'
            'PSYCHOPTIA · PSYCHOPTIA · PSYCHOPTIA · PSYCHOPTIA</div>'
            '<div data-anim="loop" data-from="-1000" data-to="0">'
            + (T("cta.bookLong") + " ") * 3 + '</div></div>')


def cta_band(depth):
    r = rel(depth)
    return f"""<section class="cb-cta-band">
<div class="container mx-auto px-6 md:px-12">
<div class="cb-cta-band__in">
<div>
<h2 class="cb-cta-band__title">{T("band.title")}</h2>
<p class="cb-cta-band__lede">{T("band.lede").format(s=SESSION, c=city())}</p>
</div>
<div class="cb-cta-band__actions">
<a class="cb-btn cb-btn--light" href="tel:+30{PHONE}">{icon('phone','w-4 h-4')}<span>{PHONE_P}</span></a>
<a class="cb-btn cb-btn--outline" href="{r}{page_slug('epikoinonia.html')}#rantevou">{T("cta.contact")}<span class="cb-btn__arrow">&#8594;</span></a>
</div>
</div>
</div>
</section>"""


def footer(depth):
    r = rel(depth)
    nav_links = "".join('<li><a href="%s%s">%s</a></li>' % (r, href, label) for label, href in nav_items())
    # Στο footer χωράνε και οι έξι: είναι λίστα, όχι μενού.
    svc_links = ('<li><a href="%s%s">%s</a></li>'
                 % (r, page_slug("ypiresies.html"), T("nav.allservices"))) + "".join(
        '<li><a href="%s%s">%s</a></li>' % (r, S(c), L(c, "nav")) for c in CATEGORIES) + "".join(
        '<li class="cb-footer__sub"><a href="%s%s">%s</a></li>' % (r, S(s), L(s, "nav"))
        for c in CATEGORIES for s in cat_children(c))
    areas = " · ".join(AREAS_NEAR)
    return f"""<footer class="cb-footer">
{footer_loop()}
<div class="container mx-auto px-6 md:px-12 relative z-10">
<div class="cb-footer__grid">

<div class="cb-footer__col cb-footer__col--brand">
{logo_block(depth, footer=True)}
<p class="cb-footer__slogan">{slogan()}</p>
<p class="cb-footer__tag">{T("foot.tag").format(c=city())}</p>
<p class="cb-footer__tag cb-footer__tag--sign">{T("foot.sign").format(l=LICENSE)}</p>
<div class="cb-cert">
<span class="cb-cert__badge"><img src="{r}assets/img/thetahealing-think.png" width="320" height="363"
 loading="lazy" decoding="async" alt="{T("cert.thinkAlt")}"></span>
<span class="cb-cert__t">{T("cert.think")}</span>
</div>
</div>

<div class="cb-footer__col">
<h2 class="cb-footer__h">{T("foot.nav")}</h2>
<ul class="cb-footer__list">{nav_links}
<li><a href="{r}{page_slug('psychologos-ilioupoli.html')}">{T("foot.localpage").format(c=city())}</a></li>
<li><a href="{r}{page_slug('syxnes-erotiseis.html')}">{T("nav.faq")}</a></li></ul>
</div>

<div class="cb-footer__col">
<h2 class="cb-footer__h">{T("nav.services")}</h2>
<ul class="cb-footer__list">{svc_links}</ul>
</div>

<div class="cb-footer__col">
<h2 class="cb-footer__h">{T("nav.contact")}</h2>
<ul class="cb-footer__list cb-footer__list--contact">
<li><a href="{MAPS}" target="_blank" rel="noopener noreferrer">{street()}<br>{ZIP_PRETTY} {city()}, {region()}</a></li>
<li><a href="tel:+30{PHONE}">{PHONE_P}</a></li>
<li><a href="mailto:{EMAIL}">{EMAIL}</a></li>
</ul>
<p class="cb-footer__hours">{T("foot.hours")}</p>
{social_links("cb-socials cb-socials--footer")}
</div>

</div>

<p class="cb-footer__areas">{T("foot.areas").format(a=areas)}</p>

<div class="cb-footer__bottom">
<p>© 2026 {brand()}. {T("foot.rights")}</p>
<p class="cb-footer__legal">
<a href="{r}{page_slug('politiki-aporritou.html')}">{T("foot.privacy")}</a>
<a href="{r}{page_slug('oroi-xrisis.html')}">{T("foot.terms")}</a>
<a href="{r}sitemap.xml">{T("foot.sitemap")}</a>
</p>
<p class="cb-credit">Made by <a href="https://clinicbrain.gr/?utm_source=client-site&amp;utm_medium=footer&amp;utm_campaign=made-by" target="_blank" rel="noopener noreferrer">CLINICBRAIN</a></p>
</div>
</div>
</footer>

<a class="cb-fab" href="tel:+30{PHONE}" aria-label="{T("cta.callAria")} {PHONE_P}">
{icon('phone','w-5 h-5')}<span>{T("cta.call")}</span></a>

<script src="{r}assets/js/{ASSETS['js']}" defer></script>
</body>
</html>"""


def breadcrumbs(depth, trail):
    """trail: [(name, relative_href_or_None)]"""
    r = rel(depth)
    parts = []
    for i, (name, href) in enumerate(trail):
        last = i == len(trail) - 1
        if last or not href:
            parts.append('<li aria-current="page">%s</li>' % name)
        else:
            parts.append('<li><a href="%s%s">%s</a></li>' % (r, href, name))
    return ('<nav class="cb-crumbs" aria-label="' + T("crumbs.aria") + '"><ol>%s</ol></nav>'
            % "".join(parts))


def page_hero(eyebrow, h1, lede, crumbs_html, marq_word=None):
    marq = marquee(marq_word, dir="1", top="22%", dark=True, repeat=5) if marq_word else ""
    return f"""<section class="cb-page-hero">
<div class="cb-page-hero__bg" aria-hidden="true"><div class="cb-hero-glow"></div><div class="cb-hero-grid"></div></div>
{marq}
<div class="container mx-auto px-6 md:px-12 relative z-10">
{crumbs_html}
<span class="cb-eyebrow cb-eyebrow--light">{eyebrow}</span>
<h1 class="cb-page-hero__h1">{h1}</h1>
<p class="cb-page-hero__lede">{lede}</p>
</div>
</section>"""


def render(*, depth, title, description, canonical, ld_graph, active, content,
           og_type="website", noindex=False, with_cta=True):
    return (head(depth=depth, title=title, description=description, canonical=canonical,
                 ld_graph=ld_graph, og_type=og_type, noindex=noindex)
            + header(depth, active, alternates(canonical)[0])
            + '\n<main id="main" data-anim="page">\n' + content + '\n</main>\n'
            + (cta_band(depth) if with_cta else "")
            + footer(depth))


# ------------------------------------------------------------------ πρόσθετο CSS
NEW_CSS = r"""
/* ==================== multipage layer — CLINICBRAIN ==================== */
/* λείπουν από το tailwind build που κληρονομήσαμε */
.w-7 { width: 1.75rem; } .h-7 { height: 1.75rem; }
.cb-violet { color: var(--cb-violet); }

html { scroll-behavior: smooth; }
@media (prefers-reduced-motion: reduce) { html { scroll-behavior: auto; } }

/* Δίχτυ ασφαλείας για οριζόντια κύλιση στο κινητό.
   Χρησιμοποιούμε clip και ΟΧΙ hidden: το hidden δημιουργεί scroll container
   και θα ακύρωνε το position:sticky σε header και πλευρική στήλη. */
body { background: var(--color-paper); overflow-x: clip; }
img, svg, iframe, video { max-width: 100%; }
img { height: auto; }
/* Τα παιδιά grid/flex έχουν min-width:auto και αρνούνται να συρρικνωθούν κάτω
   από το περιεχόμενό τους — η κλασική αιτία οριζόντιας κύλισης. */
.cb-grid-2 > *, .cb-cards > *, .cb-footer__grid > *,
.cb-facts li > *, .cb-cta-band__in > *, .cb-contact-card__row > * { min-width: 0; }

/* Μακριές συμβολοσειρές χωρίς κενά (email, διευθύνσεις) */
.cb-contact-card a, .cb-footer__list a, .cb-prose a { overflow-wrap: anywhere; }

.cb-skip { position: absolute; left: -9999px; top: 0; z-index: 10000; background: var(--cb-ink);
  color: #fff; padding: .75rem 1.25rem; font-size: .8rem; }
.cb-skip:focus { left: .5rem; top: .5rem; }
:focus-visible { outline: 2px solid var(--cb-violet); outline-offset: 3px; }

/* ---- topbar + header ---- */
.cb-topbar { background: var(--cb-ink); color: rgba(248,247,252,.78); font-size: .74rem; }
.cb-topbar__in { max-width: 96rem; margin: 0 auto; padding: .5rem 1.5rem; display: flex;
  gap: 1.5rem; align-items: center; justify-content: flex-end; flex-wrap: wrap; }
.cb-topbar__item { display: inline-flex; align-items: center; gap: .45rem; color: inherit;
  text-decoration: none; transition: color .3s ease; }
.cb-topbar__item:hover { color: #fff; }
.cb-topbar__item--tel { font-weight: 500; letter-spacing: .04em; }
@media (max-width: 640px) { .cb-topbar__in { justify-content: center; gap: 1rem; }
  .cb-topbar__item--hours { display: none; } }

.cb-header { position: sticky; top: 0; z-index: 50; background: rgba(248,247,252,.94);
  -webkit-backdrop-filter: blur(10px); backdrop-filter: blur(10px);
  border-bottom: 1px solid rgba(19,18,87,.10); padding: .85rem 0; }

/* ---- λογότυπο (εικόνα πελάτη) ---- */
/* Το `flex: none` είναι σκόπιμο: ως flex item σε γεμάτη σειρά, ο σύνδεσμος του
   λογοτύπου συρρικνωνόταν μέχρι να εξαφανιστεί η εικόνα του αντί να ξεχειλίσει
   ορατά το μενού — σφάλμα που φαινόταν μόνο σε συγκεκριμένα πλάτη. */
.cb-logo { display: block; text-decoration: none; max-width: 14rem; flex: none; }
.cb-logo img { display: block; width: 100%; height: auto; }
.cb-logo__sub { font-size: .55rem; letter-spacing: .26em; text-transform: uppercase;
  color: var(--cb-violet); padding-left: .1rem; }
/* Το footer φιλοξενεί το κάθετο lockup — έχει τον χώρο καθ' ύψος. */
.cb-logo--footer { max-width: 13rem; }
.cb-logo--footer .cb-logo__sub { color: var(--cb-lilac); }
@media (max-width: 480px) { .cb-logo { max-width: 11rem; } }

.cb-nav { display: flex; gap: 1.6rem; }
.cb-nav__link { font-size: .68rem; letter-spacing: .16em; text-transform: uppercase;
  color: var(--cb-ink); text-decoration: none; padding-bottom: .3rem; position: relative;
  white-space: nowrap; transition: color .3s ease; }
.cb-nav__link::after { content: ""; position: absolute; left: 0; bottom: 0; height: 1px; width: 0;
  background: var(--cb-violet); transition: width .35s ease; }
.cb-nav__link:hover { color: var(--cb-violet); }
.cb-nav__link:hover::after, .cb-nav__link.is-active::after { width: 100%; }
.cb-nav__link.is-active { color: var(--cb-violet); }
.cb-burger { color: var(--cb-ink); background: none; border: 0; cursor: pointer; padding: .25rem; }

/* ---- υπομενού «Υπηρεσίες» ----
   Ανοίγει με hover και με πληκτρολόγιο (:focus-within), χωρίς JavaScript.
   Το «Υπηρεσίες» παραμένει κανονικός σύνδεσμος: σε οθόνη αφής, όπου δεν
   υπάρχει hover, το πάτημα οδηγεί στη σελίδα-hub που τα περιέχει όλα. */
.cb-nav { align-items: center; }
.cb-nav__item { position: relative; display: inline-flex; align-items: center; }
.cb-nav__item > .cb-nav__link { display: inline-flex; align-items: center; gap: .3rem; }
.cb-nav__caret { width: .75rem; height: .75rem; transition: transform .3s ease; }
.cb-nav__item:hover .cb-nav__caret,
.cb-nav__item:focus-within .cb-nav__caret { transform: rotate(180deg); }

.cb-nav__drop { position: absolute; top: 100%; left: 50%; z-index: 60;
  /* το padding-top είναι γέφυρα: κρατά το hover ενεργό όσο το ποντίκι
     διασχίζει το κενό ανάμεσα στον σύνδεσμο και στο πάνελ */
  padding-top: 1.35rem; transform: translate(-50%, 10px);
  opacity: 0; visibility: hidden; pointer-events: none;
  transition: opacity .3s ease, transform .3s cubic-bezier(.16,1,.3,1), visibility .3s; }
.cb-nav__item:hover > .cb-nav__drop,
.cb-nav__item:focus-within > .cb-nav__drop {
  opacity: 1; visibility: visible; pointer-events: auto; transform: translate(-50%, 0); }

.cb-nav__drop__in { display: block; min-width: 23rem; background: #fff;
  border: 1px solid rgba(19,18,87,.1); border-radius: 4px; padding: .55rem;
  box-shadow: 0 28px 60px -32px rgba(19,18,87,.5); }
.cb-nav__drop a { display: flex; gap: .8rem; align-items: flex-start; padding: .7rem .8rem;
  border-radius: 3px; text-decoration: none; transition: background-color .25s ease; }
.cb-nav__drop a:hover { background: rgba(107,70,201,.08); }
.cb-nav__drop a > svg { width: 1.15rem; height: 1.15rem; color: var(--cb-violet);
  flex-shrink: 0; margin-top: .15rem; }
.cb-nav__dt { display: block; font-family: var(--font-serif); font-size: 1.02rem;
  line-height: 1.25; color: var(--cb-ink); letter-spacing: 0; text-transform: none; }
.cb-nav__dd { display: block; margin-top: .15rem; font-size: .7rem; font-weight: 300;
  letter-spacing: .04em; color: var(--cb-muted); }
.cb-nav__drop__all { justify-content: space-between; align-items: center !important;
  margin-top: .3rem; border-top: 1px solid rgba(19,18,87,.09); border-radius: 0 0 3px 3px;
  font-size: .62rem; letter-spacing: .2em; color: var(--cb-violet); }
.cb-nav__drop__all span:last-child { transition: transform .3s ease; }
.cb-nav__drop__all:hover span:last-child { transform: translateX(5px); }

/* Το οριζόντιο μενού ξεκινά πλέον στα 1280px και όχι στα 1024: με τις τρεις
   θεραπείες στο πρώτο επίπεδο οι ετικέτες έγιναν επτά, και σε tablet έσπαγαν
   σε δεύτερη γραμμή. Κάτω από αυτό το πλάτος αναλαμβάνει το overlay μενού,
   που τις δείχνει ούτως ή άλλως όλες. */
.xl\:flex { display: none; }
.xl\:hidden { display: block; }
@media (min-width: 1280px) {
  .xl\:flex { display: flex; }
  .xl\:hidden { display: none; }
}
/* Ως τα 1600 οι επτά ετικέτες συν το κουμπί ραντεβού θέλουν σφίξιμο για να
   μείνουν σε μία γραμμή με το λογότυπο. Στα 1440 με κανονικά μεγέθη η σειρά
   ξεχείλιζε και το λογότυπο συνθλιβόταν στο μηδέν. */
@media (min-width: 1280px) and (max-width: 1599px) {
  .cb-navbar { gap: 1.35rem; }
  .cb-nav { gap: .95rem; }
  .cb-nav__link { font-size: .6rem; letter-spacing: .09em; }
  .cb-logo { max-width: 11.5rem; }
  .cb-logo__sub { font-size: .5rem; letter-spacing: .18em; }
  .cb-btn--sm { padding: .65rem .95rem; font-size: .58rem; letter-spacing: .12em; }
}

/* Κοντά στο όριο του lg το κεντραρισμένο πάνελ θα ξέφευγε δεξιά από την οθόνη·
   εκεί το στοιχίζουμε στο δεξί άκρο του συνδέσμου. */
@media (max-width: 1200px) {
  .cb-nav__drop { left: auto; right: 0; transform: translate(0, 10px); }
  .cb-nav__item:hover > .cb-nav__drop,
  .cb-nav__item:focus-within > .cb-nav__drop { transform: translate(0, 0); }
  .cb-nav__drop__in { min-width: 21rem; }
}

@media (prefers-reduced-motion: reduce) {
  .cb-nav__drop, .cb-nav__caret { transition: none; }
}

/* ---- κουμπιά ---- */
.cb-btn { display: inline-flex; align-items: center; gap: .75rem; padding: 1.05rem 2rem;
  font-size: .7rem; letter-spacing: .2em; text-transform: uppercase; text-decoration: none;
  border: 1px solid transparent; border-radius: 2px; cursor: pointer; transition: all .4s ease;
  background: var(--cb-violet); color: #fff; }
.cb-btn:hover { background: var(--cb-ink); color: #fff; }
.cb-btn--sm { padding: .7rem 1.25rem; font-size: .64rem; }
.cb-btn--dark { background: var(--cb-ink); }
.cb-btn--dark:hover { background: var(--cb-violet); }
.cb-btn--light { background: #f8f7fc; color: var(--cb-ink); }
.cb-btn--light:hover { background: #fff; color: var(--cb-ink); }
.cb-btn--outline { background: transparent; color: #f8f7fc; border-color: rgba(248,247,252,.45); }
.cb-btn--outline:hover { background: #f8f7fc; color: var(--cb-ink); border-color: #f8f7fc; }
.cb-btn--ghost { background: transparent; color: var(--cb-ink); border-color: rgba(19,18,87,.22); }
.cb-btn--ghost:hover { background: var(--cb-ink); color: #fff; }
.cb-btn[disabled] { opacity: .55; cursor: progress; }
.cb-btn__arrow { transition: transform .3s ease; }
.cb-btn:hover .cb-btn__arrow { transform: translateX(6px); }

/* ---- overlay μενού ---- */
.dln-overlay__nav { max-height: 88vh; overflow-y: auto; padding: 2rem 1.5rem; }
.dln-overlay__sep { display: block; margin: 1.75rem 0 .5rem; font-size: .62rem; letter-spacing: .28em;
  text-transform: uppercase; color: var(--cb-lilac); }
.dln-overlay__sub { display: flex; flex-direction: column; gap: .55rem; }
.dln-overlay__sub a { font-family: var(--font-sans); font-size: .95rem; color: rgba(248,247,252,.75); }
.dln-overlay__tel { margin-top: 2rem; font-family: var(--font-sans) !important; font-size: 1.1rem !important;
  letter-spacing: .12em; border: 1px solid rgba(248,247,252,.35); padding: .8rem 1.6rem; }

/* ---- hero αρχικής ---- */
.cb-hero { position: relative; overflow: hidden; min-height: 88vh; display: flex; align-items: flex-end;
  background: linear-gradient(160deg,#12104c 0%,#232066 48%,#171459 100%); color: #f8f7fc;
  padding: 7rem 0 6rem; }
.cb-hero__bg { position: absolute; inset: 0; }
.cb-hero__in { max-width: 54rem; }
/* Ο τίτλος της αρχικής είναι το σλόγκαν και τίποτα άλλο — δεν ακολουθεί lede.
   Γι' αυτό γράφεται σε πλάγια Cormorant: πιο καλλιτεχνικό ύφος, μεγαλύτερο μέγεθος
   και ανοιχτό tracking, ώστε να στέκει μόνο του μέσα στο hero. */
.cb-hero__h1 { font-family: var(--font-serif); font-weight: 300; font-style: italic;
  letter-spacing: .005em; font-size: clamp(2.15rem, 5.4vw, 4.1rem); line-height: 1.22;
  margin: 1.3rem 0 0; max-width: 20ch;
  text-shadow: 0 2px 24px rgba(10,10,16,.65), 0 1px 4px rgba(10,10,16,.4); }
.cb-hero__lede { max-width: 46rem; font-weight: 300; font-size: 1.08rem; line-height: 1.8;
  color: rgba(248,247,252,.92); text-shadow: 0 1px 12px rgba(10,10,16,.7); }
.cb-hero__actions { display: flex; flex-wrap: wrap; gap: .9rem; margin-top: 2.5rem; }
.cb-hero .cb-eyebrow--light { text-shadow: 0 1px 10px rgba(10,10,16,.75); }
.cb-hero__cue { position: absolute; left: 50%; transform: translateX(-50%); bottom: 1.4rem; z-index: 2;
  display: flex; flex-direction: column; align-items: center; gap: .4rem;
  font-size: .58rem; letter-spacing: .3em; color: rgba(248,247,252,.5); }
@media (max-width: 640px) { .cb-hero { min-height: 78vh; padding: 4.5rem 0 5rem; } .cb-hero__cue { display: none; } }
/* Ο τίτλος σπάει στο κόμμα μόνο όσο το πρώτο ημιστίχιο χωράει σε μία γραμμή.
   Πιο κάτω από αυτό, η επιβολή της αλλαγής άφηνε ορφανό το «κατανόηση,» —
   οπότε το <br> κρύβεται και το σπάσιμο το αναλαμβάνει το text-wrap. */
@media (max-width: 1023px) {
  .cb-hero__br { display: none; }
  .cb-hero__h1 { text-wrap: balance; }
}

/* ---- η φωτογραφία πίσω από το hero ----
   Πήρε τη θέση του διακοσμητικού μαντάλα. Δεν είναι background-image αλλά <img>:
   έτσι φορτώνει με προτεραιότητα (fetchpriority) και μετράει ως το LCP στοιχείο,
   αντί να περιμένει το CSS. Το `object-position` κρατά το πρόσωπο στο κάδρο όταν
   το cover κόβει — καθ' ύψος σε πλατιά οθόνη, πλάγια σε κινητό. */
.cb-hero__photo { position: absolute; inset: 0; width: 100%; height: 100%;
  object-fit: cover; object-position: 50% 46%; }
/* Η φωτογραφία μένει στα χρώματά της: το πέπλο είναι ουδέτερο σκούρο, όχι μωβ,
   και υπάρχει μόνο όσο χρειάζεται για να διαβάζεται το λευκό κείμενο —
   μία βαθμίδα καθ' ύψος για τα κουμπιά κάτω, μία πλάγια για τον τίτλο αριστερά. */
.cb-hero__scrim { position: absolute; inset: 0;
  background: linear-gradient(180deg, rgba(10,10,16,.26) 0%, rgba(10,10,16,0) 34%, rgba(10,10,16,.72) 100%),
              linear-gradient(96deg, rgba(10,10,16,.58) 0%, rgba(10,10,16,.10) 58%, rgba(10,10,16,0) 100%); }
@media (max-width: 900px) {
  .cb-hero__photo { object-position: 54% 38%; }
  /* Σε κινητό ο τίτλος δεν έχει πού αλλού να πάει παρά πάνω στη φωτογραφία,
     οπότε εδώ το πέπλο μένει πιο κλειστό απ' ό,τι σε πλατιά οθόνη. */
  .cb-hero__scrim { background: linear-gradient(180deg, rgba(10,10,16,.38) 0%, rgba(10,10,16,.26) 26%, rgba(10,10,16,.82) 100%); }
}

/* ---- το εικαστικό μαντάλα ----
   Είναι <img> με εξωτερικό SVG· η animation ζει μέσα στο αρχείο.
   Το άνθος κάθεται δεξιά, πίσω από το κείμενο του hero, όπως στο λογότυπο. */
.cb-thread { position: absolute; right: -6%; top: 50%; width: min(62%, 46rem);
  height: auto; transform: translateY(-50%); opacity: .5; }
/* Σε στενή οθόνη το νήμα γίνεται μόλις 100px ψηλό και, κεντραρισμένο, κόβει
   την παράγραφο στη μέση. Το ανεβάζουμε στον κενό χώρο πάνω από τον τίτλο. */
@media (max-width: 900px) {
  .cb-thread { top: 2%; right: -22%; width: 88%; transform: none; opacity: .3; }
}

/* ---- εσωτερικό hero ---- */
.cb-page-hero { position: relative; overflow: hidden;
  background: linear-gradient(160deg,#12104c 0%,#232066 52%,#171459 100%);
  color: #f8f7fc; padding: 5.5rem 0 4.5rem; }
.cb-page-hero__bg { position: absolute; inset: 0; }
.cb-page-hero__h1 { font-family: var(--font-serif); font-weight: 300; letter-spacing: -.02em;
  font-size: clamp(2.1rem, 5.2vw, 3.6rem); line-height: 1.1; margin: .5rem 0 1rem; max-width: 22ch; }
.cb-page-hero__lede { max-width: 60ch; font-weight: 300; line-height: 1.75; color: rgba(248,247,252,.78);
  font-size: 1.05rem; }
.cb-eyebrow { display: inline-block; font-size: .66rem; letter-spacing: .28em; text-transform: uppercase;
  color: var(--cb-violet); border-left: 2px solid currentColor; padding-left: .85rem; }
.cb-eyebrow--light { color: var(--cb-lilac); }

/* ---- ψίχουλα ---- */
.cb-crumbs { margin-bottom: 1.6rem; }
.cb-crumbs ol { display: flex; flex-wrap: wrap; gap: .4rem; list-style: none; margin: 0; padding: 0;
  font-size: .7rem; letter-spacing: .1em; color: rgba(248,247,252,.6); }
.cb-crumbs li + li::before { content: "/"; margin-right: .4rem; opacity: .5; }
.cb-crumbs a { color: inherit; text-decoration: none; }
.cb-crumbs a:hover { color: #fff; text-decoration: underline; text-underline-offset: 3px; }

/* ---- γιγαντιαία γράμματα στο βάθος (κινούνται με το scroll) ---- */
.cb-marq { position: absolute; left: 0; width: 100%; z-index: 0; display: flex;
  overflow: hidden; white-space: nowrap; pointer-events: none; user-select: none;
  opacity: .045; }
.cb-marq--dark { opacity: .05; }
.cb-marq__track { display: flex; gap: 4rem; font-family: var(--font-serif); font-weight: 300;
  font-size: 20vw; line-height: .92; text-transform: uppercase; letter-spacing: -.05em;
  color: var(--cb-ink); will-change: transform; }
.cb-marq--dark .cb-marq__track { color: #f8f7fc; }
@media (max-width: 768px) { .cb-marq__track { font-size: 30vw; } }
@media (prefers-reduced-motion: reduce) { .cb-marq__track { transform: none !important; } }

/* Μόνο οι ενότητες με αυτή την κλάση ψαλιδίζουν — το overflow:hidden θα
   ακύρωνε το position:sticky της πλευρικής στήλης στις υπόλοιπες. */
.cb-section--marq { position: relative; overflow: hidden; }
.cb-section--marq > .container { position: relative; z-index: 10; }

.cb-footer { position: relative; overflow: hidden; }
.cb-footer__loop { position: absolute; inset: 0; z-index: 0; opacity: .045;
  display: flex; flex-direction: column; justify-content: center; gap: 2rem;
  overflow: hidden; white-space: nowrap; pointer-events: none; user-select: none; }
.cb-footer__loop > div { font-family: var(--font-serif); font-weight: 300; font-size: 15vw;
  line-height: 1; text-transform: uppercase; letter-spacing: -.05em; color: #f8f7fc; }

/* ---- τυπογραφία άρθρου ---- */
.cb-section { padding: 5.5rem 0; }
.cb-section--tight { padding: 4rem 0; }
.cb-section--beige { background: var(--color-lilac); }
.cb-section--dark { background: var(--cb-ink); color: #f8f7fc; }
.cb-h2 { font-family: var(--font-serif); font-weight: 300; letter-spacing: -.02em;
  font-size: clamp(1.85rem, 4vw, 2.9rem); line-height: 1.15; color: var(--cb-ink); margin: .6rem 0 1.1rem; }
.cb-section--dark .cb-h2 { color: #f8f7fc; }
.cb-h3 { font-family: var(--font-serif); font-weight: 400; font-size: 1.45rem; color: var(--cb-ink);
  margin: 2.4rem 0 .7rem; }
.cb-lede { font-size: 1.1rem; font-weight: 300; line-height: 1.8; color: var(--cb-muted); max-width: 62ch; }
.cb-prose { font-weight: 300; line-height: 1.85; color: var(--cb-muted); max-width: 68ch; }
.cb-prose p { margin: 0 0 1.15rem; }
.cb-prose strong { font-weight: 500; color: var(--cb-ink); }
.cb-prose a { color: var(--cb-violet); text-decoration: underline; text-underline-offset: 3px; }
.cb-prose ul, .cb-prose ol { margin: 0 0 1.4rem; padding-left: 0; list-style: none; }
.cb-prose ul li { position: relative; padding-left: 1.6rem; margin-bottom: .6rem; }
.cb-prose ul li::before { content: ""; position: absolute; left: .25rem; top: .72em; width: 6px; height: 6px;
  border-radius: 50%; background: var(--cb-violet); }
.cb-prose ol { counter-reset: cb; }
.cb-prose ol li { position: relative; padding-left: 2rem; margin-bottom: .6rem; counter-increment: cb; }
.cb-prose ol li::before { content: counter(cb); position: absolute; left: 0; top: 0;
  font-size: .72rem; letter-spacing: .1em; color: var(--cb-violet); padding-top: .35em; }
.cb-prose h3 { font-family: var(--font-serif); font-weight: 400; font-size: 1.35rem;
  color: var(--cb-ink); margin: 2rem 0 .6rem; }
.cb-grid-2 { display: grid; grid-template-columns: 1fr; gap: 3rem; }
@media (min-width: 1024px) { .cb-grid-2 { grid-template-columns: 1fr 1fr; gap: 4.5rem; align-items: start; } }
@media (min-width: 1024px) { .cb-grid-2--aside { grid-template-columns: minmax(0,1.55fr) minmax(0,1fr); } }

/* ---- κάρτες ---- */
.cb-cards { display: grid; grid-template-columns: 1fr; gap: 1.5rem; }
@media (min-width: 640px) { .cb-cards { grid-template-columns: repeat(2, 1fr); } }
@media (min-width: 1024px) { .cb-cards--3 { grid-template-columns: repeat(3, 1fr); } }
.cb-card { display: flex; flex-direction: column; gap: .85rem; padding: 2rem 1.75rem;
  background: #fff; border: 1px solid rgba(19,18,87,.08); border-radius: 4px; text-decoration: none;
  transition: transform .4s ease, box-shadow .4s ease, border-color .4s ease; }
.cb-card:hover { transform: translateY(-4px); border-color: rgba(107,70,201,.4);
  box-shadow: 0 18px 40px -24px rgba(19,18,87,.4); }
.cb-card__ic { color: var(--cb-violet); }
.cb-card__t { font-family: var(--font-serif); font-size: 1.3rem; color: var(--cb-ink); line-height: 1.25; }
.cb-card__d { font-size: .9rem; font-weight: 300; line-height: 1.65; color: var(--cb-muted); }
.cb-card__more { margin-top: auto; padding-top: .6rem; font-size: .66rem; letter-spacing: .2em;
  text-transform: uppercase; color: var(--cb-violet); }
.cb-card__more span { display: inline-block; transition: transform .3s ease; }
.cb-card:hover .cb-card__more span { transform: translateX(5px); }

/* ---- κάρτες υπηρεσίας, με τη φωτογραφία της κατηγορίας ----
   Η εικόνα πιάνει όλο το πλάτος, οπότε η κάρτα χάνει το padding της και το
   ξαναδίνει στα κειμενικά της παιδιά. Το `overflow:hidden` χρειάζεται για να
   κοπεί η εικόνα στη γωνία της κάρτας και για να μη βγει έξω στο zoom. */
.cb-card--photo { padding: 0 0 1.9rem; gap: .8rem; overflow: hidden; }
.cb-card--photo > :not(.cb-card__media) { margin-left: 1.75rem; margin-right: 1.75rem; }
.cb-card__media { position: relative; display: block; margin-bottom: .5rem;
  aspect-ratio: 16 / 10; background: rgba(19,18,87,.06); overflow: hidden; }
.cb-card__media img { width: 100%; height: 100%; object-fit: cover; display: block;
  transition: transform .7s cubic-bezier(.2,.6,.2,1); }
.cb-card:hover .cb-card__media img { transform: scale(1.045); }
/* Σκίαση μόνο στο κάτω μέρος, ώστε το μετάλλιο του εικονιδίου να ξεχωρίζει από
   ό,τι κι αν τύχει να έχει η φωτογραφία από κάτω. */
.cb-card__media::after { content: ""; position: absolute; inset: auto 0 0 0; height: 42%;
  background: linear-gradient(to top, rgba(19,18,87,.34), rgba(19,18,87,0)); }
.cb-card--photo .cb-card__ic { position: absolute; left: 1.1rem; bottom: .95rem; z-index: 1;
  display: grid; place-items: center; width: 2.9rem; height: 2.9rem; border-radius: 50%;
  background: rgba(255,255,255,.95); box-shadow: 0 8px 22px -10px rgba(19,18,87,.7); }
.cb-card--photo .cb-card__ic svg { width: 1.4rem; height: 1.4rem; }
@media (prefers-reduced-motion: reduce) { .cb-card__media img { transition: none; }
  .cb-card:hover .cb-card__media img { transform: none; } }

/* ---- πλευρική στήλη ---- */
.cb-aside { position: sticky; top: 6.5rem; display: flex; flex-direction: column; gap: 1.5rem; }
.cb-contact-card { background: #fff; border: 1px solid rgba(19,18,87,.09); border-radius: 4px;
  padding: 1.9rem 1.7rem; display: flex; flex-direction: column; gap: 1.35rem; }
.cb-contact-card__row { display: flex; gap: .85rem; align-items: flex-start; font-weight: 300;
  color: var(--cb-ink); font-size: .95rem; }
.cb-contact-card__row a { color: inherit; text-decoration: none; }
.cb-contact-card__row a:hover { color: var(--cb-violet); text-decoration: underline; text-underline-offset: 3px; }
.cb-contact-card__k { display: block; font-size: .62rem; letter-spacing: .2em; text-transform: uppercase;
  color: var(--cb-violet); margin-bottom: .3rem; }
.cb-open-badge { display: inline-block; font-size: .58rem; letter-spacing: .14em; text-transform: uppercase;
  padding: .12rem .5rem; border-radius: 999px; vertical-align: middle; }
.cb-open-badge.is-open { background: rgba(107,70,201,.16); color: #3a2790; }
.cb-open-badge.is-closed { background: rgba(19,18,87,.09); color: var(--cb-muted); }
.cb-topbar .cb-open-badge.is-open { color: #b79ae8; background: rgba(183,154,232,.14); }
.cb-topbar .cb-open-badge.is-closed { color: rgba(248,247,252,.7); background: rgba(248,247,252,.1); }

/* ---- πλαίσιο Νοηματικής ---- */
.cb-access { display: flex; gap: 1rem; align-items: flex-start; padding: 1.35rem 1.5rem;
  background: rgba(107,70,201,.07); border: 1px solid rgba(107,70,201,.22); border-radius: 4px; }
.cb-access__ic { width: 1.75rem; height: 1.75rem; color: var(--cb-violet); flex-shrink: 0; }
.cb-access strong { display: block; font-weight: 500; color: var(--cb-ink); font-size: .95rem; }
.cb-access span { display: block; margin-top: .25rem; font-weight: 300; font-size: .85rem;
  line-height: 1.6; color: var(--cb-muted); }
.cb-section--dark .cb-access { background: rgba(183,154,232,.08); border-color: rgba(183,154,232,.25); }
.cb-section--dark .cb-access__ic { color: var(--cb-lilac); }
.cb-section--dark .cb-access strong { color: #f8f7fc; }
.cb-section--dark .cb-access span { color: rgba(248,247,252,.65); }

/* ---- πίνακας γρήγορων στοιχείων ---- */
.cb-facts { list-style: none; margin: 0; padding: 0; border-top: 1px solid rgba(19,18,87,.12); }
.cb-facts li { display: grid; grid-template-columns: 1fr; gap: .2rem; padding: .95rem 0;
  border-bottom: 1px solid rgba(19,18,87,.12); font-weight: 300; color: var(--cb-muted); }
@media (min-width: 480px) { .cb-facts li { grid-template-columns: 10.5rem 1fr; gap: 1rem; align-items: baseline; } }
.cb-facts b { font-weight: 400; font-size: .66rem; letter-spacing: .18em; text-transform: uppercase;
  color: var(--cb-violet); }

/* ---- χρονολόγιο βιογραφικού ---- */
.cb-time { list-style: none; margin: 2rem 0 0; padding: 0 0 0 1.6rem;
  border-left: 1px solid rgba(19,18,87,.14); }
.cb-time li { position: relative; padding-bottom: 2rem; }
.cb-time li::before { content: ""; position: absolute; left: -1.98rem; top: .45rem; width: 9px; height: 9px;
  border-radius: 50%; background: var(--color-paper); border: 1.5px solid var(--cb-violet); }
.cb-time__k { display: block; font-size: .66rem; letter-spacing: .2em; text-transform: uppercase;
  color: var(--cb-violet); margin-bottom: .35rem; }
.cb-time__t { display: block; font-family: var(--font-serif); font-size: 1.35rem; line-height: 1.3;
  color: var(--cb-ink); }
.cb-time__d { display: block; margin-top: .5rem; font-weight: 300; line-height: 1.8;
  color: var(--cb-muted); max-width: 62ch; }
.cb-section--beige .cb-time li::before { background: var(--color-lilac); }

/* ---- απλή λίστα (επιμόρφωση / ομιλίες) ---- */
.cb-list { list-style: none; margin: 1.5rem 0 0; padding: 0; }
.cb-list li { display: grid; grid-template-columns: 1fr; gap: .15rem; padding: .8rem 0;
  border-bottom: 1px solid rgba(19,18,87,.1); font-weight: 300; color: var(--cb-muted); font-size: .95rem; }
/* «2014 — σήμερα» χρειάζεται περισσότερο χώρο από ένα σκέτο έτος */
@media (min-width: 560px) { .cb-list li { grid-template-columns: 8rem 1fr; gap: 1.25rem; align-items: baseline; } }
.cb-list b { font-weight: 400; font-size: .7rem; letter-spacing: .14em; color: var(--cb-violet); }
.cb-list em { font-style: normal; display: block; font-size: .82rem; opacity: .78; margin-top: .15rem; }

/* ---- CTA band ---- */
.cb-cta-band { background: linear-gradient(135deg,#181555 0%,#332a86 100%); color: #f8f7fc; padding: 3.5rem 0; }
.cb-cta-band__in { display: flex; flex-direction: column; gap: 1.75rem; align-items: flex-start;
  justify-content: space-between; }
@media (min-width: 900px) { .cb-cta-band__in { flex-direction: row; align-items: center; } }
.cb-cta-band__title { font-family: var(--font-serif); font-weight: 300; font-size: clamp(1.6rem,3.2vw,2.3rem); }
.cb-cta-band__lede { font-weight: 300; color: rgba(248,247,252,.75); margin-top: .4rem; }
.cb-cta-band__actions { display: flex; flex-wrap: wrap; gap: .9rem; }

/* ---- online ραντεβού (Calendly) ---- */
/* ---- φόρμα επικοινωνίας ----
   Αντικατέστησε το πλαίσιο «κλείστε ραντεβού τηλεφωνικά»: η πελάτισσα ζήτησε
   απλή φόρμα, χωρίς ατζέντα και χωρίς σύνθετο ερωτηματολόγιο. */
.cb-form-wrap { background: #fff; border: 1px solid rgba(19,18,87,.09); border-radius: 4px;
  padding: 1.6rem; box-shadow: 0 24px 60px -44px rgba(19,18,87,.5); }
@media (min-width: 768px) { .cb-form-wrap { padding: 2.1rem; } }
.cb-form__lede { font-family: var(--font-serif); font-size: 1.15rem; font-weight: 300;
  line-height: 1.6; color: var(--cb-ink); margin: 0 0 1.6rem; max-width: 44ch; }
.cb-form { display: flex; flex-direction: column; gap: 1.05rem; }
.cb-form__row { display: grid; grid-template-columns: 1fr; gap: 1.05rem; }
@media (min-width: 620px) { .cb-form__row { grid-template-columns: 1fr 1fr; } }
.cb-field { display: flex; flex-direction: column; gap: .4rem; }
.cb-field > span { font-size: .68rem; letter-spacing: .17em; text-transform: uppercase;
  color: var(--cb-muted); }
.cb-field > span em { color: var(--cb-violet); font-style: normal; }
.cb-field > span i { font-style: normal; text-transform: none; letter-spacing: .04em;
  opacity: .7; font-size: .72rem; }
.cb-field input, .cb-field textarea { width: 100%; font: inherit; font-weight: 300;
  color: var(--cb-ink); background: rgba(19,18,87,.03); border: 1px solid rgba(19,18,87,.14);
  border-radius: 3px; padding: .8rem .9rem; transition: border-color .2s ease, background-color .2s ease; }
.cb-field textarea { resize: vertical; min-height: 8rem; line-height: 1.65; }
.cb-field input:focus, .cb-field textarea:focus { outline: none; background: #fff;
  border-color: var(--cb-violet); box-shadow: 0 0 0 3px rgba(107,70,201,.16); }
/* Το :user-invalid δείχνει σφάλμα μόνο αφού ασχοληθεί ο χρήστης με το πεδίο —
   σε αντίθεση με το :invalid, που θα έβαφε κόκκινη όλη τη φόρμα στο φόρτωμα. */
.cb-field input:user-invalid, .cb-field textarea:user-invalid { border-color: #c0392b;
  background: rgba(192,57,43,.04); }
.cb-check { display: flex; gap: .7rem; align-items: flex-start; font-size: .82rem;
  font-weight: 300; line-height: 1.6; color: var(--cb-muted); }
.cb-check input { margin-top: .18rem; width: 1.05rem; height: 1.05rem; flex: none;
  accent-color: var(--cb-violet); }
.cb-check a { color: var(--cb-deep); font-weight: 500; }
.cb-form button[type=submit] { align-self: flex-start; justify-content: center; }
.cb-form__status { margin: 0; font-size: .85rem; font-weight: 300; line-height: 1.6; }
.cb-form__status[data-state="ok"] { color: #1e7d44; }
.cb-form__status[data-state="error"] { color: #c0392b; }
.cb-form__note { margin: 1.4rem 0 0; padding-top: 1.2rem; border-top: 1px solid rgba(19,18,87,.1);
  font-size: .78rem; font-weight: 300; line-height: 1.7; color: var(--cb-muted); }
.cb-form__note a { color: var(--cb-deep); font-weight: 500; }

/* ---- περιοχές εξυπηρέτησης ---- */
.cb-areas__h { font-family: var(--font-serif); font-size: 1.35rem; font-weight: 300;
  color: var(--cb-ink); margin: 2.2rem 0 .6rem; }
.cb-areas__h:first-child { margin-top: 0; }
.cb-areas__d { font-weight: 300; line-height: 1.7; color: var(--cb-muted); margin: 0 0 .9rem; }
.cb-area-list { display: flex; flex-wrap: wrap; gap: .45rem; margin-bottom: 1.4rem; }
.cb-area { font-size: .8rem; font-weight: 300; color: var(--cb-muted);
  border: 1px solid rgba(19,18,87,.12); border-radius: 999px; padding: .34rem .8rem; }
/* Οι όμορες περιοχές ξεχωρίζουν: εκεί η εγγύτητα είναι πραγματικό κριτήριο. */
.cb-area--near { color: var(--cb-deep); border-color: rgba(107,70,201,.3);
  background: rgba(107,70,201,.05); }

/* ---- footer ---- */
.cb-footer { background: var(--cb-ink); color: rgba(248,247,252,.7); padding: 4.5rem 0 2rem;
  font-weight: 300; font-size: .9rem; }
.cb-footer__grid { display: grid; grid-template-columns: 1fr; gap: 2.75rem; }
@media (min-width: 640px) { .cb-footer__grid { grid-template-columns: repeat(2, 1fr); } }
@media (min-width: 1024px) { .cb-footer__grid { grid-template-columns: 1.4fr 1fr 1.2fr 1.4fr; gap: 3rem; } }
.cb-footer__col { min-width: 0; }
.cb-footer__col--brand { max-width: 34ch; }
/* Κάτω από το σήμα στο footer, το σλόγκαν παίζει τον ρόλο του υπότιτλου του
   λογοτύπου — γι' αυτό πιο κοντά του απ' ό,τι το περιγραφικό κείμενο. */
.cb-footer__slogan { font-family: var(--font-serif); font-style: italic; font-weight: 300;
  font-size: 1.02rem; line-height: 1.55; max-width: 32ch; margin: 1.1rem 0 0;
  text-wrap: balance; color: rgba(248,247,252,.9); }
/* ---- σήματα κοινωνικών δικτύων ----
   Τα εικονίδια φέρουν τα δικά τους χρώματα, οπότε ο κύκλος από κάτω μένει
   ουδέτερος· στο σκούρο footer γίνεται λευκός για να μη «βουλιάζουν». */
/* ---- διακόπτης γλώσσας ---- */
.cb-lang { display: inline-grid; place-items: center; min-width: 2.4rem; height: 2.1rem;
  padding: 0 .55rem; border: 1px solid rgba(19,18,87,.18); border-radius: 999px;
  font-size: .68rem; letter-spacing: .14em; font-weight: 500; color: var(--cb-deep);
  text-decoration: none; transition: background-color .25s ease, border-color .25s ease; }
.cb-lang:hover { background: rgba(107,70,201,.08); border-color: rgba(107,70,201,.4); }
.dln-overlay__lang { display: inline-block; margin-top: 1rem; padding: .55rem 1.1rem;
  border: 1px solid rgba(248,247,252,.35); border-radius: 999px; color: rgba(248,247,252,.85);
  font-size: .72rem; letter-spacing: .18em; text-decoration: none; }

.cb-socials { display: inline-flex; flex-wrap: wrap; gap: .55rem; align-items: center; }
.cb-socials__a { display: grid; place-items: center; width: 2.4rem; height: 2.4rem;
  border-radius: 50%; background: rgba(19,18,87,.05); text-decoration: none;
  transition: transform .25s ease, background-color .25s ease; }
.cb-socials__a svg { width: 1.35rem; height: 1.35rem; display: block; }
.cb-socials__a:hover { transform: translateY(-2px); background: rgba(19,18,87,.1); }
.cb-socials--footer { margin-top: 1.35rem; }
.cb-socials--footer .cb-socials__a { background: rgba(248,247,252,.92); }
.cb-socials--footer .cb-socials__a:hover { background: #fff; }
@media (prefers-reduced-motion: reduce) { .cb-socials__a { transition: none; }
  .cb-socials__a:hover { transform: none; } }

/* ---- σήμα πιστοποίησης στο footer ----
   Το σήμα του φορέα είναι σχεδόν μαύρο και πάνω στο indigo θα χανόταν, οπότε
   κάθεται σε λευκή κάρτα — όπως τυπώνεται και στα ίδια τα πιστοποιητικά. */
.cb-cert { margin-top: 1.6rem; display: flex; flex-direction: column;
  align-items: flex-start; gap: .6rem; }
.cb-cert__badge { display: block; background: #fff; border-radius: 6px; padding: .55rem .7rem;
  line-height: 0; box-shadow: 0 10px 26px -18px rgba(0,0,0,.7); }
.cb-cert__badge img { width: 7.5rem; height: auto; display: block; }
/* Το 30ch έσπαγε τη λεζάντα σε δύο γραμμές χωρίς λόγο: χωράει ολόκληρη στο
   πλάτος της στήλης, οπότε το όριο το βάζει η στήλη και όχι εμείς. */
.cb-cert__t { font-size: .74rem; font-weight: 300; line-height: 1.55; color: var(--cb-lilac);
  text-wrap: balance; }

/* Οι ηλικιακές ομάδες κρέμονται οπτικά από την καρτέλα τους. */
.cb-footer__sub { padding-left: .9rem; font-size: .84rem; opacity: .78; }

.cb-footer__tag { margin: 1.25rem 0 0; max-width: 32ch; line-height: 1.7; color: rgba(248,247,252,.55); }
.cb-footer__tag--sign { margin-top: .7rem; margin-bottom: 1.5rem; color: var(--cb-lilac); }
.cb-footer__h { font-size: .64rem; letter-spacing: .24em; text-transform: uppercase;
  color: var(--cb-lilac); margin-bottom: 1.1rem; font-weight: 500; }
.cb-footer__list { list-style: none; margin: 0; padding: 0; display: flex; flex-direction: column; gap: .6rem; }
.cb-footer__list a { color: inherit; text-decoration: none; transition: color .3s ease; }
.cb-footer__list a:hover { color: #fff; text-decoration: underline; text-underline-offset: 3px; }
.cb-footer__list--contact { gap: .75rem; }
.cb-footer__hours { margin-top: 1.1rem; font-size: .8rem; line-height: 1.7; color: rgba(248,247,252,.5); }
.cb-footer__areas { margin-top: 3rem; padding-top: 1.5rem; border-top: 1px solid rgba(248,247,252,.1);
  font-size: .8rem; line-height: 1.8; color: rgba(248,247,252,.5); }
.cb-footer__areas strong { color: rgba(248,247,252,.75); font-weight: 500; }
.cb-footer__bottom { margin-top: 1.5rem; padding-top: 1.5rem; border-top: 1px solid rgba(248,247,252,.1);
  display: flex; flex-wrap: wrap; gap: .7rem 1.75rem; align-items: center; justify-content: space-between;
  font-size: .74rem; }
.cb-footer__legal { display: flex; flex-wrap: wrap; gap: 1.25rem; }
.cb-footer__legal a { color: inherit; text-decoration: none; }
.cb-footer__legal a:hover { color: #fff; text-decoration: underline; text-underline-offset: 3px; }

/* Το αιωρούμενο κουμπί κλήσης είναι position:fixed κάτω δεξιά και, στο τέρμα
   της σελίδας, κάθεται πάνω στην τελευταία γραμμή του footer — έκρυβε το
   «Made by CLINICBRAIN» και τον «Χάρτη ιστότοπου».
   Το λύνουμε με κατακόρυφο κενό αντί για οριζόντιο: το κουμπί πιάνει τα κάτω
   ~70px του παραθύρου, οπότε ο footer κρατά τόσο κενό από κάτω. Δουλεύει σε
   κάθε πλάτος, χωρίς να πειράζει τη στοίχιση της γραμμής. */
.cb-footer { padding-bottom: 6.5rem; }

/* Ο σύνδεσμος Facebook: το μπλε της πλατφόρμας δεν ανήκει στην παλέτα
   (άσπρο–μαύρο–γκρι–μέντα), οπότε κρατάμε μόνο το σχήμα. */
.cb-fb { background: transparent; border: 1px solid rgba(248,247,252,.28);
  color: rgba(248,247,252,.8); font-size: .62rem; letter-spacing: .2em; padding: .7rem 1.2rem; }
.cb-fb:hover { background: rgba(183,154,232,.12); border-color: var(--cb-lilac);
  color: #fff; transform: translateY(-2px); }

/* ---- floating call ---- */
.cb-fab { position: fixed; right: 1.25rem; bottom: 1.25rem; z-index: 45; display: inline-flex;
  align-items: center; gap: .6rem; padding: .95rem 1.4rem; border-radius: 999px; background: var(--cb-deep);
  color: #fff; text-decoration: none; font-size: .68rem; letter-spacing: .18em; text-transform: uppercase;
  box-shadow: 0 14px 30px -14px rgba(76,47,158,.75); transition: transform .3s ease, background-color .3s ease; }
.cb-fab:hover { transform: translateY(-3px); background: var(--cb-ink); }
@media (max-width: 480px) { .cb-fab span { display: none; } .cb-fab { padding: 1rem; } }

/* ---- εμφάνιση στο scroll ---- */
[data-reveal] { opacity: 0; transform: translateY(26px); transition: opacity .8s ease, transform .8s cubic-bezier(.16,1,.3,1); }
[data-reveal].is-in { opacity: 1; transform: none; }
@media (prefers-reduced-motion: reduce) { [data-reveal] { opacity: 1; transform: none; transition: none; } }

/* ---- διάφορα ---- */
.cb-note { border-left: 3px solid var(--cb-violet); background: rgba(107,70,201,.06);
  padding: 1.25rem 1.5rem; font-weight: 300; line-height: 1.75; color: var(--cb-muted); margin: 2rem 0;
  border-radius: 0 3px 3px 0; }
.cb-note--alert { border-color: var(--cb-ink); background: rgba(19,18,87,.05); }
.cb-note strong { color: var(--cb-ink); font-weight: 500; }
.cb-figure { margin: 0; }
.cb-figure img { width: 100%; display: block; border-radius: 4px; }
.cb-figure figcaption { margin-top: .7rem; font-size: .75rem; color: var(--cb-muted); font-weight: 300; }
/* Η φωτογραφία της υπηρεσίας, πάνω από την περιγραφή της. Δύο σε σειρά μόνο
   όπου η κατηγορία στεγάζει δύο μεθόδους — και μόνο εφόσον υπάρχει πλάτος. */
.cb-figs { display: grid; gap: 1.25rem; margin: 0 0 2.5rem; }
@media (min-width: 700px) { .cb-figs--2 { grid-template-columns: 1fr 1fr; } }
.cb-chips { display: flex; flex-wrap: wrap; gap: .5rem; margin-top: 1.25rem; }
.cb-chip { display: inline-block; padding: .4rem .9rem; border: 1px solid rgba(107,70,201,.3);
  border-radius: 999px; font-size: .72rem; font-weight: 300; color: var(--cb-violet); text-decoration: none;
  transition: all .3s ease; }
.cb-chip:hover { background: var(--cb-violet); color: #fff; border-color: var(--cb-violet); }
.cb-stats { display: grid; grid-template-columns: repeat(2, 1fr); gap: 1.5rem; margin-top: 2.5rem; }
@media (min-width: 900px) { .cb-stats { grid-template-columns: repeat(4, 1fr); } }
.cb-stat b { display: block; font-family: var(--font-serif); font-size: 2.4rem; font-weight: 300;
  color: var(--cb-violet); line-height: 1; }
.cb-stat span { display: block; margin-top: .5rem; font-size: .78rem; font-weight: 300; color: var(--cb-muted); }
.cb-section--dark .cb-stat b { color: var(--cb-lilac); }
.cb-section--dark .cb-stat span { color: rgba(248,247,252,.6); }
.cb-map { border: 0; width: 100%; height: 380px; display: block; filter: grayscale(.35); }

/* ==================== διορθώσεις για κινητά ==================== */

/* Πίνακας ωραρίου: κάθε ώρα αδιάσπαστη, τα διαστήματα αναδιπλώνονται.
   Οι κανόνες nowrap του base.css ακυρώνονται εδώ. */
.cb-hours { table-layout: auto; }
.cb-hours th { white-space: normal; }
.cb-hours__r { display: inline-block; white-space: nowrap; }
.cb-hours__closed { opacity: .65; }
.cb-hours__foot { margin-top: .7rem; font-size: .78rem; font-weight: 300; line-height: 1.6;
  color: var(--cb-muted); }
@media (max-width: 600px) {
  .cb-hours, .cb-hours tbody, .cb-hours tr, .cb-hours th, .cb-hours td { display: block; width: 100%; }
  .cb-hours tr { padding: .5rem 0; border-bottom: 1px solid rgba(19,18,87,.08); }
  .cb-hours tr:last-child { border-bottom: 0; padding-bottom: 0; }
  .cb-hours th { padding: 0 0 .2rem; font-size: .64rem; letter-spacing: .18em;
    text-transform: uppercase; color: var(--cb-violet); }
  .cb-hours td { padding: 0; }
}

/* Κουμπιά: λιγότερο padding και letter-spacing ώστε να χωρούν οι μακριές ετικέτες */
.cb-btn { max-width: 100%; }
@media (max-width: 480px) {
  .cb-btn { padding: .95rem 1.15rem; letter-spacing: .12em; font-size: .66rem; gap: .5rem; }
  .cb-btn--sm { padding: .65rem .9rem; }
}

/* Επικεφαλίδες: το κάτω όριο του clamp ήταν πολύ μεγάλο για οθόνες 360-390px.
   Ο τίτλος της αρχικής είναι πλέον το σλόγκαν — μακρύτερος, άρα πιο μαζεμένος. */
.cb-hero__h1 { font-size: clamp(1.95rem, 6.6vw, 4.1rem); }
.cb-page-hero__h1 { font-size: clamp(1.85rem, 6.4vw, 3.6rem); }
.cb-h2 { font-size: clamp(1.6rem, 4.6vw, 2.9rem); }

/* Στο κινητό η μπάρα κορυφής φεύγει εντελώς: το τηλέφωνο είναι ήδη διαθέσιμο
   από το αιωρούμενο κουμπί κλήσης και από το μενού. */
@media (max-width: 767px) { .cb-topbar { display: none; } }

/* Ενότητα χάρτη: το περιεχόμενο χρειάζεται τα ίδια περιθώρια με τις υπόλοιπες */
.cb-mapsection { padding-inline: 1.5rem; }
@media (min-width: 768px) { .cb-mapsection { padding-inline: 3rem; } }

/* Οι μεγάλες λέξεις («ψυχοθεραπευτικές», «νευροβιολογική») δεν χωρούν σε
   οθόνη 320px και έσπρωχναν τη σελίδα οριζόντια. */
body { overflow-wrap: break-word; }

/* Ερωτήσεις FAQ: ο τίτλος μοιράζεται τη γραμμή με το στρογγυλό κουμπί */
@media (max-width: 520px) {
  .cb-faq { padding-block: 1.4rem; }
  .cb-faq h3 { font-size: 1.15rem; line-height: 1.35; padding-right: .9rem; }
  .cb-faq .w-12 { width: 2.25rem; height: 2.25rem; }
  .cb-faq .w-5 { width: 1rem; height: 1rem; }
}

/* ==================== στρώμα Psychoptia ====================
   Το λογότυπο έχει τρία χρώματα: βαθύ indigo, μωβ και ένα χρυσό σύμβολο
   απείρου. Τα δύο πρώτα κουβαλάει ήδη η παλέτα· το χρυσό μπαίνει εδώ, με
   φειδώ, ως δεύτερος τόνος έμφασης. */

/* Το άπειρο του λογοτύπου ως διακριτικό διαχωριστικό ενοτήτων. */
/* ---- τυπογραφία των άρθρων ----
   Οι ρήσεις μέσα στα κείμενα («Ξέρω τι θέλω…») δεν είναι επικεφαλίδες αλλά
   ούτε απλές παράγραφοι: παίρνουν μεγαλύτερο μέγεθος και μωβ γραμμή. Οι πηγές
   είναι μεν σημαντικές αλλά μακριές, γι' αυτό μπαίνουν σε <details>. */
.cb-prose .cb-quote { font-family: var(--font-serif); font-style: italic; font-weight: 300;
  font-size: clamp(1.15rem, 2.4vw, 1.5rem); line-height: 1.45; color: var(--cb-ink);
  border-left: 2px solid var(--cb-violet); padding-left: 1.1rem; margin: 1.75rem 0; }
.cb-src { margin: 2.5rem 0 0; border-top: 1px solid rgba(19,18,87,.12); padding-top: 1rem; }
.cb-src summary { cursor: pointer; font-size: .68rem; letter-spacing: .16em; text-transform: uppercase;
  color: var(--cb-violet); font-weight: 500; list-style: none; }
.cb-src summary::-webkit-details-marker { display: none; }
.cb-src summary::before { content: "+ "; }
.cb-src[open] summary::before { content: "\2212 "; }
.cb-src ol { margin: 1.1rem 0 0; padding-left: 1.3rem; }
.cb-src li { font-size: .8rem; font-weight: 300; line-height: 1.6; color: var(--cb-muted);
  margin-bottom: .7rem; word-break: break-word; }

/* ---- «τι μπορούμε να δουλέψουμε μαζί»: έξι θεματικές, 3x2 ---- */
.cb-topics { display: grid; gap: 1rem; grid-template-columns: 1fr; margin-top: 2.5rem; }
@media (min-width: 640px) { .cb-topics { grid-template-columns: repeat(2, 1fr); } }
@media (min-width: 1024px) { .cb-topics { grid-template-columns: repeat(3, 1fr); gap: 1.25rem; } }
.cb-topic { background: #fff; border: 1px solid rgba(19,18,87,.09); border-radius: 5px;
  padding: 1.75rem 1.6rem; display: flex; flex-direction: column; gap: .7rem; }
.cb-topic__ic { color: var(--cb-violet); }
.cb-topic__t { font-family: var(--font-serif); font-size: 1.24rem; font-weight: 400; line-height: 1.25;
  color: var(--cb-ink); }
.cb-topic__d { font-size: .89rem; font-weight: 300; line-height: 1.7; color: var(--cb-muted); }

/* ---- «τι προσφέρει / τι δεν καλύπτει» ----
   Δύο στήλες δίπλα-δίπλα ώστε η σύγκριση να διαβάζεται με μια ματιά· σε κινητό
   πέφτουν η μία κάτω από την άλλη και τις ξεχωρίζει το χρώμα της γραμμής. */
.cb-pc { display: grid; gap: 1.75rem; margin: 1.75rem 0 2.25rem; }
@media (min-width: 720px) { .cb-pc { grid-template-columns: 1fr 1fr; gap: 2.25rem; } }
.cb-pc__col { border-top: 2px solid; padding-top: .9rem; }
.cb-pc__col--plus { border-color: var(--cb-violet); }
.cb-pc__col--minus { border-color: rgba(19,18,87,.2); }
.cb-pc h3 { font-family: var(--font-sans); font-size: .66rem; letter-spacing: .2em;
  text-transform: uppercase; font-weight: 500; color: var(--cb-ink); margin: 0 0 .9rem; }
.cb-pc__col--minus h3 { color: var(--cb-muted); }
.cb-pc ul { list-style: none; margin: 0; padding: 0; }
.cb-pc li { position: relative; padding-left: 1.05rem; margin-bottom: .7rem; font-weight: 300;
  font-size: .94rem; line-height: 1.65; color: var(--cb-muted); }
.cb-pc li::before { content: "\2014"; position: absolute; left: 0; color: var(--cb-violet);
  opacity: .55; }
.cb-pc__col--minus li::before { color: var(--cb-muted); opacity: .45; }

/* ---- η ιστορία του ονόματος ----
   Η εικόνα του ηλιοτρόπιου είναι πανοραμική (3:2) και θέλει όλο το πλάτος της
   στήλης· το «credo» των τεσσάρων γραμμών στέκεται μόνο του σε σκούρο φόντο,
   γι' αυτό γράφεται στην ίδια πλάγια γραμματοσειρά με τον τίτλο της αρχικής. */
.cb-figure--wide img { border-radius: 6px; box-shadow: 0 18px 48px rgba(19,18,87,.14); }
.cb-creed { list-style: none; margin: 0 auto; padding: 0; max-width: 46rem; text-align: center;
  display: grid; gap: 1.15rem; }
.cb-creed li { font-family: var(--font-serif); font-style: italic; font-weight: 300;
  font-size: clamp(1.35rem, 3.4vw, 2.15rem); line-height: 1.3; color: rgba(248,247,252,.8); }
.cb-creed li span { color: var(--cb-gold-soft); }
@media (max-width: 640px) { .cb-creed { text-align: left; gap: .9rem; } }

.cb-infinity { display: block; margin: 2.75rem auto; width: 3.5rem; height: auto;
  color: var(--cb-gold); opacity: .9; }
.cb-section--dark .cb-infinity, .cb-page-hero .cb-infinity,
.cb-footer .cb-infinity { color: var(--cb-gold-soft); }

/* Το eyebrow παίρνει χρυσή παύλα αντί για μωβ — ξεχωρίζει από τους συνδέσμους. */
.cb-eyebrow::before { background: var(--cb-gold); }
.cb-eyebrow--light::before { background: var(--cb-gold-soft); }

/* Πορτρέτο της ψυχολόγου: στρογγυλεμένο, με λεπτό χρυσό περίγραμμα. */
.cb-portrait { position: relative; }
.cb-portrait img { width: 100%; height: auto; display: block;
  border-radius: 1.25rem; box-shadow: 0 30px 60px -30px rgba(19,18,87,.55); }
.cb-portrait::after { content: ""; position: absolute; inset: .55rem;
  border: 1px solid rgba(240,180,90,.45); border-radius: 1rem; pointer-events: none; }

/* Οι κάρτες υπηρεσιών παίρνουν χρυσό δείκτη στο hover, όχι μωβ:
   κρατά το μωβ αποκλειστικά για τους συνδέσμους κειμένου. */
.cb-card:hover .cb-card__more { color: var(--cb-gold); }

/* Σημείωση για τις ενεργειακές θεραπείες (Theta Healing / ραδιαισθησία).
   Οπτικά ξεχωριστή από τα υπόλοιπα cb-note, γιατί λέει κάτι διαφορετικό:
   δεν είναι προειδοποίηση κρίσης, είναι οριοθέτηση πλαισίου. */
.cb-note--scope { border-left-color: var(--cb-gold); background: rgba(184,121,31,.07); }
.cb-section--dark .cb-note--scope { background: rgba(240,180,90,.10);
  border-left-color: var(--cb-gold-soft); }

/* Κάρτες άρθρων */
.cb-posts { display: grid; gap: 1.5rem; grid-template-columns: repeat(auto-fit, minmax(19rem, 1fr)); }
.cb-post { display: flex; flex-direction: column; gap: .75rem; padding: 2rem;
  background: #fff; border: 1px solid rgba(19,18,87,.10); border-radius: 1rem;
  text-decoration: none; transition: transform .35s ease, box-shadow .35s ease, border-color .35s ease; }
.cb-post:hover { transform: translateY(-4px); border-color: rgba(107,70,201,.35);
  box-shadow: 0 24px 48px -28px rgba(19,18,87,.45); }
.cb-post__k { font-size: .62rem; letter-spacing: .2em; text-transform: uppercase; color: var(--cb-gold); }
.cb-post__t { font-family: var(--font-serif); font-size: 1.6rem; font-weight: 300;
  line-height: 1.22; color: var(--cb-ink); }
.cb-post__d { font-size: .93rem; line-height: 1.75; color: var(--cb-muted); }
.cb-post__more { margin-top: auto; padding-top: .5rem; font-size: .68rem; letter-spacing: .16em;
  text-transform: uppercase; color: var(--cb-violet); }
"""
