# Given a string text and an array of strings words, return an array of all index pairs [i, j] so that the substring text[i...j] is in words.

# Return the pairs [i, j] in sorted order (i.e., sort them by their first coordinate, and in case of ties sort them by their second coordinate).


class Solution:
    def indexPairs(self, text: str, words: List[str]) -> List[List[int]]:
        output = []
        
        for i in words:
            right = len(i)
            left = 0
            while right <= len(text):
                if text[left:right] == i:
                    output.append([left, right-1])
                left += 1
                right += 1
        
        return sorted(output, key = lambda x:(x[0], x[1]))
