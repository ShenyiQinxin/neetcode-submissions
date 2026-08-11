# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        res = []
        def dfs(root):
            if not root:
                res.append('#')
                return 
            res.append(str(root.val))
            dfs(root.left)
            dfs(root.right)
        dfs(root)
        return ','.join(res)


    # 12##34##5##
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        
        if data == '#':
            return None

        data_array = data.split(',')
        i = 0
        def dfs():
            nonlocal i
            token = data_array[i]
            i += 1
            if token == '#':
                return None
            node = TreeNode(int(token))
            node.left = dfs()
            node.right = dfs()
            return node
        return dfs()
            

        


