# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def dfs(node: Optional[TreeNode]) -> Tuple[int, int, bool]:
            if not node:
                return float('inf'), float('-inf'), True

            left_min, left_max, left_is_bst = dfs(node.left)
            if not left_is_bst:
                return 0, 0, False
            right_min, right_max, right_is_bst = dfs(node.right)
            if not right_is_bst:
                return 0, 0, False

            curr_is_bst = left_max < node.val < right_min
            return min(left_min, node.val), max(right_max, node.val), curr_is_bst

        return dfs(root)[-1]