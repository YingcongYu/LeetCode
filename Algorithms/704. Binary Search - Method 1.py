# Given an array of integers nums which is sorted in ascending order, and an integer target, write a function to search target in nums. 
# If target exists, then return its index. Otherwise, return -1.

# You must write an algorithm with O(log n) runtime complexity.


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        front = 0
        end = len(nums) - 1
        while front <= end:
            mid = (front + end) // 2
            if nums[mid] == target:
                return mid
            if nums[mid] > target:
                end = mid - 1
            else:
                front = mid + 1
        return -1
