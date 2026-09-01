class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        graph = defaultdict(list)
        letters = set()
        for w in words:
            letters.update(w)
        for i in range(len(words)-1):
            w1, w2 = words[i], words[i+1]
            for j in range(min(len(w1), len(w2))):
                if w1[j] != w2[j]:
                    graph[w2[j]].append(w1[j]) # succ : preq
                    break
            else: 
                if len(w1) > len(w2):
                    return ''
        
        curr_path, visited = set(), set() 
        res = []
        def dfs(letter): # check if has cycle and cannot finish
            if letter in curr_path:
                return False
            if letter in visited:
                return True

            curr_path.add(letter)
            for nei in graph[letter]:
                if not dfs(nei):
                    return False
            visited.add(letter)
            curr_path.remove(letter)
            res.append(letter)
            return True

        
        for letter in letters:
            if not dfs(letter):
                return ''
        return ''.join(res)

            
