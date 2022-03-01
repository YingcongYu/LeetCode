# Given a string columnTitle that represents the column title as appear in an Excel sheet, return its corresponding column number.

class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        output = 0
        for i in columnTitle:
            output = ord(i) - ord('A') + 1 + output*26
        return output
