# Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it can trap after raining.


class Solution:
    def trap(self, height: List[int]) -> int:
        def find(height):
            output = 0
            length = len(height)
            slow = 0
            
            while slow < length:
                if height[slow] > 0:
                    temp = []
                    for fast in range(slow+1, length):
                        if height[slow] <= height[fast]:
                            temp.append(min(height[slow],height[fast])*(fast-slow-1))
                            slow = fast-1
                            break
                        else:
                            temp.append(-height[fast])
                    if sum(temp) > 0:
                        output += sum(temp)
                slow += 1
            
            return output
        
        index = height.index(max(height))
        return find(height[:index+1]) + find(height[index:][::-1])
