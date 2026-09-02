class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x:x[1])
        counter = 0
        prev = intervals[0]
        for curr in intervals[1:]:
            if prev[1] > curr[0]: # overlap
                counter += 1
                
            else:
                prev = curr

        return counter