class Solution:
    def numDecodings(self, s: str) -> int:

        # base
        # state dp[i] : number of ways from s[i ~...]
        # option single or pair

        dp = [0] * (len(s)+1)
        dp[len(s)] = 1 # if lawfully arrive there 
        for i in range(len(s)-1, -1, -1):
         
            if s[i] != '0':
                dp[i] += dp[i+1]

            if 10 <= int(s[i:i+2]) <= 26:
                dp[i] += dp[i+2]
      
        return dp[0]
