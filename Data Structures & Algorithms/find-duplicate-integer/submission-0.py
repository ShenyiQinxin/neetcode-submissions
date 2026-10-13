class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        slow, fast = nums[0], nums[0]
        # find the meeting point
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break

        # find the dup
        slow = nums[0] 
        while slow != fast:
            slow = nums[slow]
            fast = nums[fast]
        return slow







        
        