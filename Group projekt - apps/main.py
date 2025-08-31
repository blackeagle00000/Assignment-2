import pygame as pg
import sys
from game_logic import create_board, get_piece_moves
from pieces import load_pieces, load_small_pieces
from input_logic import handle_mouse, handle_keys, get_highlights
from chessboard_logic import draw_board, draw_captures

WINDOW_SIZE = 800   # window size
BOARD_SIZE = 8
BG = (30, 30, 30)

class Game:
    def __init__(self, board, squares, top_left, board_px):
        self.board = board
        self.squares = squares
        self.top_left = top_left
        self.board_px = board_px
        self.selected = None
        self.selector = [0, 0]
        self.turn = "w"         # "w" start

        # captured pieces tracking
        self.captured_white = []  # captured black pieces
        self.captured_black = []  # captured white pieces

    def select_square(self, r, c):
        from game_logic import get_piece_moves 

        if self.selected:
            sr, sc = self.selected
            piece = self.board[sr][sc]

            if not piece or piece[0] != self.turn:
                self.selected = None
                return None

            moves, captures, blocked = get_piece_moves(self.board, sr, sc)

            if (r, c) in moves or (r, c) in captures:

                if self.board[r][c]:
                    cap_color, cap_type = self.board[r][c]
                    code = ("w" if cap_color == "w" else "b") + cap_type[0]
                    if cap_color == "w":
                        self.captured_black.append(code)
                    else:
                        self.captured_white.append(code)


                    if cap_type == "king":
                        winner = "White" if self.turn == "w" else "Black"
                        self.board[r][c] = self.board[sr][sc]
                        self.board[sr][sc] = None
                        return winner

                self.board[r][c] = self.board[sr][sc]
                self.board[sr][sc] = None

                self.turn = "b" if self.turn == "w" else "w"

            self.selected = None
        else:
            if self.board[r][c] and self.board[r][c][0] == self.turn:
                self.selected = (r, c)

        return None

def end_game(screen, winner):
    font = pg.font.SysFont(None, 60)
    small_font = pg.font.SysFont(None, 40)

    text = font.render(f"{winner} Wins! King Captured!", True, (255, 255, 255))
    replay_text = small_font.render("Press R to Replay or Q to Quit", True, (200, 200, 200))

    screen.fill((0, 0, 0))
    screen.blit(text, (WINDOW_SIZE//2 - text.get_width()//2, WINDOW_SIZE//3))
    screen.blit(replay_text, (WINDOW_SIZE//2 - replay_text.get_width()//2, WINDOW_SIZE//2))
    pg.display.flip()

    waiting = True
    while waiting:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                sys.exit()
            elif event.type == pg.KEYDOWN:
                if event.key == pg.K_q:
                    pg.quit()
                    sys.exit()
                elif event.key == pg.K_r:
                    waiting = False


def main():
    pg.init()
    screen = pg.display.set_mode((WINDOW_SIZE, WINDOW_SIZE))
    pg.display.set_caption("Chess Game Modular")
    clock = pg.time.Clock()

    board_px = 640
    margin_bottom = 20

    top_left_x = (WINDOW_SIZE - board_px) // 2
    top_left_y = WINDOW_SIZE - board_px - margin_bottom
    top_left = (top_left_x, top_left_y)


    pieces = load_pieces()
    small_pieces = load_small_pieces()

    board = create_board()
    game = Game(board, BOARD_SIZE, top_left, board_px)

    running = True

    while running:
        winner = None
        for event in pg.event.get():
            if event.type == pg.QUIT:
                running = False
            elif event.type == pg.MOUSEBUTTONDOWN:
                winner = handle_mouse(game, pg.mouse.get_pos())
            elif event.type == pg.KEYDOWN:
                winner = handle_keys(game, event.key)

        if winner:
            end_game(screen, winner)
            board = create_board()
            game = Game(board, BOARD_SIZE, top_left, board_px)
            continue

        highlights, cursor = get_highlights(game)

        screen.fill(BG)
        draw_board(screen, top_left, board_px, BOARD_SIZE)

        square_size = board_px // BOARD_SIZE
        for color_name in highlights:
            color_map = {"yellow": (255, 255, 0),
                         "green": (0, 255, 0),
                         "red": (255, 0, 0),
                         "blue": (0, 0, 255)}
            for r, c in highlights[color_name]:
                pg.draw.rect(screen, color_map[color_name],
                             (top_left[0] + c*square_size, top_left[1] + r*square_size,
                              square_size, square_size), 4)

        cr, cc = cursor
        pg.draw.rect(screen, (200, 200, 0),
                     (top_left[0] + cc*square_size, top_left[1] + cr*square_size,
                      square_size, square_size), 2)

        for r in range(BOARD_SIZE):
            for c in range(BOARD_SIZE):
                if game.board[r][c]:
                    color, ptype = game.board[r][c]
                    piece_map = {
                        "rook": "r",
                        "knight": "n",
                        "bishop": "b",
                        "queen": "q",
                        "king": "k",
                        "pawn": "p"
                    }
                    code = ("w" if color == "w" else "b") + piece_map[ptype]
                    if code in pieces:
                        screen.blit(pieces[code],
                                    (top_left[0] + c*square_size, top_left[1] + r*square_size))

        draw_captures(screen, small_pieces, game.captured_white, game.captured_black, board_px, WINDOW_SIZE)

        pg.display.flip()
        clock.tick(60)

    pg.quit()
    sys.exit()


if __name__ == "__main__":
    main()