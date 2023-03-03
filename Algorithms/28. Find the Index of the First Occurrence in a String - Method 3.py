# Given two strings needle and haystack, return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.


class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        start = 0
        end = len(needle)

        while end <= len(haystack):
            if haystack[start:end] == needle:
                return start
            else:
                start += 1
                end += 1
        
        return -1
