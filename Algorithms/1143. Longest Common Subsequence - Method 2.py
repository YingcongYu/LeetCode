# Given two strings text1 and text2, return the length of their longest common subsequence. If there is no common subsequence, return 0.

# A subsequence of a string is a new string generated from the original string with some characters (can be none) 
# deleted without changing the relative order of the remaining characters.

# For example, "ace" is a subsequence of "abcde".
# A common subsequence of two strings is a subsequence that is common to both strings.


class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        def recur(text1, text2, m, n, ref):
            if m == 0 or n == 0:
                return 0

            if ref[m][n] != 0:
                return ref[m][n]

            if text1[m-1] == text2[n - 1]:
                ref[m][n] = 1 + recur(text1, text2, m-1, n-1, ref)
                return ref[m][n]
            else:
                ref[m][n] = max(recur(text1, text2, m-1, n, ref), recur(text1, text2, m, n-1, ref))
                return ref[m][n]

        m = len(text1)
        n = len(text2)
        ref = [[0]*(n+1) for i in range(m+1)]
        return recur(text1, text2, m, n, ref)
