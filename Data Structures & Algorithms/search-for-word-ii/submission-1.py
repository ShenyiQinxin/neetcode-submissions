class TrieNode:
    def __init__(self) -> None:
        self.children = {}
        # self.endOfWord = False
        self.word = None
    
    def insert_word(self, word):
        node = self
        for c in word:
            if c not in node.children:
                node.children[c] = TrieNode()
            node = node.children[c]
        # self.endOfWord = True
        node.word = word

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        rows, cols = len(board), len(board[0])
        res, visited = set(), set()
        root = TrieNode()
        for w in words:
            root.insert_word(w)

        def dfs(r, c, node):
            if (r<0 or r>=rows or c <0 or c>=cols or 
            board[r][c] not in node.children or (r,c) in visited):
                return 
            
            visited.add((r,c))
            node = node.children[board[r][c]]
            if node.word:
                res.add(node.word)
                node.word = None

            dfs(r-1, c, node)
            dfs(r+1, c, node)
            dfs(r, c-1, node)
            dfs(r, c+1, node)

            visited.remove((r,c))

        for r in range(rows):
            for c in range(cols):
                dfs(r, c, root)

        return list(res)
        