# A matrix diagonal is a diagonal line of cells starting from some cell in either the topmost row or leftmost column 
# and going in the bottom-right direction until reaching the matrix's end. 
# For example, the matrix diagonal starting from mat[2][0], where mat is a 6 x 3 matrix, includes cells mat[2][0], mat[3][1], and mat[4][2].

# Given an m x n matrix mat of integers, sort each matrix diagonal in ascending order and return the resulting matrix.


class Solution:
    def diagonalSort(self, mat: List[List[int]]) -> List[List[int]]:
        m = len(mat)
        n = len(mat[0])
        output = [[0]*n for _ in range(m)]
        row = 0
        col = n-1
        
        while row < m:
            if col > 0:
                temp = 0
                for num in sorted([mat[i][col+i] for i in range(min(n-col, m))]):
                    output[temp][col+temp] = num
                    temp += 1
                col -= 1
            else:
                temp = 0
                for num in sorted([mat[row+i][col+i] for i in range(min(m-row, n))]):
                    output[row+temp][col+temp] = num
                    temp += 1
                row += 1
        
        return output
