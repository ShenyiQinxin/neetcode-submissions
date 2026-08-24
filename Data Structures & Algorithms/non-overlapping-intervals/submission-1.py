class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x:x[0])
        count = 0
        prev_end = intervals[0][1]

        for i in range(1, len(intervals)):
            curr_start = intervals[i][0]
            curr_end = intervals[i][1]
            if prev_end <= curr_start:
                prev_end = curr_end # no-overlap
            else:
                
                count+=1
                prev_end = min(prev_end, curr_end)

        return count
                




        
        