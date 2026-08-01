# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        maxSeen = float('-inf')

        def postorderTraverse(node: Optional[TreeNode]) -> int:
            nonlocal maxSeen

            if not node:
                return 0

            maxSingleSideLeft = postorderTraverse(node.left)
            maxSingleSideRight = postorderTraverse(node.right)

            maxBothSides = node.val + maxSingleSideLeft + maxSingleSideRight
            maxLeft = node.val + maxSingleSideLeft
            maxRight = node.val + maxSingleSideRight

            maxSeen = max(maxSeen, maxBothSides, maxLeft, maxRight, node.val)

            return max(maxLeft, maxRight, node.val)

        postorderTraverse(root)
        return maxSeen
        