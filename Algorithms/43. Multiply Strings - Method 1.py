# Given two non-negative integers num1 and num2 represented as strings, return the product of num1 and num2, also represented as a string.

# Note: You must not use any built-in BigInteger library or convert the inputs to integer directly.


class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        nums = []
        for i in range(10):
            nums.append(str(i))
        
        def convert(num):
            output = 0
            for i, n in enumerate(num[::-1]):
                output += nums.index(n) * (10 ** i)
            return output
        
        return str(convert(num1) * convert(num2))
