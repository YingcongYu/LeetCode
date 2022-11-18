# Given an array of strings words, return the words that can be typed using letters of the alphabet on only one row of American keyboard like the image below.

# In the American keyboard:

# the first row consists of the characters "qwertyuiop",
# the second row consists of the characters "asdfghjkl", and
# the third row consists of the characters "zxcvbnm".


class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        first_row = set(list('qwertyuiop'))
        second_row = set(list('asdfghjkl'))
        third_row = set(list('zxcvbnm'))
        output = []
        for i in words:
            temp = set(list(i.lower()))
            if temp == temp.intersection(first_row) or temp == temp.intersection(second_row) or temp == temp.intersection(third_row):
                output.append(i)
        return output
