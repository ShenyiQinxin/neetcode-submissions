class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        expected_sum = (n*(n+1))//2
        sum_nums = 0
        for num in nums:
            sum_nums += num
        return expected_sum-sum_nums


        