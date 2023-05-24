# You are given two integers n and k and two integer arrays speed and efficiency both of length n. 
# There are n engineers numbered from 1 to n. speed[i] and efficiency[i] represent the speed and efficiency of the ith engineer respectively.

# Choose at most k different engineers out of the n engineers to form a team with the maximum performance.

# The performance of a team is the sum of their engineers' speeds multiplied by the minimum efficiency among their engineers.

# Return the maximum performance of this team. Since the answer can be a huge number, return it modulo 109 + 7.


class Solution:
    def maxPerformance(self, n: int, speed: List[int], efficiency: List[int], k: int) -> int:
        pairs = sorted([(speed[i], efficiency[i]) for i in range(n)], key = lambda x: x[1], reverse = True)
        output = 0
        selected = []
        heapq.heapify(selected)
        selected_performance = 0
        modulo = 10**9 + 7

        for num1, num2 in pairs:
            selected_performance += num1
            heapq.heappush(selected, num1)
            if len(selected) > k:
                selected_performance -= heapq.heappop(selected)
            output = max(output, selected_performance*num2)
        
        return output % modulo
