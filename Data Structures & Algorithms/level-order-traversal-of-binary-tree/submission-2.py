# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        order = []
        if not root:
            return order

        queue = deque([root])
        while queue:
            level_nodes = []
            for _ in range(len(queue)):
                curr = queue.popleft()
                level_nodes.append(curr.val)
                if curr.left:
                    queue.append(curr.left)
                if curr.right:
                    queue.append(curr.right)
            order.append(level_nodes)
        
        return order