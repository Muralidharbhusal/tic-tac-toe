class Player:
    def __init__ (self, symbol, name):
        self.symbol = symbol
        self.name = name

    #Getter
    def get_symbol(self):
        return self.symbol

    def select_cell(self, board):
        correct_cell = False
        while not correct_cell:
            cell = int(input(f"{self.name}'s turn. Enter a Cell Between (0-8): "))

            # Check if the input is in the cell range
            if cell < 0 or cell > len(board.cells) -1:
                print("Please enter an appropriate cell")
            elif board.is_clicked(cell):
                print("The cell is already clicked. Enter a New one \n")
            else:
                correct_cell = True
        return cell
