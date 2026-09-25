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

        # Good question, and there's a clean rule.

# Sort by start when you're *combining* or *placing* things — merging overlaps, inserting, counting how many run concurrently. You need to see intervals in the order they begin.

# Sort by end when you're *selecting* a maximum subset — keep as many non-overlapping as possible, minimum removals, activity scheduling. Ending earliest leaves the most room, so it's the greedy choice.

# Merge, insert, meeting rooms: start. Non-overlapping: end.