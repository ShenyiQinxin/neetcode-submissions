class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x:x[0])
        # print(intervals)
        res = []
        prev_start = intervals[0][0]
        prev_end = intervals[0][1]
        for i in range(1, len(intervals)):
            curr_start = intervals[i][0]
            curr_end = intervals[i][1]

            if curr_start <= prev_end:
                prev_end = max(prev_end, curr_end)
           
            else:
                res.append([prev_start, prev_end])
                prev_start = curr_start
                prev_end = curr_end
        res.append([prev_start, prev_end])
        return res


        
        