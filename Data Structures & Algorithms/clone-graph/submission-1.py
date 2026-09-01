"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None

        visited = {} # original node and its copy

        def dfs(node):
            if not node:
                return None
            if node in visited:
                return visited[node]
            copy = Node(node.val)
            visited[node] = copy
            for nei in node.neighbors:
                copy_nei = dfs(nei)
                copy.neighbors.append(copy_nei)
            return copy

        return dfs(node)
        