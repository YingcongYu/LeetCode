# Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].

# The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

# You must write an algorithm that runs in O(n) time and without using the division operation.


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        left = [1]
        right = [1]

        for i in nums[:-1]:
            left.append(left[-1]*i)
        
        for i in range(len(nums)-1, 0, -1):
            right.append(right[-1]*nums[i])

        for i in range(len(nums)):
            nums[i] = left[i] * right[-i-1]

        return nums
