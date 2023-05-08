# Given two sparse matrices mat1 of size m x k and mat2 of size k x n, return the result of mat1 x mat2. You may assume that multiplication is always possible.


class Solution:
    def multiply(self, mat1: List[List[int]], mat2: List[List[int]]) -> List[List[int]]:
        output = []

        for i in mat1:
            temp = []
            for j in zip(*mat2):
                temp.append(sum([i[x]*j[x] for x in range(len(i))]))
            output.append(temp)
        
        return output
