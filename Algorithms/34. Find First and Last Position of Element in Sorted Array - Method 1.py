# Given an array of integers nums sorted in non-decreasing order, find the starting and ending position of a given target value.

# If target is not found in the array, return [-1, -1].

# You must write an algorithm with O(log n) runtime complexity.


class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if nums:
            low = 0
            high = len(nums) - 1
            left = -1
            right = -1
            while low <= high:
                mid = (low + high) // 2
                if nums[mid] == target:
                    left = mid
                if nums[mid] >= target:
                    high = mid - 1
                else:
                    low = mid + 1
            
            low = 0
            high = len(nums) - 1
            while low <= high:
                mid = (low + high) // 2
                if nums[mid] == target:
                    right = mid
                if nums[mid] <= target:
                    low = mid + 1
                else:
                    high = mid - 1
                    
            if left <= right:
                return [left, right]
        
        return [-1, -1]
