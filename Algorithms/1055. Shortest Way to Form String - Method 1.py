# A subsequence of a string is a new string that is formed from the original string 
# by deleting some (can be none) of the characters without disturbing the relative positions of the remaining characters. 
# (i.e., "ace" is a subsequence of "abcde" while "aec" is not).

# Given two strings source and target, return the minimum number of subsequences of source such that their concatenation equals target. 
# If the task is impossible, return -1.


class Solution:
    def shortestWay(self, source: str, target: str) -> int:
        s_index = 0
        s_length = len(source)
        t_index = 0
        pre_t = 0
        output = 0

        while t_index < len(target):
            for i in range(s_index, s_length):
                if source[i] == target[t_index]:
                    s_index = i+1
                    pre_t = t_index
                    t_index += 1
                if i == s_length - 1:
                    if pre_t == t_index:
                        return -1
                    s_index = 0
                    output += 1
                    pre_t = t_index
                elif t_index == len(target):
                    output += 1
                    break
        
        return output
