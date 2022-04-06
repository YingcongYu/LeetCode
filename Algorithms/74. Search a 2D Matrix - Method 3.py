# Write an efficient algorithm that searches for a value target in an m x n integer matrix matrix. This matrix has the following properties:

# Integers in each row are sorted from left to right.
# The first integer of each row is greater than the last integer of the previous row.

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        front, back = 0, len(matrix)-1
        while back >= front:
            mid = (back+front)//2
            if target in matrix[mid]:
                return True
            elif target < matrix[mid][0]:
                back = mid-1
            else:
                front = mid+1
        return False
