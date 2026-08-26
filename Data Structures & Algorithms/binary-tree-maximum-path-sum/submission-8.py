# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        max_path_sum = float('-inf')

        def path_sum(node: Optional[TreeNode]) -> int:
            nonlocal max_path_sum

            if not node: 
                return 0
            
            left_path_sum = path_sum(node.left)
            right_path_sum = path_sum(node.right)
            combined_path_sum = left_path_sum + right_path_sum + node.val
            curr_path_sum = max(
                node.val,
                left_path_sum + node.val,
                right_path_sum + node.val,
            )

            max_path_sum = max(max_path_sum, curr_path_sum, combined_path_sum)
            return curr_path_sum
        
        path_sum(root)
        return max_path_sum