class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adj_list = [[] for _ in range(n)]
        for e in edges:
            adj_list[e[0]].append(e[1])
            adj_list[e[1]].append(e[0])
     
        visited = set()
        res = 0

        def dfs(node):
            visited.add(node)
            for nei in adj_list[node]:
                if nei not in visited:
                    dfs(nei)
          

        
        for node in range(n):
            if node not in visited:
                dfs(node)
                res += 1

        return res


        
        