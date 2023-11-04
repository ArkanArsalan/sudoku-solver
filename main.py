from sudoku import Sudoku
from sudokuGUI import SudokuGUI

board = []

def main():
    with open("./initial_state/init_state1.txt", "r") as file:
        lines = file.readlines()

        for line in lines:
            line = line.replace("\n", "")
            numbers = [int(num) for num in line.split()]
            board.append(numbers)

    gui = SudokuGUI(board)
    gui.window.mainloop()


if __name__ == "__main__":
    main()