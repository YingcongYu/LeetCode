# Given a string s and an integer k, return the maximum number of vowel letters in any substring of s with length k.

# Vowel letters in English are 'a', 'e', 'i', 'o', and 'u'.


class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        max_vowels = 0
        vowels = {'a', 'e', 'i', 'o', 'u'}

        for l in s[:k]:
            if l in vowels:
                max_vowels += 1

        temp = max_vowels
        for l1, l2 in zip(s, s[k:]):
            if l2 in vowels:
                temp += 1
            if l1 in vowels:
                temp -= 1

            if temp == k:
                return k
            elif temp > max_vowels:
                max_vowels = temp

        return max_vowels
