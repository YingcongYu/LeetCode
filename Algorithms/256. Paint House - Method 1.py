# There is a row of n houses, where each house can be painted one of three colors: red, blue, or green. 
#   The cost of painting each house with a certain color is different. You have to paint all the houses such that no two adjacent houses have the same color.

# The cost of painting each house with a certain color is represented by an n x 3 cost matrix costs.

# For example, costs[0][0] is the cost of painting house 0 with the color red; costs[1][2] is the cost of painting house 1 with color green, and so on...
# Return the minimum cost to paint all houses.


class Solution:
    def minCost(self, costs: List[List[int]]) -> int:
        from functools import cache
        @cache
        
        def dfs(i, prevColor):
            if i == len(costs):
                return 0
            
            res = float('inf')
            for color in range(3):
                if color != prevColor:
                    res = min(res, costs[i][color]+dfs(i+1,color))
            return res
        
        return dfs(0, -1)
