# You are given an m x n binary matrix grid, where 0 represents a sea cell and 1 represents a land cell.

# A move consists of walking from one land cell to another adjacent (4-directionally) land cell or walking off the boundary of the grid.

# Return the number of land cells in grid for which we cannot walk off the boundary of the grid in any number of moves.


class Solution:
    def numEnclaves(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])

        def visit(x, y):
            grid[x][y] = 0
            if x < m-1:
                if grid[x+1][y] == 1:
                    visit(x+1, y)
            if x > 0:
                if grid[x-1][y] == 1:
                    visit(x-1, y)
            if y < n-1:
                if grid[x][y+1] == 1:
                    visit(x, y+1)
            if y > 0:
                if grid[x][y-1] == 1:
                    visit(x, y-1)
        
        for i in range(m):
            if i in (0, m-1):
                for j in range(n):
                    if grid[i][j] == 1:
                        cur = visit(i, j)
            else:
                for j in (0, n-1):
                    if grid[i][j] == 1:
                        cur = visit(i, j)

        return sum(sum(x) for x in grid)
