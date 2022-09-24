# Given an integer n, return the decimal value of the binary string formed by concatenating the binary representations of 1 to n in order, modulo 109 + 7.


class Solution:
    def concatenatedBinary(self, n: int) -> int:
        output = ''
        start = 0
        while start < n:
            start += 1
            output += bin(start)[2:]
        return int(output, 2) % (10**9 + 7)
