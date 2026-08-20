# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def verticalOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []

        colToVals = defaultdict(list)
        minCol = maxCol = 0
        queue = deque([(root, 0)])
        
        while queue:
            for _ in range(len(queue)):
                node, idx = queue.popleft()
                minCol = min(minCol, idx)
                maxCol = max(maxCol, idx)
                colToVals[idx].append(node.val)
                if node.left:
                    queue.append((node.left, idx - 1))
                if node.right:
                    queue.append((node.right, idx + 1))
        
        res = []
        for col in range(minCol, maxCol + 1):
            vals = colToVals[col]
            res.append(vals)
        
        return res