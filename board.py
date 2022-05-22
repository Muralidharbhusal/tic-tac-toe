NUM_CELLS = 9


class Board:
    def __init__(self):
        self.cells = [" " for _ in range(NUM_CELLS)]

    def display(self):
        """ Displays The Board on Screen"""
        print(f"\n {self.cells[0]} | {self.cells[1]} | {self.cells[2]}")
        print("__|__|__")
        print(f"\n {self.cells[3]} | {self.cells[4]} | {self.cells[5]}")
        print("__|__|__")
        print(f"\n {self.cells[6]} | {self.cells[7]} | {self.cells[8]}")
        print("__|__|__")

    def is_clicked(self, cell_num):
        """Check if the board is full"""
        for cell in self.cells:
            if cell == " ":
                return False

    """Play Again"""

    def reset(self):
        """Empty all the cells"""
        for i in range(NUM_CELLS):
            self.cells[i] = " "
