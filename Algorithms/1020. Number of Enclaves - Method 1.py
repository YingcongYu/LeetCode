# You are given an m x n binary matrix grid, where 0 represents a sea cell and 1 represents a land cell.

# A move consists of walking from one land cell to another adjacent (4-directionally) land cell or walking off the boundary of the grid.

# Return the number of land cells in grid for which we cannot walk off the boundary of the grid in any number of moves.


class Solution:
    def numEnclaves(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        ref = [[False] * n for _ in range(m)]
        flag = [0]
        output = 0

        def visit(x, y, cur):
            ref[x][y] = True
            cur[0] += 1
            if x in (0, m-1) or y in (0, n-1):
                flag[0] = 1
            if x < m-1:
                if grid[x+1][y] == 1 and not ref[x+1][y]:
                    visit(x+1, y, cur)
            if x > 0:
                if grid[x-1][y] == 1 and not ref[x-1][y]:
                    visit(x-1, y, cur)
            if y < n-1:
                if grid[x][y+1] == 1 and not ref[x][y+1]:
                    visit(x, y+1, cur)
            if y > 0:
                if grid[x][y-1] == 1 and not ref[x][y-1]:
                    visit(x, y-1, cur)
            return cur[0]
        
        for i in range(1, m-1):
            for j in range(1, n-1):
                if grid[i][j] == 1 and not ref[i][j]:
                    cur = visit(i, j, [0])
                    if flag[0] == 0:
                        output += cur
                    flag[0] = 0
        
        return output
