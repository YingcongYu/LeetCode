# Given a string s and an integer k, return the length of the longest substring of s that contains at most k distinct characters.


class Solution:
    def lengthOfLongestSubstringKDistinct(self, s: str, k: int) -> int:
        end = 0
        output = 0
        letters = {}

        for i, n in enumerate(s):
            letters[n] = letters.get(n, 0) + 1
            
            while len(letters) > k:
                letters[s[end]] -= 1
                if letters[s[end]] == 0:
                    del letters[s[end]]
                end += 1
            
            output = max(output, i - end + 1)
        
        return output
