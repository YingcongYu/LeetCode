# You are given two strings word1 and word2. Merge the strings by adding letters in alternating order, starting with word1. 
# If a string is longer than the other, append the additional letters onto the end of the merged string.

# Return the merged string.


class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        answer = ""

        for i in range(min(len(word1), len(word2))):
            answer += word1[i] + word2[i]
        return answer + word1[min(len(word1), len(word2)):] + word2[min(len(word1), len(word2)):]
