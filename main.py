from sudokuGUI import SudokuGUI
from initial_board import open_file

def main():
    board = open_file()
    sudoku = SudokuGUI(board)
    sudoku.window.mainloop()

if __name__ == "__main__":
    main()