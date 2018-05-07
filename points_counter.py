import numpy as np


class PointsCounter:
    def __init__(self, game_board):
        self._game_board = game_board
        self._board_size = len(game_board)

    def count_move_points(self, location):
        board_copy = np.copy(self._game_board)
        board_copy[location] = 1
        column = board_copy[:, location[1]]
        row = board_copy[location[0], :]
        diag = self._get_location_diagonal(location, board_copy)
        counter_diag = self._get_location_counter_diagonal(location, board_copy)
        point_acc = 0

        if 0 not in column:
            point_acc += len(column)
        if 0 not in row:
            point_acc += len(row)
        if 0 not in diag and len(diag) > 1:
            point_acc += len(diag)
        if 0 not in counter_diag and len(counter_diag) > 1:
            point_acc += len(counter_diag)

        return point_acc

    def _get_location_counter_diagonal(self, location, board_copy):
        i, j = location[0] + 1, location[1] - 1
        counter_diagonal = [board_copy[location]]
        while i < self._board_size and j >= 0:
            counter_diagonal.append(board_copy[i, j])
            i += 1
            j -= 1
        i, j = location[0] - 1, location[1] + 1
        while i >= 0 and j < self._board_size:
            counter_diagonal.append(board_copy[i, j])
            i -= 1
            j += 1
        return counter_diagonal

    def _get_location_diagonal(self, location, board_copy):
        diagonal = [board_copy[location]]
        i, j = location[0] - 1, location[1] - 1
        while i >= 0 and j >= 0:
            diagonal.append(board_copy[i, j])
            i -= 1
            j -= 1
        i, j = location[0] + 1, location[1] + 1
        while i < self._board_size and j < self._board_size:
            diagonal.append(board_copy[i, j])
            i += 1
            j += 1
        return diagonal
