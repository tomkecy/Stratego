import points_counter


class BasicHeuristic:
    def evaluate_heuristic_score(self, game_state, move):
        board, player_1_score, player_2_score = game_state
        counter = points_counter.PointsCounter(board)
        return counter.count_move_points(move)


class MaxPointDiffHeuristic:
    def evaluate_heuristic_score(self, game_state, move, player):
        board, player_1_score, player_2_score = game_state
        counter = points_counter.PointsCounter(board)
        move_points = counter.count_move_points(move)
        if player == 1:
            return player_1_score + move_points - player_2_score
        else:
            return player_2_score + move_points - player_1_score
