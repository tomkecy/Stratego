import colorama
import game_engine
from colorama import Fore, Style

import heuristic_evaluator
from basic_game_algorithms import *
from alpha_beta_algorithm import *
from minimax_algorithm import *


class Cli:
    def __init__(self):
        colorama.init()
        self.INPUT_RUN_PLAYER_VS_AI = 1
        self.INPUT_RUN_AI_VS_AI = 2
        self.INPUT_CHANGE_BOARD_SIZE = 3
        self.INPUT_EXIT = 4
        self._heuristic = heuristic_evaluator.MaxPointDiffHeuristic()
        self._board_size = 8

        self.engine = game_engine.GameEngine(self._board_size)
        self._ai_players = []

        self._current_player = 1

    def run(self):
        self._print_menu()
        user_input = self._get_user_input()
        while user_input != self.INPUT_EXIT:
            if user_input == self.INPUT_RUN_PLAYER_VS_AI:
                self._run_player_vs_computer()
            elif user_input == self.INPUT_RUN_AI_VS_AI:
                self._run_ai_vs_ai()
            elif user_input == self.INPUT_CHANGE_BOARD_SIZE:
                self._change_board_size()
            else:
                print('Incorrect input!')
            self._print_menu()
            user_input = self._get_user_input()

    def _run_player_vs_computer(self):
        self._ai_players.clear()
        self._setup_ai_player()

        self._initialise_game()
        while self.engine.is_game_over():
            print("----------\nPlayer 1 score: %s\nPlayer 2 score %s\n----------" % self.engine.get_player_points())
            self._print_board()
            if self._current_player == 1:
                move = self._get_user_move()
                while not self.engine.make_move(move):
                    print("Invalid move, try again")
                    move = self._get_user_move()
                self.engine.make_move(move)
            else:
                game_state = self.engine.get_game_state()
                ai_move = self._ai_players[0].make_move(game_state)
                self.engine.make_move(ai_move)
            self._current_player = (self._current_player + 1) % 2

        self._print_board()
        self._print_end_game_summary()

    def _run_ai_vs_ai(self):
        self._ai_players.clear()
        self._setup_ai_player(1)
        self._setup_ai_player(2)

        self._run_ai_vs_ai_game()

    def _setup_ai_player(self, player_index=None):
        if player_index is None:
            ai_index_string = ''
        elif player_index == 1:
            ai_index_string = '1st '
        else:
            ai_index_string = '2nd '

        print('Select %sAI algorithm:\n1. Minimax\n2. Alpha-Beta' % ai_index_string)
        selected_algorithm = self._get_user_input()
        print('Enter search depth: ')
        search_depth = self._get_user_input()
        print('Select game heuristic:\n1. Basic\n2. Max point diff\n3. Waged')
        selected_heuristic = self._get_user_input()

        if selected_heuristic == 1:
            heuristic = heuristic_evaluator.BasicHeuristic()
        elif selected_heuristic == 2:
            heuristic = heuristic_evaluator.MaxPointDiffHeuristic()
        elif selected_heuristic == 3:
            heuristic = heuristic_evaluator.WagedHeuristic()
        else:
            print('Invalid input!')
            return False

        if selected_algorithm == 1:
            self._ai_players.append(MiniMaxStrategy(search_depth, heuristic, player_index))
        elif selected_algorithm == 2:
            self._ai_players.append(AlphaBetaStrategy(search_depth, heuristic, player_index))
        else:
            print('Invalid input!')
            return False
        return True

    def _run_ai_vs_ai_game(self):
        self._initialise_game()
        self._current_player = 0
        while self.engine.is_game_over():
            print("----------\nPlayer 1 score: %s\nPlayer 2 score %s\n----------" % self.engine.get_player_points())
            self._print_board()
            game_state = self.engine.get_game_state()
            player_move = self._ai_players[self._current_player].make_move(game_state)
            self.engine.make_move(player_move)

            self._current_player = (self._current_player + 1) % 2
        print("----------\nPlayer 1 score: %s\nPlayer 2 score %s\n----------" % self.engine.get_player_points())
        self._print_board()
        self._print_end_game_summary()

    def _print_board(self):
        board = self.engine.get_board()
        print('   |', end='')
        for i in range(self._board_size):
            print(' %i |' % i, end='')
        num = self._board_size + 1
        print('\n' + ('-' * 4 * num))
        for i in range(self._board_size):
            print('%i ||' % i, end='')
            for j in range(self._board_size):
                if board[i, j] == 0:
                    print(' %d |' % board[i, j], end='')
                elif board[i, j] == 1:
                    print('%s %d%s |' % (Fore.RED, board[i, j], Style.RESET_ALL), end='')
                else:
                    print('%s %d%s |' % (Fore.LIGHTCYAN_EX, board[i, j], Style.RESET_ALL), end='')
            print()

    def _print_end_game_summary(self):
        points = self.engine.get_player_points()
        print("----------\nPlayer 1 score: %s\nPlayer 2 score %s\n----------" % points)
        if points[0] == points[1]:
            print("Draw!")
        else:
            winner = "1" if points[0] > points[1] else "2"
            print("Player %s won!" % winner)

    def _get_user_move(self):
        move = None
        while move is None:
            try:
                move = int(input("Enter row: ")), int(input("Enter col: "))
            except ValueError:
                print("Invalid input")
        return move

    def _get_user_input(self):
        user_input = None
        while user_input is None:
            try:
                user_input = int(input())
            except ValueError:
                print("Invalid input")
        return user_input

    def _print_menu(self):
        print('----------\nMENU\n----------\n1. Player vs Computer\n'
              '2. Computer vs Computer\n3. Change board size\n4. Exit')

    def _initialise_game(self):
        self.engine = self.engine = game_engine.GameEngine(self._board_size)
        self._current_player = 1

    def _change_board_size(self):
        print('Enter board size: ')
        user_input = self._get_user_input()
        self._board_size = user_input
