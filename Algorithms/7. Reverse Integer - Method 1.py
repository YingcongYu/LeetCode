# Given a signed 32-bit integer x, return x with its digits reversed. If reversing x causes the value to go outside the signed 32-bit integer range [-231, 231 - 1], 
# then return 0.

# Assume the environment does not allow you to store 64-bit integers (signed or unsigned).


class Solution:
    def reverse(self, x: int) -> int:
        if x >= 0:
            x = str(x)
            new = 0
            length = 0
            while length < len(x):
                new += 10**length * int(x[length])
                length += 1
        else:
            x = str(-x)
            new = 0
            length = 0
            while length < len(x):
                new += 10**length * int(x[length])
                length += 1
            new = -new
        if new > 2**31 - 1 or new < -2**31:
            return 0
        else:
            return new
