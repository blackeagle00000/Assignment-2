import pygame as pg
from piece_setup import STARTING_POSITIONS

class ChessGame:
    def __init__(self, pieces, top_left, board_px, squares=8):
        self.pieces = pieces
        self.top_left = top_left
        self.board_px = board_px
        self.squares = squares

        # Build board (8x8 with piece codes)
        self.board = [[None for _ in range(squares)] for _ in range(squares)]
        for code, positions in STARTING_POSITIONS.items():
            for (r, c) in positions:
                self.board[r][c] = code

        self.selected = None
        self.possible_moves = []
        self.selector = [0, 0]

    def draw(self, surface):
        square_size = self.board_px // self.squares
        x0, y0 = self.top_left

        # Draw all pieces
        for r in range(self.squares):
            for c in range(self.squares):
                code = self.board[r][c]
                if code:
                    x = x0 + c * square_size
                    y = y0 + r * square_size
                    surface.blit(self.pieces[code], (x, y))

        # Highlight possible moves (red)
        for (r, c) in self.possible_moves:
            rect = pg.Rect(
                x0 + c * square_size, y0 + r * square_size,
                square_size, square_size
            )
            pg.draw.rect(surface, (255, 0, 0), rect, 3)

        # Highlight selector (yellow)
        sr, sc = self.selector
        rect = pg.Rect(
            x0 + sc * square_size, y0 + sr * square_size,
            square_size, square_size
        )
        pg.draw.rect(surface, (255, 255, 0), rect, 2)

    def select_square(self, row, col):
        if self.selected:
            if (row, col) in self.possible_moves:
                self.move_piece(self.selected, (row, col))
            self.selected = None
            self.possible_moves = []
        else:
            if self.board[row][col]:
                self.selected = (row, col)
                self.possible_moves = self.generate_moves(row, col)

    def move_piece(self, src, dst):
        sr, sc = src
        dr, dc = dst
        self.board[dr][dc] = self.board[sr][sc]
        self.board[sr][sc] = None

    def generate_moves(self, row, col):
        # Simple placeholder: highlight 1-step moves (rook-style)
        moves = []
        for dr, dc in [(-1,0),(1,0),(0,-1),(0,1)]:
            nr, nc = row + dr, col + dc
            if 0 <= nr < self.squares and 0 <= nc < self.squares:
                moves.append((nr, nc))
        return moves
