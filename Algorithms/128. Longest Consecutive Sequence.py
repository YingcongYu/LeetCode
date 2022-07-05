# Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence.

# You must write an algorithm that runs in O(n) time.\


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if nums:
            nums = sorted(list(set(nums)))
            possibles = []
            length = 1
            for i in range(1, len(nums)):
                if nums[i] - nums[i-1] == 1:
                    length += 1
                else:
                    possibles.append(length)
                    length = 1
            possibles.append(length)
            return max(possibles)
        else:
            return 0
