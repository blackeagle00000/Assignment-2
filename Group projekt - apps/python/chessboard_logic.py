import pygame

WHITE = (255, 255, 255)
BLACK = (128, 128, 128)

def draw_board(surface, top_left, board_px, squares=8):
    """Draw a chessboard of size squares x squares"""
    x0, y0 = top_left
    square = board_px // squares
    for r in range(squares):
        for c in range(squares):
            color = WHITE if (r + c) % 2 == 0 else BLACK
            rect = pygame.Rect(x0 + c * square, y0 + r * square, square, square)
            pygame.draw.rect(surface, color, rect)
