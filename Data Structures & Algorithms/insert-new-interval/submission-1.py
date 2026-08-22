class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        res = []
        new_s, new_e = newInterval
        inserted = False
        for start, end in intervals:
            # if overlap then merge, else insert
            if inserted:
                res.append([start, end])
            elif end < new_s:
                res.append([start, end])
               
            elif new_e < start:
                res.append([new_s, new_e])
                inserted = True
                res.append([start, end])
                
            else:
                new_s = min(start, new_s)
                new_e = max(end, new_e) 
            
        if not inserted:
            res.append([new_s, new_e]) 
        return res


        
                
               


            

