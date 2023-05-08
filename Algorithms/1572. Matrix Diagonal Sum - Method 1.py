# Given a square matrix mat, return the sum of the matrix diagonals.

# Only include the sum of all the elements on the primary diagonal and all the elements on the secondary diagonal that are not part of the primary diagonal.


class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        front = 0
        end = len(mat) - 1
        output = 0

        for i in mat:
            if front == end:
                output += i[front]
            else:
                output += i[front] + i[end]
            front += 1
            end -= 1
        
        return output
