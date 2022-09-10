# Write an efficient algorithm that searches for a value target in an m x n integer matrix matrix. This matrix has the following properties:

# Integers in each row are sorted in ascending from left to right.
# Integers in each column are sorted in ascending from top to bottom.


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        for i in matrix:
            if target in i:
                return True
        return False
