from sudoku import Sudoku

board = [

]

def main():
    with open("./initial_state/init_state1.txt", "r") as file:
        lines = file.readlines()

        for line in lines:
            line = line.replace("\n", "")
            numbers = [int(num) for num in line.split()]
            board.append(numbers)

    sudoku = Sudoku(board)
    sudoku.print_board()
    sudoku.solve()
    print("\nResult")
    sudoku.print_board()


if __name__ == "__main__":
    main()