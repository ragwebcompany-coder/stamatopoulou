# -*- coding: utf-8 -*-
"""Κοινά δομικά στοιχεία για τον ιστότοπο Psychoptia — Χριστίνα Σταματοπούλου."""
import json, pathlib, re
import html as _html

BASE = pathlib.Path(
    "/Users/apostolospollalis/Library/CloudStorage/GoogleDrive-apostolos@clinicbrain.gr/"
    "Shared drives/BRAIN GROUP/CLINICBRAIN/CLIENTS FORM/"
    "2026-08-24 · Psychoptia Χριστίνα Σταματοπούλου  · Ψυχολόγος"
)
WEB = BASE / "website"

# ------------------------------------------------------------------ ταυτότητα
SITE_URL    = "https://www.psychoptia.com"
BRAND       = "Psychoptia — Χριστίνα Σταματοπούλου, Κλινική Ψυχολόγος MSc"
BRAND_SHORT = "Psychoptia"
PRACTICE    = "Psychoptia"
NAME        = "Χριστίνα Σταματοπούλου"
NAME_FULL   = "Χριστίνα Σταματοπούλου, MSc"
SPECIALTY   = "Κλινική Ψυχολόγος"
TITLE_LINE  = "Κλινική Ψυχολόγος MSc"
LICENSE     = "1148616"
STREET      = "Εθνάρχου Μακαρίου 25"
CITY        = "Ηλιούπολη"
CITY_GEN    = "Ηλιούπολης"
CITY_ACC    = "Ηλιούπολη"
REGION      = "Αττική"
ZIP         = "16345"
ZIP_PRETTY  = "163 45"

# Δύο τηλέφωνα, κατόπιν οδηγίας: σταθερό ιατρείου + κινητό.
PHONE       = "2192196363"          # σταθερό — κύριο NAP
PHONE_P     = "21 9219 6363"
MOBILE      = "6972487486"          # κινητό
MOBILE_P    = "697 248 7486"

EMAIL       = "stam.christina2020@gmail.com"
EMAIL_ALT   = "Psychoptia@yahoo.gr"
GBP         = "https://www.google.com/maps/search/?api=1&query=Psychoptia+%CE%A7%CF%81%CE%B9%CF%83%CF%84%CE%AF%CE%BD%CE%B1+%CE%A3%CF%84%CE%B1%CE%BC%CE%B1%CF%84%CE%BF%CF%80%CE%BF%CF%8D%CE%BB%CE%BF%CF%85"
MAPS        = GBP
SESSION     = "50"                  # λεπτά ανά συνεδρία
LAT, LON    = "37.9310", "23.7580"  # Ηλιούπολη — να μπει το ακριβές στίγμα του γραφείου

# Περιοχές για τοπικό SEO — νότια / νοτιοανατολικά προάστια
AREAS = ["Ηλιούπολη", "Αργυρούπολη", "Άλιμος", "Γλυφάδα", "Βύρωνας", "Δάφνη",
         "Υμηττός", "Άγιος Δημήτριος", "Ελληνικό", "Νέα Σμύρνη", "Καισαριανή",
         "Νότια Προάστια"]

# Ονόματα στατικών αρχείων με αποτύπωμα περιεχομένου (συμπληρώνονται στο build).
ASSETS = {"css": "site.css", "js": "site.js"}

# ------------------------------------------------------------------ πλοήγηση
NAV = [
    ("Αρχική",       "index.html"),
    ("Βιογραφικό",   "viografiko.html"),
    ("Προσεγγίσεις", "proseggiseis.html"),
    ("Υπηρεσίες",    "ypiresies.html"),
    ("Άρθρα",        "arthra.html"),
    ("Επικοινωνία",  "epikoinonia.html"),
]

SERVICES = [
    dict(slug="ypiresies/psychotherapeia-paidion.html",
         nav="Ψυχοθεραπεία Παιδιών",
         who="Παιδιά",
         short="Ψυχοθεραπεία Παιδιών",
         teaser="Το παιδί εκφράζεται μέσα από το παιχνίδι και τη δημιουργία, πριν βρει τις λέξεις. Η θεραπεία ακολουθεί αυτόν τον δρόμο, μαζί με τους γονείς.",
         icon="child"),
    dict(slug="ypiresies/psychotherapeia-efivon.html",
         nav="Ψυχοθεραπεία Εφήβων",
         who="Έφηβοι",
         short="Ψυχοθεραπεία Εφήβων",
         teaser="Ένας χώρος δικός του, όπου ο έφηβος μιλά χωρίς να αξιολογείται — για την ταυτότητα, τις σχέσεις, το άγχος και την εικόνα του εαυτού.",
         icon="spark"),
    dict(slug="ypiresies/psychotherapeia-enilikon.html",
         nav="Ψυχοθεραπεία Ενηλίκων",
         who="Ενήλικες",
         short="Ψυχοθεραπεία Ενηλίκων",
         teaser="Ατομικές συνεδρίες για άγχος, πανικό, διάθεση, εξουθένωση, σχέσεις και ταυτότητα — με κλινική αξιολόγηση και στόχους που ορίζουμε μαζί.",
         icon="person"),
    dict(slug="ypiresies/symvouleftiki-goneon.html",
         nav="Συμβουλευτική Γονέων",
         who="Γονείς",
         short="Συμβουλευτική Γονέων",
         teaser="Όταν αλλάζει το πλαίσιο γύρω από το παιδί, αλλάζει και η δυσκολία. Όρια, επικοινωνία και σχέση γονέα–παιδιού.",
         icon="hands"),
    dict(slug="ypiresies/paigniotherapeia-dimiourgikes-technes.html",
         nav="Παιγνιοθεραπεία &amp; Δημιουργικές Τέχνες",
         who="Παιδιά &amp; έφηβοι",
         short="Παιγνιοθεραπεία &amp; Δημιουργικές&nbsp;Τέχνες",
         teaser="Παιχνίδι, ζωγραφική, αφήγηση και δραματοποίηση ως θεραπευτικά εργαλεία — εκεί όπου ο λόγος από μόνος του δεν φτάνει.",
         icon="palette"),
    dict(slug="ypiresies/enallaktikes-methodoi.html",
         nav="Theta Healing &amp; Ραδιαισθησία",
         who="Συμπληρωματικά",
         short="Theta&nbsp;Healing &amp; Θεραπευτική Ραδιαισθησία",
         teaser="Συμπληρωματικές μέθοδοι χαλάρωσης και ενεργειακής εργασίας, σε ξεχωριστό πλαίσιο από την ψυχοθεραπεία και πάντα κατόπιν συζήτησης.",
         icon="infinity"),
]

ICONS = {
 "person": '<circle cx="12" cy="7.5" r="3.5"/><path d="M4.5 21a7.5 7.5 0 0 1 15 0"/>',
 "spark": '<path d="M12 2.5 13.9 8l5.6 1.9-5.6 1.9L12 17.4 10.1 11.8 4.5 9.9 10.1 8z"/><path d="M18.5 15.5 19.3 18l2.2.8-2.2.8-.8 2.4-.8-2.4-2.2-.8 2.2-.8z"/>',
 "child": '<circle cx="12" cy="5.5" r="2.6"/><path d="M12 8.1v6.4"/><path d="M8 10.6h8"/><path d="m9.5 21 2.5-6.5L14.5 21"/>',
 "palette": '<path d="M12 3a9 9 0 1 0 0 18c1 0 1.6-.7 1.6-1.5 0-.5-.2-.8-.5-1.1-.3-.3-.5-.7-.5-1.1 0-.9.7-1.6 1.6-1.6H16a5 5 0 0 0 5-5c0-4.1-4-7.7-9-7.7z"/><circle cx="7.7" cy="11.2" r="1.1"/><circle cx="10.4" cy="7.2" r="1.1"/><circle cx="15.2" cy="7.8" r="1.1"/>',
 "infinity": '<path d="M6.6 8.6c1.9 0 3 1.4 5.4 3.4s3.5 3.4 5.4 3.4a3.4 3.4 0 0 0 0-6.8c-1.9 0-3 1.4-5.4 3.4s-3.5 3.4-5.4 3.4a3.4 3.4 0 0 1 0-6.8z"/>',
 "family": '<circle cx="7.5" cy="7" r="2.6"/><circle cx="16.5" cy="7" r="2.6"/><path d="M2.8 20a4.7 4.7 0 0 1 9.4 0"/><path d="M11.8 20a4.7 4.7 0 0 1 9.4 0"/>',
 "link": '<path d="M9.5 14.5 14.5 9.5"/><path d="M11 6.5 12.8 4.7a4 4 0 0 1 5.7 5.7l-1.9 1.8"/><path d="M13 17.5l-1.8 1.8a4 4 0 0 1-5.7-5.7l1.9-1.8"/>',
 "hands": '<path d="M12 21s-7-4.2-7-9.2A3.8 3.8 0 0 1 12 9.4a3.8 3.8 0 0 1 7 2.4c0 5-7 9.2-7 9.2z"/><path d="M12 9.4V3"/>',
 "group": '<circle cx="12" cy="6" r="2.4"/><circle cx="5" cy="10" r="2.2"/><circle cx="19" cy="10" r="2.2"/><path d="M8.2 15.5a4.2 4.2 0 0 1 7.6 0"/><path d="M2 18.5a3.6 3.6 0 0 1 5.2-2.6"/><path d="M22 18.5a3.6 3.6 0 0 0-5.2-2.6"/>',
 "flower": '<circle cx="12" cy="12" r="2.6"/><path d="M12 9.4C12 6.6 12.9 3 12 3s-.1 3.6 0 6.4"/><path d="M14.6 12c2.8 0 6.4.9 6.4 0s-3.6-.1-6.4 0"/><path d="M12 14.6c0 2.8-.9 6.4 0 6.4s.1-3.6 0-6.4"/><path d="M9.4 12c-2.8 0-6.4-.9-6.4 0s3.6.1 6.4 0"/><path d="m13.8 10.2 3.9-3.9M13.8 13.8l3.9 3.9M10.2 13.8l-3.9 3.9M10.2 10.2 6.3 6.3"/>',
 "brain": '<path d="M9.5 3.5A2.8 2.8 0 0 0 6.8 6a2.6 2.6 0 0 0-2 4.3A2.7 2.7 0 0 0 5.2 15a2.8 2.8 0 0 0 2 4 2.7 2.7 0 0 0 4.8-1.6V5.9a2.5 2.5 0 0 0-2.5-2.4z"/><path d="M14.5 3.5A2.8 2.8 0 0 1 17.2 6a2.6 2.6 0 0 1 2 4.3 2.7 2.7 0 0 1-.4 4.7 2.8 2.8 0 0 1-2 4 2.7 2.7 0 0 1-4.8-1.6V5.9a2.5 2.5 0 0 1 2.5-2.4z"/>',
 "chat": '<path d="M21 12a8 8 0 0 1-8 8H4l2-3.2A8 8 0 1 1 21 12z"/><path d="M9 11h6M9 14.5h3.5"/>',
 "shield": '<path d="M20 13c0 5-3.5 7.5-7.66 8.95a1 1 0 0 1-.67-.01C7.5 20.5 4 18 4 13V6a1 1 0 0 1 1-1c2 0 4.5-1.2 6.24-2.72a1.17 1.17 0 0 1 1.52 0C14.51 3.81 17 5 19 5a1 1 0 0 1 1 1z"/><path d="m9 12 2 2 4-4"/>',
 "grad": '<path d="M22 10v6M2 10l10-5 10 5-10 5z"/><path d="M6 12v5c3 3 9 3 12 0v-5"/>',
 "book": '<path d="M4 19.5A2.5 2.5 0 0 1 6.5 17H20"/><path d="M6.5 2H20v20H6.5A2.5 2.5 0 0 1 4 19.5v-15A2.5 2.5 0 0 1 6.5 2z"/>',
 "monitor": '<rect x="2.5" y="4" width="19" height="13" rx="2"/><path d="M9 21h6M12 17v4"/>',
 "phone": '<path d="M22 16.92v3a2 2 0 0 1-2.18 2 19.79 19.79 0 0 1-8.63-3.07 19.5 19.5 0 0 1-6-6 19.79 19.79 0 0 1-3.07-8.67A2 2 0 0 1 4.11 2h3a2 2 0 0 1 2 1.72c.13.96.36 1.9.7 2.81a2 2 0 0 1-.45 2.11L8.09 9.91a16 16 0 0 0 6 6l1.27-1.27a2 2 0 0 1 2.11-.45c.9.34 1.85.57 2.81.7A2 2 0 0 1 22 16.92z"/>',
 "pin": '<path d="M20 10c0 6-8 12-8 12s-8-6-8-12a8 8 0 0 1 16 0z"/><circle cx="12" cy="10" r="3"/>',
 "clock": '<circle cx="12" cy="12" r="10"/><path d="M12 6v6l4 2"/>',
 "mail": '<rect x="2" y="4" width="20" height="16" rx="2"/><path d="m2 7 10 6 10-6"/>',
 "chev": '<path d="m6 9 6 6 6-6"/>',
 "calendar": '<rect x="3" y="4" width="18" height="18" rx="2"/><path d="M16 2v4M8 2v4M3 10h18"/><path d="m9 16 2 2 4-4"/>',
}


def icon(name, cls="w-6 h-6", sw="1.7"):
    # τα width/height μένουν ως ασφαλές fallback, ώστε το εικονίδιο να μη
    # «σκάει» στα 300×150 αν λείψει ποτέ ο κανόνας μεγέθους από το CSS
    return ('<svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" '
            'fill="none" stroke="currentColor" stroke-width="%s" stroke-linecap="round" '
            'stroke-linejoin="round" class="%s" aria-hidden="true">%s</svg>' % (sw, cls, ICONS[name]))


def rel(depth):
    return "../" * depth


def plain(s):
    """Καθαρό κείμενο για JSON-LD: οι HTML οντότητες (&amp;, &nbsp;) δεν έχουν
    θέση σε structured data — η Google τις διαβάζει κυριολεκτικά."""
    return _html.unescape(s).replace(" ", " ").strip()


# ------------------------------------------------------------------ JSON-LD
def practice_ld():
    """Το γραφείο ως ProfessionalService — όχι MedicalClinic / Physician:
    η κλινική ψυχολόγος δεν είναι ιατρός και δεν παρέχει ιατρικές πράξεις.

    Δεν δηλώνεται openingHoursSpecification: το ωράριο αλλάζει ανά ημέρα και
    η πελάτισσα ζήτησε ρητά να μην αναγράφεται. Καλύτερα καθόλου δήλωση παρά
    λανθασμένη — η Google εμφανίζει το ωράριο αυτούσιο στα αποτελέσματα."""
    return {
        "@type": ["ProfessionalService", "LocalBusiness"],
        "@id": SITE_URL + "/#grafeio",
        "name": BRAND,
        "alternateName": ["Psychoptia", "Ψυχολόγος Ηλιούπολη – Χριστίνα Σταματοπούλου"],
        "url": SITE_URL + "/",
        "image": SITE_URL + "/assets/img/og-image.jpg",
        "logo": SITE_URL + "/assets/img/logo.png",
        "description": ("Κλινική ψυχολόγος στην Ηλιούπολη. Ψυχοθεραπεία παιδιών, εφήβων και ενηλίκων, "
                        "συμβουλευτική γονέων, παιγνιοθεραπεία και δημιουργικές τέχνες. "
                        "Συνεδρίες διά ζώσης και διαδικτυακά."),
        "priceRange": "€€",
        "currenciesAccepted": "EUR",
        "address": {
            "@type": "PostalAddress",
            "streetAddress": STREET,
            "addressLocality": CITY,
            "addressRegion": REGION,
            "postalCode": ZIP,
            "addressCountry": "GR",
        },
        "geo": {"@type": "GeoCoordinates", "latitude": LAT, "longitude": LON},
        "hasMap": MAPS,
        "telephone": "+30" + PHONE,
        "email": EMAIL,
        "sameAs": [GBP],
        "areaServed": [{"@type": "City", "name": a} for a in AREAS[:-1]],
        "availableLanguage": [{"@type": "Language", "name": "Ελληνικά"},
                              {"@type": "Language", "name": "Αγγλικά"}],
        "hasOfferCatalog": {
            "@type": "OfferCatalog",
            "name": "Υπηρεσίες ψυχοθεραπείας και συμβουλευτικής",
            "itemListElement": [
                {"@type": "Offer", "itemOffered": {"@type": "Service",
                 "name": plain(s["short"]), "url": SITE_URL + "/" + s["slug"]}}
                for s in SERVICES
            ],
        },
        "founder": {"@id": SITE_URL + "/viografiko.html#psychologos"},
        "employee": {"@id": SITE_URL + "/viografiko.html#psychologos"},
    }


def person_ld():
    return {
        "@type": "Person",
        "@id": SITE_URL + "/viografiko.html#psychologos",
        "name": NAME,
        "givenName": "Χριστίνα",
        "familyName": "Σταματοπούλου",
        "jobTitle": "Κλινική Ψυχολόγος, MSc",
        "url": SITE_URL + "/viografiko.html",
        "image": SITE_URL + "/assets/img/christina-stamatopoulou.jpg",
        "worksFor": {"@id": SITE_URL + "/#grafeio"},
        "knowsLanguage": ["el", "en"],
        "memberOf": {"@type": "Organization", "name": "Σύλλογος Ελλήνων Ψυχολόγων"},
        "hasCredential": [
            {"@type": "EducationalOccupationalCredential",
             "credentialCategory": "Άδεια ασκήσεως επαγγέλματος Ψυχολόγου",
             "identifier": LICENSE},
            {"@type": "EducationalOccupationalCredential",
             "credentialCategory": "MSc Clinical & Community Psychology"},
            {"@type": "EducationalOccupationalCredential",
             "credentialCategory": "BSc Applied Psychology"},
        ],
        "alumniOf": [
            {"@type": "CollegeOrUniversity", "name": "University of East London"},
            {"@type": "CollegeOrUniversity", "name": "University of Derby"},
        ],
        "knowsAbout": ["Κλινική ψυχολογία", "Γνωσιακή–συμπεριφορική ψυχοθεραπεία",
                       "Συστημική και οικογενειακή θεραπεία", "Παιγνιοθεραπεία",
                       "Θεραπεία μέσω τέχνης", "Συμβουλευτική γονέων",
                       "Αγχώδεις διαταραχές", "Διαταραχές πρόσληψης τροφής"],
    }


def website_ld():
    return {
        "@type": "WebSite",
        "@id": SITE_URL + "/#website",
        "url": SITE_URL + "/",
        "name": BRAND,
        "alternateName": PRACTICE,
        "inLanguage": "el-GR",
        "publisher": {"@id": SITE_URL + "/#grafeio"},
    }


def breadcrumb_ld(trail):
    """trail: [(name, href_absolute), ...]"""
    return {
        "@type": "BreadcrumbList",
        "itemListElement": [
            {"@type": "ListItem", "position": i + 1, "name": n, "item": u}
            for i, (n, u) in enumerate(trail)
        ],
    }


def faq_ld(pairs):
    return {
        "@type": "FAQPage",
        "mainEntity": [
            {"@type": "Question", "name": q,
             "acceptedAnswer": {"@type": "Answer", "text": re.sub(r"<[^>]+>", "", a)}}
            for q, a in pairs
        ],
    }


# ------------------------------------------------------------------ κοινά μπλοκ
def faq_block(pairs):
    out = []
    for q, a in pairs:
        out.append(
            '<div class="cb-faq border-b border-ink/10 py-8">'
            '<button class="w-full flex justify-between items-center text-left focus:outline-none group">'
            '<h3 class="font-serif text-2xl md:text-3xl text-ink group-hover:text-violet transition-colors pr-8">'
            + q + '</h3>'
            '<div class="w-12 h-12 rounded-full border border-ink/20 flex items-center justify-center '
            'group-hover:border-violet transition-colors shrink-0">'
            + icon("chev", "w-5 h-5 text-ink group-hover:text-violet transition-transform duration-500", "2") +
            '</div></button>'
            '<div class="faq-answer"><div class="cb-prose">' + a + '</div></div></div>'
        )
    return "\n".join(out)


def hours_note():
    """Η πελάτισσα ζήτησε ρητά να ΜΗΝ αναγράφεται ωράριο ανά ημέρα, γιατί
    αλλάζει. Στη θέση του πίνακα ωραρίου μπαίνει καθαρή διατύπωση ραντεβού."""
    return ('<p class="cb-hours__foot">Οι συνεδρίες γίνονται <strong>αποκλειστικά κατόπιν ραντεβού</strong>. '
            'Το ωράριο διαμορφώνεται ανά ημέρα — καλέστε για να βρούμε μαζί την ώρα που σας εξυπηρετεί.</p>')


def contact_card(depth):
    r = rel(depth)
    return f"""<div class="cb-contact-card">
<div class="cb-contact-card__row">{icon('pin', 'w-5 h-5 cb-violet shrink-0')}
<div><span class="cb-contact-card__k">Διεύθυνση</span>
<a href="{MAPS}" target="_blank" rel="noopener noreferrer">{STREET}, {ZIP_PRETTY} {CITY}</a></div></div>
<div class="cb-contact-card__row">{icon('phone', 'w-5 h-5 cb-violet shrink-0')}
<div><span class="cb-contact-card__k">Τηλέφωνα</span>
<a href="tel:+30{PHONE}">{PHONE_P}</a><br><a href="tel:+30{MOBILE}">{MOBILE_P}</a></div></div>
<div class="cb-contact-card__row">{icon('mail', 'w-5 h-5 cb-violet shrink-0')}
<div><span class="cb-contact-card__k">Email</span>
<a href="mailto:{EMAIL}">{EMAIL}</a></div></div>
<div class="cb-contact-card__row">{icon('clock', 'w-5 h-5 cb-violet shrink-0')}
<div><span class="cb-contact-card__k">Ραντεβού</span>
{hours_note()}</div></div>
</div>"""


def online_note():
    """Οι διαδικτυακές συνεδρίες είναι το πρακτικό διαφοροποιητικό στοιχείο."""
    return (f'<div class="cb-access">{icon("monitor", "cb-access__ic")}'
            f'<div><strong>Διά ζώσης ή διαδικτυακά</strong>'
            f'<span>Στο γραφείο στην {CITY} ή online, με τον ίδιο τρόπο εργασίας και την ίδια διάρκεια.</span></div></div>')


def crisis_note():
    return ('<div class="cb-note cb-note--alert"><strong>Σε κρίση;</strong> Η ψυχοθεραπεία δεν είναι υπηρεσία '
            'επείγουσας ανάγκης. Αν σκέφτεστε να βλάψετε τον εαυτό σας ή κάποιον άλλο, μην περιμένετε ραντεβού: '
            'καλέστε τη <a href="tel:1018">1018</a> (Γραμμή Παρέμβασης για την Αυτοκτονία, 24/7), '
            'το <a href="tel:10306">10306</a> (Γραμμή Ψυχολογικής Υποστήριξης) ή το '
            '<a href="tel:112">112</a>.</div>')


def booking_block(depth):
    """Η πελάτισσα ζήτησε ρητά «δε θέλω ατζέντα, ας με καλούν». Δεν υπάρχει
    ημερολόγιο κρατήσεων ούτε φόρμα: το τηλέφωνο είναι το κύριο κανάλι."""
    r = rel(depth)
    return f"""<div class="cb-booking">
<div class="cb-booking__ph">
{icon('phone', 'cb-booking__ic')}
<p class="cb-booking__t">Το ραντεβού κλείνεται τηλεφωνικά</p>
<p class="cb-booking__d">Δεν υπάρχει ηλεκτρονική ατζέντα — και είναι σκόπιμο. Μια σύντομη τηλεφωνική
συνομιλία αρκεί για να δούμε τι σας απασχολεί, ποιο πλαίσιο ταιριάζει και πότε μπορούμε να ξεκινήσουμε.</p>
<div class="cb-booking__actions">
<a class="cb-btn" href="tel:+30{PHONE}">{icon('phone','w-4 h-4')}<span>{PHONE_P}</span></a>
<a class="cb-btn cb-btn--ghost" href="tel:+30{MOBILE}">{icon('phone','w-4 h-4')}<span>{MOBILE_P}</span></a>
</div>
<p class="cb-booking__d cb-booking__d--em">Ή γράψτε μου και θα επικοινωνήσω μαζί σας:</p>
<div class="cb-booking__actions">
<a class="cb-btn cb-btn--ghost" href="mailto:{EMAIL}">{icon('mail','w-4 h-4')}<span>EMAIL</span></a>
</div>
</div>
<p class="cb-booking__note">Η συνεδρία διαρκεί {SESSION} λεπτά. Αν βρίσκεστε σε κρίση ή σκέφτεστε να βλάψετε τον εαυτό σας,
μην περιμένετε ραντεβού: καλέστε τη <a href="tel:1018">1018</a> (Γραμμή Παρέμβασης για την Αυτοκτονία, 24/7)
ή το <a href="tel:112">112</a>.</p>
</div>"""
