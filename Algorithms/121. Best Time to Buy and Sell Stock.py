class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        buy = float(inf)
        for i in prices:
            profit = max(profit, i-buy)
            buy = min(buy, i)
        return profit
