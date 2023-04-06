# The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this: 
#   (you may want to display this pattern in a fixed font for better legibility)

# P   A   H   N
# A P L S I I G
# Y   I   R
# And then read line by line: "PAHNAPLSIIGYIR"

# Write the code that will take a string and make this conversion given a number of rows:
# string convert(string s, int numRows);


class Solution:
    def convert(self, s: str, numRows: int) -> str:
        output = [''] * numRows
        flag = 0
        level = 0
        for i in s:
            output[level] += i
            if numRows > 1:
                if level == numRows-1:
                    flag = 1
                elif level == 0:
                    flag = 0
                if flag == 1:
                    level -= 1
                else:
                    level += 1
        return ''.join(output)
