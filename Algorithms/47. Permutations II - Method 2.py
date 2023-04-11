# Given a collection of numbers, nums, that might contain duplicates, return all possible unique permutations in any order.


class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        def recursive(counter, cur):
            if len(cur) == len(nums):
                output.append(cur)
                return
            for i in counter:
                if counter[i] > 0:
                    counter[i] -= 1
                    recursive(counter, cur+[i])
                    counter[i] += 1 
        
        output = []
        recursive(collections.Counter(nums), [])
        return output
