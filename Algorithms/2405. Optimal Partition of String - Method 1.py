# Given a string s, partition the string into one or more substrings such that the characters in each substring are unique. 
# That is, no letter appears in a single substring more than once.

# Return the minimum number of substrings in such a partition.

# Note that each character should belong to exactly one substring in a partition.


class Solution:
    def partitionString(self, s: str) -> int:
        output = 0
        pre = ''
        for i in s:
            if i in pre:
                output += 1
                pre = i
            else:
                pre += i
        return output + 1 
