class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        n = len(s)
        dp = [False] * (n+1)
        dp[0] =True

        for end in range(1, n+1):
            for start in range(end):
                if dp[start] and s[start:end] in wordDict:
                    dp[end] = True
        return dp[-1]
        