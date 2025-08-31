import pygame as pg
import os

BOARD_SIZE = 8
SQUARE_SIZE = 80
IMAGE_FOLDER = "images"

# starting position
STARTING_POSITIONS = {
    "br": [(0, 0), (0, 7)],
    "bn": [(0, 1), (0, 6)],
    "bb": [(0, 2), (0, 5)],
    "bq": [(0, 3)],
    "bk": [(0, 4)],
    "bp": [(1, c) for c in range(8)],

    "wr": [(7, 0), (7, 7)],
    "wn": [(7, 1), (7, 6)],
    "wb": [(7, 2), (7, 5)],
    "wq": [(7, 3)],
    "wk": [(7, 4)],
    "wp": [(6, c) for c in range(8)],
}


def load_pieces():
    pieces = {}
    for color in ["w", "b"]:
        for piece in ["r", "n", "b", "q", "k", "p"]:
            code = color + piece
            path = os.path.join(IMAGE_FOLDER, code + ".png")
            if not os.path.exists(path):
                print(f"Missing: {path}")
                continue
            image = pg.image.load(path)
            image = pg.transform.scale(image, (SQUARE_SIZE, SQUARE_SIZE))
            pieces[code] = image
    return pieces


def load_small_pieces():
    small_pieces = {}
    for color in ["w", "b"]:
        for piece in ["r", "n", "b", "q", "k", "p"]:
            code = color + piece
            path = os.path.join(IMAGE_FOLDER, code + ".png")
            if not os.path.exists(path):
                continue
            image = pg.image.load(path)
            image = pg.transform.scale(image, (45, 45))
            small_pieces[code] = image
    return small_pieces


def create_board():
    board = [[None for _ in range(BOARD_SIZE)] for _ in range(BOARD_SIZE)]
    for code, positions in STARTING_POSITIONS.items():
        for r, c in positions:
            color = "w" if code[0] == "w" else "b"
            piece_type = {
                "r": "rook", "n": "knight", "b": "bishop",
                "q": "queen", "k": "king", "p": "pawn"
            }[code[1]]
            board[r][c] = (color, piece_type)
    return board
