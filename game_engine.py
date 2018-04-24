import numpy as np


class GameEngine:
    def __init__(self, board_size):
        self._current_player = None
        self._PLAYER_1 = 1
        self._PLAYER_2 = 2

        self._player_1_points = 0
        self._player_2_points = 0

        self._game_board = np.zeros(shape=(board_size, board_size))

    def get_board(self):
        return self._game_board

    def make_move(self, location):
        if self._game_board[location] != 0:
            return False
        self._game_board[location] = self._current_player
        self._count_current_move_points(location)
        self._swap_current_player()

    def _swap_current_player(self):
        self._current_player = self._PLAYER_2 if self._current_player == self._PLAYER_1 else self._PLAYER_2

    def _count_current_move_points(self, location):
        column = self._game_board[:, location[1]]
        row = self._game_board[location[0], :]

        point_acc = 0

        if 0 not in column:
            point_acc += len(column)
        if 0 not in row:
            point_acc += len(row)


