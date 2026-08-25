# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def dfs(node: Optional[TreeNode]) -> Tuple[int, bool]:
            if not node:
                return 0, True
            
            left_height, left_is_balanced = dfs(node.left)
            right_height, right_is_balanced = dfs(node.right)

            curr_height = max(left_height, right_height) + 1
            curr_is_balanced = left_is_balanced and right_is_balanced and abs(left_height - right_height) <= 1

            return curr_height, curr_is_balanced
        
        return dfs(root)[1]        