from _heapq import heapify
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        minheap = []
        freq_map = Counter(nums)

        for num, count in freq_map.items():

            heapq.heappush(minheap, (count, num))
            if len(minheap) > k:
                heapq.heappop(minheap)
        print(minheap)
        return [num for count, num in minheap]
