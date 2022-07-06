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
        if len(nums) == 0:
            if lower == upper:
                output.append(str(lower))
            else:
                output.append(str(lower) + '->' + str(upper))
        elif nums[0] > lower:
                if nums[0]-1 == lower:
                    output.append(str(nums[0]-1))
                else:
                    output.append(str(lower) + '->' + str(nums[0]-1))
        for i, n in enumerate(nums):
            if i == len(nums) - 1:
                if lower == upper:
                    return []
                if n == upper:
                    break
                if n < upper:
                    if n+1 == upper:
                        output.append(str(n+1))
                    else:
                        output.append(str(n+1) + '->' + str(upper))
            elif n+1 != nums[i+1]:
                if n+2 == nums[i+1]:
                    output.append(str(n+1))
                else:
                    output.append(str(n+1) + '->' + str(nums[i+1]-1))
        return output
