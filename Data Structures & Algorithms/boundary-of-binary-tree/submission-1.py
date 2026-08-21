# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def boundaryOfBinaryTree(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        
        ans = [root.val]
        
        def getBoundary(node: Optional[TreeNode], isLeft: bool):
            nonlocal ans
            if not node:
                return
            if not node.left and not node.right:
                return
            
            if isLeft:
                ans.append(node.val)
                if node.left:
                    getBoundary(node.left, isLeft)
                else:
                    getBoundary(node.right, isLeft)
            else:
                if node.right:
                    getBoundary(node.right, isLeft)
                else:
                    getBoundary(node.left, isLeft)
                ans.append(node.val)

        def getLeaves(node: Optional[TreeNode]):
            nonlocal ans, root
            if not node:
                return

            if not node.left and not node.right and node != root:
                ans.append(node.val)
                return
            getLeaves(node.left)
            getLeaves(node.right)

        getBoundary(root.left, True)
        getLeaves(root)
        getBoundary(root.right, False)
        return ans