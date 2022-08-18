# Determine if a 9 x 9 Sudoku board is valid. Only the filled cells need to be validated according to the following rules:

# Each row must contain the digits 1-9 without repetition.
# Each column must contain the digits 1-9 without repetition.
# Each of the nine 3 x 3 sub-boxes of the grid must contain the digits 1-9 without repetition.
# Note:

# A Sudoku board (partially filled) could be valid but is not necessarily solvable.
# Only the filled cells need to be validated according to the mentioned rules.


class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        output = []
        for i in range(9):
            for j in range(9):
                if board[i][j] != '.':
                    num = board[i][j]
                    if (i, num) in output or (num, j) in output or (i//3, j//3, num) in output:
                        return False
                    else:
                        output.append((i, num))
                        output.append((num, j))
                        output.append((i//3, j//3, num))
        return True
