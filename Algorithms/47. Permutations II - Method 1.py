# Given a collection of numbers, nums, that might contain duplicates, return all possible unique permutations in any order.


class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        def recursive(nums, cur, output):
            if not nums:
                if cur not in output:
                    output.append(cur)
            for i in range(len(nums)):
                recursive(nums[:i]+nums[i+1:], cur+[nums[i]], output)      
        
        output = []
        recursive(nums, [], output)
        return output
