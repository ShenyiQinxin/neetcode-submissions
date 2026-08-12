class TrieNode:
    def __init__(self) -> None:
        self.children = {}
        self.endOfWord = False


class WordDictionary:

    def __init__(self):
        self.root = TrieNode()
        

    def addWord(self, word: str) -> None:
        currnode = self.root
        for c in word:
            if c not in currnode.children:
                currnode.children[c] = TrieNode()
            currnode = currnode.children[c]
        currnode.endOfWord = True

        

    def search(self, word: str) -> bool:
        def dfs(j, root):
            currnode = root

            for i in range(j, len(word)):
                if word[i] == '.':
                    for child in currnode.children.values():
                        if dfs(i+1, child):
                            return True
                    return False
                else:
                    if word[i] not in currnode.children:
                        return False
                    currnode = currnode.children[word[i]]
            return currnode.endOfWord
        return dfs(0, self.root)
        
