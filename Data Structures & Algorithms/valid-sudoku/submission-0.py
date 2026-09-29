class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows, cols = len(board), len(board[0])
        boxset, rowset, colset = defaultdict(set), defaultdict(set), defaultdict(set)

        for r in range(rows):
            for c in range(cols):
                if board[r][c] == '.':
                    continue
                i, j = r//3, c//3
                if board[r][c] in boxset[(i,j)]:
                    return False
                boxset[(i,j)].add(board[r][c])
                if board[r][c] in rowset[r]:
                    return False
                rowset[r].add(board[r][c])
                if board[r][c] in colset[c]:
                    return False
                colset[c].add(board[r][c])
        return True
        