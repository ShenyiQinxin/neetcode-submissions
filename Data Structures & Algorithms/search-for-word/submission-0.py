class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        #m*n*(4^l)
        def dfs(r, c, idx):
            if idx == len(word):
                return True
            if r < 0 or r >= len(board) or c < 0 or c >= len(board[0]):
                return False
            if board[r][c] != word[idx]:
                return False
            tmp = board[r][c]
            board[r][c] = '#'

            res = (dfs(r, c-1, idx+1) or
            dfs(r, c+1, idx+1) or
            dfs(r+1, c, idx+1) or
            dfs(r-1, c, idx+1))

            board[r][c] = tmp
            return res
                
            
        for r in range(len(board)):
            for c in range(len(board[0])):
                if dfs(r, c, 0):
                    return True

        return False

        