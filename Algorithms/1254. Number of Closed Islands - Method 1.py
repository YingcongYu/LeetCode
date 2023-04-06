# Given a 2D grid consists of 0s (land) and 1s (water).  
# An island is a maximal 4-directionally connected group of 0s and a closed island is an island totally (all left, top, right, bottom) surrounded by 1s.

# Return the number of closed islands.


class Solution:
    def closedIsland(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        output = 0
        flag = [0]
        visited = [[False]*n for _ in range(m)]

        def visit(x, y):
            visited[x][y] = True
            if x in (0, m-1) or y in (0, n-1):
                flag[0] = 1
            if y < n-1:
                if grid[x][y+1] == 0 and not visited[x][y+1]:
                    visit(x, y+1)
            if y > 0:
                if grid[x][y-1] == 0 and not visited[x][y-1]:
                    visit(x, y-1)
            if x < m-1:
                if grid[x+1][y] == 0 and not visited[x+1][y]:
                    visit(x+1, y)
            if x > 0:
                if grid[x-1][y] == 0 and not visited[x-1][y]:
                    visit(x-1, y)

        for i in range(1, m-1):
            for j in range(1, n-1):
                if grid[i][j] == 0 and not visited[i][j]:
                    visit(i,j)
                    if flag[0] == 1:
                        flag[0] = 0
                    else:
                        output += 1
        return output
