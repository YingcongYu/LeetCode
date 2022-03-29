# Given an integer numRows, return the first numRows of Pascal's triangle.

class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        new = [[1]]
        if numRows == 1:
            return new
        elif numRows == 0:
            return []
        else:
            for i in range(1, numRows):
                row = [1]
                for n in range(1, i):
                    row.append(new[i-1][n-1] + new[i-1][n])
                row.append(1)
                new.append(row)
            return new
