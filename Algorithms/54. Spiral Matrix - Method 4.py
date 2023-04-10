# Given an m x n matrix, return all elements of the matrix in spiral order.


class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        output = []
        m_min = 0
        m_max = len(matrix)-1
        n_min = 0
        n_max = len(matrix[0])-1

        while m_min <= m_max and n_min <= n_max:
            for i in range(n_min, n_max+1):
                output.append(matrix[m_min][i])
            m_min += 1
            for i in range(m_min, m_max+1):
                output.append(matrix[i][n_max])
            n_max -= 1
            if m_min <= m_max:
                for i in range(n_max, n_min-1, -1):
                    output.append(matrix[m_max][i])
                m_max -= 1
            if n_min <= n_max:
                for i in range(m_max, m_min-1, -1):
                    output.append(matrix[i][n_min])
                n_min += 1
        
        return output
