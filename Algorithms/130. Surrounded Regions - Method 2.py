# Given an m x n matrix board containing 'X' and 'O', capture all regions that are 4-directionally surrounded by 'X'.

# A region is captured by flipping all 'O's into 'X's in that surrounded region.


class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        queue = deque([])
        m = len(board)
        n = len(board[0])
        
        for i in range(m):
            for j in range(n):
                if board[i][j] == 'O' and (i in [0, m-1] or j in [0, n-1]):
                    queue.append((i, j))
        
        while queue:
            row, col = queue.popleft()
            if row < 0 or col < 0 or row == m or col == n or board[row][col] != 'O':
                continue
            board[row][col] = 'U'
            queue.extend([(row-1, col), (row+1, col), (row, col-1), (row, col+1)])
        
        for i in range(m):
            for j in range(n):
                if board[i][j] == 'O':
                    board[i][j] = 'X'
                elif board[i][j] == 'U':
                    board[i][j] = 'O'
