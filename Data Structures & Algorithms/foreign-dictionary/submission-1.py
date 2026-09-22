class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        res = []
        letters, graph = set(), defaultdict(list)
        for w in words:
            letters.update(w)

        for i in range(len(words)-1):
            for j in range(min(len(words[i]), len(words[i+1]))):
                if words[i][j] != words[i+1][j]:
                    graph[words[i+1][j]].append(words[i][j])
                    break
            else:
                if len(words[i]) > len(words[i+1]):
                    return ''
        
        can_finish, path = set(), set()
        def dfs(letter):
            if letter in can_finish:
                return True
            if letter in path:
                return False

            path.add(letter)
            for nei in graph[letter]:
                if not dfs(nei):
                    return False
            path.remove(letter)

            res.append(letter)
            can_finish.add(letter)
            return True

        for l in letters:
            if not dfs(l):
                return ''
        
            
        return ''.join(res)
            

        