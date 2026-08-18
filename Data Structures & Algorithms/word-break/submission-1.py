class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dp = [False] * (len(s)+1) 
        # can the prefix be segmented into dictionary word
        dp[0] = True

        for end in range(1, len(s)+1):
            for start in range(end):

                if dp[start] and s[start:end] in wordDict:
                    dp[end] = True
        return dp[len(s)]


        