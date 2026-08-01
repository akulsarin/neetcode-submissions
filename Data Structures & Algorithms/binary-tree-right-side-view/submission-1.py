# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []

        queue = deque([root])
        rightSideView = []

        while queue:
            rightMostVal = None
            for _ in range(len(queue)):
                node = queue.popleft()
                rightMostVal = node.val
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
                    
            if rightMostVal is not None:
                rightSideView.append(rightMostVal)
        
        return rightSideView
        