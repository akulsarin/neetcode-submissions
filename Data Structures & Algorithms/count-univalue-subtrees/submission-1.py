# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def countUnivalSubtrees(self, root: Optional[TreeNode]) -> int:
        count = 0

        def dfs(node: Optional[TreeNode]) -> bool:
            nonlocal count

            if not node:
                return True
            
            lUnival = dfs(node.left)
            rUnival = dfs(node.right)

            if not lUnival or not rUnival:
                return False

            if node.left and node.left.val != node.val:
                return False
            
            if node.right and node.val != node.right.val:
                return False

            count += 1
            return True

        dfs(root)
        return count