class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        q = deque()
        l = 0
        res = []

        for r in range(len(nums)):
            while q and nums[q[-1]] < nums[r]: # 1 2 1 0
                q.pop() # continue poping the back 
            q.append(r) 
            if r-l+1 == k:
                res.append(nums[q[0]])
                l+=1
                if q[0] < l: # older than the window
                    q.popleft()
            
        return res

        