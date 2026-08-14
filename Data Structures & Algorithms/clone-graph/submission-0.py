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

        mapping = {}

        def dfs(node):
            if node in mapping:
                return mapping[node]

            copy = Node(node.val)
            mapping[node] = copy
            for nei in node.neighbors:
                copy_nei = dfs(nei)
                copy.neighbors.append(copy_nei)
            return copy


        return dfs(node)
        