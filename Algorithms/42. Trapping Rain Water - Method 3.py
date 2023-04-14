# Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it can trap after raining.


class Solution:
    def trap(self, height: List[int]) -> int:
        left = 0
        right = len(height)-1
        left_max_height = height[left]
        right_max_height = height[right]
        output = 0

        while left < right:
            if left_max_height < right_max_height:
                left += 1
                left_max_height = max(height[left], left_max_height)
                output += left_max_height - height[left]
            else:
                right -= 1
                right_max_height = max(right_max_height, height[right])
                output += right_max_height - height[right]
                
        return output
