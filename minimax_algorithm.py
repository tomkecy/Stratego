import numpy as np

import heuristic_evaluator


class MiniMaxStrategy:
    def __init__(self,  search_depth):
        self._search_depth = search_depth
        self._heuristic_evaluator = heuristic_evaluator.HeuristicEvaluator()

    def make_move(self, game_state):
        move, _ = self._mini_max(game_state, self._search_depth, True)
        return move

    def _mini_max(self, game_state, depth, max_turn, move=None):
        board, _, _ = game_state
        if depth <= 0:
            return move, self._heuristic_evaluator.evaluate_heuristic_score(board, move)
        if move is not None:
            board[move] = 1

        board_size = len(board)
        valid_moves = [x for x in np.ndindex(board_size, board_size) if board[x] == 0]
        scores = []
        for move in valid_moves:
            board_copy = np.copy(board)
            scores.append(self._mini_max(board_copy, depth - 1, not max_turn, move)[1])

        if len(valid_moves) == 1:
            return valid_moves[0], scores[0]
        if max_turn:
            max_index = np.argmax(scores)
            return valid_moves[max_index], scores[max_index]
        else:
            min_index = np.argmin(scores)
            return valid_moves[min_index], scores[min_index]


