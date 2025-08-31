import pygame as pg
import sys
from chessboard_logic import draw_board
from pieces import load_pieces
from game_logic import ChessGame
from key_logic import handle_mouse, handle_keys

WINDOW_SIZE = 640
BOARD_SIZE = 8
BG = (30, 30, 30)

def main():
    pg.init()
    screen = pg.display.set_mode((WINDOW_SIZE, WINDOW_SIZE))
    pg.display.set_caption("Modular Chess Game")
    clock = pg.time.Clock()

    margin = 20
    board_px = WINDOW_SIZE - margin * 2
    top_left = (margin, margin)

    pieces, _ = load_pieces()
    game = ChessGame(pieces, top_left, board_px, BOARD_SIZE)

    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                sys.exit()
            if event.type == pg.MOUSEBUTTONDOWN:
                handle_mouse(game, event.pos)
            if event.type == pg.KEYDOWN:
                handle_keys(game, event.key)

        screen.fill(BG)
        draw_board(screen, top_left, board_px, BOARD_SIZE)
        game.draw(screen)

        pg.display.flip()
        clock.tick(60)

if __name__ == "__main__":
    main()
