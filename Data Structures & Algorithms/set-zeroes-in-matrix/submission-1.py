class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        cols, rows = len(matrix[0]), len(matrix)

        zero_rows, zero_colums = set(), set()

        for r in range(rows):
            for c in range(cols):
                if matrix[r][c] == 0:
                    zero_rows.add(r)
                    zero_colums.add(c)

        # print(zero_rows)
        # print(zero_colums)

        for r in range(rows):
            for c in range(cols):
                if r in zero_rows or c in zero_colums:
                    matrix[r][c] = 0
        
        