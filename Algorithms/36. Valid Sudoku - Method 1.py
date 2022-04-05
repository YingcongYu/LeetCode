# Determine if a 9 x 9 Sudoku board is valid. Only the filled cells need to be validated according to the following rules:

# Each row must contain the digits 1-9 without repetition.
# Each column must contain the digits 1-9 without repetition.
# Each of the nine 3 x 3 sub-boxes of the grid must contain the digits 1-9 without repetition.
# Note:

# A Sudoku board (partially filled) could be valid but is not necessarily solvable.
# Only the filled cells need to be validated according to the mentioned rules.

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for i in board:
            row = [x for x in i if x != '.']
            if len(row) != len(set(row)):
                return False
        for n in zip(*board):
            col = [x for x in n if x != '.']
            if len(col) != len(set(col)):
                return False
        for j in (0, 3, 6):
            for k in (0, 3, 6):
                matrix = [board[x][y] for x in range(j, j+3) for y in range(k, k+3)]
                matrix = [x for x in matrix if x != '.']
                if len(matrix) != len(set(matrix)):
                    return False
        return True
