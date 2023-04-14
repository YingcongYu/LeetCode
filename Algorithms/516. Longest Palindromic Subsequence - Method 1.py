# Given a string s, find the longest palindromic subsequence's length in s.

# A subsequence is a sequence that can be derived from another sequence by deleting some or no elements without changing the order of the remaining elements.


class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        s2 = s[::-1]
        length = len(s)
        dp = [0] * length
        for letter in s2:
            temp = 0
            for i in range(length):
                if temp < dp[i]:
                    temp = dp[i]
                elif letter == s[i]:
                    dp[i] = temp + 1
        return max(dp)
