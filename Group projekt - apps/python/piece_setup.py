import pygame as pg

# Mapping of starting positions (row, col)
# Top of board (row=0) = Black pieces, Bottom (row=7) = White pieces
STARTING_POSITIONS = {
    # Black pieces
    "br": [(0, 0), (0, 7)],
    "bn": [(0, 1), (0, 6)],
    "bb": [(0, 2), (0, 5)],
    "bq": [(0, 3)],
    "bk": [(0, 4)],
    "bp": [(1, c) for c in range(8)],

    # White pieces
    "wr": [(7, 0), (7, 7)],
    "wn": [(7, 1), (7, 6)],
    "wb": [(7, 2), (7, 5)],
    "wq": [(7, 3)],
    "wk": [(7, 4)],
    "wp": [(6, c) for c in range(8)],
}

def draw_starting_pieces(surface, pieces, top_left, board_px, squares=8):
    """Draw all pieces in their starting positions."""
    square_size = board_px // squares
    x0, y0 = top_left

    for code, positions in STARTING_POSITIONS.items():
        for (row, col) in positions:
            x = x0 + col * square_size
            y = y0 + row * square_size
            surface.blit(pieces[code], (x, y))
