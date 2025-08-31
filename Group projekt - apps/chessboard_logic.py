import pygame

WHITE = (255, 255, 255)
BLACK = (128, 128, 128)


def draw_board(surface, top_left, board_px, squares=8):
    x0, y0 = top_left
    square = board_px // squares
    for r in range(squares):
        for c in range(squares):
            color = WHITE if (r + c) % 2 == 0 else BLACK
            rect = pygame.Rect(x0 + c * square, y0 + r * square, square, square)
            pygame.draw.rect(surface, color, rect)


def draw_captures(surface, small_pieces, captured_white, captured_black, board_px, window_size):
    # Left side ma black piece
    x_left = 10
    y = 10
    for code in captured_white:
        surface.blit(small_pieces[code], (x_left, y))
        y += 50

    # Right side ma white piece
    x_right = window_size - 55  # 45 + 10 ko margin
    y = 10
    for code in captured_black:
        surface.blit(small_pieces[code], (x_right, y))
        y += 50
