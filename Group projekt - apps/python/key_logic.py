import pygame as pg

def handle_mouse(game, pos):
    x0, y0 = game.top_left
    square_size = game.board_px // game.squares
    mx, my = pos
    col = (mx - x0) // square_size
    row = (my - y0) // square_size

    if 0 <= row < game.squares and 0 <= col < game.squares:
        game.select_square(row, col)

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
        game.select_square(row, col)
