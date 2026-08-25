# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def preorder_dfs(node: Optional[TreeNode], path_max: int) -> int:
            if not node:
                return 0
            
            count = 0
            if node.val >= path_max:
                count += 1
                path_max = node.val
            
            count += preorder_dfs(node.left, path_max)
            count += preorder_dfs(node.right, path_max)
            return count
        
        return preorder_dfs(root, float('-inf'))