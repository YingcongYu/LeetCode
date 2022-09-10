# Write an efficient algorithm that searches for a value target in an m x n integer matrix matrix. This matrix has the following properties:

# Integers in each row are sorted in ascending from left to right.
# Integers in each column are sorted in ascending from top to bottom.


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        row = len(matrix) - 1
        col = 0
        while row >= 0 and col <= len(matrix[0]) - 1:
            if target == matrix[row][col]:
                return True
            if target < matrix[row][col]:
                row -= 1
            else:
                col += 1
        
        return False
