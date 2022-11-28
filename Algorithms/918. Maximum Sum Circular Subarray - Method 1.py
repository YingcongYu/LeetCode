# Given a circular integer array nums of length n, return the maximum possible sum of a non-empty subarray of nums.

# A circular array means the end of the array connects to the beginning of the array. Formally, the next element of nums[i] is nums[(i + 1) % n] 
# and the previous element of nums[i] is nums[(i - 1 + n) % n].

# A subarray may only include each element of the fixed buffer nums at most once. Formally, for a subarray nums[i], nums[i + 1], ..., nums[j], 
# there does not exist i <= k1, k2 <= j with k1 % n == k2 % n.


class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        max_sum = nums[0]
        min_sum = nums[0]
        cur_max = nums[0]
        cur_min = nums[0]
        
        for i in nums[1:]:
            cur_max = max(cur_max+i, i)
            max_sum = max(max_sum, cur_max)
            cur_min = min(cur_min+i, i)
            min_sum = min(min_sum, cur_min)
        
        output = max(max_sum, sum(nums) - min_sum)
        if output != 0:
            return output
        else:
            return max_sum
