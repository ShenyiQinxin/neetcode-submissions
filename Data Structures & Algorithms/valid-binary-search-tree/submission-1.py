# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValid(self, root, lower, higher):
        if not root:
            return True
        if root.val <= lower or root.val >= higher:
            return False
        return (self.isValid(root.left, lower, root.val) and
        self.isValid(root.right, root.val, higher))
   

    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        
        return self.isValid(root, float('-inf'), float('inf'))
        