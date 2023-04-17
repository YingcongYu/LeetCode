# An integer n is strictly palindromic if, for every base b between 2 and n - 2 (inclusive), the string representation of the integer n in base b is palindromic.

# Given an integer n, return true if n is strictly palindromic and false otherwise.

# A string is palindromic if it reads the same forward and backward.


class Solution:
    def isStrictlyPalindromic(self, n: int) -> bool:
        for i in range(2, n-1):
            num = ''
            temp = n
            
            while temp // i != 0:
                num += str(temp % i)
                temp = temp // i
            num += str(temp % i)
            
            if num != num[::-1]:
                return False
        
        return True
