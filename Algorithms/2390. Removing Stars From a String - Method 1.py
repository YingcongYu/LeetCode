# You are given a string s, which contains stars *.

# In one operation, you can:

# Choose a star in s.
# Remove the closest non-star character to its left, as well as remove the star itself.
# Return the string after all stars have been removed.

# Note:

# The input will be generated such that the operation is always possible.
# It can be shown that the resulting string will always be unique.


class Solution:
    def removeStars(self, s: str) -> str:
        index = 0
        while index < len(s):
            if s[index] == '*':
                s = s[:index-1] + s[index+1:]
                index -= 1
            else:
                index += 1
        return s
