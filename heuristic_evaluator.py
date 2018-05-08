import points_counter


class HeuristicEvaluator:
    def evaluate_heuristic_score(self, board, move):
        counter = points_counter.PointsCounter(board)
        return counter.count_move_points(move)