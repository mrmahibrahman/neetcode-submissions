class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        '''
        1. Go through every single row and make sure every row has no duplicate
        - use a hashset

        2. Go through every single column, and make sure every column has no duplicate
        - use a hashset (adding element to hashet is O(1)) and checking is also O(1)

        3. Go through 3x3 areas using a hashset
        - We have 9 different subsquares, 
        - 4/3 = 1 which is an integer division (always round down)
        O(9^2)
        - Key is going to be (R/3, c/3), and the value is going to be a hash set 
        '''

        # this is a hashmap key is column number and value is a set
        cols = collections.defaultdict(set)
        rows = collections.defaultdict(set)
        squares = collections.defaultdict(set) # key = (r/3, c/3))

        for r in range(9):
            for c in range(9):
                if board[r][c] == ".":
                    continue
                if (board[r][c] in rows[r] or 
                    board[r][c] in cols[c] or
                    board[r][c] in squares[r//3, c//3]):
                    return False
                cols[c].add(board[r][c])
                rows[r].add(board[r][c])
                squares[(r//3, c//3)].add(board[r][c])
        return True


