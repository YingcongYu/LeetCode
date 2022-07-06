# You are given an inclusive range [lower, upper] and a sorted unique integer array nums, where all elements are in the inclusive range.

# A number x is considered missing if x is in the range [lower, upper] and x is not in nums.

# Return the smallest sorted list of ranges that cover every missing number exactly. 
# That is, no element of nums is in any of the ranges, and each missing number is in one of the ranges.

# Each range [a,b] in the list should be output as:

# "a->b" if a != b
# "a" if a == b


class Solution:
    def findMissingRanges(self, nums: List[int], lower: int, upper: int) -> List[str]:
        output = []
        nums.insert(0, lower-1)
        nums.append(upper+1)
        for i in range(1, len(nums)):
            if nums[i] != nums[i-1]+1:
                if nums[i]-1 == nums[i-1]+1:
                    output.append(str(nums[i]-1))
                else:
                    output.append(str(nums[i-1]+1) + '->' + str(nums[i]-1))
        return output
