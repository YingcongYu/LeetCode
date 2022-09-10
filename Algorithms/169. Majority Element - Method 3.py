# Given an array nums of size n, return the majority element.

# The majority element is the element that appears more than ⌊n / 2⌋ times. You may assume that the majority element always exists in the array.


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = 0
        output = 0
        for i, n in Counter(nums).items():
            if n == max(count, n):
                output = i
                count = n
        return output
