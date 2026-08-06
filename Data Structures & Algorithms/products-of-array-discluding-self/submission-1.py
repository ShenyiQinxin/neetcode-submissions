class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        rst = [1]*len(nums)
        prefix = 1
        for i in range(len(nums)):
            rst[i] = prefix
            prefix *= nums[i]

        subfix = 1
        for i in range(len(nums)-1, -1, -1):
            rst[i] *= subfix
            subfix *= nums[i]




        return rst
        
        