class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        i_v = dict()

        for i, n in enumerate(nums):
            if target - n in i_v.keys():
                return [i_v[target-n], i]
            i_v[n] = i
        return [-1, -1]
