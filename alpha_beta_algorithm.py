import numpy as np

import heuristic_evaluator


class AlphaBetaStrategy:
    def __init__(self, game_board=None, search_depth=None):
        self._game_board = game_board
        self._heuristic_evaluator = heuristic_evaluator.HeuristicEvaluator()
        self._search_depth = search_depth

    def make_move(self):
        return self._alpha_beta(self._game_board, self._search_depth, -float('Inf'), float('Inf'), True)

    def _alpha_beta(self, board, depth, alpha, beta, max_turn, move=None):
        if depth <= 0:
            return self._heuristic_evaluator.evaluate_heuristic_score(board, move)
        if move is not None:
            board[move] = 1

        board_size = len(self._game_board)
        valid_moves = [x for x in np.ndindex(board_size, board_size) if self._game_board[x] == 0]

        if max_turn:
            for move in valid_moves:
                score = self._alpha_beta(board, depth - 1, alpha, beta, not max_turn, move)
                if score > alpha:
                    alpha = score
                if alpha >= beta:
                    return alpha
            return alpha
        else:
            for move in valid_moves:
                score = self._alpha_beta(board, depth - 1, alpha, beta, not max_turn, move)
                if score < beta:
                    beta = score
                if alpha >= beta:
                    return beta
            return beta
