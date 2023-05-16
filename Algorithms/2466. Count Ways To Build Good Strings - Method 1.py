# Given the integers zero, one, low, and high, we can construct a string by starting with an empty string, and then at each step perform either of the following:

# Append the character '0' zero times.
# Append the character '1' one times.
# This can be performed any number of times.

# A good string is a string constructed by the above process having a length between low and high (inclusive).

# Return the number of different good strings that can be constructed satisfying these properties. Since the answer can be large, return it modulo 109 + 7.


class Solution:
    def countGoodStrings(self, low: int, high: int, zero: int, one: int) -> int:
        def recursive(length):
            if length > high:
                return 0
            if length not in ref:
                if low <= length <= high:
                    ref[length] = (recursive(length + zero) + recursive(length + one) + 1) % (10**9 + 7)
                else:
                    ref[length] = (recursive(length + zero) + recursive(length + one)) % (10**9 + 7)
            return ref[length]
        
        ref = {}
        recursive(0)
        return ref[0] % (10**9 + 7)
