# You are given an integer array nums. In one move, you can pick an index i where 0 <= i < nums.length and increment nums[i] by 1.

# Return the minimum number of moves to make every value in nums unique.

# The test cases are generated so that the answer fits in a 32-bit integer.


class Solution:
    def minIncrementForUnique(self, nums: List[int]) -> int:
        nums.sort()
        output = 0
        prev = nums[0]
        for i in nums[1:]:
            if i <= prev:
                output += prev - i + 1
                prev += 1
            else:
                prev = i
        return output
