# You are given an m x n integer array grid. There is a robot initially located at the top-left corner (i.e., grid[0][0]). 
# The robot tries to move to the bottom-right corner (i.e., grid[m-1][n-1]). The robot can only move either down or right at any point in time.

# An obstacle and space are marked as 1 or 0 respectively in grid. A path that the robot takes cannot include any square that is an obstacle.

# Return the number of possible unique paths that the robot can take to reach the bottom-right corner.

# The testcases are generated so that the answer will be less than or equal to 2 * 109.


class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        row = [0] * (len(obstacleGrid[0]) + 1)
        for i in range(len(obstacleGrid)-1, -1, -1):
            newRow = row
            for j in range(len(obstacleGrid[0])-1, -1, -1):
                if i == len(obstacleGrid)-1 and j == len(obstacleGrid[0])-1 and obstacleGrid[i][j] == 0:
                    newRow[j] = 1
                elif obstacleGrid[i][j] == 0:
                    newRow[j] = newRow[j+1] + row[j]
                else:
                    newRow[j] = 0
            row = newRow
        return row[0]
