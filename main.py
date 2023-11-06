from sudoku_solver1 import SudokuSolver1
from sudoku_solver2 import SudokuSolver2
from initial_board import open_file
import copy

def main():
    board = open_file()
    copy_board = open_file()


    print("Solving using backtracking")
    s1 = SudokuSolver1(board)
    s1.solve()
    s1.print_board()
    print(f"Total recursive call: {s1.count}")

    print("\nSolving using bactracking, forward checking, and MRV")
    s2 = SudokuSolver2(copy_board)
    s2.solve()
    s2.print_board()
    print(f"Total recursive call: {s2.count}")


if __name__ == "__main__":
    main()