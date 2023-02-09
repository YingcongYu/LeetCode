# Given an m x n matrix, return all elements of the matrix in spiral order.


class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        output = [0]*len(matrix)*len(matrix[0])
        index = 0
        m = 0
        m_min = 0
        m_max = len(matrix)-1
        n = 0
        n_min = 0
        n_max = len(matrix[0])-1

        while index < len(output):
            while n <= n_max:
                output[index] = matrix[m][n]
                index += 1
                n += 1
            if index >= len(output):
                break
            n -= 1
            m += 1
            m_min += 1
            while m <= m_max:
                output[index] = matrix[m][n]
                index += 1
                m += 1
            if index >= len(output):
                break
            m -= 1
            n -= 1
            n_max -= 1
            while n >= n_min:
                output[index] = matrix[m][n]
                index += 1
                n -= 1
            if index >= len(output):
                break
            n += 1
            m -= 1
            m_max -= 1
            while m >= m_min:
                output[index] = matrix[m][n]
                index += 1
                m -= 1
            if index >= len(output):
                break
            m += 1
            n += 1
            n_min += 1
        return output
