# Given an integer array nums of length n where all the integers of nums are in the range [1, n] and each integer appears once or twice, 
# return an array of all the integers that appears twice.

# You must write an algorithm that runs in O(n) time and uses only constant extra space.


class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        ref = set()
        output = []

        for i in nums:
            if i in ref:
                output.append(i)
            else:
                ref.add(i)
        
        return output
