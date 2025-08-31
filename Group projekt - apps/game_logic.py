# game_logic.py
import pygame as pg

ROWS, COLS = 8, 8

#  highlight color
YELLOW = (255, 255, 0)    # select
GREEN = (0, 255, 0)       # empty
RED = (255, 0, 0)         # captured
BLUE = (0, 0, 255)        # blocked

# piece as tuples: (color & type)
# color = "w" or "b"
# type = pawn, rook, knight, bishop, queen, king

def create_board():
    board = [[None for _ in range(COLS)] for _ in range(ROWS)]

    # Black
    board[0] = [
        ("b", "rook"), ("b", "knight"), ("b", "bishop"), ("b", "queen"),
        ("b", "king"), ("b", "bishop"), ("b", "knight"), ("b", "rook")
    ]
    board[1] = [("b", "pawn") for _ in range(COLS)]

    # White
    board[6] = [("w", "pawn") for _ in range(COLS)]
    board[7] = [
        ("w", "rook"), ("w", "knight"), ("w", "bishop"), ("w", "queen"),
        ("w", "king"), ("w", "bishop"), ("w", "knight"), ("w", "rook")
    ]

    return board


def inside_board(r, c):
    return 0 <= r < ROWS and 0 <= c < COLS


def get_piece_moves(board, row, col):
    piece = board[row][col]
    if not piece:
        return [], [], []

    color, p_type = piece
    moves, captures, blocked = [], [], []

    directions = []

    if p_type == "pawn":
        direction = -1 if color == "w" else 1
        start_row = 6 if color == "w" else 1

        # fwd move
        if inside_board(row + direction, col) and board[row + direction][col] is None:
            moves.append((row + direction, col))
            # Double move
            if row == start_row and board[row + 2*direction][col] is None:
                moves.append((row + 2*direction, col))

        # capture
        for dc in [-1, 1]:
            nr, nc = row + direction, col + dc
            if inside_board(nr, nc):
                if board[nr][nc] and board[nr][nc][0] != color:
                    captures.append((nr, nc))
                elif board[nr][nc] and board[nr][nc][0] == color:
                    blocked.append((nr, nc))

    elif p_type == "rook":
        directions = [(1,0), (-1,0), (0,1), (0,-1)]
    elif p_type == "bishop":
        directions = [(1,1), (1,-1), (-1,1), (-1,-1)]
    elif p_type == "queen":
        directions = [(1,0), (-1,0), (0,1), (0,-1), (1,1), (1,-1), (-1,1), (-1,-1)]
    elif p_type == "king":
        for dr in [-1,0,1]:
            for dc in [-1,0,1]:
                if dr == 0 and dc == 0: continue
                nr, nc = row+dr, col+dc
                if inside_board(nr, nc):
                    if board[nr][nc] is None:
                        moves.append((nr,nc))
                    elif board[nr][nc][0] != color:
                        captures.append((nr,nc))
                    else:
                        blocked.append((nr,nc))
    elif p_type == "knight":
        knight_moves = [(2,1),(2,-1),(-2,1),(-2,-1),(1,2),(1,-2),(-1,2),(-1,-2)]
        for dr,dc in knight_moves:
            nr, nc = row+dr, col+dc
            if inside_board(nr,nc):
                if board[nr][nc] is None:
                    moves.append((nr,nc))
                elif board[nr][nc][0] != color:
                    captures.append((nr,nc))
                else:
                    blocked.append((nr,nc))

    # line pieces
    if directions:
        for dr, dc in directions:
            nr, nc = row+dr, col+dc
            while inside_board(nr,nc):
                if board[nr][nc] is None:
                    moves.append((nr,nc))
                elif board[nr][nc][0] != color:
                    captures.append((nr,nc))
                    break
                else:
                    blocked.append((nr,nc))
                    break
                nr += dr
                nc += dc

    return moves, captures, blocked
