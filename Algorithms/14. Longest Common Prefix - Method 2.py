# Write a function to find the longest common prefix string amongst an array of strings.

# If there is no common prefix, return an empty string "".


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        output = strs[0]
        for i in strs:
            while not i.startswith(output):
                output = output[:-1]
        return output
