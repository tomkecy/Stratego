import numpy as np

import points_counter


class GameEngine:
    def __init__(self, board_size):
        self._PLAYER_1 = 1
        self._PLAYER_2 = 2
        self._current_player = self._PLAYER_1

        self._player_1_points = 0
        self._player_2_points = 0

        self._board_size = board_size
        self._game_board = np.zeros(shape=(board_size, board_size))
        self._points_counter = points_counter.PointsCounter(self._game_board)

    def get_board(self):
        return self._game_board

    def make_move(self, location):
        if not self.is_valid_move(location):
            return False
        self._game_board[location] = self._current_player
        self._count_current_move_points(location)
        self._swap_current_player()
        return True

    def is_valid_move(self, location):
        x, y = location
        return x < self._board_size and y < self._board_size and self._game_board[location] == 0

    def is_game_over(self):
        return 0 in self._game_board

    def get_player_points(self):
        return self._player_1_points, self._player_2_points

    def _swap_current_player(self):
        self._current_player = self._PLAYER_2 if self._current_player == self._PLAYER_1 else self._PLAYER_1

    def _count_current_move_points(self, location):
        result = self._points_counter.count_move_points(location)
        if self._current_player == self._PLAYER_1:
            self._player_1_points += result
        else:
            self._player_2_points += result





