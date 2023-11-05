from sudoku_solver1 import SudokuSolver1
from sudoku_solver2 import SudokuSolver2
from sudokuGUI import SudokuGUI
from initial_board import open_file

def main():
    board = open_file()

    sudoku = SudokuSolver2(board)
    sudoku.print_board()
    sudoku.solve()
    sudoku.print_board()


if __name__ == "__main__":
    main()