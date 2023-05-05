# Given a string s and an integer k, return the maximum number of vowel letters in any substring of s with length k.

# Vowel letters in English are 'a', 'e', 'i', 'o', and 'u'.


class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowels = ['a', 'e', 'i', 'o', 'u']
        output = 0
        count = 0
        left = 0
        right = 0

        while right < len(s):
            if s[right] in vowels:
                    count += 1
                    output = max(output, count)
            if output == k:
                return output
            
            if right - left + 1 == k:
                if s[left] in vowels:
                    count -= 1
                left += 1
            right += 1
        
        return output
