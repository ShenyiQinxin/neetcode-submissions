class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        graph = defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        visited, count = set(), 0

        def dfs(i):
            visited.add(i)

            for nei in graph[i]:
                if nei not in visited:
                    dfs(nei)

        for i in range(n):
            if i not in visited:
                dfs(i)
                count+=1
        return count
        