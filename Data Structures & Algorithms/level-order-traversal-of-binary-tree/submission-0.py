# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        queue = deque()
        result = []

        if root:
            queue.append(root)
        else:
            return result

        level = 0
        while queue:
            level_vals = []
            for i in range(len(queue)):
                level_node = queue.popleft()
                level_vals.append(level_node.val)
                if level_node.left:
                    queue.append(level_node.left)
                if level_node.right:
                    queue.append(level_node.right)
            result.append(level_vals)

        return result
