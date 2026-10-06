class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # binary search on the answer — searching speeds from 1 up to the max pile value, checking if that speed lets her finish in time.
        l, r = 1, max(piles)
        
        while l < r:
            hours = 0
            mid = (l+r)//2
            for p in piles:
                hour = math.ceil(p/mid)
                hours += hour

            if hours <= h:
                r=mid
            else:
                l=mid+1

        return  l

        