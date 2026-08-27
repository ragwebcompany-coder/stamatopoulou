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


def to_rgba(rgb, alpha, mono=False):
    """Πίνακες -> εικόνα RGBA. Με mono=True, όλο το μελάνι γίνεται indigo."""
    h, w = alpha.shape
    out = np.zeros((h, w, 4), np.uint8)
    if mono:
        out[..., :3] = INK
        # Το άνθος έχει εσωτερικές λεπτομέρειες που, μονόχρωμες, γίνονται
        # μουτζούρα. Τις ανοίγουμε: όσο πιο σκούρο ήταν το pixel στο πρωτότυπο
        # (δηλαδή όσο πιο κοντά στο φόντο), τόσο πιο διάφανο γίνεται εδώ.
        lum = rgb.mean(axis=2) / 255.0
        alpha = np.clip(alpha * (0.35 + 0.85 * lum), 0, 1)
    else:
        out[..., :3] = np.clip(rgb, 0, 255).astype(np.uint8)
    out[..., 3] = (alpha * 255).astype(np.uint8)
    return Image.fromarray(out, "RGBA")


def save_png8(im, name):
    """PNG-8 με παλέτα και διαφάνεια.

    Το FASTOCTREE είναι ο μόνος αλγόριθμος του Pillow που κβαντίζει RGBA
    κρατώντας το alpha, και ρίχνει το αρχείο από ~200 KB σε ~30 KB χωρίς ορατή
    διαφορά σε λογότυπο με λίγα χρώματα.
    """
    im.quantize(colors=64, method=Image.FASTOCTREE).save(IMG / name, optimize=True)
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

    Γιατί μονόχρωμο στο header: το πρωτότυπο μελάνι είναι *ανοιχτό* πάνω σε
    σκούρο. Πάνω σε λευκό είτε θα εξαφανιζόταν, είτε θα έπρεπε να αντιστραφεί
    η εσωτερική σκίαση του άνθους — που το αλλοιώνει. Μια καθαρή εκδοχή ενός
    χρώματος κρατά το σχήμα ακέραιο.
    """
    # ---- κάθετο, πολύχρωμο: footer & og ------------------------------------
    rgb, alpha = cutout(LOGO_BOX)
    im = to_rgba(rgb, alpha)
    save_png8(im.resize((OUT_W, round(OUT_W * im.height / im.width)), Image.LANCZOS),
              "logo-light.png")

    # ---- οριζόντιο, μονόχρωμο: header --------------------------------------
    flower = to_rgba(*cutout(FLOWER_BOX), mono=True)
    text = to_rgba(*cutout(TEXT_BOX), mono=True)

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
    print("κοινοποίηση:");  write_og()
