class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        rows, cols = len(matrix), len(matrix[0])
        rowZero = False

        for r in range(rows):
            for c in range(cols):
                if matrix[r][c] == 0:
                    # 0th row 
                    matrix[0][c] = 0
                    # 0th column
                    if r > 0:
                        matrix[r][0] = 0
                    else: # r ==0
                        rowZero = True

        for r in range(1, rows):
            for c in range(1, cols):
                if matrix[0][c] == 0 or matrix[r][0] == 0:
                    matrix[r][c] = 0

        # 0th column
        if matrix[0][0] == 0:
            for r in range(rows):
                matrix[r][0] = 0

        # 0th row
        if rowZero:
            for c in range(cols):
                matrix[0][c] = 0






        