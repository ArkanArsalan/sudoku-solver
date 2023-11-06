import copy

class SudokuSolver2():
    def __init__(self, board):
        self.board = board
        self.count = 0

    def get_empty_cells(self):
        # Initialize list to store empty cells
        empty_cells = []

        # Iterate for every cell, if the cell contain 0 add to the empty cells list
        for i in range(len(self.board)):
            for j in range(len(self.board)):
                if self.board[i][j] == 0:
                    empty_cells.append((i, j))

        return empty_cells

    def get_possible_values(self, row, col):
        # List of all values that can be inserted to the cells
        possible_values = [1,2,3,4,5,6,7,8,9]

        # Iterate every column check if number from 1-9 already exist or not
        # If it exist, remove from possible value list
        for j in range(len(self.board)):
            if self.board[row][j] in possible_values:
                possible_values.remove(self.board[row][j])

        # Iterate every row check if number from 1-9 already exist or not
        # If it exist, remove from possible value list
        for i in range(len(self.board)):
            if self.board[i][col] in possible_values:
                possible_values.remove(self.board[i][col])

        # Iteraite every number in a the box, check if number from 1-9 already exist or not
        # If it exist, remove from possible value list
        box_col = col // 3
        box_row = row // 3

        for i in range(box_row * 3, box_row * 3 + 3):
            for j in range(box_col * 3, box_col * 3 + 3):
                if self.board[i][j] in possible_values:
                    possible_values.remove(self.board[i][j])

        # Return list of possible value can be inserted in current cells
        return list(possible_values)

    def forward_checking(self, empty_cells, n_domain):
        # Initialize new domain
        new_domain = copy.deepcopy(n_domain)
        
        # Iterate every cell in empty cells list
        for cell in empty_cells:

            row, col = cell
            possible_values = new_domain[(row, col)]

            # Iterate every column check if number from 1-9 already exist or not
            # If it exist, remove from possible value list
            for j in range(len(self.board)):
                if self.board[row][j] in possible_values:
                    possible_values.remove(self.board[row][j])

            # Iterate every row check if number from 1-9 already exist or not
            # If it exist, remove from possible value list
            for i in range(len(self.board)):
                if self.board[i][col] in possible_values:
                    possible_values.remove(self.board[i][col])

            # Iterate every number in the box, check if number from 1-9 already exist or not
            # If it exist, remove from possible value list
            box_row = (row // 3) * 3
            box_col = (col // 3) * 3

            for i in range(box_row, box_row + 3):
                for j in range(box_col, box_col + 3):
                    if self.board[i][j] in possible_values:
                        possible_values.remove(self.board[i][j])

            new_domain[(row, col)] = possible_values
            
        return new_domain

    # Choosing cell with the least amouont of possible values
    def mrv(self, empty_cells, domain):
        minimum_cell = None
        minimum_values = float('inf')

        # Iterate for every cell in empty cells list
        # Find the cell with the lest amount of possible values
        for cell in empty_cells:
            values = domain[cell]
            if len(values) < minimum_values:
                minimum_cell = cell
                minimum_values = len(values)

        return minimum_cell

    def solve(self):
        # Get all empty cells in sudoku
        empty_cells = self.get_empty_cells()

        # Domain of all possible values in the empty cells
        domain = {}
        
        # Iterate over empty cell and find all possible values that can be inserted to the cell
        for cell in empty_cells:
            domain[cell] = self.get_possible_values(cell[0], cell[1])

        # Solve the sudoku
        self._solve(empty_cells, domain)

    def _solve(self, empty_cells, domain):
        if not empty_cells:
            return True
        
        # Get the cell with the least amount of possible values
        cell = self.mrv(empty_cells, domain)

        # Get the all possible values for current cell
        values = domain[cell]

        self.count += 1

        # Loop through all possible values
        for value in values:
            # Insert the value to the cell
            self.board[cell[0]][cell[1]] = value

            # Create new_empty_cells
            new_empty_cells = empty_cells.copy()
            new_empty_cells.remove(cell)

            # Call forward checking with the new empty cells to get the new domain
            new_domain = self.forward_checking(new_empty_cells, domain)

            # Check whether all the empty cells in the new_empty_cells list still have possible values in the new_domain
            if all(len(new_domain[cell]) > 0 for cell in new_empty_cells):
                if self._solve(new_empty_cells, new_domain):
                    return True

        # Backtrack
        return False
    
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