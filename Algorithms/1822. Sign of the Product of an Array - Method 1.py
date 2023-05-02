# There is a function signFunc(x) that returns:

# 1 if x is positive.
# -1 if x is negative.
# 0 if x is equal to 0.
# You are given an integer array nums. Let product be the product of all values in the array nums.

# Return signFunc(product).


class Solution:
    def arraySign(self, nums: List[int]) -> int:
        flag = 1
        
        for i in nums:
            if i == 0:
                flag = 0
                break
            if i < 0:
                flag = -flag
        
        return flag
