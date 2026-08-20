# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def longestConsecutive(self, root: Optional[TreeNode]) -> int:
        longest = 1

        def dfs(node: Optional[TreeNode]) -> tuple[int, int]:
            nonlocal longest

            if not node:
                return (0, 0)

            inc = dcr = 1

            lInc, lDcr = dfs(node.left)
            if node.left:
                if node.val + 1 == node.left.val:
                    inc = lInc + 1
                elif node.val - 1 == node.left.val:
                    dcr = lDcr + 1

            rInc, rDcr = dfs(node.right)
            if node.right:
                if node.val + 1 == node.right.val:
                    inc = max(inc, rInc + 1)
                elif node.val - 1 == node.right.val:
                    dcr = max(dcr, rDcr + 1)

            longest = max(longest, inc, dcr)
            if node.left and node.right:
                if node.val == node.left.val + 1 and node.val == node.right.val - 1:
                    longest = max(longest, lDcr + 1 + rInc)
                elif node.val == node.left.val - 1 and node.val == node.right.val + 1:
                    longest = max(longest, lInc + 1 + rDcr)

            return (inc, dcr) 

        dfs(root)
        return longest