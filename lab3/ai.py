import copy
import random
from math import inf

class AI:
    # random ai: level = 0, minimaxAB ai: level = 1
    def __init__(self, level=1, player=2):
        self.level = level
        self.player = player
        self.count = 0

    # --- RANDOM ---

    def rnd(self, board):
        empty_sqrs = board.get_empty_squares()
        idx = random.randrange(0, len(empty_sqrs))

        return empty_sqrs[idx]  # (row, col)

    # --- MINIMAX ---

    def minimaxAB(self, board, alpha, beta, maximizing):

        # terminal case
        case = board.final_state()
        self.count += 1
        # player 1 wins
        if case == 1:
            return 1, None  # eval, move

        # player 2 wins (ai wins)
        if case == 2:
            return -1, None  # eval, move

        # draw
        elif board.isFull():
            return 0, None  # eval, move

        if maximizing:
            best_move = None
            empty_sqrs = board.get_empty_squares()

            for (row, col) in empty_sqrs:
                temp_board = copy.deepcopy(board)
                temp_board.mark_square(row, col, 1)
                eval = self.minimaxAB(temp_board, alpha, beta, False)[0]
                if eval > alpha:
                    alpha = eval
                    best_move = (row, col)

                if alpha >= beta:
                    break

            return alpha, best_move

        elif not maximizing:
            best_move = None
            empty_sqrs = board.get_empty_squares()

            for (row, col) in empty_sqrs:
                temp_board = copy.deepcopy(board)
                temp_board.mark_square(row, col, self.player)
                eval = self.minimaxAB(temp_board, alpha, beta, True)[0]
                if eval < beta:
                    beta = eval
                    best_move = (row, col)

                if alpha >= beta:
                    break
            return beta, best_move

    # --- MAIN EVAL ---

    def eval(self, main_board):
        if self.level == 0:
            # random choice
            eval = 'random'
            move = self.rnd(main_board)
        else:
            # minimaxAB algo choice
            eval, move = self.minimaxAB(main_board, -inf, inf, False)
        # eval = 1, player wins. eval = -1, algorithm wins. eval = 0, draw
        print(
            f'Algorithm has chosen the square in pos {move} with an eval of: {eval}. Num of iterations: {self.count}')
        self.count = 0

        return move  # row, col