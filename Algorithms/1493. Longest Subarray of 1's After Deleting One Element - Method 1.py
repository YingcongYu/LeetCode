# Given a binary array nums, you should delete one element from it.

# Return the size of the longest non-empty subarray containing only 1's in the resulting array. Return 0 if there is no such subarray.


class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        output = 0
        pre = 0
        cur = 0

        for i in nums:
            if i == 1:
                cur += 1
            else:
                output = max(output, pre+cur)
                pre = cur
                cur = 0
        
        output = max(output, pre+cur)
        if cur == len(nums):
            output -= 1
        return output
