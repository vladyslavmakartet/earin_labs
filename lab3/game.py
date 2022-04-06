import pygame

from ai import AI
from board import Board
from constants import *

class Game:
    def __init__(self, screen, player=2):
        self.screen = screen
        self.board = Board(self.screen)
        self.player = 2  # initial player to mark the square, player1 = cross, player2 = circle
        self.initial_player = player
        self.running = True
        self.ai = AI(player)
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
        self.__init__(self.screen, self.initial_player)
