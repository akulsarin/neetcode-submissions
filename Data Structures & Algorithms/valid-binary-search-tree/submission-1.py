# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def valid(node, left_boundary, right_boundary):
            if not node:
                return True
            
            if not (left_boundary < node.val < right_boundary):
                return False
            
            validLeft = valid(node.left, left_boundary, node.val)
            validRight = valid(node.right, node.val, right_boundary)
            return validLeft and validRight
        
        return valid(root, float("-inf"), float("inf"))