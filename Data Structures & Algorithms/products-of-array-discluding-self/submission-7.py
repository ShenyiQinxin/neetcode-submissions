class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        prefix, surfix = 1, 1
        arr = [0] * n

        for i in range(n):
            arr[i] = prefix
            prefix *= nums[i]
        
        for i in range(n-1, -1, -1):
            arr[i] *= surfix
            surfix *= nums[i]
        return arr
