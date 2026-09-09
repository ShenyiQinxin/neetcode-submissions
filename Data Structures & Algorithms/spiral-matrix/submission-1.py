class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        m = len(matrix)
        n = len(matrix[0])
        res = []
        l, r = 0, n-1
        top, bottom = 0, m-1
        while l <= r and top <= bottom:

            #top
            for i in range(l, r+1):
                res.append(matrix[top][i])
            top +=1

            # right
            for i in range(top, bottom+1):
                res.append(matrix[i][r])
            r-=1

            if not (l<=r and top<=bottom):
                break

            # bottom
            for i in range(r, l-1, -1):
                res.append(matrix[bottom][i])
            bottom-=1

            # left
            for i in range(bottom, top-1, -1):
                res.append(matrix[i][l])
            l+=1
        return res

            
                






        