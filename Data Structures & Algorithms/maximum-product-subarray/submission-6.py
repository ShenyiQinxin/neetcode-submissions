class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        n = len(nums)
     
        prev_max, prev_min = nums[0], nums[0]
        max_prod = nums[0]

        for i in range(1, n):
            prev_max_tmp = prev_max
            prev_max = max(prev_max * nums[i], nums[i], prev_min * nums[i])
            prev_min = min(prev_min * nums[i], nums[i], prev_max_tmp * nums[i])
            max_prod = max(prev_max, max_prod)
            
        return max_prod


