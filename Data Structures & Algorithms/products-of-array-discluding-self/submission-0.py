class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix_nums = []
        subfix_nums = []

        prefix = 1
        for i in range(len(nums)):
            prefix_nums.append(prefix)
            prefix *= nums[i]

        subfix = 1
        for i in range(len(nums)-1, -1, -1):
            subfix_nums.append(subfix)
            subfix *= nums[i]
        subfix_nums.reverse()

        rst = []
        for i in range(len(nums)):
            rst.append(prefix_nums[i] * subfix_nums[i])

        return rst
        
        