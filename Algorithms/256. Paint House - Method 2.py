# There is a row of n houses, where each house can be painted one of three colors: red, blue, or green. 
#   The cost of painting each house with a certain color is different. You have to paint all the houses such that no two adjacent houses have the same color.

# The cost of painting each house with a certain color is represented by an n x 3 cost matrix costs.

# For example, costs[0][0] is the cost of painting house 0 with the color red; costs[1][2] is the cost of painting house 1 with color green, and so on...
# Return the minimum cost to paint all houses.


class Solution:
    def minCost(self, costs: List[List[int]]) -> int:
        ref = costs[0][:]

        for i in range(1, len(costs)):
            ref = [
                min(ref[1], ref[2]) + costs[i][0],
                min(ref[0], ref[2]) + costs[i][1],
                min(ref[0], ref[1]) + costs[i][2]
            ]
        
        return min(ref)
