# Write a function to find the longest common prefix string amongst an array of strings.

# If there is no common prefix, return an empty string "".


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        output = ''
        for i in zip(*strs):
            if len(set(i)) == 1:
                output += i[0]
            else:
                break
        return output
