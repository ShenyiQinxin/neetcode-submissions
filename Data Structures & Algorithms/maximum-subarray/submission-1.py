class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        res = nums[0]
        max_s = nums[0]

        for i in range(1, len(nums)):
            # prev_s = max_s
            max_s = max(max_s+nums[i], nums[i])

            res = max(max_s, res)

        return res
        