class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        minheap = []
        freq_map = Counter(nums)

        for n, count in freq_map.items():
            heapq.heappush(minheap, (count, n))
            if len(minheap) > k:
                heapq.heappop(minheap)

        return [n for count, n in minheap]


        