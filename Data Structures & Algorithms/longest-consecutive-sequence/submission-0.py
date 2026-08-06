class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums_set = set(nums)
        max_len = 0
        for num in nums_set:
            
            if num -1 in nums_set:
                # num is not a begining
                continue
            # num is a begining
            count_len = 1
            curr = num
            while curr+1 in nums_set:
                curr = curr+1
                count_len+=1
            
            max_len = max(count_len, max_len)
        
        return max_len




        