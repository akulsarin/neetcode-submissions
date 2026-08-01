# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        count = 0
        result = root.val

        def inorderTraverse(node: Optional[TreeNode]) -> int:
            nonlocal count, result
            
            if not node:
                return

            if count < k:
                inorderTraverse(node.left)

            if count < k:
                count += 1
                result = node.val

            if count < k:
                inorderTraverse(node.right)

        inorderTraverse(root)
        return result



        