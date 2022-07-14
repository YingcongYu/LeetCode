# Given an array, rotate the array to the right by k steps, where k is non-negative.


class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        length = len(nums)
        nums[:] = nums[-(k%length):] +nums[:-(k%length)] 
