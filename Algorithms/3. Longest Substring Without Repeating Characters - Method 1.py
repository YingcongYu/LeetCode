# Given a string s, find the length of the longest substring without repeating characters.


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        output = 0
        front = 0
        back = 1
        while front <= back and back <= len(s):
            if len(s[front:back]) == len(set(s[front:back])):
                output = max(output, len(s[front:back]))
                back += 1
            else:
                front += 1
        return output
