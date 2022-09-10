# Write an efficient algorithm that searches for a value target in an m x n integer matrix matrix. This matrix has the following properties:

# Integers in each row are sorted in ascending from left to right.
# Integers in each column are sorted in ascending from top to bottom.


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        for i in matrix:
            if i[0] <= target <= i[-1]:
                front = 0
                back = len(i) - 1
                while front <= back:
                    mid = (front + back) // 2
                    if i[mid] == target:
                        return True
                    if i[mid] > target:
                        back = mid - 1
                    else:
                        front = mid + 1
        return False
