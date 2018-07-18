import numpy as np


class AlphaBetaStrategy:
    def __init__(self, search_depth, heuristic_evaluator, player_index, use_heuristic=False):
        self._heuristic_evaluator = heuristic_evaluator
        self._search_depth = search_depth
        self._player_index = player_index
        self._cut_offs = {}
        self._use_heuristic = use_heuristic

    def make_move(self, game_state):
        alpha_move = None, -float('Inf')
        beta_move = None, float('Inf')
        return self._alpha_beta(game_state, self._search_depth, alpha_move, beta_move, True)[0]

    def _alpha_beta(self, game_state, depth, alpha_move, beta_move, max_turn, move=None):
        game_board, player_1_score, player_2_score = game_state
        if depth <= 0:
            return move, self._heuristic_evaluator.evaluate_heuristic_score(game_state, move, self._player_index)
        if move is not None:
            game_board[move] = 1

        _, alpha = alpha_move
        _, beta = beta_move
        board_size = len(game_board)
        valid_moves = [x for x in np.ndindex(board_size, board_size) if game_board[x] == 0]
        if self._use_heuristic:
            self._cutoff_move_first_heuristic(depth, valid_moves)

        game_state_copy = np.copy(game_board), player_1_score, player_2_score
        if max_turn:
            for move in valid_moves:
                _, score = self._alpha_beta(game_state_copy, depth - 1, alpha_move, beta_move, not max_turn, move)
                if score > alpha:
                    alpha = score
                    alpha_move = move, alpha
                if alpha >= beta:
                    depth_cutoffs = self._cut_offs.get(depth, [])
                    depth_cutoffs.append(alpha_move[0])
                    self._cut_offs[depth] = depth_cutoffs
                    return alpha_move
            return alpha_move
        else:
            for move in valid_moves:
                _, score = self._alpha_beta(game_state_copy, depth - 1, alpha_move, beta_move, not max_turn, move)
                if score < beta:
                    beta = score
                    beta_move = move, beta
                if alpha >= beta:
                    depth_cutoffs = self._cut_offs.get(depth, [])
                    depth_cutoffs.append(beta_move[0])
                    self._cut_offs[depth] = depth_cutoffs
                    return beta_move
            return beta_move

    def _cutoff_move_first_heuristic(self, depth, valid_moves):
        if depth not in self._cut_offs:
            return
        cutoff_moves = self._cut_offs[depth]
        valid_cutoff_moves = list(set(valid_moves).intersection(cutoff_moves))
        for valid_cutoff_move in valid_cutoff_moves:
            valid_moves.insert(0, valid_moves.pop(valid_moves.index(valid_cutoff_move)))
