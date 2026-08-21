# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def upsideDownBinaryTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        par, right = None, None
        while root:
            nextRoot, nextRight = root.left, root.right
            root.right = par
            root.left = right
            par, right = root, nextRight
            root = nextRoot
        return par
            
        