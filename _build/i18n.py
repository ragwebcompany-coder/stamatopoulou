# -*- coding: utf-8 -*-
"""Οι δύο γλώσσες του ιστότοπου.

Ο ιστότοπος παράγεται δύο φορές — μία στα ελληνικά στη ρίζα και μία στα αγγλικά
κάτω από το /en/. Η δομή και το CSS είναι κοινά· εδώ ζουν μόνο τα κείμενα του
«σκελετού» (μενού, footer, κάρτα επικοινωνίας, φόρμα) που εμφανίζονται σε κάθε
σελίδα. Τα κείμενα των ίδιων των σελίδων ζουν στο gen_pages.py / content_en.py.

Η τρέχουσα γλώσσα κρατιέται σε module-level μεταβλητή αντί να περνά ως όρισμα
παντού: οι συναρτήσεις παραγωγής HTML είναι δεκάδες και φωλιασμένες, οπότε ένα
επιπλέον όρισμα σε κάθε μία θα ήταν θόρυβος. Το build αλλάζει γλώσσα μία φορά
ανά πέρασμα με το set_lang().
"""

LANG = "el"


def set_lang(code):
    global LANG
    assert code in ("el", "en"), code
    LANG = code


def T(key):
    """Το κείμενο του κλειδιού στην τρέχουσα γλώσσα."""
    try:
        return STRINGS[key][LANG]
    except KeyError:
        raise KeyError("λείπει μετάφραση: %s / %s" % (key, LANG)) from None


# Κάθε καταχώριση: κλειδί -> {"el": ..., "en": ...}
STRINGS = {
 # ---- πλοήγηση & σκελετός ----
 "skip":            {"el": "Μετάβαση στο περιεχόμενο", "en": "Skip to content"},
 "nav.main":        {"el": "Κύρια πλοήγηση", "en": "Main navigation"},
 "nav.mobile":      {"el": "Πλοήγηση κινητού", "en": "Mobile navigation"},
 "nav.open":        {"el": "Άνοιγμα μενού", "en": "Open menu"},
 "nav.close":       {"el": "Κλείσιμο μενού", "en": "Close menu"},
 "nav.home":        {"el": "Αρχική", "en": "Home"},
 "nav.bio":         {"el": "Βιογραφικό", "en": "About"},
 "nav.services":    {"el": "Υπηρεσίες", "en": "Services"},
 "nav.articles":    {"el": "Άρθρα", "en": "Articles"},
 "nav.contact":     {"el": "Επικοινωνία", "en": "Contact"},
 "nav.allservices": {"el": "Όλες οι υπηρεσίες", "en": "All services"},
 "nav.overview":   {"el": "ΟΛΗ Η ΚΑΤΗΓΟΡΙΑ", "en": "CATEGORY OVERVIEW"},
 "cta.book":        {"el": "ΡΑΝΤΕΒΟΥ", "en": "BOOK"},
 "cta.bookLong":    {"el": "ΚΛΕΙΣΤΕ ΡΑΝΤΕΒΟΥ", "en": "BOOK AN APPOINTMENT"},
 "cta.contact":     {"el": "ΕΠΙΚΟΙΝΩΝΙΑ", "en": "GET IN TOUCH"},
 "cta.more":        {"el": "Περισσότερα", "en": "Read more"},
 "cta.call":        {"el": "Καλέστε μας", "en": "Call us"},
 "cta.callAria":    {"el": "Καλέστε στο", "en": "Call"},
 "lang.switch":     {"el": "EN", "en": "ΕΛ"},
 "lang.switchAria": {"el": "Read this site in English", "en": "Διαβάστε το site στα ελληνικά"},
 "home.link":       {"el": "αρχική", "en": "home"},

 # ---- λωρίδα κλήσης προς δράση ----
 "band.title": {"el": "Ας κάνουμε το πρώτο βήμα", "en": "Let's take the first step"},
 "band.lede":  {"el": "Μια πρώτη συνάντηση γνωριμίας {s} λεπτών — στο γραφείο στην {c} ή διαδικτυακά. "
                      "Το ραντεβού κλείνεται με ένα τηλεφώνημα.",
                "en": "A first {s}-minute introductory session — at the practice in {c} or online. "
                      "One phone call is all it takes."},

 # ---- κάρτα επικοινωνίας ----
 "cc.address":   {"el": "Διεύθυνση", "en": "Address"},
 "cc.phone":     {"el": "Τηλέφωνο", "en": "Phone"},
 "cc.email":     {"el": "Email", "en": "Email"},
 "cc.booking":   {"el": "Ραντεβού", "en": "Appointments"},
 "cc.follow":    {"el": "Ακολουθήστε", "en": "Follow"},
 "cc.hours":     {"el": 'Οι συνεδρίες γίνονται <strong>αποκλειστικά κατόπιν ραντεβού</strong>. '
                        'Το ωράριο διαμορφώνεται ανά ημέρα — καλέστε για να βρούμε μαζί την ώρα που σας εξυπηρετεί.',
                  "en": 'Sessions are <strong>by appointment only</strong>. Hours are arranged day by day — '
                        'call and we will find a time that works for you.'},
 "cc.byAppt":    {"el": "Κατόπιν ραντεβού", "en": "By appointment"},

 # ---- διά ζώσης / διαδικτυακά ----
 "online.t": {"el": "Διά ζώσης ή διαδικτυακά", "en": "In person or online"},
 "online.d": {"el": "Στο γραφείο στην {c} — εξυπηρετώντας όλη την Αττική — ή online από οπουδήποτε "
                    "στον κόσμο, με τον ίδιο τρόπο εργασίας και την ίδια διάρκεια. "
                    "Οι συνεδρίες γίνονται στα ελληνικά και στα αγγλικά.",
              "en": "At the practice in {c} — serving all of Attica — or online from anywhere in the "
                    "world, with the same way of working and the same duration. "
                    "Sessions are held in Greek and in English."},

 # ---- σημείωμα κρίσης ----
 "crisis": {"el": '<strong>Σε κρίση;</strong> Η ψυχοθεραπεία δεν είναι υπηρεσία επείγουσας ανάγκης. '
                  'Αν σκέφτεστε να βλάψετε τον εαυτό σας ή κάποιον άλλο, μην περιμένετε ραντεβού: '
                  'καλέστε τη <a href="tel:1018">1018</a> (Γραμμή Παρέμβασης για την Αυτοκτονία, 24/7), '
                  'το <a href="tel:10306">10306</a> (Γραμμή Ψυχολογικής Υποστήριξης) ή το '
                  '<a href="tel:112">112</a>.',
            "en": '<strong>In crisis?</strong> Psychotherapy is not an emergency service. If you are '
                  'thinking of harming yourself or someone else, do not wait for an appointment: call '
                  '<a href="tel:1018">1018</a> (Suicide Intervention Line, 24/7), '
                  '<a href="tel:10306">10306</a> (Psychological Support Line) or '
                  '<a href="tel:112">112</a>.'},

 # ---- φόρμα ----
 "form.lede":     {"el": "Η πρώτη μας επαφή μπορεί να ξεκινήσει από εδώ — επικοινωνήστε μαζί μου για "
                         "πληροφορίες ή για να προγραμματίσουμε μία συνάντηση.",
                   "en": "Our first contact can start right here — write to me for information or to "
                         "arrange a first session."},
 "form.name":     {"el": "Ονοματεπώνυμο", "en": "Full name"},
 "form.email":    {"el": "Email", "en": "Email"},
 "form.phone":    {"el": "Τηλέφωνο", "en": "Phone"},
 "form.optional": {"el": "προαιρετικό", "en": "optional"},
 "form.message":  {"el": "Το μήνυμά σας", "en": "Your message"},
 "form.ph":       {"el": "Γράψτε με δυο λόγια τι σας φέρνει εδώ — δεν χρειάζονται λεπτομέρειες.",
                   "en": "In a line or two, what brings you here — no details needed."},
 "form.consent":  {"el": 'Συμφωνώ να χρησιμοποιηθούν τα στοιχεία μου αποκλειστικά για να απαντηθεί '
                         'αυτό το μήνυμα, σύμφωνα με την <a href="{u}">Πολιτική Απορρήτου</a>.',
                   "en": 'I agree that my details will be used solely to answer this message, in '
                         'accordance with the <a href="{u}">Privacy Policy</a>.'},
 "form.send":     {"el": "ΑΠΟΣΤΟΛΗ", "en": "SEND"},
 "form.note":     {"el": 'Η φόρμα δεν είναι κανάλι επείγουσας ανάγκης και δεν αντικαθιστά ραντεβού. '
                         'Αν προτιμάτε, καλέστε στο <a href="tel:+30{p}">{pp}</a>.',
                   "en": 'This form is not an emergency channel and does not replace an appointment. '
                         'If you prefer, call <a href="tel:+30{p}">{pp}</a>.'},
 "form.subject":  {"el": "Μήνυμα από το psychoptia.com", "en": "Message from psychoptia.com"},

 # ---- περιοχές ----
 "areas.inPerson": {"el": "Διά ζώσης — όλη η Αττική", "en": "In person — all of Attica"},
 "areas.near":     {"el": "Το γραφείο βρίσκεται στην {c}. Πλησιέστερες περιοχές:",
                    "en": "The practice is in {c}. Nearest areas:"},
 "areas.wider":    {"el": "Εξυπηρετούνται εξίσου και οι υπόλοιπες περιοχές της Αττικής:",
                    "en": "All other areas of Attica are served equally:"},
 "areas.online":   {"el": "Διαδικτυακά — από οπουδήποτε", "en": "Online — from anywhere"},
 "areas.onlineD":  {"el": "Οι online συνεδρίες γίνονται σε όλη την Ελλάδα και στο εξωτερικό, με τον ίδιο "
                          "τρόπο εργασίας και την ίδια διάρκεια — συχνά για Έλληνες της διασποράς: {k} "
                          "και αλλού. <strong>Οι συνεδρίες μπορούν να γίνουν και στα αγγλικά.</strong>",
                    "en": "Online sessions are held across Greece and abroad, with the same way of working "
                          "and the same duration — often for Greeks living overseas: {k} and elsewhere. "
                          "<strong>Sessions can be held in English.</strong>"},

 # ---- footer ----
 "foot.nav":     {"el": "Πλοήγηση", "en": "Navigation"},
 "foot.hours":   {"el": "Συνεδρίες αποκλειστικά κατόπιν ραντεβού.<br>Διά ζώσης ή διαδικτυακά.",
                  "en": "Sessions by appointment only.<br>In person or online."},
 "foot.areas":   {"el": "<strong>Διά ζώσης σε όλη την Αττική:</strong> {a}. "
                        "<strong>Διαδικτυακά:</strong> σε όλη την Ελλάδα και το εξωτερικό — συνεδρίες και στα αγγλικά.",
                  "en": "<strong>In person across Attica:</strong> {a}. "
                        "<strong>Online:</strong> across Greece and abroad — sessions also in English."},
 "foot.rights":  {"el": "Με την επιφύλαξη παντός δικαιώματος.", "en": "All rights reserved."},
 "foot.privacy": {"el": "Πολιτική Απορρήτου", "en": "Privacy Policy"},
 "foot.terms":   {"el": "Όροι Χρήσης", "en": "Terms of Use"},
 "foot.sitemap": {"el": "Χάρτης ιστότοπου", "en": "Sitemap"},
 "foot.madeby":  {"el": "Made by", "en": "Made by"},
 "foot.tag":     {"el": "Ψυχοθεραπεία παιδιών, εφήβων και ενηλίκων, συμβουλευτική γονέων και "
                        "παιγνιοθεραπεία, στην {c} ή διαδικτυακά.",
                  "en": "Psychotherapy for children, teenagers and adults, parent counselling and "
                        "play therapy, in {c} or online."},
 "foot.localpage": {"el": "Ψυχολόγος {c}", "en": "Psychologist in {c}"},
 "foot.sign":    {"el": "Κλινική Ψυχολόγος MSc · αρ. αδείας {l} · μέλος του Συλλόγου Ελλήνων Ψυχολόγων.",
                  "en": "Clinical Psychologist MSc · licence no. {l} · member of the Association of "
                        "Greek Psychologists."},
 "nav.faq":      {"el": "Συχνές Ερωτήσεις", "en": "FAQ"},

 # ---- κοινές επικεφαλίδες σελίδων υπηρεσίας ----
 "sp.glance":   {"el": "Με μια ματιά", "en": "At a glance"},
 "sp.faq":      {"el": "Συχνές ερωτήσεις", "en": "Frequently asked questions"},
 "sp.other":    {"el": "Άλλες υπηρεσίες", "en": "Other services"},
 "sp.serviceType": {"el": "Ψυχοθεραπεία / Συμβουλευτική", "en": "Psychotherapy / Counselling"},
 "crumbs.aria": {"el": "Διαδρομή", "en": "Breadcrumb"},
 "lang.code":   {"el": "el-GR", "en": "en-GB"},
}
