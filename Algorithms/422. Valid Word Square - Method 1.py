# Given an array of strings words, return true if it forms a valid word square.

# A sequence of strings forms a valid word square if the kth row and column read the same string, where 0 <= k < max(numRows, numColumns).


class Solution:
    def validWordSquare(self, words: List[str]) -> bool:
        rotate = [''.join(x) for x in itertools.zip_longest(*words, fillvalue = '')]
        return words == rotate
