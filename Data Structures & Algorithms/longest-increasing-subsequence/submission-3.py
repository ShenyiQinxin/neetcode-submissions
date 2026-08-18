class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:

        dp = [1] * len(nums)

        for end in range(1, len(nums)):
            for start in range(end):
                if nums[start] < nums[end]:
                    
                    dp[end] = max(dp[end], dp[start] + 1)
                    # print(dp[end])
        return max(d for d in dp)

        
        