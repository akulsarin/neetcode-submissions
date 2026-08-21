# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def upsideDownBinaryTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        newRoot = None

        def dfs(node: Optional[TreeNode], par: Optional[TreeNode], right: Optional[TreeNode]):
            nonlocal newRoot

            if not node:
                return

            if not node.left:
                newRoot = node

            dfs(node.left, node, node.right)
            node.right = par
            node.left = right

        dfs(root, None, None)
        return newRoot