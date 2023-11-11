import time

class SudokuSolver1():
    def __init__(self, board):
        self.board = board
        self.count = 0
        self.delta = 0

    def solve(self):
        start = time.time()
        self._solve()
        end = time.time()
        self.delta = (end - start)

    def _solve(self):
        # Get position of empty cell
        empty_cell = self.find_empty()
        
        # Check if empty cell exist or not
        if not empty_cell:
            return True
        else:
            row, col = empty_cell

        self.count += 1
        
        # Iterate from 1 to 9
        for num in range(1,10):
            # Check if number is valid for the current cell
            if self.valid(num, (row, col)):
                # Insert the number to the cell
                self.board[row][col] = num

                # Recursive case
                if self._solve():
                    return True

                # If any number is invalid, current cell back to 0
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
        # Print horizontal line
        for i in range(len(self.board) + 1):
            if i % 3 == 0:
                print("- - - - - - - - - - - - - ")
                if i == 9:
                    break
            
            for j in range(len(self.board[0]) + 1):
                # Print vertical line
                if j % 3 == 0:
                    if j == 9:
                        print("| ")
                    else:
                        print("| ", end="")

                # Print number
                if j <= 8:
                    print(str(self.board[i][j]) + " ", end="")

    def find_empty(self):
        # Iterate all row
        for i in range(len(self.board)):
            # Iterate all column
            for j in range(len(self.board[0])):
                # Check if the cell still empty or not, return the position if empty
                if self.board[i][j] == 0:
                    return (i, j) 
        
        # No empty cell
        return None