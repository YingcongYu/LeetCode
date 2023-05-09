# You are given an array of integers nums and an integer target.

# Return the number of non-empty subsequences of nums such that the sum of the minimum and maximum element on it is less or equal to target. 
# Since the answer may be too large, return it modulo 109 + 7.


class Solution:
    def numSubseq(self, nums: List[int], target: int) -> int:
        nums.sort()
        front = 0
        end = len(nums) - 1
        output = 0
        
        while front <= end:
            if nums[front] + nums[end] > target:
                end -= 1
            elif nums[front] + nums[end] <= target:
                output += pow(2, end-front, 10**9+7)
                front += 1
        
        return output % (10**9 + 7)
