import colorama
import game_engine
from colorama import Fore, Style
from basic_game_algorithms import *
from alpha_beta_algorithm import *
from minimax_algorithm import *


board_size = 1
engine = game_engine.GameEngine(board_size)


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


def initialise_game():
    engine = engine = game_engine.GameEngine(board_size)
    current_player = 1
    ai_players = [
        MiniMaxStrategy(1),
        # OptimisedRandomStrategy(self.engine.get_board()),
        AlphaBetaStrategy(2, 2),
    ]


def print_end_game_summary(engine):
    points = engine.get_player_points()
    print("----------\nPlayer 1 score: %s\nPlayer 2 score %s\n----------" % points)
    if points[0] == points[1]:
        print("Draw!")
    else:
        winner = "1" if points[0] > points[1] else "2"
        print("Player %s won!" % winner)


def run_ai_vs_ai(ai_players):
    engine = game_engine.GameEngine(board_size)
    current_player = 0
    while engine.is_game_over():
        print("----------\nPlayer 1 score: %s\nPlayer 2 score %s\n----------" % engine.get_player_points())
        print_board(engine, board_size)
        game_state = engine.get_game_state()
        player_move = ai_players[current_player].make_move(game_state)
        engine.make_move(player_move)

        current_player = (current_player + 1) % 2
    print("----------\nPlayer 1 score: %s\nPlayer 2 score %s\n----------" % engine.get_player_points())
    print_board(engine, board_size)
    print_end_game_summary(engine)
