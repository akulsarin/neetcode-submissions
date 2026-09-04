class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        def dfs(node: Optional[TreeNode]) -> tuple[int, int]:
            if not node:
                return (0, 0)  # (rob, not_rob)

            left_rob, left_not_rob = dfs(node.left)
            right_rob, right_not_rob = dfs(node.right)

            # Option 1: Rob this node -> children cannot be robbed
            rob_val = node.val + left_not_rob + right_not_rob

            # Option 2: Skip this node -> children can be robbed or skipped
            not_rob_val = max(left_rob, left_not_rob) + max(right_rob, right_not_rob)

            return (rob_val, not_rob_val)

        return max(dfs(root))