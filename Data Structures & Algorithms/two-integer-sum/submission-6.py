class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        k_v = defaultdict(int)

        for i in range(len(nums)):
            if target - nums[i] in k_v:
                return [k_v[target-nums[i]], i]
            k_v[nums[i]] = i
        



        