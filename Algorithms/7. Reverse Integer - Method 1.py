# Given a signed 32-bit integer x, return x with its digits reversed. If reversing x causes the value to go outside the signed 32-bit integer range [-231, 231 - 1], 
# then return 0.

# Assume the environment does not allow you to store 64-bit integers (signed or unsigned).


class Solution:
    def reverse(self, x: int) -> int:
        if x >= 0:
            new = list(str(x))
            new.reverse()
            x = 0
            length = len(new)-1
            for i in new:
                x += 10**length * int(i)
                length -= 1
        else:
            new = list(str(-x))
            new.reverse()
            x = 0
            length = len(new)-1
            for i in new:
                x += 10**length * int(i)
                length -= 1
            x = -x
        if x > 2**31 - 1 or x < -2**31:
            return 0
        else:
            return x
