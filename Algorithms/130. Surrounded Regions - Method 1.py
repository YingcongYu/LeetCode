# Given an m x n matrix board containing 'X' and 'O', capture all regions that are 4-directionally surrounded by 'X'.

# A region is captured by flipping all 'O's into 'X's in that surrounded region.


class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        def unsurrounded(row, col):
            if row < 0 or col < 0 or row == m or col == n or board[row][col] != 'O':
                return
            board[row][col] = 'U'
            unsurrounded(row+1, col)
            unsurrounded(row-1, col)
            unsurrounded(row, col+1)
            unsurrounded(row, col-1)
        
        m = len(board)
        n = len(board[0])
        
        for i in range(m):
            for j in range(n):
                if board[i][j] == 'O' and (i in [0, m-1] or j in [0, n-1]):
                    unsurrounded(i, j)
        
        for i in range(m):
            for j in range(n):
                if board[i][j] == 'O':
                    board[i][j] = 'X'
                elif board[i][j] == 'U':
                    board[i][j] = 'O'
