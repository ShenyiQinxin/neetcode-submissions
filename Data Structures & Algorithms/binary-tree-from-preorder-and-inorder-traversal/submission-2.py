# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        index_map = {v : i for i, v in enumerate(inorder)}
        pre_index = 0

        def helper(left, right):
            nonlocal pre_index

            if left > right:
                return None

            root_value = preorder[pre_index]
            pre_index += 1

            root = TreeNode(root_value)
            mid = index_map[root_value]
        
            root.left = helper(left, mid-1)
            root.right = helper(mid+1, right)

            return root


        return helper(0, len(inorder)-1)


        
        