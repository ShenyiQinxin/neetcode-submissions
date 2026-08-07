class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        # [-4,-1,-1,0,1,2]
        res = []
        for i in range(len(nums)):
            # skip dup
            if nums[i] == nums[i-1] and i > 0:
                continue
            l = i+1
            r = len(nums)-1
            while l < r:
                if nums[l] + nums[r] + nums[i] == 0:
                    res.append([nums[l], nums[r], nums[i]])
                    # skip dup
                    while l < r and nums[l] == nums[l+1]:
                        l+=1
                    while l < r and nums[r] == nums[r-1]:
                        r-=1
                    l += 1
                    r -= 1
                elif nums[l] + nums[r] + nums[i] < 0:
                    l +=1
                else:
                    r-=1
        return res

        
        