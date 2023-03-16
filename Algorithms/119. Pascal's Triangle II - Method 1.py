# Given an integer rowIndex, return the rowIndexth (0-indexed) row of the Pascal's triangle.


class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        rowIndex += 1
        output = [[1]]
        if rowIndex == 1:
            return output[0]
        elif rowIndex == 0:
            return []
        else:
            for i in range(1, rowIndex):
                row = [1]
                for n in range(1, i):
                    row.append(output[i-1][n-1] + output[i-1][n])
                row.append(1)
                output.append(row)
            return output[-1]
