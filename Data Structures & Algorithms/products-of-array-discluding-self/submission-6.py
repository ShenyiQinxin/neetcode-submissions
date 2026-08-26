class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [1] * len(nums)
        prefix = 1

        for i in range(len(nums)):
            res[i] = prefix
            prefix *= nums[i]

        surfix = 1
        for i in range(len(nums)-1, -1, -1):
            res[i] *= surfix
            surfix *= nums[i]
        # print(res)
        return res
        