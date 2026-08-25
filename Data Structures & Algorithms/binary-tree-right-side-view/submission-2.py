# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        if not root:
            return res
        
        queue = deque([root])
        while queue:
            lastNode = None
            for _ in range(len(queue)):
                lastNode = queue.popleft()
                if lastNode.left:
                    queue.append(lastNode.left)
                if lastNode.right:
                    queue.append(lastNode.right)
            if lastNode:
                res.append(lastNode.val)
        
        return res