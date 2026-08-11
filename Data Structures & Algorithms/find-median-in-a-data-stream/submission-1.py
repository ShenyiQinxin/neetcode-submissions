class MedianFinder:

    def __init__(self):
        self.lm = []
        self.rs = []
        

    def addNum(self, num: int) -> None:
        if self.lm and num <= -self.lm[0]:
            heapq.heappush(self.lm, -num)
            if len(self.lm) > len(self.rs) + 1:
                heapq.heappush(self.rs, -heapq.heappop(self.lm))
        else:
            heapq.heappush(self.rs, num) 
            if len(self.rs) > len(self.lm):   
                heapq.heappush(self.lm, -heapq.heappop(self.rs))
        
# 522817
# 1225 789
# 1225 789 <= 0
# 01225 789
    def findMedian(self) -> float:
        if len(self.lm) > len(self.rs):
            return -self.lm[0]
        elif len(self.lm) == len(self.rs):
            return (-self.lm[0]+self.rs[0])/2


        
        