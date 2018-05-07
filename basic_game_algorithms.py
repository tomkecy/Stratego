import random
import points_counter


class RandomStrategy:
    def __init__(self, game_board):
        self._game_board = game_board

    def make_move(self):
        board_size = len(self._game_board)
        valid_moves = []
        for i in range(board_size):
            for j in range(board_size):
                if self._game_board[i, j] == 0:
                    valid_moves.append((i, j))
        return random.choice(valid_moves)


class OptimisedRandomStrategy:
    def __init__(self, game_board):
        self._game_board = game_board
        self._points_counter = points_counter.PointsCounter(game_board)

    def make_move(self):
        board_size = len(self._game_board)
        valid_moves = []
        for i in range(board_size):
            for j in range(board_size):
                if self._game_board[i, j] == 0:
                    valid_moves.append((i, j))
        for move in valid_moves:
            if self._points_counter.count_move_points(move) > 0:
                return move
        return random.choice(valid_moves)
