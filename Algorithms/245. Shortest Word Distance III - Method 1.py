# Given an array of strings wordsDict and two strings that already exist in the array word1 and word2, 
# return the shortest distance between the occurrence of these two words in the list.

# Note that word1 and word2 may be the same. It is guaranteed that they represent two individual words in the list.


class Solution:
    def shortestWordDistance(self, wordsDict: List[str], word1: str, word2: str) -> int:
        index1 = float('inf')
        index2 = float('inf')
        distance = float('inf')
        
        for i, n in enumerate(wordsDict):
            if n == word1:
                if word1 == word2:
                    index2 = index1
                index1 = i
            elif n == word2:
                index2 = i
            distance = min(distance, abs(index1 - index2))
        
        return distance
