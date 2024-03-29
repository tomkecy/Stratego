import random
import numpy as np

import points_counter


class RandomStrategy:
    def make_move(self, game_state):
        game_board, _, _ = game_state
        board_size = len(game_board)
        valid_moves = []
        for i in range(board_size):
            for j in range(board_size):
                if game_board[i, j] == 0:
                    valid_moves.append((i, j))
        return random.choice(valid_moves)


class OptimisedRandomStrategy:
    def __init__(self, game_board):
        self._game_board = game_board
        self._points_counter = points_counter.PointsCounter(game_board)

    def make_move(self, game_state):
        board_size = len(self._game_board)
        valid_moves = [x for x in np.ndindex(board_size, board_size) if self._game_board[x] == 0]
        for move in valid_moves:
            if self._points_counter.count_move_points(move) > 0:
                return move
        return random.choice(valid_moves)


class LocalBestStrategy:
    def __init__(self, game_board):
        self._game_board = game_board
        self._points_counter = points_counter.PointsCounter(game_board)

    def make_move(self, game_state):
        board_size = len(self._game_board)
        valid_moves = [x for x in np.ndindex(board_size, board_size) if self._game_board[x] == 0]
        best_move = None, -float('Inf')
        for move in valid_moves:
            score = self._points_counter.count_move_points(move)
            if score > best_move[1]:
                best_move = move, score
        return best_move[0]
