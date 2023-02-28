# You are given an integer array coins representing coins of different denominations and an integer amount representing a total amount of money.

# Return the fewest number of coins that you need to make up that amount. If that amount of money cannot be made up by any combination of the coins, return -1.

# You may assume that you have an infinite number of each kind of coin.


class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        outputs = [math.inf] * (amount+1)
        outputs[0] = 0

        for coin in coins:
            for i in range(coin, amount+1):
                outputs[i] = min(outputs[i], outputs[i-coin]+1)
        
        if outputs[-1] == math.inf:
            return -1
        else:
            return outputs[-1]
