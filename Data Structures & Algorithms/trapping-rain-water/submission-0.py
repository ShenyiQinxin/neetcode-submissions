class Solution:
    def trap(self, height: List[int]) -> int:
        l, r = 0, len(height)-1
        l_max, r_max = height[0], height[len(height)-1]
        total = 0

        while l < r:
            l_max = max(l_max, height[l])
            r_max = max(r_max, height[r])
            if height[l] <= height[r]:
                l_max = max(l_max, height[l])
                l_height_diff = l_max-height[l]
                total += l_height_diff
                l+=1
            elif height[l] > height[r]:
                r_max = max(r_max, height[r])
                r_height_diff = r_max-height[r]
                total +=  r_height_diff
                r-=1
        return total




        
        