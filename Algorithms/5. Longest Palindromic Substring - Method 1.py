# Given a string s, return the longest palindromic substring in s.

# A string is called a palindrome string if the reverse of that string is the same as the original string.


class Solution:
    def longestPalindrome(self, s: str) -> str:
        length = len(s)
        
        dp = [[0]*length for _ in range(length)]
        for i in range(length):
            dp[i][i] = True
        
        output = s[-1]
        
        for i in range(length-1, -1, -1):
            for j in range(i+1, length):
                if s[i] == s[j]:
                    if i == j-1 or dp[i+1][j-1] == True:
                        dp[i][j] = True
                        if len(s[i:j+1]) > len(output):
                            output = s[i:j+1]
        return output
