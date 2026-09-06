# -*- coding: utf-8 -*-
"""Παράγει τα στατικά εικαστικά του site από τα πρωτότυπα αρχεία της πελάτισσας.

    python3 _build/make_assets.py

Πηγές (στη ρίζα του φακέλου):
  • LOGO - F4FAF825….png   — το λογότυπο, τυπωμένο σε βαθύ indigo φόντο.
  • PHOTO - ….jpg          — πέντε λήψεις: πορτρέτο και ο χώρος του γραφείου.

Απαιτεί Pillow:  python3 -m pip install Pillow
"""
import pathlib
import numpy as np
from PIL import Image, ImageDraw

BASE = pathlib.Path(__file__).resolve().parent.parent
IMG = BASE / "website" / "assets" / "img"

LOGO_SRC = BASE / "LOGO - F4FAF825-D5E2-4AD0-8A78-E2FE4213720C.png"

# Οι πέντε φωτογραφίες που επέλεξε ο πελάτης, με τον ρόλο της καθεμιάς.
PHOTOS = {
    "christina-stamatopoulou.jpg": "PHOTO - 8DC9041D-8F10-4E7C-A887-873324A72B36.jpg",  # πορτρέτο
    "grafeio.jpg":                 "PHOTO - IMG_1911.jpg",                              # ο χώρος, ευρεία λήψη
    "grafeio-synedria.jpg":        "PHOTO - 9DB60425-63DE-42CC-B576-34FC087E5AD5.jpg",  # στην πολυθρόνα
    "grafeio-grafeio.jpg":         "PHOTO - B995789B-5DC9-4577-B0B6-CB73DEA3891D.jpg",  # στο γραφείο
    "online-synedries.jpg":        "PHOTO - BD479336-1092-4B69-9E69-F81CE67521E4.jpg",  # διαδικτυακά
}

# Οι φωτογραφίες των υπηρεσιών, μία ανά θεραπευτική κατηγορία. Το κλειδί είναι
# το όνομα με το οποίο τις ζητά το site (βλ. SERVICES στο gen_common.py). Τα πεδία:
#   focus — η κατακόρυφη εστίαση της περικοπής (0 = πάνω, 1 = κάτω)· χρειάζεται
#           μόνο όπου το θέμα δεν κάθεται στο κέντρο του κάδρου.
#   card  — αν βγαίνει και σε μικρό μέγεθος για το κουτάκι της αρχικής. Η
#           ραδιαισθησία μοιράζεται κάρτα με το Theta Healing, οπότε εμφανίζεται
#           μόνο μεγάλη, μέσα στη σελίδα των ενεργειακών μεθόδων.
SERVICE_PHOTOS = {
    "svc-psychotherapeia-enilikon":  dict(src="SERVICE - psychotherapeia-enilikon.jpg", focus=0.34),
    "svc-psychotherapeia-efivon":    dict(src="SERVICE - psychotherapeia-efivon.jpg"),
    "svc-psychotherapeia-paidion":   dict(src="SERVICE - psychotherapeia-paidion.jpg"),
    "svc-symvouleftiki-goneon":      dict(src="SERVICE - symvouleftiki-goneon.jpg"),
    "svc-paigniotherapeia":          dict(src="SERVICE - paigniotherapeia.jpg"),
    "svc-theta-healing":             dict(src="SERVICE - theta-healing.jpg"),
    "svc-radiaisthisia":             dict(src="SERVICE - radiaisthisia.jpg"),
}

# Η φωτογραφία που κάθεται πίσω από το hero της αρχικής.
HERO_SRC = "PHOTO - HERO.jpg"

# Το σήμα του φορέα πιστοποίησης για το Theta Healing.
THINK_SRC = "LOGO - THETAHEALING THINK.png"

# Το πιστοποιητικό Θεραπευτικής Ραδιαισθησίας (RSSE, Πολωνία). Η πηγή είναι
# φωτογραφία του πλαστικοποιημένου εγγράφου πάνω σε γραφείο· η περικοπή κόβει
# ό,τι περισσεύει γύρω, ώστε να μείνει μόνο το ίδιο το πιστοποιητικό.
CERT_SRC = "CERT - radiaisthisia.jpg"
CERT_BOX = (22, 108, 880, 1395)

INK = (19, 18, 87)          # --cb-ink   · το indigo του λογοτύπου
LIGHT = (248, 247, 252)     # --color-paper
GOLD = (240, 180, 90)       # --cb-gold-soft
OUT_W = 900                 # πλάτος του κάθετου lockup

# Τα στοιχεία του λογοτύπου μέσα στο πρωτότυπο (941×1672). Τα όρια βρέθηκαν με
# ανίχνευση των pixel που απέχουν από το indigo φόντο (βλ. logo_alpha).
LOGO_BOX = (52, 452, 890, 1090)      # ολόκληρο το lockup, με το άπειρο
FLOWER_BOX = (288, 455, 643, 776)    # μόνο το άνθος
TEXT_BOX = (66, 783, 886, 1023)      # PSYCHOPTIA + υπογραφή + ΚΛΙΝΙΚΗ ΨΥΧΟΛΟΓΟΣ


def cutout(box):
    """Απομονώνει ένα τμήμα του λογοτύπου από το indigo φόντο του πρωτοτύπου.

    Το φόντο είναι σχεδόν συμπαγές (#111156 ± λίγο θόρυβο), οπότε η απόσταση
    κάθε pixel από αυτό δίνει απευθείας τη διαφάνεια. Κρατάμε και το χρώμα: το
    άνθος έχει βαθμίδες από μωβ σε λιλά που θα χάνονταν με μονόχρωμη αποκοπή.

    Επιστρέφει (rgb, alpha) ως πίνακες float.
    """
    full = Image.open(LOGO_SRC).convert("RGB")
    # Το φόντο εκτιμάται από τις γωνίες ΟΛΟΚΛΗΡΟΥ του καμβά, όχι του crop:
    # ένα στενό crop μπορεί να έχει μελάνι πάνω στη γωνία του.
    fa = np.asarray(full, np.float32)
    bg = np.median(np.stack([fa[0, 0], fa[0, -1], fa[-1, 0], fa[-1, -1]]), axis=0)

    a = np.asarray(full.crop(box), np.float32)
    dist = np.linalg.norm(a - bg, axis=2)
    # 26 = κάτω από αυτό είναι θόρυβος του φόντου· 108 = πλήρως αδιαφανές.
    alpha = np.clip((dist - 26.0) / (108.0 - 26.0), 0, 1)
    return a, alpha


def to_rgba(rgb, alpha):
    """Πίνακες -> εικόνα RGBA."""
    h, w = alpha.shape
    out = np.zeros((h, w, 4), np.uint8)
    out[..., :3] = np.clip(rgb, 0, 255).astype(np.uint8)
    out[..., 3] = (alpha * 255).astype(np.uint8)
    return Image.fromarray(out, "RGBA")


def deepen(rgb, k, sat=1.15):
    """Βαθαίνει το μελάνι κρατώντας την απόχρωσή του.

    Το πρωτότυπο είναι τυπωμένο *ανοιχτό* πάνω σε indigo. Πάνω στο υπόλευκο
    χαρτί του header η ίδια μελάνη μετρήθηκε σε 2.7:1 αντίθεση — κάτω από το
    ελάχιστο 3:1 για γραφικά και πολύ κάτω από το 4.5:1 που θέλει το μικρό
    κείμενο του λεκτικού. Ο πολλαπλασιασμός με `k` σκουραίνει χωρίς να πειράξει
    τις σχέσεις των καναλιών, άρα το μωβ μένει μωβ και οι πορτοκαλί μύτες των
    πετάλων μένουν πορτοκαλί· η μικρή ενίσχυση κορεσμού αναπληρώνει το
    ξεθώριασμα που φέρνει πάντα το σκούρεμα.
    """
    out = rgb * k
    grey = out.mean(axis=2, keepdims=True)
    return np.clip(grey + (out - grey) * sat, 0, 255)


def save_png8(im, name, colors=128):
    """PNG-8 με παλέτα και διαφάνεια.

    Το FASTOCTREE είναι ο μόνος αλγόριθμος του Pillow που κβαντίζει RGBA
    κρατώντας το alpha, και ρίχνει το αρχείο από ~200 KB σε ~30 KB χωρίς ορατή
    διαφορά σε λογότυπο με λίγα χρώματα.
    """
    im.quantize(colors=colors, method=Image.FASTOCTREE).save(IMG / name, optimize=True)
    print(" ", name, im.size, (IMG / name).stat().st_size // 1024, "KB")


def write_logos():
    """Τρεις εκδοχές του σήματος, για τρεις διαφορετικές θέσεις.

    `logo.png` — **οριζόντιο** lockup σε indigo, για το header. Το πρωτότυπο
    είναι κάθετο (άνθος πάνω, κείμενο κάτω) και σε μια sticky μπάρα πλάτους
    240px θα έφτανε τα 180px ύψος — θα έτρωγε μισή οθόνη. Εδώ το άνθος
    μετακινείται αριστερά του κειμένου, οπότε το ίδιο σήμα χωράει σε ~56px.

    `logo-light.png` — το πρωτότυπο κάθετο lockup, με όλα του τα χρώματα.
    Πηγαίνει εκεί όπου το φόντο είναι το indigo του ίδιου του λογοτύπου και
    υπάρχει χώρος καθ' ύψος: footer και og-image.

    Και οι δύο κρατούν τα χρώματα του πρωτοτύπου — το μωβ άνθος με τις
    πορτοκαλί μύτες. Στο header το μελάνι μόνο βαθαίνει (βλ. `deepen`), όσο
    χρειάζεται για να σταθεί πάνω στο ανοιχτό φόντο· το λεκτικό βαθαίνει
    περισσότερο από το άνθος, γιατί ως κείμενο θέλει μεγαλύτερη αντίθεση.
    """
    # ---- κάθετο, πολύχρωμο: footer & og ------------------------------------
    rgb, alpha = cutout(LOGO_BOX)
    im = to_rgba(rgb, alpha)
    save_png8(im.resize((OUT_W, round(OUT_W * im.height / im.width)), Image.LANCZOS),
              "logo-light.png")

    # ---- οριζόντιο, πολύχρωμο: header --------------------------------------
    frgb, fa = cutout(FLOWER_BOX)
    flower = to_rgba(deepen(frgb, 0.88), fa)
    trgb, ta = cutout(TEXT_BOX)
    text = to_rgba(deepen(trgb, 0.70), ta)

    H = 330                                   # ~3× το ύψος εμφάνισης στο header
    fw = round(H * flower.width / flower.height)
    flower = flower.resize((fw, H), Image.LANCZOS)

    tw = round(H * 0.66 * text.width / text.height)
    text = text.resize((tw, round(H * 0.66)), Image.LANCZOS)

    gap = round(H * 0.14)
    canvas = Image.new("RGBA", (fw + gap + tw, H), (0, 0, 0, 0))
    canvas.alpha_composite(flower, (0, 0))
    canvas.alpha_composite(text, (fw + gap, (H - text.height) // 2))
    save_png8(canvas, "logo.png")


def write_photos():
    for out, src in PHOTOS.items():
        p = Image.open(BASE / src).convert("RGB")
        w = 1400 if p.width >= p.height else 1000
        p = p.resize((w, round(w * p.height / p.width)), Image.LANCZOS)
        p.save(IMG / out, quality=80, optimize=True, progressive=True)
        print(" ", out, p.size, (IMG / out).stat().st_size // 1024, "KB")

    # Τετράγωνη περικοπή του πορτρέτου για τις μικρές θέσεις (aside, σχετικά).
    por = Image.open(IMG / "christina-stamatopoulou.jpg")
    side = min(por.size)
    left = (por.width - side) // 2
    top = round((por.height - side) * 0.06)     # ψηλά: το πρόσωπο είναι στο πάνω τρίτο
    por.crop((left, top, left + side, top + side)).resize((720, 720), Image.LANCZOS).save(
        IMG / "christina-stamatopoulou-sq.jpg", quality=85, optimize=True, progressive=True)
    print("  christina-stamatopoulou-sq.jpg")

    # Λήψη 4:3 του χώρου, για τη σελίδα «Ψυχολόγος Ηλιούπολη».
    g = Image.open(IMG / "grafeio.jpg")
    th = round(g.width * 3 / 4)
    top = max(0, round((g.height - th) * 0.5))
    g.crop((0, top, g.width, min(g.height, top + th))).resize((900, 675), Image.LANCZOS).save(
        IMG / "grafeio-43.jpg", quality=80, optimize=True, progressive=True)
    print("  grafeio-43.jpg")


def crop_ratio(im, ratio, focus=0.5):
    """Περικοπή στο ζητούμενο πλάτος/ύψος, με το θέμα στο `focus` καθ\' ύψος."""
    if im.width / im.height > ratio:                 # πολύ φαρδιά -> κόβουμε πλάγια
        w = round(im.height * ratio)
        left = round((im.width - w) * 0.5)
        return im.crop((left, 0, left + w, im.height))
    h = round(im.width / ratio)                      # πολύ ψηλή -> κόβουμε καθ\' ύψος
    top = round((im.height - h) * focus)
    return im.crop((0, top, im.width, top + h))


def write_service_photos():
    """Δύο μεγέθη ανά υπηρεσία, γιατί η ίδια λήψη παίζει σε δύο θέσεις.

    `…-card.jpg` (720×450) — μέσα στο κουτάκι της υπηρεσίας, όπου η κάρτα δεν
    ξεπερνά τα ~380 CSS px· ένα μεγάλο αρχείο εκεί θα ήταν καθαρή σπατάλη, αφού
    η αρχική δείχνει έξι τέτοιες κάρτες μαζί.

    `….jpg` (1240×775) — στην περιγραφή της αντίστοιχης σελίδας, όπου η εικόνα
    πιάνει όλο το πλάτος της στήλης κειμένου.

    Και τα δύο σε 16:10: αρκετά φαρδύ ώστε να μη σπρώχνει το κείμενο της κάρτας
    κάτω από το πτυσσόμενο, αρκετά ψηλό ώστε να χωρά το θέμα της λήψης.
    """
    for out, cfg in SERVICE_PHOTOS.items():
        base = crop_ratio(Image.open(BASE / cfg["src"]).convert("RGB"), 16 / 10,
                          cfg.get("focus", 0.5))
        sizes = [(out + ".jpg", 1240)]
        if cfg.get("card", True):
            sizes.append((out + "-card.jpg", 720))
        for name, w in sizes:
            im = base.resize((w, round(w * 10 / 16)), Image.LANCZOS)
            im.save(IMG / name, quality=78, optimize=True, progressive=True)
            print(" ", name, im.size, (IMG / name).stat().st_size // 1024, "KB")


def write_cert():
    """Το πιστοποιητικό ραδιαισθησίας, στη σελίδα της αντίστοιχης υπηρεσίας.

    Κάθετο και σε μέτριο πλάτος: εμφανίζεται σε στήλη ~22rem, οπότε τα 760px
    αρκούν και για οθόνες υψηλής πυκνότητας.
    """
    im = Image.open(BASE / CERT_SRC).convert("RGB").crop(CERT_BOX)
    im = im.resize((760, round(760 * im.height / im.width)), Image.LANCZOS)
    im.save(IMG / "cert-radiaisthisia.jpg", quality=80, optimize=True, progressive=True)
    print("  cert-radiaisthisia.jpg", im.size,
          (IMG / "cert-radiaisthisia.jpg").stat().st_size // 1024, "KB")


def write_hero():
    """Το φόντο του hero. Κρατά το 4:3 του πρωτοτύπου και όχι μια φαρδιά
    περικοπή: το CSS το κάνει `object-fit: cover`, οπότε σε στενή οθόνη
    χρειάζεται ύψος για να μη μείνει το κάδρο μισό."""
    p = Image.open(BASE / HERO_SRC).convert("RGB")
    p = p.resize((1440, round(1440 * p.height / p.width)), Image.LANCZOS)
    p.save(IMG / "hero-grafeio.jpg", quality=76, optimize=True, progressive=True)
    print("  hero-grafeio.jpg", p.size, (IMG / "hero-grafeio.jpg").stat().st_size // 1024, "KB")


def write_think_badge():
    """Το σήμα THInK / ThetaHealing Institute of Knowledge, για το footer.

    Η πηγή είναι στιγμιότυπο οθόνης: έχει μια μαύρη μπάρα πάνω αριστερά και
    άγνωστο περιθώριο γύρω από το σήμα. Αντί για καρφωμένες συντεταγμένες —
    που θα έσπαγαν με το πρώτο διαφορετικό στιγμιότυπο — εντοπίζουμε το μελάνι
    και κόβουμε εκεί. Η μπάρα εξαιρείται κοιτάζοντας μόνο κάτω από αυτήν.

    Το λευκό φόντο μένει ψημένο μέσα στην εικόνα: το σήμα είναι σχεδόν μαύρο
    και πάνω στο indigo footer θα χανόταν, οπότε κάθεται σε λευκή κάρτα και
    το CSS απλώς στρογγυλεύει τη γωνία.
    """
    im = Image.open(BASE / THINK_SRC).convert("RGB")
    a = np.asarray(im, np.uint8)
    top = 78                                   # κάτω από τη μαύρη μπάρα
    ink = a[top:665].min(axis=2) < 232
    ys, xs = np.where(ink)
    box = (int(xs.min()), int(ys.min()) + top, int(xs.max()) + 1, int(ys.max()) + top + 1)
    crop = im.crop(box)

    pad = round(crop.width * 0.06)
    canvas = Image.new("RGB", (crop.width + 2 * pad, crop.height + 2 * pad), (255, 255, 255))
    canvas.paste(crop, (pad, pad))

    w = 320                                    # 2× το μέγεθος εμφάνισης στο footer
    out = canvas.resize((w, round(w * canvas.height / canvas.width)), Image.LANCZOS)
    out.save(IMG / "thetahealing-think.png", optimize=True)
    print("  thetahealing-think.png", out.size,
          (IMG / "thetahealing-think.png").stat().st_size // 1024, "KB")


def write_og():
    """Η εικόνα κοινοποίησης: το λογότυπο στο δικό του indigo, όπως το πρωτότυπο."""
    og = Image.new("RGB", (1200, 675), INK)
    # PNG-8 με παλέτα: χρειάζεται ρητή μετατροπή σε RGBA για να δουλέψει ως μάσκα.
    logo = Image.open(IMG / "logo-light.png").convert("RGBA")
    lw = 720
    logo = logo.resize((lw, round(lw * logo.height / logo.width)), Image.LANCZOS)
    og.paste(logo, ((1200 - lw) // 2, (675 - logo.height) // 2 - 18), logo)
    ImageDraw.Draw(og).rectangle([(540, 596), (660, 598)], fill=GOLD)
    og.save(IMG / "og-image.jpg", quality=88, optimize=True, progressive=True)
    print("  og-image.jpg")


if __name__ == "__main__":
    IMG.mkdir(parents=True, exist_ok=True)
    print("λογότυπα:");     write_logos()
    print("φωτογραφίες:");  write_photos()
    print("hero:");         write_hero()
    print("υπηρεσίες:");    write_service_photos()
    print("πιστοποίηση:");  write_think_badge()
    print("δίπλωμα:");      write_cert()
    print("κοινοποίηση:");  write_og()
