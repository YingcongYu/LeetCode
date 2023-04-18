# You are given two strings word1 and word2. Merge the strings by adding letters in alternating order, starting with word1. 
# If a string is longer than the other, append the additional letters onto the end of the merged string.

# Return the merged string.


class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        index = 0
        length = len(word2)
        output = ''

        while index < length:
            try:
                output += word1[index] + word2[index]
                index += 1
            except:
                output += word2[index:]
                break
        
        if index >= length:
            output += word1[index:]
        
        return output
