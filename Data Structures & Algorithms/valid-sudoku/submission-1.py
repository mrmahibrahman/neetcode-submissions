class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        '''
            1. For each row: Check if theres a duplicate
            2. For each column: Check if theres a duplicate
            3. For each 3x3 grid: check if theres a duplicate

            for each step: we will have a hashmap where the key is the position, and the value is a hashset 
            
            idea: lets go through the board, for each row, and for each column, if theres a ".", then we continue, if not, lets see if the value is in hashmap 
            (RETURN FALSE), if not, we'll just add it to the hashmaps

            for the squares, we can do integer division to map the squares inside to make the whole grid 3x3 instead of like 9x9

            sudoku board is valid if the for loops run and no duplicate is found

        '''
        
        rows = collections.defaultdict(set)
        cols = collections.defaultdict(set)
        squares = collections.defaultdict(set)

        # Step 1: for each step
        for r in range(9):
            for c in range(9):
                if board[r][c] != ".":
                    if (board[r][c] in rows[r] or
                    board[r][c] in cols[c] or
                    board[r][c] in squares[(r//3,c//3)]):
                        return False
                    rows[r].add(board[r][c])
                    cols[c].add(board[r][c])
                    squares[(r//3,c//3)].add(board[r][c])

                    
        return True
                

                        



