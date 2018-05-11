import colorama
import game_engine
from colorama import Fore, Style

import heuristic_evaluator
from basic_game_algorithms import *
from alpha_beta_algorithm import *
from minimax_algorithm import *
from timeit import default_timer as timer


def print_board(engine, board_size):
    board = engine.get_board()
    print('   |', end='')
    for i in range(board_size):
        print(' %i |' % i, end='')
    num = board_size + 1
    print('\n' + ('-' * 4 * num))
    for i in range(board_size):
        print('%i ||' % i, end='')
        for j in range(board_size):
            if board[i, j] == 0:
                print(' %d |' % board[i, j], end='')
            elif board[i, j] == 1:
                print('%s %d%s |' % (Fore.RED, board[i, j], Style.RESET_ALL), end='')
            else:
                print('%s %d%s |' % (Fore.LIGHTCYAN_EX, board[i, j], Style.RESET_ALL), end='')
        print()


def print_end_game_summary(engine):
    points = engine.get_player_points()
    print("----------\nPlayer 1 score: %s\nPlayer 2 score %s\n----------" % points)
    if points[0] == points[1]:
        print("Draw!")
    else:
        winner = "1" if points[0] > points[1] else "2"
        print("Player %s won!" % winner)


def run_ai_vs_ai(ai_players, board_size, out_file, first_search_depth, second_search_depth, start_player, stats):
    engine = game_engine.GameEngine(board_size)
    current_player = start_player
    times = [0, 0]
    while engine.is_game_over():
        print("----------\nPlayer 1 score: %s\nPlayer 2 score %s\n----------" % engine.get_player_points())
        print_board(engine, board_size)
        game_state = engine.get_game_state()

        start = timer()
        player_move = ai_players[current_player].make_move(game_state)
        end = timer()
        times[current_player] = times[current_player] + (end - start)
        engine.make_move(player_move)

        current_player = (current_player + 1) % 2
    points = engine.get_player_points()
    print("----------\nPlayer 1 score: %s\nPlayer 2 score %s\n----------" % points)
    print_board(engine, board_size)
    print_end_game_summary(engine)
    out_file.write(
        '%s,%s,%s,%s,%s,%s\n' % (first_search_depth, second_search_depth, points[0], points[1], times[0], times[1]))
    return points


colorama.init()
file = open('heuristics.csv', 'w')

heuristics = [heuristic_evaluator.BasicHeuristic(), heuristic_evaluator.MaxPointDiffHeuristic(),
              heuristic_evaluator.WagedHeuristic()]

max_depth = 3
winning_stats = {}
earned_points = {}
for first_depth in range(1, max_depth + 1):
    for first_heuristic in heuristics:
        for second_heuristic in heuristics:
            file.write('%s,%s,%s,%s,%s,%s\n' % (
                'First Search depth', 'Second search depth', type(first_heuristic).__name__,
                type(second_heuristic).__name__, 'Player 1 time', 'Player 2 time'))
            for second_depth in range(1, max_depth + 1):
                algorithms = [
                    AlphaBetaStrategy(search_depth=first_depth, heuristic_evaluator=first_heuristic, player_index=1),
                    AlphaBetaStrategy(search_depth=second_depth, heuristic_evaluator=second_heuristic, player_index=2)]
                points = run_ai_vs_ai(algorithms, 8, file, first_depth, second_depth, 0, winning_stats)
                winner = 0
                if points[0] > points[1]:
                    winner = 1
                elif points[1] > points[0]:
                    winner = 2
                if winner != 0:
                    key = (type(first_heuristic).__name__, first_depth) if winner == 1 else (
                        type(second_heuristic).__name__, second_depth)
                    winning_stats[key] = winning_stats.get(key, 0) + 1
                key1 = (type(first_heuristic).__name__, first_depth)
                earned_points[key1] = earned_points.get(key1, 0) + points[0]

                key2 = (type(second_heuristic).__name__, second_depth)
                earned_points[key2] = earned_points.get(key2, 0) + points[1]
            file.write('\n')

file.write('%s,%s,%s\n' % ('Heuristic', 'Search depth', 'Wins'))
for winner in winning_stats:
    file.write('%s,%s,%s\n' % (winner[0], winner[1], winning_stats[winner]))

file.write('%s,%s,%s\n' % ('Heuristic', 'Search depth', 'Earned points'))
for player in earned_points:
    file.write('%s,%s,%s\n' % (player[0], player[1], earned_points[player]))
