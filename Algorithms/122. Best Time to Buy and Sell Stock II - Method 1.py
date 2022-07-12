# You are given an integer array prices where prices[i] is the price of a given stock on the ith day.

# On each day, you may decide to buy and/or sell the stock. You can only hold at most one share of the stock at any time. 
# However, you can buy it then immediately sell it on the same day.

# Find and return the maximum profit you can achieve.


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        current = prices[0]
        gain = 0
        for i in range(1, len(prices)-1):
            if prices[i-1] <= prices[i] >= prices[i+1] and prices[i] > current:
                gain += prices[i] - current
                current = 99999
            if prices[i-1] >= prices[i] <= prices[i+1] and prices[i] < current:
                current = prices[i]
        if current < prices[-1]:
            gain += prices[-1] - current
        return gain
