import game_engine
from basic_game_algorithms import *
from minimax_algorithm import *


class Cli:
    def __init__(self):
        self.engine = game_engine.GameEngine(6)
        self._ai_player = MiniMaxStrategy(self.engine.get_board(), 1)
        self._ai_opponent = MiniMaxStrategy(self.engine.get_board(), 2)

    def run(self):
        while self.engine.is_game_over():
            print("----------\nPlayer 1 score: %s\nPlayer 2 score %s\n----------" % self.engine.get_player_points())
            board = self.engine.get_board()
            print(board)
            # move = self.get_user_input()
            # while not self.engine.make_move(move):
            #     print("Invalid move, try again")
            #     move = self.get_user_input()
            player_move = self._ai_player.make_move()
            self.engine.make_move(player_move)

            opponent_move = self._ai_opponent.make_move()
            self.engine.make_move(opponent_move)

        board = self.engine.get_board()
        points = self.engine.get_player_points()
        print(board)
        print("----------\nPlayer 1 score: %s\nPlayer 2 score %s\n----------" % points)
        if points[0] == points[1]:
            print("Draw!")
        else:
            winner = "1" if points[0] > points[1] else "2"
            print("Player %s won!" % winner)

    def get_user_input(self):
        move = None
        while move is None:
            try:
                move = int(input("Enter row: ")), int(input("Enter col: "))
            except ValueError:
                print("Invalid input")
        return move
