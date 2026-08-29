# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        max_diameter = 0

        def dfs(node: Optional[TreeNode]) -> Tuple[int, int]:
            nonlocal max_diameter

            if not node:
                return 0, 0
            
            left_max = max(dfs(node.left)) + 1
            right_max = max(dfs(node.right)) + 1
            max_diameter = max(max_diameter, left_max + right_max - 1)
            return left_max, right_max

        dfs(root)
        return max_diameter - 1