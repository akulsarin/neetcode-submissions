# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def closestKValues(self, root: Optional[TreeNode], target: float, k: int) -> List[int]:
        dq = deque([])

        def inorder(node: Optional[TreeNode]):
            if not node:
                return
            
            inorder(node.left)
            if len(dq) < k:
                dq.append(node.val)
            else:
                d1 = abs(target - node.val)
                d2 = abs(target - dq[0])
                if d1 < d2:
                    dq.popleft()
                    dq.append(node.val)
            inorder(node.right)

        inorder(root)
        return list(dq)