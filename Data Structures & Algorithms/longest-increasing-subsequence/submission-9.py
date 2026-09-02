class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [1] * (n)

        for end in range(1, n):
            for start in range(end):
                if nums[end] > nums[start]:
                    dp[end] = max(dp[end], dp[start] + 1)
               
        return max(dp)

                
        
