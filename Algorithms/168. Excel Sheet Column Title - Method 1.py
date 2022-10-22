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
            if columnNumber % 26 == 0:
                output += 'Z'
                columnNumber = columnNumber // 26 - 1
            else:
                output += chr((columnNumber % 26) + ord('A') - 1)
                columnNumber = columnNumber // 26
        return output[::-1]
