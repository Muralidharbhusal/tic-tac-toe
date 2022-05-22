import random


class Game:
    def __init__ (self, board, player1, player2):
        self.board = board
        self.players = [player1, player2]
        random.shuffle(self.players)

        self.turn = 0
        self.winner = None

    def check_win(self):
        """When ghe row or column or the diagonal is equal, winner is defined"""
        tiles = self.board.cells

        return (tiles[0] != ' ' and (tiles[0] == tiles[1] == tiles[2])) or \
               (tiles[3] != ' ' and (tiles[3] == tiles[4] == tiles[5])) or \
               (tiles[6] != ' ' and (tiles[6] == tiles[7] == tiles[8])) or \
               (tiles[0] != ' ' and (tiles[0] == tiles[3] == tiles[6])) or \
               (tiles[1] != ' ' and (tiles[1] == tiles[4] == tiles[7])) or \
               (tiles[2] != ' ' and (tiles[2] == tiles[5] == tiles[8])) or \
               (tiles[0] != ' ' and (tiles[0] == tiles[4] == tiles[8])) or \
               (tiles[2] != ' ' and (tiles[2] == tiles[4] == tiles[6]))

    def play(self):
        while not self.board.is_full():
            current_player = self.players[self.turn]
            self.board.display()

            cell = current_player.select_cell(self.board)
            self.board.cells[cell] = current_player.symbol

            # Stop if there is a winner
            if self.check_win():
                self.winner = current_player.name
                break
            else:
                self.turn = 1-self.turn

        self.board.display()
        print()

        # Check if there is a winner or the board is full
        if self.winner:
            print(f"[self.winner] has won. ")
        else:
            print("It is a tie")
