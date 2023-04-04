# Given an array nums of distinct integers, return all the possible permutations. You can return the answer in any order.


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        def recursive(nums, cur, output):
            if not nums:
                output.append(cur)
            for i in range(len(nums)):
                recursive(nums[:i]+nums[i+1:], cur+[nums[i]], output)      
        
        output = []
        recursive(nums, [], output)
        return output
