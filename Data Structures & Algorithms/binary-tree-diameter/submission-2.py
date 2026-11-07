# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        max_diameter = 0

        def max_height(root):
            nonlocal max_diameter
            if not root:
                return 0

            max_left, max_right = 0, 0

            max_left = max_height(root.left)
            max_right = max_height(root.right)

            max_diameter = max(max_diameter, max_left+max_right)


            return max(max_left, max_right) + 1

        max_height(root)
        return max_diameter
        