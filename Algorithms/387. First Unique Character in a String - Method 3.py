# Given a string s, find the first non-repeating character in it and return its index. If it does not exist, return -1.

class Solution:
    def firstUniqChar(self, s: str) -> int:
        for i, n in enumerate(s):
            if n not in s[i+1:len(s)] and n not in s[0:i]:
                return i
                break
        return -1
