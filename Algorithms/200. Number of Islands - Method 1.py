# Given an m x n 2D binary grid grid which represents a map of '1's (land) and '0's (water), return the number of islands.

# An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. 
# You may assume all four edges of the grid are all surrounded by water.


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        m = len(grid)
        n = len(grid[0])
        output = 0
        visited = [[False]*n for _ in range(m)]
        
        def visit(x, y):
            visited[x][y] = True
            if y < n-1:
                if grid[x][y+1] == '1' and not visited[x][y+1]:
                    visit(x, y+1)
            if y > 0:
                if grid[x][y-1] == '1' and not visited[x][y-1]:
                    visit(x, y-1)
            if x < m-1:
                if grid[x+1][y] == '1' and not visited[x+1][y]:
                    visit(x+1, y)
            if x > 0:
                if grid[x-1][y] == '1' and not visited[x-1][y]:
                    visit(x-1, y)
        
        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1' and not visited[i][j]:
                    visit(i,j)
                    output += 1
        return output
