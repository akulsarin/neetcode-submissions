# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def longestConsecutive(self, root: Optional[TreeNode]) -> int:
        maxPath = 1

        def dfs(node: Optional[TreeNode], parentVal: int, currPath: int):
            nonlocal maxPath
            
            if not node:
                return

            if node.val == parentVal + 1:
                currPath += 1
                maxPath = max(maxPath, currPath)
            else:
                currPath = 1
            
            dfs(node.left, node.val, currPath)
            dfs(node.right, node.val, currPath)

        dfs(root, root.val, 1)
        return maxPath