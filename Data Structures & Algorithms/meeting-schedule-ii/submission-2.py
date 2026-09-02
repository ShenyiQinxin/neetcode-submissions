"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""
#  if every meeting must happen, sort by start. If you're picking which ones to keep, sort by end.
class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        intervals.sort(key=lambda x:x.start)

        minheap = []
        
        for curr in intervals:
            if minheap and minheap[0] <= curr.start:
                heapq.heappop(minheap)
            heapq.heappush(minheap, curr.end)
        return len(minheap)
        
                
            


        
        