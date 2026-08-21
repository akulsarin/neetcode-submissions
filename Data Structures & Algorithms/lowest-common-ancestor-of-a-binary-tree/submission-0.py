# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        pPath = []
        qPath = []

        def findPath(node: Optional['TreeNode'], target: int, res: List[int]) -> bool:
            if not node:
                return

            res.append(node)

            if node == target:
                return True
            if findPath(node.left, target, res):
                return True
            if findPath(node.right, target, res):
                return True
            
            res.pop()
            return False

        findPath(root, p, pPath)
        findPath(root, q, qPath)

        print("P: ", pPath)
        print("Q: ", qPath)

        res = root
        for i, pathTuple in enumerate(zip(pPath, qPath)):
            if pathTuple[0] != pathTuple[1]:
                break
            res = pathTuple[0]
        
        return res