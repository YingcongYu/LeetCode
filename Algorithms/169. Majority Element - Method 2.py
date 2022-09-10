# Given an array nums of size n, return the majority element.

# The majority element is the element that appears more than ⌊n / 2⌋ times. You may assume that the majority element always exists in the array.


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        cur = nums[0]
        check = 1
        for i in nums[1:]:
            if check == 0:
                cur = i
            if i == cur:
                check += 1
            else:
                check -= 1
        return cur
