class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        map1 = {}

        for i, v in enumerate(nums):
            if target-v in map1:
                return [map1[target-v], i]
            map1[v] = i
        
        