# Given a sorted array of distinct integers and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.

# You must write an algorithm with O(log n) runtime complexity.

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        low, high = 0, len(nums)-1
        while high >= low:
            md = (low + high) // 2
            if nums[md] == target:
                return md
            elif nums[md] < target:
                low = md + 1
            elif nums[md] > target:
                high = md - 1
        return low
