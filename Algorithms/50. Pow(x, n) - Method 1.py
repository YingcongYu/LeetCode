# Implement pow(x, n), which calculates x raised to the power n (i.e., xn).


class Solution:
    def myPow(self, x: float, n: int) -> float:
        def recursive(x, n):
            if n == 0:
                return 1
            if n == 1:
                return x
            
            if n % 2 == 1:
                return recursive(x*x, n//2) * x
            else:
                return recursive(x*x, n//2)

        if n >= 0:
            return recursive(x, n)
        else:
            return 1 / recursive(x, abs(n))
