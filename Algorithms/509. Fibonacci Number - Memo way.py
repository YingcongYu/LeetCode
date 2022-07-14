# The Fibonacci numbers, commonly denoted F(n) form a sequence, called the Fibonacci sequence, 
# such that each number is the sum of the two preceding ones, starting from 0 and 1. That is,

# F(0) = 0, F(1) = 1
# F(n) = F(n - 1) + F(n - 2), for n > 1.
# Given n, calculate F(n).


class Solution:
    def fib(self, n: int) -> int:
        memo = [None] * (n+1)
        if memo[n] is not None:
            return memo[n]
        if n == 1:
            output = 1
        elif n == 0:
            output = 0
        else:
            output = self.fib(n-1) + self.fib(n-2)
        memo[n] = output
        return output
