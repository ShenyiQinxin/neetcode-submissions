class TrieNode:
    def __init__(self) -> None:
        self.children = {}
        self.endOfWord = False

class WordDictionary:

    def __init__(self):
        self.root = TrieNode()
        

    def addWord(self, word: str) -> None:
        node = self.root
        for c in word:
            if c not in node.children:
                node.children[c] = TrieNode()
            node = node.children[c]
        node.endOfWord = True

    def search(self, word: str) -> bool:
        
        def dfs(start, node):
            for i in range(start, len(word)):
                if word[i] == '.':
                    for child in node.children.values():
                        if dfs(i+1, child):
                            return True
                    return False
                else:
                    if word[i] not in node.children:
                        return False
                    node = node.children[word[i]]
            return node.endOfWord

        return dfs(0, self.root)
        

        
