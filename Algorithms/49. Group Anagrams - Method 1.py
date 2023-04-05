# Given an array of strings strs, group the anagrams together. You can return the answer in any order.

# An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        output = []
        ref = {}
        for i in strs:
            temp = ''.join(sorted(i))
            if temp in ref.keys():
                output[ref[temp]].append(i)
            else:
                output.append([i])
                ref[temp] = len(output) - 1
        return output
