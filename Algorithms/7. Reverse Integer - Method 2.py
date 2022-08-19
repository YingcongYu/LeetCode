# Given a signed 32-bit integer x, return x with its digits reversed. If reversing x causes the value to go outside the signed 32-bit integer range [-231, 231 - 1], 
# then return 0.

# Assume the environment does not allow you to store 64-bit integers (signed or unsigned).


class Solution:
    def reverse(self, x: int) -> int:
        if x >= 0:
            x = str(x)
            x = x[::-1]
            x = int(x)
        else:
            x = str(-x)
            x = x[::-1]
            x = -int(x)
        if x > 2**31 - 1 or x < -2**31:
            return 0
        else:
            return x
