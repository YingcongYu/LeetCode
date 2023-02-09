# Given an m x n matrix, return all elements of the matrix in spiral order.


class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        index = 0
        output = []

        while matrix:
            if index % 4 == 0:
                output += matrix.pop(0)
            elif index % 4 == 1:
                output += [x.pop() for x in matrix if x]
            elif index % 4 == 2:
                output += matrix.pop()[::-1]
            else:
                output += [x.pop(0) for x in matrix if x][::-1]
            index += 1
        
        return output
