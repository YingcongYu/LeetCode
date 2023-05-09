# Given an integer array nums, return all the different possible non-decreasing subsequences of the given array with at least two elements. 
# You may return the answer in any order.


class Solution:
    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
        def recursive(nums, path):
            if len(path) > 1:
                output.add(tuple(path))
            for i in range(len(nums)):
                if not path:
                    recursive(nums[i+1:], [nums[i]])
                elif nums[i] >= path[-1]:
                    recursive(nums[i+1:], path+[nums[i]])
        
        output = set()
        recursive(nums, [])
        return output
