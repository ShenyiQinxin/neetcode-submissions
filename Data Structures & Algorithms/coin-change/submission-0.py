class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # base dp[0] = 0
        # option coins[i]
        # state: fewest coint needed to make amount
        dp = [100000] * (amount+1)
        dp[0] = 0

        for i in range(1, amount+1): #i is current amount trying to build
            
            for c in coins:
                if i - c >= 0:
                    dp[i] = min(dp[i], dp[i-c]+1) # the fewest number of coins
        
        if dp[amount] == 100000:
            return -1
        return dp[amount]
