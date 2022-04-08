# Given a string s, find the first non-repeating character in it and return its index. If it does not exist, return -1.

class Solution:
    def firstUniqChar(self, s: str) -> int:
        for i, j in Counter(s).items():
            if j == 1:
                return s.index(i)
                break
        return -1
