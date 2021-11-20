# Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

# An input string is valid if:

# Open brackets must be closed by the same type of brackets.
# Open brackets must be closed in the correct order.

class Solution:
    def isValid(self, s: str) -> bool:
        l = []
        for i in range(0, len(s)):
            if s[i] == '(' or s[i] == '[' or s[i] == '{':
                l.append(s[i])
            elif s[i] == ')':
                if len(l) == 0:
                    return False
                elif l[-1] == '(':
                    l.pop()
                else:
                    return False
            elif s[i] == ']':
                if len(l) == 0:
                    return False
                elif l[-1] == '[':
                    l.pop()
                else:
                    return False
            elif s[i] == '}':
                if len(l) == 0:
                    return False
                elif l[-1] == '{':
                    l.pop()
                else:
                    return False
        if len(l) == 0:
            return True
        else:
            return False
                
