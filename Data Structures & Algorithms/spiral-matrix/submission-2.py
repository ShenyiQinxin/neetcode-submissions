class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        rows, cols = len(matrix), len(matrix[0])
        res = []
        l, right = 0, cols-1
        top, bottom = 0, rows-1

        
        while l <= right and top <= bottom:
            # top
            for c in range(l, right+1):
                res.append(matrix[top][c])
            top+=1
            # right
            for row in range(top, bottom+1):
                res.append(matrix[row][right])
            right-=1
            if not (l <= right and top <= bottom):
                break
            # bottom
            for c in range(right, l-1, -1):
                res.append(matrix[bottom][c])
            bottom-=1
            # left
            for row in range(bottom, top-1, -1):
                res.append(matrix[row][l])
            l+=1
        return res