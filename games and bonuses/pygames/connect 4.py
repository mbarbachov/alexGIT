import numpy as np
import pygame
import sys
import math

Blue = (0, 0, 255)
black = (0, 0, 0)
red = (255, 0, 0)
yellow = (255, 255, 0)

row_count = 6
column_count = 7


def create_board():
    board = np.zeros((row_count, column_count))
    return board


def drop_piece(board, row, col, piece):
    board[row][col] = piece


def is_valid_location(board, col):
    return board[row_count - 1][col] == 0


def get_next_open_row(board, col):
    for r in range(row_count):
        if board[r][col] == 0:
            return r


def print_board(board):
    print(np.flip(board, 0))


def winning_move(board, piece):
    # check horizontal location for win
    for c in range(column_count - 3):
        for r in range(row_count):
            if board[r][c] == piece and board[r][c + 1] == piece and board[r][c + 2] == piece and board[r][
                c + 3] == piece:
                return True
    for c in range(column_count):
        for r in range(row_count - 3):
            if board[r][c] == piece and board[r + 1][c] == piece and board[r + 2][c] == piece and board[r + 3][
                c] == piece:
                return True
    # check for positively sloped diagonals
    for c in range(column_count - 3):
        for r in range(row_count - 3):
            if board[r][c] == piece and board[r + 1][c + 1] == piece and board[r + 2][c + 2] == piece and board[r + 3][
                c + 3] == piece:
                return True

    # check for negatively sloped diagonals
    for c in range(column_count - 3):
        for r in range(3, row_count):
            if board[r][c] == piece and board[r - 1][c + 1] == piece and board[r - 2][c + 2] == piece and board[r - 3][
                c + 3] == piece:
                return True


def draw_board(board):
    for c in range(column_count):
        for r in range(row_count):
            for i in range(4):
                pygame.draw.rect(screen, Blue, (c * SQUARESIZE, r * SQUARESIZE + SQUARESIZE, SQUARESIZE, SQUARESIZE))
                pygame.draw.circle(screen, black, (
                    int(c * SQUARESIZE + SQUARESIZE / 2), (r * SQUARESIZE + SQUARESIZE + SQUARESIZE / 2)), radius)

    for c in range(column_count):
        for r in range(row_count):
            for i in range(4):
                if board[r][c] == 1:
                    pygame.draw.circle(screen, red, (
                        int(c * SQUARESIZE + SQUARESIZE / 2), height - int(r * SQUARESIZE + SQUARESIZE / 2)), radius)
                elif board[r][c] == 2:
                    pygame.draw.circle(screen, yellow, (
                        int(c * SQUARESIZE + SQUARESIZE / 2), height - int(r * SQUARESIZE + SQUARESIZE / 2)), radius)
    pygame.display.update()


game_over = False
board = create_board()
turn = 0

pygame.init()

SQUARESIZE = 100

width = (column_count + 1) * SQUARESIZE
height = (row_count + 1) * SQUARESIZE

radius = int(SQUARESIZE / 2 - 5)

size = (width, height)
screen = pygame.display.set_mode(size)
draw_board(board)
pygame.display.update()

my_font = pygame.font.SysFont("monospace", 75)

while not game_over:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        if event.type == pygame.MOUSEMOTION:
            pygame.draw.rect(screen, black, (0, 0, width, SQUARESIZE))
            pos_x = event.pos[0]
            if turn == 0:
                pygame.draw.circle(screen, red, (pos_x, int(SQUARESIZE / 2)), radius)
            else:
                pygame.draw.circle(screen, yellow, (pos_x, int(SQUARESIZE / 2)), radius)
        pygame.display.update()

        if event.type == pygame.MOUSEBUTTONDOWN:
            # print(event.pos)

            if turn == 0:
                pos_x = event.pos[0]
                col = int(math.floor(pos_x / SQUARESIZE))
                if is_valid_location(board, col):
                    row = get_next_open_row(board, col)
                    drop_piece(board, row, col, 1)

                    if winning_move(board, 1):
                        pygame.draw.rect(screen, black, (0, 0, width, SQUARESIZE))
                        label = my_font.render("Player 1 Wins!!", True, red)
                        screen.blit(label, (200, 10))
                        pygame.display.update()
                        game_over = True
            else:
                pos_x = event.pos[0]
                col = int(math.floor(pos_x / SQUARESIZE))
                if is_valid_location(board, col):
                    row = get_next_open_row(board, col)
                    drop_piece(board, row, col, 2)

                    if winning_move(board, 2):
                        pygame.draw.rect(screen, black, (0, 0, width, SQUARESIZE))
                        label = my_font.render("Player 2 Wins!!", True, yellow)
                        screen.blit(label, (200, 10))
                        pygame.display.update()
                        game_over = True

            draw_board(board)
            turn += 1
            turn = turn % 2
    if game_over is True:
        pygame.time.wait(3000)
        break
