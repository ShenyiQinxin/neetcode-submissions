class Solution:
    def trap(self, height: List[int]) -> int:
        l, r = 0, len(height)-1
        area = 0
        l_max_height, r_max_height =height[l], height[r]

        while l < r:
            
            
            if height[l] <= height[r]:
                l_max_height = max(l_max_height, height[l])
                area += l_max_height-height[l]
                l+=1
            else:
                r_max_height = max(r_max_height, height[r])
                area += r_max_height-height[r]
                r-=1


        return area
        