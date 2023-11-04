import tkinter as tk
from sudoku import Sudoku

class SudokuGUI:
    def __init__(self, board):
        self.board = board
        self.window = tk.Tk()
        self.window.title("Sudoku solver")
        self.create_board()
        self.create_solve_button()
        self.sudoku = Sudoku(self.board)

    def create_board(self):
        for i in range(9):
            for j in range(9):
                cell_value = self.board[i][j]
                label = tk.Label(self.window, text=str(cell_value))
                label.grid(row=i, column=j, padx=10, pady=10, sticky="nsew")
                label.config(font=(16))
                if (i // 3 + j // 3) % 2 == 0:
                    label.config(bg="lightgray")
                else:
                    label.config(bg="white")

        for i in range(9):
            self.window.grid_rowconfigure(i, weight=1)
            self.window.grid_columnconfigure(i, weight=1)

    def create_solve_button(self):
        solve_button = tk.Button(self.window, text="Solve", command=self.solve_sudoku)
        solve_button.grid(row=9, columnspan=9, pady=10)

    def solve_sudoku(self):
        if self.sudoku.solve():
            self.update_board()

    def update_board(self):
        for i in range(9):
            for j in range(9):
                cell_value = self.board[i][j]
                label = tk.Label(self.window, text=str(cell_value))
                label.grid(row=i, column=j)
                label.config(font=(16))
                if (i // 3 + j // 3) % 2 == 0:
                    label.config(bg="lightgray")
                else:
                    label.config(bg="white")
