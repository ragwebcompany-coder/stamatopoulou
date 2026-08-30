# -*- coding: utf-8 -*-
"""Κοινά δομικά στοιχεία για τον ιστότοπο Psychoptia — Χριστίνα Σταματοπούλου."""
import json, pathlib, re
import html as _html
from i18n import T, set_lang, STRINGS
import i18n

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
# Το σλόγκαν της πελάτισσας. Εμφανίζεται στο hero της αρχικής και κάτω από το
# λογότυπο στο footer, ώστε να συνοδεύει το σήμα σε κάθε σελίδα.
SLOGAN_I18N = {"el": "Όταν το φως συναντά την κατανόηση, γεννιέται η σύνδεση",
               "en": "Where light meets understanding, connection is born"}


def slogan():
    return SLOGAN_I18N[i18n.LANG]


# Η ταυτότητα του γραφείου σε δύο γραφές. Δίνονται ως συναρτήσεις γιατί τις
# διαβάζουν κοινές συναρτήσεις (header, footer, κάρτα επικοινωνίας) που
# τρέχουν και στα δύο περάσματα του build.
def _pick(el, en):
    return el if i18n.LANG == "el" else en


def city():      return _pick(CITY, CITY_EN)
def region():    return _pick(REGION, REGION_EN)
def street():    return _pick(STREET, STREET_EN)
def pname():     return _pick(NAME, NAME_EN)
def specialty(): return _pick(SPECIALTY, "Clinical Psychologist")
def brand():     return _pick(BRAND, "Psychoptia — Christina Stamatopoulou, Clinical Psychologist MSc")
TITLE_LINE  = "Κλινική Ψυχολόγος MSc"
LICENSE     = "1148616"
STREET      = "Εθνάρχου Μακαρίου 25"
# Λατινική γραφή για την αγγλική έκδοση.
STREET_EN   = "25 Ethnarchou Makariou"
CITY_EN     = "Ilioupoli"
REGION_EN   = "Attica"
NAME_EN     = "Christina Stamatopoulou"
CITY        = "Ηλιούπολη"
CITY_GEN    = "Ηλιούπολης"
CITY_ACC    = "Ηλιούπολη"
REGION      = "Αττική"
ZIP         = "16345"
ZIP_PRETTY  = "163 45"

# Ένα τηλέφωνο, κατόπιν οδηγίας της πελάτισσας: το σταθερό του ιατρείου
# αφαιρέθηκε εντελώς από το site και μένει μόνο το κινητό.
PHONE       = "6972487486"
PHONE_P     = "697 248 7486"

EMAIL       = "psychoptia@yahoo.com"

# Τα κοινωνικά δίκτυα της πελάτισσας. Τα εικονίδια είναι τα σήματα των
# πλατφορμών στα δικά τους χρώματα — βλ. SOCIAL_ICONS παρακάτω.
SOCIALS = [
    ("facebook",  "Facebook",  "https://www.facebook.com/psychoptia"),
    ("instagram", "Instagram", "https://www.instagram.com/psychoptia"),
    ("tiktok",    "TikTok",    "https://www.tiktok.com/@psychoptia"),
]
GBP         = "https://www.google.com/maps/search/?api=1&query=Psychoptia+%CE%A7%CF%81%CE%B9%CF%83%CF%84%CE%AF%CE%BD%CE%B1+%CE%A3%CF%84%CE%B1%CE%BC%CE%B1%CF%84%CE%BF%CF%80%CE%BF%CF%8D%CE%BB%CE%BF%CF%85"
MAPS        = GBP
SESSION     = "50"                  # λεπτά ανά συνεδρία
LAT, LON    = "37.9310", "23.7580"  # Ηλιούπολη — να μπει το ακριβές στίγμα του γραφείου

# Περιοχές για τοπικό SEO. Κατόπιν οδηγίας, η κάλυψη δεν περιορίζεται πια στα
# νότια προάστια: οι διά ζώσης συνεδρίες αφορούν όλη την Αττική. Οι πρώτες
# περιοχές είναι οι όμορες του γραφείου — εκεί έχει νόημα η εγγύτητα· οι
# υπόλοιπες μπαίνουν για αναζητήσεις τύπου «ψυχολόγος + περιοχή».
# Τα τοπωνύμια δίνονται και στη λατινική τους γραφή: ο αγγλόφωνος επισκέπτης
# αναζητά «psychologist Glyfada», όχι «ψυχολόγος Γλυφάδα».
AREAS_NEAR_I18N = {
 "el": ["Ηλιούπολη", "Αργυρούπολη", "Άλιμος", "Γλυφάδα", "Βύρωνας", "Δάφνη",
        "Υμηττός", "Άγιος Δημήτριος", "Ελληνικό", "Νέα Σμύρνη", "Καισαριανή",
        "Βούλα", "Βουλιαγμένη", "Άνω Ηλιούπολη"],
 "en": ["Ilioupoli", "Argyroupoli", "Alimos", "Glyfada", "Vyronas", "Dafni",
        "Ymittos", "Agios Dimitrios", "Elliniko", "Nea Smyrni", "Kaisariani",
        "Voula", "Vouliagmeni", "Upper Ilioupoli"],
}
AREAS_WIDER_I18N = {
 "el": ["Αθήνα Κέντρο", "Παγκράτι", "Ζωγράφου", "Νέος Κόσμος", "Καλλιθέα",
        "Παλαιό Φάληρο", "Μοσχάτο", "Ταύρος", "Πετράλωνα", "Κουκάκι",
        "Χολαργός", "Παπάγου", "Αγία Παρασκευή", "Χαλάνδρι", "Μαρούσι",
        "Κηφισιά", "Νέα Ιωνία", "Γαλάτσι", "Πειραιάς", "Κορυδαλλός",
        "Νίκαια", "Περιστέρι", "Αιγάλεω", "Χαϊδάρι", "Ίλιον", "Αχαρνές",
        "Κρωπία", "Παιανία", "Σπάτα", "Μαρκόπουλο", "Ραφήνα", "Βάρη"],
 "en": ["Athens Centre", "Pangrati", "Zografou", "Neos Kosmos", "Kallithea",
        "Palaio Faliro", "Moschato", "Tavros", "Petralona", "Koukaki",
        "Cholargos", "Papagou", "Agia Paraskevi", "Chalandri", "Marousi",
        "Kifisia", "Nea Ionia", "Galatsi", "Piraeus", "Korydallos",
        "Nikaia", "Peristeri", "Egaleo", "Chaidari", "Ilion", "Acharnes",
        "Koropi", "Paiania", "Spata", "Markopoulo", "Rafina", "Vari"],
}


class _Areas(list):
    """Λίστα που διαβάζει πάντα την τρέχουσα γλώσσα.

    Οι λίστες περιοχών χρησιμοποιούνται σε δεκάδες σημεία ως απλά ονόματα
    (`AREAS_NEAR`). Αν γίνονταν συναρτήσεις θα άλλαζαν όλα τα σημεία κλήσης·
    έτσι μένουν λίστες και απλώς ξέρουν σε ποια γλώσσα βρισκόμαστε.
    """
    def __init__(self, table):
        self._t = table

    def _cur(self):
        return self._t[i18n.LANG]

    def __iter__(self):    return iter(self._cur())
    def __len__(self):     return len(self._cur())
    def __getitem__(self, i): return self._cur()[i]
    def __repr__(self):    return repr(self._cur())


AREAS_NEAR = _Areas(AREAS_NEAR_I18N)
AREAS_WIDER = _Areas(AREAS_WIDER_I18N)

AREAS = _Areas({k: AREAS_NEAR_I18N[k] + AREAS_WIDER_I18N[k] for k in ('el', 'en')})

# Χώρες όπου έχει νόημα η διαδικτυακή αναφορά (ελληνόφωνη διασπορά).
COUNTRIES = {
 "el": ["Κύπρος", "Ηνωμένο Βασίλειο", "Γερμανία", "Ολλανδία", "Βέλγιο",
        "Ελβετία", "ΗΠΑ", "Καναδάς", "Αυστραλία", "Ηνωμένα Αραβικά Εμιράτα"],
 "en": ["Cyprus", "the United Kingdom", "Germany", "the Netherlands", "Belgium",
        "Switzerland", "the USA", "Canada", "Australia", "the UAE"],
}

# Ονόματα στατικών αρχείων με αποτύπωμα περιεχομένου (συμπληρώνονται στο build).
ASSETS = {"css": "site.css", "js": "site.js"}

# ------------------------------------------------------------------ πλοήγηση
# Κάθε σελίδα υπάρχει σε δύο διευθύνσεις. Οι αγγλικές δεν είναι μεταγραφές των
# ελληνικών αλλά κανονικά αγγλικά slugs, γιατί αυτά διαβάζει η Google για την
# αγγλική έκδοση. Το μητρώο χρησιμεύει και για το hreflang και για τον
# διακόπτη γλώσσας, που πρέπει να ξέρει το αντίστοιχο κάθε σελίδας.
PAGE_SLUGS = {
    "index.html":                        "en/index.html",
    "viografiko.html":                   "en/about.html",
    "ypiresies.html":                    "en/services.html",
    "arthra.html":                       "en/articles.html",
    "epikoinonia.html":                  "en/contact.html",
    "psychologos-ilioupoli.html":        "en/psychologist-ilioupoli.html",
    "syxnes-erotiseis.html":             "en/faq.html",
    "politiki-aporritou.html":           "en/privacy-policy.html",
    "oroi-xrisis.html":                  "en/terms-of-use.html",
    "404.html":                          "en/404.html",
    "arthra/aftofrontida-frontiston.html": "en/articles/carer-self-care.html",
}
def page_slug(el_slug):
    """Το slug μιας σελίδας στην τρέχουσα γλώσσα, από το ελληνικό της slug."""
    return el_slug if i18n.LANG == "el" else PAGE_SLUGS[el_slug]


def depth_of(slug):
    """Πόσα «../» χρειάζεται μια σελίδα για να φτάσει στη ρίζα."""
    return slug.count("/")


def nav_items():
    """Η κύρια πλοήγηση στην τρέχουσα γλώσσα, ως [(ετικέτα, href)].

    Οι τρεις θεραπευτικές κατηγορίες κάθονται στο πρώτο επίπεδο, κατόπιν
    οδηγίας: η γενική καρτέλα «Υπηρεσίες» έκρυβε ακριβώς αυτό που έπρεπε να
    φαίνεται. Η σελίδα-κόμβος υπηρεσιών παραμένει, αλλά πλέον φτάνει κανείς σε
    αυτήν από το footer και όχι από το μενού.
    """
    return ([(T("nav.home"), page_slug("index.html")),
             (T("nav.bio"),  page_slug("viografiko.html"))]
            + [(L(c, "nav"), S(c)) for c in CATEGORIES]
            + [(T("nav.articles"), page_slug("arthra.html")),
               (T("nav.contact"),  page_slug("epikoinonia.html"))])


def category_of(el_slug):
    """Η καρτέλα στην οποία ανήκει μια σελίδα υπηρεσίας (ελληνικό slug).

    Χρησιμεύει σε δύο σημεία: ποια καρτέλα φωτίζεται στο μενού όταν βλέπεις
    ένα φύλλο, και τι γράφει το breadcrumb ανάμεσα στην αρχική και τη σελίδα.
    """
    for c in CATEGORIES:
        if el_slug == c["slug"] or el_slug in c["children"]:
            return c
    return None

SERVICES = [
    dict(slug="ypiresies/psychotherapeia-paidion.html",
         slug_en="en/services/child-psychotherapy.html",
         icon="child",
         photos=[dict(f="svc-psychotherapeia-paidion",
                      el=("Μικρό παιδί απλώνει το χέρι σε λούτρινο αρκουδάκι, σε φωτεινό δωμάτιο με ζωγραφιές και ξύλινα παιχνίδια",
                          "Το παιδί πλησιάζει αυτό που το δυσκολεύει μέσα από το παιχνίδι — πριν βρει τις λέξεις."),
                      en=("A young child reaching for a teddy bear in a bright room with drawings and wooden toys",
                          "A child approaches what troubles it through play — before it finds the words."))],
         el=dict(nav="Ψυχοθεραπεία Παιδιών", who="Παιδιά", short="Ψυχοθεραπεία Παιδιών",
                 teaser="Το παιδί εκφράζεται μέσα από το παιχνίδι και τη δημιουργία, πριν βρει τις λέξεις. Η θεραπεία ακολουθεί αυτόν τον δρόμο, μαζί με τους γονείς."),
         en=dict(nav="Child Psychotherapy", who="Children", short="Child Psychotherapy",
                 teaser="A child expresses itself through play and making things, long before it finds the words. Therapy follows that route — together with the parents.")),
    dict(slug="ypiresies/psychotherapeia-efivon.html",
         slug_en="en/services/adolescent-psychotherapy.html",
         icon="spark",
         photos=[dict(f="svc-psychotherapeia-efivon",
                      el=("Έφηβη με ακουστικά, καθισμένη σε φαρδύ περβάζι δίπλα σε μεγάλο παράθυρο, κοιτάζοντας έξω",
                          "Ένας τρίτος χώρος, έξω από το σπίτι και το σχολείο, όπου ο έφηβος σκέφτεται δυνατά χωρίς συνέπειες."),
                      en=("A teenager with headphones sitting on a wide window ledge, looking outside",
                          "A third space, outside home and school, where a teenager can think out loud without consequences."))],
         el=dict(nav="Ψυχοθεραπεία Εφήβων", who="Έφηβοι", short="Ψυχοθεραπεία Εφήβων",
                 teaser="Ένας χώρος δικός του, όπου ο έφηβος μιλά χωρίς να αξιολογείται — για την ταυτότητα, τις σχέσεις, το άγχος και την εικόνα του εαυτού."),
         en=dict(nav="Adolescent Psychotherapy", who="Teenagers", short="Adolescent Psychotherapy",
                 teaser="A space of their own, where a teenager speaks without being judged — about identity, relationships, anxiety and self-image.")),
    dict(slug="ypiresies/psychotherapeia-enilikon.html",
         slug_en="en/services/adult-psychotherapy.html",
         icon="person",
         photos=[dict(f="svc-psychotherapeia-enilikon",
                      el=("Ενήλικη γυναίκα καθισμένη σε πολυθρόνα δίπλα στο παράθυρο, με τα χέρια στο στήθος και κλειστά μάτια",
                          "Ατομικές συνεδρίες: χρόνος και χώρος για αυτό που επαναλαμβάνεται και δεν λύνεται μόνο του."),
                      en=("An adult woman sitting in an armchair by the window, hands on her chest and eyes closed",
                          "Individual sessions: time and space for what keeps repeating and will not resolve on its own."))],
         el=dict(nav="Ψυχοθεραπεία Ενηλίκων", who="Ενήλικες", short="Ψυχοθεραπεία Ενηλίκων",
                 teaser="Ατομικές συνεδρίες για άγχος, πανικό, διάθεση, εξουθένωση, σχέσεις και ταυτότητα — με κλινική αξιολόγηση και στόχους που ορίζουμε μαζί."),
         en=dict(nav="Adult Psychotherapy", who="Adults", short="Adult Psychotherapy",
                 teaser="Individual sessions for anxiety, panic, mood, burnout, relationships and identity — with clinical assessment and goals we set together.")),
    dict(slug="ypiresies/symvouleftiki-goneon.html",
         slug_en="en/services/parent-counselling.html",
         icon="hands",
         photos=[dict(f="svc-symvouleftiki-goneon",
                      el=("Δύο γονείς ξαπλωμένοι με το μικρό τους παιδί ανάμεσά τους, γελώντας",
                          "Η δουλειά με τους γονείς αλλάζει το πλαίσιο μέσα στο οποίο ζει το παιδί."),
                      en=("Two parents lying down with their small child between them, laughing",
                          "Work with parents changes the context the child actually lives in."))],
         el=dict(nav="Συμβουλευτική Γονέων", who="Γονείς", short="Συμβουλευτική Γονέων",
                 teaser="Όταν αλλάζει το πλαίσιο γύρω από το παιδί, αλλάζει και η δυσκολία. Όρια, επικοινωνία και σχέση γονέα–παιδιού."),
         en=dict(nav="Parent Counselling", who="Parents", short="Parent Counselling",
                 teaser="When the context around a child changes, so does the difficulty. Boundaries, communication and the parent–child relationship.")),
    dict(slug="ypiresies/paigniotherapeia-dimiourgikes-technes.html",
         slug_en="en/services/play-therapy-creative-arts.html",
         icon="palette",
         photos=[dict(f="svc-paigniotherapeia",
                      el=("Χώρος παιγνιοθεραπείας: τραπέζι με ξυλομπογιές και μπλοκ ζωγραφικής, παιδικές ζωγραφιές στον τοίχο και ξύλινα παιχνίδια",
                          "Ο χώρος του παιχνιδιού είναι το ίδιο το θεραπευτικό μέσο, όχι διάλειμμα από τη δουλειά."),
                      en=("A play therapy room: a table with coloured pencils and a sketchpad, children's drawings on the wall and wooden toys",
                          "The play space is the therapeutic medium itself, not a break from the work."))],
         el=dict(nav="Παιγνιοθεραπεία &amp; Δημιουργικές Τέχνες", who="Παιδιά &amp; έφηβοι",
                 short="Παιγνιοθεραπεία &amp; Δημιουργικές&nbsp;Τέχνες",
                 teaser="Παιχνίδι, ζωγραφική, αφήγηση και δραματοποίηση ως θεραπευτικά εργαλεία — εκεί όπου ο λόγος από μόνος του δεν φτάνει."),
         en=dict(nav="Play Therapy &amp; Creative Arts", who="Children &amp; teens",
                 short="Play Therapy &amp; Creative&nbsp;Arts",
                 teaser="Play, drawing, storytelling and dramatisation as therapeutic tools — where words alone do not reach.")),
    dict(slug="ypiresies/energeiakes-therapeies.html",
         slug_en="en/services/energy-therapies.html",
         icon="infinity",
         # Δύο λήψεις, μία ανά μέθοδο: η κάρτα δείχνει την πρώτη, η σελίδα και τις δύο.
         photos=[dict(f="svc-theta-healing",
                      el=("Δύο ζευγάρια χέρια ακουμπισμένα σε ξύλινο τραπέζι, με αναμμένο κερί και κρυστάλλους στο βάθος",
                          "Theta Healing: μια ήρεμη, καθοδηγούμενη διαδικασία βαθιάς χαλάρωσης."),
                      en=("Two pairs of hands resting on a wooden table, with a lit candle and crystals in the background",
                          "Theta Healing: a calm, guided process of deep relaxation.")),
                 dict(f="svc-radiaisthisia",
                      el=("Χέρι που κρατά εκκρεμές πάνω από κυκλικό διάγραμμα ραδιαισθησίας, με κρυστάλλους και σημειώσεις γύρω",
                          "Θεραπευτική ραδιαισθησία: εργασία με εκκρεμές και διαγράμματα, σε πλαίσιο ξεχωριστό από την ψυχοθεραπεία."),
                      en=("A hand holding a pendulum over a circular dowsing chart, with crystals and notes around it",
                          "Therapeutic dowsing: work with a pendulum and charts, in a setting separate from psychotherapy."))],
         el=dict(nav="Ενεργειακές Θεραπείες", who="Συμπληρωματικά", short="Ενεργειακές Θεραπείες",
                 teaser="Συμπληρωματικές μέθοδοι χαλάρωσης και ενεργειακής εργασίας, σε ξεχωριστό πλαίσιο από την ψυχοθεραπεία και πάντα κατόπιν συζήτησης."),
         en=dict(nav="Energy Therapies", who="Complementary", short="Energy Therapies",
                 teaser="Complementary relaxation and energy-work methods, in a setting entirely separate from psychotherapy and always after discussion.")),
]

# Οι τρεις καρτέλες που ζήτησε η πελάτισσα. Το SERVICES από πάνω κρατά τις έξι
# αναλυτικές σελίδες — δεν χάνονται, απλώς παύουν να είναι όλες ισότιμες στο
# μενού: η ψυχοθεραπεία γίνεται μία καρτέλα με τις ηλικιακές ομάδες από μέσα,
# ενώ η παιγνιοθεραπεία και οι ενεργειακές θεραπείες ανεβαίνουν σε πρώτο
# επίπεδο ώστε να μη «χάνονται» μέσα στις γενικές υπηρεσίες.
CATEGORIES = [
    dict(slug="ypiresies/psychotherapeia-symvouleftiki.html",
         slug_en="en/services/psychotherapy-counselling.html",
         icon="chat",
         photos=[dict(f="svc-psychotherapeia-enilikon",
                      el=("Ενήλικη γυναίκα καθισμένη σε πολυθρόνα δίπλα στο παράθυρο, με τα χέρια στο στήθος και κλειστά μάτια",
                          "Μία διαδικασία, τέσσερα πλαίσια — ανάλογα με την ηλικία και το αίτημα."),
                      en=("An adult woman sitting in an armchair by the window, hands on her chest and eyes closed",
                          "One process, four settings — depending on age and on what is being asked."))],
         children=["ypiresies/psychotherapeia-paidion.html",
                   "ypiresies/psychotherapeia-efivon.html",
                   "ypiresies/psychotherapeia-enilikon.html",
                   "ypiresies/symvouleftiki-goneon.html"],
         el=dict(nav="Ψυχοθεραπεία &amp; Συμβουλευτική", who="Παιδιά · Έφηβοι · Ενήλικες · Γονείς",
                 short="Ψυχοθεραπεία &amp; Συμβουλευτική",
                 teaser="Ατομικές συνεδρίες για κάθε ηλικία και συμβουλευτική γονέων. Το πλαίσιο προκύπτει από την κλινική αξιολόγηση της πρώτης συνάντησης."),
         en=dict(nav="Psychotherapy &amp; Counselling", who="Children · Teens · Adults · Parents",
                 short="Psychotherapy &amp; Counselling",
                 teaser="Individual sessions for every age, plus parent counselling. The setting follows from the clinical assessment in the first meeting.")),
    dict(slug="ypiresies/paigniotherapeia-dimiourgikes-technes.html",
         slug_en="en/services/play-therapy-creative-arts.html",
         icon="palette",
         photos=[dict(f="svc-paigniotherapeia",
                      el=("Χώρος παιγνιοθεραπείας: τραπέζι με ξυλομπογιές και μπλοκ ζωγραφικής, παιδικές ζωγραφιές στον τοίχο και ξύλινα παιχνίδια",
                          "Ο χώρος του παιχνιδιού είναι το ίδιο το θεραπευτικό μέσο, όχι διάλειμμα από τη δουλειά."),
                      en=("A play therapy room: a table with coloured pencils and a sketchpad, children's drawings on the wall and wooden toys",
                          "The play space is the therapeutic medium itself, not a break from the work."))],
         children=[],
         el=dict(nav="Παιγνιοθεραπεία", who="Παιδιά &amp; έφηβοι",
                 short="Παιγνιοθεραπεία &amp; Δημιουργικές&nbsp;Τέχνες",
                 teaser="Παιχνίδι, ζωγραφική, αφήγηση και δραματοποίηση ως θεραπευτικά εργαλεία — εκεί όπου ο λόγος από μόνος του δεν φτάνει."),
         en=dict(nav="Play Therapy", who="Children &amp; teens",
                 short="Play Therapy &amp; Creative&nbsp;Arts",
                 teaser="Play, drawing, storytelling and dramatisation as therapeutic tools — where words alone do not reach.")),
    dict(slug="ypiresies/energeiakes-therapeies.html",
         slug_en="en/services/energy-therapies.html",
         icon="infinity",
         photos=[dict(f="svc-theta-healing",
                      el=("Δύο ζευγάρια χέρια ακουμπισμένα σε ξύλινο τραπέζι, με αναμμένο κερί και κρυστάλλους στο βάθος",
                          "Συμπληρωματικές μέθοδοι, πάντα κατόπιν συζήτησης και ποτέ στη θέση ενδεδειγμένης θεραπείας."),
                      en=("Two pairs of hands resting on a wooden table, with a lit candle and crystals in the background",
                          "Complementary methods, always after discussion and never in place of indicated treatment."))],
         children=[],
         el=dict(nav="Ενεργειακές Θεραπείες", who="Συμπληρωματικά", short="Ενεργειακές Θεραπείες",
                 teaser="Theta Healing και θεραπευτική ραδιαισθησία, ως συμπληρωματικές μέθοδοι χαλάρωσης — σε πλαίσιο ξεχωριστό από την ψυχοθεραπεία."),
         en=dict(nav="Energy Therapies", who="Complementary", short="Energy Therapies",
                 teaser="Theta Healing and therapeutic dowsing, as complementary relaxation methods — in a setting separate from psychotherapy.")),
]


# Οι σελίδες υπηρεσιών συμπληρώνουν το μητρώο μόλις οριστούν.
PAGE_SLUGS.update({x["slug"]: x["slug_en"] for x in SERVICES})
PAGE_SLUGS.update({x["slug"]: x["slug_en"] for x in CATEGORIES})
EN_TO_EL = {v: k for k, v in PAGE_SLUGS.items()}


def L(item, key):
    """Το πεδίο ενός SERVICES/CATEGORIES στην τρέχουσα γλώσσα."""
    return item[i18n.LANG][key]


def S(item):
    """Το slug ενός SERVICES/CATEGORIES στην τρέχουσα γλώσσα."""
    return item["slug"] if i18n.LANG == "el" else item["slug_en"]


def photo_of(item, i=0):
    """(αρχείο, alt, λεζάντα) της i-οστής φωτογραφίας, στην τρέχουσα γλώσσα."""
    ph = item.get("photos")
    if not ph:
        return None
    alt, cap = ph[i][i18n.LANG]
    return ph[i]["f"], alt, cap


def cat_children(cat):
    """Οι αναλυτικές σελίδες που κρέμονται από μια καρτέλα."""
    by_slug = {s["slug"]: s for s in SERVICES}
    return [by_slug[c] for c in cat["children"]]


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
 "share": '<circle cx="18" cy="5" r="3"/><circle cx="6" cy="12" r="3"/><circle cx="18" cy="19" r="3"/><path d="m8.6 13.5 6.8 4M15.4 6.5l-6.8 4"/>',
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


# ------------------------------------------------------- σήματα κοινωνικών δικτύων
# Τα σήματα των πλατφορμών, στα δικά τους χρώματα (η πελάτισσα ζήτησε ρητά
# «χρωματιστά εικονίδια»). Δεν περνούν από το ICONS/icon(): εκείνα είναι
# μονόγραμμα σχέδια που κληρονομούν το currentColor, ενώ εδώ το χρώμα είναι
# μέρος του σήματος και δεν επιτρέπεται να αλλάξει από το CSS της σελίδας.
#
# Το Instagram χρειάζεται βαθμίδα, άρα και <defs> με μοναδικό id ανά εμφάνιση —
# αν το ίδιο id υπάρξει δύο φορές στη σελίδα (κάρτα επικοινωνίας + footer), ο
# browser κρατά το πρώτο και το δεύτερο εικονίδιο μένει άχρωμο. Γι' αυτό το id
# παίρνει μετρητή.
_IG_GRAD = 0

SOCIAL_PATHS = {
 "facebook": '<path fill="#1877F2" d="M24 12.07C24 5.4 18.63 0 12 0S0 5.4 0 12.07C0 18.1 4.39 23.1 10.13 24v-8.44H7.08v-3.49h3.05V9.41c0-3.02 1.79-4.69 4.53-4.69 1.31 0 2.68.24 2.68.24v2.97h-1.51c-1.49 0-1.96.93-1.96 1.89v2.25h3.33l-.53 3.49h-2.8V24C19.61 23.1 24 18.1 24 12.07z"/>',
 "tiktok": (
   # Το σήμα τυπώνεται τρεις φορές με μικρή μετατόπιση: κυανό και ματζέντα από
   # κάτω, μαύρο από πάνω — έτσι προκύπτει το χαρακτηριστικό «τρεμάρισμα».
   '<g><path fill="#25F4EE" transform="translate(-1.1 .7)" d="M16.6 5.82A4.28 4.28 0 0 1 15.54 3h-3.09v12.4a2.59 2.59 0 0 1-2.59 2.5 2.59 2.59 0 1 1 .77-5.06V9.7a5.68 5.68 0 0 0-4.87 9.65 5.68 5.68 0 0 0 9.65-4.02V8.71a7.35 7.35 0 0 0 4.29 1.37V7a4.28 4.28 0 0 1-3.1-1.18z"/>'
   '<path fill="#FE2C55" transform="translate(1.1 -.5)" d="M16.6 5.82A4.28 4.28 0 0 1 15.54 3h-3.09v12.4a2.59 2.59 0 0 1-2.59 2.5 2.59 2.59 0 1 1 .77-5.06V9.7a5.68 5.68 0 0 0-4.87 9.65 5.68 5.68 0 0 0 9.65-4.02V8.71a7.35 7.35 0 0 0 4.29 1.37V7a4.28 4.28 0 0 1-3.1-1.18z"/>'
   '<path fill="#161823" d="M16.6 5.82A4.28 4.28 0 0 1 15.54 3h-3.09v12.4a2.59 2.59 0 0 1-2.59 2.5 2.59 2.59 0 1 1 .77-5.06V9.7a5.68 5.68 0 0 0-4.87 9.65 5.68 5.68 0 0 0 9.65-4.02V8.71a7.35 7.35 0 0 0 4.29 1.37V7a4.28 4.28 0 0 1-3.1-1.18z"/></g>'),
}


def social_icon(name):
    """Το σήμα μιας πλατφόρμας ως αυτόνομο SVG 24×24."""
    global _IG_GRAD
    if name == "instagram":
        _IG_GRAD += 1
        gid = "ig%d" % _IG_GRAD
        body = (
            '<defs><radialGradient id="%s" cx=".25" cy="1.05" r="1.2">'
            '<stop offset="0" stop-color="#FDD879"/><stop offset=".28" stop-color="#F9906F"/>'
            '<stop offset=".54" stop-color="#D8256D"/><stop offset=".82" stop-color="#A034A9"/>'
            '<stop offset="1" stop-color="#5B51D8"/></radialGradient></defs>'
            '<rect x="1.4" y="1.4" width="21.2" height="21.2" rx="6.2" fill="url(#%s)"/>'
            '<circle cx="12" cy="12" r="4.6" fill="none" stroke="#fff" stroke-width="1.9"/>'
            '<circle cx="17.6" cy="6.4" r="1.35" fill="#fff"/>' % (gid, gid))
    else:
        body = SOCIAL_PATHS[name]
    return ('<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" '
            'width="24" height="24" aria-hidden="true">%s</svg>' % body)


def social_links(cls="cb-socials"):
    """Οι τρεις σύνδεσμοι. Ανοίγουν σε νέα καρτέλα με rel=noopener."""
    out = "".join(
        f'<a class="cb-socials__a cb-socials__a--{k}" href="{url}" '
        f'target="_blank" rel="noopener noreferrer me" aria-label="{label}">'
        f'{social_icon(k)}</a>' for k, label, url in SOCIALS)
    return f'<span class="{cls}">{out}</span>'


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
            "name": ("Υπηρεσίες ψυχοθεραπείας και συμβουλευτικής" if i18n.LANG == "el"
                     else "Psychotherapy and counselling services"),
            "itemListElement": [
                {"@type": "Offer", "itemOffered": {"@type": "Service",
                 "name": plain(L(x, "short")), "url": SITE_URL + "/" + S(x)}}
                for x in SERVICES
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
    return '<p class="cb-hours__foot">%s</p>' % T("cc.hours")


def contact_card(depth):
    r = rel(depth)
    return f"""<div class="cb-contact-card">
<div class="cb-contact-card__row">{icon('pin', 'w-5 h-5 cb-violet shrink-0')}
<div><span class="cb-contact-card__k">{T("cc.address")}</span>
<a href="{MAPS}" target="_blank" rel="noopener noreferrer">{street()}, {ZIP_PRETTY} {city()}</a></div></div>
<div class="cb-contact-card__row">{icon('phone', 'w-5 h-5 cb-violet shrink-0')}
<div><span class="cb-contact-card__k">{T("cc.phone")}</span>
<a href="tel:+30{PHONE}">{PHONE_P}</a></div></div>
<div class="cb-contact-card__row">{icon('mail', 'w-5 h-5 cb-violet shrink-0')}
<div><span class="cb-contact-card__k">{T("cc.email")}</span>
<a href="mailto:{EMAIL}">{EMAIL}</a></div></div>
<div class="cb-contact-card__row">{icon('clock', 'w-5 h-5 cb-violet shrink-0')}
<div><span class="cb-contact-card__k">{T("cc.booking")}</span>
{hours_note()}</div></div>
<div class="cb-contact-card__row">{icon('share', 'w-5 h-5 cb-violet shrink-0')}
<div><span class="cb-contact-card__k">{T("cc.follow")}</span>
{social_links()}</div></div>
</div>"""


def online_note():
    """Οι διαδικτυακές συνεδρίες είναι το πρακτικό διαφοροποιητικό στοιχείο."""
    return (f'<div class="cb-access">{icon("monitor", "cb-access__ic")}'
            f'<div><strong>{T("online.t")}</strong>'
            f'<span>{T("online.d").format(c=city())}</span></div></div>')


def areas_block():
    """Οι περιοχές εξυπηρέτησης ως chips — και για τον αναγνώστη, και για τις
    αναζητήσεις «ψυχολόγος + περιοχή» που ζήτησε το §9 του checklist."""
    near = "".join(f'<span class="cb-area cb-area--near">{a}</span>' for a in AREAS_NEAR)
    wide = "".join(f'<span class="cb-area">{a}</span>' for a in AREAS_WIDER)
    countries = " · ".join(COUNTRIES[i18n.LANG])
    return f"""<div class="cb-areas">
<h3 class="cb-areas__h">{T("areas.inPerson")}</h3>
<p class="cb-areas__d">{T("areas.near").format(c=city())}</p>
<div class="cb-area-list">{near}</div>
<p class="cb-areas__d">{T("areas.wider")}</p>
<div class="cb-area-list">{wide}</div>
<h3 class="cb-areas__h">{T("areas.online")}</h3>
<p class="cb-areas__d">{T("areas.onlineD").format(k=countries)}</p>
</div>"""


def crisis_note():
    return '<div class="cb-note cb-note--alert">%s</div>' % T("crisis")


# Πού στέλνει η φόρμα. Ο ιστότοπος είναι στατικός, οπότε χρειάζεται εξωτερικό
# endpoint (Formspree, Web3Forms, Vercel function κ.λπ.). Όσο μένει κενό, η
# φόρμα δουλεύει με fallback: το site.js συνθέτει το μήνυμα και ανοίγει τον
# mail client της συσκευής. Μόλις μπει endpoint, στέλνει με fetch χωρίς
# ανακατεύθυνση — δεν χρειάζεται καμία άλλη αλλαγή.
FORM_ENDPOINT = ""


def contact_form(depth):
    """Η απλή φόρμα πρώτης επικοινωνίας.

    Κατόπιν οδηγίας: χωρίς ηλεκτρονική ατζέντα, χωρίς σύνθετο ερωτηματολόγιο —
    μόνο τα απολύτως αναγκαία πεδία ώστε να μπορεί να απαντηθεί το αίτημα.
    Το τηλέφωνο μένει προαιρετικό: πολλοί προτιμούν να απαντηθούν γραπτά.

    Η συγκατάθεση είναι ξεχωριστό, μη προεπιλεγμένο checkbox: το μήνυμα μπορεί
    να περιέχει δεδομένα υγείας, οπότε δεν αρκεί μια δήλωση «με την αποστολή
    αποδέχεστε».
    """
    r = rel(depth)
    r = rel(depth)
    priv = r + page_slug("politiki-aporritou.html")
    return f"""<div class="cb-form-wrap">
<p class="cb-form__lede">{T("form.lede")}</p>
<form class="cb-form" data-contact-form data-endpoint="{FORM_ENDPOINT}" data-mailto="{EMAIL}"
 data-subject="{T("form.subject")}" method="post"
 action="{FORM_ENDPOINT or 'mailto:' + EMAIL}" novalidate>
<div class="cb-form__row">
<label class="cb-field"><span>{T("form.name")} <em>*</em></span>
<input name="name" type="text" required autocomplete="name" maxlength="80"></label>
<label class="cb-field"><span>{T("form.email")} <em>*</em></span>
<input name="email" type="email" required autocomplete="email" maxlength="120"></label>
</div>
<label class="cb-field"><span>{T("form.phone")} <i>{T("form.optional")}</i></span>
<input name="phone" type="tel" autocomplete="tel" maxlength="30"></label>
<label class="cb-field"><span>{T("form.message")} <em>*</em></span>
<textarea name="message" rows="5" required maxlength="1500"
 placeholder="{T("form.ph")}"></textarea></label>
<label class="cb-check"><input name="consent" type="checkbox" required>
<span>{T("form.consent").format(u=priv)}</span></label>
<button class="cb-btn cb-btn--dark" type="submit">{T("form.send")}<span class="cb-btn__arrow">&#8594;</span></button>
<p class="cb-form__status" data-form-status role="status" aria-live="polite"></p>
</form>
<p class="cb-form__note">{T("form.note").format(p=PHONE, pp=PHONE_P)}</p>
</div>"""
