import tkinter as tk
from sudoku_solver1 import SudokuSolver1
from sudoku_solver2 import SudokuSolver2
import copy

class SudokuGUI:
    def __init__(self, board):
        self.board = board
        self.init_board =  copy.deepcopy(self.board)
        self.window = tk.Tk()
        self.window.title("Sudoku solver")
        self.create_board()
        self.sudoku1 = None
        self.sudoku2 = None
        self.open_sudoku_solver()

    def open_sudoku_solver(self):
        self.sudoku1 = SudokuSolver1(self.board)
        self.sudoku2 = SudokuSolver2(self.board)

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

        # Create three buttons below the board
        button1 = tk.Button(self.window, text="Method 1", command=self.solve_sudoku_method1)
        button2 = tk.Button(self.window, text="method 2", command=self.solve_sudoku_method2)
        button3 = tk.Button(self.window, text="Reset", command=self.reset)
        
        # Place the buttons in the grid
        button1.grid(row=9, column=0, padx=10, pady=10, columnspan=3)
        button2.grid(row=9, column=3, padx=10, pady=10, columnspan=3)
        button3.grid(row=9, column=6, padx=10, pady=10, columnspan=3)


    def solve_sudoku_method1(self):
        print("\nSolving using backtracking")
        self.sudoku1.solve()
        self.sudoku1.print_board()
        self.update_board()
        print(f"Total recursive call: {self.sudoku1.count}")
        print(f"Completion time: {self.sudoku1.delta}")

    def solve_sudoku_method2(self):
        print("\nSolving using bactracking, forward checking, and MRV")
        self.sudoku2.solve()
        self.sudoku2.print_board()
        self.update_board()
        print(f"Total recursive call: {self.sudoku2.count}")
        print(f"Completion time: {self.sudoku2.delta}")


    def reset(self):
        self.board = copy.deepcopy(self.init_board)
        self.open_sudoku_solver()
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
