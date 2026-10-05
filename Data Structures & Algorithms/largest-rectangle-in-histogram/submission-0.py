class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = [] # index
        max_area = 0 # running max area

        for i in range(len(heights)):
            while stack and heights[i] < heights[stack[-1]]:
                top = stack.pop()
                height = heights[top]
                width = i - stack[-1] - 1 if stack else i
                max_area = max(max_area, height*width)
            
            stack.append(i)

        while stack:
            top = stack.pop()
            height = heights[top]
            width = len(heights)-stack[-1]-1 if stack else len(heights)
            max_area = max(max_area, height*width)

        return max_area













        