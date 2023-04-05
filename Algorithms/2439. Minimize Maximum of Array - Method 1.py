# You are given a 0-indexed array nums comprising of n non-negative integers.

# In one operation, you must:

# Choose an integer i such that 1 <= i < n and nums[i] > 0.
# Decrease nums[i] by 1.
# Increase nums[i - 1] by 1.

# Return the minimum possible value of the maximum integer of nums after performing any number of operations.


class Solution:
    def minimizeArrayValue(self, nums: List[int]) -> int:
        output = 0
        cur_sum = 0
        for i in range(len(nums)):
            cur_sum += nums[i]
            output = max(output, math.ceil(cur_sum/(i+1)))
        return output
