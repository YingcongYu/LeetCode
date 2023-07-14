# Given an integer array arr and an integer difference, 
# return the length of the longest subsequence in arr which is an arithmetic sequence 
# such that the difference between adjacent elements in the subsequence equals difference.

# A subsequence is a sequence that can be derived from arr by deleting some or no elements without changing the order of the remaining elements.


class Solution:
    def longestSubsequence(self, arr: List[int], difference: int) -> int:
        visited = {}
        output = 1

        for i in range(len(arr) - 1, -1, -1):
            try:
                visited[arr[i]] = visited[arr[i]+difference] + 1
                output = max(output, visited[arr[i]])
            except:
                visited[arr[i]] = 1
        
        return output
