# TODO
# split code ?
# add sounds and menu ?

import sys
import pygame

from constants import *
from game import Game


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
                    game.initial_player = 1
                    game.reset()
                    board = game.board
                    ai = game.ai
                if event.key == pygame.K_2:
                    game.initial_player = 2
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
