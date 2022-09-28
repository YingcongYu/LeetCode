# Given a string s which consists of lowercase or uppercase letters, return the length of the longest palindrome that can be built with those letters.

# Letters are case sensitive, for example, "Aa" is not considered a palindrome here.


class Solution:
    def longestPalindrome(self, s: str) -> int:
        count = Counter(s)
        output = 0
        odd = False
        for i in set(s):
            if count[i] % 2 == 0:
                output += count[i]
            else:
                output += count[i] - 1
                odd = True
        if odd:
            return output + 1
        else:
            return output
