# Given an integer array nums of length n where all the integers of nums are in the range [1, n] and each integer appears once or twice, 
# return an array of all the integers that appears twice.

# You must write an algorithm that runs in O(n) time and uses only constant extra space.


class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        ref = collections.Counter(nums)
        output = []
        
        for i in set(nums):
            if ref[i] == 2:
                output.append(i)
        
        return output
