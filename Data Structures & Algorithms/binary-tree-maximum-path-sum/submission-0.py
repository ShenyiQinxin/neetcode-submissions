# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:

        max_sum = float('-inf')

        def dfs(root):
            nonlocal max_sum
            if not root:
                return 0
            left_sum = max(0, dfs(root.left))
            right_sum = max(0, dfs(root.right))
            path_sum = root.val + left_sum + right_sum
            max_sum = max(max_sum, path_sum)
            return root.val + max(left_sum, right_sum)
        
        dfs(root)

        return max_sum
