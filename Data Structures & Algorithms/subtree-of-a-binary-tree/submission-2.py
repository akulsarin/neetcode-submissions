# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def rooted_here(root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
            if not root:
                return not subRoot
            elif not subRoot:
                return False

            return (
                root.val == subRoot.val 
                and rooted_here(root.left, subRoot.left) 
                and rooted_here(root.right, subRoot.right)
            )
        
        if not root:
            return not subRoot
        
        if rooted_here(root, subRoot):
            return True
        
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)