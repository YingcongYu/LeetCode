# It is a sweltering summer day, and a boy wants to buy some ice cream bars.

# At the store, there are n ice cream bars. You are given an array costs of length n, where costs[i] is the price of the ith ice cream bar in coins. 
# The boy initially has coins coins to spend, and he wants to buy as many ice cream bars as possible. 

# Note: The boy can buy the ice cream bars in any order.

# Return the maximum number of ice cream bars the boy can buy with coins coins.

# You must solve the problem by counting sort.


class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        ref = [0] * (max(costs)+1)
        for i in costs:
            ref[i] += 1
        
        output = 0
        for i, n in enumerate(ref):
            for _ in range(n):
                if coins < i:
                    break
                coins -= i
                output += 1
            if coins < i:
                break
        return output
