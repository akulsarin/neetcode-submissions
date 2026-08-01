# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        count = 0
        
        def dfs(node: TreeNode, path: set, maxInPath: int) -> None:
            nonlocal count

            if node in path:
                return

            path.add(node)
            oldMax = maxInPath
            if node.val >= maxInPath:
                count += 1
                maxInPath = node.val
            if node.left:
                dfs(node.left, path, maxInPath)
            if node.right:
                dfs(node.right, path, maxInPath)
            maxInPath = oldMax
            path.remove(node)

        dfs(root, set(), float('-inf'))
        return count