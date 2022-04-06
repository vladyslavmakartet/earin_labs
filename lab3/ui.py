# TODO
# split code ?
# add sounds and menu ?


# Currently it is possible to play pvp, player vs ai, player vs smart ai 
import copy
import random
import sys
import pygame
import numpy

from constants import *
from ai import AI


class Board:
    def __init__(self, screen):
        self.squares = numpy.zeros((ROWS, COLS))  # initialize board with zeros
        self.empty_squares = self.squares  # list of empty squares
        self.marked_squares = 0  # number of marked squares
        self.screen = screen
        # print(self.squares)

    def __deepcopy__(self, memo):
        copy_board = Board(self.screen)
        copy_board.squares = copy.deepcopy(self.squares, memo)
        copy_board.empty_squares = copy.deepcopy(self.empty_squares, memo)
        copy_board.marked_squares = copy.deepcopy(self.marked_squares, memo)
        return copy_board

    # returns 0 if no win yet, 1 if player1 wins, 2 if player2 wins
    def final_state(self, show=False):
        # vertical wins
        for col in range(COLS):
            if self.squares[0][col] == self.squares[1][col] == self.squares[2][col] != 0:
                if show:
                    color = CIRC_COLOR if self.squares[0][col] == 2 else CROSS_COLOR
                    iPos = (col * SQSIZE + SQSIZE // 2, 20)
                    fPos = (col * SQSIZE + SQSIZE // 2, HEIGHT - 20)
                    pygame.draw.line(self.screen, color, iPos, fPos, LINE_WIDTH)
                return self.squares[0][col]

        # horizontal wins
        for row in range(ROWS):
            if self.squares[row][0] == self.squares[row][1] == self.squares[row][2] != 0:
                if show:
                    color = CIRC_COLOR if self.squares[row][0] == 2 else CROSS_COLOR
                    iPos = (20, row * SQSIZE + SQSIZE // 2)
                    fPos = (WIDTH - 20, row * SQSIZE + SQSIZE // 2)
                    pygame.draw.line(self.screen, color, iPos, fPos, LINE_WIDTH)
                return self.squares[row][0]

        # desc diagonal
        if self.squares[0][0] == self.squares[1][1] == self.squares[2][2] != 0:
            if show:
                color = CIRC_COLOR if self.squares[1][1] == 2 else CROSS_COLOR
                iPos = (20, 20)
                fPos = (WIDTH - 20, HEIGHT - 20)
                pygame.draw.line(self.screen, color, iPos, fPos, CROSS_WIDTH)
            return self.squares[1][1]

        # asc diagonal
        if self.squares[2][0] == self.squares[1][1] == self.squares[0][2] != 0:
            if show:
                color = CIRC_COLOR if self.squares[1][1] == 2 else CROSS_COLOR
                iPos = (20, HEIGHT - 20)
                fPos = (WIDTH - 20, 20)
                pygame.draw.line(self.screen, color, iPos, fPos, CROSS_WIDTH)
            return self.squares[1][1]

        # no win yet
        return 0

    # mark square with player's number
    def mark_square(self, row, col, player):
        self.squares[row][col] = player
        self.marked_squares += 1

    # check if the square at (row, col) is empty
    def empty_square(self, row, col):
        return self.squares[row][col] == 0

    def get_empty_squares(self):
        empty_squares = []
        for row in range(ROWS):
            for col in range(COLS):
                if self.empty_square(row, col):
                    empty_squares.append((row, col))
        return empty_squares

    def isFull(self):
        return self.marked_squares == 9

    def isEmpty(self):
        return self.marked_squares == 0

class Game:
    def __init__(self, screen, player=2):
        self.screen = screen
        self.board = Board(self.screen)
        self.player = player  # initial player to mark the square, player1 = cross, player2 = circle
        self.running = True
        self.ai = AI()
        self.draw_lines()

    def draw_lines(self):
        self.screen.fill(BG_COLOR)
        # Vertical
        pygame.draw.line(self.screen, LINE_COLOR, (SQSIZE, 0),
                         (SQSIZE, HEIGHT), LINE_WIDTH)
        pygame.draw.line(self.screen, LINE_COLOR, (WIDTH - SQSIZE, 0),
                         (WIDTH - SQSIZE, HEIGHT), LINE_WIDTH)

        # Horizontal
        pygame.draw.line(self.screen, LINE_COLOR, (0, SQSIZE),
                         (WIDTH, SQSIZE), LINE_WIDTH)
        pygame.draw.line(self.screen, LINE_COLOR, (0, HEIGHT - SQSIZE),
                         (WIDTH, HEIGHT - SQSIZE), LINE_WIDTH)

    def draw_figure(self, row, col):
        # draw cross
        if self.player == 1:
            # draw desc line
            start_desc = (col * SQSIZE + OFFSET, row * SQSIZE + OFFSET)
            end_desc = (col * SQSIZE + SQSIZE - OFFSET,
                        row * SQSIZE + SQSIZE - OFFSET)
            pygame.draw.line(self.screen, CROSS_COLOR, start_desc,
                             end_desc, CROSS_WIDTH)
            # draw asc line
            start_asc = (col * SQSIZE + OFFSET, row * SQSIZE + SQSIZE - OFFSET)
            end_asc = (col * SQSIZE + SQSIZE - OFFSET, row * SQSIZE + OFFSET)
            pygame.draw.line(self.screen, CROSS_COLOR, start_asc,
                             end_asc, CROSS_WIDTH)
        # draw cirle
        elif self.player == 2:
            center = (col * SQSIZE + SQSIZE // 2, row * SQSIZE + SQSIZE // 2)
            pygame.draw.circle(self.screen, CIRC_COLOR, center, RADIUS, CIRC_WIDTH)

    def make_move(self, row, col):
        self.board.mark_square(row, col, self.player)
        self.draw_figure(row, col)
        self.next_turn()

    def next_turn(self):
        self.player = self.player % 2 + 1

    def isover(self):
        return self.board.final_state(show=True) != 0 or self.board.isFull()

    def reset(self):
        self.__init__(self.screen, self.player)


def main():
    # PYGAME SETUP
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption('TIC TAC TOE GAME')
    screen.fill(BG_COLOR)
    game = Game(screen)
    board = game.board
    ai = game.ai
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                # r-restart
                if event.key == pygame.K_r:
                    game.reset()
                    board = game.board
                    ai = game.ai
                if event.key == pygame.K_1:
                    game.player = 1
                    game.reset()
                    board = game.board
                    ai = game.ai
                if event.key == pygame.K_2:
                    game.player = 2
                    game.reset()
                    board = game.board
                    ai = game.ai
            if event.type == pygame.MOUSEBUTTONDOWN:  # a mouse click
                # from pixels coordinates to rows and cols
                pos = event.pos
                row = pos[1] // SQSIZE  # y-axis of our board
                col = pos[0] // SQSIZE  # x-axis of our board

                # huuman move
                if board.empty_square(row, col) and game.running:
                    game.make_move(row, col)
                    # print(board.squares)

                    if game.isover():
                        game.running = False

        if game.player == ai.player and game.running:

            # update the screen
            pygame.display.update()

            # ai move
            row, col = ai.eval(board)
            game.make_move(row, col)
            # print(board.squares)

            if game.isover():
                game.running = False

        pygame.display.update()
