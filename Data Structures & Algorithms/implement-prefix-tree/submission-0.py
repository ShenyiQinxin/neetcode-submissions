class TrieNode:
    # a TrieNode holds possible continuation of the prefix 
    # a trie is a tree where each node is a map from character to child node, and endofword flag; 
    def __init__(self) -> None:
        self.children  = {}
        self.endOfWord = False

#"search"
class PrefixTree:
    
    def __init__(self):
        self.root = TrieNode()
        

    def insert(self, word: str) -> None:
        currnode = self.root
        for c in word:
            # if c is not a matching child
            if c not in currnode.children:
                # insert a new <c: TrieNode> as a new child
                currnode.children[c] = TrieNode()
            # start from curr node, advance the curr pointer to the matching child
            currnode = currnode.children[c]
        currnode.endOfWord = True



    def search(self, word: str) -> bool:
        currnode = self.root
        for c in word:
            if c not in currnode.children:
                return False
            currnode = currnode.children[c]

        return currnode.endOfWord
        

    def startsWith(self, prefix: str) -> bool:
        currnode = self.root
        for c in prefix:
            if c not in currnode.children:
                return False
            currnode = currnode.children[c]
        return True
        
        