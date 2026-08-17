class Solution:
    def climbStairs(self, n: int) -> int:
        # base 
        # state
        # option 
        if n == 1:
            return 1
        dp = [0] * (n+1)
        dp[1] = 1
        dp[2] = 2
        # dp[3] = 3
        # dp[4] = 5
        # dp[5] = 6
        for i in range(3, n+1):
            dp[i] = dp[i-1] + dp [i-2]
        return dp[n] 



