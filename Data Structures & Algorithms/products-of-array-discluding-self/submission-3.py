class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # [1, 1,2,8,48]
        # [48,48,24,6, 1]
        res = [1] * len(nums)
        prefix = 1
        for i in range(len(nums)):
            res[i] = prefix
            prefix = nums[i] * prefix
        subfix = 1
        for i in range(len(nums)-1, -1, -1):
            res[i] *= subfix
            subfix = nums[i] * subfix
        return res
            
        
            
        