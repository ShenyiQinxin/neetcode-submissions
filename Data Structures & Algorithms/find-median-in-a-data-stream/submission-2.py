class MedianFinder:

    def __init__(self):
        self.left_max = []
        self.right_min = []
        

    def addNum(self, num: int) -> None:
        if not self.left_max:
            heapq.heappush(self.left_max, -num)
        elif len(self.left_max) and num < -self.left_max[0]:
            heapq.heappush(self.left_max, -num)
            if len(self.left_max) > len(self.right_min) + 1:
                heapq.heappush(self.right_min, -heapq.heappop(self.left_max))
        else:
            heapq.heappush(self.right_min, num)
            if len(self.left_max) < len(self.right_min):
                heapq.heappush(self.left_max, -heapq.heappop(self.right_min))

        

    def findMedian(self) -> float:
        if len(self.left_max) == len(self.right_min):
            return (-self.left_max[0] + self.right_min[0]) / 2
        elif len(self.left_max) > len(self.right_min):
            return -self.left_max[0] 

        
        