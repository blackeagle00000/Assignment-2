import pygame as pg
import os

# piece asset folder
IMAGE_FOLDER = "assets"

# piece to image
PIECE_FILES = {
    "bq": "bq.png",
    "bk": "bk.png",
    "br": "br.png",
    "bb": "bb.png",
    "bn": "bn.png",
    "bp": "bp.png",
    "wq": "wq.png",
    "wk": "wk.png",
    "wr": "wr.png",
    "wb": "wb.png",
    "wn": "wn.png",
    "wp": "wp.png",
}


def load_pieces():
    pieces = {}
    for code, filename in PIECE_FILES.items():
        path = os.path.join(IMAGE_FOLDER, filename)
        if not os.path.exists(path):
            print(f"Missing: {path}")
            continue

        img = pg.image.load(path)

        if code.endswith("p"):
            normal = pg.transform.scale(img, (65, 65))
        else:
            normal = pg.transform.scale(img, (80, 80))

        pieces[code] = normal
    return pieces


def load_small_pieces():
    small_pieces = {}
    for code, filename in PIECE_FILES.items():
        path = os.path.join(IMAGE_FOLDER, filename)
        if not os.path.exists(path):
            continue

        img = pg.image.load(path)
        small = pg.transform.scale(img, (45, 45))
        small_pieces[code] = small
    return small_pieces
