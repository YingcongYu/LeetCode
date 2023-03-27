# Given a m x n grid filled with non-negative numbers, find a path from top left to bottom right, which minimizes the sum of all numbers along its path.

# Note: You can only move either down or right at any point in time.


class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        row = []
        for i in range(n):
            row.append(sum(grid[-1][i:]))
        for i in range(m-2, -1, -1):
            new_row = grid[i]
            print(row)
            for j in range(n-1, -1, -1):
                if j != n-1:
                    new_row[j] += min(row[j], new_row[j+1])
                else:
                    new_row[j] += row[j]
            row = new_row
            print(row)
        return row[0]
