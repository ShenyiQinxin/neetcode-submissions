class Solution:
    def canJump(self, nums: List[int]) -> bool:
        furthest = 0
        for i in range(len(nums)):
            
            if furthest < i:
                return False
            furthest = max(furthest, i+nums[i])
        return True

        