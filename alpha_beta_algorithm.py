import numpy as np

import heuristic_evaluator


class AlphaBetaStrategy:
    def __init__(self, game_board=None, search_depth=None):
        self._game_board = game_board
        self._heuristic_evaluator = heuristic_evaluator.HeuristicEvaluator()
        self._search_depth = search_depth

    def make_move(self):
        alpha_move = None, -float('Inf')
        beta_move = None, float('Inf')
        return self._alpha_beta(self._game_board, self._search_depth, alpha_move, beta_move, True)[0]

    def _alpha_beta(self, board, depth, alpha_move, beta_move, max_turn, move=None):
        if depth <= 0:
            return move, self._heuristic_evaluator.evaluate_heuristic_score(board, move)
        if move is not None:
            board[move] = 1

        _, alpha = alpha_move
        _, beta = beta_move
        board_size = len(self._game_board)
        valid_moves = [x for x in np.ndindex(board_size, board_size) if self._game_board[x] == 0]
        board_copy = np.copy(self._game_board)
        if max_turn:
            for move in valid_moves:
                _, score = self._alpha_beta(board_copy, depth - 1, alpha_move, beta_move, not max_turn, move)
                if score > alpha:
                    alpha = score
                    alpha_move = move, alpha
                if alpha >= beta:
                    return alpha_move
            return alpha_move
        else:
            for move in valid_moves:
                _, score = self._alpha_beta(board_copy, depth - 1, alpha_move, beta_move, not max_turn, move)
                if score < beta:
                    beta = score
                    beta_move = move, beta
                if alpha >= beta:
                    return beta_move
            return beta_move
