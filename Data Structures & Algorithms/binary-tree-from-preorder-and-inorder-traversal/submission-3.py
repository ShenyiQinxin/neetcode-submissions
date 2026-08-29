# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        inorder_val_idx = {val: i for i, val in enumerate(inorder)}
        preorder_idx = 0

        def dfs(left, right): # based on preorder
            nonlocal preorder_idx
            if left > right:
                return None

            root_val = preorder[preorder_idx]
            root_idx = inorder_val_idx[root_val]
            preorder_idx += 1
            
            root = TreeNode(root_val)
            root.left = dfs(left, root_idx-1)
            root.right = dfs(root_idx+1, right)

            

            return root

        return dfs(0, len(preorder)-1)
            
            
        