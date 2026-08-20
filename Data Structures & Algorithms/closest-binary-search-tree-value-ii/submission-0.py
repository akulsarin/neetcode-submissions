# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def closestKValues(self, root: Optional[TreeNode], target: float, k: int) -> List[int]:
        maxHeap = []

        def dfs(node: Optional[TreeNode]):
            nonlocal maxHeap

            if not node:
                return

            dist = -abs(target - node.val)
            heapq.heappush(maxHeap, (dist, node.val))
            while len(maxHeap) > k:
                heapq.heappop(maxHeap)
            dfs(node.left)
            dfs(node.right)
        
        dfs(root)
        return [item[1] for item in maxHeap]