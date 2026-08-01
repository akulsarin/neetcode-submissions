# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if not preorder or not inorder:
            return None

        root = TreeNode(preorder[0])
        
        cutIdx = inorder.index(preorder[0])
        root.left = self.buildTree(preorder[1:cutIdx + 1], inorder[:cutIdx])
        root.right = self.buildTree(preorder[cutIdx + 1:], inorder[cutIdx + 1:])

        return root
        