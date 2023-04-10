# Given a positive integer n, generate an n x n matrix filled with elements from 1 to n2 in spiral order.


class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        output = [[0] * n for _ in range(n)]
        left = 0
        right = n-1
        up = 0
        down = n -1
        n = n**2
        cur = 1
        
        while cur <= n and up <= down and left <= right:
            for i in range(left, right+1):
                output[up][i] = cur
                cur += 1
            up += 1
            for i in range(up, down+1):
                output[i][right] = cur
                cur += 1
            right -= 1
            if up <= down:
                for i in range(right, left-1, -1):
                    output[down][i] = cur
                    cur += 1
                down -= 1
            if left <= right:
                for i in range(down, up-1, -1):
                    output[i][left] = cur
                    cur += 1
                left += 1
        
        return output
