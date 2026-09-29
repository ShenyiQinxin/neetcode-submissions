class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        heap = []
        map1 = Counter(nums)

        for n, c in map1.items():
            heapq.heappush(heap, (c, n))
            if len(heap) > k:
                heapq.heappop(heap)

        return [n for c, n in heap]
            