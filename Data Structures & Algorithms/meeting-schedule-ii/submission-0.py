"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:

    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        if not intervals:
            return 0

        intervals.sort(key=lambda x:x.start)
        minheap = [intervals[0].end]
        
        for inter in intervals[1:]:
            if inter.start < minheap[0]:
                heapq.heappush(minheap, inter.end)
            else:
                heapq.heappop(minheap)
                heapq.heappush(minheap, inter.end)
            
        return len(minheap)



        