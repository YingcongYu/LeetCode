# Given a string s consisting of words and spaces, return the length of the last word in the string.

# A word is a maximal substring consisting of non-space characters only.


class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        last_letter = len(s) - 1
        while s[last_letter] == " ":
            last_letter -= 1

        first_letter = last_letter
        while first_letter >= 0 and s[first_letter] != " ":
            first_letter -= 1
        
        return last_letter - first_letter
