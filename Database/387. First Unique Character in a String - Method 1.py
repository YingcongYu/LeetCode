# Given a string s, find the first non-repeating character in it and return its index. If it does not exist, return -1.

class Solution:
    def firstUniqChar(self, s: str) -> int:
        for i, n in enumerate(s):
            if s.count(n) == 1:
                return i
                break
        return -1
