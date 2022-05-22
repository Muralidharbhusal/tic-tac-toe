from board import Board
from player import Player
from game import Game
import random


def play_game(tic_tac_toe):
    run = True
    while run:
        tic_tac_toe.play()

        choice = input("\n Would You like to play again (yes/no: ").lower()
        if choice.startswith("n"):
            run = False
        else:
            tic_tac_toe.board.reset()


if __name__ == "__main__":
    symbols = ["X", "O"]
    random.shuffle(symbols)

    print("Welcome \n")
    player1_name = input("Enter player 1 name: ")
    player2_name = input("Enter Player 2 name: ")

    game_player1 = Player(symbol=symbols[0], name=player1_name)
    game_player2 = Player(symbol=symbols[1], name=player2_name)

    game_board = Board()
    game = Game(board=game_board, player1=game_player1, player2=game_player2)

    play_game(tic_tac_toe=game)
