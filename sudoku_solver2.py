
class SudokuSolver2():
    def __init__(self, board):
        self.board = board
        self.empty_cell = self.find_empty()

    def find_empty(self):          
        empty_cell = []
        for i in range(len(self.board)):
            for j in range(len(self.board)):
                if self.board[i][j] == 0:
                    empty_cell.append((i,j))
        return empty_cell
    
    def check_validation(self, num, pos):
        # Check row
        for i in range(len(self.board)):
            if self.board[pos[0]][i] == num:
                return False

        # check column
        for i in range(len(self.board)):
            if self.board[i][pos[1]] == num:
                return False
        
        # Check box
        box_col = pos[1] // 3
        box_row = pos[0] // 3
        

        for i in range(box_row * 3, box_row * 3 + 3):
            for j in range(box_col * 3, box_col * 3 + 3):
                if self.board[i][j] == num and (i,j) != pos:
                    return False
                
        return True
    
    def forward_checking(self):                   
        domains = {}
        for pos in self.empty_cell:
            domains[pos] = []
            for i in range(1, 10):
                if self.check_validation(i, pos):
                    domains[pos].append(i)

            if domains[pos] == []:
                domains[pos].pop

        return domains

    def mrv(self, domains):              
        position = []
        max_possible_input = 10   
        for domain in domains:
            if len(domains[domain]) == max_possible_input:
                position.append(domain)
            elif len(domains[domain]) < max_possible_input:
                position.clear()
                position.append(domain)
                max_possible_input = len(domains[domain])
        
        return position.pop()
    
    
    def solve(self):              
        domains = self.forward_checking()
        if not domains:
            return True
        min = self.mrv(domains)

        for i in domains[min]:
                self.board[min[0]][min[1]] = i
                self.empty_cell.remove((min[0], min[1]))

                if self.solve():
                    return True
                self.board[min[0]][min[1]] = 0
        
        self.empty_cell.append((min[0], min[1]))
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