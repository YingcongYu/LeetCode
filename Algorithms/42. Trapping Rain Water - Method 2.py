# Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it can trap after raining.


class Solution:
    def trap(self, height: List[int]) -> int:
        heighest = max(height)
        left = 0
        right = len(height) - 1
        output = heighest * (right+1) - sum(height)

        surface = 0
        while height[left] != heighest:
            if height[left] > surface:
                surface = height[left]
            output -= heighest - surface
            left += 1
        
        surface = 0
        while height[right] != heighest:
            if height[right] > surface:
                surface = height[right]
            output -= heighest - surface
            right -= 1
        
        return output
