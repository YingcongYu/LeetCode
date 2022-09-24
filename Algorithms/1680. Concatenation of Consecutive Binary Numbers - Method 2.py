# Given an integer n, return the decimal value of the binary string formed by concatenating the binary representations of 1 to n in order, modulo 109 + 7.


class Solution:
    def concatenatedBinary(self, n: int) -> int:
        output = ''
        for i in range(1, n+1):
            output += bin(i)[2:]
        return int(output, 2) % (10**9 + 7)
