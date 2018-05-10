import points_counter


class HeuristicEvaluator:
    def evaluate_heuristic_score(self, game_state, move):
        board, player_1_score, player_2_score = game_state
        counter = points_counter.PointsCounter(board)
        return counter.count_move_points(move)
