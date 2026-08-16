class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        adj_list = [[] for _ in range(n)]
        visited = set()

        for e in edges:
            adj_list[e[0]].append(e[1])
            adj_list[e[1]].append(e[0])


        def dfs(node, parent):
            visited.add(node)
           

            for child in adj_list[node]:
                if child == parent:
                    continue
                if child in visited:
                    return False   
                if not dfs(child, node):
                    return False
                    

            return True


        
        return dfs(0, -1) and len(visited) == n

        