# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        def dfs(node: Optional[TreeNode]) -> tuple[int, int]:
            if not node:
                return [0, 0]

            leftPair = dfs(node.left)
            rightPair = dfs(node.right)

            maxWithNode = node.val + leftPair[1] + rightPair[1]
            maxWithoutNode = max(leftPair) + max(rightPair)

            return [maxWithNode, maxWithoutNode]

        return max(dfs(root))