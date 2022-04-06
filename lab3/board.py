import copy
import numpy
import pygame

from constants import *

class Board:
    def __init__(self, screen):
        self.squares = numpy.zeros((ROWS, COLS))  # initialize board with zeros
        self.empty_squares = self.squares  # list of empty squares
        self.marked_squares = 0  # number of marked squares
        self.screen = screen

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
