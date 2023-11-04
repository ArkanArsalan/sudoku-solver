class Sudoku():
    def __init__(self, board):
        self.board = board

    def solve(self):
        empty_cell = self.find_empty()
        
        if not empty_cell:
            return True
        else:
            row, col = empty_cell

        for num in range(1,10):
            if self.valid(num, (row, col)):
                self.board[row][col] = num

                if self.solve():
                    return True

                self.board[row][col] = 0

        return False

    def valid(self, num, pos):
        # Check row
        for col in range(len(self.board[0])):
            if self.board[pos[0]][col] == num and pos[1] != col:
                return False

        # Check column
        for row in range(len(self.board)):
            if self.board[row][pos[1]] == num and pos[0] != row:
                return False

        # Check box
        box_col = pos[1] // 3
        box_row = pos[0] // 3

        for i in range(box_row * 3, box_row * 3 + 3):
            for j in range(box_col * 3, box_col * 3 + 3):
                if self.board[i][j] == num and (i,j) != pos:
                    return False

        return True

    def print_board(self):
        for i in range(len(self.board) + 1):
            if i % 3 == 0:
                print("- - - - - - - - - - - - - ")
                if i == 9:
                    break

            for j in range(len(self.board[0]) + 1):
                if j % 3 == 0:
                    if j == 9:
                        print("| ")
                    else:
                        print("| ", end="")

                if j <= 8:
                    print(str(self.board[i][j]) + " ", end="")

    def find_empty(self):
        for i in range(len(self.board)):
            for j in range(len(self.board[0])):
                if self.board[i][j] == 0:
                    return (i, j) 

        return None