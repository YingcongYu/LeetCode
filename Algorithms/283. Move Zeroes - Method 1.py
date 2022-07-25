# Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.

# Note that you must do this in-place without making a copy of the array.


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        extra = 0
        for i in range(len(nums)):
            if nums[i-extra] == 0:
                nums.append(0)
                nums.pop(i-extra)
                extra += 1
        return nums
