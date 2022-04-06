import copy
import random
from math import inf

class AI:
    def __init__(self, player=2):
        self.player = player
        self.count = 0

    # --- MINIMAX ---

    def minimaxAB(self, board, alpha, beta, maximizing):

        # terminal case
        case = board.final_state()
        self.count += 1
        # player 1 wins
        if case == 1:
            return 1, None  # eval, move

        # player 2 wins
        if case == 2:
            return -1, None  # eval, move

        # draw
        elif board.isFull():
            return 0, None  # eval, move

        best_move = None
        empty_sqrs = board.get_empty_squares()
        player = 2
        next_move_max = True
        if maximizing:
            player = 1
            next_move_max = False

        for (row, col) in empty_sqrs:
            temp_board = copy.deepcopy(board)
            temp_board.mark_square(row, col, player)
            eval = self.minimaxAB(temp_board, alpha, beta, next_move_max)[0]
            if maximizing and eval > alpha:
                alpha = eval
                best_move = (row, col)
            elif not maximizing and eval < beta:
                beta = eval
                best_move = (row, col)

            if alpha >= beta:
                break

        if maximizing:
            return alpha, best_move
        else:
            return beta, best_move

    # --- MAIN EVAL ---

    def eval(self, main_board):
        # minimaxAB algo choice
        maximize = self.player == 1
        eval, move = self.minimaxAB(main_board, -inf, inf, maximize)
        # eval = 1, player wins. eval = -1, algorithm wins. eval = 0, draw
        print(
            f'Algorithm has chosen the square in pos {move} with an eval of: {eval}. Num of iterations: {self.count}')
        self.count = 0

        return move  # row, col