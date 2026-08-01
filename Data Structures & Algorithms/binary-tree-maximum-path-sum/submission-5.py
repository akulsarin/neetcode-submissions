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
            maxLeft = node.val + max(0, maxSingleSideLeft)
            maxRight = node.val + max(0, maxSingleSideRight)

            maxSeen = max(maxSeen, maxBothSides, maxLeft, maxRight)

            return max(maxLeft, maxRight)

        postorderTraverse(root)
        return maxSeen
        