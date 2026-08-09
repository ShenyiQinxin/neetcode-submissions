# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:  
    def search_root(self, root, subRoot):
        if not root:
            return False
        if root.val == subRoot.val:
            return True
        return False

    def is_same_tree(self, root, subRoot):
        if not root and not subRoot:
            return True
        if not root or not subRoot:
            return False
        if root.val != subRoot.val:
            return False
        
        return (self.is_same_tree(root.left, subRoot.left) and
        self.is_same_tree(root.right, subRoot.right))
 
   

    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        # search subRoot in root
        
        if not root:
            return False
        if self.search_root(root, subRoot):
            if self.is_same_tree(root, subRoot):
                return True
       
        return (self.isSubtree(root.left, subRoot) or
            self.isSubtree(root.right, subRoot))

            