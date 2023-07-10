# Given a string s and an integer k, return the length of the longest substring of s that contains at most k distinct characters.


class Solution:
    def lengthOfLongestSubstringKDistinct(self, s: str, k: int) -> int:
        end = 0
        output = 0

        for i in range(len(s)):
            while len(set(s[end:i+1])) > k:
                end += 1
            
            output = max(output, i - end + 1)
        
        return output
