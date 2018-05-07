import game_engine
from basic_game_algorithms import *


class Cli:
    def __init__(self):
        self.engine = game_engine.GameEngine(4)
        self._ai_opponent = OptimisedRandomStrategy(self.engine.get_board())

    def run(self):
        while self.engine.is_game_over():
            print("----------\nPlayer 1 score: %s\nPlayer 2 score %s\n----------" % self.engine.get_player_points())
            board = self.engine.get_board()
            print(board)
            move = self.get_user_input()
            while not self.engine.make_move(move):
                print("Invalid move, try again")
                move = self.get_user_input()
            opponent_move = self._ai_opponent.make_move()
            self.engine.make_move(opponent_move)

        board = self.engine.get_board()
        print(board)
        print("----------\nPlayer 1 score: %s\nPlayer 2 score %s\n----------" % self.engine.get_player_points())

    def get_user_input(self):
        move = None
        while move is None:
            try:
                move = int(input("Enter row: ")), int(input("Enter col: "))
            except ValueError:
                print("Invalid input")
        return move
