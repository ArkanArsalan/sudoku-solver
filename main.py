from sudoku_solver1 import SudokuSolver1
from sudokuGUI import SudokuGUI
from initial_board import open_file

def main():
    board = open_file()

    gui = SudokuGUI(board)
    gui.window.mainloop()


if __name__ == "__main__":
    main()