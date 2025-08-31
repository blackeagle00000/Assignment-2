import pygame as pg

# Mapping piece names to filenames
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
    """Load all piece images (normal + small) and return dicts."""
    pieces = {}
    small_pieces = {}

    for code, filename in PIECE_FILES.items():
        # Load image
        img = pg.image.load(f"assets/{filename}")

        # Scale by piece type
        if code.endswith("p"):   # pawns
            normal = pg.transform.scale(img, (65, 65))
        else:
            normal = pg.transform.scale(img, (80, 80))

        small = pg.transform.scale(normal, (45, 45))

        pieces[code] = normal
        small_pieces[code] = small

    return pieces, small_pieces
