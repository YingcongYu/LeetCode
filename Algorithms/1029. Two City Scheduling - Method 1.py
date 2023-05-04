# A company is planning to interview 2n people. Given the array costs where costs[i] = [aCosti, bCosti], 
# the cost of flying the ith person to city a is aCosti, and the cost of flying the ith person to city b is bCosti.

# Return the minimum cost to fly every person to a city such that exactly n people arrive in each city.


class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        costs.sort(key = lambda x: x[0]-x[1])
        output = 0
        middle = len(costs) // 2

        for i in range(len(costs)):
            if i < middle:
                output += costs[i][0]
            else:
                output += costs[i][1]

        return output
