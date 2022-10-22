# Given an integer columnNumber, return its corresponding column title as it appears in an Excel sheet.

# For example:

# A -> 1
# B -> 2
# C -> 3
# ...
# Z -> 26
# AA -> 27
# AB -> 28 
# ...


class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        output = ''
        while columnNumber > 0:
            output = chr((columnNumber-1) % 26 + ord('A')) + output
            columnNumber = (columnNumber-1) // 26
        return output
