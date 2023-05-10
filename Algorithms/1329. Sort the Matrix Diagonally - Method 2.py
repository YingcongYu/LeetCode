# A matrix diagonal is a diagonal line of cells starting from some cell in either the topmost row or leftmost column 
# and going in the bottom-right direction until reaching the matrix's end. 
# For example, the matrix diagonal starting from mat[2][0], where mat is a 6 x 3 matrix, includes cells mat[2][0], mat[3][1], and mat[4][2].

# Given an m x n matrix mat of integers, sort each matrix diagonal in ascending order and return the resulting matrix.


class Solution:
    def diagonalSort(self, mat: List[List[int]]) -> List[List[int]]:
        m = len(mat)
        n = len(mat[0])
        dic = collections.defaultdict(list)

        for i in range(m):
            for j in range(n):
                dic[i-j].append(mat[i][j])
        
        for i in dic:
            dic[i].sort()
        
        for i in range(m):
            for j in range(n):
                mat[i][j] = dic[i-j].pop(0)
        
        return mat
