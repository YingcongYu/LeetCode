# You are given an integer array nums. You are initially positioned at the array's first index, 
# and each element in the array represents your maximum jump length at that position.

# Return true if you can reach the last index, or false otherwise.


class Solution:
    def canJump(self, nums: List[int]) -> bool:
        length = len(nums)
        current = 0
        for i, n in enumerate(nums):
            if current < i or current > length-1:
                break
            current = max(current, i+n)
        return current >= length-1
