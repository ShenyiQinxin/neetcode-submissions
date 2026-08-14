class TrieNode:

    def __init__(self) -> None:
        self.children = {}
        self.endOfWord = False
        self.word = None

    def insertWord(self, word):
        node = self
        for c in word:
            if c not in node.children:
                node.children[c] = TrieNode()
          
            node = node.children[c]
        node.endOfWord = True
        node.word = word




class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        ROWS = len(board)
        COLS = len(board[0])
        visited = set()
        res = set()
        root = TrieNode()
        for w in words:
            root.insertWord(w)

        def dfs(r, c, node):
            
            if (r < 0 or r ==ROWS or c < 0 or c == COLS or 
            board[r][c] not in node.children or (r,c) in visited):
                return


            visited.add((r,c))
            node = node.children[board[r][c]]  
            if node.endOfWord:
                res.add(node.word)

            dfs(r+1, c, node)
            dfs(r-1, c, node)
            dfs(r, c+1, node)
            dfs(r, c-1, node)

            visited.remove((r,c))


        for r in range(ROWS):
            for c in range(COLS):
                dfs(r, c, root)
            

        return list(res)





        
        