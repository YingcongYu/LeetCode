# Given an integer array nums, return the number of subarrays filled with 0.

# A subarray is a contiguous non-empty sequence of elements within an array.


class Solution:
    def zeroFilledSubarray(self, nums: List[int]) -> int:
        output = 0
        temp = 0
        for i in nums:
            if i == 0:
                temp += 1
            else:
                for j in range(1,temp+1):
                    output += j
                temp = 0
        for j in range(1,temp+1):
            output += j
        return output
