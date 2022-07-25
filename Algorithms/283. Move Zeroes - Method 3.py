# Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.

# Note that you must do this in-place without making a copy of the array.


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        zero_position = 0
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[i], nums[zero_position] = nums[zero_position], nums[i]
                zero_position += 1
        return nums
