class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        set1 = set(nums)
        max_count = 0
        for n in nums:
            if n-1 not in set1:
                count = 1
                while n+1 in set1:
                    count+=1
                    n+=1
                max_count = max(max_count, count)
        return max_count
            

        