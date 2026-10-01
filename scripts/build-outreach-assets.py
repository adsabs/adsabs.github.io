"""Rebuild the outreach page artwork from Yueyi Che's source files.

Run this when the source designs change. SRC points at the shared swag
folder, which is not in the repository; only the generated web assets are
committed. Requires Pillow.
"""
from PIL import Image
import os

SRC = "/Users/mugdhapolimera/Downloads/Swag Designs 2026 - non disciplinary"
SQ  = os.path.join(SRC, "Square_Originals")
OUT = "/Users/mugdhapolimera/github/adsabs.github.io/help/img/outreach"

def square_center(im):
    w, h = im.size
    s = min(w, h)
    return im.crop(((w-s)//2, (h-s)//2, (w-s)//2+s, (h-s)//2+s))

# --- honeycomb tiles -------------------------------------------------
tiles = [
    ("astro",     "Sticker_Astrophysics_sqr.png"),
    ("planetary", "Sticker_Planetary_sqr.png"),
    ("together",  "Sticker_Center_Clean_sqr.png"),
    ("earth",     "Sticker_EarthScience_sqr.png"),
    ("bio",       "Sticker_Bio_sar.png"),
    ("ocean",     "Ocean.png"),
    ("astrobio",  "Astrobio.png"),
]
for name, fn in tiles:
    im = Image.open(os.path.join(SQ, fn)).convert("RGB")
    im = square_center(im).resize((900, 900), Image.LANCZOS)
    p = os.path.join(OUT, "hex", f"{name}.jpg")
    im.save(p, "JPEG", quality=86, optimize=True, progressive=True)
    print(f"  hex/{name}.jpg  {os.path.getsize(p)//1024} KB")

# Heliophysics is a special case. The square sticker carries the words
# "I am a heliophysicist" burned into the art, so the tile comes from the round
# version instead. That one has transparent corners, so it is scaled up until
# the hexagon sits wholly inside the circle: the hexagon's farthest vertex is
# at 1.118r, and 1.15 leaves a margin.
helio = Image.open(os.path.join(SRC, "IMG_4750.PNG")).convert("RGB")
w, h = helio.size
up = int(min(w, h) * 1.15)
helio = helio.resize((up, up), Image.LANCZOS)
helio = helio.crop(((up-w)//2, (up-h)//2, (up-w)//2+w, (up-h)//2+h)).resize((900, 900), Image.LANCZOS)
p = os.path.join(OUT, "hex", "helio.jpg")
helio.save(p, "JPEG", quality=86, optimize=True, progressive=True)
print(f"  hex/helio.jpg  {os.path.getsize(p)//1024} KB  (text-free round source)")

# --- zine spreads ----------------------------------------------------
# Each booklet is one sheet folded into 8 pages: a 4x2 grid with the top row
# printed upside down. Reading order is
#   p1 bottom col 1, p2 bottom col 2, p3 bottom col 3,
#   p4 top col 3,    p5 top col 2,    p6 top col 1,   p7 top col 0,
#   p8 bottom col 0.
#
# Pages 2-3, 4-5 and 6-7 are FACING pages once the booklet is open, and the
# artist let lettering run across those gutters. So each spread is cropped as
# a single uncut block rather than as two panels stuck back together. That is
# why nothing is clipped: the only cuts are at x=825 and x=1650, where real
# page edges fall.
#
# Output per booklet: cover, three spreads, back cover.
VIEWS = [
    ("1", "b", 1, 2, False),   # front cover, one page
    ("2", "b", 2, 4, False),   # pages 2 and 3
    ("3", "t", 2, 4, True),    # pages 4 and 5, printed upside down
    ("4", "t", 0, 2, True),    # pages 6 and 7, printed upside down
    ("5", "b", 0, 1, False),   # back cover, one page
]

for n in (1, 2):
    sheet = Image.open(os.path.join(SRC, f"SciX_Booklet_{n}.png")).convert("RGB")
    W, H = sheet.size
    cw, ch = W // 4, H // 2
    for label, row, col_from, col_to, flip in VIEWS:
        top = 0 if row == "t" else ch
        view = sheet.crop((col_from*cw, top, col_to*cw, top + ch))
        if flip:
            view = view.rotate(180)
        view = view.resize((view.width//2, view.height//2), Image.LANCZOS)
        p_out = os.path.join(OUT, f"zine-{n}-{label}.jpg")
        view.save(p_out, "JPEG", quality=85, optimize=True, progressive=True)
        print(f"  zine-{n}-{label}.jpg  {view.size}  {os.path.getsize(p_out)//1024} KB")
