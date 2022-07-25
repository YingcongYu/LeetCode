# Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.

# Note that you must do this in-place without making a copy of the array.


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        start, end = 0, len(nums)-1
        while start < end:
            if nums[start] == 0:
                nums.pop(start)
                nums.append(0)
                end -= 1
            else:
                start += 1
        return nums
