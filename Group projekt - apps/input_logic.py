import pygame as pg
from game_logic import get_piece_moves

def handle_mouse(game, pos):
    x0, y0 = game.top_left
    square_size = game.board_px // game.squares
    mx, my = pos
    col = (mx - x0) // square_size
    row = (my - y0) // square_size

    if 0 <= row < game.squares and 0 <= col < game.squares:
        # winner capture
        winner = game.select_square(row, col)
        return winner
    return None

def handle_keys(game, key):
    if key == pg.K_UP and game.selector[0] > 0:
        game.selector[0] -= 1
    elif key == pg.K_DOWN and game.selector[0] < game.squares - 1:
        game.selector[0] += 1
    elif key == pg.K_LEFT and game.selector[1] > 0:
        game.selector[1] -= 1
    elif key == pg.K_RIGHT and game.selector[1] < game.squares - 1:
        game.selector[1] += 1
    elif key == pg.K_RETURN:
        row, col = game.selector
        winner = game.select_square(row, col)  # capture winner
        return winner
    return None

def get_highlights(game):
    """
    Returns (highlights dict, cursor position)
    highlights dict contains: yellow (selected), green (moves),
    red (captures), blue (blocked)
    """
    highlights = {"yellow": [], "green": [], "red": [], "blue": []}

    if game.selected:
        r, c = game.selected
        highlights["yellow"].append((r, c))
        moves, captures, blocked = get_piece_moves(game.board, r, c)
        highlights["green"].extend(moves)
        highlights["red"].extend(captures)
        highlights["blue"].extend(blocked)

    return highlights, game.selector  # ✅ matches main.py
