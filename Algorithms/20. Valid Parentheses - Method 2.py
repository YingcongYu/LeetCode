# Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

# An input string is valid if:

# Open brackets must be closed by the same type of brackets.
# Open brackets must be closed in the correct order.


class Solution:
    def isValid(self, s: str) -> bool:
        d = {")":"(", "]":"[", "}":"{"}
        l = ['l']
        for i in s:
            if i in d.keys():
                if d[i] != l.pop():
                    return False
            else:
                l.append(i)
        return len(l) == 1