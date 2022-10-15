# You are a professional robber planning to rob houses along a street. 
# Each house has a certain amount of money stashed, the only constraint stopping you from robbing each of them is that adjacent houses have security systems connected 
# and it will automatically contact the police if two adjacent houses were broken into on the same night.

# Given an integer array nums representing the amount of money of each house, return the maximum amount of money you can rob tonight without alerting the police.


class Solution:
    def rob(self, nums: List[int]) -> int:
        dp = {}
        
        def rob(i):
            if i >= len(nums):
                return 0
            if i in dp:
                return dp[i]
            dp[i] = max(rob(i+1), nums[i] + rob(i+2))
            return dp[i]
        
        return rob(0)
