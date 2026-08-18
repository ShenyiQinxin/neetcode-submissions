class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        # base
        # state
        # option
       
        res = nums[0]
        max_p, min_p = nums[0], nums[0]

     
        for i in range(1, len(nums)):
            prev_max = max_p
            prev_min = min_p

            max_p = max(prev_max*nums[i], prev_min*nums[i], nums[i])
            min_p = min(prev_min*nums[i], prev_max*nums[i], nums[i])
            
            res = max(res, max_p)
        return res
        




        