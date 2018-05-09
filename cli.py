import game_engine
from basic_game_algorithms import *
from alpha_beta_algorithm import *
from minimax_algorithm import *
import queue


class Cli:
    def __init__(self):
        self.INPUT_RUN_PLAYER_VS_AI = 1
        self.INPUT_RUN_AI_VS_AI = 2
        self.INPUT_EXIT = 3

        self._board_size = 4

        self.engine = game_engine.GameEngine(self._board_size)
        self._ai_players = [AlphaBetaStrategy(self.engine.get_board(), 1), AlphaBetaStrategy(self.engine.get_board(), 1)]

        self._current_player = 1

    def run(self):
        self._print_menu()
        user_input = self._get_user_input()
        while user_input != self.INPUT_EXIT:
            if user_input == self.INPUT_RUN_PLAYER_VS_AI:
                self._run_player_vs_computer()
            elif user_input == self.INPUT_RUN_AI_VS_AI:
                self._run_ai_vs_ai()
            else:
                print('Incorrect input!')
            self._print_menu()
            user_input = self._get_user_input()

    def _run_ai_vs_ai(self):
        while self.engine.is_game_over():
            print("----------\nPlayer 1 score: %s\nPlayer 2 score %s\n----------" % self.engine.get_player_points())
            board = self.engine.get_board()
            print(board)
            # move = self.get_user_input()
            # while not self.engine.make_move(move):
            #     print("Invalid move, try again")
            #     move = self.get_user_input()
            player_move = self._ai_players[self._current_player].make_move()
            self.engine.make_move(player_move)

            self._current_player = (self._current_player + 1) % 2
        board = self.engine.get_board()
        print(board)
        self._print_end_game_summary()

    def _print_end_game_summary(self):
        points = self.engine.get_player_points()
        print("----------\nPlayer 1 score: %s\nPlayer 2 score %s\n----------" % points)
        if points[0] == points[1]:
            print("Draw!")
        else:
            winner = "1" if points[0] > points[1] else "2"
            print("Player %s won!" % winner)

    def get_user_move(self):
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
        print('----------\nMENU\n----------\n1. Player vs Computer\n2. Computer vs Computer\n3. Exit')

    def _run_player_vs_computer(self):
        while self.engine.is_game_over():
            print("----------\nPlayer 1 score: %s\nPlayer 2 score %s\n----------" % self.engine.get_player_points())
            board = self.engine.get_board()
            print(board)
            # move = self.get_user_input()
            # while not self.engine.make_move(move):
            #     print("Invalid move, try again")
            #     move = self.get_user_input()
            player_move = self._current_player.make_move()
            self.engine.make_move(player_move)

            self._ai_players.put(self._current_player)
            self._current_player = self._ai_players.get()
        board = self.engine.get_board()
        print(board)
        self._print_end_game_summary()
        pass

